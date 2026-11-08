"""Hito 4.4: calibración, catálogo y contraste externo de la regla de alerta sistémica.

Solo escribe en 4.4. Lee (sin modificar) los datasets, las salidas del Hito 2 y las de 4.2.
"""
from __future__ import annotations

import csv
import json
import platform
import sys
from pathlib import Path

import numpy as np
import pandas as pd

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.dont_write_bytecode = True
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(ROOT / 'desarrollo_puntos/4.2'))
import analisis_sensibilidad as A  # noqa: E402
import regla_sistemica as R  # noqa: E402

WINDOWS = (24, 36)
METHODS = tuple(R.METHOD_COLUMNS)
PRIMARY_WINDOW = 36
EFFECT_X = (0.10, 0.20, 0.25, 0.30, 0.50, 0.75)
FLAG_X = (0.10, 0.25, 0.50)
H2 = ROOT / 'desarrollo_puntos/3.3/insumos_hito2'
EXTERNAL = HERE / 'evidencia_externa'
PDF_MONTHS = ('2020-01', '2020-02', '2020-06', '2020-07', '2021-06', '2021-07')
CONTRAST_PAIRS = (('2020-01', '2020-02'), ('2020-06', '2020-07'), ('2021-06', '2021-07'))
COMPONENT_COLUMNS = ('propiedadepm', 'compartido', 'propiedaddelcliente')
TOLERANCE_SUM = 0.02
TABLES: dict[str, list[dict]] = {}


def write_table(name, frame_or_rows):
    frame = frame_or_rows if isinstance(frame_or_rows, pd.DataFrame) else pd.DataFrame(frame_or_rows)
    frame.to_csv(HERE / name, index=False, encoding='utf-8-sig')


def hito2_fractions():
    """Reproduce 51/83, 24/83 y 18/83 desde 05_alertas_imr_reales.csv (origen fijo, diferencia absoluta)."""
    alerts = pd.read_csv(H2 / '05_alertas_imr_reales.csv')
    summary = json.loads((H2 / '00_resumen.json').read_text(encoding='utf-8'))
    total = int(summary['series_completas_49'])
    alerts['serie'] = alerts.clave + '|' + alerts.columna
    alerts['componente'] = alerts.clave.str.split(' | ', regex=False).str[2]
    alerts['periodo'] = alerts.fecha.str[:7]
    months = [R.period_label(2020 * 12 + i) for i in range(24)]          # vigilancia 2020-01 ... 2021-12
    rows = []
    for month in months:
        g = alerts[alerts.periodo == month]
        rows.append(dict(periodo=month, series_evaluadas=total, series_con_alerta=g.serie.nunique(),
                         fraccion=g.serie.nunique() / total, categorias_evaluadas=None, categorias_con_alerta=None,
                         componentes_evaluados=None, componentes_con_alerta=g.componente.nunique(), aplicable=1))
    frame = pd.DataFrame(rows)
    counts = frame.set_index('periodo').series_con_alerta
    assert (counts['2020-02'], counts['2020-07'], counts['2021-07']) == (51, 24, 18), 'No reproduce 51/24/18 del plan'
    assert int(alerts.shape[0]) == int(summary['alertas_imr_reales'])
    return frame, alerts


def composition(long, method, month):
    column = R.METHOD_COLUMNS[method]
    g = long[long.mes == month_index(month)]
    evaluated = g.groupby('componente').size()
    alerting = g[g[column]].groupby('componente').size()
    return evaluated, alerting


def month_index(label):
    year, month = map(int, label.split('-'))
    return year * 12 + month - 1


def published_vs_csv():
    """Transcripción de los PDF de EPM frente a los valores del CSV y a la suma de componentes."""
    published = pd.read_csv(EXTERNAL / 'tarifas_epm_publicadas.csv')
    items, mapping, path = R.canonical_epm_items()
    raw = pd.read_csv(ROOT / 'fuentes_datos/datos/Datos_seleccionados/EPM/epm_sfcd-b3ey.csv', encoding='utf-8-sig')
    months = {n: i for i, n in enumerate(('Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto',
                                          'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'), 1)}
    raw = raw[(raw.tipodeinformacion == 'Monomia') & (raw.tipodetarifa == 'Costo Unitario') & (raw.nivel == 'I')].copy()
    raw['periodo'] = raw.year.astype('Int64').astype(str) + '-' + raw.mes.map(months).astype('Int64').astype(str).str.zfill(2)
    raw['componente'] = [mapping.get(('tipodedato', v), v) for v in raw.tipodedato]
    comparison, sums = [], []
    for row in published.itertuples(index=False):
        if row.componente.startswith('CU'):
            continue
        csv_rows = raw[(raw.periodo == row.periodo) & (raw.componente == row.componente)]
        for column in COMPONENT_COLUMNS:
            values = csv_rows[column].dropna().unique()
            comparison.append(dict(periodo=row.periodo, componente=row.componente, columna=column,
                                   valor_publicado=getattr(row, column),
                                   valores_en_csv=';'.join(f'{v:.2f}' for v in values),
                                   coincide=int(len(values) == 1 and abs(values[0] - getattr(row, column)) < 1e-9)))
    for period, g in published.groupby('periodo'):
        total = g[g.componente == 'CU total'].iloc[0]
        parts = g[~g.componente.str.startswith('CU')]
        for column in COMPONENT_COLUMNS:
            sums.append(dict(periodo=period, columna=column, cu_total_publicado=getattr(total, column),
                             suma_componentes=round(float(parts[column].sum()), 2),
                             diferencia=round(float(parts[column].sum() - getattr(total, column)), 2),
                             dentro_de_tolerancia=int(abs(parts[column].sum() - getattr(total, column)) <= TOLERANCE_SUM + 1e-9)))
    return published, pd.DataFrame(comparison), pd.DataFrame(sums)


def main():
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
    datasets, inputs = A.load_sources()
    quarantine = ROOT / 'desarrollo_puntos/3.7/EPM/cuarentena_registros.csv'
    guarded = {ROOT / e['ruta']: e['sha256'] for e in inputs.values()}
    guarded.update({quarantine: A.sha256(quarantine)})
    for path in (H2 / '05_alertas_imr_reales.csv', H2 / '00_resumen.json', H2 / '02_catalogo_variantes.csv',
                 ROOT / 'desarrollo_puntos/4.2/efecto_regla_sistemica_inyecciones.csv',
                 ROOT / 'desarrollo_puntos/4.2/efecto_regla_sistemica_reales.csv',
                 *sorted(EXTERNAL.glob('*.pdf')), EXTERNAL / 'tarifas_epm_publicadas.csv',
                 EXTERNAL / 'referencias_documentales.csv'):
        guarded[path] = A.sha256(path)

    canonical, mapping, _ = R.canonical_epm_items()
    populations = {('EPM', 'canonicas'): canonical,
                   ('EPM', 'originales'): R.with_components(datasets['EPM'], 'EPM'),
                   ('CHEC', 'originales'): R.with_components(datasets['CHEC'], 'CHEC'),
                   ('SSPD', 'originales'): R.with_components(datasets['SSPD'], 'SSPD'),
                   ('XM', 'originales'): R.with_components(datasets['XM'], 'XM')}
    fractions, longs = [], {}
    for (source, labels), items in populations.items():
        for window in WINDOWS:
            long = R.evaluate_items(items, window)
            longs[(source, labels, window)] = long
            for method in METHODS:
                frame = R.monthly_fractions(long, method)
                frame.insert(0, 'metodo', method)
                frame.insert(0, 'referencia', window)
                frame.insert(0, 'etiquetas', labels)
                frame.insert(0, 'fuente', source)
                frame['protocolo'] = 'ventana_movil_log'
                fractions.append(frame)
    h2_fraction, h2_alerts = hito2_fractions()
    h2_frame = h2_fraction.copy()
    for column, value in (('fuente', 'EPM'), ('etiquetas', 'canonicas_hito2'), ('referencia', 36),
                          ('metodo', 'IMR_clasica_hito2'), ('protocolo', 'origen_fijo_diferencia_absoluta')):
        h2_frame[column] = value
    all_fractions = pd.concat(fractions + [h2_frame], ignore_index=True)
    write_table('fracciones_mensuales.csv', all_fractions)
    write_table('reproduccion_hito2.csv', h2_fraction)

    # ---- calibración de X (EPM, con los meses que fija el plan) y efecto en todas las fuentes
    calibration, summary, effect = [], [], []
    keys = ['fuente', 'etiquetas', 'referencia', 'metodo', 'protocolo']
    for key, frame in all_fractions.groupby(keys, dropna=False):
        meta = dict(zip(keys, key))
        events = R.EVENT_MONTHS if meta['fuente'] == 'EPM' else ()
        frame = frame.sort_values('periodo')
        table = R.calibrate(frame, events=events)
        for name, value in reversed(list(meta.items())):
            table.insert(0, name, value)
        if meta['fuente'] == 'EPM':
            calibration.append(table)
            sep = R.separability(frame)
            best = table.dropna(subset=['exactitud_balanceada'])
            top = best[best.exactitud_balanceada == best.exactitud_balanceada.max()]
            row = dict(**meta, meses_evaluables=int((frame.aplicable == 1).sum()),
                       **{f'fraccion_{k}': v for k, v in sep['fraccion_por_evento'].items()},
                       eventos_evaluables=sep['eventos_evaluables'],
                       X_minimo_para_no_marcar_fondo=sep['X_minimo_para_no_marcar_fondo'],
                       X_maximo_para_capturar_todos=sep['X_maximo_para_capturar_todos'],
                       banda_factible=int(sep['banda_factible']),
                       X_mejor_exactitud_balanceada=float(top.umbral_X.max()),
                       exactitud_balanceada_maxima=float(best.exactitud_balanceada.max()),
                       eventos_capturados_en_X_trabajo=int(table[table.umbral_X == R.X_WORK].eventos_capturados.iloc[0]),
                       meses_marcados_en_X_trabajo=int(table[table.umbral_X == R.X_WORK].meses_marcados_total.iloc[0]))
            summary.append(row)
        selected = table[table.umbral_X.isin(EFFECT_X)].copy()
        selected['alertas_retenidas'] = selected.alertas_totales - selected.alertas_reclasificadas
        effect.append(selected[keys + ['umbral_X', 'meses_marcados_total', 'alertas_totales', 'alertas_reclasificadas',
                                       'alertas_retenidas', 'fraccion_alertas_reclasificadas']])
    write_table('calibracion_X.csv', pd.concat(calibration, ignore_index=True))
    write_table('calibracion_resumen.csv', pd.DataFrame(summary))
    write_table('efecto_regla_sobre_alertas_reales.csv', pd.concat(effect, ignore_index=True))

    # ---- composición de las alertas en los meses del plan (amplitud: cuántos componentes)
    rows = []
    for (source, labels, window), long in longs.items():
        if source != 'EPM':
            continue
        for method in METHODS:
            for month in R.EVENT_MONTHS:
                if month_index(month) not in set(long.mes):
                    continue
                evaluated, alerting = composition(long, method, month)
                for component in alerting.index:
                    rows.append(dict(fuente='EPM', etiquetas=labels, referencia=window, metodo=method, periodo=month,
                                     componente=component, series_con_alerta=int(alerting[component]),
                                     series_evaluadas_componente=int(evaluated[component])))
    for month in R.EVENT_MONTHS:
        g = h2_alerts[h2_alerts.periodo == month].groupby('componente').serie.nunique()
        for component, count in g.items():
            rows.append(dict(fuente='EPM', etiquetas='canonicas_hito2', referencia=36, metodo='IMR_clasica_hito2',
                             periodo=month, componente=component, series_con_alerta=int(count), series_evaluadas_componente=None))
    composition_table = pd.DataFrame(rows)
    write_table('composicion_alertas_meses_plan.csv', composition_table)

    # ---- inventario de series por variante (las etiquetas originales fragmentan las series de EPM)
    inventory = []
    for (source, labels), items in populations.items():
        row = dict(fuente=source, etiquetas=labels, series_totales=len(items))
        for window in WINDOWS:
            long = longs[(source, labels, window)]
            row[f'series_evaluables_ref{window}'] = int(long.serie.nunique())
            row[f'meses_evaluables_ref{window}'] = int(long.mes.nunique())
        inventory.append(row)
    write_table('inventario_series_por_variante.csv', inventory)

    # ---- tamaño de cada componente: cuánto aportaría a la fracción si todas sus series alertaran
    sizes = []
    for window in WINDOWS:
        long = longs[('EPM', 'canonicas', window)]
        counts = long.groupby(['mes', 'componente']).size().reset_index(name='series_del_componente')
        counts['series_evaluadas_mes'] = counts.mes.map(long.groupby('mes').size())
        counts['fraccion_si_alertan_todas'] = counts.series_del_componente / counts.series_evaluadas_mes
        counts['periodo'] = counts.mes.map(R.period_label)
        counts.insert(0, 'referencia', window)
        sizes.append(counts.drop(columns='mes'))
    write_table('tamano_componentes_epm.csv', pd.concat(sizes, ignore_index=True))

    # ---- catálogo de candidatos sistémicos
    catalog = []
    contrasted = {'2020-02': 'cotejado_con_publicacion_EPM_ene_feb_2020',
                  '2020-07': 'cotejado_con_publicacion_EPM_jun_jul_2020',
                  '2021-07': 'cotejado_con_publicacion_EPM_jun_jul_2021'}
    primary = all_fractions[(all_fractions.aplicable == 1) & (all_fractions.fraccion > min(FLAG_X)) &
                            (all_fractions.protocolo == 'ventana_movil_log') &
                            (all_fractions.referencia.isin(WINDOWS)) &
                            ~((all_fractions.fuente == 'EPM') & (all_fractions.etiquetas == 'originales'))]
    h2_flagged = h2_frame[h2_frame.fraccion > min(FLAG_X)]
    for frame in (primary, h2_flagged):
        for r in frame.itertuples(index=False):
            row = dict(fuente=r.fuente, etiquetas=r.etiquetas, protocolo=r.protocolo, referencia=r.referencia,
                       metodo=r.metodo, periodo=r.periodo, series_evaluadas=r.series_evaluadas,
                       series_con_alerta=r.series_con_alerta, fraccion=r.fraccion,
                       categorias_con_alerta=r.categorias_con_alerta, componentes_con_alerta=r.componentes_con_alerta)
            for x in FLAG_X:
                row[f'sistemico_X{int(round(100 * x))}'] = int(r.fraccion > x)
            row['estado'] = ('candidato_sistemico' if r.fraccion > R.X_WORK else 'por_debajo_del_umbral_de_trabajo')
            row['evidencia_externa'] = contrasted.get(r.periodo, 'sin_contraste') if r.fuente == 'EPM' else 'sin_contraste'
            catalog.append(row)
    write_table('catalogo_alertas_sistemicas.csv', pd.DataFrame(catalog))

    # ---- contraste con las publicaciones oficiales de EPM
    published, comparison, sums = published_vs_csv()
    write_table('verificacion_transcripcion_pdf.csv', comparison)
    write_table('verificacion_suma_componentes.csv', sums)
    assert comparison.coincide.all(), 'La transcripción de los PDF no coincide con el CSV'
    assert sums.dentro_de_tolerancia.all(), 'La suma de componentes no reproduce el CU total publicado'
    long36 = longs[('EPM', 'canonicas', PRIMARY_WINDOW)]
    long24 = longs[('EPM', 'canonicas', 24)]
    rows = []
    for base, month in CONTRAST_PAIRS:
        a = published[published.periodo == base].set_index('componente')
        b = published[published.periodo == month].set_index('componente')
        h2_month = h2_alerts[h2_alerts.periodo == month].groupby('componente').serie.nunique()
        for component in b.index:
            if component.startswith('CU'):
                continue
            old, new = float(a.loc[component, 'propiedadepm']), float(b.loc[component, 'propiedadepm'])
            row = dict(mes_base=base, mes=month, componente=component, valor_base=old, valor_mes=new,
                       cambio_absoluto=round(new - old, 2),
                       cambio_porcentual=(100 * (new - old) / old) if old > 0 and new > 0 else None,
                       cambio_log=float(np.log(new / old)) if old > 0 and new > 0 else None,
                       observacion='cruza_cero: sin logaritmo; la serie queda fuera del protocolo logarítmico' if old <= 0 or new <= 0 else '')
            for label, long in (('W36', long36), ('W24', long24)):
                for method in METHODS:
                    evaluated, alerting = composition(long, method, month)
                    row[f'series_con_alerta_{method}_{label}'] = int(alerting.get(component, 0))
                    row[f'series_evaluadas_{label}'] = int(evaluated.get(component, 0))
            row['series_con_alerta_hito2_IMR_absoluta'] = int(h2_month.get(component, 0))
            rows.append(row)
        cu = {k: float(x.loc['CU total', 'propiedadepm']) for k, x in (('base', a), ('mes', b))}
        applied = float(b.loc['CU CREG 012 de 2020', 'propiedadepm']) if 'CU CREG 012 de 2020' in b.index else None
        rows.append(dict(mes_base=base, mes=month, componente='CU total (publicado)', valor_base=cu['base'], valor_mes=cu['mes'],
                         cambio_absoluto=round(cu['mes'] - cu['base'], 2),
                         cambio_porcentual=100 * (cu['mes'] - cu['base']) / cu['base'], cambio_log=float(np.log(cu['mes'] / cu['base'])),
                         observacion=(f"fila «CU CREG 012 de 2020»: {applied:.2f}".replace('.', ',') if applied else '')))
    write_table('contraste_componentes.csv', pd.DataFrame(rows))

    # ---- costo de enmascaramiento (4.2): individuales frente a colectivos
    masking = pd.read_csv(ROOT / 'desarrollo_puntos/4.2/efecto_regla_sistemica_inyecciones.csv')
    masking = masking[(masking.referencia == 36) & (masking.cohorte == 'comun') & masking.metodo.isin(METHODS)]
    cost = (masking.groupby(['fuente', 'clase_ensayo', 'metodo', 'umbral_fraccion'])[['casos', 'detecciones_t_o_t1', 'retenidas_t_o_t1']]
            .sum().reset_index())
    cost['detecciones_enmascaradas'] = cost.detecciones_t_o_t1 - cost.retenidas_t_o_t1
    cost['fraccion_enmascarada'] = cost.detecciones_enmascaradas / cost.detecciones_t_o_t1
    write_table('costo_enmascaramiento_4_2.csv', cost)

    for path, before in guarded.items():
        assert A.sha256(path) == before, f'Se modificó una entrada: {path}'
    config = {
        'fecha_cliente': '2026-11-07', 'ventanas_referencia': WINDOWS, 'metodos': METHODS,
        'protocolo': 'origen móvil: el mes m se evalúa con los W cambios logarítmicos anteriores; cambios solo entre meses consecutivos',
        'regla': f'mes sistémico si series_con_alerta/series_evaluadas > X y series_evaluadas >= {R.N_MIN}',
        'X_malla': [R.X_GRID[0], R.X_GRID[-1], 'paso 0,01'], 'X_trabajo_propuesto': R.X_WORK,
        'estado_X_trabajo': 'propuesta; no aprobada por el director',
        'meses_del_plan': R.EVENT_MONTHS, 'N_MIN': R.N_MIN,
        'etiquetas_EPM': {'canonicas': 'catálogo de variantes del Hito 2 (3.3/insumos_hito2/02_catalogo_variantes.csv), copia de trabajo',
                          'originales': 'etiquetas tal como están en el CSV (protocolo 4.1/4.2)'},
        'variantes_calibradas': 'EPM canónicas y originales × W 24 y 36 × I-MR clásica y MAD 3σ, más la reproducción del Hito 2 (origen fijo, diferencia absoluta, 83 series)',
        'MAD_cero': 'señal si el cambio difiere de la mediana (como 4.1 y 4.2)',
        'entradas': inputs, 'cuarentena_EPM': {'ruta': quarantine.relative_to(ROOT).as_posix(), 'sha256': A.sha256(quarantine)},
        'dependencias': {p.relative_to(ROOT).as_posix(): A.sha256(p) for p in (
            ROOT / '0_Recomendaciones_profesor/plan_hitos_3-6_detallado.txt',
            H2 / '05_alertas_imr_reales.csv', H2 / '00_resumen.json', H2 / '02_catalogo_variantes.csv',
            ROOT / 'desarrollo_puntos/4.2/efecto_regla_sistemica_inyecciones.csv',
            ROOT / 'desarrollo_puntos/4.2/analisis_sensibilidad.py', ROOT / 'desarrollo_puntos/4.1/zscore_robusto.py')},
        'evidencia_externa': {p.relative_to(ROOT).as_posix(): A.sha256(p) for p in sorted(EXTERNAL.glob('*'))},
        'versiones': {'python': platform.python_version(), 'numpy': np.__version__, 'pandas': pd.__version__}}
    (HERE / 'configuracion.json').write_text(json.dumps(config, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print('Calibración, catálogo y contraste generados en', HERE)


if __name__ == '__main__':
    main()
