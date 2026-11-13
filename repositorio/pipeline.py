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
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parent
PREP = 'Code/Data_Acquisition_and_Understanding/'
MODEL = 'Code/Modeling/'
EVAL = 'Code/Evaluation/'
MEDALLION_MANIFEST = ROOT / 'Data/medallion_manifest.json'
TASKS = {
    'trazabilidad': [PREP + 'trazabilidad/trazabilidad.py'],
    'cuarentena': [PREP + 'cuarentena_bootstrap/EPM/cuarentena.py', PREP + 'cuarentena_bootstrap/cuarentena_fuentes.py'],
    'cartas': [MODEL + f'cartas/{source}/cartas_log_{source.lower()}.py' for source in ('EPM', 'CHEC', 'SSPD', 'XM')],
    'revision-cartas': [MODEL + 'cartas/revision_cartas_fuentes.py', MODEL + 'cartas/EPM/revision_cartas_epm.py'],
    'matriz': [PREP + 'calidad/medir_matriz_oe1.py'],
    'bootstrap': [PREP + 'cuarentena_bootstrap/bootstrap_categorias.py'],
    'zscore': [MODEL + 'detectores/zscore_robusto.py'],
    'isolation-forest': [MODEL + 'detectores/isolation_forest_referencia_vigilancia.py'],
    'calibracion': [MODEL + 'detectores/calibracion_cv_tasa_igualada.py'],
    'sensibilidad': [MODEL + 'sensibilidad/analisis_sensibilidad.py'],
    'metricas': [MODEL + 'metricas/experimento_tasa_igualada.py'],
    'sistemica': [MODEL + 'regla_sistemica/calibrar_regla_sistemica.py'],
    'scorecard': [EVAL + 'scorecard/generar_scorecard_oe1.py'],
    'niveles-costos': [EVAL + 'niveles_costos/analizar_niveles_costos.py'],
    'muestra-h6': [EVAL + 'hito6/generar_muestra_alertas.py'],
    'figuras': [MODEL + f'{folder}/{name}.py' for folder, name in (
        ('sensibilidad', 'informe_sensibilidad'), ('metricas', 'informe_metricas'),
        ('regla_sistemica', 'informe_regla_sistemica'))],
}
BASELINE = ('trazabilidad', 'cuarentena', 'cartas', 'revision-cartas', 'matriz', 'bootstrap', 'scorecard', 'niveles-costos')
TESTS = (('sensibilidad', 'test_sensibilidad.py'), ('metricas', 'test_metricas.py'), ('regla_sistemica', 'test_regla_sistemica.py'))

# Son semillas base realmente utilizadas por los scripts; algunas técnicas derivan
# semillas por fuente, serie o partición. No se modifican desde el tablero.
SEEDS = {
    'bootstrap': {'bootstrap_categorias': 20261105},
    'isolation-forest': {'isolation_forest': 20261106},
    'calibracion': {'isolation_forest_base': 20261106},
    'sensibilidad': {'sensibilidad_base': 20261106},
    'metricas': {'metricas_base': 20261107},
    'muestra-h6': {'seleccion_muestra': 42},
}


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
    scripts = sorted((ROOT / 'Code').rglob('*.py')) + [Path(__file__)]
    for p in scripts:
        ast.parse(p.read_text(encoding='utf-8-sig'), filename=str(p))
    for group in TASKS.values():
        for entry in group:
            if not (ROOT / entry).is_file():
                raise RuntimeError(f'No existe el comando: {entry}')
    print(json.dumps({'estado': 'correcto', 'capas_medallon': len(medallion['capas']),
                      'archivos_mapeados': len(manifest),
                      'scripts_sintaxis_correcta': len(scripts), 'datos_integros': len(raw),
                      'figuras_regenerables_ausentes': len(regenerable_missing)}, indent=2))


def main():
    parser = argparse.ArgumentParser(description='Framework de calidad de datos de energía; ejecutar desde cualquier carpeta.')
    parser.add_argument('accion', choices=['listar', 'validar', 'pruebas', 'auditar', 'ejecutar'])
    parser.add_argument('etapa', nargs='?', choices=['baseline', *TASKS])
    parser.add_argument('--semilla', type=int, default=None,
                        help='No configurable: los métodos usan las semillas fijas documentadas')
    args = parser.parse_args()
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
        for folder, pattern in TESTS:
            run(['-m', 'unittest', 'discover', '-s', MODEL + folder, '-p', pattern, '-v'])
        run(['-m', 'unittest', 'discover', '-s', MODEL.rstrip('/'), '-p', 'test_medallon_compat.py', '-v'])
        run(['-m', 'unittest', 'discover', '-s', EVAL.rstrip('/'), '-p', 'test_correcciones.py', '-v'])
    elif args.accion == 'auditar':
        for folder, _ in TESTS:
            run([MODEL + folder + '/verificar_resultados.py'])
    elif args.accion == 'ejecutar':
        manifest = execution_manifest(args.etapa)
        print(f'Manifiesto: {manifest.relative_to(ROOT)}', flush=True)
        for task in BASELINE if args.etapa == 'baseline' else (args.etapa,):
            for script in TASKS[task]:
                print(f'Ejecutando {script}', flush=True)
                run([script])


if __name__ == '__main__':
    main()
