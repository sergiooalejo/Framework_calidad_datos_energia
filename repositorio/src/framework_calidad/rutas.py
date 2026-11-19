"""Localización explícita del checkout que contiene datos y protocolos."""
from pathlib import Path
import os


def project_root(required=True):
    configured = os.environ.get('FRAMEWORK_ENERGIA_ROOT')
    if configured:
        root = Path(configured).expanduser().resolve()
        if not (root / 'configs/proyecto.json').is_file():
            raise FileNotFoundError(f'FRAMEWORK_ENERGIA_ROOT no contiene configs/proyecto.json: {root}')
        return root
    for origin in (Path(__file__).resolve().parent, Path.cwd()):
        for candidate in (origin, *origin.parents):
            if (candidate / 'configs/proyecto.json').is_file():
                return candidate
            nested = candidate / 'repositorio'
            if (nested / 'configs/proyecto.json').is_file():
                return nested
    if required:
        raise FileNotFoundError('Ejecute desde repositorio/ o defina FRAMEWORK_ENERGIA_ROOT.')
    return Path.cwd()
