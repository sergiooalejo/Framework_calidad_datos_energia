"""Carga de configuraciones YAML de reglas sin ejecutar lógica implícita."""

from pathlib import Path
from typing import Any

import yaml


def cargar_configuracion(ruta: str | Path) -> dict[str, Any]:
    """Carga una configuración YAML y exige que su raíz sea un objeto."""
    path = Path(ruta)
    if not path.exists():
        raise FileNotFoundError(f"No existe la configuración: {path}")
    with path.open("r", encoding="utf-8") as stream:
        content = yaml.safe_load(stream) or {}
    if not isinstance(content, dict):
        raise ValueError("La configuración YAML debe tener una raíz tipo objeto")
    return content


def listar_indicadores(configuracion: dict[str, Any]) -> list[dict[str, Any]]:
    """Devuelve los indicadores declarados, sin interpretar sus umbrales."""
    indicadores = configuracion.get("indicadores", [])
    if not isinstance(indicadores, list):
        raise ValueError("La clave 'indicadores' debe ser una lista")
    return indicadores

