"""Pruebas de propiedades de 4.3 (sin leer los datasets ni escribir archivos)."""

from pathlib import Path as _ProjectPath
_PROJECT_ROOT = next(p for p in _ProjectPath(__file__).resolve().parents if (p / "project.json").is_file())
import sys
import unittest
from pathlib import Path

import numpy as np

HERE = (_PROJECT_ROOT / 'Data/gold/outputs/metricas')
sys.dont_write_bytecode = True
sys.path.insert(0, str((_PROJECT_ROOT / 'Code/Modeling/metricas')))
sys.path.insert(0, str((_PROJECT_ROOT / 'Code/Modeling/sensibilidad')))
from metricas_base import (draw_distinct_origins, f1_score, imr_score, level_ratio_score,  # noqa: E402
                           observed_rate, positive_scale, precision_at_prevalence,
                           robust_z_score, threshold_for_rate, NORMAL_MEDIAN)
from analisis_sensibilidad import local_predictions  # noqa: E402


class MetricsTests(unittest.TestCase):
    def test_umbral_no_supera_la_tasa_objetivo(self):
        rng = np.random.default_rng(1)
        scores = rng.normal(size=1000)
        for rate in (0.01, 0.05, 0.10, 0.30):
            thr = threshold_for_rate(scores, rate)
            self.assertAlmostEqual(observed_rate(scores, thr), rate, places=12)

    def test_tasa_igualada_entre_metodos_con_escalas_distintas(self):
        rng = np.random.default_rng(2)
        a, b = rng.exponential(1, 500), 1e6 * rng.lognormal(0, 2, 500)
        ta, tb = threshold_for_rate(a, 0.05), threshold_for_rate(b, 0.05)
        self.assertEqual(observed_rate(a, ta), observed_rate(b, tb))

    def test_cero_alertas_esperadas_y_tasa_completa(self):
        scores = np.arange(10.0)
        self.assertEqual(observed_rate(scores, threshold_for_rate(scores, 0.05)), 0.0)
        self.assertEqual(observed_rate(scores, threshold_for_rate(scores, 1.0)), 1.0)

    def test_empates_no_inflan_la_tasa(self):
        scores = np.array([5.0] * 50 + [1.0] * 50)
        thr = threshold_for_rate(scores, 0.20)
        self.assertLessEqual(observed_rate(scores, thr), 0.20)

    def test_puntaje_IMR_equivale_a_las_cartas_de_4_2(self):
        rng = np.random.default_rng(3)
        params = dict(mean=0.01, mr_mean=0.02, median=0.0, mad=0.015, level_reference=100.0)
        current, previous = rng.normal(0, .08, 400), rng.normal(0, .08, 400)
        flags = local_predictions(params, current, previous, np.full(400, 100.0))
        np.testing.assert_array_equal(imr_score(current, previous, 0.01, 0.02) > 1, flags[:, 2])

    def test_zscore_robusto_3_equivale_a_MAD_3sigma(self):
        rng = np.random.default_rng(4)
        params = dict(mean=0., mr_mean=1., median=0.002, mad=0.015, level_reference=100.0)
        current = rng.normal(0, .08, 400)
        flags = local_predictions(params, current, np.zeros(400), np.full(400, 100.0))
        z = robust_z_score(current, 0.002, 0.015 / NORMAL_MEDIAN)
        np.testing.assert_array_equal(z > 3.0, flags[:, 4])

    def test_R12_es_monotono_en_el_factor(self):
        params = dict(mean=0., mr_mean=1., median=0., mad=1., level_reference=100.0)
        levels = np.array([400., 600., 1100., 2500.])
        flags = local_predictions(params, np.zeros(4), np.zeros(4), levels)
        for column, factor in ((8, 5), (9, 10), (10, 20)):
            np.testing.assert_array_equal(level_ratio_score(levels, 100.0) > factor, flags[:, column])

    def test_escala_de_respaldo_sin_epsilon(self):
        self.assertEqual(positive_scale(2.0, np.zeros(5)), 2.0)
        self.assertEqual(positive_scale(0.0, np.array([0., 0., 0., 3.])), 0.75)   # desviación absoluta media
        self.assertEqual(positive_scale(0.0, np.ones(6)), 1.0)                    # serie constante

    def test_precision_y_F1_valores_conocidos(self):
        self.assertAlmostEqual(float(precision_at_prevalence(0.8, 0.2, 0.5)), 0.8)
        self.assertAlmostEqual(float(precision_at_prevalence(0.8, 0.05, 0.05)), 0.04 / (0.04 + 0.0475))
        self.assertAlmostEqual(float(f1_score(0.5, 1.0)), 2 / 3)
        self.assertTrue(np.isnan(precision_at_prevalence(0.0, 0.0, 0.05)))
        self.assertTrue(np.isnan(f1_score(0.0, 0.0)))

    def test_precision_crece_con_la_prevalencia_y_recall_no_depende_de_ella(self):
        values = [float(precision_at_prevalence(0.7, 0.05, p)) for p in (0.01, 0.05, 0.10, 0.5)]
        self.assertEqual(values, sorted(values))

    def test_sorteo_sin_reemplazo_y_disponibilidad(self):
        rng = np.random.default_rng(5)
        n_series, n_origins, n_types = 6, 11, 6
        matrix = -np.ones((n_series, n_origins, n_types), dtype=int)
        counter = 0
        for s in range(n_series):
            for t in range(n_origins):
                for k in range(n_types):
                    if s == 5 and t >= 2:          # serie con solo dos orígenes
                        continue
                    if k == 5 and s % 2 == 0:      # 'otra_medida' no siempre existe
                        continue
                    matrix[s, t, k] = counter
                    counter += 1
        indices, valid, chosen = draw_distinct_origins(matrix, 3, 200, rng)
        for r in range(200):
            for s in range(n_series):
                picks = chosen[r, s][valid[r, s]]
                self.assertEqual(len(set(picks)), len(picks))               # meses distintos
                for pick, index in zip(chosen[r, s][valid[r, s]], indices[r, s][valid[r, s]]):
                    self.assertTrue(index in matrix[s, pick])               # el caso pertenece al mes
        self.assertEqual(valid[:, 5].sum(axis=1).max(), 2)                  # no inventa orígenes
        self.assertTrue(valid[:, :5].all())

    def test_sorteo_reproducible_con_semilla_y_tipos_equiprobables(self):
        matrix = np.arange(11 * 6).reshape(1, 11, 6)
        a = draw_distinct_origins(matrix, 3, 50, np.random.default_rng(9))[0]
        b = draw_distinct_origins(matrix, 3, 50, np.random.default_rng(9))[0]
        np.testing.assert_array_equal(a, b)
        types = draw_distinct_origins(matrix, 3, 4000, np.random.default_rng(10))[0] % 6
        shares = np.bincount(types.ravel(), minlength=6) / types.size
        self.assertTrue(np.all(np.abs(shares - 1 / 6) < 0.02))


if __name__ == '__main__':
    unittest.main(verbosity=2)
