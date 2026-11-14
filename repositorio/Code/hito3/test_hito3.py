"""Pruebas del protocolo H3: calendario, cuarentena, conglomerados y captura."""
from copy import deepcopy
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from Code.hito3 import acquisition, core, opportunity


def points(values, start=24000):
    return {start+i: dict(value=v, reason='', keys=[str(i)], registros=1) for i,v in enumerate(values)}


class Hito3Tests(unittest.TestCase):
    def test_yaml_restaura_fichas_ausentes_sin_desplazar_resultados(self):
        import importlib.util
        import yaml
        spec = importlib.util.spec_from_file_location('matrix_h3_test', ROOT/'Code/Data_Acquisition_and_Understanding/calidad/medir_matriz_oe1.py')
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        med = {cfg['fuente']:({control:dict(numerador=i, denominador=100, valor=i, estado='medido', nota=control)
                              for i,control in enumerate(module.ORDEN,1)}, {}) for cfg in module.FUENTES}
        with tempfile.TemporaryDirectory(dir=ROOT) as folder:
            path = Path(folder)/'matriz.yaml'
            path.write_text('indicadores:\n- id: R04\n  estado_medicion: antiguo\n',encoding='utf-8')
            with patch.object(module,'MATRIZ_YAML',path):
                module.escribir_yaml(med,'2026-11-13T00:00:00Z')
            result = yaml.safe_load(path.read_text(encoding='utf-8'))['indicadores']
            self.assertEqual([r['id'] for r in result],module.ORDEN)
            for index,row in enumerate(result,1):
                self.assertEqual(row['resultado']['epm']['numerador'],index)
                self.assertEqual(row['resultado']['chec']['nota'],row['id'])

    def test_limites_i_mr_y_corte_fijo(self):
        import math
        data = points([math.exp(.01*i + .005*(i % 2)) for i in range(49)])
        summary, detail = core.evaluate_series('EPM', ('a',), 'punta', data)
        reference = [r['cambio_log'] for r in detail[:36]]
        mr = sum(abs(b-a) for a,b in zip(reference, reference[1:]))/35
        mean = sum(reference)/36
        self.assertAlmostEqual(summary['limite_superior'], mean+2.66*mr)
        self.assertAlmostEqual(summary['limite_mr'], 3.267*mr)
        data[24048]['value'] *= 1000
        changed, _ = core.evaluate_series('EPM', ('a',), 'punta', data)
        self.assertEqual(summary['limite_superior'], changed['limite_superior'])
        self.assertEqual(changed['señales'], 1)

    def test_cuarentena_excluye_ambos_extremos_sin_desplazar_corte(self):
        data = points([100+i for i in range(49)])
        data[24020]['reason'] = 'cuarentena'
        summary, detail = core.evaluate_series('EPM', ('a',), 'punta', data)
        self.assertEqual([r['periodo'] for r in detail if r['cambio_log'] is None], [core.label(24020),core.label(24021)])
        self.assertEqual(summary['cambios_referencia'], 34)
        self.assertEqual(summary['fin_referencia'], core.label(24036))
        self.assertEqual(detail[21]['rango_movil'], None)

    def test_no_concatena_rachas(self):
        data = points([100+i for i in range(49)])
        del data[24020]
        summary, detail = core.evaluate_series('EPM', ('a',), 'punta', data)
        self.assertEqual(summary['estado'], 'historia_insuficiente')
        self.assertFalse(detail)

    def test_cuarentena_es_por_celda_y_r12_advertencia(self):
        row = {c:'10' for c in core.SOURCES['EPM']['measures']}
        row.update(year='2020', mes='Enero')
        finding = dict(regla='R12 Magnitud', clave_contenido=core.content_key(row), columna='Punta', severidad='Error')
        q = core.quarantine([row], [finding])
        self.assertEqual(q[0]['severidad'], 'Advertencia')
        series = core.build_series('EPM', [row], q)
        self.assertEqual(series[(('', '', '', '', ''), 'punta')][24240]['reason'], 'cuarentena')
        self.assertEqual(series[(('', '', '', '', ''), 'compartido')][24240]['reason'], '')

    def test_conflictos_no_se_promedian_y_reordenamiento_es_invariante(self):
        row = dict(year='2020', mes='Enero', punta='10')
        second = dict(row, punta='1000')
        first = core.build_series('EPM', [row,second])
        self.assertEqual(first, core.build_series('EPM', [second,row]))
        self.assertEqual(first[(('', '', '', '', ''), 'punta')][24240]['reason'], 'duplicado_conflictivo')

    def test_bootstrap_remuestrea_categorias_completas(self):
        summaries = [dict(fuente='EPM', categoria=c, estado='evaluable', señales=hit, cambios_vigilancia=12)
                     for c,hit in [('a',0),('a',0),('a',0),('b',12)]]
        result = core.cluster_bootstrap(summaries, repetitions=200)
        self.assertEqual(result[0]['categorias'], 2)
        self.assertEqual(result[0]['series'], 4)
        self.assertEqual(result[0]['tasa'], .25)
        self.assertEqual(result[0]['ic95_inferior'], 0)
        self.assertEqual(result[0]['ic95_superior'], 1)
        self.assertEqual(result, core.cluster_bootstrap(list(reversed(summaries)), repetitions=200))

    def test_sin_ic_con_una_categoria(self):
        result = core.cluster_bootstrap([dict(fuente='XM',categoria='a',estado='evaluable',señales=0,cambios_vigilancia=12)])
        self.assertIsNone(result[0]['ic95_inferior'])

    def test_identidad_conserva_duplicados_e_ignora_id_api(self):
        a, b = {'x':'1', ':id':'abc'}, {'x':'2', ':id':'def'}
        self.assertTrue(core.compare_rows([a,b,a], [dict(a, **{':id':'xyz'}),a,b])['mismos_registros'])
        self.assertFalse(core.compare_rows([a,b,a], [a,b])['mismos_registros'])

    def test_api_guarda_ids_hashes_y_no_inventa_captura_completa(self):
        def fetch(url):
            if '/api/views/' in url:
                obj = {'columns':[{'fieldName':'x'}]}
            elif 'count' in url:
                obj = [{'n':'1'}]
            else:
                obj = [{':id':'real-id', 'x':'dato'}]
            return json.dumps(obj).encode(), obj
        with tempfile.TemporaryDirectory(dir=ROOT) as folder:
            output = acquisition.download('EPM', base=folder, fetch=fetch)
            doc = json.loads((output/'manifiesto.json').read_text(encoding='utf-8'))
            self.assertEqual(doc['estado'], 'completa')
            self.assertEqual(core.read_csv(output/'identificadores.csv')[0]['api_row_id'], 'real-id')
            self.assertEqual(doc['sha256_datos'], core.digest(output/'datos.csv'))
            def bad(url):
                raw,obj = fetch(url)
                if isinstance(obj,list) and obj and ':id' in obj[0]:
                    del obj[0][':id']
                return json.dumps(obj).encode(),obj
            with self.assertRaises(ValueError):
                acquisition.download('EPM', base=folder, fetch=bad)
            failed = [json.loads(p.read_text(encoding='utf-8')) for p in Path(folder).rglob('manifiesto.json')]
            self.assertEqual(sum(d['estado']=='incompleta' for d in failed), 1)

    def test_opo_no_convierte_cobertura_en_puntualidad(self):
        result,_ = opportunity.measure('sfcd-b3ey')
        self.assertEqual(result['estado'], 'no_medible')
        self.assertIsNone(result['valor'])

    def test_opo_intervalo_indeterminado_y_plazo_real(self):
        with tempfile.TemporaryDirectory(dir=ROOT) as folder:
            evidence = Path(folder)/'evidencia.txt'
            evidence.write_text('registro de observacion', encoding='utf-8')
            row = dict(estado_evidencia='verificada', revisor='revisor', fundamento_plazo_url='https://example.org/plazo',
                       consumidor='investigador', archivo_evidencia=str(evidence), sha256_evidencia=core.digest(evidence),
                       fecha_limite='2026-11-01T12:00:00-05:00', observado_ausente_hasta='2026-11-01T11:00:00-05:00',
                       observado_presente_desde='2026-11-01T13:00:00-05:00')
            self.assertEqual(opportunity.classify(row)[0], 'indeterminada')
            row['disponible_desde_exacto'] = '2026-11-01T11:30:00-05:00'
            self.assertEqual(opportunity.classify(row)[0], 'a_tiempo')
            row['disponible_desde_exacto'] = '2026-11-01T12:01:00-05:00'
            self.assertEqual(opportunity.classify(row)[0], 'tardia')


if __name__ == '__main__':
    unittest.main()
