"""Entregables documentales regenerables y verificación de criterios del Hito 3."""
from collections import Counter, defaultdict
import json

from .core import ROOT, SOURCES, read_csv, month_index, number, content_key, write_csv

OUT = ROOT / 'Data/gold/outputs/hito3'


def original_sspd_matrix():
    """Matriz complementaria para la fuente literal del plan, sin inventar dominios."""
    cfg = SOURCES['SSPD_PLAN']
    rows = read_csv(ROOT / cfg['path'])
    template = [r for r in read_csv(ROOT / 'Data/gold/outputs/calidad/matriz_oe1.csv') if r['fuente']=='EPM']
    total = len(rows)
    present = sum(all(r.get(c, '').strip() for c in cfg['period']) for r in rows)
    valid = sum(month_index(r, cfg) is not None for r in rows)
    numeric = [(r.get(c, ''),number(r.get(c))) for r in rows for c in cfg['measures'] if r.get(c, '').strip()]
    duplicate = sum(v-1 for v in Counter(content_key(r) for r in rows).values())
    keys = Counter(tuple(r.get(c, '') for c in (*cfg['categories'], *cfg['period'])) for r in rows)
    conflicts = sum(n-1 for n in keys.values())
    zero = sum(all(number(r.get(c))==0 for c in cfg['measures']) for r in rows)
    negatives = sum(v is not None and v < 0 for _,v in numeric)
    serials = sum(v is not None and v.is_integer() and 36526 <= v <= 47483 for _,v in numeric)
    mapping = defaultdict(set)
    for r in rows:
        mapping[r['id_empresa']].add(r['empresa'])
    data = {
        'R01': (present,total,'medido','Campos anio y mes informados; no son fecha de publicación.'),
        'R02': (valid,present,'medido','Año entero y mes entre 1 y 12.'),
        'R03': (sum(v is not None for _,v in numeric),len(numeric),'medido','Diez medidas contables informadas convertibles a número finito; pesos según metadatos oficiales.'),
        'R04': (total-duplicate,total,'medido','Filas sin copias exactas adicionales; se conserva una por cada contenido.'),
        'R05': (total-conflicts,total,'provisional','Filas sin repetición adicional de clave candidata empresa + mercado + estrato/sector + año + mes; falta confirmar clave con el publicador.'),
        'R06': (None,None,'no_medible','Se observan códigos 1–16 de estra_sector, pero falta catálogo autorizado; observarlos no valida su dominio.'),
        'R07': (None,None,'no_medible',f'Se observan {negatives} celdas negativas. Refacturaciones pueden generar ajustes; no se impone no negatividad sin catálogo de dominio.'),
        'R08': (None,None,'no_aplica','No tiene columnas EPM/compartido/cliente ni relación de propiedad tarifaria.'),
        'R09': (None,None,'no_aplica','No tiene nivel de tensión ni punta/fuera de punta.'),
        'R10': (total-zero,total,'provisional','Filas con al menos una de las diez medidas contables distinta de cero; advertencia para revisión, no prueba de dato faltante.'),
        'R11': (serials,len(numeric),'provisional','Importes enteros en intervalo de seriales Excel; solo sospecha, muchos importes legítimos pueden coincidir.'),
        'R12': (None,None,'no_medible','Solo ocho períodos; sin referencia/vigilancia suficiente para el protocolo mensual.'),
        'INT01': (len(rows[0]),16,'medido','Contrato de 16 columnas contrastado con metadatos API conservados.'),
        'INT02': (sum(len(v)==1 for v in mapping.values()),len(mapping),'provisional','Consistencia interna de id_empresa a empresa; no sustituye catálogo externo.'),
        'EXA01': (None,None,'no_medible','Falta referencia independiente de registros contables por empresa/mercado/estrato/mes.'),
        'OPO01': (None,None,'no_medible','Faltan disponibilidad histórica y plazo documentado.'),
        'MAP01': (None,None,'no_medible','No se presuponen equivalencias de empresas, mercados ni códigos de sector.'),
        'DEF01': (16,16,'provisional','Metadatos oficiales describen las 16 columnas; estra_sector tiene definición general pero carece de catálogo de códigos.'),
        'CART01': (None,None,'no_aplica','Ocho períodos observados: no se ejecuta carta I-MR ni Isolation Forest con protocolo 36+12.'),
    }
    result = []
    for t in template:
        row = dict(t)
        n,d,state,note = data[t['control']]
        lower = t['control'] in ('R11',)
        row.update(fuente='SSPD_PLAN',dataset_id='vfjy-6fka',aplicacion_fuente=note,
                   poblacion='Registros contables y medidas aplicables del snapshot vfjy-6fka; ver resultado_nota.',
                   numerador=note,denominador='Filas, celdas informadas o códigos elegibles según el control; tamaño en resultado_denominador.',
                   resultado_numerador='' if n is None else n,resultado_denominador='' if d is None else d,
                   resultado_valor='' if not d else 100*n/d,estado_medicion=state,resultado_nota=note,
                   precondiciones='Adaptación al esquema contable; no transferir reglas de tarifas sin revisar el dominio.',
                   tendencia='Menor requiere interpretación de contexto' if lower else 'Mayor es mejor en controles de conformidad',
                   unidad_observacion='celda contable' if t['control'] in ('R03','R07','R11') else 'fila o clave indicada en resultado_nota')
        if t['control'] in ('R07','R08','R09','R12','CART01','R06','EXA01','OPO01','MAP01'):
            row.update(umbral_operador='',umbral_valor='',estado_umbral='no_aplica_o_pendiente_evidencia',
                       justificacion_umbral='No se define cumplimiento sin aplicabilidad y evidencia.')
        if t['control'] in ('R07','R10','R11','R12'):
            row.update(severidad='advertencia', umbral_operador='',umbral_valor='',estado_umbral='pendiente_calibracion')
        result.append(row)
    write_csv(OUT / 'SSPD_PLAN/matriz_oe1.csv', result, list(result[0]))


def generate(comparisons):
    original_sspd_matrix()
    profiles = {s:json.loads((OUT / s / 'perfil.json').read_text(encoding='utf-8')) for s in SOURCES}
    bootstrap = read_csv(OUT/'bootstrap_categorias.csv')
    table = ['| Fuente | Dataset | Filas de entrada | Períodos | Series evaluadas | Categorías remuestreadas |',
             '|---|---|---:|---:|---:|---:|']
    for s,p in profiles.items():
        b = next(r for r in bootstrap if r['fuente']==s)
        table.append(f"| {s} | {p['dataset_id']} | {p['filas']} | {p['periodos']} | {b['series']} | {b['categorias']} |")
    text = '''# Verificación del Hito 3

Estado: implementación local corregida y reproducida, con cierre integral pendiente
de evidencia externa y de la integración en el documento académico oficial.

## Evidencia de las fuentes y del remuestreo

'''+ '\n'.join(table) + '''

SSPD son agregados mensuales derivados de ebby-cjha. SSPD_PLAN es el conjunto literal
vfjy-6fka solicitado en el plan. Se conservan ambos; no se presenta uno como el otro.
Las categorías son claves completas de negocio, sin la columna de medida. En EPM se
mantienen juntas las propiedades; nunca se remuestrean propiedades independientes.
Los 28 grupos y 83 series del Hito 2 no se fuerzan sobre otra población: el protocolo
actual exige una racha mensual de 49 observaciones y excluye valores conflictivos.
El inventario enumera todos los conglomerados y sus tamaños.

## Correcciones implementadas

- I sobre diferencias de logaritmos con límites media ± 2,66 × MR media;
  MR con límite 3,267 × MR media. Límites estimados solo con referencia.
- Corte de 36 posiciones mensuales de referencia y 12 de vigilancia; se informan
  denominadores válidos, exclusiones y referencias insuficientes. No se rellenan huecos.
- Cuarentena por celda: se excluyen ambos cambios que tocan el valor. R08 sin celda
  identificable aparta las tres propiedades, conservando punta/fuera de punta.
- No se promedian duplicados conflictivos. Los idénticos conservan linaje por contenido.
- R12 es Advertencia; la mediana procede de referencia y no de vigilancia.
- Isolation Forest usa cuatro rasgos logarítmicos, escala y percentil 99,5 solo con
  referencia y modelos separados por fecha de corte. Los huecos invalidan el rezago.
- Bootstrap de 2.000 réplicas por categorías completas; numeradores y denominadores
  se remuestrean juntos. XM tiene una categoría y no recibe un IC inferencial.
- OPO01 admite evidencia temporal con plazo, consumidor, revisor y archivo con hash.
  Sin ella se informa no medible, sin convertir cobertura temporal en puntualidad.
- Se reparó el YAML heredado: faltaban R02, R03 y R05 y sus resultados se desplazaban
  por posición. Ahora se escriben 19 indicadores por id, reconciliados con el CSV.
  CART01 reporta la tasa de alertas definida en la ficha, no su complemento.

## Comprobación entre descargas

'''
    for c in comparisons:
        text += f"- {c['fuente']}: {c['estado']}; mismos registros={c.get('mismos_registros')}; mismos hallazgos R01–R11={c.get('mismos_hallazgos_R01_R11')}; mismas cartas y claves={c.get('mismas_cartas_y_claves')}.\n"
    text += '''
Las capturas son peticiones reales independientes, consecutivas, con :id, páginas
originales, fecha UTC y SHA-256. Demuestran igualdad en esos dos cortes, no
estabilidad futura ni fecha histórica de publicación. CHEC actual incorpora registros
posteriores al snapshot experimental; no sustituye silenciosamente la entrada del Hito 4.
Las diferencias de representación entre CSV histórico y API se conservan y no se
confunden con una nueva validación del valor económico.

## Entregables y pendientes

| Actividad | Evidencia local | Estado |
|---|---|---|
| 3.1 Matriz y fichas OE1 | matriz principal CSV/YAML/TXT; matriz SSPD_PLAN complementaria | Especificada y medida donde hay evidencia; oportunidad/catálogos pendientes |
| 3.2 Caracterización | FICHAS_FUENTES_HITO3.md y perfiles JSON | Disponible; semántica no documentada por publicador sigue delimitada |
| 3.3 Réplica | notebook, hallazgos y matriz de vfjy-6fka; informe de diferencias | Disponible; cartas no aplican con ocho períodos |
| 3.4 CREG | ACTUALIZACION_ANTEPROYECTO_HITO3.md, apartado OE2/5.8, y búsqueda conservada | Reformulación por escrito; aceptación académica pendiente |
| 3.5 Cartas y rasgos IF | cartas_detalle/resumen, isolation_forest y modelos JSON | Corregida y reproducida; aceptación de supuestos pendiente |
| 3.6 Trazabilidad | capturas API, comparacion_descargas.json y claves en hallazgos/cartas | Igualdad comprobada en dos capturas EPM/CHEC/vfjy-6fka |
| 3.7 Cuarentena y bootstrap | cuarentena_celdas_epm.csv, inventario y bootstrap_categorias.csv | Corregida; R12 es advertencia |
| Anteproyecto actualizado | ACTUALIZACION_ANTEPROYECTO_HITO3.md | Texto listo en repositorio; no se afirma editado el documento oficial externo |

No se declara el cierre de las ocho dimensiones: OPO01 requiere evidencia de
disponibilidad y plazo, y EXA01 solo cubre muestras parciales. Faltan catálogos
autorizados, responsables nominales y aprobación de umbrales. Ninguna ejecución de
código sustituye estas evidencias. La consulta formal del Hito 6 no se considera hecha.

## Reproducción

Desde repositorio/: `python pipeline.py ejecutar hito3`. Para nuevas capturas reales:
`python pipeline.py ejecutar hito3-descargar` y después ejecutar hito3.
Pruebas: `python -B -m unittest discover -s Code/hito3 -p "test_*.py" -v`.
El notebook HITO3_REPLICACION.ipynb ejecuta ese mismo flujo.

Las salidas previas se conservan en Docs/evidencia_historica/antes_correccion_hito3/.
Los experimentos 4.2–4.4 son evidencia de su protocolo histórico: deben reevaluarse
antes de atribuirles las nuevas cartas, denominadores o cuarentenas.
'''
    (ROOT/'Docs/VERIFICACION_HITO3.md').write_text(text, encoding='utf-8')
    consumers = {'EPM':'usuarios tarifarios, comercializadores e investigadores de tarifas',
                 'CHEC':'usuarios tarifarios, comercializadores e investigadores de costos unitarios',
                 'SSPD':'analistas de facturación y consumo de empresas ZNI',
                 'XM':'analistas del mercado y demanda energética; demanda no equivale a consumo facturado',
                 'SSPD_PLAN':'analistas de subsidios, contribuciones y FOES; supervisión y contabilidad sectorial'}
    fichas = '# Fichas de caracterización vigentes · Hito 3\n\nLas definiciones detalladas y evidencia histórica se conservan en REFERENCIA_TECNICA.md.\n'
    for s,p in profiles.items():
        fichas += f"\n## {s} · {p['dataset_id']}\n\n- Archivo: `{p['archivo']}`.\n- SHA-256: `{p['sha256']}`.\n- {p['filas']} filas; {len(p['columnas'])} columnas; {p['periodos']} períodos distintos de {p['inicio']} a {p['fin']}.\n- Consumidores: {consumers[s]}.\n- Datos críticos: período, clave de negocio y medidas. Clave: {', '.join(SOURCES[s]['categories'])}. Medidas: {', '.join(SOURCES[s]['measures'])}.\n- Ausentes por columna: {json.dumps(p['ausentes_por_columna'], ensure_ascii=False)}.\n"
        if s=='SSPD_PLAN':
            fichas += '\nLos metadatos oficiales definen importes contables en pesos, año/mes contables y estrato/sector. No contiene Rango de Consumo: la afirmación de 2.143 ausentes no se puede atribuir a este esquema. Los ocho períodos no alcanzan 49 meses; solo reglas transversales. Los códigos de estrato/sector requieren catálogo autorizado. Véanse las dos capturas y sus metadatos originales.\n'
        elif s in ('EPM','CHEC'):
            fichas += '\nTarifas/componentes: las unidades y aplicabilidades exactas dependen de concepto, nivel y modalidad; los catálogos internos no son confirmación del publicador. Exactitud disponible solo para el alcance contrastado. Oportunidad histórica pendiente.\n'
        else:
            fichas += '\nUnidad y agregación: véanse diccionarios versionados SSPD/XM y ficha histórica. No se aplican relaciones de propiedad de EPM a consumo/demanda. Exactitud independiente y oportunidad siguen delimitadas por evidencia.\n'
    (ROOT/'Docs/FICHAS_FUENTES_HITO3.md').write_text(fichas,encoding='utf-8')
    report = dict(estado='parcial_no_cierre_integral', implementacion='corregida_y_ejecutada',
        descargas_reales=comparisons, faltantes_externos=['Oportunidad real con plazo y disponibilidad verificables EPM/CHEC',
        'Catálogos externos y aprobación de semántica/umbrales/responsables', 'Integración y aprobación del documento académico oficial'],
        documentos=['Docs/VERIFICACION_HITO3.md','Docs/FICHAS_FUENTES_HITO3.md','Docs/ACTUALIZACION_ANTEPROYECTO_HITO3.md'])
    (OUT/'criterios_cierre.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
