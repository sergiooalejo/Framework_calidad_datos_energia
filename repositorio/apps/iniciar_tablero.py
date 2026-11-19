"""Acceso compatible al tablero de apps/tablero_streamlit.py."""
from pathlib import Path
import runpy
_ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'configs/proyecto.json').is_file())
runpy.run_path(str(_ROOT / 'apps/tablero_streamlit.py'), run_name='__main__')
