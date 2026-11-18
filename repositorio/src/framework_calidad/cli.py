"""Punto de entrada local: python pipeline.py --help."""
from pathlib import Path
import argparse
import ast
import csv
import hashlib
import json
import os
import subprocess
import sys
import tomllib
from .paths import project_root
from datetime import datetime, timezone

ROOT = project_root(required=False)
PREP = 'Code/Data_Acquisition_and_Understanding/'
MODEL = 'Code/Modeling/'
EVAL = 'Code/Evaluation/'
MEDALLION_MANIFEST = ROOT / 'Data/medallion_manifest.json'
CONFIG_PATH = ROOT / 'configs/pipeline.toml'
CONFIG = tomllib.loads(CONFIG_PATH.read_text(encoding='utf-8')) if CONFIG_PATH.is_file() else {}
TASKS = CONFIG.get('tareas', {})
BASELINE = tuple(CONFIG.get('baseline', ()))
SEEDS = CONFIG.get('semillas', {})
TESTS = (('sensibilidad', 'test_sensibilidad.py'), ('metricas', 'test_metricas.py'),
         ('regla_sistemica', 'test_regla_sistemica.py'))


def seeds_for_stage(stage):
    return dict(SEEDS['bootstrap'] if stage == 'baseline' else SEEDS.get(stage, {}))


def run(args):
    subprocess.run([sys.executable, '-B', *args], cwd=ROOT, check=True,
                   env=dict(os.environ, PYTHONDONTWRITEBYTECODE='1', PYTHONIOENCODING='utf-8'))


def execution_manifest(stage):
    """Registra la ejecución y las huellas de archivos de entrada disponibles."""
    files = []
    for data_root in (ROOT / 'Data/bronze/datos', ROOT / 'Data/silver/datos'):
        if data_root.exists():
            for path in sorted(data_root.rglob('*')):
                if path.is_file():
                    files.append({
                        'ruta': str(path.relative_to(ROOT)),
                        'sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
                        'bytes': path.stat().st_size,
                    })
    payload = {
        'ejecucion_utc': datetime.now(timezone.utc).isoformat(),
        'etapa': stage,
        'version_paquete': '0.1.0',
        'semillas_base': seeds_for_stage(stage),
        'nota_semillas': 'Fijas por método; algunas se derivan por fuente, serie o partición.',
        'python': sys.version,
        'archivos_entrada': files,
    }
    out = ROOT / 'Data/gold/outputs/ejecuciones'
    out.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
    target = out / f'manifiesto_{stamp}.json'
    target.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding='utf-8')
    return target


def validate():
    """Verifica estructura y datos sin regenerar resultados ni requerir paquetes externos."""
    for relative in ('src/framework_calidad/__init__.py', 'apps/streamlit_app.py',
                     'configs/pipeline.toml', 'tests/test_organizacion.py',
                     'scripts/verificar.py', 'notebooks/HITO3_REPLICACION.ipynb'):
        if not (ROOT / relative).is_file():
            raise RuntimeError(f'Falta un componente del proyecto: {relative}')
    if not set(BASELINE).issubset(TASKS):
        raise RuntimeError('El baseline contiene etapas no registradas')
    medallion = json.loads(MEDALLION_MANIFEST.read_text(encoding='utf-8'))
    missing_layers = {
        layer: [path for path in paths if not (ROOT / path).exists()]
        for layer, paths in medallion['capas'].items()
    }
    missing_layers = {layer: paths for layer, paths in missing_layers.items() if paths}
    if missing_layers:
        raise RuntimeError(f'Faltan rutas de la arquitectura medallón: {missing_layers}')
    manifest = list(csv.DictReader((ROOT / 'Docs/MIGRACION.csv').open(encoding='utf-8')))
    regenerable_prefixes = ('Data/gold/outputs/sensibilidad/figuras/', 'Data/gold/outputs/metricas/figuras/',
                            'Data/gold/outputs/regla_sistemica/figuras/')
    absent = [r['destino'] for r in manifest
              if not (ROOT / r['destino'].split('#')[0]).is_file()
              and not r['destino'].split('#')[0].startswith(regenerable_prefixes)]
    regenerable_missing = [r['destino'] for r in manifest
                           if not (ROOT / r['destino'].split('#')[0]).is_file()
                           and r['destino'].split('#')[0].startswith(regenerable_prefixes)]
    if absent:
        raise RuntimeError(f'Faltan archivos: {absent}')
    raw = [r for r in manifest if r['destino'].startswith(('Data/bronze/datos/', 'Data/silver/datos/'))]
    for row in raw:
        actual = hashlib.sha256((ROOT / row['destino']).read_bytes()).hexdigest()
        if actual != row['sha256_destino']:
            raise RuntimeError(f"Cambió el dato de entrada: {row['destino']}")
    scripts = sorted({p for folder in ('src', 'apps', 'tests', 'scripts', 'Code') for p in (ROOT / folder).rglob('*.py')})
    for p in scripts:
        ast.parse(p.read_text(encoding='utf-8-sig'), filename=str(p))
    for group in TASKS.values():
        if group and group[0] == '-m':
            if not (ROOT / (group[1].replace('.', '/') + '.py')).is_file():
                raise RuntimeError(f'No existe el módulo: {group[1]}')
            continue
        for entry in group:
            if not (ROOT / entry).is_file():
                raise RuntimeError(f'No existe el comando: {entry}')
    print(json.dumps({'estado': 'correcto', 'capas_medallon': len(medallion['capas']),
                      'archivos_mapeados': len(manifest),
                      'scripts_sintaxis_correcta': len(scripts), 'datos_integros': len(raw),
                      'figuras_regenerables_ausentes': len(regenerable_missing)}, indent=2))


def main():
    # Contrato UTF-8 para clientes que capturan la salida en Windows y Linux.
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, 'reconfigure'):
            stream.reconfigure(encoding='utf-8')
    parser = argparse.ArgumentParser(description='Framework de calidad de datos de energía; ejecutar desde cualquier carpeta.')
    parser.add_argument('accion', choices=['listar', 'validar', 'pruebas', 'auditar', 'ejecutar'])
    parser.add_argument('etapa', nargs='?', choices=['baseline', *TASKS])
    parser.add_argument('--semilla', type=int, default=None,
                        help='No configurable: los métodos usan las semillas fijas documentadas')
    args = parser.parse_args()
    if not CONFIG or not (ROOT / 'project.json').is_file():
        parser.error('No se encontró el proyecto. Ejecute desde repositorio/ o defina FRAMEWORK_ENERGIA_ROOT.')
    if args.accion == 'ejecutar' and not args.etapa:
        parser.error('ejecutar requiere una etapa; consultar listar')
    if args.accion != 'ejecutar' and args.etapa:
        parser.error('la etapa solo se utiliza con ejecutar')
    if args.semilla is not None:
        parser.error('La semilla no es configurable: cada método usa su semilla fija documentada.')
    if args.accion == 'listar':
        print('baseline: ' + ' -> '.join(BASELINE))
        for name, scripts in TASKS.items():
            print(name + ':\n  ' + '\n  '.join(scripts))
    elif args.accion == 'validar':
        validate()
    elif args.accion == 'pruebas':
        run(['-m', 'unittest', 'discover', '-s', 'tests', '-p', 'test_*.py', '-v'])
        run(['-m', 'unittest', 'discover', '-s', 'Code/hito4', '-p', 'test_*.py', '-v'])
        run(['-m', 'unittest', 'discover', '-s', 'Code/hito3', '-p', 'test_*.py', '-v'])
        for folder, pattern in TESTS:
            run(['-m', 'unittest', 'discover', '-s', MODEL + folder, '-p', pattern, '-v'])
        run(['-m', 'unittest', 'discover', '-s', MODEL.rstrip('/'), '-p', 'test_medallon_compat.py', '-v'])
    elif args.accion == 'auditar':
        for folder, _ in TESTS:
            run([MODEL + folder + '/verificar_resultados.py'])
    elif args.accion == 'ejecutar':
        manifest = execution_manifest(args.etapa)
        print(f'Manifiesto: {manifest.relative_to(ROOT)}', flush=True)
        for task in BASELINE if args.etapa == 'baseline' else (args.etapa,):
            if TASKS[task][0] == '-m':
                print('Ejecutando ' + ' '.join(TASKS[task]), flush=True)
                run(TASKS[task])
                continue
            for script in TASKS[task]:
                print(f'Ejecutando {script}', flush=True)
                run([script])


if __name__ == '__main__':
    main()
