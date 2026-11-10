"""Audita 4.4: huellas, fracciones recalculadas con otra implementación, calibración y contraste."""
from __future__ import annotations

from pathlib import Path as _ProjectPath
_PROJECT_ROOT = next(p for p in _ProjectPath(__file__).resolve().parents if (p / "project.json").is_file())

import hashlib
import json
import os
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

import numpy as np
import pandas as pd

HERE = (_PROJECT_ROOT / 'Outputs/regla_sistemica')
ROOT = _PROJECT_ROOT
sys.dont_write_bytecode = True
sys.path.insert(0, str((_PROJECT_ROOT / 'Code/Modeling/regla_sistemica')))
import regla_sistemica as R  # noqa: E402

TOL = 1e-9


def digest(path):
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1 << 20), b''):
            h.update(block)
    return h.hexdigest()


def naive_fractions(items, window, method):
    """Mes a mes y serie a serie, sin vectorizar: contraste independiente de `rolling_signals`."""
    totals, alerts = defaultdict(int), defaultdict(int)
    for item in items:
        levels, months = item['valores'], item['meses']
        changes = [float(np.log(levels[i + 1]) - np.log(levels[i])) for i in range(len(levels) - 1)]
        for j in range(window, len(changes)):
            ref = changes[j - window:j]
            current, previous = changes[j], changes[j - 1]
            mean = sum(ref) / window
            mr = sum(abs(ref[i + 1] - ref[i]) for i in range(window - 1)) / (window - 1)
            ordered = sorted(ref)
            median = (ordered[window // 2 - 1] + ordered[window // 2]) / 2 if window % 2 == 0 else ordered[window // 2]
            deviations = sorted(abs(v - median) for v in ref)
            mad = (deviations[window // 2 - 1] + deviations[window // 2]) / 2 if window % 2 == 0 else deviations[window // 2]
            if method == 'IMR_clasica':
                signal = abs(current - mean) > 2.66 * mr or abs(current - previous) > 3.267 * mr
            else:
                signal = (current != median) if mad == 0 else (0.6744897501960817 * abs(current - median) / mad > 3.0)
            month = int(months[j + 1])
            totals[month] += 1
            alerts[month] += int(signal)
    return {R.period_label(m): (totals[m], alerts[m]) for m in totals}


def main():
    sys.stdout.reconfigure(encoding='utf-8')
    config = json.loads(((_PROJECT_ROOT / 'Outputs/regla_sistemica/configuracion.json')).read_text(encoding='utf-8'))
    checks = []
    for entry in [*config['entradas'].values(), config['cuarentena_EPM']]:
        assert digest(ROOT / entry['ruta']) == entry['sha256'], entry['ruta']
    for group in ('dependencias', 'evidencia_externa'):
        for path, expected in config[group].items():
            assert digest(ROOT / path) == expected, path
    checks.append('Datasets, cuarentena, dependencias y los seis PDF de EPM conservan sus huellas')

    fractions = pd.read_csv((_PROJECT_ROOT / 'Outputs/regla_sistemica/fracciones_mensuales.csv'))
    # 1. fracciones: coherencia interna y recálculo ingenuo de EPM canónica
    assert np.allclose(fractions.fraccion, fractions.series_con_alerta / fractions.series_evaluadas, atol=TOL)
    assert ((fractions.series_evaluadas >= R.N_MIN).astype(int) == fractions.aplicable).all()
    assert (fractions.series_con_alerta <= fractions.series_evaluadas).all()
    items, _, _ = R.canonical_epm_items()
    compared = 0
    for window in (24, 36):
        for method in R.METHOD_COLUMNS:
            naive = naive_fractions(items, window, method)
            table = fractions[(fractions.fuente == 'EPM') & (fractions.etiquetas == 'canonicas') &
                              (fractions.referencia == window) & (fractions.metodo == method)]
            assert set(table.periodo) == set(naive), (window, method)
            for row in table.itertuples(index=False):
                assert (row.series_evaluadas, row.series_con_alerta) == naive[row.periodo], (window, method, row.periodo)
                compared += 1
    checks.append(f'{compared} meses de EPM canónica recalculados con una implementación distinta: conteos idénticos')

    # 2. reproducción del Hito 2
    alerts = pd.read_csv((_PROJECT_ROOT / 'Outputs/adaptadores/insumos_hito2/05_alertas_imr_reales.csv'))
    alerts['serie'] = alerts.clave + '|' + alerts.columna
    per_month = alerts.assign(periodo=alerts.fecha.str[:7]).groupby('periodo').serie.nunique()
    assert (per_month['2020-02'], per_month['2020-07'], per_month['2021-07']) == (51, 24, 18)
    h2 = pd.read_csv((_PROJECT_ROOT / 'Outputs/regla_sistemica/reproduccion_hito2.csv')).set_index('periodo')
    assert (h2.series_evaluadas == 83).all() and h2.series_con_alerta.sum() == per_month.sum()
    checks.append('Cifras 51/83, 24/83 y 18/83 del plan reproducidas desde 05_alertas_imr_reales.csv')

    # 3. calibración y banda factible recalculadas
    summary = pd.read_csv((_PROJECT_ROOT / 'Outputs/regla_sistemica/calibracion_resumen.csv'))
    calibration = pd.read_csv((_PROJECT_ROOT / 'Outputs/regla_sistemica/calibracion_X.csv'))
    keys = ['etiquetas', 'referencia', 'metodo', 'protocolo']
    for _, row in summary.iterrows():
        frame = fractions[(fractions.fuente == 'EPM') & (fractions.etiquetas == row.etiquetas) &
                          (fractions.referencia == row.referencia) & (fractions.metodo == row.metodo) &
                          (fractions.protocolo == row.protocolo)]
        sep = R.separability(frame)
        assert abs(row.X_minimo_para_no_marcar_fondo - sep['X_minimo_para_no_marcar_fondo']) < TOL
        assert abs(row.X_maximo_para_capturar_todos - sep['X_maximo_para_capturar_todos']) < TOL
        assert bool(row.banda_factible) == sep['banda_factible']
        table = calibration[(calibration.etiquetas == row.etiquetas) & (calibration.referencia == row.referencia) &
                            (calibration.metodo == row.metodo) & (calibration.protocolo == row.protocolo)].sort_values('umbral_X')
        assert (np.diff(table.eventos_capturados) <= 0).all() and (np.diff(table.meses_marcados_total) <= 0).all()
        assert (np.diff(table.alertas_reclasificadas) <= 0).all()
        evaluable = frame[frame.aplicable == 1]
        for x in (0.10, 0.25, 0.50):
            flagged = evaluable[evaluable.fraccion > x]
            line = table[np.isclose(table.umbral_X, x)].iloc[0]
            assert line.meses_marcados_total == len(flagged)
            assert line.alertas_reclasificadas == flagged.series_con_alerta.sum()
    assert not summary.banda_factible.any(), 'Alguna variante tiene banda factible: revisar el informe'
    checks.append('Banda de X, capturas y alertas reclasificadas recalculadas desde las fracciones; ninguna variante tiene banda factible')

    # 4. efecto sobre alertas reales
    effect = pd.read_csv((_PROJECT_ROOT / 'Outputs/regla_sistemica/efecto_regla_sobre_alertas_reales.csv'))
    assert (effect.alertas_retenidas + effect.alertas_reclasificadas == effect.alertas_totales).all()
    undefined = effect.fraccion_alertas_reclasificadas.isna()
    assert (effect[undefined].alertas_totales == 0).all(), 'NaN solo si no hay alertas en meses evaluables'
    assert set(effect[undefined].fuente) <= {'XM'}, 'Solo XM (una serie, sin meses con >= 10 series) puede quedar sin definir'
    assert effect.fraccion_alertas_reclasificadas.dropna().between(0, 1).all()
    checks.append('Alertas retenidas + reclasificadas = alertas totales; XM sin meses evaluables queda indefinido, no en cero')

    # 5. catálogo
    catalog = pd.read_csv((_PROJECT_ROOT / 'Outputs/regla_sistemica/catalogo_alertas_sistemicas.csv'))
    assert np.allclose(catalog.fraccion, catalog.series_con_alerta / catalog.series_evaluadas, atol=TOL)
    for x in (10, 25, 50):
        assert ((catalog.fraccion > x / 100).astype(int) == catalog[f'sistemico_X{x}']).all()
    assert ((catalog.fraccion > R.X_WORK) == (catalog.estado == 'candidato_sistemico')).all()
    assert (catalog.series_evaluadas >= R.N_MIN).all()
    checks.append(f'Catálogo de {len(catalog)} filas: fracciones, banderas por X y estado coherentes')

    # 6. contraste: transcripción, suma de componentes y cambios porcentuales
    comparison = pd.read_csv((_PROJECT_ROOT / 'Outputs/regla_sistemica/verificacion_transcripcion_pdf.csv'))
    sums = pd.read_csv((_PROJECT_ROOT / 'Outputs/regla_sistemica/verificacion_suma_componentes.csv'))
    assert comparison.coincide.all() and len(comparison) == 108
    assert sums.dentro_de_tolerancia.all() and (sums.diferencia.abs() <= 0.02 + 1e-9).all()
    published = pd.read_csv((_PROJECT_ROOT / 'Outputs/regla_sistemica/evidencia_externa/tarifas_epm_publicadas.csv')).set_index(['periodo', 'componente'])
    contrast = pd.read_csv((_PROJECT_ROOT / 'Outputs/regla_sistemica/contraste_componentes.csv'))
    for row in contrast.itertuples(index=False):
        name = 'CU total' if str(row.componente).startswith('CU total') else row.componente
        old = published.loc[(row.mes_base, name), 'propiedadepm']
        new = published.loc[(row.mes, name), 'propiedadepm']
        assert abs(row.valor_base - old) < TOL and abs(row.valor_mes - new) < TOL
        if old > 0 and new > 0:
            assert abs(row.cambio_porcentual - 100 * (new - old) / old) < 1e-9
        else:
            assert pd.isna(row.cambio_porcentual)
    checks.append('108 celdas de los PDF = CSV; suma de componentes = CU total (±0,02); cambios porcentuales recalculados')

    # 7. costo de enmascaramiento (tomado de 4.2)
    cost = pd.read_csv((_PROJECT_ROOT / 'Outputs/regla_sistemica/costo_enmascaramiento_4_2.csv'))
    assert np.allclose(cost.fraccion_enmascarada, (cost.detecciones_t_o_t1 - cost.retenidas_t_o_t1) / cost.detecciones_t_o_t1, atol=TOL)
    assert (cost.retenidas_t_o_t1 <= cost.detecciones_t_o_t1).all()
    checks.append('Fracciones de enmascaramiento reconciliadas con los conteos de 4.2')

    # 8. pruebas automáticas
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1', PYTHONIOENCODING='utf-8')
    tests = subprocess.run([sys.executable, '-I', '-m', 'unittest', 'discover', '-s', str((_PROJECT_ROOT / 'Code/Modeling/regla_sistemica')), '-p', 'test_regla_sistemica.py', '-v'],
                           capture_output=True, text=True, encoding='utf-8', env=env, cwd=str((_PROJECT_ROOT / 'Code/Modeling/regla_sistemica')))
    assert tests.returncode == 0, tests.stdout + tests.stderr
    n_tests = sum(1 for line in tests.stderr.splitlines() if line.strip().endswith('... ok'))
    checks.append(f'{n_tests} pruebas automáticas (sin fuga de futuro, equivalencia con el cálculo ingenuo, regla estricta, etiquetas canónicas): correctas')

    report = {'estado': 'correcto', 'fecha_cliente': '2026-11-07', 'comprobaciones': checks,
              'filas_fracciones_mensuales': len(fractions), 'variantes_calibradas': len(summary),
              'filas_catalogo': len(catalog), 'pruebas_automaticas': n_tests}
    ((_PROJECT_ROOT / 'Outputs/regla_sistemica/verificacion.json')).write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    artifacts = [{'archivo': p.relative_to(HERE).as_posix(), 'bytes': p.stat().st_size, 'sha256': digest(p)}
                 for p in sorted(HERE.rglob('*')) if p.is_file() and p.name != 'manifiesto_resultados.json'
                 and '__pycache__' not in p.parts]
    ((_PROJECT_ROOT / 'Outputs/regla_sistemica/manifiesto_resultados.json')).write_text(
        json.dumps({'entradas': config['entradas'], 'archivos': artifacts}, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
