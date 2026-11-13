"""Z-score robusto sobre cambios logarítmicos para Hito 4.1, viñeta 1."""
from __future__ import annotations

from pathlib import Path as _ProjectPath
_PROJECT_ROOT = next(p for p in _ProjectPath(__file__).resolve().parents if (p / "project.json").is_file())

import argparse
import csv
import hashlib
import json
import math
import statistics
from pathlib import Path

HERE = (_PROJECT_ROOT / 'Data/gold/outputs/detectores')
ROOT = _PROJECT_ROOT
REF_CHANGES = 36
WATCH_CHANGES = 12
CONSISTENCY = 0.6744897501960817


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def median_abs_deviation(values: list[float]) -> tuple[float, float]:
    median = statistics.median(values)
    return median, statistics.median([abs(value - median) for value in values])


def row_hash(row: dict[str, str]) -> str:
    payload = json.dumps(row, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def log_changes(period_values: dict[tuple[int, int], list[float]]) -> list[tuple[tuple[int, int], float]]:
    periods = sorted(period_values)
    values = [statistics.mean(period_values[period]) for period in periods]
    changes = []
    for previous_period, period, previous, current in zip(periods, periods[1:], values, values[1:]):
        consecutive = period[0] * 12 + period[1] == previous_period[0] * 12 + previous_period[1] + 1
        if consecutive and previous > 0 and current > 0 and math.isfinite(previous) and math.isfinite(current):
            changes.append((period, math.log(current) - math.log(previous)))
    return changes


def build_series(source: str):
    """Reuse the source, series keys and measures from the Hito 3 cards."""
    if source == "EPM":
        path = (_PROJECT_ROOT / 'Data/bronze/datos/Datos_seleccionados/EPM/epm_sfcd-b3ey.csv')
        rows = read_csv(path)
        months = {name: number for number, name in enumerate(("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"), 1)}
        cats = ("tipodeinformacion", "tipodetarifa", "tipodedato", "rangodeconsumo", "nivel")
        measures = ("propiedadepm", "compartido", "propiedaddelcliente", "punta", "fueradepunta")
        quarantine_file = (_PROJECT_ROOT / 'Data/gold/outputs/cuarentena_bootstrap/EPM/cuarentena_registros.csv')
        quarantined = {row["clave_contenido"] for row in read_csv(quarantine_file)} if quarantine_file.exists() else set()
        series = {}
        for row in rows:
            if row_hash(row) in quarantined or not row.get("year") or row.get("mes") not in months:
                continue
            period = (int(row["year"]), months[row["mes"]])
            key = tuple(row.get(column, "") for column in cats)
            for measure in measures:
                try:
                    value = float(row[measure])
                except (KeyError, TypeError, ValueError):
                    continue
                if value > 0 and math.isfinite(value):
                    series.setdefault((key, measure), {}).setdefault(period, []).append(value)
        return path, series

    if source == "CHEC":
        path = (_PROJECT_ROOT / 'Data/bronze/datos/Datos_seleccionados/CHEC/chec_c698-wqig.csv')
        rows = read_csv(path)
        cats = ("comercializador_codigo", "mercado_codigo", "costounitariotarifa_tipomed", "nivel_tension_codigo", "modalidadcobro_propiedad", "claseservicio_codigo", "costounitariotarifa_rangoconsumo", "costounitariotarifa_tipomercado")
        measures = ("costounitariotarifa_cu", "costounitariotarifa_valor_tarifa")
        series = {}
        for row in rows:
            try:
                period = (int(row["costounitariotarifa_ano"]), int(row["costounitariotarifa_mes"]))
            except (KeyError, TypeError, ValueError):
                continue
            key = tuple(row.get(column, "") for column in cats)
            for measure in measures:
                try:
                    value = float(row[measure])
                except (KeyError, TypeError, ValueError):
                    continue
                if value > 0 and math.isfinite(value):
                    series.setdefault((key, measure), {}).setdefault(period, []).append(value)
        return path, series

    if source == "SSPD":
        path = (_PROJECT_ROOT / 'Data/silver/datos/Datos_seleccionados/SSPD/sspd_ebby-cjha_mensual.csv')
        rows = read_csv(path)
        cats = ("identificador_empresa", "estrato_sector", "ubicacion", "tipo_conexion", "tipo_lectura", "tipo_factura")
        measures = ("consumo_basico_sum", "consumo_compl_sum", "consumo_mayor800_sum", "valor_total_sum")
        series = {}
        for row in rows:
            try:
                period = (int(row["anio"]), int(row["periodo"]))
            except (KeyError, TypeError, ValueError):
                continue
            key = tuple(row.get(column, "") for column in cats)
            for measure in measures:
                try:
                    value = float(row[measure])
                except (KeyError, TypeError, ValueError):
                    continue
                if value > 0 and math.isfinite(value):
                    series.setdefault((key, measure), {}).setdefault(period, []).append(value)
        return path, series

    if source == "XM":
        path = (_PROJECT_ROOT / 'Data/silver/datos/Datos_seleccionados/XM_piloto/xm_demanda_mensual_piloto.csv')
        rows = read_csv(path)
        series = {}
        for row in sorted(rows, key=lambda item: item["periodo"]):
            try:
                year, month = (int(part) for part in row["periodo"].split("-"))
                value = float(row["demanda_kwh"])
            except (KeyError, TypeError, ValueError):
                continue
            if value > 0 and math.isfinite(value):
                series.setdefault((("EPMC|EPMD|STR02",), "demanda_kwh"), {}).setdefault((year, month), []).append(value)
        return path, series

    raise ValueError(f"Fuente no soportada: {source}")


def evaluate(source: str, threshold: float):
    input_path, series = build_series(source)
    input_hash = sha256(input_path)
    detail, summary = [], []
    for (key, measure), period_values in sorted(series.items()):
        changes = log_changes(period_values)
        if len(changes) < REF_CHANGES + WATCH_CHANGES:
            continue
        reference = [value for _, value in changes[:REF_CHANGES]]
        surveillance = changes[REF_CHANGES:REF_CHANGES + WATCH_CHANGES]
        median, mad = median_abs_deviation(reference)
        signals = 0
        for period, change in surveillance:
            if mad == 0:
                z_value = None
                signal = change != median
                scale_status = "mad_cero"
            else:
                z_value = CONSISTENCY * (change - median) / mad
                signal = abs(z_value) > threshold
                scale_status = "mad_positivo"
            signals += int(signal)
            identity = "|".join(key)
            detail.append({"fuente": source, "serie": identity, "medida": measure, "periodo_vigilancia": f"{period[0]:04d}-{period[1]:02d}", "clave_alerta_estable": f"{source}:{identity}:{measure}:{period[0]:04d}-{period[1]:02d}", "snapshot_sha256": input_hash, "cambio_log": f"{change:.12g}", "mediana_referencia": f"{median:.12g}", "mad_referencia": f"{mad:.12g}", "z_robusto": "" if z_value is None else f"{z_value:.12g}", "umbral": f"{threshold:.12g}", "señal": int(signal), "estado_escala": scale_status})
        summary.append({"fuente": source, "serie": "|".join(key), "medida": measure, "periodos_disponibles": len(period_values), "cambios_referencia": REF_CHANGES, "cambios_vigilancia": len(surveillance), "mediana_referencia": f"{median:.12g}", "mad_referencia": f"{mad:.12g}", "umbral": f"{threshold:.12g}", "señales": signals, "tasa_alerta_vigilancia": f"{signals / len(surveillance):.12g}", "estado_escala": "mad_cero" if mad == 0 else "mad_positivo"})
    return detail, summary, input_path


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    fields = list(rows[0]) if rows else ["fuente"]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--umbral", type=float, default=3.267, choices=(2.66, 3.0, 3.267))
    args = parser.parse_args()
    details, summaries, inputs = [], [], {}
    for source in ("EPM", "CHEC", "SSPD", "XM"):
        detail, summary, input_path = evaluate(source, args.umbral)
        details.extend(detail)
        summaries.extend(summary)
        inputs[source] = {"ruta": str(input_path), "sha256": sha256(input_path)}
    write_csv((_PROJECT_ROOT / 'Data/gold/outputs/detectores/zscore_robusto_detalle.csv'), details)
    write_csv((_PROJECT_ROOT / 'Data/gold/outputs/detectores/zscore_robusto_resumen.csv'), summaries)
    config = {"metodo": "zscore_robusto_logaritmico", "formula": "0.6744897501960817 * (cambio_log - mediana_referencia) / MAD_referencia", "umbral": args.umbral, "cambios_referencia": REF_CHANGES, "cambios_vigilancia": WATCH_CHANGES, "fuentes": list(inputs), "entradas": inputs, "cuarentena_epm_aplicada": True, "mad_cero": "señal si el cambio es distinto de la mediana; z_robusto queda vacío"}
    ((_PROJECT_ROOT / 'Data/gold/outputs/detectores/configuracion.json')).write_text(json.dumps(config, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"series={len(summaries)} observaciones_vigilancia={len(details)} señales={sum(int(row['señales']) for row in summaries)}")


if __name__ == "__main__":
    main()
