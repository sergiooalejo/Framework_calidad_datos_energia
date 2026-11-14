"""OPO01: disponibilidad frente al plazo, con evidencia local verificable."""
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

from .core import ROOT, digest, read_csv


def instant(value, zone):
    if not value:
        return None
    result = datetime.fromisoformat(value.replace('Z', '+00:00'))
    if 'T' not in value and ' ' not in value:
        raise ValueError('Se requiere hora para evaluar el plazo, no solo fecha')
    if result.tzinfo is None:
        result = result.replace(tzinfo=ZoneInfo(zone))
    return result


def classify(row):
    if row.get('estado_evidencia') != 'verificada' or not row.get('revisor'):
        return 'pendiente', 'Evidencia y revisor pendientes'
    if not row.get('fundamento_plazo_url') or not row.get('consumidor'):
        return 'pendiente', 'Falta fundamento del plazo o consumidor'
    path = (ROOT / row.get('archivo_evidencia', '')).resolve()
    if not path.is_relative_to(ROOT.resolve()) or not path.is_file() or digest(path) != row.get('sha256_evidencia'):
        return 'pendiente', 'Evidencia local inexistente, fuera del repositorio o con hash distinto'
    try:
        zone = row.get('zona_horaria') or 'America/Bogota'
        deadline = instant(row.get('fecha_limite', ''), zone)
        exact = instant(row.get('disponible_desde_exacto', ''), zone)
        absent = instant(row.get('observado_ausente_hasta', ''), zone)
        present = instant(row.get('observado_presente_desde', ''), zone)
        if deadline is None:
            return 'pendiente', 'No se ha acreditado fecha limite'
        if exact:
            return ('a_tiempo', '') if exact <= deadline else ('tardia', '')
        if absent and present and absent >= present:
            return 'pendiente', 'Intervalo temporal incoherente'
        if present and present <= deadline:
            return 'a_tiempo', 'Disponible antes del plazo'
        if absent and absent >= deadline:
            return 'tardia', 'Ausencia acreditada al vencer el plazo'
        return 'indeterminada', 'El intervalo de observacion no permite resolver el plazo'
    except (ValueError, KeyError) as exc:
        return 'pendiente', str(exc)


def measure(dataset, path=None):
    path = path or ROOT / 'Data/gold/outputs/calidad/plantilla_oportunidad.csv'
    rows = [r for r in read_csv(path) if r.get('dataset_id') == dataset]
    seen = set()
    classified = []
    for row in rows:
        identity = tuple(row.get(k, '') for k in ('publicacion_id', 'periodo', 'version'))
        if not all(identity) or identity in seen:
            raise ValueError('Identidad de publicación ausente o duplicada en OPO01')
        seen.add(identity)
        state, note = classify(row)
        classified.append(dict(row, clasificacion_calculada=state, motivo_calculado=note))
    count = sum(r['clasificacion_calculada'] == 'a_tiempo' for r in classified)
    evaluable = sum(r['clasificacion_calculada'] in ('a_tiempo', 'tardia') for r in classified)
    return dict(numerador=count if evaluable else None, denominador=evaluable or None,
                valor=100*count/evaluable if evaluable else None,
                estado='provisional' if evaluable else 'no_medible',
                nota=f'OPO01 con evidencia temporal: {evaluable}/{len(rows)} publicaciones registradas evaluables. '
                     'Sin inventario completo de publicaciones esperadas no acredita toda la dimension. '
                     'La presencia de meses o la fecha de descarga no sustituyen disponibilidad y plazo.'), classified
