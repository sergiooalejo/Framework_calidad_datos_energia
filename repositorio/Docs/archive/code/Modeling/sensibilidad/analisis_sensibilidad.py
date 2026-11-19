"""Hito 4.2: sensibilidad reproducible sobre cuatro fuentes locales.

Solo escribe en 4.2. Reutiliza la carga de 4.1, pero exige una racha mensual
continua y fija los mismos doce meses de vigilancia al variar la referencia.
"""
from __future__ import annotations

from pathlib import Path as _ProjectPath
_PROJECT_ROOT = next(p for p in _ProjectPath(__file__).resolve().parents if (p / "project.json").is_file())

import csv
import gzip
import hashlib
import io
import json
import math
import os
from pathlib import Path
import platform
import sys
import time

import numpy as np
import pandas as pd
import sklearn
from sklearn.ensemble import IsolationForest

HERE = (_PROJECT_ROOT / 'Outputs/sensibilidad')
ROOT = _PROJECT_ROOT
sys.dont_write_bytecode = True
sys.path.insert(0, str((_PROJECT_ROOT / 'Code/Modeling/detectores')))
from zscore_robusto import build_series, sha256

SEED = 20261106
WINDOWS = (24, 36, 48)
WATCH = 12
B = 1000
NORMAL_MEDIAN = 0.6744897501960817
SYSTEMIC = (0.10, 0.25, 0.50, 0.75)
SOURCES = ('EPM', 'CHEC', 'SSPD', 'XM')
METHODS = ('I_2.66_MRmedia', 'MR_3.267_MRmedia', 'IMR_clasica',
           'MAD_2.66sigma', 'MAD_3sigma', 'MAD_3.267sigma',
           'IF_p99', 'IF_p99.5', 'R12_f5', 'R12_f10', 'R12_f20')
TABLES: dict[str, list[dict]] = {}
BOOT_WEIGHTS = {}


def add(table, row):
    TABLES.setdefault(table, []).append(row)


def write_table(name, rows):
    path = HERE / name
    path.parent.mkdir(exist_ok=True, parents=True)
    fields = list(dict.fromkeys(k for row in rows for k in row)) or ['estado']
    with path.open('w', encoding='utf-8-sig', newline='') as stream:
        writer = csv.DictWriter(stream, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


class CompressedTable:
    def __init__(self, name):
        self.raw = (HERE / name).open('wb')
        self.gz = gzip.GzipFile(filename='', mode='wb', fileobj=self.raw, mtime=0)
        self.stream = io.TextIOWrapper(self.gz, encoding='utf-8', newline='')
        self.writer = None
        self.count = 0

    def write(self, row):
        if self.writer is None:
            self.writer = csv.DictWriter(self.stream, fieldnames=list(row))
            self.writer.writeheader()
        self.writer.writerow(row)
        self.count += 1

    def close(self):
        self.stream.close()
        self.raw.close()


def period_label(month):
    year, month0 = divmod(int(month), 12)
    return f'{year:04d}-{month0 + 1:02d}'


def category(source, key):
    if source == 'EPM':
        return '|'.join(key[:2] + key[-1:])
    if source == 'CHEC':
        return '|'.join(key[:2] + key[3:4])
    if source == 'SSPD':
        return '|'.join(key[:2])
    return '|'.join(key)


def longest_run(period_values):
    """No concatena cambios de rachas separadas por meses ausentes."""
    runs = []
    for (year, month), values in sorted(period_values.items()):
        current = year * 12 + month - 1
        if not runs or current != runs[-1][-1][0] + 1:
            runs.append([])
        value = float(np.mean(values))
        if not (math.isfinite(value) and value > 0):
            raise ValueError('La capa de carga debe entregar valores positivos finitos')
        runs[-1].append((current, value))
    return max(runs, key=lambda run: (len(run), run[-1][0]))


def load_sources():
    datasets, inputs = {}, {}
    for source in SOURCES:
        path, raw = build_series(source)
        inputs[source] = {'ruta': path.relative_to(ROOT).as_posix(), 'sha256': sha256(path)}
        series = []
        for (key, measure), values in sorted(raw.items()):
            run = longest_run(values)
            sid = hashlib.sha256(json.dumps([source, key, measure], ensure_ascii=False).encode()).hexdigest()[:24]
            item = {'fuente': source, 'sid': sid, 'serie': '|'.join(key), 'key': key,
                    'medida': measure, 'categoria': category(source, key),
                    'meses': np.array([p for p, _ in run]),
                    'valores': np.array([v for _, v in run]), 'raw': values}
            series.append(item)
            row = {k: item[k] for k in ('fuente', 'sid', 'serie', 'medida', 'categoria')}
            row.update(meses_disponibles=len(values), meses_racha=len(run),
                       inicio_racha=period_label(run[0][0]), fin_racha=period_label(run[-1][0]))
            row.update({f'elegible_ref_{w}': int(len(run) >= w + WATCH + 1) for w in WINDOWS})
            add('inventario_series.csv', row)
        datasets[source] = series
    return datasets, inputs


def scales_from_reference(raw):
    center = np.median(raw, axis=0)
    scale = np.median(np.abs(raw - center), axis=0) / NORMAL_MEDIAN
    mean_deviation = np.mean(np.abs(raw - center), axis=0)
    scale = np.where(scale > 0, scale, mean_deviation)
    scale = np.where(scale > 0, scale, np.std(raw, axis=0))
    return center, np.where(scale > 0, scale, 1.0)


def raw_features(levels, changes, level_reference):
    previous = np.r_[0.0, changes[:-1]]
    return np.column_stack((changes, previous, np.abs(changes - previous),
                            np.log(levels[1:] / level_reference)))


def fit_series(item, window):
    levels = item['valores'][-(window + WATCH + 1):]
    months = item['meses'][-(window + WATCH + 1):]
    assert len(levels) == window + WATCH + 1
    assert np.all(np.diff(months) == 1)
    changes = np.diff(np.log(levels))
    ref = changes[:window]
    level_reference = float(np.median(levels[:window + 1]))
    raw = raw_features(levels, changes, level_reference)
    center, scale = scales_from_reference(raw[:window])
    return dict(item=item, levels=levels, months=months, changes=changes,
                mean=float(np.mean(ref)), mr_mean=float(np.mean(np.abs(np.diff(ref)))),
                median=float(np.median(ref)), mad=float(np.median(np.abs(ref - np.median(ref)))),
                level_reference=level_reference, center=center, scale=scale,
                features=(raw - center) / scale, window=window)


def local_predictions(params, current, previous, level):
    """Las posiciones de METHODS son parte del contrato de las tablas anchas."""
    p = params
    i_signal = np.abs(current - p['mean']) > 2.66 * p['mr_mean']
    mr_signal = np.abs(current - previous) > 3.267 * p['mr_mean']
    z_abs = np.abs(current - p['median']) * NORMAL_MEDIAN
    mad_signals = [z_abs > k * p['mad'] for k in (2.66, 3.0, 3.267)]
    # MAD=0 conserva el criterio de 4.1: distinto de la mediana -> señal.
    return np.column_stack([i_signal, mr_signal, i_signal | mr_signal, *mad_signals,
                            np.zeros_like(i_signal), np.zeros_like(i_signal),
                            *[np.abs(level) > f * p['level_reference'] for f in (5, 10, 20)]])


def cluster_intervals(categories, numerators, denominators):
    """Bootstrap de categorías completas; razón de totales, no promedio de tasas."""
    labels, inverse = np.unique(np.asarray(categories), return_inverse=True)
    if len(labels) < 2:
        return [(None, None)] * numerators.shape[1], 'sin_IC_menos_de_dos_categorias'
    totals = np.zeros((len(labels), numerators.shape[1] + 1))
    np.add.at(totals[:, :-1], inverse, numerators)
    np.add.at(totals[:, -1], inverse, denominators)
    key = tuple(labels)
    if key not in BOOT_WEIGHTS:
        seed = SEED + int(hashlib.sha256('|'.join(key).encode()).hexdigest()[:8], 16)
        rng = np.random.default_rng(seed)
        BOOT_WEIGHTS[key] = rng.multinomial(len(labels), np.full(len(labels), 1 / len(labels)), size=B)
    sampled = BOOT_WEIGHTS[key] @ totals
    rates = sampled[:, :-1] / sampled[:, -1, None]
    return [tuple(np.quantile(rates[:, j], [.025, .975])) for j in range(rates.shape[1])], 'bootstrap_categorias'


def build_cases(parameters, raw_lookup, window):
    cases = []
    omitted = []
    for index, p in enumerate(parameters):
        item = p['item']
        for t in range(WATCH - 1):
            pos = window + t + 1  # Posición en niveles; t se refiere a vigilancia.
            value = p['levels'][pos]
            month = int(p['months'][pos])
            options = {'decimal_x1000': value * 1000,
                       'decimal_div1000': value / 1000,
                       'serial_excel_43577': 43577.0,
                       'aumento_10pct': value * 1.10,
                       'valor_no_actualizado': p['levels'][pos - 1]}
            alternative = raw_lookup.get((item['key'], month, item['medida']))
            if alternative is not None:
                options['otra_medida'] = alternative
            else:
                omitted.append((index, t, 'otra_medida', 'sin_otra_medida_positiva_distinta'))
            for kind, new in options.items():
                if new == value:
                    omitted.append((index, t, kind, 'la_alteracion_no_cambia_el_valor'))
                    continue
                cases.append(dict(si=index, t=t, tipo=kind, nuevo=float(new), original=float(value),
                                  clase='individual', evento=''))
    # Prueba de estrés: alteraciones simultáneas, no evidencia de un cambio regulatorio.
    coverage = {}
    for index, p in enumerate(parameters):
        for t, month in enumerate(p['months'][window + 1:-1]):
            coverage.setdefault(int(month), []).append((index, t))
    if coverage:
        month, active = max(coverage.items(), key=lambda pair: (len(pair[1]), pair[0]))
        for kind, factor in (('masivo_10pct', 1.10), ('masivo_x1000', 1000.0)):
            for index, t in active:
                value = parameters[index]['levels'][window + t + 1]
                cases.append(dict(si=index, t=t, tipo=kind, nuevo=float(value * factor),
                                  original=float(value), clase='colectivo',
                                  evento=f'{kind}:{period_label(month)}'))
    return cases, omitted


def alternate_values(items):
    by_key_month = {}
    for item in items:
        for (year, month), values in item['raw'].items():
            by_key_month.setdefault((item['key'], year * 12 + month - 1), []).append((item['medida'], float(np.mean(values))))
    result = {}
    for (key, month), measures in by_key_month.items():
        measures = sorted(measures)
        for measure, value in measures:
            alternative = next((v for m, v in measures if m != measure and v != value), None)
            if alternative is not None:
                result[(key, month, measure)] = alternative
    return result


def fit_calendar_models(parameters, source, panel, window):
    groups = {}
    for index, p in enumerate(parameters):
        groups.setdefault(int(p['months'][-1]), []).append(index)
    bank = {}
    for anchor, indices in sorted(groups.items()):
        train = np.vstack([parameters[i]['features'][:window] for i in indices])
        max_ref = max(int(parameters[i]['months'][window]) for i in indices)
        min_watch = min(int(parameters[i]['months'][window+1]) for i in indices)
        assert max_ref < min_watch, 'Entrenamiento posterior a vigilancia de otra serie'
        model = IsolationForest(n_estimators=300, contamination='auto', max_samples=min(256,len(train)),
                                random_state=SEED, n_jobs=1)
        model.fit(train)
        scores = -model.score_samples(train)
        thresholds = np.quantile(scores, [.99,.995])
        bank[anchor] = (model, thresholds, indices)
        for i in indices:
            parameters[i]['if_anchor'] = anchor
            parameters[i]['if_thresholds'] = thresholds
        add('modelos_IF.csv', dict(fuente=source,cohorte=panel,referencia=window,
            fin_vigilancia=period_label(anchor),series=len(indices),observaciones_referencia=len(train),
            ultimo_mes_entrenamiento=period_label(max_ref),primer_mes_vigilancia=period_label(min_watch),
            umbral_p99=float(thresholds[0]),umbral_p99_5=float(thresholds[1]),
            max_samples=min(256,len(train)),arboles=300,semilla=SEED))
    return bank


def score_cases(parameters, cases, bank):
    result = np.zeros((len(cases), 2, len(METHODS)), dtype=bool)
    features = np.zeros((len(cases), 2, 4))
    for ci, case in enumerate(cases):
        p = parameters[case['si']]
        j = p['window'] + case['t']
        before = p['levels'][j]
        after = p['levels'][j + 2]
        d = math.log(case['nuevo']) - math.log(before)
        next_d = math.log(after) - math.log(case['nuevo'])
        previous = p['changes'][j - 1]
        current = np.array([d, next_d])
        prev = np.array([previous, d])
        levels = np.array([case['nuevo'], after])
        result[ci] = local_predictions(p, current, prev, levels)
        raw = np.column_stack((current, prev, np.abs(current - prev), np.log(levels / p['level_reference'])))
        features[ci] = (raw - p['center']) / p['scale']
    for anchor,(model,thresholds,_) in bank.items():
        ci = np.array([i for i,case in enumerate(cases) if parameters[case['si']]['if_anchor']==anchor],dtype=int)
        if len(ci):
            scores = -model.score_samples(features[ci].reshape(-1, 4)).reshape(len(ci), 2)
            result[ci, :, 6] = scores > thresholds[0]
            result[ci, :, 7] = scores > thresholds[1]
    return result


def verify_monotonic(predictions):
    assert np.all(predictions[..., 3] >= predictions[..., 4])
    assert np.all(predictions[..., 4] >= predictions[..., 5])
    assert np.all(predictions[..., 6] >= predictions[..., 7])
    assert np.all(predictions[..., 8] >= predictions[..., 9])
    assert np.all(predictions[..., 9] >= predictions[..., 10])


def summarize_scenario(source, panel, window, parameters, base, cases, injected, omitted,
                       real_writer, cases_writer, model_info):
    common = dict(fuente=source, cohorte=panel, referencia=window)
    cats = [p['item']['categoria'] for p in parameters]
    categories_count = len(set(cats))
    series_count = len(parameters)
    real_num = base.sum(axis=1)
    intervals, status = cluster_intervals(cats, real_num, np.full(series_count, WATCH))
    for mi, method in enumerate(METHODS):
        total = int(real_num[:, mi].sum())
        low, high = intervals[mi]
        add('tasas_alerta_reales.csv', dict(**common, metodo=method, series=series_count,
            categorias=categories_count, observaciones=series_count * WATCH, alertas=total,
            tasa_alerta=total / (series_count * WATCH), ic95_inferior=low, ic95_superior=high,
            estado_intervalo=status, etiqueta='alertas_reales_sin_verdad_terreno'))

    month_counts, baseline_counts = {}, {}
    for si, p in enumerate(parameters):
        item = p['item']
        for t, month in enumerate(p['months'][window + 1:]):
            month = int(month)
            month_counts[month] = month_counts.get(month, 0) + 1
            baseline_counts.setdefault(month, np.zeros(len(METHODS), dtype=int))
            baseline_counts[month] += base[si, t]
            row = dict(**common, sid=item['sid'], serie=item['serie'], medida=item['medida'],
                       categoria=item['categoria'], periodo=period_label(month))
            row.update({method: int(base[si, t, mi]) for mi, method in enumerate(METHODS)})
            real_writer.write(row)
        add('parametros_por_serie.csv', dict(**common, sid=item['sid'], serie=item['serie'],
            medida=item['medida'], categoria=item['categoria'],
            inicio_referencia=period_label(p['months'][1]), fin_referencia=period_label(p['months'][window]),
            inicio_vigilancia=period_label(p['months'][window + 1]), fin_vigilancia=period_label(p['months'][-1]),
            media_log=p['mean'], mr_medio=p['mr_mean'], mediana_log=p['median'], mad_log=p['mad'],
            estado_mad='mad_cero' if p['mad'] == 0 else 'mad_positivo',
            mediana_nivel_referencia=p['level_reference'],
            limite_I_inferior=p['mean'] - 2.66 * p['mr_mean'], limite_I_superior=p['mean'] + 2.66 * p['mr_mean'],
            limite_MR_superior=3.267 * p['mr_mean'], sigma_MAD=p['mad'] / NORMAL_MEDIAN,
            modelo_IF_fin_vigilancia=period_label(p['if_anchor']),
            umbral_IF_p99=float(p['if_thresholds'][0]),umbral_IF_p99_5=float(p['if_thresholds'][1])))

    for month, n in sorted(month_counts.items()):
        for mi, method in enumerate(METHODS):
            alerts = int(baseline_counts[month][mi])
            for x in SYSTEMIC:
                applicable = n >= 2
                systemic = applicable and alerts / n > x
                add('alertas_sistemicas_por_mes.csv', dict(**common, metodo=method, periodo=period_label(month),
                    umbral_fraccion=x, series_observadas=n, series_con_alerta=alerts,
                    fraccion_alerta=alerts / n, aplicable=int(applicable), candidato_sistemico=int(systemic),
                    alertas_retenidas=0 if systemic else alerts,
                    interpretacion='candidato_sin_confirmacion_regulatoria' if systemic else 'sin_reclasificacion'))
    for mi, method in enumerate(METHODS):
        raw = int(real_num[:, mi].sum())
        for x in SYSTEMIC:
            suppressed = sum(int(baseline_counts[month][mi]) for month, n in month_counts.items()
                             if n >= 2 and baseline_counts[month][mi] / n > x)
            add('efecto_regla_sistemica_reales.csv', dict(**common, metodo=method, umbral_fraccion=x,
                observaciones=series_count * WATCH, alertas_originales=raw, alertas_reclasificadas=suppressed,
                alertas_retenidas=raw - suppressed, tasa_original=raw / (series_count * WATCH),
                tasa_retenida=(raw - suppressed) / (series_count * WATCH),
                reduccion_puntos_porcentuales=100 * suppressed / (series_count * WATCH)))

    # Actualizar el contexto mensual del ensayo; en el estrés se alteran todas las series del evento.
    collective_counts = {}
    for ci, case in enumerate(cases):
        if case['clase'] != 'colectivo':
            continue
        p = parameters[case['si']]
        counts = collective_counts.setdefault(case['evento'], {m: c.copy() for m, c in baseline_counts.items()})
        for offset in (0, 1):
            month = int(p['months'][window + case['t'] + 1 + offset])
            counts[month] += injected[ci, offset].astype(int) - base[case['si'], case['t'] + offset].astype(int)

    systematic_stats = {}
    individual_indices = []
    novel = np.zeros_like(injected)
    for ci, case in enumerate(cases):
        p = parameters[case['si']]
        item = p['item']
        t = case['t']
        original_flags = base[case['si'], t:t + 2]
        novel[ci] = injected[ci] & ~original_flags
        if case['clase'] == 'individual':
            individual_indices.append(ci)
        row = dict(**common, caso_id=f"{item['sid']}:{period_label(p['months'][window+t+1])}:{case['tipo']}",
                   sid=item['sid'], serie=item['serie'], medida=item['medida'], categoria=item['categoria'],
                   periodo_t=period_label(p['months'][window+t+1]), tipo=case['tipo'],
                   clase_ensayo=case['clase'], evento=case['evento'],
                   valor_original=case['original'], valor_inyectado=case['nuevo'])
        for mi, method in enumerate(METHODS):
            row[method + '_t'] = int(injected[ci, 0, mi])
            row[method + '_t1'] = int(injected[ci, 1, mi])
            row[method + '_nueva_t'] = int(novel[ci, 0, mi])
            row[method + '_nueva_t1'] = int(novel[ci, 1, mi])
        cases_writer.write(row)
        for x in SYSTEMIC:
            kept = injected[ci].copy()
            for offset in (0, 1):
                month = int(p['months'][window + t + 1 + offset])
                n = month_counts[month]
                if case['clase'] == 'colectivo':
                    counts = collective_counts[case['evento']][month]
                else:
                    counts = baseline_counts[month] + injected[ci, offset].astype(int) - original_flags[offset].astype(int)
                if n >= 2:
                    kept[offset] &= ~(counts / n > x)
            for mi, method in enumerate(METHODS):
                key = (case['clase'], case['tipo'], case['evento'], x, method)
                stat = systematic_stats.setdefault(key, np.zeros(5, dtype=int))
                stat += [1, injected[ci, 0, mi], injected[ci, :, mi].any(),
                         kept[0, mi], kept[:, mi].any()]

    for kind in sorted({cases[i]['tipo'] for i in individual_indices}):
        idx = np.array([i for i in individual_indices if cases[i]['tipo'] == kind])
        case_cats = [parameters[cases[i]['si']]['item']['categoria'] for i in idx]
        n = len(idx)
        for mi, method in enumerate(METHODS):
            at_t = injected[idx, 0, mi]
            at_both = injected[idx, :, mi].any(axis=1)
            new_t = novel[idx, 0, mi]
            new_both = novel[idx, :, mi].any(axis=1)
            nums = np.column_stack((at_t, at_both, at_both.astype(int) - at_t, new_t, new_both))
            ints, state = cluster_intervals(case_cats, nums, np.ones(n))
            add('deteccion_inyecciones.csv', dict(**common, tipo=kind, metodo=method, casos=n,
                series=len({cases[i]['si'] for i in idx}), categorias=len(set(case_cats)),
                detecciones_t=int(at_t.sum()), detecciones_t_o_t1=int(at_both.sum()),
                tasa_t=float(at_t.mean()), tasa_t_o_t1=float(at_both.mean()),
                ganancia_horizonte=float(at_both.mean() - at_t.mean()),
                ic95_t_inferior=ints[0][0], ic95_t_superior=ints[0][1],
                ic95_t_o_t1_inferior=ints[1][0], ic95_t_o_t1_superior=ints[1][1],
                ic95_ganancia_inferior=ints[2][0], ic95_ganancia_superior=ints[2][1],
                detecciones_nuevas_t=int(new_t.sum()), detecciones_nuevas_t_o_t1=int(new_both.sum()),
                tasa_nueva_t=float(new_t.mean()), tasa_nueva_t_o_t1=float(new_both.mean()),
                estado_intervalo=state))
    for (kind, error, event, x, method), (n, t, both, kt, kb) in systematic_stats.items():
        assert kt <= t and kb <= both
        add('efecto_regla_sistemica_inyecciones.csv', dict(**common, clase_ensayo=kind,
            tipo=error, evento=event, umbral_fraccion=x, metodo=method, casos=int(n),
            detecciones_t=int(t), detecciones_t_o_t1=int(both),
            retenidas_t=int(kt), retenidas_t_o_t1=int(kb),
            detecciones_enmascaradas_t_o_t1=int(both - kb),
            tasa_original_t_o_t1=both / n, tasa_retenida_t_o_t1=kb / n,
            fraccion_detecciones_enmascaradas=(both - kb) / both if both else None))
    # Interacción explícita de cartas, percentil IF y factor R12 por unión de señales.
    individual = np.array(individual_indices, dtype=int)
    for chart_index in (2, 4):
        for if_index in (6, 7):
            for r12_index in (8, 9, 10):
                indices = [chart_index, if_index, r12_index]
                real_combined = base[:, :, indices].any(axis=2)
                trial_combined = injected[individual][:, :, indices].any(axis=2)
                combined_intervals, combined_state = cluster_intervals(cats,
                    real_combined.sum(axis=1)[:,None], np.full(series_count, WATCH))
                low, high = combined_intervals[0]
                add('combinaciones_framework.csv', dict(**common, cartas=METHODS[chart_index],
                    percentil_IF=99 if if_index==6 else 99.5, factor_R12={8:5,9:10,10:20}[r12_index],
                    series=series_count, observaciones=series_count*WATCH,
                    alertas=int(real_combined.sum()), tasa_alerta=float(real_combined.mean()),
                    ic95_inferior=low, ic95_superior=high, estado_intervalo=combined_state,
                    casos_inyectados=len(individual), detecciones_t=int(trial_combined[:,0].sum()),
                    detecciones_t_o_t1=int(trial_combined.any(axis=1).sum()),
                    tasa_deteccion_t=float(trial_combined[:,0].mean()),
                    tasa_deteccion_t_o_t1=float(trial_combined.any(axis=1).mean())))
    for si, t, kind, reason in omitted:
        item = parameters[si]['item']
        add('inyecciones_omitidas.csv', dict(**common, sid=item['sid'], tipo=kind,
            periodo_t=period_label(parameters[si]['months'][window+t+1]), motivo=reason))

    return {p['item']['sid']: (p['item']['categoria'], base[i].sum(axis=0),
                              tuple(p['months'][window+1:])) for i, p in enumerate(parameters)}


def run_scenario(source, panel, window, items, lookup, real_writer, cases_writer):
    started = time.perf_counter()
    params = [fit_series(item, window) for item in items]
    bank = fit_calendar_models(params, source, panel, window)
    base = np.stack([local_predictions(p, p['changes'][window:], p['changes'][window-1:-1],
                                      p['levels'][window+1:]) for p in params])
    for _, (model, thresholds, indices) in bank.items():
        watch_features = np.vstack([params[i]['features'][window:] for i in indices])
        watch_scores = -model.score_samples(watch_features).reshape(len(indices), WATCH)
        base[indices, :, 6] = watch_scores > thresholds[0]
        base[indices, :, 7] = watch_scores > thresholds[1]
    cases, omitted = build_cases(params, lookup, window)
    injected = score_cases(params, cases, bank)
    verify_monotonic(base)
    verify_monotonic(injected)
    info = dict(fuente=source, cohorte=panel, referencia=window, series=len(params),
                observaciones_referencia=len(params)*window, observaciones_vigilancia=len(params)*WATCH,
                modelos_calendario=len(bank),
                casos_individuales=sum(c['clase']=='individual' for c in cases),
                casos_colectivos=sum(c['clase']=='colectivo' for c in cases),
                series_mad_cero=sum(p['mad']==0 for p in params))
    result = summarize_scenario(source, panel, window, params, base, cases, injected, omitted,
                                real_writer, cases_writer, info)
    info['segundos'] = time.perf_counter() - started
    add('ejecuciones.csv', info)
    print(f"{source} {panel} ref={window}: series={len(params)}, casos={len(cases)}, {info['segundos']:.1f}s", flush=True)
    return result


def paired_comparison(results):
    for source in SOURCES:
        reference = results.get((source, 'comun', 36), {})
        for window in (24, 48):
            alternative = results.get((source, 'comun', window), {})
            sids = sorted(reference.keys() & alternative.keys())
            if not sids:
                add('comparacion_ventanas_pareada.csv', dict(fuente=source, referencia_base=36,
                    referencia_alternativa=window, estado='no_evaluable_sin_cohorte_comun', series=0))
                continue
            for sid in sids:
                assert reference[sid][2] == alternative[sid][2]
            categories = [reference[sid][0] for sid in sids]
            differences = np.stack([alternative[sid][1]-reference[sid][1] for sid in sids])
            intervals, status = cluster_intervals(categories, differences, np.full(len(sids), WATCH))
            for mi, method in enumerate(METHODS):
                low, high = intervals[mi]
                add('comparacion_ventanas_pareada.csv', dict(fuente=source, referencia_base=36,
                    referencia_alternativa=window, estado='mismas_series_y_mismos_meses', metodo=method,
                    series=len(sids), categorias=len(set(categories)), observaciones=len(sids)*WATCH,
                    diferencia_tasa=float(differences[:,mi].sum()/(len(sids)*WATCH)),
                    ic95_inferior=low, ic95_superior=high, estado_intervalo=status))


def main():
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
    datasets, inputs = load_sources()
    quarantine = (_PROJECT_ROOT / 'Outputs/cuarentena_bootstrap/EPM/cuarentena_registros.csv')
    originals = {ROOT / entry['ruta']: entry['sha256'] for entry in inputs.values()}
    originals[quarantine] = sha256(quarantine)
    real_writer = CompressedTable('alertas_reales_detalle.csv.gz')
    cases_writer = CompressedTable('inyecciones_detalle.csv.gz')
    results = {}
    for source, all_items in datasets.items():
        lookup = alternate_values(all_items)
        available = {w: [item for item in all_items if len(item['meses']) >= w+WATCH+1] for w in WINDOWS}
        feasible = [w for w in WINDOWS if available[w]]
        common_items = available[max(feasible)] if feasible else []
        for panel in ('disponible', 'comun'):
            for window in WINDOWS:
                items = available[window] if panel=='disponible' else common_items if window in feasible else []
                add('cobertura_ventanas.csv', dict(fuente=source, cohorte=panel, referencia=window,
                    vigilancia=WATCH, minimo_meses=window+WATCH+1, series_candidatas=len(all_items),
                    series_elegibles=len(items), categorias=len({i['categoria'] for i in items}),
                    estado='evaluable' if items else 'no_evaluable_sin_longitud_suficiente',
                    ventanas_comunes='|'.join(map(str,feasible))))
                if not items:
                    continue
                results[(source,panel,window)] = run_scenario(source,panel,window,items,lookup,real_writer,cases_writer)
    real_writer.close()
    cases_writer.close()
    paired_comparison(results)
    for name, rows in TABLES.items():
        write_table(name, rows)
    for path, before in originals.items():
        assert sha256(path) == before, f'Se modificó la entrada {path}'
    config = {'fecha_cliente':'2026-11-06', 'semilla':SEED, 'referencias':WINDOWS,
        'vigilancia':WATCH, 'origenes_inyeccion':'todos los primeros 11 meses; sin reemplazo; último mes solo seguimiento',
        'paneles':{'disponible':'todas las series elegibles por ventana',
                   'comun':'mismas series en todas las ventanas viables de cada fuente; SSPD solo 24 y 36'},
        'anclaje':'últimos 12 cambios de la racha consecutiva más larga; desempate por fin más reciente',
        'normalizacion_MAD':NORMAL_MEDIAN,'I_coeficiente':2.66,'MR_coeficiente':3.267,
        'multiplicadores_MAD':[2.66,3.0,3.267], 'percentiles_IF':[.99,.995],
        'IF_arboles':300,'IF_max_samples':256,'IF_n_jobs':1,
        'IF_ajuste':'modelo por fuente/ventana/cohorte/calendario de vigilancia; último entrenamiento anterior a primera vigilancia del modelo; escalas y umbrales solo con referencia',
        'IF_max_samples_efectivo':'min(256, observaciones de referencia del grupo de calendario)',
        'rasgos_IF':['cambio_log','cambio_log_anterior','diferencia_absoluta_cambios','nivel_log_relativo_mediana_referencia'],
        'factores_R12':[5,10,20],'R12':'abs(nivel) > factor * mediana(abs(niveles_referencia)); no usa vigilancia',
        'umbrales_sistemicos':SYSTEMIC,'regla_sistemica':'fracción estrictamente mayor que X; mínimo 2 series observadas por fuente/método/mes',
        'bootstrap':{'repeticiones':B,'unidad':'categoría completa dentro de fuente; se remuestrean numeradores y denominadores juntos',
                     'intervalo':'percentil 2.5 y 97.5; sin IC si hay menos de dos categorías; descriptivo condicional al snapshot'},
        'MAD_cero':'señal si el cambio difiere de la mediana; no se añade epsilon',
        'verdad_terreno':'solo la perturbación artificial; las alertas reales carecen de etiquetas completas',
        'entradas':inputs,'cuarentena_EPM':{'ruta':quarantine.relative_to(ROOT).as_posix(),'sha256':sha256(quarantine)},
        'dependencias':{p.relative_to(ROOT).as_posix():sha256(p) for p in (
            (_PROJECT_ROOT / 'Docs/Antecedentes/plan_hitos_3-6_detallado.txt'),
            (_PROJECT_ROOT / 'Code/Modeling/detectores/zscore_robusto.py'))},
        'versiones':{'python':platform.python_version(),'numpy':np.__version__,'pandas':pd.__version__,'sklearn':sklearn.__version__},
        'detalle':{'alertas_reales':real_writer.count,'inyecciones':cases_writer.count},
        'verificaciones':['entradas_intactas','rachas_consecutivas','mismos_meses_en_panel_comun',
                          'monotonia_MAD_IF_R12','reclasificacion_no_aumenta_detecciones',
                          'ultimo_entrenamiento_IF_anterior_a_toda_vigilancia_del_modelo']}
    ((_PROJECT_ROOT / 'Outputs/sensibilidad/configuracion.json')).write_text(json.dumps(config,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    from informe_sensibilidad import generate
    generate()
    artifacts=[]
    for path in sorted(HERE.rglob('*')):
        if path.is_file() and path.name!='manifiesto_resultados.json' and '__pycache__' not in path.parts:
            artifacts.append({'archivo':path.relative_to(HERE).as_posix(),'bytes':path.stat().st_size,'sha256':sha256(path)})
    ((_PROJECT_ROOT / 'Outputs/sensibilidad/manifiesto_resultados.json')).write_text(json.dumps({'entradas':inputs,'archivos':artifacts},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(f'Finalizado: {real_writer.count} observaciones y {cases_writer.count} inyecciones; resultados en {HERE}',flush=True)


if __name__=='__main__':
    main()
