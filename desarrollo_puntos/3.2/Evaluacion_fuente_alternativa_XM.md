# Fuente alternativa investigada: demanda eléctrica de XM/SIMEM

Consulta: 4 de noviembre de 2026. Se buscó electricidad colombiana, consumo/demanda, mínimo 10.000 registros, historia temporal para cartas y evidencia para medir las ocho dimensiones. El análisis considera que el profesor exige medirlas todas.

Actualización posterior al análisis inicial: se ejecutó un piloto de 61 meses para el grupo EPMC/EPMD/STR02. Los datos están en `fuentes_datos/datos/Datos_en_revision/XM_piloto/` y la decisión de cuatro fuentes en `fuentes_datos/PROPUESTA_CUATRO_FUENTES.md`. La longitud y continuidad se comprobaron bajo la política de mayor TX numérica disponible por mes; no bajo la versión final marcada en el calendario. Exactitud y oportunidad siguen pendientes. Las consultas puntuales que se describen abajo corresponden a la exploración inicial.

## Resultado de la búsqueda

La alternativa más prometedora fuera de las fuentes tarifarias es **XM/SIMEM: histórico de demanda real por agente**, dataset `c1b851`. Se comprobaron datos reales en kWh, códigos de agente como texto y versiones de liquidación. Es una recomendación para un piloto con alcance retrospectivo, no una afirmación de cumplimiento completo del proyecto.

Portal: https://www.simem.co/

Documentación oficial: https://github.com/EquipoAnaliticaXM/API_XM

Referencia en datos.gov.co: https://www.datos.gov.co/d/bt68-juyf . Su título corresponde a la estructura de demandas por código SIC, mercado y sistema; la evidencia efectiva de esta revisión se obtuvo directamente de SIMEM con el ID `c1b851`.

API de muestra: https://www.simem.co/backend-files/api/PublicData?datasetId=c1b851&startdate=2020-01-01&enddate=2020-01-02

El archivo de evidencia [perfiles/evaluacion_candidato_xm.json](perfiles/evaluacion_candidato_xm.json) conserva parámetros, metadatos, esquema, conteos, ejemplos y hashes de respuestas. Las muestras completas de las consultas no se incorporaron al repositorio y no se cambiaron los datasets seleccionados.

## Qué se comprobó directamente

| Condición | Evidencia |
|---|---|
| Electricidad colombiana | Variables del proceso de demandas del ASIC/XM |
| Magnitud energética | `CodigoVariable=DdaReal`, `UnidadMedida=kWh`, `CodigoDuracion=PT1H` |
| Volumen | Consulta 1–2 de enero de 2020: **17.472 registros**. Consulta 1–2 de enero de 2025: **106.632 registros**. Son tamaños de respuestas de dos días, no totales del conjunto |
| Identificación | `CodigoSICAgente`, `MercadoComercializacion`, `SistemaTransmision`, fecha/hora, variable y versión; no se usan NIU de facturas personales |
| Horizonte histórico | Se obtuvieron registros en 2020 y 2025. Eso demuestra acceso a cortes separados por cinco años, pero no demuestra continuidad de todos los meses por agente |
| Actualización | El metadato declara `c1b851` retirado y finalizado con corte 2026-06-30. Es utilizable como histórico; no prometer un flujo vivo |
| Versiones | Las respuestas incluyen `Version`; una misma hora puede tener múltiples revisiones y nunca deben sumarse entre sí |
| Publicación | Se obtuvieron registros de los conjuntos de versiones mensuales `24914f` y diarias `7a30a3`, con `FechaPublicacion`, `FechaInicio`, `FechaFin` y `Version` |

**Demanda no equivale a consumo facturado residencial:** representa energía del proceso de mercado; tiene otro uso y otras reglas que el CSV no residencial. La interpretación y las pérdidas incluidas se deben fijar según la variable y documentación seleccionadas.

## Advertencia sobre el reemplazo vigente

El inventario oficial relaciona `DdaReal` con el conjunto `14fabb`, llamado **Demanda real nacional**. Se comprobaron 4.512 registros para 1–2 de octubre de 2026, pero cero para 1–2 de enero de 2020. No se puede asumir que conserva el mismo histórico que `c1b851` ni concatenar ambos sin armonizar dimensiones y versiones. El conjunto antiguo y el vigente tienen estructuras diferentes.

No debe descargarse el conjunto nuevo pensando que basta para el protocolo mensual de 49/61 observaciones. Para una tesis retrospectiva puede fijarse el antiguo como snapshot; para operación futura hace falta un adaptador al esquema vigente.

## Cómo cubriría las ocho dimensiones

| Dimensión | Control posible y evidencia que falta |
|---|---|
| Completitud | Horas esperadas por agente, variable y versión; confirmar actividad de cada agente, dominio y calendario antes de contar ausencias |
| Validez | Tipos, fechas, unidad kWh, duración PT1H y dominios numéricos documentados |
| Unicidad | Clave candidata variable + agente + mercado + sistema + hora + versión; comprobarla sin confundir revisiones con duplicados |
| Consistencia | Coherencia de unidad/duración, agregaciones y revisiones equivalentes; no imponer ecuaciones que la fuente no define |
| Integridad | Relaciones de códigos con maestras oficiales de agentes y mercados, con vigencia temporal |
| Razonabilidad | Cartas y modelos sobre series homogéneas. Para conservar el protocolo mensual, descargar horas completas y agregar después de fijar versión; no multiplicar meses a partir de filas horarias |
| Exactitud | Contrastar una muestra con una publicación oficial de XM/Sinergox del mismo concepto, alcance y versión. Es concordancia documental, no medición independiente de cada contador físico |
| Oportunidad | Vincular cada versión con su fecha declarada de publicación y un plazo operativo/normativo documentado; todavía falta validar cobertura de ese vínculo y fundamento del plazo |

Los registros de publicaciones son un avance respecto de un archivo con solo fecha de facturación. Sin embargo, **tener `FechaPublicacion` no basta para declarar oportunidad evaluada**. Hay que comprobar qué publicación representa y qué versión se juzga. Por ejemplo, enero de 2020 tiene una versión TX5 con fecha declarada de publicación en agosto de 2021: puede ser una revisión, no la publicación inicial. No corresponde calificarla como retraso inicial sin reconstruir esa historia.

El cliente oficial contiene funciones que generan fechas/versiones auxiliares cuando faltan registros. Para OPO01 se deben conservar las respuestas crudas del servicio, distinguiendo fechas declaradas, deducidas y auxiliares. No usar fechas generadas como evidencia observada.

## Qué exige adaptar del proyecto

R08 y R09 del caso tarifario EPM se basan en propiedad, nivel y columnas específicas que no existen aquí. Esta fuente no cumple la condición de ejecutar literalmente esas mismas reglas. Se necesitarían equivalentes justificados de consistencia del proceso de demanda, con trazabilidad del cambio y validación con el director. Tampoco deben inventarse dos reglas para forzar el número doce.

Si el requisito es mantener sin cambios la semántica de las doce reglas tarifarias, **no se recomienda reemplazar EPM/CHEC por XM**. En ese escenario se debe completar evidencia externa para las fuentes tarifarias o ampliar su alcance con seguimiento documentado de publicaciones.

## Alternativas de tarifas revisadas

- `td8k-vhq9` (costo unitario): **12.607 filas, solo seis meses de reporte de 2023**. Su metadato incluye `fech_public`, pero la referencia CHEC ya conservada contiene el centinela `1900-01-01` en ese campo. No basta para cartas mensuales ni para oportunidad.
- `4is2-3nif` (tarifas publicadas): **17.806 filas, solo seis meses de reporte de 2023**. Tiene fecha de publicación y nombre del diario; no resuelve la historia temporal del protocolo actual. No se verificó aquí la calidad de todas esas fechas.
- `supers_icnr-l4iw.csv`: **402.500 filas y doce meses**, con problemas de representación de identificadores. Útil como complemento de facturación, no como solución de historia mensual.

## Decisión recomendada

El mejor candidato nuevo para **investigar demanda con trazabilidad de versiones** es XM/SIMEM. Antes de seleccionarlo definitivamente se requiere un piloto: verificar continuidad mensual completa de un grupo fijo, descargar maestras, contrastar valores y enlazar publicaciones con plazos.

No se encontró una fuente verificada que reúna simultáneamente consumo, historia mensual completa por grupo, las doce reglas tarifarias intactas y evidencia ya suficiente para las ocho dimensiones. Esto es el resultado de esta búsqueda, no una afirmación de inexistencia de datos públicos.

Las conclusiones anteriores del repositorio que afirman que una combinación “no existe en Colombia” deben entenderse como resultados de búsquedas acotadas. Esta evaluación no respalda una afirmación universal de inexistencia.
