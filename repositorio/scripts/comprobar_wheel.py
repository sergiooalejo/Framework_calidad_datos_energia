"""Instala el wheel sin dependencias en una carpeta temporal y prueba sus accesos."""
import argparse
import os
from pathlib import Path
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('wheel', type=Path)
    args = parser.parse_args()
    wheel = args.wheel.resolve()
    if not wheel.is_file():
        parser.error(f'No existe el wheel: {wheel}')
    with tempfile.TemporaryDirectory() as folder:
        target = Path(folder) / 'instalado'
        subprocess.run([sys.executable, '-m', 'pip', 'install', '--no-deps', '--no-index',
                        '--target', str(target), str(wheel)], check=True)
        env = dict(os.environ, PYTHONPATH=str(target), FRAMEWORK_ENERGIA_ROOT=str(ROOT),
                   PYTHONDONTWRITEBYTECODE='1', PYTHONIOENCODING='utf-8')
        code = ("from pathlib import Path; import framework_calidad as f; "
                "import framework_calidad.config as c; "
                "assert 'instalado' in Path(c.__file__).parts; "
                "assert f.listar_indicadores({'indicadores': [{'id': 'R01'}]}) == [{'id': 'R01'}]; "
                "print('API instalada: correcta')")
        subprocess.run([sys.executable, '-B', '-c', code], cwd=folder, env=env, check=True)
        subprocess.run([sys.executable, '-B', '-m', 'framework_calidad', 'validar'],
                       cwd=folder, env=env, check=True)
        executable = target / 'bin' / ('framework-energia.exe' if os.name == 'nt' else 'framework-energia')
        subprocess.run([str(executable), 'listar'], cwd=folder, env=env, check=True)


if __name__ == '__main__':
    main()
