# Verificación del Hito 3

Estado: implementación local corregida y reproducida, con cierre integral pendiente
de evidencia externa y de la integración en el documento académico oficial.

## Evidencia de las fuentes y del remuestreo

| Fuente | Dataset | Filas de entrada | Períodos | Series evaluadas | Categorías remuestreadas |
|---|---|---:|---:|---:|---:|
| EPM | sfcd-b3ey | 3623 | 61 | 61 | 22 |
| CHEC | c698-wqig | 40609 | 225 | 272 | 138 |
| SSPD | ebby-cjha | 15075 | 59 | 387 | 157 |
| XM | c1b851 | 61 | 61 | 1 | 1 |
| SSPD_PLAN | vfjy-6fka | 5396 | 8 | 0 | 0 |

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

- EPM: comparadas; mismos registros=True; mismos hallazgos R01–R11=True; mismas cartas y claves=True.
- CHEC: comparadas; mismos registros=True; mismos hallazgos R01–R11=True; mismas cartas y claves=True.
- SSPD_PLAN: comparadas; mismos registros=True; mismos hallazgos R01–R11=True; mismas cartas y claves=True.

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
