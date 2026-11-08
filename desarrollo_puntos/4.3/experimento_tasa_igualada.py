"""Hito 4.3: precisión, recall y F1 a tasa de alerta igualada, curvas y sorteo sin reemplazo.

Solo escribe en 4.3. Reutiliza de 4.2 la carga de series, las inyecciones y los modelos
Isolation Forest, de modo que el experimento sea comparable y verificable contra sus tablas.
Añade lo que 4.1 dejó pendiente: LOF y KNN (plan, Hito 4, actividad 1) como métodos de
comparación, y puntajes continuos para poder igualar la tasa de alerta de todos los métodos.
"""
from __future__ import annotations

import csv
import gzip
import io
import json
import math
import platform
import sys
import time
import warnings
import zlib
from pathlib import Path

import numpy as np
import pandas as pd
import sklearn
from sklearn.neighbors import LocalOutlierFactor, NearestNeighbors

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.dont_write_bytecode = True
sys.path.insert(0, str(HERE.parent / '4.2'))
sys.path.insert(0, str(HERE.parent / '4.4'))   # equivalencias de etiquetas EPM (una sola implementación)
sys.path.insert(0, str(HERE))
import analisis_sensibilidad as A  # noqa: E402  (carga 4.1 y define el protocolo común)
import regla_sistemica as R44  # noqa: E402  (solo para canonical_epm_items)
from metricas_base import (ERROR_TYPES, METHODS, METHOD_LABELS, f1_score,  # noqa: E402
                           imr_score, level_ratio_score, observed_rate, positive_scale,
                           precision_at_prevalence, robust_z_score, threshold_for_rate,
                           draw_distinct_origins, NORMAL_MEDIAN)

SEED = 20261107
WINDOW = 36
WATCH = A.WATCH
SOURCES = A.SOURCES
HEAD_ALPHAS = (0.01, 0.02, 0.05, 0.10)
HEADLINE_ALPHA = 0.05
CURVE_ALPHAS = tuple(float(x) for x in np.geomspace(0.0025, 0.30, 40))
PREVALENCES = (0.01, 0.05, 0.10)
BOOTSTRAPS = 1000
REPLICATES = 500
DRAW_K = 3
LOF_K = 20
KNN_K = 5
MIN_EXPECTED_ALERTS = 5
LOF_EXPLODED = 1e6   # LOF numérico estalla (~1e9-1e10) cuando hay más duplicados exactos que vecinos
HORIZONS = ('t', 't_o_t1')
M = len(METHODS)
K = len(ERROR_TYPES)
TABLES: dict[str, list[dict]] = {}
SERIES_CONST: dict = {}
DETAIL_BASE = DETAIL_CASES = None


def add(name, row):
    TABLES.setdefault(name, []).append(row)


def write_table(name, rows):
    fields = list(dict.fromkeys(key for row in rows for key in row)) or ['estado']
    with (HERE / name).open('w', encoding='utf-8-sig', newline='') as stream:
        writer = csv.DictWriter(stream, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


class GzipTable:
    def __init__(self, name):
        self.raw = (HERE / name).open('wb')
        gz = gzip.GzipFile(filename='', mode='wb', fileobj=self.raw, mtime=0)
        self.stream = io.TextIOWrapper(gz, encoding='utf-8', newline='')
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


# ------------------------------------------------------------------ preparación
def select_items(all_items):
    """Panel común con referencia 36, igual que en 4.2 (EPM 27, CHEC 276, SSPD 321, XM 1)."""
    available = {w: [i for i in all_items if len(i['meses']) >= w + WATCH + 1] for w in A.WINDOWS}
    feasible = [w for w in A.WINDOWS if available[w]]
    common = available[max(feasible)] if feasible else []
    return common if WINDOW in feasible else []


def series_constants(params):
    n = len(params)
    const = {k: np.zeros(n) for k in ('mean', 'mr_scale', 'median', 'sigma', 'level_ref')}
    center, scale = np.zeros((n, 4)), np.zeros((n, 4))
    for i, p in enumerate(params):
        ref = p['changes'][:WINDOW]
        const['mean'][i] = p['mean']
        const['mr_scale'][i] = positive_scale(p['mr_mean'], ref)
        const['median'][i] = p['median']
        const['sigma'][i] = positive_scale(p['mad'] / NORMAL_MEDIAN, ref)
        const['level_ref'][i] = p['level_reference']
        center[i], scale[i] = p['center'], p['scale']
    const['center'], const['scale'] = center, scale
    return const


def fit_auxiliary_models(params, bank):
    """LOF y KNN con el mismo conjunto de entrenamiento y calendario que cada IF."""
    aux, rows, unique = {}, 0, 0
    for anchor, (_, _, indices) in bank.items():
        train = np.vstack([params[i]['features'][:WINDOW] for i in indices])
        lof = LocalOutlierFactor(n_neighbors=min(LOF_K, len(train) - 1), novelty=True).fit(train)
        knn = NearestNeighbors(n_neighbors=min(KNN_K, len(train))).fit(train)
        aux[anchor] = (lof, knn)
        rows += len(train)
        unique += len(np.unique(train.round(12), axis=0))
    return aux, dict(filas=rows, filas_unicas=unique)


def score_all(params, bank, aux, si, current, previous, levels, features):
    """Puntajes continuos (n, horizontes, métodos). Más alto = más anómalo, en todos."""
    n, horizons = current.shape
    out = np.zeros((n, horizons, M))
    c = SERIES_CONST
    out[:, :, 0] = imr_score(current, previous, c['mean'][si][:, None], c['mr_scale'][si][:, None])
    out[:, :, 1] = robust_z_score(current, c['median'][si][:, None], c['sigma'][si][:, None])
    out[:, :, 5] = level_ratio_score(levels, c['level_ref'][si][:, None])
    anchors = np.array([p['if_anchor'] for p in params])[si]
    for anchor, (model, _, _) in bank.items():
        rows = np.where(anchors == anchor)[0]
        if not len(rows):
            continue
        x = features[rows].reshape(-1, 4)
        out[rows, :, 2] = (-model.score_samples(x)).reshape(len(rows), horizons)
        lof, knn = aux[anchor]
        out[rows, :, 3] = (-lof.score_samples(x)).reshape(len(rows), horizons)
        out[rows, :, 4] = knn.kneighbors(x)[0].mean(axis=1).reshape(len(rows), horizons)
    assert np.isfinite(out).all(), 'Puntaje no finito: revisar duplicados o escalas'
    return out


def base_inputs(params):
    n = len(params)
    si = np.repeat(np.arange(n), WATCH)
    current = np.concatenate([p['changes'][WINDOW:] for p in params])[:, None]
    previous = np.concatenate([p['changes'][WINDOW - 1:-1] for p in params])[:, None]
    levels = np.concatenate([p['levels'][WINDOW + 1:] for p in params])[:, None]
    features = np.concatenate([p['features'][WINDOW:] for p in params])[:, None, :]
    return si, current, previous, levels, features


def case_inputs(params, cases):
    n = len(cases)
    current, previous, levels = np.zeros((n, 2)), np.zeros((n, 2)), np.zeros((n, 2))
    features = np.zeros((n, 2, 4))
    si = np.array([c['si'] for c in cases], dtype=int)
    for ci, case in enumerate(cases):
        p = params[case['si']]
        j = p['window'] + case['t']
        before, after = p['levels'][j], p['levels'][j + 2]
        d = math.log(case['nuevo']) - math.log(before)
        next_d = math.log(after) - math.log(case['nuevo'])
        current[ci] = (d, next_d)
        previous[ci] = (p['changes'][j - 1], d)
        levels[ci] = (case['nuevo'], after)
    raw = np.stack((current, previous, np.abs(current - previous),
                    np.log(levels / SERIES_CONST['level_ref'][si][:, None])), axis=2)
    features = (raw - SERIES_CONST['center'][si][:, None, :]) / SERIES_CONST['scale'][si][:, None, :]
    return si, current, previous, levels, features


# --------------------------------------------------------------- agregaciones
def pair_any(alert, n_series):
    """(n_series*12, ...) -> pares de meses consecutivos (n_series*11, ...)."""
    shaped = alert.reshape(n_series, WATCH, *alert.shape[1:])
    return (shaped[:, :-1] | shaped[:, 1:]).reshape(n_series * (WATCH - 1), *alert.shape[1:])


def hits_matrix(case_scores, thresholds):
    """(n, M, A, 2): detección en t y en t o t+1 para cada umbral igualado."""
    first = case_scores[:, 0, :, None] > thresholds[None, :, :]
    second = case_scores[:, 1, :, None] > thresholds[None, :, :]
    return np.stack((first, first | second), axis=3)


def category_totals(cat_cases, typ_cases, hits, cat_base, base_alert, cat_pair, pair_alert, G):
    num = np.zeros((G, K) + hits.shape[1:])
    np.add.at(num, (cat_cases, typ_cases), hits.astype(float))
    den = np.zeros((G, K))
    np.add.at(den, (cat_cases, typ_cases), 1.0)
    fp_t = np.zeros((G,) + base_alert.shape[1:])
    np.add.at(fp_t, cat_base, base_alert.astype(float))
    fp_2 = np.zeros((G,) + pair_alert.shape[1:])
    np.add.at(fp_2, cat_pair, pair_alert.astype(float))
    den_t = np.bincount(cat_base, minlength=G).astype(float)
    den_2 = np.bincount(cat_pair, minlength=G).astype(float)
    return num, den, fp_t, fp_2, den_t, den_2


def macro_and_fpr(num, den, fp_t, fp_2, den_t, den_2, weights=None):
    """TPR por tipo, TPR macro (tipos con igual peso) y FPR por horizonte."""
    w = np.ones(num.shape[0]) if weights is None else weights
    n_t, d = np.tensordot(w, num, axes=(0, 0)), w @ den
    with np.errstate(divide='ignore', invalid='ignore'):
        tpr_k = np.where(d[:, None, None, None] > 0, n_t / d[:, None, None, None], np.nan)
        fpr_t = (w @ fp_t.reshape(len(w), -1)) / (w @ den_t)
        fpr_2 = (w @ fp_2.reshape(len(w), -1)) / (w @ den_2)
    shape = fp_t.shape[1:]
    fpr = np.stack((fpr_t.reshape(shape), fpr_2.reshape(shape)), axis=-1)
    with warnings.catch_warnings():
        warnings.simplefilter('ignore', RuntimeWarning)
        macro = np.nanmean(tpr_k, axis=0)
    return tpr_k, macro, fpr


def derived_metrics(macro, fpr, prevalence):
    precision = precision_at_prevalence(macro, fpr, prevalence)
    return precision, f1_score(precision, macro)


def interval(samples):
    with warnings.catch_warnings():
        warnings.simplefilter('ignore', RuntimeWarning)
        return np.nanpercentile(samples, [2.5, 97.5], axis=0)


# --------------------------------------------------------------------- escenario
def run_source(source, all_items, verify=True):
    timing = {}
    started = time.perf_counter()
    items = select_items(all_items)
    if not items:
        return None
    lookup = A.alternate_values(all_items)
    params = [A.fit_series(item, WINDOW) for item in items]
    bank = A.fit_calendar_models(params, source, 'comun', WINDOW)
    aux, train_stats = fit_auxiliary_models(params, bank)
    global SERIES_CONST
    SERIES_CONST = series_constants(params)
    timing['ajuste_modelos'] = time.perf_counter() - started

    n_series = len(params)
    categories = sorted({p['item']['categoria'] for p in params})
    G = len(categories)
    cat_series = np.array([categories.index(p['item']['categoria']) for p in params])

    t0 = time.perf_counter()
    cases_all, omitted = A.build_cases(params, lookup, WINDOW)
    individual_positions = [i for i, c in enumerate(cases_all) if c['clase'] == 'individual']
    cases = [cases_all[i] for i in individual_positions]
    typ = np.array([ERROR_TYPES.index(c['tipo']) for c in cases], dtype=int)
    si_c, cur_c, prev_c, lev_c, feat_c = case_inputs(params, cases)
    S_case = score_all(params, bank, aux, si_c, cur_c, prev_c, lev_c, feat_c)
    si_b, cur_b, prev_b, lev_b, feat_b = base_inputs(params)
    S_base = score_all(params, bank, aux, si_b, cur_b, prev_b, lev_b, feat_b)[:, 0, :]
    timing['puntajes'] = time.perf_counter() - t0

    case_ids = [f"{params[c['si']]['item']['sid']}:{A.period_label(params[c['si']]['months'][WINDOW + c['t'] + 1])}:{c['tipo']}"
                for c in cases]
    verification = (verify_against_42(source, params, bank, cases_all, individual_positions, S_case, S_base, case_ids)
                    if verify else None)   # la variante canónica no existe en 4.2: no hay con qué compararla

    # ---- tasa igualada: un umbral por método y tasa objetivo, calculado en puntajes reales
    t0 = time.perf_counter()
    all_alphas = tuple(sorted(set(HEAD_ALPHAS) | set(CURVE_ALPHAS)))
    thr_all = np.array([[threshold_for_rate(S_base[:, m], a) for a in all_alphas] for m in range(M)])
    head_index = [all_alphas.index(a) for a in HEAD_ALPHAS]
    thr_head = thr_all[:, head_index]
    n_obs = S_base.shape[0]
    lof_exploded = float((S_base[:, METHODS.index('LOF')] > LOF_EXPLODED).mean())
    lof_degenerate = lof_exploded >= HEAD_ALPHAS[0]

    def method_status(method, alpha):
        """Estado de interpretabilidad de una celda método × tasa; no altera el cálculo."""
        if alpha * n_obs < MIN_EXPECTED_ALERTS:
            return 'no_interpretable_baja_resolucion'
        if method == 'LOF' and lof_degenerate:
            return 'degenerado_por_duplicados'
        return 'evaluable'

    for m, method in enumerate(METHODS):
        for ai, alpha in enumerate(HEAD_ALPHAS):
            observed = observed_rate(S_base[:, m], thr_head[m, ai])
            rate_status = ('tasa_igualada' if abs(observed - alpha) <= 1.0 / n_obs + 1e-12
                           else 'tasa_inferior_por_empates')
            add('umbrales_tasa_igualada.csv', dict(
                fuente=source, metodo=method, tasa_objetivo=alpha, umbral=thr_head[m, ai],
                observaciones_reales=n_obs, alertas_reales=int((S_base[:, m] > thr_head[m, ai]).sum()),
                tasa_observada=observed, estado_tasa=rate_status,
                estado_metodo=method_status(method, alpha),
                etiqueta='alertas_reales_sin_verdad_terreno'))

    hits = hits_matrix(S_case, thr_head)                                  # (n, M, A, 2)
    base_alert = S_base[:, :, None] > thr_head[None, :, :]               # (n_obs, M, A)
    pair_alert = pair_any(base_alert, n_series)                           # (n_series*11, M, A)
    cat_cases = cat_series[si_c]
    cat_base = np.repeat(cat_series, WATCH)
    cat_pair = np.repeat(cat_series, WATCH - 1)
    totals = category_totals(cat_cases, typ, hits, cat_base, base_alert, cat_pair, pair_alert, G)
    num, den, fp_t, fp_2, den_t, den_2 = totals
    present = den.sum(axis=0) > 0
    tpr_k, macro, fpr = macro_and_fpr(*totals)

    # ---- bootstrap por categoría completa (mismo remuestreo para TPR y FPR)
    rng = np.random.default_rng(SEED + zlib.crc32(source.encode()))
    ci_available = G >= 2
    if ci_available:
        W = rng.multinomial(G, np.full(G, 1.0 / G), size=BOOTSTRAPS).astype(float)
        boot_tpr_k = np.zeros((BOOTSTRAPS, K) + macro.shape)
        boot_macro = np.zeros((BOOTSTRAPS,) + macro.shape)
        boot_fpr = np.zeros((BOOTSTRAPS,) + fpr.shape)
        for b in range(BOOTSTRAPS):
            tk, mc, fp = macro_and_fpr(*totals, weights=W[b])
            boot_tpr_k[b], boot_macro[b], boot_fpr[b] = tk, mc, fp
        for k in np.where(~present)[0]:
            boot_tpr_k[:, k] = np.nan
        with warnings.catch_warnings():
            warnings.simplefilter('ignore', RuntimeWarning)
            boot_macro = np.nanmean(boot_tpr_k[:, present], axis=1)
    timing['tasa_igualada_y_bootstrap'] = time.perf_counter() - t0

    # ---- tablas: detección por tipo, métricas globales
    cat_names = {k: len({categories[g] for g in range(G) if den[g, k] > 0}) for k in range(K)}
    for k, error in enumerate(ERROR_TYPES):
        if not present[k]:
            continue
        idx = np.where(typ == k)[0]
        for m, method in enumerate(METHODS):
            for ai, alpha in enumerate(HEAD_ALPHAS):
                for hi, horizon in enumerate(HORIZONS):
                    low = high = None
                    if ci_available:
                        low, high = interval(boot_tpr_k[:, k, m, ai, hi])
                    add('deteccion_por_tipo_tasa_igualada.csv', dict(
                        fuente=source, metodo=method, tasa_objetivo=alpha, tipo=error, horizonte=horizon,
                        casos=int(len(idx)), series=int(len({si_c[i] for i in idx})),
                        categorias=cat_names[k], detecciones=int(hits[idx, m, ai, hi].sum()),
                        recall=float(tpr_k[k, m, ai, hi]), ic95_inferior=low, ic95_superior=high,
                        estado_metodo=method_status(method, alpha),
                        estado_intervalo='bootstrap_categorias' if ci_available else 'sin_IC_menos_de_dos_categorias'))
    for m, method in enumerate(METHODS):
        for ai, alpha in enumerate(HEAD_ALPHAS):
            for hi, horizon in enumerate(HORIZONS):
                for prevalence in PREVALENCES:
                    precision, f1 = derived_metrics(macro[m, ai, hi], fpr[m, ai, hi], prevalence)
                    row = dict(fuente=source, metodo=method, tasa_objetivo=alpha, horizonte=horizon,
                               prevalencia_supuesta=prevalence, recall_macro=float(macro[m, ai, hi]),
                               tasa_alerta_sin_error_conocido=float(fpr[m, ai, hi]),
                               precision_conservadora=float(precision), f1=float(f1))
                    if ci_available:
                        bp, bf = derived_metrics(boot_macro[:, m, ai, hi], boot_fpr[:, m, ai, hi], prevalence)
                        for name, samples in (('recall_macro', boot_macro[:, m, ai, hi]),
                                              ('tasa_alerta_sin_error_conocido', boot_fpr[:, m, ai, hi]),
                                              ('precision_conservadora', bp), ('f1', bf)):
                            lo, hi_ = interval(samples)
                            row[f'ic95_inferior_{name}'], row[f'ic95_superior_{name}'] = lo, hi_
                    row['estado_metodo'] = method_status(method, alpha)
                    row['estado_intervalo'] = 'bootstrap_categorias' if ci_available else 'sin_IC_menos_de_dos_categorias'
                    add('metricas_globales.csv', row)

    # ---- diferencias pareadas frente a I-MR (mismas categorías remuestreadas en ambos métodos)
    if ci_available:
        base_m = METHODS.index('IMR')
        for m, method in enumerate(METHODS):
            if m == base_m:
                continue
            for ai, alpha in enumerate(HEAD_ALPHAS):
                for hz, horizon in enumerate(HORIZONS):
                    for prevalence in PREVALENCES:
                        _, f1_method = derived_metrics(macro[m, ai, hz], fpr[m, ai, hz], prevalence)
                        _, f1_base = derived_metrics(macro[base_m, ai, hz], fpr[base_m, ai, hz], prevalence)
                        _, boot_f1_method = derived_metrics(boot_macro[:, m, ai, hz], boot_fpr[:, m, ai, hz], prevalence)
                        _, boot_f1_base = derived_metrics(boot_macro[:, base_m, ai, hz], boot_fpr[:, base_m, ai, hz], prevalence)
                        d_recall = boot_macro[:, m, ai, hz] - boot_macro[:, base_m, ai, hz]
                        d_f1 = boot_f1_method - boot_f1_base
                        r_lo, r_hi = interval(d_recall)
                        f_lo, f_hi = interval(d_f1)
                        add('diferencias_vs_IMR.csv', dict(
                            fuente=source, metodo=method, referencia='IMR', tasa_objetivo=alpha,
                            horizonte=horizon, prevalencia_supuesta=prevalence,
                            delta_recall=float(macro[m, ai, hz] - macro[base_m, ai, hz]),
                            ic95_inferior_delta_recall=r_lo, ic95_superior_delta_recall=r_hi,
                            delta_f1=float(f1_method - f1_base),
                            ic95_inferior_delta_f1=f_lo, ic95_superior_delta_f1=f_hi,
                            ic_f1_excluye_cero=int(f_lo > 0 or f_hi < 0),
                            estado_metodo=method_status(method, alpha),
                            comparaciones_multiples='sin_correccion'))

    # ---- curva de detección contra tasa de alerta (todas las tasas de la malla)
    hits_curve = hits_matrix(S_case, thr_all)
    macro_curve = np.zeros((M, len(all_alphas), 2))
    for k in np.where(present)[0]:
        sel = typ == k
        macro_curve += hits_curve[sel].mean(axis=0) / present.sum()
    for m, method in enumerate(METHODS):
        for ai, alpha in enumerate(all_alphas):
            add('curva_deteccion.csv', dict(
                fuente=source, metodo=method, tasa_objetivo=alpha,
                tasa_observada=observed_rate(S_base[:, m], thr_all[m, ai]),
                recall_macro_t=float(macro_curve[m, ai, 0]), recall_macro_t_o_t1=float(macro_curve[m, ai, 1]),
                estado_metodo=method_status(method, alpha)))

    # ---- puntos operativos nativos (umbral propio de cada método; sin IC)
    native = np.full((n_series, M), np.nan)
    native[:, 0], native[:, 1], native[:, 5] = 1.0, 3.0, 10.0
    native[:, 2] = [p['if_thresholds'][1] for p in params]
    native_cases = np.stack((S_case[:, 0, :] > native[si_c], S_case[:, 1, :] > native[si_c]), axis=1)
    native_hits = np.stack((native_cases[:, 0], native_cases[:, 0] | native_cases[:, 1]), axis=2)
    native_base = S_base > native[si_b]
    native_pair = pair_any(native_base, n_series)
    for m, method in enumerate(METHODS):
        if np.isnan(native[0, m]):
            continue
        for hi, horizon in enumerate(HORIZONS):
            recalls = [native_hits[typ == k, m, hi].mean() for k in np.where(present)[0]]
            macro_native = float(np.mean(recalls))
            fpr_native = float((native_base if hi == 0 else native_pair)[:, m].mean())
            for prevalence in PREVALENCES:
                precision, f1 = derived_metrics(macro_native, fpr_native, prevalence)
                add('puntos_operativos_nativos.csv', dict(
                    fuente=source, metodo=method, horizonte=horizon, umbral_nativo={
                        'IMR': 'puntaje>1 (2,66 y 3,267 del plan)', 'Z_robusto': '|z|>3',
                        'IF': 'percentil 99,5 de entrenamiento', 'R12': 'nivel>10 x mediana'}[method],
                    prevalencia_supuesta=prevalence, recall_macro=macro_native,
                    tasa_alerta_sin_error_conocido=fpr_native, precision_conservadora=float(precision),
                    f1=float(f1), etiqueta='sin_IC_punto_operativo_de_4_2'))

    # ---- sorteo sin reemplazo: k orígenes distintos por serie y réplica
    t0 = time.perf_counter()
    case_matrix = -np.ones((n_series, WATCH - 1, K), dtype=int)
    for ci, case in enumerate(cases):
        case_matrix[case['si'], case['t'], typ[ci]] = ci
    draw_rng = np.random.default_rng(SEED + 1 + zlib.crc32(source.encode()))
    indices, valid, chosen = draw_distinct_origins(case_matrix, DRAW_K, REPLICATES, draw_rng)
    unique_chosen = np.sort(np.where(valid, chosen, -1 - np.arange(DRAW_K)[None, None, :]), axis=2)
    assert np.all(unique_chosen[:, :, 1:] != unique_chosen[:, :, :-1]), 'El sorteo repitió un mes dentro de una serie'
    picked = hits[indices]                                                # (R, S, k, M, A, 2)
    weight = valid[..., None, None, None]
    tests_per_replicate = valid.sum(axis=(1, 2))
    draw_tpr = (picked * weight).sum(axis=(1, 2)) / tests_per_replicate[:, None, None, None]
    type_counts = np.zeros((REPLICATES, K))
    for k in range(K):
        type_counts[:, k] = ((typ[indices] == k) & valid).sum(axis=(1, 2))
    for m, method in enumerate(METHODS):
        for ai, alpha in enumerate(HEAD_ALPHAS):
            for hi, horizon in enumerate(HORIZONS):
                lo, hi_ = np.percentile(draw_tpr[:, m, ai, hi], [2.5, 97.5])
                add('sorteo_sin_reemplazo.csv', dict(
                    fuente=source, metodo=method, tasa_objetivo=alpha, horizonte=horizon,
                    replicas=REPLICATES, origenes_por_serie=DRAW_K,
                    pruebas_por_replica_media=float(tests_per_replicate.mean()),
                    recall_sorteo_media=float(draw_tpr[:, m, ai, hi].mean()),
                    recall_sorteo_p2_5=float(lo), recall_sorteo_p97_5=float(hi_),
                    estado_metodo=method_status(method, alpha),
                    recall_exhaustivo_macro=float(macro[m, ai, hi]),
                    diferencia_sorteo_menos_exhaustivo=float(draw_tpr[:, m, ai, hi].mean() - macro[m, ai, hi]),
                    meses_distintos_por_serie='todos_distintos_por_construccion'))
    timing['sorteo'] = time.perf_counter() - t0

    # ---- pruebas por tipo (denominadores honestos) y cobertura
    for k, error in enumerate(ERROR_TYPES):
        idx = np.where(typ == k)[0]
        months = {int(params[cases[i]['si']]['months'][WINDOW + cases[i]['t'] + 1]) for i in idx}
        add('pruebas_por_tipo.csv', dict(
            fuente=source, tipo=error, casos=int(len(idx)), series=int(len({si_c[i] for i in idx})),
            categorias=int(len({cat_cases[i] for i in idx})),
            meses_calendario_distintos=len(months),
            pruebas_por_replica_media=float(type_counts[:, k].mean()),
            estado='presente' if len(idx) else 'sin_casos_en_esta_fuente'))
    reasons = {}
    for _, _, kind, reason in omitted:
        reasons[(kind, reason)] = reasons.get((kind, reason), 0) + 1
    for (kind, reason), count in sorted(reasons.items()):
        add('inyecciones_omitidas.csv', dict(fuente=source, tipo=kind, motivo=reason, casos=count))
    add('cobertura_experimento.csv', dict(
        fuente=source, referencia=WINDOW, vigilancia=WATCH, series=n_series, categorias=G,
        observaciones_reales=n_obs, casos_individuales=len(cases),
        series_con_escala_MR_cero=int(sum(p['mr_mean'] == 0 for p in params)),
        series_con_MAD_cero=int(sum(p['mad'] == 0 for p in params)),
        modelos_calendario=len(bank), ic_disponible=int(ci_available),
        entrenamiento_filas=train_stats['filas'], entrenamiento_filas_unicas=train_stats['filas_unicas'],
        LOF_fraccion_puntajes_reales_explotados=lof_exploded,
        LOF_estado='degenerado_por_duplicados' if lof_degenerate else 'evaluable',
        nota='XM: una serie y una categoría; resultados descriptivos' if not ci_available else ''))

    # ---- detalle auditable (puntajes continuos)
    for i, p in enumerate(params):
        item = p['item']
        for j in range(WATCH):
            row = dict(fuente=source, sid=item['sid'], categoria=item['categoria'],
                       periodo=A.period_label(p['months'][WINDOW + 1 + j]))
            row.update({f'puntaje_{method}': float(S_base[i * WATCH + j, m]) for m, method in enumerate(METHODS)})
            DETAIL_BASE.write(row)
    for ci, case in enumerate(cases):
        p = params[case['si']]
        row = dict(fuente=source, caso_id=case_ids[ci], sid=p['item']['sid'], categoria=p['item']['categoria'],
                   periodo_t=A.period_label(p['months'][WINDOW + case['t'] + 1]), tipo=case['tipo'])
        for m, method in enumerate(METHODS):
            row[f'puntaje_{method}_t'] = float(S_case[ci, 0, m])
            row[f'puntaje_{method}_t1'] = float(S_case[ci, 1, m])
        DETAIL_CASES.write(row)

    timing['total'] = time.perf_counter() - started
    add('ejecuciones.csv', dict(fuente=source, series=n_series, casos=len(cases), observaciones_reales=n_obs,
                                modelos_calendario=len(bank), replicas=REPLICATES, bootstraps=BOOTSTRAPS,
                                **{f'segundos_{k}': v for k, v in timing.items()}))
    print(f"{source}: series={n_series}, casos={len(cases)}, obs={n_obs}, {timing['total']:.1f}s", flush=True)
    return verification


# -------------------------------------------------------- verificación contra 4.2
def verify_against_42(source, params, bank, cases_all, individual_positions, S_case, S_base, case_ids):
    """Las banderas nativas deben coincidir con las de 4.2; los puntajes, con sus umbrales."""
    native_42 = A.score_cases(params, cases_all, bank)[individual_positions]      # (n, 2, 11)
    si = np.array([cases_all[i]['si'] for i in individual_positions], dtype=int)
    mr_positive = np.array([p['mr_mean'] > 0 for p in params])[si]
    mad_positive = np.array([p['mad'] > 0 for p in params])[si]
    if_thr = np.array([p['if_thresholds'][1] for p in params])[si]
    pairs = {'IMR': (0, 2, 1.0, mr_positive), 'Z_robusto': (1, 4, 3.0, mad_positive),
             'IF': (2, 7, None, np.ones_like(mr_positive)), 'R12': (5, 9, 10.0, np.ones_like(mr_positive))}
    result = {'fuente': source, 'casos': int(len(si)), 'metodos': {}}
    for method, (mine, theirs, threshold, comparable) in pairs.items():
        limit = if_thr[:, None] if threshold is None else threshold
        mine_flags = S_case[:, :, mine] > limit
        diff = mine_flags != native_42[:, :, theirs]
        result['metodos'][method] = dict(
            discrepancias_total=int(diff.sum()), discrepancias_series_con_escala_positiva=int(diff[comparable].sum()),
            casos_comparables=int(comparable.sum() * 2))
        assert diff[comparable].sum() == 0, f'{source}/{method}: los puntajes no reproducen 4.2'
    # 4.2 guardó sus banderas; comprobar que A.score_cases es determinista respecto al archivo.
    detail = pd.read_csv(A.HERE / 'inyecciones_detalle.csv.gz', compression='gzip',
                         usecols=['fuente', 'cohorte', 'referencia', 'caso_id', 'clase_ensayo',
                                  'IMR_clasica_t', 'MAD_3sigma_t', 'IF_p99.5_t', 'R12_f10_t'])
    detail = detail[(detail.fuente == source) & (detail.cohorte == 'comun') &
                    (detail.referencia == WINDOW) & (detail.clase_ensayo == 'individual')].set_index('caso_id')
    mine_ids = pd.Series(range(len(case_ids)), index=case_ids)
    assert mine_ids.index.is_unique and set(mine_ids.index) == set(detail.index), 'Casos distintos a los de 4.2'
    order = mine_ids.loc[detail.index].to_numpy()
    for column, theirs in (('IMR_clasica_t', 2), ('MAD_3sigma_t', 4), ('IF_p99.5_t', 7), ('R12_f10_t', 9)):
        assert (native_42[order, 0, theirs].astype(int) == detail[column].to_numpy()).all(), column
    result['coincide_con_inyecciones_detalle_4_2'] = True
    return result


def sha256(path):
    return A.sha256(path)


def main():
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
    global DETAIL_BASE, DETAIL_CASES
    datasets, inputs = A.load_sources()
    quarantine = ROOT / 'desarrollo_puntos/3.7/EPM/cuarentena_registros.csv'
    guarded = {ROOT / e['ruta']: e['sha256'] for e in inputs.values()}
    guarded[quarantine] = sha256(quarantine)
    guarded[A.HERE / 'inyecciones_detalle.csv.gz'] = sha256(A.HERE / 'inyecciones_detalle.csv.gz')
    guarded[ROOT / 'desarrollo_puntos/3.3/insumos_hito2/02_catalogo_variantes.csv'] = sha256(ROOT / 'desarrollo_puntos/3.3/insumos_hito2/02_catalogo_variantes.csv')
    DETAIL_BASE = GzipTable('puntajes_reales.csv.gz')
    DETAIL_CASES = GzipTable('puntajes_inyecciones.csv.gz')
    verification = []
    for source in SOURCES:
        outcome = run_source(source, datasets[source])
        if outcome:
            verification.append(outcome)
    canonical_items, _, _ = R44.canonical_epm_items()
    run_source('EPM_canonicas', canonical_items, verify=False)
    DETAIL_BASE.close()
    DETAIL_CASES.close()
    for name, rows in TABLES.items():
        write_table(name, rows)
    for path, before in guarded.items():
        assert sha256(path) == before, f'Se modificó una entrada: {path}'
    (HERE / 'verificacion_contra_4_2.json').write_text(
        json.dumps({'estado': 'coincide', 'detalle': verification}, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    config = {
        'fecha_cliente': '2026-11-07', 'semilla': SEED, 'referencia': WINDOW, 'vigilancia': WATCH,
        'panel': 'comun, igual que el escenario principal de 4.2 (EPM 27, CHEC 276, SSPD 321, XM 1 series)',
        'variante_sensibilidad': 'EPM_canonicas: EPM con las equivalencias de etiquetas del Hito 2 (3.3/insumos_hito2/02_catalogo_variantes.csv), copia de trabajo; no existe en 4.2 y no se compara con él',
        'metodos': {m: METHOD_LABELS[m] for m in METHODS},
        'puntajes': {
            'IMR': 'max(|c-media|/(2,66*MR), |c-anterior|/(3,267*MR)); >1 equivale a la unión I o MR',
            'Z_robusto': '|c-mediana|/(MAD/0,6745); >3 equivale a MAD_3sigma de 4.2',
            'IF': '-score_samples del modelo de 4.2 (300 árboles, 4 rasgos, un modelo por calendario)',
            'LOF': f'-score_samples de LocalOutlierFactor(novelty=True, n_neighbors={LOF_K}) sobre los mismos rasgos',
            'KNN': f'distancia media a los {KNN_K} vecinos de referencia más cercanos, mismos rasgos',
            'R12': '|nivel| / mediana de referencia; el factor 5, 10 o 20 es el umbral'},
        'escala_de_respaldo': 'MAD o MR igual a cero: desviación absoluta media, luego desviación estándar, luego 1; solo para ordenar puntajes',
        'tasa_igualada': {'tasas_objetivo': HEAD_ALPHAS, 'tasa_destacada': HEADLINE_ALPHA,
                          'definicion': 'umbral = (floor(tasa*n)+1)-ésimo puntaje más alto de las observaciones reales de vigilancia de la fuente; sin etiquetas',
                          'no_interpretable_baja_resolucion': f'menos de {MIN_EXPECTED_ALERTS} alertas esperadas',
                          'LOF_degenerado': f'fracción de puntajes reales LOF > {LOF_EXPLODED:g} mayor o igual a {HEAD_ALPHAS[0]}'},
        'etiquetas': 'positivo = valor inyectado en t; negativo = observaciones reales sin inyección, incluidas las alertas reales sin error conocido',
        'horizontes': {'t': 'alerta en el mes inyectado (FPR sobre los 12 meses reales)',
                       't_o_t1': 'alerta en t o t+1 (FPR sobre pares de meses consecutivos, 11 por serie)'},
        'recall_global': 'macro: promedio de los recall por tipo, cada tipo con el mismo peso (mezcla uniforme de los seis tipos)',
        'prevalencias_supuestas': PREVALENCES,
        'bootstrap': {'repeticiones': BOOTSTRAPS, 'unidad': 'categoría completa dentro de la fuente; TPR y FPR remuestreados juntos',
                      'intervalo': 'percentiles 2,5 y 97,5; sin IC con menos de dos categorías'},
        'sorteo': {'replicas': REPLICATES, 'origenes_por_serie': DRAW_K,
                   'diseno': 'k meses de origen distintos por serie, sin reemplazo; un tipo de error uniforme por mes'},
        'entradas': inputs, 'cuarentena_EPM': {'ruta': quarantine.relative_to(ROOT).as_posix(), 'sha256': sha256(quarantine)},
        'dependencias': {p.relative_to(ROOT).as_posix(): sha256(p) for p in (
            ROOT / '0_Recomendaciones_profesor/plan_hitos_3-6_detallado.txt',
            ROOT / 'desarrollo_puntos/4.2/analisis_sensibilidad.py',
            ROOT / 'desarrollo_puntos/4.2/inyecciones_detalle.csv.gz',
            ROOT / 'desarrollo_puntos/4.1/zscore_robusto.py',
            ROOT / 'desarrollo_puntos/3.3/insumos_hito2/02_catalogo_variantes.csv',
            ROOT / 'desarrollo_puntos/4.4/regla_sistemica.py')},
        'versiones': {'python': platform.python_version(), 'numpy': np.__version__,
                      'pandas': pd.__version__, 'sklearn': sklearn.__version__},
        'detalle': {'puntajes_reales': DETAIL_BASE.count, 'puntajes_inyecciones': DETAIL_CASES.count}}
    (HERE / 'configuracion.json').write_text(json.dumps(config, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(f"Finalizado: {DETAIL_BASE.count} observaciones y {DETAIL_CASES.count} casos puntuados en {HERE}", flush=True)


if __name__ == '__main__':
    main()
