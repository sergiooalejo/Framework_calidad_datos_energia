"""API reutilizable del framework de calidad de datos energéticos."""

# Compatibilidad con PYTHONPATH=Code; la implementacion vive en Hito 5.
from pathlib import Path
__path__ = [str(Path(__file__).resolve().parents[1] / "hito5/framework_calidad")]

from .io import cargar_csv, resumen_dataframe
from .profiling import perfilar_dataframe
from .rules import evaluar_regla
from .reporting import escribir_csv
from .config import cargar_configuracion, listar_indicadores

__all__ = [
    "cargar_csv",
    "resumen_dataframe",
    "perfilar_dataframe",
    "evaluar_regla",
    "escribir_csv",
    "cargar_configuracion",
    "listar_indicadores",
]

