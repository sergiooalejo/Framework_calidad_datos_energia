"""Resuelve rutas y huellas de ejecuciones anteriores a la migración medallón."""
from pathlib import Path
import hashlib

ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'project.json').is_file())

def historical_path(path, expected=None):
    path = Path(path)
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
        return ROOT / 'Docs/codigo_historico' / relative[len('Code/'):]
    if relative.startswith('Outputs/'):
        suffix = relative[len('Outputs/'):]
        if suffix.startswith('adaptadores/'):
            current = ROOT / 'Data/silver/outputs' / suffix
        else:
            current = ROOT / 'Data/gold/outputs' / suffix
        archived = ROOT / 'Docs/evidencia_historica/outputs' / suffix
        if suffix == 'cuarentena_bootstrap/EPM/cuarentena_registros.csv':
            archived = ROOT / 'Docs/evidencia_historica/cuarentena_epm.csv'
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
