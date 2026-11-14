"""Comprueba los accesos de ejecución e imports después de mover los hitos."""
from pathlib import Path
import os
import subprocess
import sys
import tempfile
import unittest

ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'project.json').is_file())


class OrganizacionTests(unittest.TestCase):
    def command(self, args, cwd=ROOT, env=None):
        result = subprocess.run(
            [sys.executable, '-B', *args], cwd=cwd, env=env,
            capture_output=True, text=True, encoding='utf-8',
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        return result.stdout

    def test_cli_anterior_y_modulo_desde_otra_carpeta(self):
        expected = self.command(['-m', 'Code.hito5.run', 'listar'])
        self.assertIn('Code.hito6.run', expected)
        with tempfile.TemporaryDirectory() as directory:
            self.assertEqual(expected, self.command([str(ROOT / 'pipeline.py'), 'listar'], cwd=directory))
            self.assertEqual(expected, self.command([str(ROOT / 'Code/hito5/run.py'), 'listar'], cwd=directory))

    def test_generador_conserva_acceso_anterior(self):
        expected = self.command(['-m', 'Code.hito6.run', '--help'])
        self.assertIn('--salida', expected)
        for relative in ('Code/hito6/generar_muestra_alertas.py',
                         'Code/Evaluation/hito6/generar_muestra_alertas.py'):
            self.assertIn('--salida', self.command([str(ROOT / relative), '--help']))

    def test_api_con_import_anterior_y_ruta_instalable(self):
        script = (
            'from pathlib import Path; import framework_calidad as f; '
            'import framework_calidad.config as c; '
            'assert "hito5" in Path(c.__file__).parts; '
            'assert f.listar_indicadores({"indicadores": [{"id": "R01"}]}) == [{"id": "R01"}]; '
            'print(",".join(f.__all__))'
        )
        outputs = []
        for relative in ('Code', 'Code/hito5'):
            env = dict(os.environ, PYTHONPATH=str(ROOT / relative))
            outputs.append(self.command(['-c', script], env=env))
        self.assertEqual(*outputs)


if __name__ == '__main__':
    unittest.main()
