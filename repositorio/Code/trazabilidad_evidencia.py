"""Resuelve rutas migradas y verifica evidencia anterior sin reescribir manifiestos."""
from pathlib import Path
import hashlib
import json
import zipfile


def _layout(root):
    path = Path(root) / 'configs/mapa_codigo.json'
    return json.loads(path.read_text(encoding='utf-8')) if path.is_file() else {'files': {}}


def _relative(root, name):
    root = Path(root).resolve()
    path = Path(str(name).replace('\\', '/'))
    if path.is_absolute():
        return path.resolve().relative_to(root).as_posix()
    candidate = (root / path).resolve()
    return candidate.relative_to(root).as_posix()


def resolve_current_path(root, name):
    try:
        relative = _relative(root, name)
    except ValueError:
        return Path(name)
    row = _layout(root)['files'].get(relative)
    layout_path = Path(root) / 'configs/mapa_estructura.json'
    project = json.loads(layout_path.read_text(encoding='utf-8')) if layout_path.is_file() else {}
    current = row['current'] if row else project.get('files', {}).get(relative, relative)
    seen = set()
    while current not in seen:
        seen.add(current)
        moved = project.get('files', {}).get(current, current)
        if moved == current:
            for old, new in sorted(project.get('prefixes', {}).items(), key=lambda item: len(item[0]), reverse=True):
                if current == old or current.startswith(old + '/'):
                    moved = new + current[len(old):]
                    break
        if moved == current:
            break
        current = moved
    return Path(root) / current


def evidence_digest(root, name, expected=None):
    relative = _relative(root, name)
    direct = resolve_current_path(root, relative)
    if direct.is_file():
        actual = hashlib.sha256(direct.read_bytes()).hexdigest()
        if expected is None or actual == expected:
            return actual
    layout = _layout(root)
    row = layout['files'].get(relative)
    if row and expected == row['original_sha256']:
        current = Path(root) / row['current']
        if not current.is_file() or hashlib.sha256(current.read_bytes()).hexdigest() != row['current_sha256']:
            return None
        with zipfile.ZipFile(Path(root) / layout['archive']) as archive:
            return hashlib.sha256(archive.read(relative)).hexdigest()
    return hashlib.sha256(direct.read_bytes()).hexdigest() if direct.is_file() else None


def matches_evidence(root, name, expected):
    return evidence_digest(root, name, expected) == expected
