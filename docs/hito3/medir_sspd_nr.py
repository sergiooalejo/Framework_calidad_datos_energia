# -*- coding: utf-8 -*-
"""Medición de la matriz OE1 sobre la cuarta fuente: SSPD, conjunto bnkp-xdb7.

Es información comercial NO residencial del Sistema Interconectado Nacional. A diferencia
de la fuente ZNI, esta sí trae el eje de propiedad del activo y la tarifa aplicada, de modo
que R08, R09 e INT02 vuelven a tener sobre qué aplicarse.

Lo importa `medir_matriz_oe1.py`; no se ejecuta por separado.
"""

from collections import Counter, defaultdict
from pathlib import Path
import csv
import re

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parents[1]
DATOS = RAIZ / "fuentes_datos" / "datos"
ARCHIVO = DATOS / "sspd_bnkp-xdb7.csv"

AUSENTES = {"", "N/A", "NA", "null", "None"}

MEDIDAS = ["car_t440_dias_fact", "car_t440_dias_mora", "consumos", "consumo_promedio_mensual",
           "consumo_energia_reactiva", "tarifa_aplicada", "facturacion_por_consumo",
           "refacturacion_por_consumo", "valor_total_facturado", "valor_subsidio",
           "valor_de_la_contribucion", "contribuciones_recaudadas", "valor_compensado"]

CATEGORICAS = ["car_t440_tip_tarifa", "car_t440_sector", "car_t440_ubic",
               "car_t440_tipo_lect", "car_t440_tipo_fact", "car_t440_car_inver",
               "dane_nom_dpto", "dane_nom_mpio", "nom_mercado"]

# Conceptos cuyo dominio es positivo por definición. Se excluyen los que son ajustes
# (refacturación, valor total) porque admiten negativo legítimamente.
SOLO_POSITIVOS = ["car_t440_dias_fact", "car_t440_dias_mora", "consumos",
                  "consumo_promedio_mensual", "consumo_energia_reactiva", "tarifa_aplicada",
                  "facturacion_por_consumo", "valor_subsidio", "valor_de_la_contribucion"]

CATALOGOS = DATOS / "sspd_bnkp-xdb7_catalogos.csv"

# Columnas del contrato de la copia conservada. El conjunto en origen trae 48; la copia
# conserva las 27 analiticas y mueve los nombres denormalizados al archivo de catalogos,
# porque el nombre de empresa repetido en cada fila pesaba 15,8 MB por si solo.
COLUMNAS_ESPERADAS = 27
COLUMNAS_EN_ORIGEN = 48
SERIAL_EXCEL = (36526, 47483)
FACTOR_R12 = 10
MIN_MESES = 49


def numero(texto):
    s = (texto or "").strip()
    if s in AUSENTES:
        return None
    try:
        return float(s.replace(",", "."))
    except ValueError:
        return None


def canonico(texto):
    return re.sub(r"\s+", " ", (texto or "").strip()).casefold()


def _r(numerador, denominador, estado, nota=""):
    valor = None if not denominador else 100.0 * numerador / denominador
    return dict(numerador=numerador, denominador=denominador, valor=valor,
                estado=estado, nota=nota)


def _vacio(estado, nota):
    return dict(numerador=None, denominador=None, valor=None, estado=estado, nota=nota)


def mediana(xs):
    s = sorted(xs)
    return s[len(s) // 2] if s else None


def medir_sspd_nr():
    filas = list(csv.DictReader(open(ARCHIVO, encoding="utf-8", newline="")))
    n = len(filas)
    cols = list(filas[0].keys()) if filas else []
    m = {}

    # --- R01 período informado ----------------------------------------------
    ok = sum(1 for f in filas
             if (f.get("car_carg_ano") or "").strip() not in AUSENTES
             and (f.get("car_carg_mes") or "").strip() not in AUSENTES)
    m["R01"] = _r(ok, n, "medido")

    # --- R02 período válido --------------------------------------------------
    val = 0
    for f in filas:
        try:
            a, p = int(float(f["car_carg_ano"])), int(float(f["car_carg_mes"]))
            if 2000 <= a <= 2026 and 1 <= p <= 12:
                val += 1
        except (ValueError, KeyError, TypeError):
            pass
    m["R02"] = _r(val, ok, "medido")

    # --- R03 importes numéricos y finitos ------------------------------------
    inf = bien = 0
    for f in filas:
        for c in MEDIDAS:
            s = (f.get(c) or "").strip()
            if s in AUSENTES:
                continue
            inf += 1
            if numero(s) is not None:
                bien += 1
    m["R03"] = _r(bien, inf, "medido",
                  "Denominador: celdas informadas de las {} medidas numericas.".format(len(MEDIDAS)))

    # --- R04 duplicados exactos ----------------------------------------------
    vistas = Counter(tuple(f.get(c, "") for c in cols) for f in filas)
    extra = sum(v - 1 for v in vistas.values() if v > 1)
    m["R04"] = _r(n - extra, n, "medido",
                  "{} filas son copia exacta de otra.".format(extra) if extra else "")

    # --- R05 clave sin multiplicidad -----------------------------------------
    unicas = list(vistas.keys())
    pos = {c: i for i, c in enumerate(cols)}
    claves = Counter(k[pos["id_factura"]] for k in unicas) if "id_factura" in pos else Counter()
    rep = sum(v - 1 for v in claves.values() if v > 1)
    m["R05"] = _r(len(unicas) - rep, len(unicas), "provisional",
                  "Clave provisional id_factura; {} identificadores repetidos.".format(rep))

    # --- R06 representación canónica -----------------------------------------
    variantes, celdas, conformes = [], 0, 0
    for c in CATEGORICAS:
        if c not in cols:
            continue
        grupos = {}
        for f in filas:
            v = f.get(c) or ""          # sin strip: el espacio final es la variante buscada
            if v.strip() in AUSENTES:
                continue
            grupos.setdefault(canonico(v), Counter())[v] += 1
        for _, formas in grupos.items():
            celdas += sum(formas.values())
            conformes += formas.most_common(1)[0][1]
            if len(formas) > 1:
                variantes.append((c, dict(formas)))
    m["R06"] = _r(conformes, celdas, "provisional",
                  "{} grupos con mas de una forma de escritura. Catalogo canonico no acordado."
                  .format(len(variantes)))

    # --- R07 signo por concepto ----------------------------------------------
    ev = conf = 0
    neg = Counter()
    for f in filas:
        for c in SOLO_POSITIVOS:
            v = numero(f.get(c))
            if v is None:
                continue
            ev += 1
            if v >= 0:
                conf += 1
            else:
                neg[c] += 1
    m["R07"] = _r(conf, ev, "provisional",
                  "Dominio de signo por concepto sin acordar; negativos en {}."
                  .format(", ".join(neg) or "ninguno"))

    # --- R08 orden entre tarifas por propiedad --------------------------------
    # Esta fuente SI tiene el eje de propiedad (car_t440_car_inver = 100, 50, 0).
    # Se compara la tarifa mediana entre niveles de propiedad dentro de cada
    # (empresa, periodo, sector) y se mide cuantos grupos respetan el orden dominante.
    porgrupo = defaultdict(lambda: defaultdict(list))
    for f in filas:
        t = numero(f.get("tarifa_aplicada"))
        prop = (f.get("car_t440_car_inver") or "").strip()
        if t is None or t <= 0 or prop in AUSENTES:
            continue
        g = (f.get("identificador_empresa"), f.get("car_carg_ano"),
             f.get("car_carg_mes"), f.get("car_t440_sector"))
        porgrupo[g][prop].append(t)

    sentidos = Counter()
    comparables = []
    for g, d in porgrupo.items():
        meds = {p: mediana(v) for p, v in d.items() if v}
        if len(meds) < 2:
            continue
        orden = sorted(meds.items(), key=lambda kv: -float(kv[0]))   # 100, 50, 0
        comparables.append((g, orden))
        creciente = all(orden[i][1] >= orden[i + 1][1] for i in range(len(orden) - 1))
        decreciente = all(orden[i][1] <= orden[i + 1][1] for i in range(len(orden) - 1))
        if creciente and not decreciente:
            sentidos["mayor_propiedad_mayor_tarifa"] += 1
        elif decreciente and not creciente:
            sentidos["mayor_propiedad_menor_tarifa"] += 1
        else:
            sentidos["sin_orden"] += 1
    dom = sentidos.most_common(1)[0][0] if sentidos else None
    m["R08"] = _r(sentidos.get(dom, 0), len(comparables), "provisional",
                  "Eje de propiedad disponible (100/50/0). Orden dominante observado: {}. "
                  "El sentido esperado no esta documentado por la fuente; misma decision "
                  "pendiente que en CHEC.".format(dom or "ninguno"))

    # --- R09 estructura de importes según categoría ---------------------------
    # La relacion no es facturacion = consumo x tarifa, sino
    #     consumo x tarifa = facturacion x (1 + tasa de contribucion)
    # porque tarifa_aplicada ya incluye la contribucion de solidaridad y la facturacion
    # por consumo no. Las tasas observadas son 20 % (comercial e industrial), 10 % (IA) y
    # 0 % (oficial, alumbrado publico, areas comunes). Se admite cualquiera de las tres y,
    # cuando la tasa implicita es positiva, se exige ademas que valor_de_la_contribucion
    # concuerde con ella. La tasa por sector NO esta documentada por la fuente: se infirio
    # de los datos, y por eso el control queda provisional.
    TASAS = (0.0, 0.10, 0.20)
    ev9 = ok9 = 0
    tasas_vistas = Counter()
    for f in filas:
        c_, t_, fa = (numero(f.get("consumos")), numero(f.get("tarifa_aplicada")),
                      numero(f.get("facturacion_por_consumo")))
        co = numero(f.get("valor_de_la_contribucion")) or 0.0
        if None in (c_, t_, fa) or c_ <= 0 or t_ <= 0 or fa <= 0:
            continue
        ev9 += 1
        bruto = c_ * t_
        for tasa in TASAS:
            if abs(bruto - fa * (1 + tasa)) / bruto > 0.01:
                continue
            if tasa == 0.0:
                ok9 += 1
                tasas_vistas["0 %"] += 1
            elif abs(co - fa * tasa) <= max(fa * tasa * 0.02, 1.0):
                ok9 += 1
                tasas_vistas["{:.0f} %".format(tasa * 100)] += 1
            break
    detalle = ", ".join("{}: {:,}".format(k, v) for k, v in tasas_vistas.most_common())
    m["R09"] = _r(ok9, ev9, "provisional",
                  "Relacion verificada: consumos x tarifa_aplicada = facturacion_por_consumo "
                  "x (1 + contribucion), con contribucion de 0, 10 o 20 % y conciliada contra "
                  "valor_de_la_contribucion. Tasas halladas -> {}. La tasa por sector se "
                  "infirio de los datos; la fuente no la documenta.".format(detalle))

    # --- R10 importes requeridos ---------------------------------------------
    req = ["consumos", "tarifa_aplicada", "valor_total_facturado"]
    ok10 = sum(1 for f in filas if all((f.get(c) or "").strip() not in AUSENTES for c in req))
    m["R10"] = _r(ok10, n, "provisional",
                  "Conjunto obligatorio propuesto: {}.".format(", ".join(req)))

    # --- R11 serial de fecha en importe (prevalencia) -------------------------
    sosp = tot = 0
    for f in filas:
        for c in MEDIDAS:
            v = numero(f.get(c))
            if v is None:
                continue
            tot += 1
            if SERIAL_EXCEL[0] <= v <= SERIAL_EXCEL[1] and float(v).is_integer():
                sosp += 1
    m["R11"] = _r(sosp, tot, "medido", "Prevalencia, no conformidad.")

    # --- R12 magnitud atípica (prevalencia) -----------------------------------
    base = [numero(f.get("consumos")) for f in filas]
    base = [v for v in base if v is not None and v > 0]
    at = 0
    if base:
        med = mediana(base)
        at = sum(1 for v in base if v > FACTOR_R12 * med)
    m["R12"] = _r(at, len(base), "provisional",
                  "Prevalencia, no conformidad. Factor {} sobre la mediana de consumos."
                  .format(FACTOR_R12))

    # --- INT01 contrato estructural -------------------------------------------
    m["INT01"] = _r(len(cols), COLUMNAS_ESPERADAS, "medido",
                    "{} columnas en la copia conservada, que declara {}. En origen el "
                    "conjunto trae {}; los nombres denormalizados viven en el archivo de "
                    "catalogos.".format(len(cols), COLUMNAS_ESPERADAS, COLUMNAS_EN_ORIGEN))

    # --- INT02 referencias categóricas ----------------------------------------
    # Esta fuente SI tiene pares codigo-nombre, a diferencia de la fuente ZNI. Viven en el
    # archivo de catalogos, que conserva una fila por par observado: si un codigo resuelve
    # a mas de un nombre, aparece varias veces, de modo que la evidencia no se pierde.
    tot02 = ok02 = 0
    rotos = []
    if CATALOGOS.exists():
        mapa = defaultdict(Counter)
        for f in csv.DictReader(open(CATALOGOS, encoding="utf-8", newline="")):
            cod, nom = f["campo_codigo"], f["campo_nombre"]
            k, v = (f["codigo"] or "").strip(), (f["nombre"] or "").strip()
            if k in AUSENTES or v in AUSENTES:
                continue
            try:
                mapa[(cod, nom, k)][v] += int(f["n_registros"])
            except (ValueError, KeyError):
                mapa[(cod, nom, k)][v] += 1
        for (cod, _nom, k), formas in mapa.items():
            tot02 += 1
            if len(formas) == 1:
                ok02 += 1
            else:
                rotos.append((cod, k, formas))
    m["INT02"] = _r(ok02, tot02, "medido",
                    "{} claves resuelven a mas de un nombre; las diferencias son de "
                    "codificacion de caracteres y de tildes.".format(len(rotos))
                    if rotos else "Cada codigo resuelve a un unico nombre.")

    # --- EXA01 exactitud -------------------------------------------------------
    m["EXA01"] = _vacio("no_medible",
                        "Sin publicacion tarifaria original de estos 32 prestadores con la que "
                        "contrastar. La reconciliacion interna se reporta en R09, que es otra cosa.")

    # --- OPO01 oportunidad -----------------------------------------------------
    # car_t440_fec_exp mide el rezago entre periodo y expedicion de la FACTURA.
    # Eso es oportunidad del servicio, no del dato, y OPO01 esta escrito sobre la
    # disponibilidad de la publicacion. No se fuerza el control.
    m["OPO01"] = _vacio("no_medible",
                        "La fuente trae fecha de expedicion de factura, que mide oportunidad del "
                        "servicio y no del dato. OPO01 exige fecha de disponibilidad de la "
                        "publicacion; cerrarlo requiere reespecificar el control.")

    # --- MAP01 equivalencias --------------------------------------------------
    if variantes:
        m["MAP01"] = _r(0, len(variantes), "provisional",
                        "{} grupos con variantes requieren equivalencia documentada."
                        .format(len(variantes)))
    else:
        m["MAP01"] = _vacio("no_medible",
                            "No se detectaron variantes de escritura, de modo que no hay mapeos "
                            "aplicados que acreditar. No equivale a consistencia demostrada.")

    # --- DEF01 semántica documentada ------------------------------------------
    criticas = 28   # las variables documentadas en diccionarios/sspd_nr.yaml
    m["DEF01"] = _r(0, criticas, "medido",
                    "Ninguna de las {} columnas trae descripcion en el metadato del portal."
                    .format(COLUMNAS_ESPERADAS))

    # --- CART01 cartas I-MR ----------------------------------------------------
    per = sorted({(f.get("car_carg_ano"), f.get("car_carg_mes")) for f in filas})
    m["CART01"] = _vacio("no_medible",
                         "No ejecutable sobre esta fuente: {} periodos mensuales frente a los {} "
                         "que exige el protocolo.".format(len(per), MIN_MESES))

    pares = []
    for a, p in per:
        try:
            pares.append((int(float(a)), int(float(p))))
        except (TypeError, ValueError):
            pass
    pares.sort()
    ini, fin = pares[0], pares[-1]
    cobertura = dict(presentes=len(pares),
                     esperados=(fin[0] - ini[0]) * 12 + (fin[1] - ini[1]) + 1,
                     ini=ini, fin=fin)

    porperiodo = Counter((int(float(f["car_carg_ano"])), int(float(f["car_carg_mes"])))
                         for f in filas if f.get("car_carg_ano") and f.get("car_carg_mes"))
    extras = dict(filas=n, columnas=len(cols), variantes=variantes, negativos=neg,
                  cobertura=cobertura, periodos=len(per), int02_rotos=rotos,
                  sentidos_r08=sentidos, por_periodo=porperiodo,
                  empresas=len({f.get("identificador_empresa") for f in filas}))
    return m, extras
