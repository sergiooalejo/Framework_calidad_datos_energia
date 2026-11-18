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
    commands = [['pipeline.py', 'validar']]
    if not args.sin_pruebas:
        commands.append(['pipeline.py', 'pruebas'])
    commands += [['-m', 'Code.hito3.verify'], ['-m', 'Code.hito4.verify']]
    for command in commands:
        print('Verificando: ' + ' '.join(command), flush=True)
        subprocess.run([sys.executable, '-B', '-X', 'utf8', *command], cwd=ROOT, check=True,
                       env=dict(os.environ, PYTHONDONTWRITEBYTECODE='1', PYTHONIOENCODING='utf-8'))


if __name__ == '__main__':
    main()
