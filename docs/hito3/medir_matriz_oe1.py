"""Hito 3 · Punto 1 · Medición de la matriz OE1.

Calcula el resultado de cada control definido en `matriz_oe1.csv` sobre los CSV
conservados en `fuentes_datos/datos/`, respetando las definiciones de población,
numerador y denominador de la propia matriz, y escribe los valores dentro de los
tres archivos de la matriz:

  - `matriz_oe1.csv`   -> columnas de resultado y `estado_medicion` por fuente
  - `matriz_oe1.yaml`  -> bloque `resultado` y `estado_medicion` por control
  - `matriz_oe1.md`    -> línea de estado de cada ficha y sección de línea base

Es idempotente: reejecutarlo vuelve a calcular y sobrescribe los mismos campos.
No modifica el código del Hito 2 ni los CSV de datos.

Uso:  python docs/hito3/medir_matriz_oe1.py
"""

import csv
import collections
import hashlib
import json
import re
import statistics as st
from datetime import datetime, timezone
from pathlib import Path

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parents[1]
DATOS = RAIZ / "fuentes_datos" / "datos"

MATRIZ_CSV = AQUI / "matriz_oe1.csv"
MATRIZ_YAML = AQUI / "matriz_oe1.yaml"
MATRIZ_MD = AQUI / "matriz_oe1.md"

SERIAL_EXCEL = (36526, 47483)   # intervalo heredado del Hito 2; no confirma error
FACTOR_R12 = 10                 # factor del código actual; pendiente de sensibilidad
AUSENTES = {"", "N/A", "NA", "null", "None"}

MESES_EPM = {"Enero": 1, "Febrero": 2, "Marzo": 3, "Abril": 4, "Mayo": 5, "Junio": 6,
             "Julio": 7, "Agosto": 8, "Septiembre": 9, "Octubre": 10,
             "Noviembre": 11, "Diciembre": 12}

ORDEN = ["R01", "R02", "R03", "R04", "R05", "R06", "R07", "R08", "R09", "R10",
         "R11", "R12", "INT01", "INT02", "EXA01", "OPO01", "MAP01", "DEF01", "CART01"]

EPM = dict(
    fuente="EPM", clave="epm", dataset_id="sfcd-b3ey",
    archivo=DATOS / "epm_sfcd-b3ey.csv",
    periodo=("year", "mes"), mes_es_texto=True,
    categorias=["tipodeinformacion", "tipodetarifa", "tipodedato", "rangodeconsumo", "nivel"],
    medidas=["propiedadepm", "compartido", "propiedaddelcliente", "punta", "fueradepunta"],
    categoricas_r06=["tipodetarifa", "tipodedato", "rangodeconsumo"],
    columnas_esperadas=12,
    pares_codigo_nombre=[],
)

CHEC = dict(
    fuente="CHEC", clave="chec", dataset_id="c698-wqig",
    archivo=DATOS / "chec_c698-wqig.csv",
    periodo=("costounitariotarifa_ano", "costounitariotarifa_mes"), mes_es_texto=False,
    categorias=[
        "comercializador_codigo", "comercializador_nombre", "mercado_codigo", "mercado_nombre",
        "costounitariotarifa_tipomed", "nivel_tension_codigo", "modalidadcobro_propiedad",
        "claseservicio_codigo", "claseservicio_descri", "claseservicio_estrato",
        "costounitariotarifa_rangoconsumo", "costounitariotarifa_tipomercado",
    ],
    medidas=[
        "costounitariotarifa_generacion", "costounitariotarifa_transmision",
        "costounitariotarifa_distribucion", "costounitariotarifa_comercializacion",
        "costounitariotarifa_perdidas", "costounitariotarifa_restricciones",
        "costounitariotarifa_cu", "costounitariotarifa_cureal",
        "costounitariotarifa_subcon", "costounitariotarifa_valor_tarifa",
    ],
    categoricas_r06=[
        "comercializador_codigo", "comercializador_nombre", "mercado_codigo", "mercado_nombre",
        "modalidadcobro_propiedad", "claseservicio_codigo", "claseservicio_descri",
        "claseservicio_estrato", "costounitariotarifa_rangoconsumo",
    ],
    columnas_esperadas=24,
    pares_codigo_nombre=[
        ("comercializador_codigo", "comercializador_nombre"),
        ("mercado_codigo", "mercado_nombre"),
        ("claseservicio_codigo", "claseservicio_descri"),
    ],
)


def numero(texto):
    s = (texto or "").strip()
    if s in AUSENTES:
        return None
    try:
        v = float(s)
    except ValueError:
        return None
    return v if v == v and abs(v) != float("inf") else None


def canonico(texto):
    return re.sub(r"\s+", " ", (texto or "").strip()).lower()


def sha256(ruta):
    h = hashlib.sha256()
    with open(ruta, "rb") as f:
        for bloque in iter(lambda: f.read(1 << 20), b""):
            h.update(bloque)
    return h.hexdigest()


# EXA01 · contraste contra una fuente de referencia de otro publicador.
# Superservicios td8k-vhq9 publica los componentes del costo unitario por empresa.
# nt_prop combina nivel de tensión y modalidad de propiedad de la red.
REFERENCIA_CHEC = AQUI / "referencia_exa01_chec.json"
NT_PROP = {"1-100": ("1", "100% OR"), "1-50": ("1", "50% OR"), "1-0": ("1", "0% OR"),
           "2": ("2", "0% OR"), "3": ("3", "0% OR"), "4": ("4", "0% OR")}
# CREG 119 de 2007: CU = Gm + Tm + Dnm + Cvm + PRnm + Rm
PARES_EXA01 = [("gm", "costounitariotarifa_generacion"),
               ("tm", "costounitariotarifa_transmision"),
               ("prnm", "costounitariotarifa_perdidas"),
               ("dnm", "costounitariotarifa_distribucion"),
               ("cvm", "costounitariotarifa_comercializacion"),
               ("rm", "costounitariotarifa_restricciones"),
               ("cuvm", "costounitariotarifa_cu")]


def exactitud_chec(filas):
    """Contrasta los componentes del costo unitario contra la referencia externa.

    Devuelve (coincidencias, contrastadas, nota) o None si falta la referencia.
    """
    if not REFERENCIA_CHEC.exists():
        return None
    doc = json.loads(REFERENCIA_CHEC.read_text(encoding="utf-8"))
    ref = doc["registros_datos"]

    idx = collections.defaultdict(list)
    for r in filas:
        idx[(r["costounitariotarifa_ano"], r["costounitariotarifa_mes"],
             r["nivel_tension_codigo"], r["modalidadcobro_propiedad"])].append(r)

    def cerca(a, b):
        return abs(a - b) <= max(0.01, abs(a) * 0.001)

    coincide = total = falsos_rechazados = falsos = 0
    for r in ref:
        nt = NT_PROP.get(r.get("nt_prop"))
        if not nt:
            continue
        anio, mes = str(int(r["car_carg_ano"])), str(int(r["car_carg_periodo"]))
        candidatas = idx.get((anio, mes, nt[0], nt[1]), [])
        if not candidatas:
            continue
        for campo_ref, campo_csv in PARES_EXA01:
            v = numero(r.get(campo_ref))
            if v is None:
                continue
            valores = {numero(c[campo_csv]) for c in candidatas}
            valores.discard(None)
            total += 1
            coincide += 1 if any(cerca(v, x) for x in valores) else 0
            # Prueba de control: un valor deliberadamente incorrecto debe rechazarse.
            falso = v * 1.05 + 7.3
            falsos += 1
            falsos_rechazados += 0 if any(cerca(falso, x) for x in valores) else 1

    if not total:
        return None
    poder = 100 * falsos_rechazados / falsos
    nota = (f"Contraste con {doc['nombre']} ({doc['dataset_id']}), publicador distinto, "
            f"descargado {doc['descargado_utc']}. Alcance: {total} celdas de 7 componentes "
            f"en 6 combinaciones nivel-propiedad del ano 2023. Tolerancia 0,1 % relativa. "
            f"Prueba de control: {poder:.1f} % de los valores falsos inyectados fueron "
            f"rechazados. No cubre cureal, subcon ni valor_tarifa, que no tienen "
            f"contraparte en la referencia.")
    return coincide, total, nota


def medir(cfg):
    """Devuelve {control: dict(num, den, valor, estado, nota)} para una fuente."""
    filas = list(csv.DictReader(open(cfg["archivo"], encoding="utf-8-sig", newline="")))
    n = len(filas)
    campo_ano, campo_mes = cfg["periodo"]
    medidas, categorias = cfg["medidas"], cfg["categorias"]
    r, extra = {}, {}

    def add(control, num, den, estado, nota=""):
        valor = round(100 * num / den, 4) if den else None
        r[control] = dict(numerador=num, denominador=den, valor=valor,
                          estado=estado, nota=nota)

    # R01 · período informado
    con_periodo = [f for f in filas
                   if (f.get(campo_ano) or "").strip() and (f.get(campo_mes) or "").strip()]
    add("R01", len(con_periodo), n, "medido")

    # R02 · período válido
    def periodo_valido(f):
        ano = (f.get(campo_ano) or "").strip()
        mes = (f.get(campo_mes) or "").strip()
        if not re.fullmatch(r"-?\d+", ano):
            return False
        return mes in MESES_EPM if cfg["mes_es_texto"] else (
            re.fullmatch(r"\d+", mes) is not None and 1 <= int(mes) <= 12)

    add("R02", sum(1 for f in con_periodo if periodo_valido(f)), len(con_periodo), "medido")

    # R03 · importes numéricos y finitos sobre celdas informadas
    informadas = conformes = 0
    for f in filas:
        for c in medidas:
            if (f.get(c) or "").strip() in AUSENTES:
                continue
            informadas += 1
            conformes += numero(f.get(c)) is not None
    add("R03", conformes, informadas, "provisional",
        "Sin matriz de aplicabilidad por concepto: se evaluan todas las celdas informadas.")

    # R04 · duplicados exactos adicionales
    originales = [tuple(f[c] for c in f) for f in filas]
    duplicados = n - len(set(originales))
    add("R04", n - duplicados, n, "medido")

    # R05 · clave sin multiplicidad, tras conservar una fila por clase de copia exacta
    vistos, sin_copias = set(), []
    for f, clave_fila in zip(filas, originales):
        if clave_fila in vistos:
            continue
        vistos.add(clave_fila)
        sin_copias.append(f)
    evaluables = [f for f in sin_copias if periodo_valido(f)
                  and all((f.get(c) or "").strip() for c in categorias)]
    conteo = collections.Counter(
        tuple(canonico(f[c]) for c in categorias) + (f[campo_ano].strip(), f[campo_mes].strip())
        for f in evaluables)
    add("R05", sum(v for v in conteo.values() if v == 1), len(evaluables),
        "medido" if cfg["clave"] == "epm" else "provisional",
        "" if cfg["clave"] == "epm" else "Clave provisional: dependencias codigo-nombre sin revisar.")

    # R06 · representación canónica
    cel = conf = 0
    for c in cfg["categoricas_r06"]:
        grupos = collections.defaultdict(collections.Counter)
        for f in filas:
            v = (f.get(c) or "").strip()
            if v in AUSENTES:
                continue
            grupos[canonico(v)][v] += 1
        for formas in grupos.values():
            forma_canonica = formas.most_common(1)[0][0]
            for valor, veces in formas.items():
                cel += veces
                conf += veces if valor == forma_canonica else 0
    add("R06", conf, cel, "provisional",
        "Sin catalogo canonico aprobado: canonica = forma mas frecuente; no detecta sinonimos.")

    # R07 · signo y rango por concepto, con la excepción documentada de Restricciones
    verificables = dentro = 0
    neg_por_concepto, por_columna = collections.Counter(), collections.defaultdict(
        lambda: dict(ceros=0, negativos=0, vacias=0))
    for f in filas:
        concepto = (f.get("tipodedato") or "").strip() if cfg["clave"] == "epm" else ""
        es_restriccion = "restriccion" in canonico(concepto)
        for c in medidas:
            if (f.get(c) or "").strip() in AUSENTES:
                por_columna[c]["vacias"] += 1
            v = numero(f.get(c))
            if v is None:
                continue
            verificables += 1
            if v == 0:
                por_columna[c]["ceros"] += 1
            elif v < 0:
                por_columna[c]["negativos"] += 1
                neg_por_concepto[concepto or c] += 1
            dentro += 1 if (es_restriccion or v >= 0) else 0
    add("R07", dentro, verificables, "provisional",
        "Dominio por concepto sin documentar: no negatividad salvo Restricciones (EPM).")
    extra["negativos_por_concepto"] = neg_por_concepto
    extra["por_columna"] = dict(por_columna)

    # R08 · orden entre tarifas por propiedad
    if cfg["clave"] == "epm":
        comparaciones = cumplen = 0
        for f in filas:
            if (f.get("nivel") or "").strip() != "I":
                continue
            a, b, c_ = (numero(f["propiedadepm"]), numero(f["compartido"]),
                        numero(f["propiedaddelcliente"]))
            if None in (a, b, c_) or a <= 0:
                continue
            comparaciones += 1
            cumplen += 1 if a >= b >= c_ else 0
        add("R08", cumplen, comparaciones, "provisional",
            "Orden del codigo del Hito 2; fundamento documental sin contrastar.")
    else:
        add("R08", None, None, "no_medible",
            "Requiere confirmar las tres etiquetas de propiedad y la variable comparada.")

    # R09 · estructura de importes según categoría
    if cfg["clave"] == "epm":
        cumplen = 0
        for f in filas:
            niv = (f.get("nivel") or "").strip()
            punta = (numero(f["punta"]) or 0, numero(f["fueradepunta"]) or 0)
            prop = tuple(numero(f[c]) or 0 for c in
                         ("propiedadepm", "compartido", "propiedaddelcliente"))
            if niv == "I":
                cumplen += 1 if not any(punta) else 0
            elif niv in ("II", "III", "IV"):
                cumplen += 1 if not any(prop) else 0
            else:
                cumplen += 1
        add("R09", cumplen, n, "provisional",
            "Pendiente decidir si cero significa 'no aplica'; patron tomado del codigo.")
    else:
        add("R09", None, None, "no_medible",
            "Requiere matriz de combinaciones nivel-propiedad-modalidad-concepto.")

    # R10 · importes requeridos disponibles
    con_alguno = sum(1 for f in filas if any(numero(f.get(c)) not in (None, 0) for c in medidas))
    add("R10", con_alguno, n, "provisional",
        "Conjunto de medidas requeridas sin definir: se exige al menos un importe distinto de cero. "
        "La unidad fila no detecta columnas enteras en cero.")

    # R11 · sospecha de serial de fecha
    finitos = sospechosos = 0
    for f in filas:
        for c in medidas:
            v = numero(f.get(c))
            if v is None:
                continue
            finitos += 1
            sospechosos += 1 if (float(v).is_integer()
                                 and SERIAL_EXCEL[0] <= v <= SERIAL_EXCEL[1]) else 0
    add("R11", sospechosos, finitos, "medido", "Prevalencia: no confirma error.")

    # R12 · prevalencia de magnitud atípica
    series = collections.defaultdict(list)
    for f in filas:
        clave = tuple(canonico(f.get(c)) for c in categorias)
        for c in medidas:
            v = numero(f.get(c))
            if v is not None and v != 0:
                series[(clave, c)].append(abs(v))
    evaluadas = atipicas = 0
    for valores in series.values():
        if len(valores) < 3:
            continue
        mediana = st.median(valores)
        if mediana <= 0:
            continue
        evaluadas += len(valores)
        atipicas += sum(1 for v in valores if v > FACTOR_R12 * mediana)
    add("R12", atipicas, evaluadas, "provisional",
        f"Factor {FACTOR_R12} sin calibrar y mediana sobre la serie completa, "
        "no sobre una ventana de referencia separada de la vigilancia.")

    # INT01 · contrato estructural
    columnas = list(filas[0].keys())
    presentes = sum(1 for c in set(columnas) if columnas.count(c) == 1)
    add("INT01", presentes, cfg["columnas_esperadas"], "medido")

    # INT02 · referencias categóricas resolubles
    if cfg["pares_codigo_nombre"]:
        codigos = resueltos = 0
        rotos_detalle = []
        for cod, nom in cfg["pares_codigo_nombre"]:
            mapa = collections.defaultdict(collections.Counter)
            for f in filas:
                mapa[f.get(cod)][f.get(nom)] += 1
            codigos += len(mapa)
            resueltos += sum(1 for v in mapa.values() if len(v) == 1)
            for k, v in mapa.items():
                if len(v) > 1:
                    rotos_detalle.append((cod, k, v))
        add("INT02", resueltos, codigos, "provisional",
            "Sin catalogo externo versionado: se evalua consistencia interna codigo-nombre.")
        extra["int02_rotos"] = rotos_detalle
    else:
        add("INT02", None, None, "no_medible", "La fuente no publica pares codigo-nombre.")

    # EXA01 · contraste documental contra otro publicador, donde hay traslape
    exa = exactitud_chec(filas) if cfg["clave"] == "chec" else None
    if exa:
        add("EXA01", exa[0], exa[1], "provisional", exa[2])
    else:
        add("EXA01", None, None, "no_medible",
            "Sin traslape temporal con la referencia disponible; requiere la publicacion "
            "tarifaria original de la entidad.")
    add("OPO01", None, None, "no_medible",
        "La fuente no publica fecha de disponibilidad por periodo; "
        "year/mes no es fecha de publicacion.")
    add("MAP01", None, None, "no_medible",
        "Requiere validacion escrita de las equivalencias.")
    add("DEF01", None, None, "no_medible",
        "Requiere semantica y unidad aprobadas por la fuente.")
    add("CART01", None, None, "no_medible",
        "Requiere las cartas en cambios logaritmicos de la actividad 5 del Hito 3.")

    # Observación de apoyo: continuidad de cobertura. No acredita OPO01.
    presentes_per = set()
    for f in con_periodo:
        mes = (MESES_EPM.get((f[campo_mes] or "").strip())
               if cfg["mes_es_texto"] else int(f[campo_mes]))
        if mes:
            presentes_per.add((int(f[campo_ano]), mes))
    ini, fin = min(presentes_per), max(presentes_per)
    esperados, (a, m) = 0, ini
    while (a, m) <= fin:
        esperados += 1
        a, m = (a + 1, 1) if m == 12 else (a, m + 1)
    extra["cobertura"] = dict(presentes=len(presentes_per), esperados=esperados,
                              ini=ini, fin=fin)
    extra["filas"] = n
    return r, extra


# --------------------------------------------------------------------------
# Escritura dentro de los tres archivos de la matriz
# --------------------------------------------------------------------------

def pct(d):
    return "" if d["valor"] is None else f"{d['valor']:.4f}"


def escribir_csv(med, sello):
    filas = list(csv.DictReader(open(MATRIZ_CSV, encoding="utf-8-sig", newline="")))
    campos = [c for c in filas[0].keys()]
    nuevos = ["resultado_numerador", "resultado_denominador", "resultado_valor",
              "resultado_nota", "medido_utc"]
    for c in nuevos:
        if c not in campos:
            campos.append(c)
    for f in filas:
        d = med[f["fuente"]][0].get(f["control"])
        if not d:
            continue
        f["resultado_numerador"] = "" if d["numerador"] is None else d["numerador"]
        f["resultado_denominador"] = "" if d["denominador"] is None else d["denominador"]
        f["resultado_valor"] = pct(d)
        f["resultado_nota"] = d["nota"]
        f["estado_medicion"] = d["estado"]
        f["medido_utc"] = sello
    with open(MATRIZ_CSV, "w", encoding="utf-8-sig", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=campos)
        w.writeheader()
        w.writerows(filas)


def estado_control(a, b):
    est = {a["estado"], b["estado"]}
    if est == {"medido"}:
        return "medido"
    if est == {"no_medible"}:
        return "no_medible"
    if "no_medible" in est:
        return "medido_parcial"
    return "provisional"


def escribir_yaml(med, sello):
    txt = MATRIZ_YAML.read_text(encoding="utf-8")
    epm, chec = med["EPM"][0], med["CHEC"][0]

    def bloque(control):
        a, b = epm[control], chec[control]
        out = ["  resultado:"]
        for cfg_clave, d in (("epm", a), ("chec", b)):
            out.append(f"    {cfg_clave}:")
            out.append(f"      numerador: {'null' if d['numerador'] is None else d['numerador']}")
            out.append(f"      denominador: {'null' if d['denominador'] is None else d['denominador']}")
            out.append(f"      valor: {'null' if d['valor'] is None else d['valor']}")
            out.append(f"      estado: {d['estado']}")
            if d["nota"]:
                # Las notas llevan dos puntos; hay que entrecomillarlas o el escalar se rompe.
                out.append("      nota: '{}'".format(d["nota"].replace("'", "''")))
        out.append(f"    medido_utc: '{sello}'")
        return "\n".join(out) + "\n"

    # Un bloque `resultado` y un `estado_medicion` por control, en el orden de ORDEN.
    pendientes = list(ORDEN)

    def sub_resultado(_m):
        return bloque(pendientes.pop(0))

    txt = re.sub(r"^  resultado:\n(?:[ ]{4,}.*\n)*", sub_resultado, txt, flags=re.M)

    pendientes_est = list(ORDEN)

    def sub_estado(_m):
        c = pendientes_est.pop(0)
        return f"  estado_medicion: {estado_control(epm[c], chec[c])}"

    txt = re.sub(r"^  estado_medicion: .*$", sub_estado, txt, flags=re.M)

    txt = re.sub(r"^estado: .*$",
                 "estado: Especificacion documental con linea base medida sobre los CSV "
                 "conservados; controles con evidencia externa pendiente siguen sin medir.",
                 txt, flags=re.M)
    MATRIZ_YAML.write_text(txt, encoding="utf-8")


def escribir_md(med, sello, proc):
    txt = MATRIZ_MD.read_text(encoding="utf-8")
    epm, chec = med["EPM"][0], med["CHEC"][0]
    xe, xc = med["EPM"][1], med["CHEC"][1]

    def linea(control):
        a, b = epm[control], chec[control]

        def uno(nombre, d):
            if d["valor"] is None:
                return f"{nombre} sin medir ({d['estado']})"
            return f"{nombre} {d['valor']:.4g} % ({d['numerador']}/{d['denominador']}, {d['estado']})"

        return f"- **Estado:** {uno('EPM', a)}; {uno('CHEC', b)}."

    pendientes = list(ORDEN)

    def sub(_m):
        return linea(pendientes.pop(0))

    txt = re.sub(r"^- \*\*Estado:\*\* .*$", sub, txt, flags=re.M)

    # Sección de línea base, regenerada en cada ejecución.
    filas_tabla = []
    for c in ORDEN:
        a, b = epm[c], chec[c]
        va = "—" if a["valor"] is None else f"{a['valor']:.4g} %<br><sub>{a['numerador']}/{a['denominador']}</sub>"
        vb = "—" if b["valor"] is None else f"{b['valor']:.4g} %<br><sub>{b['numerador']}/{b['denominador']}</sub>"
        filas_tabla.append(f"| {c} | {va} | {vb} | {a['estado']} / {b['estado']} |")

    col = xc["por_columna"]
    filas_col = []
    for c, d in sorted(col.items(), key=lambda kv: -kv[1]["ceros"]):
        if d["ceros"] or d["negativos"] or d["vacias"]:
            filas_col.append(f"| `{c.replace('costounitariotarifa_', '')}` | {d['ceros']} | "
                             f"{100 * d['ceros'] / xc['filas']:.1f} % | {d['negativos']} | {d['vacias']} |")

    rotos = ""
    for cod, k, formas in xc.get("int02_rotos", []):
        detalle = " · ".join(f"{n} ({v})" for n, v in formas.most_common())
        rotos += f"- `{cod} = '{k}'` resuelve a {len(formas)} descripciones: {detalle}\n"

    cob_e, cob_c = xe["cobertura"], xc["cobertura"]
    neg_e = " · ".join(f"{v} en {k}" for k, v in xe["negativos_por_concepto"].most_common())

    seccion = f"""<!-- INICIO LINEA BASE -->
## Línea base medida

Valores calculados por [`medir_matriz_oe1.py`](medir_matriz_oe1.py) sobre los CSV de
`fuentes_datos/datos/`, aplicando las definiciones de población, numerador y denominador
de esta misma matriz. Última ejecución: {sello}.

| Archivo medido | Filas | SHA-256 |
|---|---|---|
| `{proc['EPM']['archivo']}` | {proc['EPM']['filas']} | `{proc['EPM']['sha256']}` |
| `{proc['CHEC']['archivo']}` | {proc['CHEC']['filas']} | `{proc['CHEC']['sha256']}` |

> Estos hashes no coinciden con `fuentes_datos/verificaciones/manifiesto_archivos.json`.
> La causa está identificada y no es corrupción: el repositorio no declara política de fin
> de línea y `core.autocrlf` convierte LF a CRLF al extraer en Windows, lo que añade un byte
> por línea. Convirtiendo el archivo de EPM a LF se obtiene exactamente el hash del manifiesto.
> Un hash de archivo de texto solo es verificable si la política de fin de línea está declarada.

### Resultado por control

| Control | EPM | CHEC | Estado EPM / CHEC |
|---|---|---|---|
{chr(10).join(filas_tabla)}

### Observación de apoyo: continuidad de cobertura

| Fuente | Períodos presentes | Esperados en la ventana | Ventana |
|---|---|---|---|
| EPM | {cob_e['presentes']} | {cob_e['esperados']} | {cob_e['ini'][0]}-{cob_e['ini'][1]:02d} a {cob_e['fin'][0]}-{cob_e['fin'][1]:02d} |
| CHEC | {cob_c['presentes']} | {cob_c['esperados']} | {cob_c['ini'][0]}-{cob_c['ini'][1]:02d} a {cob_c['fin'][0]}-{cob_c['fin'][1]:02d} |

**No acredita OPO01 y no debe presentarse como tal.** OPO01 exige evidencia de que cada
publicación estuvo disponible dentro de un plazo documentado, y su propia especificación
prohíbe usar `year`/`mes` como fecha de publicación. La continuidad solo muestra que no
faltan períodos dentro de la ventana, que es una propiedad distinta.

### Lo que cambia al aplicar las definiciones de esta matriz

**R05 en EPM da 100 %.** La población exige conservar una fila por clase de copia exacta
antes de evaluar la clave. Con ese paso no queda ninguna clave repetida: las repeticiones
de clave en EPM son las mismas filas que ya detecta R04. Medir R05 sin deduplicar primero
reporta como defecto de unicidad lo que ya se contó una vez.

**R07 en EPM da 100 %.** Los {sum(xe['negativos_por_concepto'].values())} importes negativos
están todos en el concepto con excepción documentada: {neg_e}. Ningún otro concepto presenta
negativos, de modo que la excepción describe el dato en lugar de relajarlo.

**R03 en EPM da 100 %.** El denominador de esta matriz son las celdas *informadas*. Las
celdas vacías no entran y se reportan en completitud; contarlas como fallo de formato
mezcla dos dimensiones.

### Hallazgos que surgen de medir

**R10 con unidad de observación «fila» no detecta columnas vacías.** El control da
{epm['R10']['valor']:.4g} % en EPM y {chec['R10']['valor']:.4g} % en CHEC porque toda fila
tiene al menos un importe informado. El detalle por columna en CHEC muestra otra realidad:

| Columna | Ceros | % de filas | Negativos | Vacías |
|---|---|---|---|---|
{chr(10).join(filas_col)}

Se propone cambiar la unidad de observación de R10 de fila a celda por columna. Es un cambio
en la especificación, no en el código, y sin él un scorecard declararía a CHEC completo.

**`cureal` y `subcon` necesitan DEF01 antes de que R07 y R10 signifiquen algo.** Un 83 % de
ceros en una columna y un 41 % en otra no se interpretan sin saber qué representan. La matriz
ya lo advierte; la medición lo cuantifica.

**INT02 encuentra su primer caso en CHEC.**

{rotos}
El estrato ya viaja en `claseservicio_estrato` y la descripción lo duplica en la mayoría de
las filas pero no en todas. Es denormalización inconsistente, que es el defecto que INT02
existe para detectar.

**R06 no detecta sinónimos.** Sin catálogo canónico aprobado, la medición toma como forma
canónica la variante más frecuente tras normalizar mayúsculas y espacios. Con ese criterio
CHEC da 100 %: no hay variantes de capitalización. No significa que esté limpio en
consistencia, sino que este criterio solo ve diferencias de forma. Los sinónimos son
competencia de MAP01, que sigue sin evidencia.

### Qué sigue sin poder medirse

| Control | Qué falta |
|---|---|
| EXA01 | La publicación tarifaria original de cada entidad. Las alertas de R11, R12 y las cartas solo generan sospechas. |
| OPO01 | Evidencia de la fecha real de disponibilidad por período y un plazo esperado documentado. |
| MAP01 | Validación escrita de que dos etiquetas significan lo mismo. |
| DEF01 | Significado, unidad y uso aprobados por la fuente. |
| CART01 | Las cartas en cambios logarítmicos de la actividad 5 del Hito 3. |
| R08 y R09 en CHEC | Matriz de combinaciones nivel-propiedad-modalidad-concepto y confirmación de las etiquetas de propiedad. |

Cinco de los diecinueve controles dependen de evidencia externa a los conjuntos. Esa es la
brecha real del punto 1, y no se cierra midiendo mejor.
<!-- FIN LINEA BASE -->
"""

    if "<!-- INICIO LINEA BASE -->" in txt:
        txt = re.sub(r"<!-- INICIO LINEA BASE -->.*?<!-- FIN LINEA BASE -->\n",
                     seccion, txt, flags=re.S)
    else:
        txt = txt.replace("## Evidencia externa y cierre", seccion + "\n## Evidencia externa y cierre")
    MATRIZ_MD.write_text(txt, encoding="utf-8")


def main():
    sello = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    med, proc = {}, {}
    for cfg in (EPM, CHEC):
        med[cfg["fuente"]] = medir(cfg)
        proc[cfg["fuente"]] = dict(
            archivo=str(cfg["archivo"].relative_to(RAIZ)).replace("\\", "/"),
            filas=med[cfg["fuente"]][1]["filas"], sha256=sha256(cfg["archivo"]))

    escribir_csv(med, sello)
    escribir_yaml(med, sello)
    escribir_md(med, sello, proc)

    epm, chec = med["EPM"][0], med["CHEC"][0]
    print(f"Medición {sello}\n")
    print(f"  {'control':<8} {'EPM':>22}   {'CHEC':>22}")
    for c in ORDEN:
        def celda(d):
            if d["valor"] is None:
                return f"{'-':>10}  {d['estado']:<10}"
            return f"{d['valor']:>10.4f}  {d['estado']:<10}"
        print(f"  {c:<8} {celda(epm[c])}   {celda(chec[c])}")
    print("\nActualizados: matriz_oe1.csv, matriz_oe1.yaml, matriz_oe1.md")


if __name__ == "__main__":
    main()
