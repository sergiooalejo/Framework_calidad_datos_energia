"""Acceso compatible a la CLI vigente en Code/hito5/run.py."""
import sys
from Code.hito5 import run as _implementation

if __name__ == "__main__":
    _implementation.main()
else:
    # Conserva el mismo modulo para consumidores que ajustan ROOT en pruebas.
    sys.modules[__name__] = _implementation
