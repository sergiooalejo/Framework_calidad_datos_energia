"""Contratos comunes para detectores de anomalías del framework."""

from collections.abc import Callable

import pandas as pd


def aplicar_detector(df: pd.DataFrame, detector: Callable[[pd.DataFrame], pd.Series]) -> pd.Series:
    """Ejecuta un detector y valida que entregue una etiqueta por fila."""
    labels = detector(df)
    if len(labels) != len(df):
        raise ValueError("El detector debe devolver una etiqueta por cada fila")
    return pd.Series(labels, index=df.index, name="anomalia")

