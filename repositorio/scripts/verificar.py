"""Verifica el checkout sin regenerar resultados científicos."""
import argparse
import os
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--sin-pruebas', action='store_true', help='Omitir suites ya ejecutadas')
    args = parser.parse_args()
    commands = [['scripts/flujo_trabajo.py', 'validar']]
    if not args.sin_pruebas:
        commands.append(['scripts/flujo_trabajo.py', 'pruebas'])
    commands += [['-m', 'Code.data_quality.verificar'], ['-m', 'Code.experiments.verificar']]
    for command in commands:
        print('Verificando: ' + ' '.join(command), flush=True)
        subprocess.run([sys.executable, '-B', '-X', 'utf8', *command], cwd=ROOT, check=True,
                       env=dict(os.environ, PYTHONDONTWRITEBYTECODE='1', PYTHONIOENCODING='utf-8'))


if __name__ == '__main__':
    main()
