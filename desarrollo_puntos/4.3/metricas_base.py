"""Funciones puras del Hito 4.3: puntajes continuos, tasa de alerta igualada y métricas.

No lee datos ni escribe archivos. Todo lo que aquí se calcula es determinista, de modo que
`test_metricas.py` pueda comprobar sus propiedades sin ejecutar el experimento completo.
"""
from __future__ import annotations

import numpy as np

NORMAL_MEDIAN = 0.6744897501960817
I_COEF = 2.66
MR_COEF = 3.267

# Orden fijo: las posiciones son parte del contrato de las tablas anchas.
METHODS = ('IMR', 'Z_robusto', 'IF', 'LOF', 'KNN', 'R12')
METHOD_LABELS = {
    'IMR': 'Cartas I-MR',
    'Z_robusto': 'Z-score robusto (MAD)',
    'IF': 'Isolation Forest',
    'LOF': 'LOF',
    'KNN': 'KNN (distancia media, k=5)',
    'R12': 'R12 (magnitud del nivel)',
}
ERROR_TYPES = ('decimal_x1000', 'decimal_div1000', 'serial_excel_43577',
               'aumento_10pct', 'valor_no_actualizado', 'otra_medida')


# ---------------------------------------------------------------- escalas y puntajes
def positive_scale(primary: float, reference: np.ndarray) -> float:
    """Escala estrictamente positiva sin añadir un epsilon arbitrario.

    Si la escala principal es cero se usa la desviación absoluta media de la referencia
    y, en último término, su desviación estándar; con una serie constante la escala es 1.
    Es la misma jerarquía de respaldo que 4.2 usa para escalar los rasgos del IF.
    Se necesita aquí únicamente para poder *ordenar* puntajes: la regla nativa de 4.1/4.2
    para MAD=0 (cualquier cambio distinto de la mediana es señal) se verifica aparte.
    """
    if primary > 0:
        return float(primary)
    reference = np.asarray(reference, dtype=float)
    mean_dev = float(np.mean(np.abs(reference - np.median(reference))))
    if mean_dev > 0:
        return mean_dev
    std = float(np.std(reference))
    return std if std > 0 else 1.0


def imr_score(current, previous, mean, mr_scale):
    """Puntaje I-MR: supera 1 exactamente cuando la carta I o la carta MR señalan."""
    current, previous = np.asarray(current, float), np.asarray(previous, float)
    return np.maximum(np.abs(current - mean) / (I_COEF * mr_scale),
                      np.abs(current - previous) / (MR_COEF * mr_scale))


def robust_z_score(current, median, sigma):
    """|z| robusto con sigma = MAD / 0,6745; la señal clásica es |z| > 3."""
    return np.abs(np.asarray(current, float) - median) / sigma


def level_ratio_score(level, level_reference):
    """R12: |nivel| / mediana de referencia; el factor 5, 10 o 20 es el umbral."""
    return np.abs(np.asarray(level, float)) / level_reference


# ------------------------------------------------------------------ tasa igualada
def threshold_for_rate(scores, rate: float) -> float:
    """Umbral tal que `puntaje > umbral` produce a lo sumo `rate` de alertas.

    Con empates en la frontera la tasa observada puede quedar por debajo de la objetivo;
    quien llame debe reportar la tasa observada, no solo la objetivo. Con k = 0 alertas
    esperadas el umbral es el máximo (ninguna alerta); con rate >= 1 nada se excluye.
    """
    ordered = np.sort(np.asarray(scores, float).ravel())[::-1]
    k = int(np.floor(rate * len(ordered) + 1e-9))
    if k >= len(ordered):
        return -np.inf
    return float(ordered[k])


def observed_rate(scores, threshold: float) -> float:
    scores = np.asarray(scores, float)
    return float(np.mean(scores > threshold)) if scores.size else float('nan')


# ---------------------------------------------------------------------- métricas
def precision_at_prevalence(tpr, fpr, prevalence):
    """Precisión esperada si una fracción `prevalence` de las observaciones tiene error.

    Recall y tasa de falsas alertas no dependen de la prevalencia; la precisión sí. En
    lugar de fijar una prevalencia artificial (en el experimento la prevalencia la decide
    el diseño de las inyecciones) se reporta para varias prevalencias supuestas.
    """
    tpr, fpr = np.asarray(tpr, float), np.asarray(fpr, float)
    denominator = tpr * prevalence + fpr * (1.0 - prevalence)
    with np.errstate(divide='ignore', invalid='ignore'):
        return np.where(denominator > 0, tpr * prevalence / denominator, np.nan)


def f1_score(precision, recall):
    precision, recall = np.asarray(precision, float), np.asarray(recall, float)
    denominator = precision + recall
    with np.errstate(divide='ignore', invalid='ignore'):
        return np.where(denominator > 0, 2 * precision * recall / denominator, np.nan)


# ------------------------------------------------------- sorteo sin reemplazo
def draw_distinct_origins(case_matrix: np.ndarray, k: int, replicates: int,
                          rng: np.random.Generator):
    """Sortea, para cada réplica y serie, `k` meses de origen distintos y un tipo por mes.

    `case_matrix[serie, origen, tipo]` contiene el índice del caso o -1 si no existe. Los
    meses se eligen sin reemplazo (ordenando claves aleatorias) y el tipo de error se elige
    uniformemente entre los disponibles de ese mes. Devuelve (índices, válido) con forma
    (réplicas, series, k); `válido` es falso cuando la serie no tiene k meses disponibles.
    """
    n_series, n_origins, n_types = case_matrix.shape
    available_origin = (case_matrix >= 0).any(axis=2)
    keys = rng.random((replicates, n_series, n_origins))
    keys[:, ~available_origin] = np.inf
    chosen = np.argsort(keys, axis=2)[:, :, :k]
    series_index = np.arange(n_series)[None, :, None]
    valid = np.take_along_axis(np.broadcast_to(available_origin, keys.shape), chosen, axis=2)
    type_keys = rng.random((replicates, n_series, k, n_types))
    type_keys[~(case_matrix[series_index, chosen] >= 0)] = np.inf
    chosen_type = np.argmin(type_keys, axis=3)
    indices = case_matrix[series_index, chosen, chosen_type]
    valid &= indices >= 0
    return np.where(valid, indices, 0), valid, chosen
