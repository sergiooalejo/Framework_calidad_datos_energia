"""Pruebas de propiedades de la regla sistémica (4.4). No escriben en los datasets."""
import sys
import unittest
from pathlib import Path

import numpy as np
import pandas as pd

HERE = Path(__file__).resolve().parent
sys.dont_write_bytecode = True
sys.path.insert(0, str(HERE))
import regla_sistemica as R  # noqa: E402


def brute_force(changes, window):
    """Implementación ingenua, mes a mes, para contrastar la versión vectorizada."""
    out = []
    for j in range(window, len(changes)):
        ref = changes[j - window:j]
        mean, mr = ref.mean(), np.abs(np.diff(ref)).mean()
        median = np.median(ref)
        mad = np.median(np.abs(ref - median))
        imr = abs(changes[j] - mean) > R.I_COEF * mr or abs(changes[j] - changes[j - 1]) > R.MR_COEF * mr
        z = (changes[j] != median) if mad == 0 else (R.NORMAL_MEDIAN * abs(changes[j] - median) / mad > 3.0)
        out.append((j, imr, z))
    return out


def make_item(name, values, start=24240, component='C', category='K'):
    return dict(serie=name, medida='valor', categoria=category, componente=component,
                meses=start + np.arange(len(values)), valores=np.asarray(values, float))


class RuleTests(unittest.TestCase):
    def test_vectorizado_igual_al_calculo_ingenuo(self):
        rng = np.random.default_rng(1)
        for window in (24, 36):
            changes = rng.normal(0, 0.03, 90)
            changes[50] = 0.4
            changes[10:34] = 0.0            # tramo con MAD cero
            index, imr, mad = R.rolling_signals(changes, window)
            expected = brute_force(changes, window)
            self.assertEqual(list(index), [e[0] for e in expected])
            self.assertEqual(list(imr), [e[1] for e in expected])
            self.assertEqual(list(mad), [e[2] for e in expected])

    def test_sin_fuga_del_futuro(self):
        rng = np.random.default_rng(2)
        changes = rng.normal(0, 0.03, 80)
        altered = changes.copy()
        altered[60:] *= 50                  # el futuro cambia, el pasado no
        _, imr_a, mad_a = R.rolling_signals(changes, 36)
        _, imr_b, mad_b = R.rolling_signals(altered, 36)
        np.testing.assert_array_equal(imr_a[:60 - 36], imr_b[:60 - 36])
        np.testing.assert_array_equal(mad_a[:60 - 36], mad_b[:60 - 36])

    def test_exige_la_ventana_completa(self):
        index, imr, mad = R.rolling_signals(np.zeros(30), 36)
        self.assertEqual(len(index), 0)
        index, _, _ = R.rolling_signals(np.random.default_rng(3).normal(0, .01, 40), 36)
        self.assertEqual(index[0], 36)

    def test_regla_desigualdad_estricta_y_minimo_de_series(self):
        fraction = np.array([0.25, 0.2501, 0.9, 0.9])
        applicable = np.array([1, 1, 1, 0])
        np.testing.assert_array_equal(R.classify(fraction, applicable, 0.25), [False, True, True, False])

    def test_denominador_solo_con_series_evaluables(self):
        rng = np.random.default_rng(4)
        long_items = [make_item(f's{i}', 100 * np.exp(np.cumsum(rng.normal(0, .01, 61)))) for i in range(12)]
        short = make_item('corta', 100 * np.exp(np.cumsum(rng.normal(0, .01, 30))))      # menos de 36 cambios
        long = R.evaluate_items(long_items + [short], 36)
        self.assertNotIn('corta|valor', set(long.serie))
        fractions = R.monthly_fractions(long, 'IMR_clasica')
        self.assertTrue((fractions.series_evaluadas == 12).all())
        self.assertTrue((fractions.aplicable == 1).all())

    def test_fraccion_y_amplitud(self):
        rng = np.random.default_rng(5)
        items = []
        for i in range(10):
            values = 100 * np.exp(np.cumsum(rng.normal(0, .01, 61)))
            if i < 4:
                values[45:] *= 3.0                                  # salto común en 4 de 10 series
            items.append(make_item(f's{i}', values, component='A' if i < 2 else 'B' if i < 4 else 'C'))
        long = R.evaluate_items(items, 36)
        row = R.monthly_fractions(long, 'IMR_clasica').set_index('periodo')
        month = R.period_label(24240 + 45)
        self.assertEqual(row.loc[month, 'series_con_alerta'], 4)
        self.assertAlmostEqual(row.loc[month, 'fraccion'], 0.4)
        self.assertEqual(row.loc[month, 'componentes_con_alerta'], 2)
        self.assertEqual(row.loc[month, 'componentes_evaluados'], 3)

    def test_calibracion_es_monotona_y_las_alertas_se_conservan(self):
        fractions = pd.DataFrame({
            'periodo': ['2020-01', '2020-02', '2020-03', '2020-04', '2020-05'],
            'series_con_alerta': [1, 30, 8, 12, 0], 'series_evaluadas': [50] * 5,
            'fraccion': [0.02, 0.6, 0.16, 0.24, 0.0], 'aplicable': [1] * 5})
        table = R.calibrate(fractions, events=('2020-02', '2020-04'))
        self.assertTrue((np.diff(table.eventos_capturados) <= 0).all())
        self.assertTrue((np.diff(table.meses_marcados_total) <= 0).all())
        self.assertTrue((np.diff(table.alertas_reclasificadas) <= 0).all())
        self.assertTrue((table.alertas_reclasificadas <= table.alertas_totales).all())
        low = table[table.umbral_X == 0.15].iloc[0]
        self.assertEqual((low.eventos_capturados, low.meses_fondo_marcados), (2, 1))   # captura ambos y marca marzo
        high = table[table.umbral_X == 0.25].iloc[0]
        self.assertEqual((high.eventos_capturados, high.meses_fondo_marcados), (1, 0))

    def test_banda_factible_e_infactible(self):
        feasible = pd.DataFrame({'periodo': ['a', 'b', 'c'], 'fraccion': [0.6, 0.3, 0.05],
                                 'series_con_alerta': [1, 1, 1], 'series_evaluadas': [1, 1, 1], 'aplicable': [1, 1, 1]})
        sep = R.separability(feasible, events=('a', 'b'))
        self.assertTrue(sep['banda_factible'])
        self.assertEqual((sep['X_minimo_para_no_marcar_fondo'], sep['X_maximo_para_capturar_todos']), (0.05, 0.3))
        blocked = feasible.assign(fraccion=[0.6, 0.2, 0.24])      # un mes de fondo supera a un evento
        self.assertFalse(R.separability(blocked, events=('a', 'b'))['banda_factible'])

    def test_reproduce_51_24_18_del_plan(self):
        import calibrar_regla_sistemica as C
        frame, alerts = C.hito2_fractions()
        counts = frame.set_index('periodo').series_con_alerta
        self.assertEqual((counts['2020-02'], counts['2020-07'], counts['2021-07']), (51, 24, 18))
        self.assertTrue((frame.series_evaluadas == 83).all())
        self.assertEqual(len(frame), 24)

    def test_etiquetas_canonicas_reunen_las_variantes_en_una_sola_serie(self):
        items, mapping, _ = R.canonical_epm_items()
        key = ('Monomia', 'Costo Unitario', 'Costo compra: Gm, i', 'N/A', 'I')
        match = [i for i in items if i['medida'] == 'propiedadepm' and tuple(i['key'][:2]) == key[:2]
                 and i['key'][2] == key[2] and i['key'][4] == 'I']
        self.assertTrue(match)
        months = match[0]['meses']
        self.assertLessEqual(months.min(), 2020 * 12 + 0)           # incluye enero de 2020 (variante «Gm, i»)
        self.assertGreaterEqual(months.max(), 2020 * 12 + 6)        # y julio de 2020 (variante «Costo Compra»)
        self.assertTrue(np.all(np.diff(months) == 1))
        self.assertIn(('tipodedato', 'Costo Compra: Gm, i'), mapping)


if __name__ == '__main__':
    unittest.main(verbosity=2)
