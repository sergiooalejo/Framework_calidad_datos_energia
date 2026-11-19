"""Perfilamiento descriptivo desacoplado de los scripts de cada fuente."""

import pandas as pd


def perfilar_dataframe(df: pd.DataFrame, columnas: list[str] | None = None) -> pd.DataFrame:
    """Calcula conteo, nulos, únicos y tipo para cada columna seleccionada."""
    selected = columnas or list(df.columns)
    missing = sorted(set(selected) - set(df.columns))
    if missing:
        raise KeyError(f"Columnas inexistentes: {missing}")
    rows = []
    for column in selected:
        series = df[column]
        rows.append(
            {
                "columna": column,
                "tipo": str(series.dtype),
                "filas": int(len(series)),
                "nulos": int(series.isna().sum()),
                "porcentaje_nulos": float(series.isna().mean() * 100),
                "unicos": int(series.nunique(dropna=True)),
            }
        )
    return pd.DataFrame(rows)

