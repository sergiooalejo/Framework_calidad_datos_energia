"""Entrada compatible al protocolo corregido del Hito 3."""
from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'project.json').is_file())
sys.path.insert(0, str(ROOT))
from Code.hito3.entry import review_epm

if __name__ == "__main__":
    review_epm()
