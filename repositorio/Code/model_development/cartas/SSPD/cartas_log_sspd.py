"""Entrada compatible al protocolo corregido del Hito 3."""
from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'configs/proyecto.json').is_file())
sys.path.insert(0, str(ROOT))
from Code.data_quality.operaciones_calidad import cards

if __name__ == "__main__":
    cards('SSPD')
