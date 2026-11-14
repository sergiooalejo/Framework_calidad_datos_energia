"""Comprueba sin escribir la evidencia generada por el Hito 3."""
import json

from .core import ROOT, SOURCES, digest, read_csv


def main():
    import yaml
    out = ROOT / 'Data/gold/outputs/hito3'
    manifest = json.loads((out/'manifiesto.json').read_text(encoding='utf-8'))
    for group in ('codigo','configuraciones_y_evidencia','salidas'):
        for relative, expected in manifest[group].items():
            if digest(ROOT/relative) != expected:
                raise ValueError('Huella distinta: ' + relative)
    for entry in manifest['entradas']:
        if digest(ROOT/entry['archivo']) != entry['sha256']:
            raise ValueError('Dato modificado: ' + entry['archivo'])
    matrix = read_csv(ROOT/'Data/gold/outputs/calidad/matriz_oe1.csv')
    specification = yaml.safe_load((ROOT/'Data/gold/outputs/calidad/matriz_oe1.yaml').read_text(encoding='utf-8'))
    indicators = {i['id']:i for i in specification['indicadores']}
    assert len(indicators)==19 and len(matrix)==76
    for row in matrix:
        result = indicators[row['control']]['resultado'][row['fuente'].lower()]
        assert result['estado']==row['estado_medicion'], (row['control'],row['fuente'])
        assert (None if row['resultado_numerador']=='' else float(row['resultado_numerador'])) == result['numerador']
        assert (None if row['resultado_denominador']=='' else float(row['resultado_denominador'])) == result['denominador']
    for row in matrix:
        if row['control']=='CART01' and row['resultado_denominador']:
            details = read_csv(out/f"{row['fuente']}/cartas_detalle.csv")
            hits = sum(int(r['senal_imr']) for r in details if r['fase']=='vigilancia' and r['senal_imr'])
            assert float(row['resultado_numerador'])==hits
    evaluated = 0
    for source in SOURCES:
        summary = read_csv(out/f'{source}/cartas_resumen.csv')
        detail = read_csv(out/f'{source}/cartas_detalle.csv')
        current = [r for r in summary if r['estado']=='evaluable']
        evaluated += len(current)
        assert len(detail) == 48*len(current), source
        assert len({d['clave_alerta_estable'] for d in detail}) == len(detail), source
        assert sum(int(r['señales']) for r in current) == sum(int(r['senal_imr']) for r in detail if r['fase']=='vigilancia' and r['senal_imr']), source
        assert all(r['cambio_log']=='' and r['rango_movil']=='' for r in detail if r['motivo_exclusion']), source
    models = json.loads((out/'isolation_forest_modelos.json').read_text(encoding='utf-8'))['modelos']
    assert all(m['primera_vigilancia'] is None or m['fin_referencia'] < m['primera_vigilancia'] for m in models)
    comparisons = json.loads((out/'comparacion_descargas.json').read_text(encoding='utf-8'))['comparaciones']
    assert len(comparisons)==3
    assert all(c.get('mismos_registros') and c.get('mismos_hallazgos_R01_R11') and c.get('mismas_cartas_y_claves') for c in comparisons)
    assert all(r['severidad']=='Advertencia' for r in read_csv(out/'cuarentena_celdas_epm.csv') if r['regla']=='R12')
    print(json.dumps(dict(estado='correcto', series_evaluadas=evaluated, modelos_if=len(models),
        pares_descargas_verificados=len(comparisons), cierre_integral=False,
        nota='Evidencia externa y aceptación académica pendientes; ver criterios_cierre.json'),ensure_ascii=False,indent=2))


if __name__ == '__main__':
    main()
