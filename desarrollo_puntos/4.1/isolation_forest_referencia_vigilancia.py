"""Isolation Forest del Hito 4.1: referencia contra vigilancia.

Esta implementación es independiente de los scripts de Hitos 2 y 3. Lee sus
fuentes originales, reutiliza el constructor de series del Z-score robusto y
escribe todas sus salidas en archivos propios de 4.1.

Protocolo:
* cambios logarítmicos mensuales consecutivos;
* 36 cambios de referencia para entrenar;
* 12 cambios de vigilancia para evaluar;
* Isolation Forest independiente por fuente;
* umbral de referencia en el percentil 99.5 de los puntajes de entrenamiento.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import statistics
from pathlib import Path

import numpy as np
from sklearn.ensemble import IsolationForest

from zscore_robusto import REF_CHANGES, WATCH_CHANGES, build_series, log_changes


HERE = Path(__file__).resolve().parent
SEED = 20261106
N_ESTIMATORS = 300
CONTAMINATION = "auto"
THRESHOLD_QUANTILE = 0.995


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def robust_scale(values: list[float]) -> tuple[float, float]:
    """Return median and a nonzero robust scale for one feature."""
    median = statistics.median(values)
    mad = statistics.median([abs(value - median) for value in values])
    scale = 1.4826 * mad
    if scale == 0:
        deviations = [abs(value - median) for value in values]
        scale = statistics.mean(deviations) if deviations else 1.0
    if scale == 0:
        scale = statistics.pstdev(values) if len(values) > 1 else 1.0
    return median, scale or 1.0


def feature_rows(period_values):
    """Create four features from a series of log changes.

    The feature for change i uses the current change, previous change, their
    absolute difference and the relative log level at the current period.
    The level is normalized with the reference median and is not used to
    define the training/vigilance split.
    """
    periods = sorted(period_values)
    values = [statistics.mean(period_values[period]) for period in periods]
    changes = log_changes(period_values)
    if len(changes) < REF_CHANGES + WATCH_CHANGES:
        return []
    value_by_period = dict(zip(periods, values))
    positive_levels = [value for value in values if value > 0 and math.isfinite(value)]
    if not positive_levels:
        return []
    level_reference = statistics.median(positive_levels[: REF_CHANGES + 1])
    rows = []
    for index, (period, change) in enumerate(changes):
        if index == 0:
            previous_change = 0.0
        else:
            previous_change = changes[index - 1][1]
        current_level = value_by_period.get(period)
        if current_level is None or current_level <= 0:
            continue
        rows.append({
            "period": period,
            "change_log": change,
            "features_raw": [
                change,
                previous_change,
                abs(change - previous_change),
                math.log(current_level / level_reference),
            ],
        })
    if len(rows) < REF_CHANGES + WATCH_CHANGES:
        return []
    scales = [robust_scale([row["features_raw"][j] for row in rows[:REF_CHANGES]]) for j in range(4)]
    for row in rows:
        row["features"] = np.array([
            (row["features_raw"][j] - scales[j][0]) / scales[j][1]
            for j in range(4)
        ], dtype=float)
    return rows[: REF_CHANGES + WATCH_CHANGES]


def write_csv(path: Path, rows: list[dict]) -> None:
    fields = list(rows[0]) if rows else ["fuente"]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--percentil", type=float, default=THRESHOLD_QUANTILE,
                        choices=(0.99, 0.995, 0.9975))
    args = parser.parse_args()

    detail = []
    summary = []
    inputs = {}
    model_info = {}
    for source in ("EPM", "CHEC", "SSPD", "XM"):
        input_path, series = build_series(source)
        input_hash = sha256(input_path)
        inputs[source] = {"ruta": str(input_path), "sha256": input_hash}
        training, evaluation = [], []
        series_rows = {}
        for (key, measure), period_values in sorted(series.items()):
            rows = feature_rows(period_values)
            if not rows:
                continue
            identity = "|".join(key)
            series_id = f"{identity}||{measure}"
            series_rows[series_id] = (key, measure, rows)
            training.extend(row["features"] for row in rows[:REF_CHANGES])
            evaluation.extend((series_id, row) for row in rows[REF_CHANGES:REF_CHANGES + WATCH_CHANGES])
        if not training:
            continue
        model = IsolationForest(n_estimators=N_ESTIMATORS, contamination=CONTAMINATION, random_state=SEED)
        model.fit(np.vstack(training))
        reference_scores = -model.score_samples(np.vstack(training))
        threshold = float(np.quantile(reference_scores, args.percentil))
        model_info[source] = {
            "series_entrenamiento": len(series_rows),
            "observaciones_referencia": len(training),
            "observaciones_vigilancia": len(evaluation),
            "umbral": threshold,
            "percentil_umbral": args.percentil,
        }
        signals = 0
        evaluation_matrix = np.vstack([row["features"] for _, row in evaluation])
        evaluation_scores = -model.score_samples(evaluation_matrix)
        for (series_id, row), score_value in zip(evaluation, evaluation_scores):
            score = float(score_value)
            signal = score > threshold
            signals += int(signal)
            identity, measure = series_id.rsplit("||", 1)
            detail.append({
                "fuente": source,
                "serie": identity,
                "medida": measure,
                "periodo_vigilancia": f"{row['period'][0]:04d}-{row['period'][1]:02d}",
                "clave_alerta_estable": f"{source}:{identity}:{measure}:{row['period'][0]:04d}-{row['period'][1]:02d}",
                "snapshot_sha256": input_hash,
                "cambio_log": f"{row['change_log']:.12g}",
                "puntaje_if": f"{score:.12g}",
                "umbral_referencia": f"{threshold:.12g}",
                "percentil_umbral": f"{args.percentil:.6g}",
                "señal": int(signal),
                "datos_entrenamiento": "referencia_36_cambios",
            })
        summary.append({
            "fuente": source,
            "series_entrenamiento": len(series_rows),
            "observaciones_referencia": len(training),
            "observaciones_vigilancia": len(evaluation),
            "umbral_referencia": f"{threshold:.12g}",
            "percentil_umbral": f"{args.percentil:.6g}",
            "señales_vigilancia": signals,
            "tasa_alerta_vigilancia": f"{signals / len(evaluation):.12g}",
        })

    write_csv(HERE / "isolation_forest_referencia_vigilancia_detalle.csv", detail)
    write_csv(HERE / "isolation_forest_referencia_vigilancia_resumen.csv", summary)
    config = {
        "metodo": "isolation_forest_referencia_vigilancia",
        "semilla": SEED,
        "n_estimators": N_ESTIMATORS,
        "contamination": CONTAMINATION,
        "formula_particion": "36 cambios logarítmicos consecutivos de referencia + 12 de vigilancia",
        "caracteristicas": ["cambio_log_actual", "cambio_log_anterior", "diferencia_absoluta_entre_cambios", "nivel_log_relativo_a_mediana_referencia"],
        "escalamiento": "mediana y MAD robustos calculados dentro de referencia; fallback documentado si escala cero",
        "umbral": "percentil de puntajes de entrenamiento por fuente",
        "percentil_umbral": args.percentil,
        "entrenamiento_solo_referencia": True,
        "evaluacion_solo_vigilancia": True,
        "fuentes": list(inputs),
        "entradas": inputs,
        "modelos": model_info,
    }
    (HERE / "isolation_forest_referencia_vigilancia_configuracion.json").write_text(json.dumps(config, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"fuentes={len(summary)} series={sum(int(row['series_entrenamiento']) for row in summary)} vigilancia={len(detail)} señales={sum(int(row['señales_vigilancia']) for row in summary)}")


if __name__ == "__main__":
    main()
