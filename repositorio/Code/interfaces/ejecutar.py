"""Acceso compatible; la CLI vigente está en src/framework_calidad/consola.py."""
from pathlib import Path
import sys
_ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'configs/proyecto.json').is_file())
sys.path.insert(0, str(_ROOT / 'src'))
from framework_calidad import consola as _implementation
if __name__ == '__main__':
    _implementation.main()
else:
    sys.modules[__name__] = _implementation
