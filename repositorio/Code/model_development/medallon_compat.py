"""Resuelve rutas y huellas de ejecuciones anteriores a la migración medallón."""
from pathlib import Path
import hashlib

ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'configs/proyecto.json').is_file())

def historical_path(path, expected=None):
    path = Path(path)
    try:
        relative_now = path.relative_to(ROOT).as_posix()
    except ValueError:
        relative_now = ''
    if relative_now.startswith(('Data/', 'Docs/', 'z_findings/')):
        import sys
        sys.path.insert(0, str(ROOT))
        from Code.trazabilidad_evidencia import resolve_current_path
        path = resolve_current_path(ROOT, path)
    if expected and path.is_file():
        with path.open('rb') as stream:
            actual = hashlib.file_digest(stream, 'sha256').hexdigest()
        if actual == expected:
            return path
    try:
        relative = path.relative_to(ROOT).as_posix()
    except ValueError:
        return path
    if relative.startswith('Code/'):
        return ROOT / 'Docs/archive/code' / relative[len('Code/'):]
    if relative.startswith('Outputs/'):
        suffix = relative[len('Outputs/'):]
        if suffix.startswith('adaptadores/'):
            current = ROOT / 'z_findings/preparation' / suffix
        else:
            current = ROOT / 'z_findings/results' / suffix
        archived = ROOT / 'z_findings/archive/evidence/outputs' / suffix
        if suffix == 'cuarentena_bootstrap/EPM/cuarentena_registros.csv':
            archived = ROOT / 'z_findings/archive/evidence/cuarentena_epm.csv'
        if expected and current.is_file():
            with current.open('rb') as stream:
                if hashlib.file_digest(stream, 'sha256').hexdigest() == expected:
                    return current
        if expected and archived.is_file():
            with archived.open('rb') as stream:
                if hashlib.file_digest(stream, 'sha256').hexdigest() == expected:
                    return archived
        return current
    if relative.startswith('Data/datos/'):
        suffix = relative[len('Data/datos/'):]
        derived = suffix.endswith(('sspd_ebby-cjha_mensual.csv', 'xm_demanda_mensual_piloto.csv'))
        derived = derived or suffix.startswith('Datos_en_revision/sspd_bnkp-xdb7')
        layer = 'silver' if derived else 'bronze'
        return ROOT / 'Data' / layer / 'datos' / suffix
    return path
