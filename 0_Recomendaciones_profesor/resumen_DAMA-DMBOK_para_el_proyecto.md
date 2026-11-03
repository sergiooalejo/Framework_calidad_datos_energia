# DAMA-DMBOK2 aplicado al proyecto: lo que el trabajo debe tomar del capítulo 13 (Data Quality)

Guía para el trabajo de grado *Framework automatizado para la evaluación de la calidad de datos en registros administrativos del sector energético en Colombia* (Grupo 03; dirección del trabajo). Referencia: DAMA International (2017), *DAMA-DMBOK2*, capítulo 13.

Actualización del 27 de octubre de 2026: el profesor exige medir las ocho dimensiones en EPM y CHEC. La especificación vigente está en [la matriz OE1](hito3/matriz_oe1.md). Este resumen describe antecedentes del Hito 2; R11/R12 no acreditan exactitud y la oportunidad ya no se excluye.

## 1. Definición y propósito

- **Calidad de datos** en DMBOK es *aptitud para el uso* (fitness for purpose): los datos son de calidad si sirven para lo que sus consumidores necesitan. No es una propiedad absoluta del archivo.
- **Gestión de calidad de datos** es la planeación, implementación y control de actividades que aplican técnicas de gestión de calidad a los datos para asegurar que sean aptos para su consumo.
- **Lo que falta en el proyecto:** nunca se dice quién consume las tarifas de EPM ni para qué (regulador, comercializador, usuario, investigador). Sin ese consumidor no se puede justificar qué dimensiones importan ni qué umbral es aceptable. Debe quedar escrito en la caracterización de cada fuente (OE2).

## 2. Dimensiones de calidad

DMBOK2 consolida las dimensiones de Strong y Wang, English, Loshin y DAMA UK (2013). Las ocho que lista son:

| Dimensión | Qué mide | En el proyecto |
|---|---|---|
| Exactitud (accuracy) | Grado en que el dato representa la realidad | EXA01: contraste muestral con publicación oficial; R11/R12 y modelos solo generan sospechas |
| Completitud (completeness) | Presencia de los datos requeridos | R01 período presente, R10 importes en cero |
| Consistencia (consistency) | Coherencia entre valores dentro y entre conjuntos | R06 etiqueta canónica, R08 orden EPM ≥ Compartido ≥ Cliente, R09 columnas por nivel |
| Integridad (integrity) | Integridad referencial y estructural | INT01/INT02 propuestos: esquema y referencias a catálogos; no confundir unicidad de clave con integridad completa |
| Razonabilidad (reasonability) | El patrón del dato cumple expectativas | Cartas I-MR y detección de anomalías: es aquí donde encajan, no solo en exactitud |
| Oportunidad (timeliness) | El dato está disponible cuando se necesita | OPO01: disponibilidad real frente a plazo documentado; evidencia externa pendiente y evaluación obligatoria |
| Unicidad (uniqueness) | Ninguna entidad aparece más de una vez | R04 duplicado exacto, R05 clave repetida |
| Validez (validity) | Valores dentro del dominio, tipo, formato y rango definidos | R02 año y mes, R03 formato numérico, R07 no negatividad |

Nota sobre ISO/IEC 25012: sus características inherentes son exactitud, completitud, consistencia, credibilidad y actualidad. Unicidad y validez no existen con ese nombre en la norma: vienen de DAMA. El documento debe decir qué toma de cada marco y no presentarlos como equivalentes.

**Lo que falta:** el Hito 2 etiqueta reglas con dimensiones pero no define cada dimensión para este conjunto, no usa razonabilidad (que es donde DMBOK ubica el monitoreo estadístico) y deja integridad y oportunidad sin mencionar.

## 3. Tipos de regla de negocio

DMBOK2 (siguiendo a Loshin) clasifica las reglas de calidad en diez tipos. Cada regla del proyecto debe declarar su tipo:

1. Conformidad definicional (el dato significa lo mismo en todos los usos).
2. Presencia de valor y completitud de registro: R01, R10.
3. Cumplimiento de formato: R03.
4. Pertenencia a dominio de valores: R02 (meses), R06 (catálogo de etiquetas).
5. Conformidad de rango: R07, R11, R12.
6. Conformidad de mapeo (equivalencias entre codificaciones): sinónimos 0-CS y Rango 0 - CS.
7. Reglas de consistencia entre atributos: R08, R09.
8. Verificación de exactitud contra una fuente de referencia: pendiente, requiere la publicación original de EPM o la resolución CREG.
9. Verificación de unicidad: R04, R05.
10. Validación de oportunidad: OPO01; dentro del alcance obligatorio, pendiente de evidencia temporal verificable.

## 4. Cómo se define una métrica

DMBOK2 exige que una métrica de calidad tenga seis propiedades: **medible**, **relevante para el negocio**, con **umbral de aceptación**, con **responsable** (steward), **controlable** (si falla, alguien puede actuar) y con **tendencia** (se mide en el tiempo). Esto es exactamente lo que pide el OE1 y lo que el Hito 2 no entrega.

Plantilla que cada indicador del proyecto debe llenar:

| Campo | Ejemplo con R08 |
|---|---|
| Nombre | Orden de tarifas por propiedad de red |
| Dimensión | Consistencia |
| Tipo de regla | Consistencia entre atributos |
| Regla | Propiedad EPM ≥ Compartido ≥ Propiedad del Cliente en Nivel I |
| Fórmula | 1 − (filas que incumplen / filas de Nivel I con importes) |
| Unidad | Porcentaje de filas |
| Umbral | ≥ 99,5 % (justificar) |
| Severidad | Error / advertencia / informativa |
| Frecuencia | Por cada descarga del portal |
| Responsable | Quien ejecuta el framework |
| Tendencia | Valor por mes de publicación |

## 5. Ciclo de actividades

DMBOK2 organiza la gestión de calidad como ciclo Shewhart-Deming (planear, hacer, verificar, actuar) con estas actividades:

1. **Definir qué es dato de alta calidad** para los consumidores identificados.
2. **Definir la estrategia** de calidad.
3. **Identificar los datos críticos y las reglas de negocio.** No todo se controla igual: hay que decir qué columnas son críticas (los importes) y cuáles son de apoyo.
4. **Evaluación inicial** mediante perfilamiento (data profiling): es el Hito 1.
5. **Identificar y priorizar mejoras.**
6. **Definir metas** de mejora.
7. **Operar**: gestionar reglas, medir y monitorear, gestionar incidentes, documentar procedimientos y corregir defectos.

El framework del proyecto cubre las actividades 3, 4 y 7. El documento debe decirlo con estos nombres y señalar que la 1 y la 3 se resuelven en la caracterización de la fuente.

## 6. Técnicas que DMBOK2 recomienda y que el proyecto ya usa sin citarlas

- **Perfilamiento de datos**: evaluación inicial de estructura, nulos, dominios y duplicados. Es el Hito 1.
- **Módulos de verificación y auditoría en código**: reglas ejecutables, reutilizables y con bitácora. Es lo que el artefacto debe ser.
- **Control estadístico de procesos**: DMBOK2 dedica una sección a cartas de control con límites superior e inferior para distinguir variación común de variación especial en los datos. Es la justificación de las cartas I-MR dentro del marco DAMA, y resuelve la objeción de que las cartas no estaban en el anteproyecto. Hay que citarlo.
- **Análisis de causa raíz**: la hipótesis del serial de Excel es un análisis de causa raíz y debe presentarse como tal.
- **Gestión de incidentes de calidad**: el archivo de hallazgos ya es una bitácora de incidentes. Falta estado (abierto, confirmado, descartado), responsable y fecha de resolución.
- **Tablero de calidad (scorecard)**: indicadores por dimensión con umbral y tendencia. Es el tablero del anteproyecto.

## 7. Qué deben escribir los estudiantes

1. En el marco teórico: las ocho dimensiones con definición de DMBOK2, cuáles usa el proyecto y por qué, y la relación con ISO/IEC 25012.
2. En la metodología: los diez tipos de regla, el ciclo de actividades y las técnicas, con la sección de control estadístico de procesos como respaldo de las cartas.
3. Como entregable del OE1: una matriz con cada regla clasificada por dimensión y tipo, con su métrica en la plantilla de la sección 4.
4. En la caracterización de cada fuente: consumidores, uso, datos críticos y, para cada dimensión, el umbral de aceptación justificado.
5. En resultados: un scorecard por fuente y dimensión, además de las curvas de detección.
