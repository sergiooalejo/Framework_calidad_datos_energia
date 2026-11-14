"""Acceso compatible al tablero vigente en Code/hito5/app_streamlit.py."""
from pathlib import Path
import runpy

runpy.run_path(str(Path(__file__).resolve().parent / "Code/hito5/app_streamlit.py"), run_name="__main__")
