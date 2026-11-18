"""Acceso compatible; la CLI vigente está en src/framework_calidad/cli.py."""
from pathlib import Path
import sys
_ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'project.json').is_file())
sys.path.insert(0, str(_ROOT / 'src'))
from framework_calidad import cli as _implementation
if __name__ == '__main__':
    _implementation.main()
else:
    sys.modules[__name__] = _implementation
