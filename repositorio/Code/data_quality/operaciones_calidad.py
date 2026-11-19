"""Adaptadores para los comandos históricos del Hito 3."""
from .nucleo import ROOT, SOURCES, cluster_bootstrap, quarantine, read_csv, write_csv


def prepare_quarantine():
    rows = quarantine(read_csv(ROOT / SOURCES['EPM']['path']),
                      read_csv(ROOT / 'z_findings/audits/trazabilidad_filas/03_hallazgos_trazabilidad.csv'))
    write_csv(ROOT / 'z_findings/results/data_quality/cuarentena_celdas_epm.csv', rows, list(rows[0]))
    return rows


def cards(source):
    from .ejecutar import run_source
    return run_source(source, prepare_quarantine() if source == 'EPM' else [], mirror=True)


def bootstrap():
    summaries = []
    for source in SOURCES:
        rows, _ = cards(source)
        summaries.extend(rows)
    rows = cluster_bootstrap(summaries)
    save_bootstrap(rows)
    print('Bootstrap vigente: categorias completas; z_findings/results/data_quality/bootstrap_categorias.csv')


def save_bootstrap(rows):
    import json
    write_csv(ROOT / 'z_findings/results/data_quality/bootstrap_categorias.csv', rows, list(rows[0]))
    legacy = ROOT / 'z_findings/results/cuarentena_bootstrap/bootstrap'
    write_csv(legacy / 'bootstrap_categorias.csv', rows, list(rows[0]))
    (legacy / 'configuracion.json').write_text(json.dumps(dict(unidad='categoria_completa',
        repeticiones=2000, semilla=20261105, estado='protocolo_hito3_corregido',
        inventario='z_findings/results/data_quality/inventario_categorias.csv'), indent=2)+'\n', encoding='utf-8')
    (legacy / 'README.txt').write_text('Bootstrap vigente: categorías completas dentro de cada fuente, '
        'con medidas y numeradores/denominadores juntos. No remuestrea series dentro de categorías. '
        'Ver z_findings/reports/data_quality/verificacion.md y z_findings/results/data_quality/inventario_categorias.csv. '
        'La versión anterior se conserva en z_findings/archive/evidence/antes_correccion_hito3/.\n', encoding='utf-8')


def review_epm():
    _, detail = cards('EPM')
    alerts = [dict(r, clasificacion='pendiente_revision') for r in detail if r['fase'] == 'vigilancia' and r['senal_imr']]
    write_csv(ROOT / 'z_findings/results/cartas/EPM/revision_senales_cartas_epm.csv', alerts,
              list(detail[0]) if detail else ['fuente', 'clave_alerta_estable'])
