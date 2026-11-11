"""API reutilizable del framework de calidad de datos energéticos."""

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

