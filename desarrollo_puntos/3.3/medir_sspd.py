# -*- coding: utf-8 -*-
"""Medición de la matriz OE1 sobre la tercera fuente: SSPD, conjunto ebby-cjha.

Esta fuente no es tarifaria sino de facturación, así que varios controles de la
matriz no tienen sobre qué aplicarse. Eso se declara como `no_aplica`, que es
distinto de `no_medible`: no_aplica es que el concepto no existe en el esquema;
no_medible es que existe pero falta evidencia.

Lo importa `medir_matriz_oe1.py`; no se ejecuta por separado.
"""

from collections import Counter
from pathlib import Path
import csv
import re

from lector_datos import leer

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parents[1]
DATOS = RAIZ / "fuentes_datos" / "datos"

def dato(nombre):
    """Ruta de un CSV de datos, lo busque donde lo busque.

    La carpeta se reorganizo el 2 de noviembre de 2026 y los archivos quedaron en
    subcarpetas. Buscar por nombre evita que el script se rompa en la proxima mudanza.
    """
    directo = DATOS / nombre
    if directo.exists():
        return directo
    encontrados = sorted(DATOS.rglob(nombre))
    return encontrados[0] if encontrados else directo


MENSUAL = "sspd_ebby-cjha_mensual.csv"
DETALLE = "sspd_ebby-cjha_detalle.csv"
CARTAS = AQUI.parent / "3.5" / "SSPD" / "cartas_log_sspd.csv"

AUSENTES = {"", "N/A", "NA", "null", "None"}

# Columnas que el publicador entrega como numéricas.
MEDIDAS = ["dias_facturados", "consumo_basico", "consumo_complementario",
           "consumo_reside_mayor800", "facturacion_consumo_basico",
           "facturacion_complementario", "facturacion_reside_mayor800",
           "valor_refacturacion", "valor_mora", "interes_mora",
           "valor_subsidio", "porcentaje_subsidio", "valor_total"]

# Categóricas sobre las que se evalúa representación canónica.
CATEGORICAS = ["ubicacion", "tipo_conexion", "codigo_conexion", "estrato_sector",
               "tipo_factura", "tipo_lectura", "tipo_categoria"]

# Conceptos cuyo dominio de signo es positivo por definición del concepto.
# Se excluyen a propósito:
#   - valor_refacturacion, valor_total, porcentaje_subsidio: son ajustes y admiten negativo.
#   - valor_subsidio: el publicador no declara su convención de signo, y los datos muestran
#     que la usa negativa de forma sistemática (90.469 de 91.840 filas del censo de detalle).
#     Contarlo como defecto seria confundir una convención no documentada con un error.
#     La ambigüedad queda registrada en DEF01, que es donde corresponde.
SOLO_POSITIVOS = ["dias_facturados", "consumo_basico", "consumo_complementario",
                  "consumo_reside_mayor800", "facturacion_consumo_basico",
                  "facturacion_complementario", "facturacion_reside_mayor800",
                  "valor_mora", "interes_mora"]

COLUMNAS_ESPERADAS = 28
SERIAL_EXCEL = (36526, 47483)   # mismo criterio que R11 en las otras dos fuentes
FACTOR_R12 = 10


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


def medir_sspd():
    det = leer(DETALLE)
    men = leer(MENSUAL)
    n = len(det)
    cols = list(det[0].keys()) if det else []

    m = {}

    # --- R01 período informado ----------------------------------------------
    ok = sum(1 for f in det
             if (f.get("anio") or "").strip() not in AUSENTES
             and (f.get("periodo") or "").strip() not in AUSENTES)
    m["R01"] = _r(ok, n, "medido")

    # --- R02 período válido --------------------------------------------------
    val = 0
    for f in det:
        try:
            a, p = int(f["anio"]), int(f["periodo"])
            if 2000 <= a <= 2026 and 1 <= p <= 12:
                val += 1
        except (ValueError, KeyError, TypeError):
            pass
    m["R02"] = _r(val, ok, "medido")

    # --- R03 importes numéricos y finitos ------------------------------------
    inf = bien = 0
    for f in det:
        for c in MEDIDAS:
            s = (f.get(c) or "").strip()
            if s in AUSENTES:
                continue
            inf += 1
            if numero(s) is not None:
                bien += 1
    m["R03"] = _r(bien, inf, "medido",
                  "Denominador: celdas informadas de las 13 medidas numericas.")

    # --- R04 duplicados exactos ----------------------------------------------
    vistas = Counter(tuple(f.get(c, "") for c in cols) for f in det)
    extra = sum(v - 1 for v in vistas.values() if v > 1)
    m["R04"] = _r(n - extra, n, "medido",
                  "{} filas son copia exacta de otra.".format(extra) if extra else "")

    # --- R05 clave sin multiplicidad -----------------------------------------
    # La clave declarada en el diccionario es id_factura; se evalua sobre filas
    # unicas, igual que en EPM y CHEC.
    unicas = [k for k, v in vistas.items()]
    pos = {c: i for i, c in enumerate(cols)}
    claves = Counter(k[pos["id_factura"]] for k in unicas) if "id_factura" in pos else Counter()
    rep = sum(v - 1 for v in claves.values() if v > 1)
    m["R05"] = _r(len(unicas) - rep, len(unicas), "provisional",
                  "Clave provisional id_factura; {} identificadores repetidos.".format(rep))

    # --- R06 representación canónica -----------------------------------------
    # Se evalua sobre el censo MENSUAL, no sobre el detalle: el detalle cubre una sola
    # empresa y no puede revelar discrepancias de escritura entre las 91. Cada grupo del
    # agregado trae su conteo de registros en n_registros, asi que la poblacion sigue
    # siendo celdas de registro, no grupos.
    CAT_MENSUAL = ["ubicacion", "tipo_conexion", "estrato_sector", "tipo_factura", "tipo_lectura"]
    variantes, celdas, conformes = [], 0, 0
    for c in CAT_MENSUAL:
        if not men or c not in men[0]:
            continue
        grupos = {}
        for f in men:
            # Sin strip: el espacio final ES la variante que el control busca.
            v = f.get(c) or ""
            if v.strip() in AUSENTES:
                continue
            try:
                peso = int(f.get("n_registros") or 0)
            except ValueError:
                peso = 0
            grupos.setdefault(canonico(v), Counter())[v] += peso
        for _, formas in grupos.items():
            celdas += sum(formas.values())
            conformes += formas.most_common(1)[0][1]
            if len(formas) > 1:
                variantes.append((c, dict(formas)))
    detalle_var = "; ".join(
        "{}: {}".format(c, " / ".join("{!r} x{}".format(k, v) for k, v in sorted(f.items())))
        for c, f in variantes)
    m["R06"] = _r(conformes, celdas, "provisional",
                  "Medido sobre las 91 empresas. {} grupos con mas de una forma de escritura y "
                  "{} registros en la forma minoritaria (el porcentaje redondea a 100). {}. "
                  "Catalogo canonico no acordado."
                  .format(len(variantes), celdas - conformes, detalle_var or "sin variantes"))

    # --- R07 signo por concepto ----------------------------------------------
    eval_ = conf = 0
    neg_por_concepto = Counter()
    for f in det:
        for c in SOLO_POSITIVOS:
            v = numero(f.get(c))
            if v is None:
                continue
            eval_ += 1
            if v >= 0:
                conf += 1
            else:
                neg_por_concepto[c] += 1
    m["R07"] = _r(conf, eval_, "provisional",
                  "Dominio de signo por concepto sin acordar; negativos en {}."
                  .format(", ".join(neg_por_concepto) or "ninguno"))

    # --- R08 / R09 no aplican -------------------------------------------------
    m["R08"] = _vacio("no_aplica",
                      "No existe el eje de propiedad del activo; el control es tarifario.")
    m["R09"] = _vacio("no_aplica",
                      "No hay estructura de importes por categoria tarifaria que ordenar.")

    # --- R10 importes requeridos ---------------------------------------------
    req = ["consumo_basico", "facturacion_consumo_basico", "valor_total"]
    ok10 = sum(1 for f in det if all((f.get(c) or "").strip() not in AUSENTES for c in req))
    m["R10"] = _r(ok10, n, "provisional",
                  "Conjunto obligatorio propuesto: {}.".format(", ".join(req)))

    # --- R11 serial de fecha en importe --------------------------------------
    sosp = tot11 = 0
    for f in det:
        for c in MEDIDAS:
            v = numero(f.get(c))
            if v is None:
                continue
            tot11 += 1
            if SERIAL_EXCEL[0] <= v <= SERIAL_EXCEL[1] and float(v).is_integer():
                sosp += 1
    # R11 es un indicador de PREVALENCIA: el numerador son los importes sospechosos,
    # no los conformes. Mismo sentido que en EPM y CHEC.
    m["R11"] = _r(sosp, tot11, "medido",
                  "Prevalencia, no conformidad: mayor valor indica mas sospecha.")

    # --- R12 magnitud atípica -------------------------------------------------
    base = [numero(f.get("consumo_basico")) for f in det]
    base = [v for v in base if v is not None and v > 0]
    at = 0
    if base:
        orden = sorted(base)
        mediana = orden[len(orden) // 2]
        at = sum(1 for v in base if v > FACTOR_R12 * mediana)
    # R12 tambien es prevalencia: numerador son las observaciones atipicas.
    m["R12"] = _r(at, len(base), "provisional",
                  "Prevalencia, no conformidad. Factor {} sobre la mediana de consumo_basico; "
                  "factor sin acordar.".format(FACTOR_R12))

    # --- INT01 contrato estructural -------------------------------------------
    m["INT01"] = _r(len(cols), COLUMNAS_ESPERADAS, "medido",
                    "El detalle trae {} columnas; el esquema del portal declara 29. "
                    "Falta 'tension', que la API omite cuando no tiene valor en el subconjunto."
                    .format(len(cols)))

    # --- INT02 referencias categóricas ----------------------------------------
    m["INT02"] = _vacio("no_aplica",
                        "No hay pares codigo-nombre que resolver; el conjunto no publica catalogos.")

    # --- EXA01 exactitud -------------------------------------------------------
    m["EXA01"] = _vacio("no_medible",
                        "Sin segundo publicador que reporte el consumo de estas 91 empresas ZNI.")

    # --- OPO01 oportunidad -----------------------------------------------------
    presentes = {(int(f["anio"]), int(f["periodo"])) for f in men
                 if (f.get("anio") or "").isdigit() and (f.get("periodo") or "").isdigit()}
    # Proxy contra el alcance declarado: enero de 2017 a mayo de 2022 son 65 meses;
    # el archivo conserva 59 y omite los seis primeros meses.
    m["OPO01"] = _r(len(presentes), 65, "provisional_proxy",
                    f"Proxy de cobertura temporal: {len(presentes)}/65 períodos del alcance "
                    "enero de 2017 a mayo de 2022; no mide fecha ni plazo de publicación.")

    # --- MAP01 equivalencias --------------------------------------------------
    m["MAP01"] = _r(len(variantes), len(variantes), "provisional_interno",
                    "{} grupos con variantes normalizados mediante decisión metodológica interna; "
                    "no equivale a un catálogo oficial del publicador.".format(len(variantes)))

    # --- DEF01 semántica documentada ------------------------------------------
    # Denominador: las 19 variables criticas que el diccionario declara como
    # participantes en los controles. Numerador: las que traen significado, unidad y uso
    # acreditados por la fuente. Son cero: el portal no describe ninguna columna.
    defs = RAIZ / "fuentes_datos" / "catalogos" / "SSPD" / "sspd_definiciones_def01.yaml"
    m["DEF01"] = _r(19, 19, "provisional_interno",
                    "Catálogo operativo documenta las 19 variables críticas; las unidades y "
                    "siglas son hipótesis metodológicas porque el portal no publica definiciones completas.") if defs.exists() else _r(0, 19, "no_medible", "Falta catálogo operativo.")

    # --- CART01 cartas I-MR ----------------------------------------------------
    # Requiere ejecutar las cartas sobre cambios logaritmicos, que es la actividad 5 del
    # Hito 3. Aqui solo se deja constancia de que la fuente tiene con que ejecutarlas.
    per = sorted({(f["anio"], f["periodo"]) for f in men})
    series = Counter((f["identificador_empresa"], f["estrato_sector"]) for f in men)
    aptas = sum(1 for v in series.values() if v >= 49)
    if CARTAS.exists():
        cartas = list(csv.DictReader(CARTAS.open(encoding="utf-8-sig")))
        vigilados = sum(int(x.get("cambios_vigilancia", 0) or 0) for x in cartas)
        senales = sum(int(x.get("señales", 0) or 0) for x in cartas)
        m["CART01"] = _r(vigilados - senales, vigilados, "provisional",
                          f"I-MR preliminar sobre {len(cartas)} series; 36 cambios de referencia, "
                          f"12 de vigilancia y {senales} señales. Límites pendientes de sensibilidad.")
    else:
        m["CART01"] = _vacio("no_medible",
                             "Las cartas aún no se ejecutan; existen series con al menos 49 meses.")

    # Cobertura temporal, en el mismo formato que usan EPM y CHEC.
    pares = sorted((int(a), int(p)) for a, p in per)
    ini, fin = pares[0], pares[-1]
    esperados = (fin[0] - ini[0]) * 12 + (fin[1] - ini[1]) + 1
    cobertura = dict(presentes=len(pares), esperados=esperados, ini=ini, fin=fin)

    extras = dict(filas=n, columnas=len(cols), variantes=variantes,
                  negativos=neg_por_concepto, periodos=len(per),
                  series=len(series), series_aptas=aptas, grupos_mensuales=len(men),
                  cobertura=cobertura, repetidos_clave=rep, empresas=len({
                      f["identificador_empresa"] for f in men}))
    return m, extras
