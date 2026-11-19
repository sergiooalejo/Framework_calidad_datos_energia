"""Comprueba los accesos de ejecución e imports después de mover los hitos."""
from pathlib import Path
import os
import subprocess
import sys
import tempfile
import unittest

ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'configs/proyecto.json').is_file())


class OrganizacionTests(unittest.TestCase):
    def command(self, args, cwd=ROOT, env=None):
        result = subprocess.run(
            [sys.executable, '-B', *args], cwd=cwd, env=env,
            capture_output=True, text=True, encoding='utf-8',
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        return result.stdout

    def test_cli_anterior_y_modulo_desde_otra_carpeta(self):
        expected = self.command(['-m', 'Code.interfaces.ejecutar', 'listar'])
        self.assertIn('Code.external_validation.ejecutar', expected)
        with tempfile.TemporaryDirectory() as directory:
            self.assertEqual(expected, self.command([str(ROOT / 'scripts/flujo_trabajo.py'), 'listar'], cwd=directory))
            self.assertEqual(expected, self.command([str(ROOT / 'Code/interfaces/ejecutar.py'), 'listar'], cwd=directory))

    def test_generador_conserva_acceso_anterior(self):
        expected = self.command(['-m', 'Code.external_validation.ejecutar', '--help'])
        self.assertIn('--salida', expected)
        for relative in ('Code/external_validation/generar_muestra_alertas.py',
                         'Code/model_evaluation/external_validation/generar_muestra_alertas.py'):
            self.assertIn('--salida', self.command([str(ROOT / relative), '--help']))

    def test_api_con_import_anterior_y_ruta_instalable(self):
        script = (
            'from pathlib import Path; import framework_calidad as f; '
            'import framework_calidad.configuracion as c; '
            'assert "src" in Path(c.__file__).parts; '
            'assert f.listar_indicadores({"indicadores": [{"id": "R01"}]}) == [{"id": "R01"}]; '
            'print(",".join(f.__all__))'
        )
        outputs = []
        for relative in ('src', 'Code', 'Code/interfaces'):
            env = dict(os.environ, PYTHONPATH=str(ROOT / relative))
            outputs.append(self.command(['-c', script], env=env))
        self.assertEqual(len(set(outputs)), 1)


if __name__ == '__main__':
    unittest.main()
