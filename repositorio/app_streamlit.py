"""Acceso compatible al tablero de apps/streamlit_app.py."""
from pathlib import Path
import runpy
_ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'project.json').is_file())
runpy.run_path(str(_ROOT / 'apps/streamlit_app.py'), run_name='__main__')
