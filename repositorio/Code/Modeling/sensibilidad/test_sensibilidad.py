"""Pruebas de propiedades del experimento, sin escribir en los datasets."""

from pathlib import Path as _ProjectPath
_PROJECT_ROOT = next(p for p in _ProjectPath(__file__).resolve().parents if (p / "project.json").is_file())
import unittest
import numpy as np
from analisis_sensibilidad import (longest_run, fit_series, local_predictions,
                                  verify_monotonic, cluster_intervals, fit_calendar_models)


class SensitivityTests(unittest.TestCase):
    def item(self):
        x = np.arange(61)
        return {'meses':24000+x, 'valores':100*np.exp(.01*x+.005*np.sin(x)),
                'sid':'prueba','categoria':'A','serie':'prueba','medida':'valor'}

    def test_no_concatena_huecos(self):
        periods={(2020,1):[1],(2020,2):[2],(2020,4):[4],(2020,5):[5]}
        run=longest_run(periods)
        self.assertEqual(len(run),2)
        self.assertEqual(run[-1][0],2020*12+4)

    def test_futuro_no_cambia_referencia_ni_escalas(self):
        original=self.item()
        changed={**original,'valores':original['valores'].copy()}
        changed['valores'][-12:]*=1000
        a,b=fit_series(original,36),fit_series(changed,36)
        for key in ('mean','mr_mean','median','mad','level_reference'):
            self.assertEqual(a[key],b[key])
        np.testing.assert_array_equal(a['features'][:36],b['features'][:36])
        np.testing.assert_array_equal(a['center'],b['center'])
        np.testing.assert_array_equal(a['scale'],b['scale'])

    def test_ventanas_mantienen_vigilancia_identica(self):
        watches=[fit_series(self.item(),w)['months'][w+1:] for w in (24,36,48)]
        for watch in watches[1:]:np.testing.assert_array_equal(watches[0],watch)

    def test_IF_no_entrena_con_futuro_de_otra_serie(self):
        a=self.item()
        b={**self.item(),'meses':self.item()['meses']+120,'sid':'futura'}
        params=[fit_series(a,36),fit_series(b,36)]
        bank=fit_calendar_models(params,'PRUEBA','comun',36)
        self.assertEqual(len(bank),2)
        for _,_,indices in bank.values():
            self.assertLess(max(params[i]['months'][36] for i in indices),
                            min(params[i]['months'][37] for i in indices))

    def test_coeficientes_I_y_MR_tienen_papeles_distintos(self):
        params={'mean':0.,'mr_mean':1.,'median':0.,'mad':1.,'level_reference':100.}
        result=local_predictions(params,np.array([2.8,0.]),np.array([2.8,4.]),np.array([100.,100.]))
        self.assertTrue(result[0,0]);self.assertFalse(result[0,1])
        self.assertFalse(result[1,0]);self.assertTrue(result[1,1])
        self.assertTrue(np.all(result[:,2]))

    def test_mad_cero_sin_epsilon(self):
        params={'mean':0.,'mr_mean':0.,'median':0.,'mad':0.,'level_reference':100.}
        result=local_predictions(params,np.array([0.,.1]),np.array([0.,0.]),np.array([100.,100.]))
        self.assertFalse(result[0,4]);self.assertTrue(result[1,4])

    def test_r12_monotono_y_sin_usar_vigilancia(self):
        p=fit_series(self.item(),36)
        result=local_predictions(p,np.zeros(3),np.zeros(3),np.array([600.,1100.,3000.]))
        verify_monotonic(result)
        self.assertTrue(np.all(result[:,8]>=result[:,9]))
        self.assertTrue(np.all(result[:,9]>=result[:,10]))

    def test_no_inventa_intervalo_para_XM(self):
        intervals,status=cluster_intervals(['XM'],np.array([[1,2]]),np.array([12]))
        self.assertEqual(intervals,[(None,None),(None,None)])
        self.assertEqual(status,'sin_IC_menos_de_dos_categorias')

    def test_bootstrap_razon_de_totales_con_agrupacion(self):
        intervals,status=cluster_intervals(['A','A','B'],np.array([[2],[0],[4]]),np.array([2,2,8]))
        self.assertEqual(status,'bootstrap_categorias')
        self.assertTrue(.0<=intervals[0][0]<=intervals[0][1]<=1.)


if __name__=='__main__':unittest.main(verbosity=2)
