"""Entrada y salida controlada para datasets y resultados."""

from pathlib import Path
from typing import Iterable

import pandas as pd


def cargar_csv(ruta: str | Path, *, encoding: str = "utf-8-sig") -> pd.DataFrame:
    """Carga un CSV sin modificarlo y entrega un DataFrame independiente."""
    path = Path(ruta)
    if not path.exists():
        raise FileNotFoundError(f"No existe el archivo: {path}")
    return pd.read_csv(path, encoding=encoding, low_memory=False)


def resumen_dataframe(df: pd.DataFrame) -> dict[str, int]:
    """Devuelve metadatos básicos, útiles para trazabilidad y perfilamiento."""
    return {
        "filas": int(df.shape[0]),
        "columnas": int(df.shape[1]),
        "nulos": int(df.isna().sum().sum()),
        "duplicados": int(df.duplicated().sum()),
    }

