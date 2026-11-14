"""Reproduce el Hito 3 sobre Bronze/Silver y genera evidencia en Gold."""
from __future__ import annotations

from collections import Counter, defaultdict
from datetime import datetime, timezone
import json
import math
from pathlib import Path
import statistics as st
import subprocess
import sys

from .core import (ROOT, SOURCES, aliases, business_key, build_series, cluster_bootstrap,
                   content_key, digest, evaluate_series, label, month_index, number,
                   observation_key, quarantine, read_csv, write_csv)

OUT = ROOT / 'Data/gold/outputs/hito3'
SEED = 20261105


def dump(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False) + '\n', encoding='utf-8')


def static_findings(source, rows):
    """Hallazgos transversales por contenido; las adaptaciones quedan explícitas.

    Es evidencia complementaria a las 19 fichas de la matriz, no convierte una
    regla no aplicable en un control aprobado. R12 se evalúa tras fijar referencia.
    """
    cfg = SOURCES[source]
    mapping = aliases() if source == 'EPM' else {}
    result = []
    exact = Counter(content_key(r) for r in rows)
    handled_duplicates = set()
    by_business = Counter((business_key(source, r, mapping), month_index(r, cfg)) for r in rows)
    for row in sorted(rows, key=content_key):
        key, period = content_key(row), month_index(row, cfg)
        category = business_key(source, row, mapping)

        def add(rule, column, reason, severity='Advertencia', count=1):
            identity = [source, key, rule, column, reason]
            result.append(dict(fuente=source, dataset_id=cfg['dataset'], regla=rule, columna=column,
                clave_contenido=key, clave_observacion=observation_key(source, category, period, column) if period is not None else '',
                id_hallazgo=content_key({'evento': json.dumps(identity, ensure_ascii=False)}),
                periodo=label(period) if period is not None else '', categoria=json.dumps(category, ensure_ascii=False),
                valor=row.get(column, ''), severidad=severity, motivo=reason, multiplicidad=count))

        if any(not row.get(c, '').strip() for c in cfg['period']):
            add('R01', '|'.join(cfg['period']), 'Periodo ausente', 'Error')
        elif period is None:
            add('R02', '|'.join(cfg['period']), 'Periodo no construible', 'Error')
        for col in cfg['measures']:
            value = number(row.get(col))
            if row.get(col, '').strip() and value is None:
                add('R03', col, 'Valor no numerico o no finito', 'Error')
            if value is not None and value < 0:
                add('R07', col, 'Signo requiere dominio documentado; no se corrige automaticamente')
            if source in ('EPM', 'CHEC', 'SSPD_PLAN') and value is not None and value.is_integer() and 36526 <= value <= 47483:
                add('R11', col, 'Posible serial Excel; no confirma conversion de fecha')
        if key not in handled_duplicates and exact[key] > 1:
            add('R04', '', 'Duplicado exacto adicional', 'Error', exact[key]-1)
            handled_duplicates.add(key)
        if period is not None and by_business[(category, period)] > 1:
            add('R05', '', 'Clave de negocio compartida; no se promedia si los valores discrepan')
        for col in cfg['categories']:
            if mapping.get((col, row.get(col, '')), row.get(col, '')) != row.get(col, ''):
                add('R06', col, 'Etiqueta con equivalencia operativa interna; original conservado')
        values = [number(row.get(c)) for c in cfg['measures']]
        if all(v == 0 for v in values):
            add('R10', '', 'Todas las medidas de esta fila son cero; revisar aplicabilidad')
        if source == 'EPM':
            a, b, c = values[:3]
            if all(v is not None for v in (a, b, c)) and not a >= b >= c:
                add('R08', 'Propiedad', 'Orden EPM >= compartido >= cliente no satisfecho')
            level = row.get('nivel', '')
            if (level == 'I' and any(v not in (None, 0) for v in values[3:])) or (level in ('II', 'III', 'IV') and any(v not in (None, 0) for v in values[:3])):
                add('R09', 'nivel', 'Columnas monetarias requieren revision segun nivel')
    # Duplicados exactos comparten identidad: un hallazgo por evento y multiplicidad.
    unique = {r['id_hallazgo']: r for r in result}
    return [unique[k] for k in sorted(unique)]


def profile(source, rows, series):
    cfg = SOURCES[source]
    periods = sorted({p for r in rows if (p := month_index(r, cfg)) is not None})
    return dict(fuente=source, dataset_id=cfg['dataset'], archivo=cfg['path'], sha256=digest(ROOT / cfg['path']),
                filas=len(rows), columnas=list(rows[0]) if rows else [],
                ausentes_por_columna={c: sum(not r.get(c, '').strip() for r in rows) for c in rows[0]} if rows else {},
                duplicados_exactos=sum(n-1 for n in Counter(content_key(r) for r in rows).values()),
                periodos=len(periods), inicio=label(periods[0]) if periods else None, fin=label(periods[-1]) if periods else None,
                series_candidatas_incluyendo_ceros=len(series),
                series_con_valores_positivos=sum(any(p['value'] is not None and p['value'] > 0 for p in values.values()) for values in series.values()),
                nota='SSPD y XM: tabla mensual derivada, no conteo de microdatos crudos.' if source in ('SSPD', 'XM') else 'Snapshot local conservado; no se atribuye fecha original de descarga.')


def isolation_forest(details):
    """Cuatro rasgos logarítmicos. Escalado y umbral usan solo referencia.

    Un modelo por fuente y fecha de corte evita entrenar con meses posteriores a
    la primera vigilancia de alguna serie. No reutiliza salidas antiguas del H4.
    """
    import numpy as np
    from sklearn.ensemble import IsolationForest
    per_series = defaultdict(list)
    for row in details:
        per_series[(row['fuente'], row['categoria'], row['medida'])].append(row)
    banks = defaultdict(list)
    omitted = []
    for identity, points in sorted(per_series.items()):
        reference = [p for p in points if p['fase'] == 'referencia']
        cutoff = max(p['periodo'] for p in reference)
        features = []
        for index, p in enumerate(points):
            change, previous = p['cambio_log'], p['cambio_log_anterior']
            if change is None or (index and previous is None):
                omitted.append(dict(fuente=p['fuente'], clave_alerta_estable=p['clave_alerta_estable'],
                                    motivo='Cambio o rezago no disponible; no se cruza hueco ni cuarentena'))
                continue
            previous = 0.0 if index == 0 else previous
            raw = [change, previous, abs(change-previous), math.log(p['valor_actual']/p['mediana_nivel_referencia'])]
            features.append((p, raw))
        train = [x for p, x in features if p['fase'] == 'referencia']
        if len(train) < 2:
            continue
        centers = np.median(train, axis=0)
        scales = 1.4826 * np.median(np.abs(np.array(train)-centers), axis=0)
        fallback = np.mean(np.abs(np.array(train)-centers), axis=0)
        scales = np.where(scales > 0, scales, np.where(fallback > 0, fallback, 1.0))
        for p, raw in features:
            banks[(identity[0], cutoff)].append((p, (np.array(raw)-centers)/scales))
    output, models = [], []
    for (source, cutoff), records in sorted(banks.items()):
        train = np.array([x for p, x in records if p['fase'] == 'referencia'])
        model = IsolationForest(n_estimators=300, contamination='auto', random_state=20261106, n_jobs=1).fit(train)
        threshold = float(np.quantile(-model.score_samples(train), .995))
        watch = [(p, x) for p, x in records if p['fase'] == 'vigilancia']
        for (p, _), score in zip(watch, -model.score_samples(np.array([x for _, x in watch])) if watch else []):
            output.append(dict(fuente=source, categoria=p['categoria'], medida=p['medida'], periodo=p['periodo'],
                clave_alerta_estable=p['clave_alerta_estable'], fin_referencia=cutoff, puntaje_if=float(score),
                umbral=threshold, senal_if=int(score > threshold), cambio_log=p['cambio_log']))
        models.append(dict(fuente=source, fin_referencia=cutoff, primera_vigilancia=min((p['periodo'] for p, _ in watch), default=None),
                           filas_entrenamiento=len(train), filas_vigilancia=len(watch), percentil=.995, umbral=threshold, semilla=20261106))
    dump(OUT / 'isolation_forest_modelos.json', dict(rasgos=['cambio_log', 'cambio_log_anterior', 'abs_diferencia_cambios_log', 'log_nivel_relativo_mediana_referencia'],
         modelos=models, exclusiones=omitted, numpy=np.__version__, nota='Rasgo rezagado inicial cero; posteriores huecos se excluyen. Escala constante=1 solo para ordenar rasgos constantes.'))
    write_csv(OUT / 'isolation_forest.csv', output, list(output[0]) if output else ['fuente', 'clave_alerta_estable'])
    return models


def reconcile_downloads():
    from .acquisition import compare_downloads
    comparisons = compare_downloads()
    for result in comparisons:
        if result['estado'] != 'comparadas':
            continue
        source = result['fuente']
        if source not in SOURCES:
            # El conjunto histórico pedido por el plan se perfila con su contrato real.
            a, b = [read_csv(ROOT / result[key] / 'datos.csv') for key in ('primera', 'segunda')]
            result['perfil_plan'] = dict(filas=len(b), columnas=list(b[0]) if b else [],
                ausentes={c: sum(not r.get(c, '').strip() for r in b) for c in b[0]} if b else {})
            continue
        downloaded = [read_csv(ROOT / result[key] / 'datos.csv') for key in ('primera', 'segunda')]
        a, b = [static_findings(source, rows) for rows in downloaded]
        result['mismos_hallazgos_R01_R11'] = a == b
        result['hallazgos_primera'], result['hallazgos_segunda'] = len(a), len(b)
        signatures = []
        for rows, findings in zip(downloaded, (a, b)):
            qrows = quarantine(rows, [dict(r, columna='Propiedad' if r['columna'] == 'Propiedad' else r['columna']) for r in findings]) if source == 'EPM' else []
            summaries, details = [], []
            for (category, measure), points in sorted(build_series(source, rows, qrows).items()):
                summary, detail = evaluate_series(source, category, measure, points)
                summaries.append(summary); details.extend(detail)
            signatures.append(dict(resumen=summaries, detalle=details))
        result['mismas_cartas_y_claves'] = signatures[0] == signatures[1]
        result['cartas_elegibles'] = sum(r['estado'] == 'evaluable' for r in signatures[0]['resumen'])
    dump(OUT / 'comparacion_descargas.json', dict(comparaciones=comparisons,
         alcance='Dos capturas reales consecutivas. No acreditan estabilidad futura ni publicación oportuna histórica.'))
    return comparisons


def run_source(source, quarantine_rows=None, mirror=False):
    cfg = SOURCES[source]
    rows = read_csv(ROOT / cfg['path'])
    qrows = quarantine_rows or []
    series = build_series(source, rows, qrows)
    summaries, details = [], []
    for (category, measure), points in sorted(series.items()):
        summary, detail = evaluate_series(source, category, measure, points)
        summaries.append(summary); details.extend(detail)
    # Campos completos incluso cuando no hay series elegibles.
    summary_fields = sorted({key for r in summaries for key in r} | {'fuente', 'serie', 'medida', 'señales', 'cambios_vigilancia'})
    write_csv(OUT / f'{source}/cartas_resumen.csv', summaries, summary_fields)
    if mirror:
        write_csv(ROOT / f'Data/gold/outputs/cartas/{source}/cartas_log_{source.lower()}.csv',
                  [r for r in summaries if r['estado'] == 'evaluable'], summary_fields)
    write_csv(OUT / f'{source}/cartas_detalle.csv', details, list(details[0]) if details else ['fuente', 'clave_alerta_estable'])
    findings = static_findings(source, rows)
    for d in details:
        # R12 evalúa niveles de vigilancia con referencia previa, incluidas celdas
        # apartadas preventivamente si tienen valor numérico; no entra en límites.
        if d['fase'] == 'vigilancia' and d['valor_actual'] is not None and abs(d['valor_actual']) > 10*d['mediana_nivel_referencia']:
            findings.append(dict(fuente=source, dataset_id=cfg['dataset'], regla='R12', columna=d['medida'],
                clave_contenido='|'.join(json.loads(d['claves_filas'])), clave_observacion=d['clave_alerta_estable'],
                id_hallazgo='R12:' + d['clave_alerta_estable'], periodo=d['periodo'], categoria=d['categoria'],
                valor=d['valor_actual'], severidad='Advertencia', motivo='Nivel > 10 x mediana de referencia; no confirma error', multiplicidad=1))
    write_csv(OUT / f'{source}/hallazgos.csv', findings, list(findings[0]) if findings else ['fuente', 'regla', 'id_hallazgo'])
    dump(OUT / f'{source}/perfil.json', profile(source, rows, series))
    return summaries, details


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    rows = read_csv(ROOT / SOURCES['EPM']['path'])
    # Se contrasta el contenido de las filas: nunca se usa la posición para excluir.
    findings = read_csv(ROOT / 'Data/silver/verificaciones/trazabilidad_filas/03_hallazgos_trazabilidad.csv')
    qrows = quarantine(rows, findings)
    write_csv(OUT / 'cuarentena_celdas_epm.csv', qrows, list(qrows[0]))
    # Versión vigente de los hallazgos históricos, sin alterar el insumo del Hito 2.
    current = [dict(r, severidad='Advertencia' if r.get('regla', '')[:3] == 'R12' else r.get('severidad', '')) for r in findings]
    write_csv(OUT / 'hallazgos_epm_h2_reclasificados.csv', current, list(current[0]))
    summaries, details = [], []
    for source in SOURCES:
        summary, detail = run_source(source, qrows if source == 'EPM' else [], mirror=True)
        summaries.extend(summary); details.extend(detail)
        if source == 'EPM':
            alerts = [d for d in detail if d['fase'] == 'vigilancia' and d['senal_imr']]
            write_csv(ROOT / 'Data/gold/outputs/cartas/EPM/revision_senales_cartas_epm.csv',
                      alerts, list(detail[0]) if detail else ['fuente','clave_alerta_estable'])
    boot = cluster_bootstrap(summaries)
    from .entry import save_bootstrap
    save_bootstrap(boot)
    # Inventario explícito de conglomerados, nunca una categoría por estrato amplio.
    groups = defaultdict(lambda: [0, 0, 0])
    for s in summaries:
        if s['estado'] == 'evaluable':
            g = groups[(s['fuente'], s['categoria'])]
            g[0] += 1; g[1] += s['señales']; g[2] += s['cambios_vigilancia']
    clusters = [dict(fuente=s, categoria=c, series=g[0], senales=g[1], observaciones=g[2]) for (s,c),g in sorted(groups.items())]
    write_csv(OUT / 'inventario_categorias.csv', clusters, ['fuente','categoria','series','senales','observaciones'])
    models = isolation_forest(details)
    comparisons = reconcile_downloads()
    subprocess.run([sys.executable, '-B', str(ROOT / 'Code/Modeling/cartas/revision_cartas_fuentes.py')], cwd=ROOT, check=True)
    # La matriz consume las cartas vigentes y las mismas ventanas de R12.
    subprocess.run([sys.executable, '-B', str(ROOT / 'Code/Data_Acquisition_and_Understanding/calidad/medir_matriz_oe1.py')], cwd=ROOT, check=True)
    subprocess.run([sys.executable, '-B', str(ROOT / 'Code/Evaluation/scorecard/generar_scorecard_oe1.py')], cwd=ROOT, check=True)
    from .report import generate
    generate(comparisons)
    manifest = dict(ejecucion_utc=datetime.now(timezone.utc).isoformat(), version_protocolo='hito3-2',
        semillas={'bootstrap':SEED, 'isolation_forest':20261106},
        entradas=[dict(archivo=c['path'], sha256=digest(ROOT / c['path'])) for c in SOURCES.values()],
        categorias=boot, modelos_if=len(models), comparaciones_descargas=comparisons,
        estado='implementacion_corregida_con_pendientes_de_evidencia_externa',
        pendientes=['Oportunidad histórica: disponibilidad real y plazo esperado de EPM/CHEC',
                    'Catálogos y semántica externos; umbrales y responsables nominales',
                    'Integración y aprobación del anteproyecto oficial fuera del repositorio'],
        nota_hito4='Los experimentos 4.2–4.4 conservan sus datos/configuración históricos. No se declaran recalculados con el protocolo H3 corregido.')
    # Huellas de código y configuración permiten identificar exactamente el protocolo.
    manifest['codigo'] = {str(p.relative_to(ROOT)):digest(p) for p in sorted((ROOT / 'Code/hito3').glob('*.py'))}
    manifest['configuraciones_y_evidencia'] = {str(p.relative_to(ROOT)):digest(p) for p in (
        ROOT / 'Data/silver/catalogos/EPM/epm_etiquetas.yaml',
        ROOT / 'Data/silver/verificaciones/trazabilidad_filas/03_hallazgos_trazabilidad.csv',
        ROOT / 'Data/gold/outputs/calidad/plantilla_oportunidad.csv',
        ROOT / 'Data/gold/outputs/calidad/matriz_oe1.csv',
        ROOT / 'Data/gold/outputs/calidad/matriz_oe1.yaml',
        ROOT / 'Code/Data_Acquisition_and_Understanding/calidad/medir_matriz_oe1.py')}
    manifest['salidas'] = {str(p.relative_to(ROOT)):digest(p) for p in sorted(OUT.rglob('*')) if p.is_file() and p.name != 'manifiesto.json'}
    dump(OUT / 'manifiesto.json', manifest)
    print('Hito 3 corregido:', OUT, flush=True)


if __name__ == '__main__':
    main()
