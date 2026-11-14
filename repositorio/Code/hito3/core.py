"""Contratos de fuentes, identidad y cartas I-MR sin interpolación.

No escribe al importar. El calendario se fija antes de excluir valores; una
cuarentena no desplaza una observación de vigilancia a la referencia.
"""
from __future__ import annotations

from collections import Counter, defaultdict
import csv
import hashlib
import io
import json
import math
from pathlib import Path
import random
import statistics as st
import zipfile

ROOT = Path(__file__).resolve().parents[2]
MONTHS = dict(zip(('Enero Febrero Marzo Abril Mayo Junio Julio Agosto Septiembre '
                   'Octubre Noviembre Diciembre').split(), range(1, 13)))
SOURCES = {
    'EPM': dict(dataset='sfcd-b3ey', path='Data/bronze/datos/Datos_seleccionados/EPM/epm_sfcd-b3ey.csv',
                period=('year', 'mes'), categories=('tipodeinformacion', 'tipodetarifa', 'tipodedato', 'rangodeconsumo', 'nivel'),
                measures=('propiedadepm', 'compartido', 'propiedaddelcliente', 'punta', 'fueradepunta')),
    'CHEC': dict(dataset='c698-wqig', path='Data/bronze/datos/Datos_seleccionados/CHEC/chec_c698-wqig.csv',
                period=('costounitariotarifa_ano', 'costounitariotarifa_mes'),
                categories=('comercializador_codigo', 'mercado_codigo', 'costounitariotarifa_tipomed', 'nivel_tension_codigo',
                            'modalidadcobro_propiedad', 'claseservicio_codigo', 'costounitariotarifa_rangoconsumo', 'costounitariotarifa_tipomercado'),
                measures=('costounitariotarifa_cu', 'costounitariotarifa_valor_tarifa')),
    'SSPD': dict(dataset='ebby-cjha', path='Data/silver/datos/Datos_seleccionados/SSPD/sspd_ebby-cjha_mensual.csv',
                period=('anio', 'periodo'), categories=('identificador_empresa', 'estrato_sector', 'ubicacion', 'tipo_conexion', 'tipo_lectura', 'tipo_factura'),
                measures=('consumo_basico_sum', 'consumo_compl_sum', 'consumo_mayor800_sum', 'valor_total_sum')),
    'XM': dict(dataset='c1b851', path='Data/silver/datos/Datos_seleccionados/XM_piloto/xm_demanda_mensual_piloto.csv',
                period=('periodo',), categories=('CodigoSICAgente', 'MercadoComercializacion', 'SistemaTransmision'), measures=('demanda_kwh',)),
    'SSPD_PLAN': dict(dataset='vfjy-6fka', path='Data/bronze/datos/Datos_seleccionados/SSPD_PLAN/sspd_vfjy-6fka.csv',
                period=('anio', 'mes'), categories=('id_empresa', 'id_mercado', 'estra_sector'),
                measures=('subsidios', 'contribuciones', 'cont_no_recau_a_6m', 'cont_recau_last_conc',
                          'g_rec_mmin_fssri_pgn', 'giros_recib_otros', 'giros_efect_mminas', 'giros_efect_otros', 'foes', 'devolucion_foes')),
}


def read_csv(path):
    path = Path(path)
    if path.suffix == '.zip':
        with zipfile.ZipFile(path) as archive:
            names = [n for n in archive.namelist() if n.lower().endswith('.csv')]
            if len(names) != 1:
                raise ValueError('Se requiere exactamente un CSV dentro del ZIP')
            with archive.open(names[0]) as stream:
                return list(csv.DictReader(io.TextIOWrapper(stream, encoding='utf-8-sig', newline='')))
    with path.open(encoding='utf-8-sig', newline='') as stream:
        return list(csv.DictReader(stream))


def write_csv(path, rows, fields):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('w', encoding='utf-8', newline='') as stream:
        writer = csv.DictWriter(stream, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def digest(path):
    with Path(path).open('rb') as stream:
        return hashlib.file_digest(stream, 'sha256').hexdigest()


def content_key(row):
    clean = {k: v for k, v in row.items() if not k.startswith(':')}
    return hashlib.sha256(json.dumps(clean, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def number(value):
    try:
        result = float(value)
        return result if math.isfinite(result) else None
    except (ValueError, TypeError):
        return None


def month_index(row, cfg):
    try:
        if len(cfg['period']) == 1:
            year, month = map(int, row[cfg['period'][0]].split('-'))
        else:
            year = int(row[cfg['period'][0]])
            month = MONTHS.get(row[cfg['period'][1]]) or int(row[cfg['period'][1]])
        if year < 1 or not 1 <= month <= 12:
            return None
        return year * 12 + month - 1
    except (ValueError, TypeError, KeyError):
        return None


def label(index):
    year, month = divmod(index, 12)
    return f'{year:04d}-{month + 1:02d}'


def aliases():
    # Catálogo interno ya versionado. No modifica los valores de Bronze.
    import yaml
    document = yaml.safe_load((ROOT / 'Data/silver/catalogos/EPM/epm_etiquetas.yaml').read_text(encoding='utf-8'))
    return {(r['campo'], r['etiqueta_original']): r['etiqueta_canonica_candidata'] for r in document['entradas']}


def business_key(source, row, mapping=None):
    cfg = SOURCES[source]
    mapping = mapping or {}
    values = tuple(mapping.get((c, row.get(c, '')), row.get(c, '')) for c in cfg['categories'])
    return values


def observation_key(source, category, period, measure):
    payload = [SOURCES[source]['dataset'], list(category), label(period), measure]
    return hashlib.sha256(json.dumps(payload, ensure_ascii=False, separators=(',', ':')).encode()).hexdigest()


def quarantine(rows, findings):
    """Expande nombres históricos a celdas; R08 ambiguo aparta tres propiedades.

    No deduce la celda correcta de una relación de orden rota. Las otras medidas
    de la fila siguen disponibles. R12 siempre es advertencia, sin confirmar error.
    """
    existing = {content_key(r) for r in rows}
    names = {'Punta': ('punta',), 'Fuera de Punta': ('fueradepunta',),
             'EPM': ('propiedadepm',), 'Compartido': ('compartido',), 'Cliente': ('propiedaddelcliente',),
             'Propiedad': ('propiedadepm', 'compartido', 'propiedaddelcliente')}
    result = []
    seen = set()
    for finding in findings:
        rule = finding.get('regla', '')[:3]
        if rule not in ('R08', 'R11', 'R12') and not (rule == 'R07' and finding.get('severidad') == 'Error'):
            continue
        key = finding.get('clave_contenido', '')
        if key not in existing:
            raise ValueError('Hallazgo sin correspondencia con el snapshot EPM: ' + key)
        original = finding.get('columna', '')
        columns = names.get(original, (original,) if original in SOURCES['EPM']['measures'] else ())
        if not columns:
            raise ValueError('Columna de cuarentena sin mapeo: ' + original)
        for column in columns:
            identity = key, column, rule
            if identity in seen:
                continue
            seen.add(identity)
            result.append(dict(dataset_id='sfcd-b3ey', clave_contenido=key, columna=column, regla=rule,
                               severidad='Advertencia' if rule == 'R12' else finding.get('severidad', 'Advertencia'),
                               estado='cuarentena_preventiva', confirmacion='pendiente',
                               motivo='Relación de orden ambigua: tres propiedades' if original == 'Propiedad' else 'Celda señalada; no se corrige ni interpola'))
    return sorted(result, key=lambda r: (r['clave_contenido'], r['columna'], r['regla']))


def build_series(source, rows, quarantined=(), canonical=True):
    cfg = SOURCES[source]
    mapping = aliases() if source == 'EPM' and canonical else {}
    blocked = {(r['clave_contenido'], r['columna']) for r in quarantined}
    grouped = defaultdict(lambda: defaultdict(list))
    for row in rows:
        period = month_index(row, cfg)
        if period is None:
            continue
        category = business_key(source, row, mapping)
        key = content_key(row)
        for measure in cfg['measures']:
            grouped[(category, measure)][period].append((number(row.get(measure)), (key, measure) in blocked, key))
    series = {}
    for identity, periods in grouped.items():
        series[identity] = {}
        for period, values in periods.items():
            distinct = {v for v, _, _ in values}
            blocked_cell = any(b for _, b, _ in values)
            if blocked_cell:
                reason = 'cuarentena'
            elif len(distinct) != 1:
                reason = 'duplicado_conflictivo'
            elif None in distinct:
                reason = 'no_numerico_o_no_finito'
            elif next(iter(distinct)) <= 0:
                reason = 'no_positivo'
            else:
                reason = ''
            series[identity][period] = dict(value=next(iter(distinct)) if len(distinct) == 1 else None,
                reason=reason, keys=sorted({k for _, _, k in values}), registros=len(values))
    return series


def longest_run(periods):
    runs = []
    for month in sorted(periods):
        if not runs or month != runs[-1][-1] + 1:
            runs.append([])
        runs[-1].append(month)
    return min(runs, key=lambda r: (-len(r), r[0])) if runs else []


def evaluate_series(source, category, measure, points, reference=36, watch=12):
    """Referencia de 36 posiciones mensuales; exclusiones no mueven el corte.

    Se conserva toda la racha más larga (empate: más antigua). Tras 36 cambios
    de calendario se observan 12. Las escalas solo usan cambios válidos de la
    referencia, y MR solo se calcula entre dos cambios consecutivos válidos.
    """
    run = longest_run(points)
    base = dict(fuente=source, categoria=json.dumps(category, ensure_ascii=False), serie='|'.join(category), medida=measure)
    if len(run) < reference + watch + 1:
        return dict(**base, estado='historia_insuficiente', periodos=len(run)), []
    selected = run[:reference + watch + 1]
    changes = []
    previous_change = None
    for index, month in enumerate(selected[1:]):
        a, b = points[month - 1], points[month]
        reason = a['reason'] or b['reason']
        change = None if reason else math.log(b['value']) - math.log(a['value'])
        mr = abs(change - previous_change) if change is not None and previous_change is not None else None
        changes.append(dict(period=month, change=change, mr=mr, previous=previous_change, reason=reason))
        previous_change = change
    ref = [p['change'] for p in changes[:reference] if p['change'] is not None]
    moving_ranges = [p['mr'] for p in changes[:reference] if p['mr'] is not None]
    if len(ref) < 2 or not moving_ranges:
        return dict(**base, estado='referencia_insuficiente', periodos=len(run)), []
    mean, mr_mean = st.mean(ref), st.mean(moving_ranges)
    lo, hi, mr_hi = mean - 2.66 * mr_mean, mean + 2.66 * mr_mean, 3.267 * mr_mean
    ref_levels = [points[m]['value'] for m in selected[:reference + 1] if not points[m]['reason']]
    level_median = st.median(ref_levels)
    detail = []
    for index, p in enumerate(changes):
        month, change, mr = p['period'], p['change'], p['mr']
        signal_i = int(change < lo or change > hi) if change is not None else None
        signal_mr = int(mr > mr_hi) if mr is not None else None
        # La unión solo es evaluable cuando I lo es. MR faltante no equivale a MR=0.
        signal = int(bool(signal_i or signal_mr)) if change is not None else None
        current = points[month]
        detail.append(dict(**base, periodo=label(month), fase='referencia' if index < reference else 'vigilancia',
            clave_alerta_estable=observation_key(source, category, month, measure),
            claves_filas=json.dumps(current['keys']), valor_actual=current['value'], valor_anterior=points[month - 1]['value'],
            cambio_log=change, rango_movil=mr, cambio_log_anterior=p['previous'],
            limite_inferior=lo, limite_superior=hi, limite_mr=mr_hi,
            senal_i=signal_i, senal_mr=signal_mr, senal_imr=signal, motivo_exclusion=p['reason'],
            mediana_nivel_referencia=level_median, estado_escala='mr_cero' if mr_mean == 0 else 'regular',
            clasificacion='pendiente_revision' if signal and index >= reference else 'sin_confirmacion'))
    surveillance = [d for d in detail if d['fase'] == 'vigilancia']
    summary = dict(**base, estado='evaluable', periodos=len(run), inicio_referencia=label(selected[1]), fin_referencia=label(selected[reference]),
        inicio_vigilancia=label(selected[reference + 1]), fin_vigilancia=label(selected[-1]),
        cambios_referencia=len(ref), cambios_vigilancia=sum(d['cambio_log'] is not None for d in surveillance),
        excluidos_referencia=reference-len(ref), excluidos_vigilancia=sum(d['cambio_log'] is None for d in surveillance),
        rangos_referencia=len(moving_ranges), media_referencia=mean, mr_media=mr_mean,
        limite_inferior=lo, limite_superior=hi, limite_mr=mr_hi,
        señales=sum(d['senal_imr'] or 0 for d in surveillance),
        señales_i=sum(d['senal_i'] or 0 for d in surveillance), señales_mr=sum(d['senal_mr'] or 0 for d in surveillance))
    return summary, detail


def percentile(values, probability):
    values = sorted(values)
    position = (len(values) - 1) * probability
    low = int(position)
    return values[low] + (values[min(low + 1, len(values) - 1)] - values[low]) * (position - low)


def cluster_bootstrap(summaries, repetitions=2000, seed=20261105):
    """Remuestrea categorías completas y conserva juntos numerador/denominador."""
    result = []
    for source in sorted({r['fuente'] for r in summaries}):
        groups = defaultdict(lambda: [0, 0, 0])
        for row in summaries:
            if row['fuente'] != source or row.get('estado') != 'evaluable' or not row['cambios_vigilancia']:
                continue
            group = groups[row['categoria']]
            group[0] += row['señales']; group[1] += row['cambios_vigilancia']; group[2] += 1
        values = [groups[k] for k in sorted(groups)]
        if not values:
            result.append(dict(fuente=source, categorias=0, series=0, senales=0, observaciones=0,
                               tasa=None, ic95_inferior=None, ic95_superior=None, estado='sin_observaciones',
                               unidad_remuestreo='categoria_completa', repeticiones=repetitions, semilla=seed))
            continue
        numerator, denominator, series = map(sum, zip(*values))
        samples = []
        rng = random.Random(seed)
        if len(values) > 1:
            for _ in range(repetitions):
                draw = [values[rng.randrange(len(values))] for _ in values]
                samples.append(sum(g[0] for g in draw) / sum(g[1] for g in draw))
        result.append(dict(fuente=source, categorias=len(values), series=series, senales=numerator,
            observaciones=denominator, tasa=numerator/denominator,
            ic95_inferior=percentile(samples, .025) if samples else None,
            ic95_superior=percentile(samples, .975) if samples else None,
            estado='bootstrap_categorias' if samples else 'sin_IC_una_categoria',
            unidad_remuestreo='categoria_completa', repeticiones=repetitions, semilla=seed))
    return result


def compare_rows(first, second):
    """Compara multiconjuntos: tolera reordenamiento y conserva duplicados."""
    a, b = Counter(content_key(r) for r in first), Counter(content_key(r) for r in second)
    return dict(filas_primera=sum(a.values()), filas_segunda=sum(b.values()),
                mismos_registros=a == b, registros_retirados=sum((a-b).values()), registros_agregados=sum((b-a).values()))
