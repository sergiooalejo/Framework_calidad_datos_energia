"""Regresiones de los nuevos accesos de ejecución y configuración."""
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'configs/proyecto.json').is_file())


class CliActualTests(unittest.TestCase):
    def command(self, args, cwd, env):
        return subprocess.run([sys.executable, '-B', *args], cwd=cwd, env=env,
                              capture_output=True, text=True, encoding='utf-8')

    def test_modulo_nuevo_desde_fuera_usa_checkout_explicito(self):
        env = dict(os.environ, PYTHONPATH=str(ROOT / 'src'), FRAMEWORK_ENERGIA_ROOT=str(ROOT))
        with tempfile.TemporaryDirectory() as folder:
            current = self.command(['-m', 'framework_calidad', 'listar'], folder, env)
            previous = self.command([str(ROOT / 'scripts/flujo_trabajo.py'), 'listar'], folder, env)
        self.assertEqual(current.returncode, 0, current.stderr)
        self.assertEqual(previous.returncode, 0, previous.stderr)
        self.assertEqual(current.stdout, previous.stdout)

    def test_raiz_explicita_invalida_no_ejecuta(self):
        with tempfile.TemporaryDirectory() as folder:
            env = dict(os.environ, PYTHONPATH=str(ROOT / 'src'), FRAMEWORK_ENERGIA_ROOT=folder)
            result = self.command(['-m', 'framework_calidad', 'ejecutar', 'hito4'], folder, env)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('no contiene configs/proyecto.json', result.stderr)
        self.assertNotIn('Ejecutando', result.stdout)

    def test_registro_configura_realmente_los_comandos(self):
        # Una copia de configuración con una etapa nueva debe aparecer sin editar Python.
        import shutil
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / 'configs').mkdir()
            shutil.copyfile(ROOT / 'configs/proyecto.json', root / 'configs/proyecto.json')
            source = (ROOT / 'configs/etapas.toml').read_text(encoding='utf-8')
            source = source.replace('[tareas]', '[tareas]\nprueba_registro = ["ejemplo.py"]')
            (root / 'configs/etapas.toml').write_text(source, encoding='utf-8')
            env = dict(os.environ, PYTHONPATH=str(ROOT / 'src'), FRAMEWORK_ENERGIA_ROOT=folder)
            result = self.command(['-m', 'framework_calidad', 'listar'], folder, env)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('prueba_registro:\n  ejemplo.py', result.stdout)


if __name__ == '__main__':
    unittest.main()
