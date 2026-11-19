"""Acceso compatible al generador vigente en Code/external_validation/."""
from pathlib import Path
import sys

ROOT = next(p for p in Path(__file__).resolve().parents if (p / "configs/proyecto.json").is_file())
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
from Code.external_validation.generar_muestra_alertas import main

if __name__ == "__main__":
    main()
