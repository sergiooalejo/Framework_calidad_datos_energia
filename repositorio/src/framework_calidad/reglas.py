"""Evaluación mínima de reglas declarativas sobre columnas."""

from collections.abc import Callable

import pandas as pd


def evaluar_regla(
    df: pd.DataFrame,
    columna: str,
    regla: Callable[[pd.Series], pd.Series],
    *,
    regla_id: str = "regla_sin_id",
) -> dict[str, object]:
    """Evalúa una función booleana y devuelve un resultado auditable."""
    if columna not in df.columns:
        raise KeyError(f"Columna inexistente: {columna}")
    resultado = regla(df[columna]).fillna(False).astype(bool)
    return {
        "regla_id": regla_id,
        "columna": columna,
        "filas_evaluadas": int(len(resultado)),
        "filas_cumplen": int(resultado.sum()),
        "filas_no_cumplen": int((~resultado).sum()),
        "porcentaje_cumplimiento": float(resultado.mean() * 100) if len(resultado) else 0.0,
    }

