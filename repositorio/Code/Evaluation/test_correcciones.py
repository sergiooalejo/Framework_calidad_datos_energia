"""Comprueba trazabilidad de semillas, scorecard y protección de muestras."""

import csv
import ast
import gzip
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'project.json').is_file())
sys.path.insert(0, str(ROOT))
import pipeline


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class CorreccionesTests(unittest.TestCase):
    def test_semillas_base_coinciden_con_los_scripts(self):
        sources = {
            'bootstrap_categorias': 'Code/Data_Acquisition_and_Understanding/cuarentena_bootstrap/bootstrap_categorias.py',
            'isolation_forest': 'Code/Modeling/detectores/isolation_forest_referencia_vigilancia.py',
            'sensibilidad_base': 'Code/Modeling/sensibilidad/analisis_sensibilidad.py',
            'metricas_base': 'Code/Modeling/metricas/experimento_tasa_igualada.py',
        }
        declared = {key: value for values in pipeline.SEEDS.values() for key, value in values.items()}
        for key, relative in sources.items():
            tree = ast.parse((ROOT / relative).read_text(encoding='utf-8-sig'))
            assignments = [node for node in tree.body if isinstance(node, ast.Assign)
                           and any(isinstance(t, ast.Name) and t.id == 'SEED' for t in node.targets)]
            self.assertEqual(len(assignments), 1, relative)
            self.assertEqual(declared[key], ast.literal_eval(assignments[0].value), relative)
        self.assertEqual(declared['isolation_forest_base'], declared['isolation_forest'])

    def test_semilla_de_muestra_coincide_con_el_generador(self):
        tree = ast.parse((ROOT / 'Code/hito6/generar_muestra_alertas.py').read_text(encoding='utf-8'))
        calls = [node for node in ast.walk(tree) if isinstance(node, ast.Call)
                 and isinstance(node.func, ast.Attribute) and isinstance(node.func.value, ast.Name)
                 and node.func.value.id == 'random' and node.func.attr == 'Random']
        self.assertEqual(len(calls), 1)
        self.assertEqual(ast.literal_eval(calls[0].args[0]), pipeline.SEEDS['muestra-h6']['seleccion_muestra'])

    def test_semilla_no_configurable_no_ejecuta_etapa(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / 'pipeline.py'), 'ejecutar', 'bootstrap', '--semilla', '17'],
            capture_output=True, text=True, encoding='utf-8', cwd=ROOT,
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('no es configurable', result.stderr)
        self.assertNotIn('Ejecutando', result.stdout)

    def test_manifiesto_registra_semilla_real_de_bootstrap(self):
        with tempfile.TemporaryDirectory() as directory, patch.object(pipeline, 'ROOT', Path(directory)):
            path = pipeline.execution_manifest('bootstrap')
            manifest = json.loads(path.read_text(encoding='utf-8'))
            self.assertEqual(manifest['semillas_base'], {'bootstrap_categorias': 20261105})
            self.assertNotIn('semilla', manifest)
            self.assertEqual(pipeline.seeds_for_stage('scorecard'), {})

    def test_scorecard_no_promedia_tasas_opuestas(self):
        module = load_module('scorecard_test', ROOT / 'Code/Evaluation/scorecard/generar_scorecard_oe1.py')
        with tempfile.TemporaryDirectory() as directory:
            source, target = Path(directory) / 'matriz.csv', Path(directory) / 'scorecard.csv'
            with source.open('w', encoding='utf-8', newline='') as stream:
                writer = csv.DictWriter(stream, fieldnames=['fuente', 'dimension', 'estado_medicion', 'resultado_valor'])
                writer.writeheader()
                writer.writerows([
                    {'fuente': 'CHEC', 'dimension': 'razonabilidad', 'estado_medicion': 'provisional', 'resultado_valor': '0'},
                    {'fuente': 'CHEC', 'dimension': 'razonabilidad', 'estado_medicion': 'provisional', 'resultado_valor': '98.8829'},
                ])
            with patch.object(module, 'MATRIX', source), patch.object(module, 'OUT', target):
                module.main()
            with target.open(encoding='utf-8', newline='') as stream:
                row = next(csv.DictReader(stream))
            self.assertEqual(row['promedio_indicadores'], '')
            self.assertEqual(row['controles'], '2')
            self.assertIn('pendiente', row['nota'])

    def test_muestra_no_sobrescribe_revision_y_no_afirma_lof(self):
        module = load_module('muestra_test', ROOT / 'Code/hito6/generar_muestra_alertas.py')
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / 'entrada.csv.gz'
            old = Path(directory) / 'muestra_alertas_50.csv'
            fields = ['fuente', 'cohorte', 'referencia', 'sid', 'serie', 'medida', 'categoria', 'periodo', *module.METHODS]
            with gzip.open(source, 'wt', encoding='utf-8', newline='') as stream:
                writer = csv.DictWriter(stream, fieldnames=fields)
                writer.writeheader()
                for source_name, quota in module.QUOTAS.items():
                    for i in range(quota):
                        row = dict.fromkeys(fields, '0')
                        row.update(fuente=source_name, sid=str(i), periodo='2020-01')
                        row['I_2.66_MRmedia'] = '1'
                        writer.writerow(row)
            old.write_text('revision irremplazable\n', encoding='utf-8')
            with patch.object(module, 'INPUT', source), patch.object(module, 'OUTPUT', old):
                created = module.main([])
                self.assertNotEqual(created, old)
                self.assertEqual(old.read_text(encoding='utf-8'), 'revision irremplazable\n')
                with created.open(encoding='utf-8-sig', newline='') as stream:
                    reader = csv.DictReader(stream)
                    self.assertNotIn('LOF', reader.fieldnames)
                    self.assertIn('serie', reader.fieldnames)
                    self.assertEqual(len(list(reader)), 50)
                with self.assertRaises(FileExistsError):
                    module.main(['--salida', str(old)])
                self.assertEqual(old.read_text(encoding='utf-8'), 'revision irremplazable\n')


if __name__ == '__main__':
    unittest.main()
