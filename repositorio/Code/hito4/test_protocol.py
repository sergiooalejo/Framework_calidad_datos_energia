"""Propiedades del protocolo: sin fuga temporal, misma geometría, métricas honestas."""
from copy import deepcopy
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

import numpy as np
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT))
from Code.hito4 import protocol as P
from Code.hito4.run import build_cases,injection_requests
from Code.hito4 import report
from Code.hito3.core import write_csv


def item(sid='serie'):
    changes=.01+np.sin(np.arange(48)*1.7)*.02
    values=100*np.exp(np.r_[0,np.cumsum(changes)])
    return dict(sid=sid,levels=values,months=np.arange(24000,24049),fuente='EPM',
                category='["categoria"]',category_tuple=('a','b','c','d','I'),medida='punta')


class ProtocolTests(unittest.TestCase):
    def test_folds_se_ordenan_dentro_de_referencia(self):
        for window in (24,36,48):
            schedule=P.folds(window)
            self.assertEqual(len(schedule),3)
            self.assertEqual(schedule[-1][-1],window)
            self.assertTrue(all(0<a<b<=window for a,b in schedule))

    def test_vigilancia_no_cambia_umbrales_ni_geometria(self):
        rows=[item('a'),item('b')]
        before,_,schedule,_=P.calibrate(rows,36)
        final=P.fit_bank(rows,36)
        changed=deepcopy(rows)
        for row in changed:row['levels'][37:]*=1000000
        after,_,_,_=P.calibrate(changed,36)
        other=P.fit_bank(changed,36)
        self.assertEqual(before,after)
        self.assertEqual(final.audit['huella_geometria'],other.audit['huella_geometria'])
        self.assertTrue(all(s['entrenamiento_hasta']<s['validacion_desde']<=s['validacion_hasta']<=s['referencia_hasta'] for s in schedule))

    def test_lof_deduplica_solo_entrenamiento_para_todos_los_ml(self):
        rows=[item(str(i)) for i in range(8)]
        bank=P.fit_bank(rows,36)
        self.assertGreater(bank.audit['duplicados_referencia'],0)
        self.assertEqual(len(bank.lof._fit_X),bank.audit['vectores_unicos'])
        self.assertEqual(bank.knn.n_samples_fit_,bank.audit['vectores_unicos'])
        scores=P.score_bank(bank,rows,[('0',36),('1',36)])
        self.assertTrue(np.isfinite(scores).all())
        self.assertTrue(np.array_equal(scores[0],scores[1]))

    def test_geometria_constante_se_declara_no_interpretable(self):
        row=item();row['levels'][:]=100
        bank=P.fit_bank([row],36)
        self.assertIsNone(bank.lof)
        self.assertEqual(bank.audit['lof_estado'],'sin_geometria_menos_de_tres_vectores')
        thresholds,_,_,_=P.calibrate([row],36)
        self.assertIsNone(thresholds['LOF'][.05])

    def test_calibracion_respeta_empates_y_no_fuerza_tasa_de_prueba(self):
        calibration=np.array([0.,0.,1.,1.,2.,3.,4.,5.,6.,7.])
        cutoff=P.threshold(calibration,.2)
        self.assertLessEqual(np.mean(calibration>cutoff),.2)
        self.assertEqual(np.mean(np.array([100.,100.])>cutoff),1.)

    def test_escala_cero_no_inventa_epsilon_ni_infinito(self):
        self.assertEqual(float(P.bound_ratio(0.,0.)),0.)
        self.assertEqual(float(P.bound_ratio(5.,0.)),1.)
        self.assertAlmostEqual(float(P.bound_ratio(3.,1.)),.75)

    def test_inyecciones_se_comparten_y_no_reentrenan(self):
        row=item();row['window']=36
        cases,_=build_cases([row],36,{})
        self.assertEqual(len({c['caso_id'] for c in cases}),len(cases))
        bank=P.fit_bank([row],36)
        before=bank.audit['huella_geometria']
        requests=injection_requests(cases)
        scores=P.score_values(bank,requests)
        self.assertEqual(scores.shape,(2*len(cases),6))
        self.assertEqual(before,bank.audit['huella_geometria'])
        self.assertTrue(all(c['tipo']!='otra_medida' for c in cases))

    def test_precision_depende_de_prevalencia_y_no_es_precision_empirica(self):
        p,f=P.ratio_metrics(np.array([.8]),np.array([.05]),.01)
        expected=.8*.01/(.8*.01+.05*.99)
        self.assertAlmostEqual(p[0],expected)
        p2,_=P.ratio_metrics(np.array([.8]),np.array([.05]),.1)
        self.assertGreater(p2[0],p[0])

    def test_scorecard_no_confunde_cumplimiento_con_aprobacion(self):
        with tempfile.TemporaryDirectory(dir=ROOT) as folder:
            root=Path(folder);out=root/'salidas';out.mkdir()
            rows=[dict(fuente='EPM',control='R01',dimension='completitud',estado_medicion='medido',umbral_operador='>=',umbral_valor='100',resultado_valor='100'),
                  dict(fuente='EPM',control='OPO01',dimension='oportunidad',estado_medicion='no_medible',umbral_operador='>=',umbral_valor='100',resultado_valor='')]
            write_csv(root/'Data/gold/outputs/calidad/matriz_oe1.csv',rows,list(rows[0]))
            with patch.object(report,'ROOT',root),patch.object(report,'OUT',out):
                indicators,summary=report.scorecard()
            self.assertEqual(indicators[0]['estado_frente_umbral'],'satisface_umbral_propuesto')
            self.assertEqual(indicators[0]['decision_final'],'pendiente_aprobacion')
            self.assertEqual(indicators[1]['decision_final'],'pendiente_evidencia')
            self.assertTrue(all(r['promedio_indicadores']=='' for r in summary))


if __name__=='__main__':unittest.main()
