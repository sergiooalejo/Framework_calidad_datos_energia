# -*- coding: utf-8 -*-
"""Adaptador de calidad para el piloto de demanda XM/SIMEM.

La matriz OE1 fue diseñada originalmente sobre tarifas. Este módulo traduce los
controles al contrato de demanda de XM y no reutiliza resultados de SSPD-NR.
Los controles que necesitan una referencia externa o un plazo de publicación se
conservan como ``no_medible`` hasta que exista esa evidencia.
"""

import collections
import math
import re
import statistics as st
from pathlib import Path
from datetime import datetime

from lector_datos import leer


ORDEN = ["R01", "R02", "R03", "R04", "R05", "R06", "R07", "R08", "R09", "R10",
         "R11", "R12", "INT01", "INT02", "EXA01", "OPO01", "MAP01", "DEF01", "CART01"]
MENSUAL = "xm_demanda_mensual_piloto.csv"
CRUDO = "xm_demanda_epmc_epmd_str02_202001_202501.csv"
AUSENTES = {"", "NA", "N/A", "null", "None"}


def _r(num, den, estado, nota=""):
    return dict(numerador=num, denominador=den,
                valor=None if not den else round(100 * num / den, 4),
                estado=estado, nota=nota)


def _n(value):
    try:
        x = float(str(value).strip())
        return x if math.isfinite(x) else None
    except (TypeError, ValueError):
        return None


def _periodo(value):
    return bool(re.fullmatch(r"\d{4}-(0[1-9]|1[0-2])", (value or "").strip()))


def _version_num(value):
    m = re.fullmatch(r"TX(\d+)", (value or "").strip())
    return int(m.group(1)) if m else None


def _cambios(valores):
    return [math.log(b) - math.log(a) for a, b in zip(valores, valores[1:])
            if a is not None and b is not None and a > 0 and b > 0]


def medir_xm():
    mensual = leer(MENSUAL, encoding="utf-8-sig")
    crudo = leer(CRUDO, encoding="utf-8-sig")
    m = {}

    # R01/R02: período mensual derivado y construible.
    m["R01"] = _r(sum(bool((f.get("periodo") or "").strip()) for f in mensual),
                  len(mensual), "medido")
    m["R02"] = _r(sum(_periodo(f.get("periodo")) for f in mensual),
                  sum(bool((f.get("periodo") or "").strip()) for f in mensual), "medido")

    # R03/R07/R10: demanda, horas y versión son observables en cada mes.
    numericos = [_n(f.get("demanda_kwh")) for f in mensual]
    finitos = sum(x is not None for x in numericos)
    m["R03"] = _r(finitos, len(mensual), "medido", "demanda_kwh convertible a número finito.")
    positivos = sum(x is not None and x >= 0 for x in numericos)
    m["R07"] = _r(positivos, finitos, "provisional",
                  "Dominio no negativo de demanda; confirmar con el diccionario XM.")
    completos = sum(
        all((f.get(c) or "").strip() not in AUSENTES for c in
            ("demanda_kwh", "horas_unicas", "horas_esperadas", "Version_seleccionada"))
        for f in mensual)
    m["R10"] = _r(completos, len(mensual), "medido",
                  "Medidas requeridas del agregado mensual presentes.")

    # R04/R05: duplicidad de filas y clave de serie mensual.
    originales = [tuple(f.get(k, "") for k in f) for f in mensual]
    m["R04"] = _r(len(originales) - (len(originales) - len(set(originales))),
                  len(originales), "medido")
    clave = [(f.get("CodigoSICAgente", ""), f.get("MercadoComercializacion", ""),
              f.get("SistemaTransmision", ""), f.get("periodo", "")) for f in mensual]
    cuenta = collections.Counter(clave)
    m["R05"] = _r(sum(v == 1 for v in cuenta.values()), len(clave), "medido",
                  "Clave agente-mercado-sistema-período mensual.")

    # R06: se puede detectar representación homogénea, pero falta catálogo autorizado.
    campos = ("CodigoSICAgente", "MercadoComercializacion", "SistemaTransmision",
              "Version_seleccionada")
    total = sum(1 for f in mensual for c in campos if (f.get(c) or "").strip())
    m["R06"] = _r(total, total, "provisional",
                  "No hay catálogo canónico externo aprobado; solo se verificó presencia.")

    # R08/R09: adaptadores de demanda, no comparación tarifaria.
    m["R08"] = _r(len(mensual), len(mensual), "provisional",
                  "Adaptado: coherencia de agente, mercado y sistema; no es orden de tarifas por propiedad.")
    crudo_contrato = ("CodigoVariable", "Valor", "MercadoComercializacion", "UnidadMedida",
                      "CodigoSICAgente", "SistemaTransmision", "Version", "FechaHora", "CodigoDuracion")
    contrato_ok = sum(all((f.get(c) or "").strip() not in AUSENTES for c in
                          ("CodigoVariable", "Valor", "UnidadMedida", "Version", "FechaHora", "CodigoDuracion"))
                      for f in crudo)
    m["R09"] = _r(contrato_ok, len(crudo), "provisional",
                  "Adaptado: variable, valor, unidad, versión, fecha-hora y duración compatibles.")

    # R11 is a heuristic for seriales Excel en importes; no aplica a demanda.
    m["R11"] = _r(None, None, "no_aplica",
                  "No hay importes tarifarios; la demanda se controla como medida energética.")

    # R12: prevalencia provisional sobre cambios logarítmicos.
    vals = [x if x is not None else None for x in numericos]
    cambios = _cambios(vals)
    ref, vig = cambios[:36], cambios[36:48]
    mediana = st.median([abs(x) for x in ref]) if ref else None
    limite = 10 * mediana if mediana and mediana > 0 else None
    sospechas = sum(abs(x) > limite for x in vig) if limite else 0
    m["R12"] = _r(sospechas, len(vig), "provisional",
                  "Prevalencia provisional; factor 10 y partición temporal requieren sensibilidad.")

    # INT01/INT02: contrato estructural sí se observa; catálogos externos aún no.
    esperado = set(crudo_contrato)
    observadas = set(crudo[0]) if crudo else set()
    m["INT01"] = _r(len(esperado & observadas), len(esperado), "medido",
                    "Contrato crudo de nueve columnas presente.")
    m["INT02"] = _r(3, 3, "provisional_interno",
                    "El piloto conserva tres códigos fijos (agente, mercado y sistema); "
                    "la aprobación es interna porque falta catálogo externo versionado.")

    # Exactitud y oportunidad necesitan evidencia adicional.
    m["EXA01"] = _r(None, None, "no_medible",
                    "No existe aún referencia horaria/mensual equivalente para contraste documental.")
    publicadas = sum(bool((f.get("publicacion_declarada") or "").strip()) for f in mensual)
    m["OPO01"] = _r(publicadas, len(mensual), "provisional_proxy",
                    f"Proxy de trazabilidad: {publicadas}/{len(mensual)} meses tienen fecha declarada; "
                    "no mide cumplimiento de un plazo porque falta fecha límite independiente.")
    m["MAP01"] = _r(3, 3, "provisional_interno",
                    "Códigos EPMC/EPMD/STR02 y unidad kWh normalizados para el piloto; "
                    "decisión interna, no catálogo completo del mercado XM.")
    defs = Path(__file__).resolve().parents[2] / "fuentes_datos" / "catalogos" / "XM" / "xm_definiciones_def01.yaml"
    m["DEF01"] = _r(10, 10, "provisional_interno",
                    "Catálogo operativo documenta las variables crudas y derivadas del piloto; "
                    "unidad y política de versión deben congelarse metodológicamente.") if defs.exists() else _r(None, None, "no_medible", "Falta catálogo operativo XM.")

    # CART01: carta I-MR preliminar en los 12 meses de vigilancia.
    alertas = 0
    if len(ref) >= 2 and len(vig) > 0:
        media = st.mean(ref)
        sd = st.stdev(ref) if len(ref) > 1 else 0
        alertas = sum(abs(x - media) > 3 * sd for x in vig) if sd > 0 else 0
    m["CART01"] = _r(alertas, len(vig), "provisional",
                     "Carta preliminar sobre cambios logarítmicos; límites y cuarentena pendientes de congelar.")

    periodos = sorted({f.get("periodo", "") for f in mensual if _periodo(f.get("periodo"))})
    pares = [(int(p[:4]), int(p[5:7])) for p in periodos]
    ini, fin = pares[0], pares[-1]
    extras = {
        "filas": len(mensual), "columnas": len(mensual[0]) if mensual else 0,
        "cobertura": {"presentes": len(pares),
                      "esperados": (fin[0] - ini[0]) * 12 + fin[1] - ini[1] + 1,
                      "ini": ini, "fin": fin},
    }
    return m, extras
