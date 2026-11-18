"""Persistencia de resultados con creación explícita de directorios."""

from pathlib import Path

import pandas as pd


def escribir_csv(df: pd.DataFrame, ruta: str | Path) -> Path:
    """Escribe un resultado CSV y devuelve la ruta creada."""
    path = Path(ruta)
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False, encoding="utf-8-sig")
    return path

