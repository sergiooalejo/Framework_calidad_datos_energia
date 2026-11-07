"""Calibra Z-score robusto e Isolation Forest por validación cruzada.

El objetivo es aproximar la tasa de alerta de las cartas logarítmicas del Hito 3
sin usar los 12 meses de vigilancia para elegir el umbral. Las series se
reparten en cinco grupos; cada umbral se calcula con las series de referencia
que no pertenecen al grupo evaluado.
"""
from __future__ import annotations

import csv
import json
import statistics
from pathlib import Path

import numpy as np
from sklearn.ensemble import IsolationForest

from isolation_forest_referencia_vigilancia import SEED, feature_rows
from zscore_robusto import build_series, REF_CHANGES, WATCH_CHANGES

HERE = Path(__file__).resolve().parent
K = 5
N_ESTIMATORS = 200


def target_rate(source: str) -> float:
    cards = {
        "EPM": (48, 720),
        "CHEC": (37, 3312),
        "SSPD": (143, 4332),
        "XM": (0, 12),
    }
    numerator, denominator = cards[source]
    return numerator / denominator if denominator else 0.0


def z_values(rows):
    ref = [row["change_log"] for row in rows[:REF_CHANGES]]
    median = statistics.median(ref)
    mad = statistics.median([abs(value - median) for value in ref])
    if mad == 0:
        return [float("inf") if row["change_log"] != median else 0.0 for row in rows]
    return [0.6744897501960817 * (row["change_log"] - median) / mad for row in rows]


def write_csv(path, rows):
    fields = list(rows[0]) if rows else ["fuente"]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def main():
    output = []
    for source in ("EPM", "CHEC", "SSPD", "XM"):
        _, raw_series = build_series(source)
        series = {}
        for (key, measure), period_values in sorted(raw_series.items()):
            rows = feature_rows(period_values)
            if rows:
                series[f"{'|'.join(key)}||{measure}"] = rows
        ids = sorted(series)
        groups = {series_id: index % K for index, series_id in enumerate(ids)}
        rate = target_rate(source)
        if len(ids) < 2:
            for method in ("isolation_forest", "zscore_robusto"):
                output.append({"fuente": source, "metodo": method, "fold": "no_calibrable", "tasa_objetivo_cartas": rate, "umbral": "", "series_entrenamiento": 0, "series_evaluacion": len(ids), "observaciones_vigilancia": len(ids) * WATCH_CHANGES, "señales_vigilancia": "", "tasa_observada": ""})
            continue
        for fold in range(K):
            training_ids = [series_id for series_id in ids if groups[series_id] != fold]
            test_ids = [series_id for series_id in ids if groups[series_id] == fold]
            if not test_ids:
                continue
            train_features = np.vstack([row["features"] for series_id in training_ids for row in series[series_id][:REF_CHANGES]])
            model = IsolationForest(n_estimators=N_ESTIMATORS, contamination="auto", random_state=SEED + fold)
            model.fit(train_features)
            train_scores = -model.score_samples(train_features)
            if rate == 0:
                if_threshold = float("inf")
            else:
                if_threshold = float(np.quantile(train_scores, 1 - rate))
            test_features = np.vstack([row["features"] for series_id in test_ids for row in series[series_id][REF_CHANGES:REF_CHANGES + WATCH_CHANGES]])
            test_scores = -model.score_samples(test_features)
            if_signals = int(np.sum(test_scores > if_threshold))

            train_z = np.concatenate([np.abs(z_values(series[series_id]))[:REF_CHANGES] for series_id in training_ids])
            z_threshold = float("inf") if rate == 0 else float(np.quantile(train_z, 1 - rate))
            test_z = np.concatenate([np.abs(z_values(series[series_id]))[REF_CHANGES:REF_CHANGES + WATCH_CHANGES] for series_id in test_ids])
            z_signals = int(np.sum(test_z > z_threshold))
            observations = len(test_z)
            output.extend([
                {"fuente": source, "metodo": "isolation_forest", "fold": fold, "tasa_objetivo_cartas": rate, "umbral": if_threshold, "series_entrenamiento": len(training_ids), "series_evaluacion": len(test_ids), "observaciones_vigilancia": observations, "señales_vigilancia": if_signals, "tasa_observada": if_signals / observations},
                {"fuente": source, "metodo": "zscore_robusto", "fold": fold, "tasa_objetivo_cartas": rate, "umbral": z_threshold, "series_entrenamiento": len(training_ids), "series_evaluacion": len(test_ids), "observaciones_vigilancia": observations, "señales_vigilancia": z_signals, "tasa_observada": z_signals / observations},
            ])
    write_csv(HERE / "calibracion_cv_tasa_igualada.csv", output)
    config = {"grupos": K, "metodo_tasa_objetivo": "tasa de señales de cartas Hito 3", "no_usa_vigilancia_para_umbral": True, "fuentes": ["EPM", "CHEC", "SSPD", "XM"], "nota": "XM tiene tasa objetivo cero; el umbral queda infinito y no se esperan señales."}
    (HERE / "calibracion_cv_tasa_igualada_configuracion.json").write_text(json.dumps(config, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"filas={len(output)} archivo=calibracion_cv_tasa_igualada.csv")


if __name__ == "__main__":
    main()
