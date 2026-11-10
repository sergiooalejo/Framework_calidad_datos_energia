"""Audita 4.3: recalcula umbrales, detecciones y métricas desde los puntajes guardados."""
from __future__ import annotations

from pathlib import Path as _ProjectPath
_PROJECT_ROOT = next(p for p in _ProjectPath(__file__).resolve().parents if (p / "project.json").is_file())

import hashlib
import json
import os
import subprocess
import sys
from pathlib import Path

import numpy as np
import pandas as pd

HERE = (_PROJECT_ROOT / 'Outputs/metricas')
ROOT = _PROJECT_ROOT
sys.dont_write_bytecode = True
sys.path.insert(0, str((_PROJECT_ROOT / 'Code/Modeling/metricas')))
from metricas_base import (ERROR_TYPES, METHODS, f1_score, precision_at_prevalence,  # noqa: E402
                           threshold_for_rate)

TOL = 1e-12


def digest(path):
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1 << 20), b''):
            h.update(block)
    return h.hexdigest()


def main():
    sys.stdout.reconfigure(encoding='utf-8')
    config = json.loads(((_PROJECT_ROOT / 'Outputs/metricas/configuracion.json')).read_text(encoding='utf-8'))
    checks = []
    for entry in [*config['entradas'].values(), config['cuarentena_EPM']]:
        assert digest(ROOT / entry['ruta']) == entry['sha256'], entry['ruta']
    for path, expected in config['dependencias'].items():
        assert digest(ROOT / path) == expected, path
    checks.append('Datasets, cuarentena y dependencias conservan sus huellas')
    manifest = json.loads(((_PROJECT_ROOT / 'Outputs/metricas/manifiesto_resultados.json')).read_text(encoding='utf-8')) \
        if ((_PROJECT_ROOT / 'Outputs/metricas/manifiesto_resultados.json')).exists() else None

    alphas = tuple(config['tasa_igualada']['tasas_objetivo'])
    prevalences = tuple(config['prevalencias_supuestas'])
    real = pd.read_csv((_PROJECT_ROOT / 'Outputs/metricas/puntajes_reales.csv.gz'))
    cases = pd.read_csv((_PROJECT_ROOT / 'Outputs/metricas/puntajes_inyecciones.csv.gz'))
    thresholds = pd.read_csv((_PROJECT_ROOT / 'Outputs/metricas/umbrales_tasa_igualada.csv'))
    by_type = pd.read_csv((_PROJECT_ROOT / 'Outputs/metricas/deteccion_por_tipo_tasa_igualada.csv'))
    metrics = pd.read_csv((_PROJECT_ROOT / 'Outputs/metricas/metricas_globales.csv'))
    curve = pd.read_csv((_PROJECT_ROOT / 'Outputs/metricas/curva_deteccion.csv'))
    sources = list(real.fuente.unique())
    assert len(real) == config['detalle']['puntajes_reales'] and len(cases) == config['detalle']['puntajes_inyecciones']

    # 1. umbrales y tasas observadas desde los puntajes reales
    recomputed_thr = {}
    for source in sources:
        scores = real[real.fuente == source]
        for method in METHODS:
            values = scores[f'puntaje_{method}'].to_numpy()
            for alpha in alphas:
                thr = threshold_for_rate(values, alpha)
                recomputed_thr[(source, method, alpha)] = thr
                row = thresholds[(thresholds.fuente == source) & (thresholds.metodo == method) &
                                 (thresholds.tasa_objetivo == alpha)].iloc[0]
                assert abs(row.umbral - thr) <= TOL * max(1, abs(thr)), (source, method, alpha)
                assert row.alertas_reales == int((values > thr).sum())
                assert row.alertas_reales <= np.floor(alpha * len(values) + 1e-9)
    checks.append('Umbrales y alertas reales reproducidos desde puntajes_reales; nunca superan la tasa objetivo')

    # 2. detecciones por tipo, recall macro y FPR desde los puntajes guardados
    macro, fpr = {}, {}
    for source in sources:
        c = cases[cases.fuente == source]
        r = real[real.fuente == source].copy()
        r['orden'] = r.groupby('sid').cumcount()
        for method in METHODS:
            st, st1 = c[f'puntaje_{method}_t'].to_numpy(), c[f'puntaje_{method}_t1'].to_numpy()
            values = r[f'puntaje_{method}'].to_numpy()
            for alpha in alphas:
                thr = recomputed_thr[(source, method, alpha)]
                hit_t, hit_2 = st > thr, (st > thr) | (st1 > thr)
                recalls = {'t': [], 't_o_t1': []}
                for kind in ERROR_TYPES:
                    sel = (c.tipo == kind).to_numpy()
                    if not sel.any():
                        continue
                    for horizon, hit in (('t', hit_t), ('t_o_t1', hit_2)):
                        row = by_type[(by_type.fuente == source) & (by_type.metodo == method) &
                                      (by_type.tasa_objetivo == alpha) & (by_type.tipo == kind) &
                                      (by_type.horizonte == horizon)].iloc[0]
                        assert row.casos == sel.sum() and row.detecciones == hit[sel].sum()
                        assert abs(row.recall - hit[sel].mean()) <= TOL
                        if pd.notna(row.ic95_inferior):
                            assert row.ic95_inferior <= row.ic95_superior
                        recalls[horizon].append(hit[sel].mean())
                alert = values > thr
                r['alerta'] = alert
                paired = r.groupby('sid').alerta.apply(lambda s: (s.to_numpy()[:-1] | s.to_numpy()[1:])).explode().astype(bool)
                macro[(source, method, alpha, 't')] = float(np.mean(recalls['t']))
                macro[(source, method, alpha, 't_o_t1')] = float(np.mean(recalls['t_o_t1']))
                fpr[(source, method, alpha, 't')] = float(alert.mean())
                fpr[(source, method, alpha, 't_o_t1')] = float(paired.mean())
    checks.append('Detecciones por tipo reproducidas desde puntajes_inyecciones (casos, aciertos y recall exactos)')

    # 3. métricas globales: macro, FPR, precisión y F1
    for row in metrics.itertuples(index=False):
        key = (row.fuente, row.metodo, row.tasa_objetivo, row.horizonte)
        assert abs(row.recall_macro - macro[key]) <= 1e-9, key
        assert abs(row.tasa_alerta_sin_error_conocido - fpr[key]) <= 1e-9, key
        precision = float(precision_at_prevalence(macro[key], fpr[key], row.prevalencia_supuesta))
        f1 = float(f1_score(precision, macro[key]))
        for observed, expected in ((row.precision_conservadora, precision), (row.f1, f1)):
            assert (np.isnan(observed) and np.isnan(expected)) or abs(observed - expected) <= 1e-9, key
        if pd.notna(row.ic95_inferior_f1):
            assert row.ic95_inferior_f1 <= row.ic95_superior_f1
            assert row.ic95_inferior_recall_macro <= row.ic95_superior_recall_macro
    expected_rows = len(sources) * len(METHODS) * len(alphas) * 2 * len(prevalences)
    assert len(metrics) == expected_rows, (len(metrics), expected_rows)
    checks.append(f'{len(metrics)} filas de métricas globales: macro, tasa de alerta, precisión y F1 recalculados')

    # 4. propiedades: t o t+1 >= t, curvas monótonas, estados marcados
    wide = metrics.pivot_table(index=['fuente', 'metodo', 'tasa_objetivo', 'prevalencia_supuesta'],
                               columns='horizonte', values='recall_macro')
    assert (wide['t_o_t1'] >= wide['t'] - TOL).all()
    for (source, method), frame in curve.groupby(['fuente', 'metodo']):
        frame = frame.sort_values('tasa_objetivo')
        assert (np.diff(frame.recall_macro_t) >= -TOL).all() and (np.diff(frame.recall_macro_t_o_t1) >= -TOL).all()
        assert (frame.recall_macro_t_o_t1 >= frame.recall_macro_t - TOL).all()
    xm = metrics[metrics.fuente == 'XM']
    assert (xm.estado_metodo == 'no_interpretable_baja_resolucion').all() and xm.ic95_inferior_f1.isna().all()
    cover = pd.read_csv((_PROJECT_ROOT / 'Outputs/metricas/cobertura_experimento.csv'))
    for row in cover.itertuples(index=False):
        degenerate = metrics[(metrics.fuente == row.fuente) & (metrics.metodo == 'LOF') &
                             (metrics.estado_metodo == 'degenerado_por_duplicados')]
        assert (len(degenerate) > 0) == (row.LOF_estado == 'degenerado_por_duplicados')
    checks.append('Recall t o t+1 >= t; curvas no decrecientes; XM y LOF degenerado marcados sin IC ni interpretación')

    # 5. sorteo sin reemplazo y comparación con 4.2
    draw = pd.read_csv((_PROJECT_ROOT / 'Outputs/metricas/sorteo_sin_reemplazo.csv'))
    assert (draw.meses_distintos_por_serie == 'todos_distintos_por_construccion').all()
    assert (draw.recall_sorteo_p2_5 <= draw.recall_sorteo_media + TOL).all()
    against = json.loads(((_PROJECT_ROOT / 'Outputs/metricas/verificacion_contra_4_2.json')).read_text(encoding='utf-8'))
    assert against['estado'] == 'coincide'
    for item in against['detalle']:
        assert item['coincide_con_inyecciones_detalle_4_2']
        for method, stat in item['metodos'].items():
            assert stat['discrepancias_series_con_escala_positiva'] == 0, (item['fuente'], method)
    checks.append('Sorteo con meses distintos; banderas nativas idénticas a 4.2 en series con escala positiva')

    # 6. pruebas automáticas
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1', PYTHONIOENCODING='utf-8')
    tests = subprocess.run([sys.executable, '-I', '-m', 'unittest', 'discover', '-s', str((_PROJECT_ROOT / 'Code/Modeling/metricas')), '-p', 'test_metricas.py', '-v'],
                           capture_output=True, text=True, encoding='utf-8', env=env, cwd=str((_PROJECT_ROOT / 'Code/Modeling/metricas')))
    assert tests.returncode == 0, tests.stdout + tests.stderr
    n_tests = sum(1 for line in tests.stderr.splitlines() if line.strip().endswith('... ok'))
    checks.append(f'{n_tests} pruebas automáticas de propiedades: correctas')

    report = {'estado': 'correcto', 'fecha_cliente': '2026-11-07', 'comprobaciones': checks,
              'fuentes': sources, 'filas_metricas_globales': len(metrics),
              'observaciones_reales_puntuadas': len(real), 'casos_puntuados': len(cases),
              'pruebas_automaticas': n_tests}
    ((_PROJECT_ROOT / 'Outputs/metricas/verificacion.json')).write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    artifacts = [{'archivo': p.relative_to(HERE).as_posix(), 'bytes': p.stat().st_size, 'sha256': digest(p)}
                 for p in sorted(HERE.rglob('*')) if p.is_file() and p.name != 'manifiesto_resultados.json'
                 and '__pycache__' not in p.parts]
    ((_PROJECT_ROOT / 'Outputs/metricas/manifiesto_resultados.json')).write_text(
        json.dumps({'entradas': config['entradas'], 'archivos': artifacts}, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
