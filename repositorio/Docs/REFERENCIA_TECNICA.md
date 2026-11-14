# Referencia técnica consolidada

**Nota de vigencia del Hito 4:** [VERIFICACION_HITO4.md](VERIFICACION_HITO4.md)
y [RESULTADOS_HITO4.md](RESULTADOS_HITO4.md) documentan el protocolo corregido,
la política LOF, el scorecard, las figuras y el nuevo contraste normativo. Las
secciones consolidadas siguientes describen sus experimentos históricos.

**Nota de vigencia del Hito 3:** las secciones siguientes conservan antecedentes.
Para la implementación corregida, descargas reales, categorías completas,
cuarentena por celda y límites I-MR prevalece
[VERIFICACION_HITO3.md](VERIFICACION_HITO3.md).
El texto de integración académica está en
[ACTUALIZACION_ANTEPROYECTO_HITO3.md](ACTUALIZACION_ANTEPROYECTO_HITO3.md).

Las secciones conservan el detalle y las fechas de cada evidencia. Los estados históricos no sustituyen el estado vigente de PROYECTO.md. La numeración 3.x/4.x indica procedencia, no la estructura de ejecución.

## Índice
- [0_Recomendaciones_profesor/resumen_DAMA-DMBOK_para_el_proyecto.md](#doc-a4bc47109979)
- [0_Recomendaciones_profesor/revision_hito2.md](#doc-94e9bf18d464)
- [desarrollo_puntos/3.1/EVIDENCIA_EXACTITUD_OPORTUNIDAD.md](#doc-dfcefa4bff36)
- [desarrollo_puntos/3.1/matriz_oe1.md](#doc-cd000226e09e)
- [desarrollo_puntos/3.1/README.md](#doc-ec2f495b53a8)
- [desarrollo_puntos/3.2/CHEC/DECISION_CATALOGOS_CHEC.md](#doc-cd7e104c7bc9)
- [desarrollo_puntos/3.2/CHEC/Ficha_caracterizacion_01_chec_c698-wqig.md](#doc-1b5778bfd6a3)
- [desarrollo_puntos/3.2/EPM/Ficha_caracterizacion_02_epm_sfcd-b3ey.md](#doc-6e7ee696f27e)
- [desarrollo_puntos/3.2/README.md](#doc-6d09f59e62b7)
- [desarrollo_puntos/3.2/SSPD/Ficha_caracterizacion_03_sspd_ebby-cjha.md](#doc-da864825bc1a)
- [desarrollo_puntos/3.2/XM/Ficha_caracterizacion_04_xm_c1b851.md](#doc-eab9a734865a)
- [desarrollo_puntos/3.3/CHEC/REVISION_REGLAS_CHEC.md](#doc-f0cd728e94a3)
- [desarrollo_puntos/3.3/EPM/REVISION_REGLAS_EPM.md](#doc-44ac9713606e)
- [desarrollo_puntos/3.3/INFORME_DIFERENCIAS_FUENTES.md](#doc-7dec091a7816)
- [desarrollo_puntos/3.3/insumos_hito2/README.md](#doc-70d8b8e8b09a)
- [desarrollo_puntos/3.3/README.md](#doc-1daec17adf88)
- [desarrollo_puntos/3.3/SSPD/REVISION_REGLAS_SSPD.md](#doc-d9da2f0b37a2)
- [desarrollo_puntos/3.3/XM/README.md](#doc-05a8db13b38d)
- [desarrollo_puntos/3.3/XM/REVISION_REGLAS_XM.md](#doc-5cd7ac79d74f)
- [desarrollo_puntos/3.4/Evaluacion_fuente_alternativa_XM.md](#doc-50ab77624282)
- [desarrollo_puntos/3.4/README.md](#doc-8c63814239f9)
- [desarrollo_puntos/3.5/README.md](#doc-6927d6df7ab3)
- [desarrollo_puntos/3.6/README.md](#doc-2c881ea64a55)
- [desarrollo_puntos/3.6/REPRODUCIBILIDAD_HITO3.md](#doc-cff2689f65ac)
- [desarrollo_puntos/3.7/bootstrap/README.md](#doc-30e3a1a159ec)
- [desarrollo_puntos/3.7/EPM/README_CUARENTENA.md](#doc-9d236b840cde)
- [desarrollo_puntos/3.7/README.md](#doc-fcfdcb7af446)
- [desarrollo_puntos/3_documentacion_general/CIERRE_HITO3.md](#doc-f1d8ec2447b1)
- [desarrollo_puntos/3_documentacion_general/CONTEXTO_PREVIO_HITO3.md](#doc-b2834637e78b)
- [desarrollo_puntos/3_documentacion_general/PENDIENTES_APROBACION_HITO3.md](#doc-349c3e6eb49a)
- [desarrollo_puntos/3_documentacion_general/plan_hitos_3-6_detallado.md](#doc-bfabfa5b4a96)
- [desarrollo_puntos/3_documentacion_general/README.md](#doc-393500a1bb5a)
- [desarrollo_puntos/3_documentacion_general/REVISION_HITOS_3_4.md](#doc-e95ee88a713e)
- [desarrollo_puntos/3_documentacion_general/VALIDACION_ROLES_UMBRALES.md](#doc-45878726ae90)
- [desarrollo_puntos/3_documentacion_general/VERIFICACION_ORGANIZACION.md](#doc-7d24dd3127fd)
- [desarrollo_puntos/4.1/CIERRE_VIÑETA_1.md](#doc-fd8cd320f92a)
- [desarrollo_puntos/4.1/NOTA_SSPD_361_356.md](#doc-712708a8fc91)
- [desarrollo_puntos/4.1/PENDIENTES_HITO_4_1_VIÑETAS_1_Y_2.md](#doc-e7f9f86a97c5)
- [desarrollo_puntos/4.1/README.md](#doc-81f243d988ee)
- [desarrollo_puntos/4.1/README_ISOLATION_FOREST.md](#doc-ec554867a4f3)
- [desarrollo_puntos/4.2/INFORME_SENSIBILIDAD.md](#doc-6e8fab534d7e)
- [desarrollo_puntos/4.2/README.md](#doc-15dec98a30e1)
- [desarrollo_puntos/4.3/INFORME_METRICAS.md](#doc-7712518cbe50)
- [desarrollo_puntos/4.3/README.md](#doc-a66acf433abb)
- [desarrollo_puntos/4.4/INFORME_REGLA_SISTEMICA.md](#doc-4ce62780cc42)
- [desarrollo_puntos/4.4/README.md](#doc-c26806ebe30e)
- [desarrollo_puntos/4.5/README.md](#doc-74d9a3dc3145)
- [desarrollo_puntos/4.6/INFORME_NIVELES_COSTO.md](#doc-9616b9e5ae82)
- [desarrollo_puntos/4.6/README.md](#doc-dd387e3f4a37)
- [fuentes_datos/datos/Datos_en_revision/CREG_prioridad/README.md](#doc-c1f90ad6d430)
- [fuentes_datos/datos/Datos_seleccionados/CHEC/README.md](#doc-e41c39d2c4be)
- [fuentes_datos/datos/Datos_seleccionados/EPM/README.md](#doc-4cb35e3c7465)
- [fuentes_datos/datos/Datos_seleccionados/README.md](#doc-9f3e7a240956)
- [fuentes_datos/datos/Datos_seleccionados/SSPD/README.md](#doc-daeaab5c0588)
- [fuentes_datos/datos/Datos_seleccionados/XM_piloto/README.md](#doc-ebb04b15ad96)
- [fuentes_datos/DECISION_FUENTES_PRINCIPALES.md](#doc-e81c2bcf3ffb)
- [fuentes_datos/FUENTES_PROBABLES_EN_REVISION.md](#doc-df3b3bd5e550)
- [fuentes_datos/JUSTIFICACION_SELECCION.md](#doc-49ce02ddaa81)
- [fuentes_datos/PROPUESTA_CUATRO_FUENTES.md](#doc-0f3a50ee68a6)
- [fuentes_datos/README.md](#doc-8b50327833d5)
- [fuentes_datos/REVISION_CREG_ELECTRICIDAD.md](#doc-1e1e212fc147)
- [fuentes_datos/verificaciones/SOLICITUD_VALIDACION_EPM.md](#doc-f87bbef16802)
- [fuentes_datos/verificaciones/trazabilidad_filas/README.md](#doc-351c00955bb1)
- [requirements/README.md](#doc-e050028ca414)

<a id="doc-a4bc47109979"></a>

## 0_Recomendaciones_profesor/resumen_DAMA-DMBOK_para_el_proyecto.md

### DAMA-DMBOK2 aplicado al proyecto: lo que el trabajo debe tomar del capítulo 13 (Data Quality)

Guía para el trabajo de grado *Framework automatizado para la evaluación de la calidad de datos en registros administrativos del sector energético en Colombia* (Grupo 03; dirección del trabajo). Referencia: DAMA International (2017), *DAMA-DMBOK2*, capítulo 13.

Actualización del 27 de octubre de 2026: el profesor exige medir las ocho dimensiones en EPM y CHEC. La especificación vigente está en [la matriz OE1](REFERENCIA_TECNICA.md#doc-cd000226e09e). Este resumen describe antecedentes del Hito 2; R11/R12 no acreditan exactitud y la oportunidad ya no se excluye.

#### 1. Definición y propósito

- **Calidad de datos** en DMBOK es *aptitud para el uso* (fitness for purpose): los datos son de calidad si sirven para lo que sus consumidores necesitan. No es una propiedad absoluta del archivo.
- **Gestión de calidad de datos** es la planeación, implementación y control de actividades que aplican técnicas de gestión de calidad a los datos para asegurar que sean aptos para su consumo.
- **Lo que falta en el proyecto:** nunca se dice quién consume las tarifas de EPM ni para qué (regulador, comercializador, usuario, investigador). Sin ese consumidor no se puede justificar qué dimensiones importan ni qué umbral es aceptable. Debe quedar escrito en la caracterización de cada fuente (OE2).

#### 2. Dimensiones de calidad

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

#### 3. Tipos de regla de negocio

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

#### 4. Cómo se define una métrica

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

#### 5. Ciclo de actividades

DMBOK2 organiza la gestión de calidad como ciclo Shewhart-Deming (planear, hacer, verificar, actuar) con estas actividades:

1. **Definir qué es dato de alta calidad** para los consumidores identificados.
2. **Definir la estrategia** de calidad.
3. **Identificar los datos críticos y las reglas de negocio.** No todo se controla igual: hay que decir qué columnas son críticas (los importes) y cuáles son de apoyo.
4. **Evaluación inicial** mediante perfilamiento (data profiling): es el Hito 1.
5. **Identificar y priorizar mejoras.**
6. **Definir metas** de mejora.
7. **Operar**: gestionar reglas, medir y monitorear, gestionar incidentes, documentar procedimientos y corregir defectos.

El framework del proyecto cubre las actividades 3, 4 y 7. El documento debe decirlo con estos nombres y señalar que la 1 y la 3 se resuelven en la caracterización de la fuente.

#### 6. Técnicas que DMBOK2 recomienda y que el proyecto ya usa sin citarlas

- **Perfilamiento de datos**: evaluación inicial de estructura, nulos, dominios y duplicados. Es el Hito 1.
- **Módulos de verificación y auditoría en código**: reglas ejecutables, reutilizables y con bitácora. Es lo que el artefacto debe ser.
- **Control estadístico de procesos**: DMBOK2 dedica una sección a cartas de control con límites superior e inferior para distinguir variación común de variación especial en los datos. Es la justificación de las cartas I-MR dentro del marco DAMA, y resuelve la objeción de que las cartas no estaban en el anteproyecto. Hay que citarlo.
- **Análisis de causa raíz**: la hipótesis del serial de Excel es un análisis de causa raíz y debe presentarse como tal.
- **Gestión de incidentes de calidad**: el archivo de hallazgos ya es una bitácora de incidentes. Falta estado (abierto, confirmado, descartado), responsable y fecha de resolución.
- **Tablero de calidad (scorecard)**: indicadores por dimensión con umbral y tendencia. Es el tablero del anteproyecto.

#### 7. Qué deben escribir los estudiantes

1. En el marco teórico: las ocho dimensiones con definición de DMBOK2, cuáles usa el proyecto y por qué, y la relación con ISO/IEC 25012.
2. En la metodología: los diez tipos de regla, el ciclo de actividades y las técnicas, con la sección de control estadístico de procesos como respaldo de las cartas.
3. Como entregable del OE1: una matriz con cada regla clasificada por dimensión y tipo, con su métrica en la plantilla de la sección 4.
4. En la caracterización de cada fuente: consumidores, uso, datos críticos y, para cada dimensión, el umbral de aceptación justificado.
5. En resultados: un scorecard por fuente y dimensión, además de las curvas de detección.


<a id="doc-94e9bf18d464"></a>

## 0_Recomendaciones_profesor/revision_hito2.md

### Revisión técnica del Hito 2

**Borrador preparado para revisión del director. No es el concepto oficial hasta que el director lo apruebe.**

Trabajo de grado: *Framework automatizado para la evaluación de la calidad de datos en registros administrativos del sector energético en Colombia*. Estudiantes: Grupo 03. Fecha de revisión: 23 de octubre de 2026.

Material revisado: anteproyecto (junio de 2026), retroalimentación de junio, presentaciones del Hito 1 y del Hito 2, y el código entregado hasta el Hito 2. El código se ejecutó de principio a fin en un entorno limpio con una descarga nueva del conjunto de EPM (sfcd-b3ey, datos.gov.co).

#### 1. Veredicto

El Hito 2 es un avance sólido y honesto. El código se ejecuta sin modificaciones y reproduce todas las cifras de las diapositivas: 445 filas con etiquetas no canónicas, 10 duplicados, 83 series, 77 limpias, 8.282 pruebas, 80 / 80 / 88 % de detección, 11,4 % de alertas en meses limpios y 51 de 83 series alertando en febrero de 2020. La evaluación con errores inyectados, el umbral de Isolation Forest por validación cruzada y el bootstrap por series responden a las observaciones mayores 3 y 4 de la retroalimentación de junio. El hallazgo de los seriales de fecha de Excel es real y está bien argumentado.

Los problemas están en tres frentes: una inconsistencia entre lo que la diapositiva 9 defiende y lo que el pipeline hace, un supuesto estadístico frágil en las cartas, y una sobreestimación del tamaño muestral efectivo.

#### 2. Observaciones mayores

1. **La cuarentena no se aplica a las cartas.** La diapositiva 9 sostiene que las reglas van antes que las cartas porque un error en la referencia deja la carta ciega. En el código, las seis series con valores en cuarentena solo se marcan como sucias: sus límites y sus alertas reales se calculan con el error dentro de la referencia. La figura B se construyó a mano, interpolando el valor, fuera del pipeline. La cuarentena por valor debe entrar en la función de límites, y la imputación, si se usa, debe declararse.

2. **Las cartas trabajan sobre cambios absolutos de tarifas indexadas.** Las tarifas crecen con la inflación; la varianza de los cambios crece con el nivel y los límites fijos de 2017 a 2019 quedan estrechos en 2021. Se ve en la figura B: los cambios de 2021 derivan hacia arriba y disparan alertas sin error. Usar diferencias logarítmicas o porcentuales corrige buena parte de las alertas tardías y hace comparables las series, también para los rasgos del Isolation Forest.

3. **No son 83 series independientes.** De las 83, 69 son 23 categorías del Nivel I por sus tres columnas de propiedad, y esas columnas son casi transformaciones lineales una de otra (razones medianas 0,964 y 0,928). El número efectivo está cerca de 30. Esto infla el bootstrap por serie y el conjunto de entrenamiento del Isolation Forest, y explica por qué las reglas detectan el 54 % de las desviaciones del 10 %: la regla de orden entre columnas las atrapa porque el margen entre ellas es menor que el 10 %. El bootstrap debe remuestrear por categoría y los resultados deben reportarse por nivel.

4. **El número de registro no es trazable entre descargas.** Una descarga nueva del portal trae las mismas 3.623 filas en otro orden. Los casos 2047, 3131, 3133 y 2348 de la diapositiva 7 aparecen en otra descarga como 1043, 1808, 1810 y 3092. La clave de trazabilidad debe ser de contenido (categoría, fecha, columna) o el identificador de fila de la API, y el hash SHA-256 debe acompañarse de la fecha de descarga.

5. **Faltan precisión y F1.** El anteproyecto los promete y la retroalimentación los pidió. Se reporta recall por tipo de error y tasa de alerta en meses limpios, que es lo correcto a tasa igualada, pero F1 debe aparecer al menos en la comparación global. Las "falsas alarmas" de los datos reales son alertas sin error conocido, no falsas alarmas confirmadas, y así deben llamarse.

6. **La pseudo-replicación debe declararse.** Veinte sorteos por serie y tipo caen en 13 meses distintos en promedio, y la columna equivocada tiene 760 pruebas frente a 1.540 de los otros tipos. Las 8.282 pruebas no son independientes. El bootstrap por series lo mitiga, pero el documento debe decirlo y reportar las pruebas por tipo.

7. **Febrero de 2020 no es una falsa alarma.** Las alertas se concentran en febrero y julio de 2020 y julio de 2021, meses de ajuste tarifario de inicio de semestre, probablemente la entrada de los cargos de distribución de la Resolución CREG 015 de 2018. Una carta de individuales está diseñada para detectar justamente eso. La regla de alerta sistémica que proponen (alertas compartidas por muchas series en el mismo mes) debe formalizarse dentro del framework.

#### 3. Pendientes del anteproyecto y forma

- **Hipótesis frente a diseño sigue sin resolverse.** El anteproyecto conserva H1 y H0 inferenciales junto con Design Science, y el Hito 2 no compara contra ningún método manual. Salida: definir las reglas estáticas como el procedimiento tradicional (lo que hacen MinTIC y Deequ) y el framework como reglas más cartas. Con el bootstrap existente (88 % frente a 73 %, intervalos que no se solapan) la hipótesis se vuelve contrastable.
- **El conjunto de datos del anteproyecto no es el que se usa.** El documento nombra Superservicios y la CREG; el trabajo se hace sobre tarifas de EPM. Población, muestra y sección 5.8 deben actualizarse y EPM debe justificarse.
- **Las cartas de control no están en el anteproyecto.** Ni en objetivos, ni en marco teórico, ni en la lista de técnicas (Z-score, KNN, Isolation Forest extendido, PCA, K-Means, DBSCAN). Deben incorporarse como método estadístico clásico, con respaldo en Jones-Farmer et al. (2014) y en la técnica de control estadístico de procesos del DAMA-DMBOK2, capítulo 13.
- **Todavía no es un framework.** Es un guion lineal que depende de la carga manual en Colab, redefine variables de la Parte 1 en la Parte 2 y no tiene archivo de dependencias. Docker, Poetry y el tablero de Power BI del anteproyecto no aparecen.
- **R12 es demasiado severa.** Marcar como error todo valor mayor a diez veces la mediana de su serie y ponerlo en cuarentena puede eliminar valores legítimos en series que cruzan cero, como Restricciones. Debe ser advertencia hasta confirmación.
- **Detalles.** El código de la diapositiva 11 no es el del archivo entregado. Los dos sinónimos de rango de consumo siguen sin confirmar con EPM. La detección en t o t+1 y el rasgo de "cambio siguiente" del Isolation Forest hacen el método retrospectivo, válido para auditar datos publicados pero debe decirse.

#### 4. Sobre el alcance

Un solo conjunto de 3.623 filas no descalifica una tesis de maestría si la pregunta es metodológica, y el protocolo de comparación con errores inyectados es un aporte defendible. Lo que hace corto el trabajo frente al anteproyecto aprobado es: una sola fuente, un tamaño efectivo pequeño, un solo modelo de aprendizaje automático, ausencia de análisis de sensibilidad, ausencia del artefacto prometido y ningún error confirmado con la entidad. El plan de hitos 3 a 6 (`plan_hitos_3-6_detallado.md`) organiza el cierre de esas brechas trazado a los cuatro objetivos específicos.

#### 5. Verificación de reproducción

| Cifra de la presentación | Valor reproducido |
|---|---|
| Filas y columnas | 3.623 × 12 |
| Variantes de etiqueta / filas afectadas | 11 / 445 |
| Duplicados exactos adicionales | 10 |
| Series posibles / con 49 meses o más / limpias | 202 / 83 / 77 |
| Pruebas inyectadas | 8.282 |
| Detección total: reglas / cartas / IF / reglas + cartas | 73 / 80 / 80 / 88 % |
| Alertas en meses limpios: cartas / IF (umbral CV) | 11,4 / 12,0 % |
| Series con alerta en febrero de 2020 | 51 de 83 |
| IC 95 % de la diferencia IF − cartas | −1,4 a +2,3 puntos |


<a id="doc-dfcefa4bff36"></a>

## desarrollo_puntos/3.1/EVIDENCIA_EXACTITUD_OPORTUNIDAD.md

### Evidencia de exactitud y oportunidad — preparación

Este documento deja preparado el procedimiento y separa la evidencia disponible de la evidencia
que todavía necesita aprobación o contraste externo. No convierte una referencia en una medición
de exactitud si aún no existe una comparación fila a fila.

#### Exactitud (EXA01)

##### Diseño aprobado como propuesta

- Muestra: 30 registros por fuente, estratificados por periodo y categoría.
- Campos: periodo, identificadores de categoría y componentes monetarios disponibles.
- Comparación: igualdad después de normalizar unidad y redondeo documentado.
- Resultado: coincidencias / comparaciones válidas × 100.
- Evidencia: URL, archivo de referencia, SHA-256 y fecha de consulta.

La muestra de 30 registros por fuente es exploratoria y no sustituye una auditoría estadística de
la población completa.

##### Evidencia actualmente disponible

CHEC tiene una referencia externa preparada en
`desarrollo_puntos/3.1/referencia_exa01_chec.json` (108 registros de Superservicios, consulta
descargada el 2026-10-28). El archivo permite seleccionar pares comparables, pero todavía no
contiene una tabla de coincidencias fila a fila; por eso EXA01 sigue provisional.

Para EPM, SSPD y XM no existe todavía una referencia equivalente aprobada. No se inventan
coincidencias ni porcentajes.

##### Plantilla

La captura debe diligenciarse en [plantilla_exactitud.csv](../Data/gold/outputs/calidad/plantilla_exactitud.csv). Cada fila debe
conservar el `snapshot_sha256` del dataset evaluado y el `sha256_referencia` del contraste.

#### Oportunidad (OPO01)

##### Fórmula propuesta

`retraso_días = fecha_disponible - fecha_límite`.

Si no existe fecha límite publicada, se registra la fecha de publicación observada y se clasifica
como `provisional_proxy`; no se declara cumplimiento.

##### Evidencia actualmente disponible

XM tiene fechas declaradas de publicación para 60 de 61 versiones mensuales del piloto. Falta
julio de 2021 y aún debe aprobarse el plazo esperado; por tanto, XM tiene evidencia parcial, no
cierre de oportunidad.

EPM, CHEC y SSPD conservan fecha de descarga y cobertura, pero no un plazo de publicación oficial
por periodo. Sus resultados de oportunidad deben permanecer como proxy o pendiente.

##### Plantilla

La captura debe diligenciarse en [plantilla_oportunidad.csv](../Data/gold/outputs/calidad/plantilla_oportunidad.csv), incluyendo
la URL o archivo que demuestra cada fecha. No usar la fecha de descarga como fecha de publicación.

#### Decisiones que debe aprobar el director

1. Aceptar la muestra exploratoria de 30 registros por fuente o cambiar su tamaño.
2. Aprobar la referencia de Superservicios para contrastar CHEC.
3. Definir tolerancia de redondeo y equivalencia de unidades.
4. Aprobar el proxy de oportunidad cuando no exista un plazo publicado.
5. Aceptar que los resultados sin contraste siguen como `provisional` o `provisional_proxy`.


<a id="doc-cd000226e09e"></a>

## desarrollo_puntos/3.1/matriz_oe1.md

### Matriz OE1: dimensiones, métricas, indicadores y reglas

Hito 3, actividad 1 · 27 de octubre de 2026 · EPM y CHEC.

**Estado:** especificación documental elaborada. No se presentan resultados de medición ni se declara cumplida la evaluación de las ocho dimensiones.

#### Alcance y uso

**Migración de fuente:** esta matriz reemplaza SSPD-NR por XM/SIMEM. Las cifras históricas de SSPD-NR no se transfieren a XM; XM se mide con un adaptador preliminar específico de demanda.

Se definen 19 indicadores: las doce reglas base y siete controles complementarios. El CSV contiene 76 filas, una por control y fuente (19 × 4). El YAML es la especificación completa; el script ejecuta los adaptadores de cada fuente.

Consumidores previstos: equipo de tesis para auditar tarifas, facturación y demanda eléctrica, y usuarios analíticos que necesitan comparar registros por categoría, versión y período. La finalidad es detectar problemas de representación y valores sospechosos con evidencia trazable; no certificar legalidad de tarifas ni exactitud económica por sí sola.

Se toma DAMA-DMBOK2 (2017), capítulo 13, como edición base. Las definiciones operativas, métricas y umbrales son del proyecto. El resumen oficial de cambios de DAMA confirma que una edición revisada incorpora una dimensión adicional; no se mezclan ediciones.

#### Ocho dimensiones y relación con ISO

La relación con ISO/IEC 25012 es conceptual y parcial; no se afirma que sus características sean las mismas ocho dimensiones ni que la matriz certifique cumplimiento de la norma. Oportunidad de publicación no equivale por sí sola a actualidad del dato. Credibilidad no se añade como novena dimensión obligatoria.

| Dimensión | Definición aplicada a tarifas | Indicadores | Relación ISO |
|---|---|---|---|
| Completitud | Presencia de campos y observaciones requeridos para interpretar cada tarifa. | R01, R10 | completeness; directa conceptual |
| Validez | Conformidad de períodos, categorías e importes con dominios documentados. | R02, R03, R07, R11 | Sin equivalencia nominal única; sin equivalencia nominal unica |
| Unicidad | Una sola representación por entidad tarifaria y período dentro del alcance definido. | R04, R05 | Sin equivalencia nominal única; sin equivalencia nominal unica |
| Consistencia | Coherencia de etiquetas y relaciones de tarifas al comparar categorías equivalentes. | R06, R08, R09, MAP01, DEF01 | consistency; directa conceptual |
| Integridad | Estructura completa y referencias de categorías resolubles en catálogos versionados. | INT01, INT02 | Sin equivalencia nominal única; relacion parcial con completeness y consistency |
| Razonabilidad | Comportamiento tarifario compatible con una referencia temporal y contexto documentados. | R12, CART01 | Sin equivalencia nominal única; sin equivalencia nominal unica |
| Exactitud | Concordancia de valores con una publicación oficial equivalente y verificada. | EXA01 | accuracy; directa conceptual con alcance muestral |
| Oportunidad | Disponibilidad de la publicación requerida dentro del plazo que necesita el consumidor. | OPO01 | currentness; parcial no equivalente a actualidad |

#### Diez tipos de regla

Los tipos son una clasificación, no diez reglas adicionales ni una exigencia de asignación uno a uno. Una regla puede tener más de un tipo; se declara un principal para evitar doble conteo. Los nombres en español son traducciones de trabajo.

| Tipo | Nombre | Controles clasificados |
|---|---|---|
| T01 | Conformidad definicional | DEF01 |
| T02 | Presencia y completitud | R01, R10 |
| T03 | Cumplimiento de formato | R03 |
| T04 | Pertenencia a dominio | R02, R06 |
| T05 | Conformidad de rango | R02, R07, R11, R12, CART01 |
| T06 | Conformidad de mapeo | MAP01 |
| T07 | Consistencia entre atributos | R08, R09, INT01, INT02 |
| T08 | Verificación de exactitud | EXA01 |
| T09 | Verificación de unicidad | R04, R05 |
| T10 | Validación de oportunidad | OPO01 |

#### Reglas comunes de medición

- Todo indicador se calcula como porcentaje de unidades definidas; nunca mezclar celdas, filas, referencias y publicaciones en un denominador. Las tasas R11, R12 y CART01 son prevalencias de sospechas/alertas, no porcentajes de errores confirmados.
- Reportar elegibles, evaluadas, exclusiones por causa, fallos y cobertura por fuente, control y período. Si falta evidencia, el resultado es parcial o pendiente, sin aprobar la dimensión.
- Denominador cero produce valor nulo y motivo; no se convierte en 100 %. Toda exclusión debe ser visible y justificada antes de observar resultados.
- Las metas de 100 % son propuestas de conformidad total para unidades aplicables, no umbrales del profesor, de DAMA, de ISO ni del publicador. Las tasas estadísticas no tienen un umbral de aceptación inventado; requieren calibración.
- Tendencia por mes de vigencia y versión de descarga. Para oportunidad se usa período de publicación esperado. No confundir un análisis retrospectivo por vigencia con seguimiento histórico de publicación.
- Los responsables son roles; falta asignar nombres. No se inventan integrantes ni aprobaciones del director.
- Se conserva el original; las tasas se distinguen antes/después de preparar datos. No eliminar los fallos antes de calcular la calidad de la fuente.
- La meta final exige medición de las ocho dimensiones en cada fuente con alcance explícito. Los estados pendientes no acreditan el cierre.

#### Fichas completas por indicador

##### R01 · Período informado

- **Dimensión / tipo:** completitud / T02 (Presencia y completitud).
- **Métrica y población:** Todas las filas del snapshot original. Unidad observada: fila.
- **Numerador:** Filas con ambos campos de período informados.
- **Denominador:** Número total de filas.
- **Indicador:** 100 × numerador / denominador; unidad: porcentaje.
- **Umbral:** ≥ 100 % propuesto. Meta de conformidad total para las unidades aplicables; es una propuesta del proyecto, no un umbral de DAMA, ISO o del publicador. Reportar tasa continua aunque no alcance la meta.
- **Severidad:** error; se refiere al hallazgo, sin confirmación automática de error real.
- **Frecuencia:** En cada ejecución y nueva versión de descarga; por mes de vigencia cuando corresponda.
- **Responsable:** responsable_reglas_negocio; nombre pendiente.
- **Tendencia:** Mayor es mejor Por fuente y período de vigencia; conservar también el snapshot y versión de control.
- **EPM:** year y mes no vacíos.
- **CHEC:** costounitariotarifa_ano y costounitariotarifa_mes no vacíos.
- **Precondiciones:** N/A no es un período válido; distinguir presencia de validez.
- **Estado:** EPM 99.97 % (3622/3623, medido); CHEC 100 % (40609/40609, medido); SSPD 100 % (91840/91840, medido); XM 100 % (61/61, medido).

##### R02 · Período válido

- **Dimensión / tipo:** validez / T04 (Pertenencia a dominio).
- **Métrica y población:** Filas con período presente por R01. Unidad observada: fila.
- **Numerador:** Filas cuyo año es entero y cuyo mes pertenece al dominio; fecha construible.
- **Denominador:** Filas con período presente.
- **Indicador:** 100 × numerador / denominador; unidad: porcentaje.
- **Umbral:** ≥ 100 % propuesto. Meta de conformidad total para las unidades aplicables; es una propuesta del proyecto, no un umbral de DAMA, ISO o del publicador. Reportar tasa continua aunque no alcance la meta.
- **Severidad:** error; se refiere al hallazgo, sin confirmación automática de error real.
- **Frecuencia:** En cada ejecución y nueva versión de descarga; por mes de vigencia cuando corresponda.
- **Responsable:** responsable_reglas_negocio; nombre pendiente.
- **Tendencia:** Mayor es mejor Por fuente y período de vigencia; conservar también el snapshot y versión de control.
- **EPM:** Mapear nombres de mes mediante catálogo explícito; validar year como entero sin truncar.
- **CHEC:** Validar año y mes enteros; mes de 1 a 12.
- **Precondiciones:** No rechazar nuevas fechas solo por exceder la cobertura de la descarga previa. Reportar excluidos por ausencia en R01.
- **Estado:** EPM 100 % (3622/3622, medido); CHEC 100 % (40609/40609, medido); SSPD 100 % (91840/91840, medido); XM 100 % (61/61, medido).

##### R03 · Importes numéricos y finitos

- **Dimensión / tipo:** validez / T03 (Cumplimiento de formato).
- **Métrica y población:** Celdas monetarias informadas en campos aplicables según concepto. Unidad observada: celda.
- **Numerador:** Celdas convertibles sin ambigüedad a número finito.
- **Denominador:** Celdas informadas y aplicables.
- **Indicador:** 100 × numerador / denominador; unidad: porcentaje.
- **Umbral:** ≥ 100 % propuesto. Meta de conformidad total para las unidades aplicables; es una propuesta del proyecto, no un umbral de DAMA, ISO o del publicador. Reportar tasa continua aunque no alcance la meta.
- **Severidad:** error; se refiere al hallazgo, sin confirmación automática de error real.
- **Frecuencia:** En cada ejecución y nueva versión de descarga; por mes de vigencia cuando corresponda.
- **Responsable:** responsable_reglas_negocio; nombre pendiente.
- **Tendencia:** Mayor es mejor Por fuente y período de vigencia; conservar también el snapshot y versión de control.
- **EPM:** Cinco columnas monetarias; preservar texto original y evitar conversión ambigua de separadores.
- **CHEC:** Diez medidas declaradas texto; convertir con convención explícita y conservar original.
- **Precondiciones:** Matriz de aplicabilidad por concepto; nulos se reportan en completitud. No aceptar NaN o infinito como importes válidos.
- **Estado:** EPM 100 % (18110/18110, provisional); CHEC 100 % (406035/406035, provisional); SSPD 100 % (1193920/1193920, medido); XM 100 % (61/61, medido).

##### R04 · Ausencia de duplicados exactos adicionales

- **Dimensión / tipo:** unicidad / T09 (Verificación de unicidad).
- **Métrica y población:** Todas las filas originales, sin campos técnicos generados. Unidad observada: fila.
- **Numerador:** Total de filas menos duplicados exactos adicionales.
- **Denominador:** Número total de filas.
- **Indicador:** 100 × numerador / denominador; unidad: porcentaje.
- **Umbral:** ≥ 100 % propuesto. Meta de conformidad total para las unidades aplicables; es una propuesta del proyecto, no un umbral de DAMA, ISO o del publicador. Reportar tasa continua aunque no alcance la meta.
- **Severidad:** error; se refiere al hallazgo, sin confirmación automática de error real.
- **Frecuencia:** En cada ejecución y nueva versión de descarga; por mes de vigencia cuando corresponda.
- **Responsable:** responsable_reglas_negocio; nombre pendiente.
- **Tendencia:** Mayor es mejor Por fuente y período de vigencia; conservar también el snapshot y versión de control.
- **EPM:** Comparar las 12 columnas originales.
- **CHEC:** Comparar las 24 columnas originales.
- **Precondiciones:** Una clase de n filas idénticas aporta n-1 duplicados; no usar esa cifra para R05.
- **Estado:** EPM 99.72 % (3613/3623, medido); CHEC 100 % (40609/40609, medido); SSPD 100 % (91840/91840, medido); XM 100 % (61/61, medido).

##### R05 · Clave tarifaria sin multiplicidad

- **Dimensión / tipo:** unicidad / T09 (Verificación de unicidad).
- **Métrica y población:** Filas con clave completa y período válido; tras identificar copias exactas y conservar una por clase. Unidad observada: fila.
- **Numerador:** Filas cuya clave candidata tiene una sola representación.
- **Denominador:** Filas con clave evaluable en esa etapa.
- **Indicador:** 100 × numerador / denominador; unidad: porcentaje.
- **Umbral:** ≥ 100 % propuesto. Meta de conformidad total para las unidades aplicables; es una propuesta del proyecto, no un umbral de DAMA, ISO o del publicador. Reportar tasa continua aunque no alcance la meta.
- **Severidad:** advertencia; se refiere al hallazgo, sin confirmación automática de error real.
- **Frecuencia:** En cada ejecución y nueva versión de descarga; por mes de vigencia cuando corresponda.
- **Responsable:** responsable_reglas_negocio; nombre pendiente.
- **Tendencia:** Mayor es mejor Por fuente y período de vigencia; conservar también el snapshot y versión de control.
- **EPM:** Cinco categorías normalizadas + fecha mensual.
- **CHEC:** Doce categorías originales como clave provisional + fecha; revisar dependencias código-nombre antes de fijar clave final.
- **Precondiciones:** Versionar la clave y las equivalencias. Todas las filas de una clave multiplicada incumplen; separar redundancia semántica y valores en conflicto.
- **Estado:** EPM 100 % (3612/3612, medido); CHEC 88.44 % (35914/40609, provisional); SSPD 91.63 % (84154/91840, provisional); XM 100 % (61/61, medido).

##### R06 · Representación canónica

- **Dimensión / tipo:** consistencia / T04 (Pertenencia a dominio).
- **Métrica y población:** Celdas categóricas informadas con catálogo canónico aprobado. Unidad observada: celda categórica.
- **Numerador:** Celdas cuyo valor original ya coincide con su forma canónica.
- **Denominador:** Celdas categóricas con catálogo aprobado.
- **Indicador:** 100 × numerador / denominador; unidad: porcentaje.
- **Umbral:** ≥ 100 % propuesto. Meta de conformidad total para las unidades aplicables; es una propuesta del proyecto, no un umbral de DAMA, ISO o del publicador. Reportar tasa continua aunque no alcance la meta.
- **Severidad:** advertencia; se refiere al hallazgo, sin confirmación automática de error real.
- **Frecuencia:** En cada ejecución y nueva versión de descarga; por mes de vigencia cuando corresponda.
- **Responsable:** responsable_reglas_negocio; nombre pendiente.
- **Tendencia:** Mayor es mejor Por fuente y período de vigencia; conservar también el snapshot y versión de control.
- **EPM:** Tipo de tarifa, tipo de dato y rango de consumo; conservar variantes originales.
- **CHEC:** Código/nombre, modalidad, clase, estrato y rangos según catálogo de cada campo.
- **Precondiciones:** Una variante no canónica es advertencia de estandarización, no necesariamente valor incorrecto. No convertir la moda observada en referencia oficial; medir cobertura de catálogo aparte.
- **Estado:** EPM 98.85 % (8626/8726, provisional); CHEC 100 % (340215/340215, provisional); SSPD 100 % (59527773/59527785, provisional); XM 100 % (244/244, provisional).

##### R07 · Signo y rango por concepto

- **Dimensión / tipo:** validez / T05 (Conformidad de rango).
- **Métrica y población:** Importes numéricos aplicables con dominio documentado. Unidad observada: celda.
- **Numerador:** Importes dentro del dominio específico del concepto.
- **Denominador:** Importes con dominio verificable.
- **Indicador:** 100 × numerador / denominador; unidad: porcentaje.
- **Umbral:** ≥ 100 % propuesto. Meta de conformidad total para las unidades aplicables; es una propuesta del proyecto, no un umbral de DAMA, ISO o del publicador. Reportar tasa continua aunque no alcance la meta.
- **Severidad:** error; se refiere al hallazgo, sin confirmación automática de error real.
- **Frecuencia:** En cada ejecución y nueva versión de descarga; por mes de vigencia cuando corresponda.
- **Responsable:** responsable_reglas_negocio; nombre pendiente.
- **Tendencia:** Mayor es mejor Por fuente y período de vigencia; conservar también el snapshot y versión de control.
- **EPM:** Revisar restricciones por separado; no aplicar no negatividad general a todos los conceptos.
- **CHEC:** Definir dominio de cada componente; subcon y cureal requieren definición antes de evaluar.
- **Precondiciones:** Excluir solo con causa explícita cuando falte el dominio; eso no aprueba el control.
- **Estado:** EPM 100 % (18110/18110, provisional); CHEC 98.99 % (401948/406035, provisional); SSPD 100 % (826560/826560, provisional); XM 100 % (61/61, provisional).

##### R08 · Orden entre tarifas por propiedad

- **Dimensión / tipo:** consistencia / T07 (Consistencia entre atributos).
- **Métrica y población:** Comparaciones completas de igual período, concepto y categoría salvo propiedad; nivel 1. Unidad observada: comparación de propiedad.
- **Numerador:** Comparaciones que respetan el orden documentado con tolerancia de redondeo.
- **Denominador:** Comparaciones completas con orden autorizado.
- **Indicador:** 100 × numerador / denominador; unidad: porcentaje.
- **Umbral:** ≥ 100 % propuesto. Meta de conformidad total para las unidades aplicables; es una propuesta del proyecto, no un umbral de DAMA, ISO o del publicador. Reportar tasa continua aunque no alcance la meta.
- **Severidad:** advertencia; se refiere al hallazgo, sin confirmación automática de error real.
- **Frecuencia:** En cada ejecución y nueva versión de descarga; por mes de vigencia cuando corresponda.
- **Responsable:** responsable_reglas_negocio; nombre pendiente.
- **Tendencia:** Mayor es mejor Por fuente y período de vigencia; conservar también el snapshot y versión de control.
- **EPM:** Propiedad EPM >= compartida >= cliente en la misma fila del nivel I; contrastar fundamento documental.
- **CHEC:** Alinear filas por las demás categorías y propiedad; confirmar las tres etiquetas y variable comparada antes de exigir el orden.
- **Precondiciones:** No comparar filas con estrato, modalidad o rango diferentes. Falta de un miembro de comparación se registra como falta de cobertura, no cumplimiento.
- **Estado:** EPM 99.91 % (2146/2148, provisional); CHEC 100 % (40598/40598, provisional); SSPD no aplica (no_aplica); XM 100 % (61/61, provisional).

##### R09 · Estructura de importes según categoría

- **Dimensión / tipo:** consistencia / T07 (Consistencia entre atributos).
- **Métrica y población:** Filas con nivel/modalidad identificados y matriz de aplicabilidad documentada. Unidad observada: fila.
- **Numerador:** Filas que cumplen todas las condiciones de aplicabilidad por nivel y modalidad.
- **Denominador:** Filas con matriz de aplicabilidad evaluable.
- **Indicador:** 100 × numerador / denominador; unidad: porcentaje.
- **Umbral:** ≥ 100 % propuesto. Meta de conformidad total para las unidades aplicables; es una propuesta del proyecto, no un umbral de DAMA, ISO o del publicador. Reportar tasa continua aunque no alcance la meta.
- **Severidad:** advertencia; se refiere al hallazgo, sin confirmación automática de error real.
- **Frecuencia:** En cada ejecución y nueva versión de descarga; por mes de vigencia cuando corresponda.
- **Responsable:** responsable_reglas_negocio; nombre pendiente.
- **Tendencia:** Mayor es mejor Por fuente y período de vigencia; conservar también el snapshot y versión de control.
- **EPM:** Revisar patrón del código: nivel I usa propiedad; otros niveles usan punta/fuera de punta. Validar si cero significa no aplica.
- **CHEC:** Comprobar combinaciones nivel-propiedad-modalidad-concepto; no exigir columnas punta/fuera de punta inexistentes.
- **Precondiciones:** En CHEC este es un adaptador semántico, no una copia literal del código EPM.
- **Estado:** EPM 100 % (3623/3623, provisional); CHEC 100 % (40609/40609, provisional); SSPD no aplica (no_aplica); XM 100 % (119928/119928, provisional).

##### R10 · Importes requeridos disponibles

- **Dimensión / tipo:** completitud / T02 (Presencia y completitud).
- **Métrica y población:** Filas para las que se conocen las medidas requeridas. Unidad observada: fila.
- **Numerador:** Filas con todos los importes obligatorios informados y sin marcador de ausencia documentado.
- **Denominador:** Filas con conjunto de medidas requeridas definido.
- **Indicador:** 100 × numerador / denominador; unidad: porcentaje.
- **Umbral:** ≥ 100 % propuesto. Meta de conformidad total para las unidades aplicables; es una propuesta del proyecto, no un umbral de DAMA, ISO o del publicador. Reportar tasa continua aunque no alcance la meta.
- **Severidad:** advertencia; se refiere al hallazgo, sin confirmación automática de error real.
- **Frecuencia:** En cada ejecución y nueva versión de descarga; por mes de vigencia cuando corresponda.
- **Responsable:** responsable_reglas_negocio; nombre pendiente.
- **Tendencia:** Mayor es mejor Por fuente y período de vigencia; conservar también el snapshot y versión de control.
- **EPM:** Evaluar columnas aplicables por nivel y concepto.
- **CHEC:** Evaluar tarifa/CU y componentes requeridos por el concepto; no exigir todo campo en toda fila.
- **Precondiciones:** Cambio propuesto frente al código: todos ceros no prueba incompletitud. Un cero informado cuenta como presente salvo documentación que lo defina como ausencia.
- **Estado:** EPM 99.94 % (3621/3623, provisional); CHEC 100 % (40609/40609, provisional); SSPD 100 % (91840/91840, provisional); XM 100 % (61/61, medido).
- **Cambio frente al código:** El Hito 2 alerta filas con todos los importes en cero. Conservar ese hallazgo como sospecha, pero no medirlo como ausencia confirmada.

##### R11 · Sospecha de serial de fecha en importe

- **Dimensión / tipo:** validez / T05 (Conformidad de rango).
- **Métrica y población:** Importes numéricos finitos en campos monetarios aplicables. Unidad observada: celda.
- **Numerador:** Importes enteros dentro del intervalo configurado de seriales Excel.
- **Denominador:** Importes numéricos finitos aplicables.
- **Indicador:** 100 × numerador / denominador; unidad: porcentaje.
- **Umbral:** Pendiente de calibración; informativo. No se prescribe tasa cero ni se equiparan alertas con errores. Calibrar en referencia y validación; congelar antes de vigilancia.
- **Severidad:** advertencia; se refiere al hallazgo, sin confirmación automática de error real.
- **Frecuencia:** En cada ejecución y nueva versión de descarga; por mes de vigencia cuando corresponda.
- **Responsable:** responsable_reglas_negocio; nombre pendiente.
- **Tendencia:** Interpretar según contexto; menor no significa necesariamente mejor calidad. Por fuente y período de vigencia; conservar también el snapshot y versión de control.
- **EPM:** Intervalo heredado [36526, 47483]; no confirma error.
- **CHEC:** Misma heurística solo tras revisar escala y unidad; los valores legítimos pueden caer en el intervalo.
- **Precondiciones:** No es indicador de exactitud confirmada ni criterio automático de cuarentena.
- **Estado:** EPM 0.0166 % (3/18110, medido); CHEC 0 % (0/406035, medido); SSPD 0.03828 % (457/1193920, medido); XM no aplica (no_aplica).
- **Cambio frente al código:** Reclasificación propuesta de Exactitud a Validez y severidad de sospecha; no se cambió el motor.
- **Parámetros:** {"serial_min": 36526, "serial_max": 47483}.

##### R12 · Prevalencia de magnitud atípica

- **Dimensión / tipo:** razonabilidad / T05 (Conformidad de rango).
- **Métrica y población:** Observaciones numéricas en series homogéneas con referencia válida. Unidad observada: serie-mes.
- **Numerador:** Observaciones con abs(valor) > factor * mediana(abs(referencia)).
- **Denominador:** Observaciones evaluables en vigilancia.
- **Indicador:** 100 × numerador / denominador; unidad: porcentaje.
- **Umbral:** Pendiente de calibración; informativo. No se prescribe tasa cero ni se equiparan alertas con errores. Calibrar en referencia y validación; congelar antes de vigilancia.
- **Severidad:** advertencia; se refiere al hallazgo, sin confirmación automática de error real.
- **Frecuencia:** En cada ejecución y nueva versión de descarga; por mes de vigencia cuando corresponda.
- **Responsable:** responsable_metricas_anomalias; nombre pendiente.
- **Tendencia:** Interpretar según contexto; menor no significa necesariamente mejor calidad. Por fuente y período de vigencia; conservar también el snapshot y versión de control.
- **EPM:** Serie = categorías + columna monetaria.
- **CHEC:** Serie = categorías + variable monetaria; no mezclar CU y tarifa.
- **Precondiciones:** Mediana de referencia estrictamente positiva; no estimarla con vigilancia. Factor 10 heredado, pendiente sensibilidad 5/10/20. No sustituye valoración de inflación, subsidio o cambio regulatorio.
- **Estado:** EPM 0.0426 % (4/9379, provisional); CHEC 0 % (0/355289, provisional); SSPD 0 % (0/90469, provisional); XM 0 % (0/12, provisional).
- **Cambio frente al código:** El código usa mediana de toda la serie y severidad Error; se propone referencia temporal y Advertencia.
- **Parámetros:** {"factor": 10, "sensibilidad": [5, 10, 20]}.

##### INT01 · Contrato estructural íntegro

- **Dimensión / tipo:** integridad / T07 (Consistencia entre atributos).
- **Métrica y población:** Columnas y contratos de tipo declarados por versión del esquema. Unidad observada: columna esperada.
- **Numerador:** Columnas presentes exactamente una vez con contrato de lectura compatible.
- **Denominador:** Columnas esperadas en el esquema versionado.
- **Indicador:** 100 × numerador / denominador; unidad: porcentaje.
- **Umbral:** ≥ 100 % propuesto. Meta de conformidad total para las unidades aplicables; es una propuesta del proyecto, no un umbral de DAMA, ISO o del publicador. Reportar tasa continua aunque no alcance la meta.
- **Severidad:** error; se refiere al hallazgo, sin confirmación automática de error real.
- **Frecuencia:** En cada ejecución y nueva versión de descarga; por mes de vigencia cuando corresponda.
- **Responsable:** responsable_datos; nombre pendiente.
- **Tendencia:** Mayor es mejor Por fuente y período de vigencia; conservar también el snapshot y versión de control.
- **EPM:** Doce columnas oficiales, con cinco medidas numéricas.
- **CHEC:** Veinticuatro columnas oficiales; texto monetario es compatible si existe conversión definida.
- **Precondiciones:** Columnas extra se reportan aparte como deriva de esquema, sin suponer pérdida. Este control no demuestra integridad referencial por sí solo.
- **Estado:** EPM 100 % (12/12, medido); CHEC 100 % (24/24, medido); SSPD 100 % (28/28, medido); XM 100 % (9/9, medido).

##### INT02 · Referencias categóricas resolubles

- **Dimensión / tipo:** integridad / T07 (Consistencia entre atributos).
- **Métrica y población:** Referencias aplicables de categorías/códigos contra catálogos versionados. Unidad observada: referencia por fila.
- **Numerador:** Referencias que resuelven a una entidad y combinación vigente permitida.
- **Denominador:** Referencias con catálogo verificable.
- **Indicador:** 100 × numerador / denominador; unidad: porcentaje.
- **Umbral:** ≥ 100 % propuesto. Meta de conformidad total para las unidades aplicables; es una propuesta del proyecto, no un umbral de DAMA, ISO o del publicador. Reportar tasa continua aunque no alcance la meta.
- **Severidad:** error; se refiere al hallazgo, sin confirmación automática de error real.
- **Frecuencia:** En cada ejecución y nueva versión de descarga; por mes de vigencia cuando corresponda.
- **Responsable:** responsable_datos; nombre pendiente.
- **Tendencia:** Mayor es mejor Por fuente y período de vigencia; conservar también el snapshot y versión de control.
- **EPM:** Relacionar combinación tarifaria con catálogo de modalidades, conceptos, nivel y rangos autorizado.
- **CHEC:** Comercializador, mercado y clase código-nombre; combinaciones permitidas de nivel/propiedad/estrato.
- **Precondiciones:** El catálogo debe tener referencia documental; no basta extraer todos los valores del mismo CSV. Una referencia sin clave es fallo si la clave es obligatoria; catálogo ausente es falta de evidencia.
- **Estado:** EPM no aplica (no_aplica); CHEC 96.15 % (25/26, provisional); SSPD no aplica (no_aplica); XM 100 % (3/3, provisional_interno).

##### EXA01 · Concordancia documental de importes

- **Dimensión / tipo:** exactitud / T08 (Verificación de exactitud).
- **Métrica y población:** Muestra predefinida de importes con categoría, unidad y mes comparables. Unidad observada: celda seleccionada para contraste.
- **Numerador:** Celdas contrastadas que coinciden con el valor de referencia bajo precisión documentada.
- **Denominador:** Celdas efectivamente contrastadas con referencia verificada.
- **Indicador:** 100 × numerador / denominador; unidad: porcentaje.
- **Umbral:** ≥ 100 % propuesto. Meta de conformidad total para las unidades aplicables; es una propuesta del proyecto, no un umbral de DAMA, ISO o del publicador. Reportar tasa continua aunque no alcance la meta.
- **Severidad:** error; se refiere al hallazgo, sin confirmación automática de error real.
- **Frecuencia:** En cada ejecución y nueva versión de descarga; por mes de vigencia cuando corresponda.
- **Responsable:** responsable_validacion; nombre pendiente.
- **Tendencia:** Mayor es mejor Por fuente y período de vigencia; conservar también el snapshot y versión de control.
- **EPM:** Publicación tarifaria original EPM con concepto, nivel, propiedad y franja equivalentes.
- **CHEC:** Publicación CHEC con mercado, estrato, nivel, propiedad, concepto y período equivalentes.
- **Precondiciones:** Seleccionar muestra antes de buscar concordancia; registrar semilla, estratos y universo. Separar muestra aleatoria de alertas seleccionadas por conveniencia. Usar Decimal y regla de redondeo documentada a precisión comparable; no elegir tolerancia después de observar diferencias. Publicación original es referencia de concordancia, no prueba independiente de tarifa económicamente correcta.
- **Estado:** EPM 100 % (18/18, provisional); CHEC 100 % (756/756, provisional); SSPD sin medir (no_medible); XM sin medir (no_medible).
- **Parámetros:** {"tamano_muestra_por_fuente": null, "semilla": 2026, "precision_comparacion": null, "regla_redondeo": null}.

##### OPO01 · Publicaciones disponibles dentro del plazo

- **Dimensión / tipo:** oportunidad / T10 (Validación de oportunidad).
- **Métrica y población:** Publicaciones esperadas por fuente y período dentro del alcance temporal fijado. Unidad observada: publicación fuente-período-versión.
- **Numerador:** Publicaciones con evidencia que acredita disponibilidad a más tardar en la fecha límite.
- **Denominador:** Publicaciones con fecha límite y disponibilidad evaluable mediante evidencia.
- **Indicador:** 100 × numerador / denominador; unidad: porcentaje.
- **Umbral:** ≥ 100 % propuesto. Meta de conformidad total para las unidades aplicables; es una propuesta del proyecto, no un umbral de DAMA, ISO o del publicador. Reportar tasa continua aunque no alcance la meta.
- **Severidad:** advertencia; se refiere al hallazgo, sin confirmación automática de error real.
- **Frecuencia:** En cada ejecución y nueva versión de descarga; por mes de vigencia cuando corresponda.
- **Responsable:** responsable_datos; nombre pendiente.
- **Tendencia:** Mayor es mejor Por fuente y período de vigencia; conservar también el snapshot y versión de control.
- **EPM:** Reconstruir evidencia temporal de publicaciones EPM, sin usar year/mes como fecha de publicación.
- **CHEC:** Reconstruir evidencia de publicaciones CHEC; fecha de carga del dataset no prueba cada período.
- **Precondiciones:** Definir primero consumidor, obligación o plazo operativo y zona horaria. Primera observación en un rastreo solo acota disponibilidad: clasificar como indeterminado si el intervalo cruza el plazo. Ausencia de evidencia no demuestra ni puntualidad ni retraso. Un seguimiento prospectivo se declara aparte; no valida el histórico retrospectivamente.
- **Estado:** EPM 100 % (61/61, provisional_proxy); CHEC 100 % (225/225, provisional_proxy); SSPD 90.77 % (59/65, provisional_proxy); XM 98.36 % (60/61, provisional_proxy).
- **Parámetros:** {"plazo_documentado": null, "zona_horaria": "America/Bogota", "periodo_inicio": null, "periodo_fin": null}.

##### MAP01 · Equivalencias de etiquetas verificadas

- **Dimensión / tipo:** consistencia / T06 (Conformidad de mapeo).
- **Métrica y población:** Equivalencias aplicadas por el adaptador en las filas del snapshot. Unidad observada: mapeo utilizado.
- **Numerador:** Mapeos con significado equivalente y fundamento registrado.
- **Denominador:** Mapeos distintos aplicados.
- **Indicador:** 100 × numerador / denominador; unidad: porcentaje.
- **Umbral:** ≥ 100 % propuesto. Meta de conformidad total para las unidades aplicables; es una propuesta del proyecto, no un umbral de DAMA, ISO o del publicador. Reportar tasa continua aunque no alcance la meta.
- **Severidad:** error; se refiere al hallazgo, sin confirmación automática de error real.
- **Frecuencia:** En cada ejecución y nueva versión de descarga; por mes de vigencia cuando corresponda.
- **Responsable:** responsable_datos; nombre pendiente.
- **Tendencia:** Mayor es mejor Por fuente y período de vigencia; conservar también el snapshot y versión de control.
- **EPM:** Validar por escrito equivalencias como variantes de 0-CS; no asumirlas solo por similitud.
- **CHEC:** Validar etiquetas de propiedad, clase y mercado; no fusionar códigos distintos por nombre parecido.
- **Precondiciones:** Sin equivalencias usadas, denominador cero se reporta sin unidades, no como 100 %. R06 mide representación original; MAP01 verifica que normalizar no cambie significado.
- **Estado:** EPM 100 % (2/2, provisional_interno); CHEC 100 % (3/3, provisional_interno); SSPD 100 % (3/3, provisional_interno); XM 100 % (3/3, provisional_interno).

##### DEF01 · Semántica de variables críticas documentada

- **Dimensión / tipo:** consistencia / T01 (Conformidad definicional).
- **Métrica y población:** Variables críticas incluidas en las reglas o en las series de cada fuente. Unidad observada: variable crítica.
- **Numerador:** Variables con significado, unidad y uso aprobados mediante evidencia de la fuente.
- **Denominador:** Variables críticas planificadas.
- **Indicador:** 100 × numerador / denominador; unidad: porcentaje.
- **Umbral:** ≥ 100 % propuesto. Meta de conformidad total para las unidades aplicables; es una propuesta del proyecto, no un umbral de DAMA, ISO o del publicador. Reportar tasa continua aunque no alcance la meta.
- **Severidad:** advertencia; se refiere al hallazgo, sin confirmación automática de error real.
- **Frecuencia:** En cada ejecución y nueva versión de descarga; por mes de vigencia cuando corresponda.
- **Responsable:** responsable_datos; nombre pendiente.
- **Tendencia:** Mayor es mejor Por fuente y período de vigencia; conservar también el snapshot y versión de control.
- **EPM:** Tipo de dato y cinco importes; distinguir COP/kWh y otros cargos según concepto.
- **CHEC:** CU, tarifa, componentes; confirmar tipomed, cureal y subcon si intervienen en controles.
- **Precondiciones:** Indicador de preparación semántica del contrato; no es exactitud de los valores. No excluir del denominador una variable solo porque su significado aún no se conoce.
- **Estado:** EPM 100 % (12/12, provisional_interno); CHEC 100 % (24/24, provisional_interno); SSPD 100 % (19/19, provisional_interno); XM 100 % (10/10, provisional_interno).

##### CART01 · Tasa de alertas de cartas I-MR

- **Dimensión / tipo:** razonabilidad / T05 (Conformidad de rango).
- **Métrica y población:** Cambios logarítmicos válidos y vigilados tras referencia independiente. Unidad observada: serie-mes vigilado.
- **Numerador:** Meses vigilados que activan I o MR (unión, sin doble conteo).
- **Denominador:** Meses efectivamente vigilados.
- **Indicador:** 100 × numerador / denominador; unidad: porcentaje.
- **Umbral:** Pendiente de calibración; informativo. No se prescribe tasa cero ni se equiparan alertas con errores. Calibrar en referencia y validación; congelar antes de vigilancia.
- **Severidad:** advertencia; se refiere al hallazgo, sin confirmación automática de error real.
- **Frecuencia:** En cada ejecución y nueva versión de descarga; por mes de vigencia cuando corresponda.
- **Responsable:** responsable_metricas_anomalias; nombre pendiente.
- **Tendencia:** Interpretar según contexto; menor no significa necesariamente mejor calidad. Por fuente y período de vigencia; conservar también el snapshot y versión de control.
- **EPM:** Categorías EPM y variable monetaria; agrupar dependencia por categoría en evaluación.
- **CHEC:** Categorías CHEC y CU/tarifa por separado; no sumar como réplicas independientes.
- **Precondiciones:** Solo valores positivos, únicos y meses consecutivos; no interpolar para ocultar huecos. Referencia base propuesta de 36 cambios y al menos 12 de vigilancia (49 observaciones). Excluir cambios que tocan valores en cuarentena; MR exige cambios válidos adyacentes. Contrastar alertas sistémicas con contexto; no clasificarlas automáticamente como error ni como cambio regulatorio confirmado.
- **Estado:** EPM 93.33 % (672/720, provisional); CHEC 98.88 % (3275/3312, provisional); SSPD 96.7 % (4189/4332, provisional); XM 0 % (0/12, provisional).
- **Parámetros:** {"cambios_referencia_base": 36, "min_cambios_vigilancia": 12, "sensibilidad_referencia": [24, 36, 48], "constante_I": 2.66, "constante_MR": 3.267}.

<!-- INICIO LINEA BASE -->
#### Línea base medida

Valores calculados por [`medir_matriz_oe1.py`](../Code/Data_Acquisition_and_Understanding/calidad/medir_matriz_oe1.py) sobre los CSV de
`fuentes_datos/datos/`, aplicando las definiciones de población, numerador y denominador
de esta misma matriz. Última ejecución: 2026-11-09T18:43:52Z.

| Archivo medido | Filas | SHA-256 |
|---|---|---|
| `fuentes_datos/datos/Datos_seleccionados/EPM/epm_sfcd-b3ey.csv` | 3623 | `b974a37a171b9178476fbd2baba21470e8845076af105ef9c178e80690f09920` |
| `fuentes_datos/datos/Datos_seleccionados/CHEC/chec_c698-wqig.csv` | 40609 | `1f34f85ada431220a39b2bacf10a1dd09bd440b3e7eab61b61d53094508af08c` |
| `fuentes_datos/datos/Datos_seleccionados/SSPD/sspd_ebby-cjha_detalle-compressed.zip` | 91840 | `ac2231358b78eeadb7a2bd99b5311e8a34467130d34d246efb19cb05bbcd3257` |
| `fuentes_datos/datos/Datos_seleccionados/XM_piloto/xm_demanda_mensual_piloto.csv` | 61 | `fe51fd1cdcbd229ef66b44e81d5312d0f3537ce237873bf52d4a25397f48e975` |

> Estos hashes no coinciden con `fuentes_datos/verificaciones/manifiesto_archivos.json`.
> La causa está identificada y no es corrupción: el repositorio no declara política de fin
> de línea y `core.autocrlf` convierte LF a CRLF al extraer en Windows, lo que añade un byte
> por línea. Convirtiendo el archivo de EPM a LF se obtiene exactamente el hash del manifiesto.
> Un hash de archivo de texto solo es verificable si la política de fin de línea está declarada.

##### Resultado por control

| Control | EPM | CHEC | SSPD | XM | Estado EPM / CHEC / SSPD / XM |
|---|---|---|---|---|---|
| R01 | 99.97 %<br><sub>3622/3623</sub> | 100 %<br><sub>40609/40609</sub> | 100 %<br><sub>91840/91840</sub> | 100 %<br><sub>61/61</sub> | medido / medido / medido / medido |
| R02 | 100 %<br><sub>3622/3622</sub> | 100 %<br><sub>40609/40609</sub> | 100 %<br><sub>91840/91840</sub> | 100 %<br><sub>61/61</sub> | medido / medido / medido / medido |
| R03 | 100 %<br><sub>18110/18110</sub> | 100 %<br><sub>406035/406035</sub> | 100 %<br><sub>1193920/1193920</sub> | 100 %<br><sub>61/61</sub> | provisional / provisional / medido / medido |
| R04 | 99.72 %<br><sub>3613/3623</sub> | 100 %<br><sub>40609/40609</sub> | 100 %<br><sub>91840/91840</sub> | 100 %<br><sub>61/61</sub> | medido / medido / medido / medido |
| R05 | 100 %<br><sub>3612/3612</sub> | 88.44 %<br><sub>35914/40609</sub> | 91.63 %<br><sub>84154/91840</sub> | 100 %<br><sub>61/61</sub> | medido / provisional / provisional / medido |
| R06 | 98.85 %<br><sub>8626/8726</sub> | 100 %<br><sub>340215/340215</sub> | 100 %<br><sub>59527773/59527785</sub> | 100 %<br><sub>244/244</sub> | provisional / provisional / provisional / provisional |
| R07 | 100 %<br><sub>18110/18110</sub> | 98.99 %<br><sub>401948/406035</sub> | 100 %<br><sub>826560/826560</sub> | 100 %<br><sub>61/61</sub> | provisional / provisional / provisional / provisional |
| R08 | 99.91 %<br><sub>2146/2148</sub> | 100 %<br><sub>40598/40598</sub> | n/a | 100 %<br><sub>61/61</sub> | provisional / provisional / no_aplica / provisional |
| R09 | 100 %<br><sub>3623/3623</sub> | 100 %<br><sub>40609/40609</sub> | n/a | 100 %<br><sub>119928/119928</sub> | provisional / provisional / no_aplica / provisional |
| R10 | 99.94 %<br><sub>3621/3623</sub> | 100 %<br><sub>40609/40609</sub> | 100 %<br><sub>91840/91840</sub> | 100 %<br><sub>61/61</sub> | provisional / provisional / provisional / medido |
| R11 | 0.0166 %<br><sub>3/18110</sub> | 0 %<br><sub>0/406035</sub> | 0.03828 %<br><sub>457/1193920</sub> | n/a | medido / medido / medido / no_aplica |
| R12 | 0.0426 %<br><sub>4/9379</sub> | 0 %<br><sub>0/355289</sub> | 0 %<br><sub>0/90469</sub> | 0 %<br><sub>0/12</sub> | provisional / provisional / provisional / provisional |
| INT01 | 100 %<br><sub>12/12</sub> | 100 %<br><sub>24/24</sub> | 100 %<br><sub>28/28</sub> | 100 %<br><sub>9/9</sub> | medido / medido / medido / medido |
| INT02 | n/a | 96.15 %<br><sub>25/26</sub> | n/a | 100 %<br><sub>3/3</sub> | no_aplica / provisional / no_aplica / provisional_interno |
| EXA01 | 100 %<br><sub>18/18</sub> | 100 %<br><sub>756/756</sub> | — | — | provisional / provisional / no_medible / no_medible |
| OPO01 | 100 %<br><sub>61/61</sub> | 100 %<br><sub>225/225</sub> | 90.77 %<br><sub>59/65</sub> | 98.36 %<br><sub>60/61</sub> | provisional_proxy / provisional_proxy / provisional_proxy / provisional_proxy |
| MAP01 | 100 %<br><sub>2/2</sub> | 100 %<br><sub>3/3</sub> | 100 %<br><sub>3/3</sub> | 100 %<br><sub>3/3</sub> | provisional_interno / provisional_interno / provisional_interno / provisional_interno |
| DEF01 | 100 %<br><sub>12/12</sub> | 100 %<br><sub>24/24</sub> | 100 %<br><sub>19/19</sub> | 100 %<br><sub>10/10</sub> | provisional_interno / provisional_interno / provisional_interno / provisional_interno |
| CART01 | 93.33 %<br><sub>672/720</sub> | 98.88 %<br><sub>3275/3312</sub> | 96.7 %<br><sub>4189/4332</sub> | 0 %<br><sub>0/12</sub> | provisional / provisional / provisional / provisional |

`n/a` significa que el control no aplica a esa fuente porque el concepto no existe en su
esquema. Es distinto de `—`, que es falta de evidencia.

##### Observación de apoyo: continuidad de cobertura

| Fuente | Períodos presentes | Esperados en la ventana | Ventana |
|---|---|---|---|
| EPM | 61 | 61 | 2016-12 a 2021-12 |
| CHEC | 225 | 225 | 2008-01 a 2026-09 |
| SSPD | 59 | 59 | 2017-07 a 2022-05 |
| XM | 61 | 61 | 2020-01 a 2025-01 |

**No acredita OPO01 y no debe presentarse como tal.** OPO01 exige evidencia de que cada
publicación estuvo disponible dentro de un plazo documentado, y su propia especificación
prohíbe usar `year`/`mes` como fecha de publicación. La continuidad solo muestra que no
faltan períodos dentro de la ventana, que es una propiedad distinta.

##### Lo que cambia al aplicar las definiciones de esta matriz

**R05 en EPM da 100 %.** La población exige conservar una fila por clase de copia exacta
antes de evaluar la clave. Con ese paso no queda ninguna clave repetida: las repeticiones
de clave en EPM son las mismas filas que ya detecta R04. Medir R05 sin deduplicar primero
reporta como defecto de unicidad lo que ya se contó una vez.

**R07 en EPM da 100 %.** Los 15 importes negativos
están todos en el concepto con excepción documentada: 15 en Restricciones: Rm. Ningún otro concepto presenta
negativos, de modo que la excepción describe el dato en lugar de relajarlo.

**R03 en EPM da 100 %.** El denominador de esta matriz son las celdas *informadas*. Las
celdas vacías no entran y se reportan en completitud; contarlas como fallo de formato
mezcla dos dimensiones.

##### Hallazgos que surgen de medir

**R10 con unidad de observación «fila» no detecta columnas vacías.** El control da
99.94 % en EPM y 100 % en CHEC porque toda fila
tiene al menos un importe informado. El detalle por columna en CHEC muestra otra realidad:

| Columna | Ceros | % de filas | Negativos | Vacías |
|---|---|---|---|---|
| `cureal` | 33871 | 83.4 % | 0 | 0 |
| `subcon` | 16854 | 41.5 % | 3360 | 11 |
| `generacion` | 11 | 0.0 % | 0 | 0 |
| `restricciones` | 0 | 0.0 % | 727 | 11 |
| `distribucion` | 0 | 0.0 % | 0 | 11 |
| `comercializacion` | 0 | 0.0 % | 0 | 11 |
| `perdidas` | 0 | 0.0 % | 0 | 11 |

Se propone cambiar la unidad de observación de R10 de fila a celda por columna. Es un cambio
en la especificación, no en el código, y sin él un scorecard declararía a CHEC completo.

**`cureal` y `subcon` necesitan DEF01 antes de que R07 y R10 signifiquen algo.** Un 83 % de
ceros en una columna y un 41 % en otra no se interpretan sin saber qué representan. La matriz
ya lo advierte; la medición lo cuantifica.

**INT02 encuentra su primer caso en CHEC.**

- `claseservicio_codigo = 'RS'` resuelve a 7 descripciones: Residencial Estrato 4 (4560) · Residencial Estrato 5 (2955) · Residencial Estrato 6 (2907) · Residencial (1800) · Residencial Estrato 2 (1092) · Residencial Estrato 3 (1073) · Residencial Estrato 1 (956)

El estrato ya viaja en `claseservicio_estrato` y la descripción lo duplica en la mayoría de
las filas pero no en todas. Es denormalización inconsistente, que es el defecto que INT02
existe para detectar.

**R06 no detecta sinónimos.** Sin catálogo canónico aprobado, la medición toma como forma
canónica la variante más frecuente tras normalizar mayúsculas y espacios. Con ese criterio
CHEC da 100 %: no hay variantes de capitalización. No significa que esté limpio en
consistencia, sino que este criterio solo ve diferencias de forma. Los sinónimos son
competencia de MAP01, que sigue sin evidencia.

##### Qué sigue sin poder medirse

| Control | Qué falta |
|---|---|
| EXA01 | La publicación tarifaria original de cada entidad. Las alertas de R11, R12 y las cartas solo generan sospechas. |
| OPO01 | Evidencia de la fecha real de disponibilidad por período y un plazo esperado documentado. |
| MAP01 | Validación escrita de que dos etiquetas significan lo mismo. |
| DEF01 | Significado, unidad y uso aprobados por la fuente. |
| CART01 | Las cartas en cambios logarítmicos de la actividad 5 del Hito 3. |
| R08 y R09 en CHEC | Matriz de combinaciones nivel-propiedad-modalidad-concepto y confirmación de las etiquetas de propiedad. |

Cinco de los diecinueve controles dependen de evidencia externa a los conjuntos. Esa es la
brecha real del punto 1, y no se cierra midiendo mejor.
<!-- FIN LINEA BASE -->

#### Evidencia externa y cierre

Exactitud y oportunidad requieren datos que no están en los CSV de tarifas. Se incluyen plantillas vacías; no se inventan fechas, documentos ni resultados. Para integridad se necesita también un catálogo autorizado y versionado.

- `plantilla_exactitud.csv`: universo/muestra preseleccionada, clave, celda, referencia, precisión y verificación. Una muestra de alertas no estima por sí sola exactitud poblacional.
- `plantilla_oportunidad.csv`: calendario esperado, límites de observación de disponibilidad y evidencia; separar períodos sin evidencia de retrasos confirmados.
- `plantilla_catalogos.csv`: valores, relaciones y equivalencias con fuente y vigencia. Un catálogo extraído del mismo CSV no valida su corrección.

El punto 1 entrega la matriz y las fichas; su validación metodológica sigue pendiente de revisión del equipo/director, cierre de catálogos y calibración. La implementación y los scorecards empíricos corresponden a las siguientes actividades. No se marca completo el Hito 3.

#### Referencias

- DAMA International (2017). *DAMA-DMBOK2*, cap. 13, tabla de dimensiones (pp. 461–462) y tipos de regla, sección 1.3.7 (pp. 467–468). [PDF del editor](https://technicspub.com/wp-content/uploads/2023/07/DAMA-DMBOK2.pdf). Se consultó para contrastar las categorías; las fichas son formulaciones propias del proyecto.
- [DAMA: cambios en la edición revisada](https://www.damadmbok.org/dmbok2-revisions). Consulta: 27 de octubre de 2026.
- [ISO/IEC 25012:2008, ficha oficial](https://www.iso.org/standard/35736.html) y [vista previa](https://www.iso.org/obp/ui/?_escaped_fragment_=iso:std:iso-iec:25012:ed-1:v1:en). Relación conceptual; no se reproducen requisitos no consultados de la norma.
- Anteproyecto y retroalimentación del 21 de junio de 2026 (`documentos/`); exigencia adicional de ocho dimensiones comunicada por el usuario.
- `codigo/codigo_hasta_hito2.py`, Parte 2. No se modificó el motor ni se ejecutaron nuevas métricas de calidad.


<a id="doc-ec2f495b53a8"></a>

## desarrollo_puntos/3.1/README.md

### 3.1 · Matriz dimensión → métrica → indicador → regla (OE1)

Corresponde a la actividad 1 del Hito 3. Aquí se reúnen las definiciones de los
indicadores, sus resultados y las evidencias que sustentan cada medición.

| Archivo o grupo | Función |
|---|---|
| [matriz_oe1.md](REFERENCIA_TECNICA.md#doc-cd000226e09e) | Definiciones, ocho dimensiones, diez tipos de regla y fichas de indicadores. |
| [matriz_oe1.csv](../Data/gold/outputs/calidad/matriz_oe1.csv) | Matriz principal: 76 registros, 19 controles por cada una de cuatro fuentes. |
| [matriz_oe1.yaml](../Data/gold/outputs/calidad/matriz_oe1.yaml) | Especificación documental y resultados por control y fuente. |
| [medir_matriz_oe1.py](../Code/Data_Acquisition_and_Understanding/calidad/medir_matriz_oe1.py) | Calcula la matriz; utiliza los adaptadores de [3.3](REFERENCIA_TECNICA.md#doc-1daec17adf88) y las cartas de [3.5](REFERENCIA_TECNICA.md#doc-6927d6df7ab3). |
| [EVIDENCIA_EXACTITUD_OPORTUNIDAD.md](REFERENCIA_TECNICA.md#doc-dfcefa4bff36) | Procedimiento y limitaciones de EXA01 y OPO01. |
| [referencia_exa01_chec.json](../Data/gold/outputs/calidad/referencia_exa01_chec.json) | Referencia externa conservada para el contraste de exactitud CHEC. |
| [plantilla_exactitud.csv](../Data/gold/outputs/calidad/plantilla_exactitud.csv), [plantilla_oportunidad.csv](../Data/gold/outputs/calidad/plantilla_oportunidad.csv), [plantilla_catalogos.csv](../Data/gold/outputs/calidad/plantilla_catalogos.csv) | Plantillas sin diligenciar para evidencia y validación de indicadores. |
| `matriz_dimensiones_dataset_*.py`, `indicadores_calidad_*_por_columna.csv`, `incidencias_calidad_*.csv`, `resumen_calidad_*.json` | Evaluación auxiliar por columna de EPM y CHEC; se conserva junto a los scripts que la generan. |

La evaluación auxiliar por columna y la matriz principal tienen definiciones y unidades
distintas. No deben mezclarse sus resultados ni asumirse como dos versiones equivalentes.
Por ejemplo, los indicadores auxiliares emplean proxies y tratan marcadores de ausencia
según su propia lógica; la matriz declara la aplicabilidad y el estado por control.

Desde la raíz del proyecto:

```powershell
python desarrollo_puntos/3.1/medir_matriz_oe1.py
```

La reorganización conserva los resultados existentes. No aprueba umbrales, cambia
fórmulas ni resuelve las diferencias metodológicas del plan; los pendientes siguen en
[el documento general](REFERENCIA_TECNICA.md#doc-349c3e6eb49a).


<a id="doc-cd7e104c7bc9"></a>

## desarrollo_puntos/3.2/CHEC/DECISION_CATALOGOS_CHEC.md

### Análisis técnico de catálogos CHEC

#### Perfil observado

Archivo analizado: `fuentes_datos/datos/Datos_seleccionados/CHEC/chec_c698-wqig.csv`.

- 40.609 filas y 24 columnas.
- 19 años y 12 meses; periodo observado 2008–2026.
- No hay nulos en las columnas de periodo ni en los identificadores categóricos principales.
- Hay 11 nulos en cada uno de estos componentes: distribución, comercialización, pérdidas,
  restricciones y subcon.
- `costounitariotarifa_restricciones` contiene valores negativos; no deben eliminarse sin confirmar
  su significado económico.

#### Catálogos observados

| Campo | Valores distintos | Interpretación operativa provisional |
|---|---:|---|
| comercializador_codigo | 1 | Código del comercializador; conservar como texto. |
| mercado_codigo | 2 | Código de mercado; debe corresponder con `mercado_nombre`. |
| costounitariotarifa_tipomed | 3 | Código de modalidad de medición; significado formal pendiente. |
| nivel_tension_codigo | 4 | Nivel de tensión; es categoría, no voltaje medido. |
| modalidadcobro_propiedad | 4 | Etiquetas de modalidad/propiedad; requiere catálogo CHEC. |
| claseservicio_codigo | 23 | Código de clase de servicio. |
| claseservicio_descri | 29 | Descripción; hay más descripciones que códigos, por lo que debe revisarse la correspondencia. |
| claseservicio_estrato | 7 | Estrato o categoría no aplicable en algunos servicios. |
| costounitariotarifa_rangoconsumo | 2 | Tramo tarifario; no es consumo observado en kWh. |
| costounitariotarifa_tipomercado | 1 | Código de tipo de mercado; significado pendiente. |

#### Clave candidata

La combinación provisional de periodo y categorías principales produce 37.252 claves distintas
para 40.609 filas: quedan 3.357 filas repetidas y la multiplicidad máxima es cuatro. Por tanto,
no se puede declarar unicidad todavía.

La clave debe confirmarse con CHEC o mediante el metadato oficial. Mientras tanto, se conserva la
clave candidata del diccionario y se reporta R05 como provisional. Las filas repetidas pueden ser
versiones de componentes o registros semánticamente distintos; no se deben eliminar por posición.

#### Decisiones que requieren aprobación

1. Definir formalmente los códigos de `tipomed`, `tipomercado` y `rangoconsumo`.
2. Confirmar la relación código-descripción de clase de servicio.
3. Confirmar si los valores negativos de restricciones y subcon son válidos por concepto.
4. Confirmar la unidad monetaria y la relación entre CU, CU real, subcon y valor de tarifa.
5. Confirmar la clave completa y el tratamiento de multiplicidades.
6. Definir quién mantiene el catálogo y cómo se versiona.

Este documento es evidencia técnica preparatoria; no convierte las interpretaciones provisionales en
catálogos oficiales.


<a id="doc-1b5778bfd6a3"></a>

## desarrollo_puntos/3.2/CHEC/Ficha_caracterizacion_01_chec_c698-wqig.md

### Ficha de caracterización: chec_c698-wqig

#### Identificación

| Atributo | Descripción |
|---|---|
| Archivo | `chec_c698-wqig.csv` |
| Ubicación | `fuentes_datos/datos/Datos_seleccionados/` |
| Tema | Costos unitarios y tarifas de energía eléctrica reportados para mercados atendidos por CHEC |
| Formato | CSV delimitado por comas, encabezados en la primera fila y campos entre comillas |
| Tamaño | 9.626.732 bytes (aprox. 9,18 MiB) |
| Registros | 40.609 |
| Variables | 24 |
| Cobertura temporal | Enero de 2008 a septiembre de 2026; 225 meses calendario presentes |
| Ámbito geográfico/comercial | Mercados CHEC (código 1234, 37.683 registros) y Pereira (código 1218, 2.926 registros) |
| Unidad de observación | Una combinación reportada de periodo, mercado, tipología de medición, nivel de tensión, modalidad de cobro, clase de servicio y rango de consumo |
| Granularidad temporal | Mensual |

#### Contenido y variables

Los nombres se conservan tal como aparecen en el CSV. Las magnitudes monetarias parecen corresponder a valores unitarios de tarifa; el archivo no incluye una unidad explícita, por lo que debe confirmarse en el metadato de origen antes de compararlas o convertirlas.

| Variable(s) | Interpretación según el nombre |
|---|---|
| `costounitariotarifa_ano`, `costounitariotarifa_mes` | Año y mes del reporte. |
| `comercializador_codigo`, `comercializador_nombre` | Identificador y nombre del comercializador (CHCC / CENTRAL HIDROELECTRICA DE CALDAS S.A. E.S.P.). |
| `mercado_codigo`, `mercado_nombre` | Código y nombre del mercado (CHEC o PEREIRA). |
| `costounitariotarifa_tipomed` | Tipo de medición: aparecen `S`, `HP` y `HM`; no se proporciona catálogo explicativo. |
| `nivel_tension_codigo` | Nivel de tensión codificado (1 a 4). |
| `modalidadcobro_propiedad` | Modalidad de cobro/propiedad del OR (por ejemplo, `0% OR`, `50% OR`, `100% OR`, `0% OR SIN AOM`). |
| `claseservicio_codigo`, `claseservicio_descri` | Código y descripción de la clase de servicio (29 descripciones observadas). Incluye clases residenciales, comerciales, industriales, oficiales y especiales. |
| `claseservicio_estrato` | Estrato residencial cuando aplica; `NA` en registros donde no se especifica o no corresponde. |
| `costounitariotarifa_rangoconsumo` | Rango de consumo codificado (se observan 1 y 2); requiere catálogo para interpretar sus umbrales. |
| `costounitariotarifa_tipomercado` | Tipo de mercado codificado; solo se observa `R`. |
| `costounitariotarifa_generacion`, `costounitariotarifa_transmision`, `costounitariotarifa_distribucion`, `costounitariotarifa_comercializacion`, `costounitariotarifa_perdidas`, `costounitariotarifa_restricciones` | Componentes de costo/tarifa asociados a generación, transmisión, distribución, comercialización, pérdidas y restricciones. |
| `costounitariotarifa_cu`, `costounitariotarifa_cureal` | Campos `CU` y `CU real`; la definición operativa debe confirmarse en el diccionario de origen. |
| `costounitariotarifa_subcon` | Componente o indicador de subsidio/contribución (interpretación tentativa por el nombre; confirmar en metadatos). |
| `costounitariotarifa_valor_tarifa` | Valor de tarifa reportado. |

#### Perfil de calidad y consistencia

- No se encontraron filas duplicadas al comparar las 24 columnas completas.
- No hay celdas vacías en 19 de las 24 columnas. Las cinco columnas con vacíos tienen 11 cada una: `distribucion`, `comercializacion`, `perdidas`, `restricciones` y `subcon` (55 vacíos en total, 0,0056 % de las 975.816 celdas).
- `claseservicio_estrato` contiene 25.266 valores literales `NA` (62,2 %). Deben tratarse como no aplicables/no informados según la clase; no convertirlos automáticamente en cero.
- Los años y meses cubren todos los meses de enero de 2008 a septiembre de 2026 (225/225), pero esto no garantiza que cada combinación de mercado y categoría exista todos los meses.
- Rango de valores observado para los campos numéricos de componentes y tarifas: generación 0–416,1932; transmisión 18,4788–66,8118; distribución 15,6263–335,3986; comercialización 23,1498–197,6767; pérdidas 2,1007–77,6352; restricciones −20,3656–163,8239; `CU` 199,3432–1.114,0034; `CU real` 0–934,8447; `subcon` −0,6000001–0,2; `valor_tarifa` 102,1672–1.336,8041. Los extremos negativos o cero ameritan validar reglas del dato, no son por sí solos prueba de error.
- Los códigos `tipomed`, `nivel_tension`, `claseservicio`, `rangoconsumo` y `tipomercado` requieren sus catálogos para análisis semántico confiable.
- El nombre del archivo sugiere una descarga de datos abiertos, pero el CSV no contiene URL, fecha de extracción, licencia, versión ni diccionario de datos. Registrar esos metadatos al incorporar el dataset al flujo de análisis.

#### Recomendaciones de uso

1. Parsear año, mes, códigos y magnitudes como tipos numéricos; conservar códigos con su catálogo y evitar perder ceros iniciales si existieran en futuras versiones.
2. Normalizar `NA` como valor faltante/no aplicable y diferenciarlo de las celdas vacías.
3. Consultar el diccionario de la fuente para confirmar unidades, significado de códigos y fórmulas de `CU`, `CU real`, `subcon` y `valor_tarifa`.
4. Al comparar series, controlar por mercado, clase de servicio, nivel de tensión, modalidad y rango de consumo; no promediar sin definir ponderaciones.
5. Para un corte reproducible, consignar que este archivo llega hasta septiembre de 2026.

#### Alcance de esta ficha

Caracterización calculada directamente sobre el archivo local. Las definiciones que no están explícitas en los nombres se señalan como tentativas o pendientes de contraste con los metadatos oficiales de publicación.

#### Evidencia incorporada en el Hito 3

- `EXA01` contrasta 756 celdas con Superservicios y obtiene 100 % de coincidencia en la
  muestra disponible.
- `DEF01` dispone del catálogo operativo de las 24 columnas en
  `fuentes_datos/catalogos/CHEC/chec_definiciones_def01.yaml`.
- `MAP01` registra 3/3 equivalencias código-nombre aprobadas metodológicamente por el
  proyecto, sin presentarlas como catálogo oficial CHEC.
- `cartas_log_chec.csv` contiene 276 series y 37 señales preliminares que deben revisarse
  frente a las publicaciones tarifarias.
- `OPO01` usa cobertura temporal 225/225 como proxy, no como puntualidad histórica.


<a id="doc-6e7ee696f27e"></a>

## desarrollo_puntos/3.2/EPM/Ficha_caracterizacion_02_epm_sfcd-b3ey.md

### Ficha de caracterización: epm_sfcd-b3ey

#### Identificación

| Atributo | Descripción |
|---|---|
| Archivo | `epm_sfcd-b3ey.csv` |
| Ubicación del archivo fuente | `fuentes_datos/datos/Datos_seleccionados/` |
| Tema | Información de costos unitarios y tarifas de energía eléctrica de EPM |
| Formato | CSV, delimitado por comas, encabezados en la primera fila y valores entre comillas |
| Tamaño | 426.826 bytes (aprox. 417 KiB) |
| Registros | 3.623 filas de datos |
| Variables | 12 |
| Cobertura temporal observada | Diciembre de 2016 a diciembre de 2021; 61 combinaciones año-mes presentes |
| Granularidad temporal | Mensual, con desgloses según tipo de información, tarifa, dato, consumo, nivel y propiedad |
| Unidad de observación | Una combinación de las categorías tarifarias y periodo, con valores reportados para EPM, compartido, cliente, punta y fuera de punta |
| Unidad de medida | No indicada en el archivo. Confirmar en el diccionario o la fuente antes de interpretar o comparar valores. |

#### Contenido y variables

| Variable(s) | Interpretación según el nombre y valores observados |
|---|---|
| `tipodeinformacion` | Modalidad de información: `Monomia` o `Horaria`. |
| `tipodetarifa` | Categoría de tarifa. Se observan `Costo Unitario`, `Tarifa`, `Residencial`, `No Residencial`, `Áreas Comunes` y una variante de capitalización (`No residencial`). |
| `tipodedato` | Componente, categoría de usuario o dato tarifario. Hay 28 valores distintos, entre ellos cargos de transporte, restricciones, costos de compra y estratos. |
| `rangodeconsumo` | Segmento de consumo: aparecen `N/A`, `Fuera de Punta`, `Punta`, `Rango 0 - CS`, `Rango > CS`, `Todo el consumo`, `0-CS` y `Mayor CS`. Confirmar equivalencias con el catálogo de origen. |
| `nivel` | Nivel de tensión, representado por números romanos I, II, III y IV. |
| `propiedadepm` | Valor asociado a propiedad de EPM. Su semántica y unidad exactas no se definen en el archivo. |
| `compartido` | Valor asociado al componente compartido. Su semántica y unidad exactas no se definen en el archivo. |
| `propiedaddelcliente` | Valor asociado a propiedad del cliente. Su semántica y unidad exactas no se definen en el archivo. |
| `punta`, `fueradepunta` | Valores para los periodos punta y fuera de punta; contienen muchos ceros según las categorías. |
| `year`, `mes` | Año y nombre del mes en español. Hay 2016–2021; 2016 solo tiene diciembre y 2017–2021 incluyen los doce meses. |

#### Perfil de calidad y consistencia

- Se leyeron 3.623 filas y 12 columnas; el archivo se decodifica correctamente como UTF-8 con BOM.
- Hay una fila parcialmente incompleta (fila 657 del archivo): conserva las seis categorías iniciales, pero deja vacíos los cinco valores (`propiedadepm`, `compartido`, `propiedaddelcliente`, `punta`, `fueradepunta`) y el periodo (`year`, `mes`). En total son 7 celdas vacías.
- Se identificaron 10 filas duplicadas exactas al comparar las 12 columnas. Conviene confirmar si son duplicados de extracción o si la fuente admite repeticiones antes de eliminarlas.
- Hay diferencias de escritura que pueden fragmentar categorías: `No Residencial` / `No residencial`; `Rango 0 - CS` / `0-CS`; `Rango > CS` / `Mayor CS`; `Costo compra: Gm, i` / `Costo compra: Gm,i`.
- Los campos de valor contienen valores extremos que requieren validar contra la publicación de origen. Por ejemplo, fila 2048: `compartido=205151.00` frente a `propiedadepm=213.50` y `propiedaddelcliente=197.37`; filas 3132 y 3134 contienen `punta=43577.00` y `punta=43501.00`, respectivamente. No se corrigieron ni eliminaron.
- También se observan valores negativos (mínimo −1,61 en campos de valor). Revisar si son ajustes válidos o errores de captura.
- El archivo no incorpora URL o fecha de descarga, licencia, versión, unidad de medida ni catálogo formal de códigos.

#### Recomendaciones de uso

1. Conservar los valores originales y crear una copia de trabajo para normalizar mayúsculas, espacios y variantes de etiquetas después de contrastarlas con la fuente.
2. Tratar la fila sin periodo como registro incompleto; no imputar sus valores sin una regla documentada.
3. Revisar los duplicados y valores extremos con el recurso oficial antes de decidir su exclusión, corrección o conservación.
4. Convertir `year` y los valores monetarios a tipos numéricos, y mapear los nombres de meses a una fecha mensual estandarizada.
5. Obtener metadatos para interpretar `propiedadepm`, `compartido`, `propiedaddelcliente`, la unidad de medida y los códigos de rangos/niveles.
6. En comparaciones, segmentar por tipo de información, tarifa, dato, rango de consumo, nivel y periodo; no combinar categorías heterogéneas sin definir una regla.

#### Alcance de esta ficha

Caracterización calculada directamente sobre el archivo local. Las interpretaciones de las columnas se basan en sus nombres y valores observados; las definiciones y unidades que no constan en el CSV quedan pendientes de verificación con los metadatos oficiales.

#### Evidencia incorporada en el Hito 3

- La comparación reproducible de `fuentes_datos/verificaciones/EPM/epm_exactitud_referencias.json`
  coincide en 18 de 18 celdas con seis filas de publicaciones oficiales de EPM (2020 y
  2021). Es una muestra de exactitud, no una certificación de todo el histórico.
- `desarrollo_puntos/3.5/EPM/cartas_log_epm.csv` contiene 60 series con referencia de 36
  cambios y vigilancia de 12 cambios en escala logarítmica. El resultado actual es
  preliminar y debe someterse a sensibilidad antes de usarlo como alerta operativa.
- La matriz OE1 deja `INT02` como no aplicable (no hay pares código-nombre). `OPO01` se
  evalúa con un proxy de cobertura temporal (períodos presentes frente a esperados), no
  como puntualidad histórica, porque el archivo no conserva fechas de publicación.
  `MAP01` queda como `provisional_interno`: sus equivalencias fueron aprobadas por el
  equipo del proyecto para normalización analítica, sin presentarlas como confirmación
  oficial de EPM. `DEF01` cuenta ahora con el catálogo operativo de las 12 columnas en
  `fuentes_datos/catalogos/EPM/epm_definiciones_def01.yaml`; sus unidades monetarias son
  condicionales al `tipodedato`. `CART01` permanece provisional hasta completar su
  calibración metodológica.


<a id="doc-6d09f59e62b7"></a>

## desarrollo_puntos/3.2/README.md

### 3.2 · Fichas de caracterización por fuente (OE2)

Corresponde a la actividad 2 del Hito 3: identidad de la fuente, cobertura, variables,
granularidad, interpretación, usos y limitaciones.

| Fuente | Ficha |
|---|---|
| CHEC · c698-wqig | [Caracterización CHEC](REFERENCIA_TECNICA.md#doc-1b5778bfd6a3) |
| EPM · sfcd-b3ey | [Caracterización EPM](REFERENCIA_TECNICA.md#doc-6e7ee696f27e) |
| Superservicios ZNI · ebby-cjha | [Caracterización SSPD](REFERENCIA_TECNICA.md#doc-da864825bc1a) |
| XM/SIMEM · c1b851 | [Caracterización del piloto XM](REFERENCIA_TECNICA.md#doc-eab9a734865a) |

[DECISION_CATALOGOS_CHEC.md](REFERENCIA_TECNICA.md#doc-cd7e104c7bc9) describe códigos, unidades,
semántica y clave candidata. Pertenece aquí por su contenido de caracterización, aunque
también sustenta las reglas y su aplicación.

En `perfiles/` se conservan:

- `sspd_verificacion_cobertura_seleccion.json`: evidencia de cobertura agregada SSPD;
  no demuestra continuidad individual de cada usuario.
- `xm_piloto_cobertura.json`: perfil del piloto y de su selección de versiones; conserva
  evidencia de la exploración, que debe leerse junto a la ficha actual.
- `perfil_supers_icnr-l4iw.json`: perfil histórico de una fuente en revisión, que no es
  el dataset SSPD ZNI de la matriz principal.

Los resultados históricos del Hito 2 están en [3.3/insumos_hito2](REFERENCIA_TECNICA.md#doc-70d8b8e8b09a).
La evaluación de candidatos CREG y XM está en [3.4](REFERENCIA_TECNICA.md#doc-8c63814239f9).


<a id="doc-da864825bc1a"></a>

## desarrollo_puntos/3.2/SSPD/Ficha_caracterizacion_03_sspd_ebby-cjha.md

### Ficha de caracterización: sspd_ebby-cjha

#### Identificación

| Atributo | Descripción |
|---|---|
| Dataset | `ebby-cjha` |
| Portal | https://www.datos.gov.co/d/ebby-cjha |
| Archivo de detalle | `fuentes_datos/datos/Datos_seleccionados/SSPD/sspd_ebby-cjha_detalle-compressed.zip` |
| Archivo agregado | `fuentes_datos/datos/Datos_seleccionados/SSPD/sspd_ebby-cjha_mensual.csv` |
| Publicador | Superintendencia de Servicios Públicos Domiciliarios |
| Tema | Información comercial residencial y no residencial de energía eléctrica |
| Filas de origen | 11.905.557 |
| Columnas de origen | 29 |
| Cobertura | Julio de 2017 a mayo de 2022, 59 períodos mensuales |
| Ámbito | Zonas No Interconectadas (ZNI) |
| Unidad de observación | Factura/usuario y período mensual |

#### Columnas del detalle

| Grupo | Columnas e interpretación |
|---|---|
| Identificación | `identificador_empresa` (prestador), `niu` (usuario), `id_factura` (factura), `codigo_localidad` (localidad), `codigo_conexion` (conexión). |
| Tiempo | `anio` (año), `periodo` (mes), `fecha_expedicion` (expedición de factura), `fecha_inicio_periodo` (inicio del período), `dias_facturados` (duración facturada). |
| Clasificación | `ubicacion` (urbana/rural u otro código), `tipo_conexion`, `estrato_sector`, `tipo_factura`, `tipo_lectura`, `tipo_categoria`. |
| Consumo | `consumo_basico`, `consumo_complementario`, `consumo_reside_mayor800`. Son consumos facturados por tramo; la unidad debe confirmarse documentalmente, aunque se espera kWh. |
| Facturación | `facturacion_consumo_basico`, `facturacion_complementario`, `facturacion_reside_mayor800`. |
| Otros valores | `valor_refacturacion`, `valor_mora`, `interes_mora`, `valor_subsidio`, `porcentaje_subsidio`, `valor_total`. |

#### Archivo agregado mensual

El archivo agregado no es una segunda fuente. Es una transformación reproducible del mismo dataset. Sus columnas son `identificador_empresa`, `anio`, `periodo`, `estrato_sector`, `ubicacion`, `tipo_conexion`, `tipo_lectura`, `tipo_factura`, `n_registros`, `consumo_basico_sum`, `consumo_basico_min`, `consumo_basico_max`, `consumo_compl_sum`, `consumo_mayor800_sum`, `fact_basico_sum`, `valor_total_sum`, `valor_subsidio_sum` y `dias_facturados_sum`.

#### Utilidad para el plan de hitos

- Aporta consumo observado, que no existe en EPM ni CHEC.
- Permite probar perfilamiento, reglas de calidad, agrupación mensual y razonabilidad.
- Tiene 59 meses globales; 117 grupos agregados presentan consumo básico positivo durante al menos 49 meses consecutivos.
- Permite probar transferencia del framework a 91 prestadores ZNI.
- Sirve para Hito 3 y para preparar Hito 4, pero las cartas deben ejecutarse sobre series homogéneas, no sobre el total de filas.

#### Limitaciones y adaptación de reglas

- Es ZNI; no debe compararse directamente con las reglas tarifarias de EPM/CHEC.
- R08 y R09 no aplican literalmente porque no existe el mismo eje de propiedad/modalidad tarifaria.
- La continuidad agregada no demuestra continuidad individual de cada usuario.
- `fecha_expedicion` mide facturación, no disponibilidad del dataset; no cierra OPO01.
- Exactitud requiere contraste con una fuente documental o maestra externa.
- Cero no debe convertirse automáticamente en dato faltante.

#### Dimensiones DAMA-DMBOK2

La fuente permite evaluar completitud, validez, unicidad, consistencia, integridad y razonabilidad con los datos disponibles. Exactitud y oportunidad requieren evidencia adicional. La aplicabilidad de cada regla debe registrarse explícitamente en la matriz, sin usar `no_aplica` para ocultar una falta de evidencia.

Archivo de definición: [`sspd.yaml`](../Data/silver/diccionarios/SSPD/sspd.yaml).

#### Cierre del Hito 3

El catálogo operativo de las variables críticas está en
`fuentes_datos/catalogos/SSPD/sspd_definiciones_def01.yaml`. Las cartas preliminares se
encuentran en `desarrollo_puntos/3.5/SSPD/cartas_log_sspd.csv`: 361 series, 4.332 cambios
vigilados y 143 señales. `OPO01` se evaluó como proxy de cobertura (59/65 períodos) y
`EXA01` permanece sin medir por falta de una fuente externa comparable para las empresas
ZNI. Estas limitaciones están descritas en
`desarrollo_puntos/3.3/SSPD/REVISION_REGLAS_SSPD.md`.


<a id="doc-eab9a734865a"></a>

## desarrollo_puntos/3.2/XM/Ficha_caracterizacion_04_xm_c1b851.md

### Ficha de caracterización: XM/SIMEM `c1b851`

#### Identificación

| Atributo | Descripción |
|---|---|
| Dataset histórico | `c1b851` |
| Portal | https://www.simem.co/ |
| Documentación API | https://github.com/EquipoAnaliticaXM/API_XM |
| Archivo crudo local | `fuentes_datos/datos/Datos_seleccionados/XM_piloto/xm_demanda_epmc_epmd_str02_202001_202501.csv` |
| Archivo mensual derivado | `fuentes_datos/datos/Datos_seleccionados/XM_piloto/xm_demanda_mensual_piloto.csv` |
| Publicador | XM/SIMEM |
| Tema | Demanda real de energía eléctrica |
| Alcance del piloto | Agente `EPMC`, mercado `EPMD`, sistema `STR02` |
| Período consultado | Enero de 2020 a enero de 2025 |
| Registros crudos | 119.928, incluyendo versiones por hora |
| Serie derivada | 61 observaciones mensuales y 44.592 observaciones horarias únicas |

#### Columnas del archivo crudo

| Columna | Interpretación |
|---|---|
| `CodigoVariable` | Código de la variable reportada, como demanda real. |
| `Valor` | Valor de demanda. |
| `MercadoComercializacion` | Mercado de comercialización. |
| `UnidadMedida` | Unidad del valor; en el piloto, kWh. |
| `CodigoSICAgente` | Código del agente del mercado. |
| `SistemaTransmision` | Sistema de transmisión. |
| `Version` | Versión de la información publicada. |
| `FechaHora` | Fecha y hora de la observación horaria. |
| `CodigoDuracion` | Duración del intervalo, por ejemplo `PT1H`. |

#### Columnas de la serie mensual derivada

| Columna | Interpretación |
|---|---|
| `periodo` | Mes de agregación. |
| `CodigoSICAgente` | Agente seleccionado. |
| `MercadoComercializacion` | Mercado seleccionado. |
| `SistemaTransmision` | Sistema seleccionado. |
| `Version_seleccionada` | Versión elegida para el mes. |
| `horas` | Registros horarios usados. |
| `horas_unicas` | Horas únicas encontradas. |
| `horas_esperadas` | Horas esperadas para el calendario del mes. |
| `demanda_kwh` | Suma mensual de demanda. |
| `publicacion_declarada` | Fecha de publicación declarada en el calendario de versiones. |

#### Regla de construcción de la serie

Para cada mes se seleccionó la versión numérica `TX` más alta disponible, se excluyeron `TXF` y `TXR`, se conservaron horas únicas y se sumaron sus valores. No se sumaron versiones entre sí, no se interpolaron horas faltantes y no se rellenaron valores.

Esta política produjo 61 meses completos y positivos. Exigir únicamente la versión marcada `esMaximaVersion=1` produce 53 meses y no alcanza la continuidad requerida; por eso la política debe quedar aprobada y congelada antes de comparar técnicas.

#### Utilidad para el plan de hitos

- Proporciona una variable operacional diferente de tarifas y facturación: demanda eléctrica.
- Permite probar agregación horaria-mensual, trazabilidad de versiones y continuidad temporal.
- Tiene longitud suficiente para el escenario de 48 cambios de referencia y 12 meses de vigilancia.
- Permite aplicar cartas, Isolation Forest, Z-score robusto y comparar métodos en Hito 4.
- Es útil para validar la reproducibilidad del framework sobre un dominio energético distinto.

#### Limitaciones y adaptación de reglas

- Es un piloto filtrado, no el mercado completo.
- La serie mensual depende de una política de selección de versiones; no debe presentarse como “última versión oficial” sin una justificación adicional.
- R08 y R09, diseñadas para propiedad y modalidad tarifaria, deben reemplazarse por controles equivalentes de demanda.
- Exactitud requiere una referencia horaria o mensual equivalente.
- Oportunidad requiere vincular todas las observaciones con una fecha de disponibilidad y un plazo esperado; junio de 2021 aún carece de ese vínculo.

#### Dimensiones DAMA-DMBOK2

La fuente permite trabajar completitud, validez, unicidad, consistencia, integridad y razonabilidad. Exactitud y oportunidad siguen pendientes de evidencia externa. La matriz debe conservar el método de versión, el filtro y el hash como parte de la trazabilidad.

La fuente es publicada por XM y no por CREG. CREG se utiliza como referencia regulatoria, no como atribución del dataset.

#### Cierre del Hito 3

El catálogo operativo está en `fuentes_datos/catalogos/XM/xm_definiciones_def01.yaml`.
La matriz incorpora mapeos internos para agente, mercado, sistema y unidad, y `OPO01`
usa un proxy de trazabilidad de 60/61 meses con fecha declarada. `EXA01` permanece sin
medir por falta de una referencia horaria o mensual independiente; esta limitación y las
adaptaciones de R08/R09 están documentadas en `desarrollo_puntos/3.3/XM/REVISION_REGLAS_XM.md`.
La carta I-MR está disponible en `desarrollo_puntos/3.5/XM/cartas_log_xm.csv` y se
reproduce con `cartas_log_xm.py`.


<a id="doc-f0cd728e94a3"></a>

## desarrollo_puntos/3.3/CHEC/REVISION_REGLAS_CHEC.md

### CHEC: cierre de controles del Hito 3

Fuente: `fuentes_datos/datos/Datos_seleccionados/CHEC/chec_c698-wqig.csv` (`c698-wqig`,
40.609 filas y 24 columnas).

El script y la salida de cartas citados abajo están en
[3.5/CHEC](REFERENCIA_TECNICA.md#doc-6927d6df7ab3). El análisis de códigos y semántica está en
[3.2/CHEC](REFERENCIA_TECNICA.md#doc-cd7e104c7bc9).

#### Evidencia y resultados

- `EXA01` contrasta 756 celdas contra Superservicios (`td8k-vhq9`) y obtiene 100 % de
  coincidencia en el alcance temporal y categórico disponible.
- `fuentes_datos/catalogos/CHEC/chec_definiciones_def01.yaml` documenta las 24 columnas,
  diferenciando códigos, categorías, componentes y agregados monetarios. El cierre es
  metodológico interno porque faltan algunos catálogos formales de CHEC.
- `MAP01` evalúa 3/3 mapeos código-nombre con aprobación metodológica interna.
- `cartas_log_chec.py` genera `cartas_log_chec.csv` con 276 series y 3.312 cambios
  vigilados; se detectan 37 señales preliminares.
- `OPO01` usa un proxy de cobertura temporal de 225/225 meses. No representa el plazo
  histórico de publicación porque el CSV no contiene fecha de disponibilidad.

#### Limitaciones

Las 37 señales deben revisarse contra cambios tarifarios oficiales antes de clasificarlas
como errores. Las unidades y siglas de `tipomed`, `CU real`, `subcon` y `valor_tarifa`
deben interpretarse con el catálogo formal del publicador; mientras no exista, se reportan
como definiciones operativas del proyecto.


<a id="doc-44ac9713606e"></a>

## desarrollo_puntos/3.3/EPM/REVISION_REGLAS_EPM.md

### EPM: cierre de controles del Hito 3

Fuente: `fuentes_datos/datos/Datos_seleccionados/EPM/epm_sfcd-b3ey.csv` (`sfcd-b3ey`, 3.623 filas).
La medición se ejecuta con `python3 desarrollo_puntos/3.1/medir_matriz_oe1.py`.

Los archivos de cartas y revisión de señales citados abajo están en
[3.5/EPM](REFERENCIA_TECNICA.md#doc-6927d6df7ab3); los de cuarentena, en
[3.7/EPM](REFERENCIA_TECNICA.md#doc-9d236b840cde).

#### Evidencia incorporada

- `fuentes_datos/verificaciones/EPM/epm_exactitud_referencias.json` conserva seis
  comparaciones reproducibles (enero/diciembre de 2020, abril/diciembre de 2021) contra
  los PDF oficiales de EPM. Se contrastan `propiedadepm`, `compartido` y
  `propiedaddelcliente` en nivel I.
- `cartas_log_epm.py` genera `cartas_log_epm.csv`: 60 series con al menos 49 períodos,
  36 cambios de referencia y 12 de vigilancia. No se imputan meses ni se mezclan valores
  no positivos. El resultado es una línea base preliminar para CART01.
- `revision_cartas_epm.py` genera `revision_senales_cartas_epm.csv` con las 50 señales
  individuales, sus períodos, valores anterior/actual y límites. La columna
  `clasificacion` queda como `pendiente_revision` hasta contrastar cada señal con su
  publicación mensual; no se convierten automáticamente en errores.
- `cuarentena.py` genera `cuarentena_registros.csv` con 9 filas derivadas de R08, R11,
  R12 y R07-error. `cartas_log_epm.py` las excluye por `clave_contenido`, sin modificar
  el CSV fuente ni interpolar valores.
- Los metadatos oficiales locales se usan para DEF01. La cobertura es parcial: describen
  7 de 12 columnas, pero no fijan la unidad y semántica completa de todos los importes.
- `fuentes_datos/catalogos/EPM/epm_etiquetas.yaml` documenta las equivalencias aprobadas
  metodológicamente por el equipo del proyecto. Esta aprobación es interna y no sustituye
  una confirmación de EPM; el CSV original no se modifica.
- `fuentes_datos/catalogos/EPM/epm_definiciones_def01.yaml` documenta las 12 columnas con
  significado, unidad, aplicación y evidencia. Las unidades de las medidas son
  condicionales al `tipodedato` y no se tratan como una unidad única.

#### Estado interpretado

| Control | Estado | Interpretación |
|---|---|---|
| EXA01 | provisional | La muestra coincide con la publicación oficial; falta ampliar a todos los meses y categorías. |
| MAP01 | provisional_interno | Las variantes se normalizan con una decisión metodológica del proyecto; no se presenta como aprobación oficial de EPM. |
| DEF01 | provisional_interno | Las 12 columnas tienen definición operativa documentada; las unidades condicionadas y la aprobación son metodológicas del proyecto. |
| CART01 | provisional | Ya existe carta I-MR preliminar en cambios logarítmicos; falta sensibilidad y revisión de dominio. |
| INT02 | no aplica | No existen pares código-nombre en el esquema EPM. |
| OPO01 | provisional_proxy | Se comparan los períodos presentes frente a los esperados (61/61); esto evalúa cobertura temporal, no el plazo histórico real de publicación. |

Por tanto, EPM ya no queda con controles técnicos sin ejecutar: las brechas restantes
son de evidencia o aprobación externa y están separadas de los resultados medidos. El
proxy de OPO01 se presenta explícitamente como una aproximación, no como puntualidad.


<a id="doc-7dec091a7816"></a>

## desarrollo_puntos/3.3/INFORME_DIFERENCIAS_FUENTES.md

### Informe de diferencias entre fuentes — Hito 3

#### Alcance

Este informe compara la aplicación de la matriz OE1 y de las cartas de control a las cuatro
fuentes seleccionadas: EPM (`sfcd-b3ey`), CHEC (`c698-wqig`), Superservicios (`ebby-cjha`) y
XM/SIMEM (`c1b851`). La comparación se basa en `matriz_oe1.csv`, las fichas de caracterización,
las cartas logarítmicas y el bootstrap por categoría. No mezcla registros ni resultados entre
fuentes.

Ubicaciones actuales: [matriz OE1](../Data/gold/outputs/calidad/matriz_oe1.csv),
[fichas](REFERENCIA_TECNICA.md#doc-6d09f59e62b7), [cartas](REFERENCIA_TECNICA.md#doc-6927d6df7ab3) y
[bootstrap](../Data/gold/outputs/cuarentena_bootstrap/bootstrap/bootstrap_categorias.csv).

#### Diferencias estructurales

| Fuente | Naturaleza del dato | Unidad de carta | Tratamiento específico |
|---|---|---|---|
| EPM | Tarifas históricas de energía eléctrica | Serie mensual por combinación tarifaria | Se excluyen de los límites los cambios que tocan registros en cuarentena; no se imputan valores. |
| CHEC | Costos unitarios y tarifas por categoría | Serie mensual por combinación de categoría y nivel | La clave y los catálogos requieren confirmación documental; los negativos no se eliminan automáticamente porque pueden representar restricciones o ajustes. |
| SSPD | Información comercial residencial/no residencial | Serie mensual por combinación de identificadores y concepto | Se aplican reglas transversales; los controles que requieren propiedad o catálogo externo pueden quedar como no aplicables. |
| XM/SIMEM | Demanda eléctrica horaria agregada | Serie horaria de demanda (`demanda_kwh`) | Adaptación explícita de reglas originalmente tarifarias; el resultado es piloto y no se interpreta como tarifa. |

#### Comparación de la matriz OE1

La matriz contiene 19 controles para cada fuente (76 filas). Las ocho dimensiones DAMA-DMBOK
están representadas en cada ficha y no se elimina una dimensión porque la fuente tenga un
esquema diferente. Cuando el concepto no existe se registra `no_aplica`; cuando faltan datos
para calcularlo se registra `no_medible`.

| Fuente | Medido | Provisional | Provisional interno | Proxy | No medible | No aplica |
|---|---:|---:|---:|---:|---:|---:|
| EPM | 6 | 9 | 2 | 1 | 0 | 1 |
| CHEC | 5 | 11 | 2 | 1 | 0 | 0 |
| SSPD | 6 | 6 | 2 | 1 | 1 | 3 |
| XM | 7 | 6 | 3 | 1 | 1 | 1 |

Los estados no son calificaciones finales de calidad. `Provisional` indica que falta cerrar una
decisión metodológica o documental; `provisional_proxy` indica que se usó una medida indirecta;
`no_medible` indica ausencia de evidencia; y `no_aplica` indica que el concepto no existe en el
esquema de esa fuente.

#### Cartas y bootstrap

Las cartas usan cambios logarítmicos y se ejecutan solo donde existe una serie temporal suficiente.
SSPD tiene series mensuales aptas para el análisis disponible; XM usa una adaptación de demanda.
El archivo `../3.7/bootstrap/bootstrap_categorias.csv` calcula intervalos del 95 % para la tasa de señales
de CART01 remuestreando series dentro de cada categoría. La ejecución tiene 105 categorías:
EPM (8), CHEC (4), SSPD (92) y XM (1). XM y una categoría de SSPD tienen una sola serie, por lo
que sus intervalos son degenerados.

#### Diferencias que deben conservarse en la interpretación

1. Una misma regla puede tener distinto denominador por la estructura y cobertura de cada fuente.
2. Un porcentaje mayor no implica automáticamente mejor calidad si se obtuvo con menor población,
   un proxy o un catálogo no aprobado.
3. Las alertas de cartas identifican señales de comportamiento atípico; no sustituyen un contraste
   documental de exactitud.
4. La oportunidad no queda demostrada por la fecha de descarga. Requiere fecha de publicación,
   frecuencia comprometida y evidencia de disponibilidad.
5. La ausencia de una dimensión en el esquema se informa como `no_aplica`, no como cero ni como
   cumplimiento total.

#### Conclusión

Las cuatro fuentes son comparables a nivel metodológico porque pasan por la misma matriz, pero no
son intercambiables a nivel semántico. EPM y CHEC permiten concentrar el análisis tarifario;
SSPD aporta información comercial y consumo; XM aporta una fuente operativa de demanda. Esta
distinción debe mantenerse en el Hito 4 al construir scorecards y comparar técnicas.


<a id="doc-70d8b8e8b09a"></a>

## desarrollo_puntos/3.3/insumos_hito2/README.md

### Salidas de la ejecución del Hito 2

Esta carpeta conserva el código y las salidas históricas del Hito 2 como insumos de
replicación. Su ubicación no acredita que el Hito 3 esté cerrado ni que estas salidas
correspondan a Superservicios. Los archivos 06, 07 y 11 son además insumos del Hito 4.

#### Fichas de caracterización

- [CHEC](REFERENCIA_TECNICA.md#doc-1b5778bfd6a3).
- [EPM](REFERENCIA_TECNICA.md#doc-6e7ee696f27e).
- [SSPD ZNI](REFERENCIA_TECNICA.md#doc-da864825bc1a).
- [XM/SIMEM](REFERENCIA_TECNICA.md#doc-eab9a734865a). Son las fichas de las fuentes incorporadas al conjunto metodológico actual.

Archivos que produce `codigo_hasta_hito2.py` al correr de principio a fin. Se
versionan porque el plan de hitos los nombra como **insumo** de los hitos 3 y 4, y sin
ellos esas actividades no se pueden iniciar.

#### Procedencia de esta ejecución

| | |
|---|---|
| Fecha de ejecución | 27 de octubre de 2026 |
| Entrada | Histórico de tarifas de EPM, conjunto `sfcd-b3ey` |
| Descarga | `https://www.datos.gov.co/api/views/sfcd-b3ey/rows.csv?accessType=DOWNLOAD`, 27-10-2026 23:12:43 UTC |
| SHA-256 de la entrada | `8d792b49c1f15ded30183d1488199c5230b63e856be53723d65b665ca2b797e8` |
| Filas × columnas | 3.623 × 12 |
| Entorno | Python 3.12.10 · pandas 2.3.3 · scikit-learn 1.9.1 · statsmodels 0.15.0 |

El mismo SHA-256 queda registrado dentro de `00_resumen.json`, que lo calcula el propio
código.

#### Verificación

La ejecución reproduce **las trece cifras** de la tabla de verificación de
`0_Recomendaciones_profesor/revision_hito2.md`, sin ninguna diferencia:

| Cifra | Valor |
|---|---|
| Filas y columnas | 3.623 × 12 |
| Variantes de etiqueta / filas afectadas | 11 / 445 |
| Duplicados exactos adicionales | 10 |
| Series posibles / con ≥49 meses / limpias | 202 / 83 / 77 |
| Pruebas inyectadas | 8.282 |
| Detección: reglas / cartas / IF / reglas+cartas | 73 / 80 / 80 / 88 % |
| Alertas en meses limpios: cartas / IF | 11,4 / 12,0 % |
| Series con alerta en feb-2020 | 51 de 83 |
| IC 95 % de la diferencia IF − cartas | −1,4 a +2,3 puntos |

Esto constituye el **primer dato de reproducibilidad entre ambientes** que pide el Hito 6:
el Hito 2 se desarrolló en Colab y estas salidas provienen de una ejecución en Windows.

#### Dos condiciones para reejecutarlo

**1. Codificación.** El código imprime el símbolo `≥` en el nombre de la regla R08. Una
consola de Windows con la codificación por defecto falla con `UnicodeEncodeError`. Hay que
forzar UTF-8 por entorno, sin tocar el código:

```
PYTHONUTF8=1 PYTHONIOENCODING=utf-8 MPLBACKEND=Agg python desarrollo_puntos/3.3/insumos_hito2/codigo_hasta_hito2.py
```

Esto es un hallazgo de reproducibilidad en sí mismo: el código es reproducible siempre que
el entorno se declare; sin declararlo, falla.

**2. Nombres de columna.** El código espera los **nombres de visualización** del portal
(`Año`, `Mes`, `Tipo de Tarifa`, `Propiedad Epm`…) y lee el archivo como `epm_tarifas.csv`
desde la carpeta de trabajo.

El CSV conservado en `fuentes_datos/datos/epm_sfcd-b3ey.csv` trae los **nombres técnicos de
la API** (`year`, `mes`, `tipodetarifa`, `propiedadepm`…), porque se descargó por el
endpoint `/resource/`. **Con ese archivo el pipeline falla con `KeyError`.** Para
reejecutar hay que descargar por el endpoint `rows.csv?accessType=DOWNLOAD` o añadir un
mapeo de nombres en la capa de carga.

Resolver esto corresponde a la actividad 3 del Hito 3, que exige que el pipeline corra
«sin cambios manuales en las dos fuentes».

#### Archivos

| Archivo | Contenido | Lo usa |
|---|---|---|
| `00_resumen.json` | Cifras agregadas y SHA-256 de la entrada | Verificación |
| `02_catalogo_variantes.csv` | Variantes de etiqueta y su forma canónica | R06, MAP01 |
| `03_hallazgos.csv` | Bitácora de incidencias por regla | **Insumo de los hitos 3 y 6** |
| `04_resumen_reglas.csv` | Filas marcadas por regla | Hito 3 |
| `05_alertas_imr_reales.csv` | Alertas de las cartas sobre datos reales | **Insumo de los hitos 3 y 6** |
| `06_experimento_inyeccion.csv` | Resultado por prueba inyectada | **Insumo del hito 4** |
| `07_deteccion_por_tipo.csv` | Detección por tipo de error y método | **Insumo del hito 4** |
| `08_copia_preparada.csv` | Copia preparada con trazabilidad | **Insumo del hito 3** |
| `11_puntajes_limpios_por_serie.csv` | Puntajes en meses sin error conocido | **Insumo del hito 4** |
| `figuras/` (no incluida en esta carpeta) | Las cuatro gráficas que genera el código del Hito 2 | Presentación |

#### Advertencia

Estas salidas corresponden a **una** descarga del portal. El criterio de cierre del Hito 3
exige obtener los mismos hallazgos con **dos descargas distintas**, y la revisión del Hito 2
documenta que el portal devuelve las mismas filas en otro orden entre descargas. Esa
comprobación corresponde a la actividad 6 y no está hecha.


<a id="doc-1daec17adf88"></a>

## desarrollo_puntos/3.3/README.md

### 3.3 · Réplica del pipeline y diferencias entre fuentes

Corresponde a la actividad 3 del Hito 3. Agrupa la adaptación de reglas a los esquemas
de las fuentes y el informe de diferencias de su aplicación.

| Archivo o carpeta | Función |
|---|---|
| [INFORME_DIFERENCIAS_FUENTES.md](REFERENCIA_TECNICA.md#doc-7dec091a7816) | Comparación de estructura, aplicabilidad, medición y limitaciones. |
| [medir_sspd.py](../Code/Data_Acquisition_and_Understanding/adaptadores/medir_sspd.py) | Adaptador de la matriz para SSPD ZNI, ebby-cjha. |
| [medir_xm.py](../Code/Data_Acquisition_and_Understanding/adaptadores/medir_xm.py) | Adaptador específico del piloto de demanda XM. |
| [lector_datos.py](../Code/Data_Acquisition_and_Understanding/adaptadores/lector_datos.py) | Carga compartida de CSV, incluidos los conservados en ZIP. |
| [EPM](REFERENCIA_TECNICA.md#doc-44ac9713606e), [CHEC](REFERENCIA_TECNICA.md#doc-f0cd728e94a3), [SSPD](REFERENCIA_TECNICA.md#doc-d9da2f0b37a2), [XM](REFERENCIA_TECNICA.md#doc-5cd7ac79d74f) | Documentación de aplicación, adaptación y estado de controles por fuente; también remite a las cartas. |
| [insumos_hito2](REFERENCIA_TECNICA.md#doc-70d8b8e8b09a) | Código y resultados EPM históricos usados como referencia para la réplica. Incluye insumos posteriores del Hito 4. |
| [medir_sspd_nr.py](../Code/Data_Acquisition_and_Understanding/adaptadores/medir_sspd_nr.py) | Adaptador histórico de bnkp-xdb7; se conserva como antecedente y no participa en la matriz principal actual. |

El script de medición principal está en [3.1](../Code/Data_Acquisition_and_Understanding/calidad/medir_matriz_oe1.py), porque su
producto es la matriz OE1. Desde allí importa los adaptadores de esta carpeta.

El plan original menciona Superservicios vfjy-6fka y ocho períodos. Los archivos
actuales documentan SSPD ebby-cjha, con 59 períodos globales, y otras fuentes. La
organización respeta los archivos existentes y no cambia su alcance para hacerlos
coincidir con el ejemplo histórico del plan. Su aprobación metodológica es un asunto
distinto de su ubicación.


<a id="doc-d9da2f0b37a2"></a>

## desarrollo_puntos/3.3/SSPD/REVISION_REGLAS_SSPD.md

### SSPD: cierre de controles del Hito 3

Fuente: `ebby-cjha`, información comercial de energía en ZNI. La copia conserva el
censo mensual de 91 empresas y el detalle completo de una empresa.

El script y la salida de cartas se conservan en [3.5/SSPD](REFERENCIA_TECNICA.md#doc-6927d6df7ab3).

#### Resultados incorporados

- `DEF01`: 19/19 variables críticas documentadas en
  `fuentes_datos/catalogos/SSPD/sspd_definiciones_def01.yaml`. Es una definición
  metodológica porque el portal no publica descripciones completas.
- `MAP01`: 3/3 grupos de variantes normalizados internamente, sin afirmar que exista
  aprobación oficial de la SSPD.
- `OPO01`: proxy de cobertura 59/65 períodos del alcance enero de 2017 a mayo de 2022
  (90,77 %). Los seis primeros meses de 2017 no están en la fuente.
- `CART01`: 361 series con al menos 49 períodos, 4.332 cambios vigilados y 143 señales
  preliminares. Las señales no se clasifican automáticamente como errores.

#### Limitaciones

`EXA01` permanece sin medir directamente porque no se encontró una segunda fuente que
reporte los mismos consumos de las 91 empresas ZNI con la misma granularidad. La exactitud
debe presentarse como limitación de evidencia, no como 100 % inferido del propio archivo.
R08 y R09 no aplican al esquema tarifario de esta fuente. Las unidades de consumo y
facturación son hipótesis operativas hasta contar con un diccionario formal del publicador.


<a id="doc-05a8db13b38d"></a>

## desarrollo_puntos/3.3/XM/README.md

### XM/SIMEM · c1b851

Aquí se conserva la revisión metodológica específica de XM/SIMEM. El adaptador ejecutable
`medir_xm.py` permanece en la carpeta raíz de `3.3` porque la matriz global lo importa
directamente; los datos crudos y derivados están en `fuentes_datos/datos/Datos_seleccionados/XM_piloto/`.


<a id="doc-5cd7ac79d74f"></a>

## desarrollo_puntos/3.3/XM/REVISION_REGLAS_XM.md

### Revisión metodológica de reglas para XM/SIMEM

#### Propósito

El script y la salida de cartas citados en este documento están en
[3.5/XM](REFERENCIA_TECNICA.md#doc-6927d6df7ab3). La matriz se conserva en [3.1](REFERENCIA_TECNICA.md#doc-cd000226e09e).

Este documento realiza el punto 1 del siguiente paso del Hito 3: revisar la matriz OE1 para XM y recordar el significado de cada regla. XM contiene demanda horaria y versiones de publicación, no tarifas. Por eso una regla tarifaria no se copia literalmente: se adapta por propósito y se deja evidencia de la decisión.

Estados utilizados:

- **Directa:** puede medirse con el contrato actual de XM.
- **Adaptada:** conserva el propósito de la regla, pero cambia la unidad o relación evaluada.
- **No medible:** necesita una fuente externa o una decisión todavía inexistente.
- **No aplica:** el concepto original no existe en XM.

#### Reglas base R01–R12

| Regla | Qué controla | Aplicación en XM | Estado actual |
|---|---|---|---|
| **R01** | Período informado | Verifica que `periodo` exista en la serie mensual derivada y que `FechaHora` exista en el crudo. | Directa; 61/61 meses. |
| **R02** | Período válido | Comprueba formato `AAAA-MM`, fechas válidas y horas que puedan convertirse a fecha-hora. | Directa; debe conservar la zona horaria definida. |
| **R03** | Formato numérico | Comprueba que `Valor` y `demanda_kwh` sean números finitos. | Directa; medida preliminar 100 %. |
| **R04** | Duplicados exactos | Busca filas idénticas en el archivo horario o mensual, sin usar la posición de la fila como identificador. | Directa. |
| **R05** | Multiplicidad de clave | Usa la clave `agente + mercado + sistema + versión + FechaHora` para el crudo y `agente + mercado + sistema + periodo` para el agregado. | Directa, con versiones separadas. |
| **R06** | Representación canónica | Revisa escritura consistente de agente, mercado, sistema, versión, unidad y duración. | Adaptada; falta catálogo oficial externo. |
| **R07** | Signo y dominio | Verifica que la demanda sea finita y no negativa, y que la duración y unidad pertenezcan al dominio autorizado. | Adaptada; confirmar formalmente el dominio de demanda. |
| **R08** | Coherencia de tarifas por propiedad | En EPM/CHEC compara tarifas según propiedad. En XM no existe propiedad tarifaria. Se reemplaza por coherencia entre agente, mercado y sistema dentro de una misma serie. | Adaptada; no es una prueba de orden tarifario. |
| **R09** | Aplicabilidad según nivel y modalidad | En EPM/CHEC revisa qué componentes tarifarios aplican. En XM comprueba la compatibilidad `CodigoVariable–UnidadMedida–CodigoDuracion–Version`. | Adaptada. |
| **R10** | Medidas requeridas presentes | Comprueba que cada mes tenga demanda, versión, horas únicas y horas esperadas. | Directa; medida preliminar 100 %. |
| **R11** | Posible serial de fecha en importes | Busca números que parecen fechas de Excel dentro de importes. XM no tiene importes tarifarios. | No aplica a XM. |
| **R12** | Magnitud atípica | Compara cambios de demanda frente a la mediana de una ventana de referencia. | Adaptada; factor 10 provisional y requiere sensibilidad. |

#### Controles complementarios

| Control | Qué controla | Aplicación en XM | Estado actual |
|---|---|---|---|
| **INT01** | Integridad estructural | Verifica las nueve columnas del contrato crudo y las columnas esperadas del agregado mensual. | Directa; contrato crudo 9/9. |
| **INT02** | Integridad referencial | Contrasta códigos de agente, mercado y sistema contra catálogos autorizados y versionados. | No medible; faltan catálogos externos. |
| **EXA01** | Exactitud documental | Contrasta una muestra de `Valor` o `demanda_kwh` con una referencia horaria/mensual equivalente. | No medible; falta referencia independiente. |
| **OPO01** | Oportunidad | Compara disponibilidad real de cada publicación con un plazo esperado documentado. | No medible; hay fechas declaradas, pero falta plazo y vínculo completo. |
| **MAP01** | Equivalencia de etiquetas | Documenta transformaciones como códigos, unidades o versiones y demuestra que conservan el significado. | No medible; no se han aplicado mapeos documentados. |
| **DEF01** | Definición semántica | Verifica que las variables críticas tengan significado, unidad y regla de uso aprobados. | No medible; falta aprobación documental completa. |
| **CART01** | Cartas I-MR | Aplica cartas sobre cambios logarítmicos de `demanda_kwh` después de separar referencia y vigilancia. | Provisional; se calcularon 12 meses de vigilancia, pero faltan congelar límites, cuarentena y sensibilidad. |

#### Decisiones metodológicas recomendadas

1. Mantener R08 y R09 en la matriz porque el profesor exige evaluar las ocho dimensiones, pero identificarlas como adaptaciones de dominio y no como equivalentes literales de las reglas tarifarias.
2. No convertir R11 en una aprobación automática: en XM queda `no_aplica` porque no hay importes, y esa diferencia se reporta como una característica del esquema.
3. Mantener R12 y CART01 como advertencias estadísticas. Una alerta no demuestra que el valor sea incorrecto.
4. Usar 36 cambios de referencia y 12 de vigilancia para la comparación común. XM tiene 60 cambios disponibles; se conservan los restantes para sensibilidad.
5. No declarar cerradas exactitud ni oportunidad hasta obtener, respectivamente, una referencia equivalente y un plazo de publicación documentado.

#### Actualización del adaptador

El catálogo `fuentes_datos/catalogos/XM/xm_definiciones_def01.yaml` documenta las
variables crudas y derivadas del piloto. Se incorporó un proxy de oportunidad con las
fechas declaradas de publicación (60/61 meses), mapeos internos para los códigos fijos
del piloto y una evaluación de integridad referencial interna. Estas decisiones no
equivalen a un catálogo completo ni a una fecha límite oficial de XM.
La carta I-MR queda materializada en `cartas_log_xm.csv` y se reproduce con
`cartas_log_xm.py`: 61 meses, 36 cambios de referencia, 12 de vigilancia y 0 señales
con los límites preliminares actuales.

#### Resultado del punto 1

La matriz de XM es metodológicamente utilizable como adaptador de demanda: 7 controles
tienen medición directa, 6 son provisionales, 3 son provisionales internos, 1 es un proxy,
1 no aplica por ausencia de importes tarifarios y EXA01 requiere evidencia externa. Esto
permite continuar con la formalización de cartas del Hito 3 sin afirmar que la exactitud
documental esté cerrada.


<a id="doc-50ab77624282"></a>

## desarrollo_puntos/3.4/Evaluacion_fuente_alternativa_XM.md

### Fuente alternativa investigada: demanda eléctrica de XM/SIMEM

Consulta: 4 de noviembre de 2026. Se buscó electricidad colombiana, consumo/demanda, mínimo 10.000 registros, historia temporal para cartas y evidencia para medir las ocho dimensiones. El análisis considera que el profesor exige medirlas todas.

Actualización posterior al análisis inicial: se ejecutó un piloto de 61 meses para el grupo EPMC/EPMD/STR02. Los datos están en `fuentes_datos/datos/Datos_seleccionados/XM_piloto/` y la decisión de cuatro fuentes en `fuentes_datos/PROPUESTA_CUATRO_FUENTES.md`. La longitud y continuidad se comprobaron bajo la política de mayor TX numérica disponible por mes; no bajo la versión final marcada en el calendario. Exactitud y oportunidad siguen pendientes. Las consultas puntuales que se describen abajo corresponden a la exploración inicial.

#### Resultado de la búsqueda

La alternativa más prometedora fuera de las fuentes tarifarias es **XM/SIMEM: histórico de demanda real por agente**, dataset `c1b851`. Se comprobaron datos reales en kWh, códigos de agente como texto y versiones de liquidación. Es una recomendación para un piloto con alcance retrospectivo, no una afirmación de cumplimiento completo del proyecto.

Portal: https://www.simem.co/

Documentación oficial: https://github.com/EquipoAnaliticaXM/API_XM

Referencia en datos.gov.co: https://www.datos.gov.co/d/bt68-juyf . Su título corresponde a la estructura de demandas por código SIC, mercado y sistema; la evidencia efectiva de esta revisión se obtuvo directamente de SIMEM con el ID `c1b851`.

API de muestra: https://www.simem.co/backend-files/api/PublicData?datasetId=c1b851&startdate=2020-01-01&enddate=2020-01-02

El archivo de evidencia [perfiles/evaluacion_candidato_xm.json](../Data/gold/outputs/seleccion_fuentes/perfiles/evaluacion_candidato_xm.json) conserva parámetros, metadatos, esquema, conteos, ejemplos y hashes de respuestas. Las muestras completas de las consultas no se incorporaron al repositorio y no se cambiaron los datasets seleccionados.

#### Qué se comprobó directamente

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

#### Advertencia sobre el reemplazo vigente

El inventario oficial relaciona `DdaReal` con el conjunto `14fabb`, llamado **Demanda real nacional**. Se comprobaron 4.512 registros para 1–2 de octubre de 2026, pero cero para 1–2 de enero de 2020. No se puede asumir que conserva el mismo histórico que `c1b851` ni concatenar ambos sin armonizar dimensiones y versiones. El conjunto antiguo y el vigente tienen estructuras diferentes.

No debe descargarse el conjunto nuevo pensando que basta para el protocolo mensual de 49/61 observaciones. Para una tesis retrospectiva puede fijarse el antiguo como snapshot; para operación futura hace falta un adaptador al esquema vigente.

#### Cómo cubriría las ocho dimensiones

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

#### Qué exige adaptar del proyecto

R08 y R09 del caso tarifario EPM se basan en propiedad, nivel y columnas específicas que no existen aquí. Esta fuente no cumple la condición de ejecutar literalmente esas mismas reglas. Se necesitarían equivalentes justificados de consistencia del proceso de demanda, con trazabilidad del cambio y validación con el director. Tampoco deben inventarse dos reglas para forzar el número doce.

Si el requisito es mantener sin cambios la semántica de las doce reglas tarifarias, **no se recomienda reemplazar EPM/CHEC por XM**. En ese escenario se debe completar evidencia externa para las fuentes tarifarias o ampliar su alcance con seguimiento documentado de publicaciones.

#### Alternativas de tarifas revisadas

- `td8k-vhq9` (costo unitario): **12.607 filas, solo seis meses de reporte de 2023**. Su metadato incluye `fech_public`, pero la referencia CHEC ya conservada contiene el centinela `1900-01-01` en ese campo. No basta para cartas mensuales ni para oportunidad.
- `4is2-3nif` (tarifas publicadas): **17.806 filas, solo seis meses de reporte de 2023**. Tiene fecha de publicación y nombre del diario; no resuelve la historia temporal del protocolo actual. No se verificó aquí la calidad de todas esas fechas.
- `supers_icnr-l4iw.csv`: **402.500 filas y doce meses**, con problemas de representación de identificadores. Útil como complemento de facturación, no como solución de historia mensual.

#### Decisión recomendada

El mejor candidato nuevo para **investigar demanda con trazabilidad de versiones** es XM/SIMEM. Antes de seleccionarlo definitivamente se requiere un piloto: verificar continuidad mensual completa de un grupo fijo, descargar maestras, contrastar valores y enlazar publicaciones con plazos.

No se encontró una fuente verificada que reúna simultáneamente consumo, historia mensual completa por grupo, las doce reglas tarifarias intactas y evidencia ya suficiente para las ocho dimensiones. Esto es el resultado de esta búsqueda, no una afirmación de inexistencia de datos públicos.

Las conclusiones anteriores del repositorio que afirman que una combinación “no existe en Colombia” deben entenderse como resultados de búsquedas acotadas. Esta evaluación no respalda una afirmación universal de inexistencia.


<a id="doc-8c63814239f9"></a>

## desarrollo_puntos/3.4/README.md

### 3.4 · Decisión sobre la fuente CREG

Corresponde a la actividad 4 del Hito 3: revisar candidatos CREG y documentar las
alternativas o la reformulación del alcance de OE2.

| Evidencia | Contenido |
|---|---|
| [perfiles/creg_electricidad_anexos.json](../Data/gold/outputs/seleccion_fuentes/perfiles/creg_electricidad_anexos.json) | Revisión de anexos eléctricos CREG, hojas, tamaños y hashes. |
| [perfiles/creg_prioridad_perfil.json](../Data/gold/outputs/seleccion_fuentes/perfiles/creg_prioridad_perfil.json) | Perfil del conjunto CREG de gas ek3f-5wn4, descartado para el alcance eléctrico. |
| [Evaluacion_fuente_alternativa_XM.md](REFERENCIA_TECNICA.md#doc-50ab77624282) | Evaluación de demanda XM como alternativa y requisitos de adaptación. |
| [perfiles/evaluacion_candidato_xm.json](../Data/gold/outputs/seleccion_fuentes/perfiles/evaluacion_candidato_xm.json) | Consultas, metadatos y evidencia de la evaluación inicial del candidato XM. |

La explicación de la búsqueda CREG y la propuesta de fuentes ya existentes se conservan
en [REVISION_CREG_ELECTRICIDAD.md](REFERENCIA_TECNICA.md#doc-1e1e212fc147) y
[PROPUESTA_CUATRO_FUENTES.md](REFERENCIA_TECNICA.md#doc-0f3a50ee68a6).

La [ficha del piloto XM](REFERENCIA_TECNICA.md#doc-eab9a734865a) pertenece a 3.2;
su evaluación como alternativa pertenece a este punto. XM es el publicador de su dataset;
su selección no lo convierte en una fuente publicada por CREG. Esta carpeta no registra
una nueva aprobación del director ni una búsqueda adicional en internet.


<a id="doc-6927d6df7ab3"></a>

## desarrollo_puntos/3.5/README.md

### 3.5 · Cartas en cambios logarítmicos

Corresponde a la actividad 5 del Hito 3. Conserva los scripts de cartas y sus salidas,
organizados por fuente.

| Fuente | Script | Resultado |
|---|---|---|
| EPM | [cartas_log_epm.py](../Code/Modeling/cartas/EPM/cartas_log_epm.py) | [cartas_log_epm.csv](../Data/gold/outputs/cartas/EPM/cartas_log_epm.csv) |
| CHEC | [cartas_log_chec.py](../Code/Modeling/cartas/CHEC/cartas_log_chec.py) | [cartas_log_chec.csv](../Data/gold/outputs/cartas/CHEC/cartas_log_chec.csv) |
| SSPD | [cartas_log_sspd.py](../Code/Modeling/cartas/SSPD/cartas_log_sspd.py) | [cartas_log_sspd.csv](../Data/gold/outputs/cartas/SSPD/cartas_log_sspd.csv) |
| XM | [cartas_log_xm.py](../Code/Modeling/cartas/XM/cartas_log_xm.py) | [cartas_log_xm.csv](../Data/gold/outputs/cartas/XM/cartas_log_xm.csv) |

EPM también conserva [revision_cartas_epm.py](../Code/Modeling/cartas/EPM/revision_cartas_epm.py) y su
[tabla de señales](../Data/gold/outputs/cartas/EPM/revision_senales_cartas_epm.csv). La revisión de señales tiene su
propia implementación; moverla no certifica equivalencia con el cálculo principal.

Desde la raíz del proyecto, por ejemplo:

```powershell
python desarrollo_puntos/3.5/EPM/cartas_log_epm.py
```

El script EPM lee la cuarentena de [3.7/EPM](REFERENCIA_TECNICA.md#doc-9d236b840cde).
Las cartas son insumo de la matriz 3.1 y del bootstrap 3.7. Las revisiones que explican
reglas y adaptaciones por fuente permanecen en [3.3](REFERENCIA_TECNICA.md#doc-1daec17adf88).

Esta ubicación identifica la actividad a la que pertenece el material disponible.
No acredita que estén completadas la modificación de rasgos del Isolation Forest ni
las actualizaciones del marco teórico y de la metodología exigidas por el plan.


<a id="doc-2c881ea64a55"></a>

## desarrollo_puntos/3.6/README.md

### 3.6 · Trazabilidad estable entre descargas

Corresponde a la actividad 6 del Hito 3: identificación por contenido, huellas de archivos,
manifiesto y comprobación de reproducibilidad.

- [trazabilidad.py](../Code/Data_Acquisition_and_Understanding/trazabilidad/trazabilidad.py): genera claves estables, manifiesto y copias trazables
  de los hallazgos y alertas históricos de `3.3/insumos_hito2/`.
- [trazabilidad/manifiesto_ejecucion.json](../Data/gold/outputs/trazabilidad/trazabilidad/manifiesto_ejecucion.json):
  manifiesto conservado de la ejecución previa; no se ha sustituido por uno nuevo al moverlo.
- [REPRODUCIBILIDAD_HITO3.md](REFERENCIA_TECNICA.md#doc-cff2689f65ac): evidencia existente y requisito
  pendiente de una segunda descarga independiente.

Las salidas de identidad por fila permanecen en
[fuentes_datos/verificaciones/trazabilidad_filas](REFERENCIA_TECNICA.md#doc-351c00955bb1),
conforme a la organización previa de las verificaciones.

Desde la raíz del proyecto:

```powershell
python desarrollo_puntos/3.6/trazabilidad.py
```

La reorganización no genera descargas, fechas ni hashes nuevos de los datasets. Un
manifiesto de una copia congelada no demuestra por sí solo estabilidad entre descargas.


<a id="doc-cff2689f65ac"></a>

## desarrollo_puntos/3.6/REPRODUCIBILIDAD_HITO3.md

### Reproducibilidad del Hito 3

#### Estado de la primera versión

La primera versión de cada fuente está congelada mediante SHA-256 en
`trazabilidad/manifiesto_ejecucion.json`. El manifiesto registra archivo, tamaño, filas, columnas,
fecha de ejecución y clave de contenido. La matriz, las cartas y el bootstrap se regeneran con
los scripts existentes sin modificar los CSV fuente.

#### Prueba ejecutada

Se ejecutaron consecutivamente:

```bash
python3 desarrollo_puntos/3.1/medir_matriz_oe1.py
python3 desarrollo_puntos/3.7/bootstrap_categorias.py
python3 desarrollo_puntos/3.6/trazabilidad.py
```

La ejecución produce 76 filas de matriz, 105 categorías bootstrap y un manifiesto para cuatro
archivos fuente.

#### Segunda versión requerida

Todavía no se dispone de una segunda descarga real de cada portal. Por tanto, no se declara
reproducibilidad temporal ni estabilidad de las fuentes. Para cerrar este requisito debe guardarse
una segunda versión sin sobrescribir la primera, por ejemplo en `versiones/2026-11-05/`, con su
propio SHA-256 y fecha de descarga.

Si no es posible obtener una segunda descarga, el informe debe declarar que la prueba realizada es
reproducibilidad técnica sobre una versión congelada, no comparación entre descargas.

#### Política de archivos

La política propuesta es UTF-8, encabezado conservado, fin de línea LF y sin modificar el contenido
original. Cualquier conversión debe generar un archivo nuevo y registrar el hash antes y después.
Esta propuesta requiere aprobación para convertirse en política oficial del proyecto.


<a id="doc-30e3a1a159ec"></a>

## desarrollo_puntos/3.7/bootstrap/README.md

### Bootstrap por categoría

El archivo `bootstrap_categorias.csv` calcula la tasa de señales de CART01 y su IC95 % por categoría. Se remuestrean series dentro de cada categoría, sin mezclar fuentes. La semilla es 20261105 y se ejecutan 2000 repeticiones.

La tasa es descriptiva: una señal no equivale automáticamente a un error de datos. Categorías con una sola serie tienen un intervalo degenerado y deben interpretarse con cautela.

La ejecución actual produce 105 categorías: EPM (8), CHEC (4), SSPD (92) y XM (1).
La unidad estadística es la serie de cartas, no cada fila del CSV; por eso no se mezclan observaciones de fuentes, años o categorías distintas. SSPD tiene una categoría de una sola serie y XM también; sus intervalos son necesariamente degenerados.

#### Reproducir

Desde la raíz del repositorio:

```bash
python3 desarrollo_puntos/3.7/bootstrap_categorias.py
```

El script lee las cartas generadas en las carpetas de cada fuente y reemplaza de forma determinista `bootstrap_categorias.csv`, `configuracion.json` y este resumen. La semilla fija permite comparar ejecuciones mientras no cambien las cartas de entrada.


<a id="doc-9d236b840cde"></a>

## desarrollo_puntos/3.7/EPM/README_CUARENTENA.md

### Cuarentena EPM

`cuarentena_registros.csv` contiene las filas apartadas antes de calcular las cartas.

El script de cartas está en [3.5/EPM/cartas_log_epm.py](../Code/Modeling/cartas/EPM/cartas_log_epm.py)
y lee este archivo de cuarentena desde su ubicación en 3.7.
Se construye con `cuarentena.py` a partir de los hallazgos trazables del Hito 2:

- R08: incoherencia entre propiedades.
- R11: posible serial de fecha en un importe.
- R12: magnitud extrema frente a la mediana de la serie.
- R07 con severidad Error: signo fuera del dominio documentado.

La cuarentena no elimina ni corrige valores. `cartas_log_epm.py` excluye cualquier cambio
mensual que toque una fila cuyo `clave_contenido` esté en este archivo. No se interpolan
meses ni se ajustan los límites usando valores de vigilancia.


<a id="doc-fcfdcb7af446"></a>

## desarrollo_puntos/3.7/README.md

### 3.7 · Cuarentena por valor y remuestreo

Corresponde a la actividad 7 del Hito 3.

| Archivo o grupo | Función |
|---|---|
| [EPM/cuarentena.py](../Code/Data_Acquisition_and_Understanding/cuarentena_bootstrap/EPM/cuarentena.py), [cuarentena_registros.csv](../Data/gold/outputs/cuarentena_bootstrap/EPM/cuarentena_registros.csv), [README_CUARENTENA.md](REFERENCIA_TECNICA.md#doc-9d236b840cde) | Materialización y explicación de los registros apartados para las cartas EPM. |
| [cuarentena_fuentes.py](../Code/Data_Acquisition_and_Understanding/cuarentena_bootstrap/cuarentena_fuentes.py) | Generación conservadora de cuarentenas CHEC, SSPD y XM; escribe en las verificaciones de fuentes. |
| [bootstrap_categorias.py](../Code/Data_Acquisition_and_Understanding/cuarentena_bootstrap/bootstrap_categorias.py) | Remuestreo y cálculo de intervalos a partir de las cartas de 3.5. |
| [bootstrap/README.md](REFERENCIA_TECNICA.md#doc-30e3a1a159ec), [resultados](../Data/gold/outputs/cuarentena_bootstrap/bootstrap/bootstrap_categorias.csv), [configuración](../Data/gold/outputs/cuarentena_bootstrap/bootstrap/configuracion.json) | Evidencia y parámetros del bootstrap conservado: 105 grupos, 2.000 repeticiones y semilla fija. |

Desde la raíz del proyecto:

```powershell
python desarrollo_puntos/3.7/EPM/cuarentena.py
python desarrollo_puntos/3.7/bootstrap_categorias.py
```

El material existente remuestrea **series dentro de cada categoría**; el texto del plan
original pide bootstrap **por categoría, no por serie**. La ubicación es correcta por
actividad, pero esa diferencia metodológica requiere revisión y no se resuelve cambiando
carpetas. Tampoco se modifica aquí la severidad de R12 ni la lógica de exclusión de cambios.

Los pendientes estadísticos se mantienen en
[PENDIENTES_APROBACION_HITO3.md](REFERENCIA_TECNICA.md#doc-349c3e6eb49a).


<a id="doc-f1d8ec2447b1"></a>

## desarrollo_puntos/3_documentacion_general/CIERRE_HITO3.md

### Cierre del Hito 3

#### Resultado

El Hito 3 queda documentado y reproducible para las cuatro fuentes seleccionadas. Se entregan
las fichas de caracterización, la matriz OE1, las reglas por fuente, las cartas logarítmicas, la
trazabilidad por fila, la cuarentena y el bootstrap por categoría.

#### Entregables verificables

- [Matriz OE1](REFERENCIA_TECNICA.md#doc-cd000226e09e), [CSV](../Data/gold/outputs/calidad/matriz_oe1.csv) y [YAML](../Data/gold/outputs/calidad/matriz_oe1.yaml): 19 controles × 4 fuentes.
- [Informe de diferencias entre fuentes](REFERENCIA_TECNICA.md#doc-7dec091a7816).
- [Fichas de caracterización](REFERENCIA_TECNICA.md#doc-6d09f59e62b7) para EPM, CHEC, SSPD y XM.
- [Cartas de EPM](REFERENCIA_TECNICA.md#doc-44ac9713606e), [CHEC](REFERENCIA_TECNICA.md#doc-f0cd728e94a3),
  [SSPD](REFERENCIA_TECNICA.md#doc-d9da2f0b37a2) y [XM](REFERENCIA_TECNICA.md#doc-5cd7ac79d74f).
- [Trazabilidad estable](REFERENCIA_TECNICA.md#doc-351c00955bb1), con
  SHA-256, manifiesto de ejecución y claves de contenido.
- [Cuarentena](REFERENCIA_TECNICA.md#doc-9d236b840cde) y verificaciones conservadoras de las demás fuentes.
- [Bootstrap por categoría](REFERENCIA_TECNICA.md#doc-30e3a1a159ec), con 2.000 repeticiones y semilla fija.
- [Evidencia de exactitud y oportunidad](REFERENCIA_TECNICA.md#doc-dfcefa4bff36), con procedimiento,
  fuentes disponibles y plantillas pendientes de diligenciar.
- [Reproducibilidad](REFERENCIA_TECNICA.md#doc-cff2689f65ac), con la primera ejecución verificada y el requisito
  de una segunda versión independiente.

#### Criterio de cierre y límites

El pipeline se puede ejecutar sin editar manualmente los datos fuente y los resultados quedan
asociados a una versión mediante SHA-256. Cada control tiene dimensión, fórmula, denominador,
umbral, estado y nota por fuente.

El cierre no significa que todas las dimensiones hayan alcanzado 100 % ni que toda evidencia sea
definitiva. Persisten estados provisionales, proxies, controles no aplicables y dos controles no
medibles por falta de evidencia. Exactitud necesita contraste documental y oportunidad necesita
evidencia de publicación y plazo; las alertas estadísticas no sustituyen ninguno de los dos.

#### Entrada al Hito 4

El Hito 4 puede comenzar con esta línea base. Sus primeros productos deben ser el scorecard por
fuente y dimensión, la comparación de técnicas bajo el mismo protocolo y el análisis de
sensibilidad. Los resultados provisionales deben conservarse separados de los medidos y no se
deben comparar porcentajes sin revisar población, unidad y aplicabilidad.

Antes de declarar los Hitos 3 y 4 formalmente aprobados, debe diligenciarse
[PENDIENTES_APROBACION_HITO3.md](REFERENCIA_TECNICA.md#doc-349c3e6eb49a). Ese documento concentra las
decisiones que dependen del director, de una fuente de contraste, de una segunda descarga o de
la selección metodológica del Hito 4; no se han presentado como cumplidas.


<a id="doc-b2834637e78b"></a>

## desarrollo_puntos/3_documentacion_general/CONTEXTO_PREVIO_HITO3.md

### Hito 3 · Puntos 1 y 2

Documento de contexto conservado de la organización anterior. Sus estados describen
distintas etapas de trabajo y pueden diferir de documentos posteriores. Para la ubicación
actual de los archivos, consultar el [índice del Hito 3](REFERENCIA_TECNICA.md#doc-393500a1bb5a).

El estado de cierre y la transición al Hito 4 están documentados en [CIERRE_HITO3.md](REFERENCIA_TECNICA.md#doc-f1d8ec2447b1).

| Punto | Entregable | Documento |
|---|---|---|
| 1 | Matriz OE1 con plantilla llena por regla | [`matriz_oe1.md`](REFERENCIA_TECNICA.md#doc-cd000226e09e) |
| 2 | Fichas de caracterización por fuente | [Fichas en desarrollo_puntos/3.2](REFERENCIA_TECNICA.md#doc-6d09f59e62b7) |

Las fichas del punto 2 son condición del punto 1: los umbrales de la matriz se sostienen
sobre el consumidor del dato que allí se declare. Ese bloque sigue pendiente de decisión.

#### Punto 1 · Matriz OE1

El punto 1 tiene una línea base histórica para EPM, CHEC, SSPD (Zonas No Interconectadas) y XM/SIMEM. XM ya cuenta con un adaptador preliminar de demanda; sus resultados son provisionales cuando dependen de catálogos, referencias o plazos externos. No se modificó el código del Hito 2.

Los tres archivos de la matriz incluyen la línea base disponible sobre los datos conservados en `fuentes_datos/datos/`: resultado, estado y nota por control y fuente. XM se mide con reglas adaptadas a demanda y no hereda resultados de SSPD-NR.

#### Archivos

- [Matriz y fichas explicadas](REFERENCIA_TECNICA.md#doc-cd000226e09e): lectura principal, ocho dimensiones, diez tipos de regla y diecinueve indicadores, con el resultado de cada ficha y la sección de línea base.
- [Matriz CSV](../Data/gold/outputs/calidad/matriz_oe1.csv): 76 filas (19 controles × 4 fuentes), legible en Excel con UTF-8 y separador coma; incluye las columnas de resultado.
- [Especificación YAML](../Data/gold/outputs/calidad/matriz_oe1.yaml): definiciones, fórmulas, parámetros, decisiones de medición y bloque `resultado` por fuente. Es documental; no es un motor de reglas ejecutado.
- [Revisión de reglas para XM](REFERENCIA_TECNICA.md#doc-5cd7ac79d74f): significado de R01–R12 y de los siete controles complementarios, con las adaptaciones de demanda.
- [Plantilla de exactitud](../Data/gold/outputs/calidad/plantilla_exactitud.csv): contraste de una muestra con publicaciones verificadas.
- [Plantilla de oportunidad](../Data/gold/outputs/calidad/plantilla_oportunidad.csv): plazos, evidencia temporal e intervalos de disponibilidad.
- [Plantilla de catálogos](../Data/gold/outputs/calidad/plantilla_catalogos.csv): dominios, equivalencias y relaciones con fundamento documental.
- [Script de medición](../Code/Data_Acquisition_and_Understanding/calidad/medir_matriz_oe1.py): calcula el resultado de cada control y lo escribe dentro de los tres archivos anteriores. Reejecutable e idempotente con `python3 desarrollo_puntos/3.1/medir_matriz_oe1.py`; registra el SHA-256 de cada archivo medido.
- [Referencia externa de EXA01](../Data/gold/outputs/calidad/referencia_exa01_chec.json): registros de CHEC en `td8k-vhq9` de Superservicios, con su consulta y fecha de descarga. Permite contrastar exactitud sin depender de una respuesta de la entidad, y hace el contraste reproducible sin red.
- [Trazabilidad estable](REFERENCIA_TECNICA.md#doc-351c00955bb1):
  SHA-256 por archivo, fecha de ejecución, clave de contenido e identificador estable de
  fila para los cuatro datasets; también genera copias trazables de hallazgos y alertas.
- [Bootstrap por categoría](REFERENCIA_TECNICA.md#doc-30e3a1a159ec):
  intervalos de confianza del 95 % para la tasa descriptiva de señales de CART01,
  remuestreando series dentro de cada categoría y sin mezclar fuentes. Incluye la semilla,
  el número de repeticiones y la unidad de remuestreo para reproducibilidad.
- [Informe de diferencias entre fuentes](REFERENCIA_TECNICA.md#doc-7dec091a7816): comparación de
  estructura, aplicabilidad, estados de medición y restricciones de interpretación.
- [Pendientes de aprobación del Hito 3](REFERENCIA_TECNICA.md#doc-349c3e6eb49a): documento único con
  roles, umbrales, catálogos, evidencia externa, reproducibilidad y decisiones estadísticas.
- [Evidencia de exactitud y oportunidad](REFERENCIA_TECNICA.md#doc-dfcefa4bff36): procedimiento,
  evidencia disponible y plantillas para cerrar EXA01 y OPO01.
- [Reproducibilidad del Hito 3](REFERENCIA_TECNICA.md#doc-cff2689f65ac): prueba ejecutada, hashes y requisito
  de una segunda versión independiente.

Las tres plantillas contienen solo cabeceras: están pendientes de diligenciar con evidencia real. No existen referencias o fechas de publicación inventadas.

#### Estado de la medición

La especificación la elaboró el entregable anterior; esta entrega añade el resultado calculado de cada control. El `estado_medicion` de cada fila distingue tres situaciones:

| Estado | Qué significa |
|---|---|
| `medido` | La definición de la matriz se aplica sin supuestos añadidos. El valor no cambia salvo que cambien los datos. |
| `provisional` | Hay valor, pero depende de una decisión documental todavía abierta (catálogo canónico, dominio por concepto, conjunto de medidas requeridas, factor de R12, clave definitiva de CHEC). El valor puede cambiar cuando esa decisión se cierre. |
| `no_medible` | No hay numerador posible con la evidencia disponible. No es falta de definición, es falta de evidencia. |
| `no_aplica` | El concepto del control no existe en el esquema de esa fuente. No es una brecha: es una diferencia estructural, y debe leerse distinto de `no_medible`. |

Cobertura actual: los 19 controles tienen resultado en las cuatro fuentes, aunque algunos son
provisionales, proxies o no aplican por la estructura de la fuente. Las cartas logarítmicas ya
se ejecutaron para EPM, CHEC, SSPD y XM. Exactitud y oportunidad conservan limitaciones de
evidencia externa; oportunidad se reporta mediante proxies explícitos cuando solo existe
cobertura o fecha declarada.

La línea base actual corresponde a EPM, CHEC, SSPD ZNI y XM/SIMEM. SSPD-NR y sus
artefactos permanecen en revisión histórica y no forman parte de la matriz principal.

La cuarta fuente histórica devolvió a **R08, R09 e INT02** un caso donde medirse. En SSPD quedaron `no_aplica` porque su esquema no tiene eje de propiedad ni pares código-nombre; SSPD-NR sí los tenía, y los midió en 92,24 %, 98,60 % y 98,75 % respectivamente. Esos resultados no se deben atribuir a XM: la matriz de XM aún debe construirse con sus reglas de demanda.

Cada valor va acompañado de su numerador, su denominador y una nota que declara los supuestos aplicados. Las cifras se recalculan ejecutando el script; no se transcriben a mano.

#### Qué cambia frente al plan anterior

La oportunidad pasa de excluida a obligatoria por instrucción del profesor. Se mantienen R01–R12 y se añaden INT01/INT02, EXA01, OPO01, MAP01, DEF01 y CART01 para completar la especificación conceptual. No se fuerza una asignación uno a uno entre doce reglas y diez tipos.

Las metas de conformidad del 100 % son propuestas del proyecto; los umbrales de tasas de alertas requieren calibración y no se fijan en cero. Deben validarse antes de declarar cumplimiento. El documento distingue cambios propuestos al código (especialmente R10/R11/R12) de su comportamiento actual.

#### Pendientes residuales después del cierre documental

1. Asignar nombres a los roles y validar los criterios/umbrales con el equipo y dirección.
2. Confirmar catálogos, unidades, semántica, clave candidata y adaptaciones R08/R09 para CHEC.
3. Completar la evidencia de exactitud y oportunidad. EXA01 ya tiene un contraste parcial en CHEC contra otro publicador; falta cubrir EPM, que no tiene traslape temporal con esa referencia, y falta por completo la evidencia de oportunidad en ambas fuentes. «No evaluable» no acredita el requisito de ocho dimensiones.
4. Generar scorecards y análisis de sensibilidad en el Hito 4.
5. Revisar dos propuestas que surgen de medir: cambiar la unidad de observación de R10 de fila a celda por columna, y declarar la política de fin de línea de los CSV para que sus hashes sean verificables.

6. Interpretar el bootstrap por categoría junto con la matriz: el intervalo cuantifica la
   variabilidad entre series, no demuestra por sí solo que una señal sea un error. El grupo
   XM y cualquier categoría con una sola serie tienen un intervalo degenerado; deben reportarse
   como evidencia descriptiva y no como inferencia poblacional.

La actividad cuenta con su entregable documental; la validación metodológica, implementación, medición y cierre del Hito 3 siguen pendientes. El plan detallado en Markdown y esta matriz contienen el alcance actualizado; las imágenes del plan son una representación anterior y no deben usarse para excluir oportunidad.


<a id="doc-349c3e6eb49a"></a>

## desarrollo_puntos/3_documentacion_general/PENDIENTES_APROBACION_HITO3.md

### Pendientes de aprobación — Hitos 3 y 4

Este es el documento único para registrar las decisiones metodológicas y de negocio que todavía requieren aprobación del director o del equipo. Incluye las decisiones heredadas del Hito 3 y las nuevas decisiones del Hito 4. En cada apartado se explica qué se debe decidir y por qué es necesario hacerlo. Los scripts y resultados ya ejecutados no deben modificarse hasta cerrar estas decisiones.

#### Estado general

La matriz OE1, las fichas, las cartas, la trazabilidad, la cuarentena, el bootstrap, las técnicas comparadas, el análisis de sensibilidad, el scorecard provisional y el análisis de niveles/costos ya están implementados. Permanecen pendientes las decisiones que afectan interpretación, umbrales, catálogos, evidencia externa y selección del método final.

#### 1. Roles y gobernanza

| Decisión requerida | Propuesta inicial | Por qué se necesita | Estado |
|---|---|---|---|
| Responsable de reglas de negocio | Persona que conoce tarifas, consumo y categorías | Las reglas dependen del significado del negocio; sin esta persona, un código podría interpretarse de forma incorrecta. | Pendiente de asignar nombre o cargo |
| Responsable de datos | Persona que descarga, versiona y conserva archivos | Alguien debe garantizar que se usa el archivo correcto y que los hashes y versiones se conservan. | Pendiente de asignar nombre o cargo |
| Responsable de métricas y anomalías | Persona que ejecuta cartas, bootstrap y scripts | La medición debe poder repetirse y tener un responsable técnico. | Pendiente de asignar nombre o cargo |
| Responsable de validación | Director o persona que revisa la muestra externa | Las alertas estadísticas no prueban exactitud; alguien debe contrastar los valores con evidencia externa. | Pendiente de confirmar |
| Aprobador final | Director del proyecto | La tesis necesita una autoridad que confirme que los criterios son aceptables metodológicamente. | Pendiente de confirmar |

##### Propuesta de distribución para validar con el profesor

Se propone que el equipo de estudiantes comparta la ejecución técnica y que se asigne una persona
principal para conservar los datos y otra para ejecutar las métricas. El director o profesor actuaría
como aprobador final. El responsable de reglas de negocio y el responsable de validación podrían ser
el director, un experto del sector energético o una persona que el equipo designe formalmente.

Esta distribución es una propuesta de trabajo y no supone que exista actualmente un experto externo
ni que una persona haya aceptado formalmente un rol. Una misma persona podría asumir más de un rol si
el profesor lo considera adecuado, siempre que quede registrado quién responde por cada actividad.

| Rol propuesto | Responsable sugerido | Actividades principales | Confirmación solicitada |
|---|---|---|---|
| Reglas de negocio | Director, experto energético o integrante designado | Validar significados, unidades, categorías, rangos y reglas específicas de las fuentes | Confirmar quién tiene autoridad para aprobar la interpretación del negocio |
| Datos | Integrante del equipo | Descargar, conservar, versionar y verificar los datasets mediante SHA-256 | Confirmar quién custodiará los archivos y evidencias |
| Métricas y anomalías | Integrante técnico del equipo | Ejecutar cartas, bootstrap, modelos, métricas y verificadores | Confirmar quién será responsable de las ejecuciones técnicas |
| Validación | Director, experto energético o integrante designado | Contrastar alertas con publicaciones y fuentes externas | Confirmar quién revisará y aceptará la evidencia externa |
| Aprobación final | Director o profesor de tesis | Aprobar umbrales, métodos, catálogos, alcance y decisiones metodológicas | Confirmar que el director ejercerá esta función |

La tabla muestra una distribución sugerida, no una asignación definitiva. Los nombres o cargos se
completarán únicamente después de la confirmación del profesor.

##### Preguntas para el profesor

1. ¿Está de acuerdo con estos cinco roles y con la distribución propuesta?
2. ¿Una misma persona puede asumir simultáneamente los roles de responsable de datos, métricas,
   reglas de negocio o validación?
3. ¿Es necesario registrar nombres propios o es suficiente indicar el cargo o la responsabilidad?
4. ¿Confirma que el director será el aprobador final de umbrales, métodos, catálogos y alcance?

**Estado:** propuesta pendiente de revisión y aprobación. No se deben inventar nombres ni declarar
un experto externo hasta contar con una confirmación explícita.

#### 2. Umbrales y severidad

| Grupo | Controles | Propuesta | Por qué se necesita | Estado |
|---|---|---|---|---|
| Integridad mínima | R01–R04, R07, INT01, INT02, MAP01 | Meta de 100 % | Estos controles representan condiciones básicas del archivo; una tolerancia podría ocultar filas imposibles de relacionar o interpretar. | Pendiente de aprobación |
| Completitud y consistencia | R05, R06, R08–R10, DEF01 | Meta de 100 %, reportada como tasa continua; advertencia cuando corresponda | El equipo debe decidir qué faltantes o variantes son aceptables para el uso energético previsto. | Pendiente de aprobación |
| Exactitud | EXA01 | 100 % en la muestra validada | Un porcentaje de coincidencia solo tiene sentido si se define la fuente de verdad, la muestra y la tolerancia de redondeo. | Pendiente de aprobar muestra y fuente |
| Oportunidad | OPO01 | Medir retraso publicación-descarga; usar proxy si no existe plazo publicado | Sin plazo esperado no se puede saber si una publicación fue tardía; el proxy debe reconocerse como indirecto. | Pendiente de aprobar plazo/proxy |
| Estadística | R11, R12, CART01 | Advertencia; no convertir señal automáticamente en error | Una señal identifica un comportamiento atípico, pero puede corresponder a un cambio real de tarifa o demanda. | Pendiente de calibración |

El 100 % es una meta del proyecto, no un umbral impuesto por DAMA-DMBOK ni ISO. Si el director aprueba tolerancias diferentes, deben registrarse junto con su justificación.

##### Propuesta resumida para aprobar

| Tipo de control | Propuesta | Interpretación del resultado | Decisión solicitada |
|---|---|---|---|
| Integridad mínima | 100 % | Un incumplimiento se reporta como error porque impide interpretar o relacionar correctamente el dato | Confirmar si la meta debe ser estrictamente 100 % |
| Completitud y consistencia | Meta de 100 %, con tasa continua y advertencia | Un valor menor muestra una desviación que debe analizarse; no se elimina automáticamente el registro | Confirmar qué porcentaje o casos son aceptables como advertencia |
| Exactitud | 100 % de coincidencia en la muestra validada, con tolerancia de redondeo previamente definida | Solo se evalúan registros contrastados contra una fuente oficial aprobada | Aprobar muestra, fuente de verdad y tolerancia numérica |
| Oportunidad | Medir el retraso real cuando exista fecha y plazo; utilizar `provisional_proxy` cuando no exista plazo publicado | Un proxy no demuestra el plazo real, solo aproxima la disponibilidad | Aprobar el plazo esperado o aceptar explícitamente el proxy |
| Señales estadísticas | Advertencia, nunca error automático | Una alerta puede representar un cambio real de tarifa, demanda o regulación | Confirmar que toda alerta requiere revisión antes de clasificarse como error |

##### Preguntas para el profesor sobre los umbrales

1. ¿Aprueba una meta del 100 % para integridad, completitud y consistencia, o propone tolerancias?
2. ¿Qué nivel de incumplimiento debe generar advertencia y cuál debe considerarse error?
3. ¿Aprueba la muestra de 30 registros por fuente para exactitud?
4. ¿Qué fuente oficial y qué tolerancia de redondeo deben utilizarse para validar importes?
5. ¿Acepta que la oportunidad se reporte como `provisional_proxy` cuando el portal no publique un plazo?
6. ¿Confirma que las alertas estadísticas no se convierten automáticamente en errores de calidad?

**Estado:** propuesta pendiente de revisión y aprobación. Los porcentajes calculados actualmente son
resultados de medición; no constituyen por sí mismos umbrales aprobados.

#### 3. Catálogos y semántica de CHEC

Se debe aprobar el significado de categorías, niveles, unidades y conceptos tarifarios; el catálogo canónico y las equivalencias; la unidad de cada importe y el tratamiento de valores negativos; la clave candidata para identificar una tarifa por período; la aplicación definitiva de R08 y R09; y el responsable de mantener los catálogos.

**Por qué:** CHEC contiene códigos cuyo significado no está completamente explícito en el archivo. Si se interpretan sin catálogo, se podrían marcar como errores valores válidos o comparar conceptos que no tienen la misma unidad. La clave también debe aprobarse porque existen multiplicidades y no es seguro eliminar filas repetidas automáticamente.

**Estado:** análisis técnico en [DECISION_CATALOGOS_CHEC.md](REFERENCIA_TECNICA.md#doc-cd7e104c7bc9); aprobación documental pendiente.

##### Propuesta de decisiones para CHEC

| Aspecto | Propuesta técnica | Por qué es necesario | Confirmación solicitada |
|---|---|---|---|
| Categorías y códigos | Mantener los valores originales y construir un catálogo canónico versionado | Evita modificar la fuente y permite distinguir variantes de escritura | Confirmar qué equivalencias representan el mismo concepto |
| Niveles tarifarios | Conservar los niveles 1–4 como categorías independientes | Agruparlos podría mezclar tarifas con comportamientos y unidades diferentes | Confirmar que los niveles 1–4 no deben combinarse |
| Unidades | Registrar explícitamente la unidad de cada componente e importe antes de comparar | Dos valores numéricamente similares pueden estar expresados en unidades distintas | Aprobar el catálogo de unidades y conversiones permitidas |
| Valores negativos | No marcar automáticamente valores negativos; revisar su significado por concepto, especialmente restricciones | Un valor negativo puede ser válido según el componente tarifario | Confirmar qué conceptos admiten valores negativos |
| Clave de tarifa | Usar una clave compuesta por período, categoría, nivel y concepto, sin eliminar duplicados automáticamente | Las multiplicidades pueden representar registros distintos o conflictos que requieren revisión | Aprobar la clave candidata y la política frente a duplicados |
| R08 y R09 | Aplicar las reglas solo cuando exista una matriz de aplicabilidad documentada | Sin conocer qué campos aplican a cada nivel, un supuesto puede generar falsos errores | Confirmar la matriz de aplicabilidad y la interpretación de ceros |
| Mantenimiento | Asignar un responsable para versionar el catálogo cuando cambie la fuente | Un catálogo sin control de versiones puede cambiar los resultados históricos | Confirmar responsable y frecuencia de actualización |

##### Preguntas para el profesor sobre CHEC

1. ¿Aprueba construir un catálogo canónico sin alterar los valores originales?
2. ¿Confirma que los niveles 1–4 deben analizarse por separado?
3. ¿Quién puede validar el significado de los códigos, unidades y conceptos tarifarios?
4. ¿Qué conceptos pueden tener valores negativos válidos?
5. ¿Aprueba la clave compuesta propuesta y la decisión de no eliminar duplicados automáticamente?
6. ¿Confirma que R08 y R09 deben quedar como provisionales hasta aprobar la matriz de aplicabilidad?
7. ¿Quién será responsable de mantener y aprobar futuras versiones del catálogo?

**Estado:** propuesta técnica pendiente de validación semántica y aprobación documental. Hasta entonces,
las equivalencias y reglas CHEC deben presentarse como provisionales.

#### 4. Evidencia de exactitud

Se propone contrastar 30 registros por fuente, estratificados por período y categoría, contra una fuente oficial independiente o una publicación oficial del mismo período. Debe aprobarse la fuente, el tamaño y método de selección, los campos comparados, la tolerancia numérica y el tratamiento de diferencias por redondeo o unidad.

**Por qué:** una carta de control o una regla de formato solo muestra coherencia interna. EXA01 necesita una fuente externa que permita afirmar si el valor publicado coincide con una referencia confiable. Sin aprobar la muestra y la tolerancia, el porcentaje de exactitud no sería reproducible.

**Estado:** procedimiento y plantilla en [EVIDENCIA_EXACTITUD_OPORTUNIDAD.md](REFERENCIA_TECNICA.md#doc-dfcefa4bff36); la muestra y la fuente no están aprobadas.

##### Propuesta para evaluar exactitud

| Elemento | Propuesta | Por qué es necesario | Confirmación solicitada |
|---|---|---|---|
| Fuente de contraste | Publicación oficial del mismo período; usar una fuente independiente cuando exista | Permite comprobar que el valor del dataset coincide con un documento verificable | Aprobar la fuente oficial y aclarar cuándo se considera independiente |
| Tamaño de muestra | 30 registros por fuente, estratificados por período y categoría | Evita validar solo los casos más fáciles o más recientes | Confirmar tamaño y método de selección |
| Campos comparados | Período, categoría, unidad y valores monetarios o de consumo aplicables | La comparación debe hacerse entre conceptos equivalentes | Aprobar las columnas obligatorias por fuente |
| Tolerancia numérica | Definirla antes de comparar, según precisión publicada y redondeo; propuesta inicial: 0,01 en importes con dos decimales | Una diferencia de redondeo no debe clasificarse como error | Aprobar tolerancia y regla de redondeo |
| Diferencias | Separar diferencia por redondeo, unidad, transcripción o valor no coincidente | No todas las diferencias tienen la misma causa ni gravedad | Aprobar categorías de diferencia y tratamiento |
| Evidencia | Conservar URL, fecha de consulta, PDF/archivo, SHA-256 y transcripción | Permite repetir la revisión y demostrar qué documento se utilizó | Confirmar los elementos mínimos de la evidencia |
| Resultado | Reportar porcentaje de coincidencia de la muestra como EXA01, no como exactitud de todo el dataset | Una muestra no permite afirmar que todas las filas sean correctas | Confirmar el alcance limitado del indicador |

La validación propuesta mide **concordancia documental**. No demuestra por sí sola que la tarifa sea
económicamente correcta ni reemplaza una auditoría del publicador. Si solo se dispone de una publicación
del mismo proveedor, el resultado debe describirse como coincidencia con la publicación oficial y no como
validación completamente independiente.

##### Preguntas para el profesor sobre exactitud

1. ¿Aprueba utilizar 30 registros por fuente con selección estratificada?
2. ¿Qué fuente debe considerarse referencia oficial para cada dataset?
3. ¿Cuándo debe exigirse una fuente independiente y cuándo basta una publicación oficial del mismo proveedor?
4. ¿Aprueba la tolerancia inicial de 0,01 o establece otra según la unidad y precisión de cada fuente?
5. ¿Aprueba reportar EXA01 como concordancia de la muestra, sin generalizarlo a todo el dataset?
6. ¿Qué tratamiento debe darse a diferencias causadas por redondeo, unidad, transcripción o actualización?

**Estado:** procedimiento definido, pero fuente, muestra, tolerancia y alcance requieren aprobación.

#### 5. Evidencia de oportunidad

Se propone registrar fecha de publicación o actualización, fecha de descarga, frecuencia esperada, retraso calculado y evidencia de la URL o metadato. Si el publicador no declara un plazo esperado, debe aprobarse el uso de un proxy y reportarse como `provisional_proxy`.

**Por qué:** la fecha de descarga no indica cuándo el dato estuvo disponible para los usuarios. Se necesita un plazo esperado para distinguir una publicación oportuna de una tardía. Si el portal no publica ese plazo, el director debe aceptar expresamente una medición indirecta.

**Estado:** procedimiento en [EVIDENCIA_EXACTITUD_OPORTUNIDAD.md](REFERENCIA_TECNICA.md#doc-dfcefa4bff36); pendiente de aprobar el plazo o proxy por fuente.

##### Propuesta para evaluar oportunidad

| Elemento | Propuesta | Por qué es necesario | Confirmación solicitada |
|---|---|---|---|
| Fecha de publicación | Usar la fecha declarada por el portal o el publicador | El período del dato no equivale a la fecha en que se publicó | Confirmar qué metadato tiene prioridad |
| Fecha de descarga | Registrar fecha, hora y zona horaria de cada captura | Permite calcular el retraso observado y repetir la medición | Aprobar formato y zona horaria |
| Plazo esperado | Usar el plazo oficial del publicador o la obligación aplicable | Sin plazo no se puede clasificar puntualidad o retraso | Definir plazo por fuente |
| Proxy | Usar disponibilidad del período como `provisional_proxy` cuando no exista plazo | Es una aproximación y no una medición directa del retraso | Aceptar o rechazar el proxy por fuente |
| Evidencia | Conservar URL, metadatos, fecha de consulta y SHA-256 | Permite demostrar qué estaba disponible en la fecha observada | Aprobar elementos mínimos |
| Interpretación | Reportar “medible”, “provisional_proxy” o “no medible” | Evita presentar una aproximación como resultado definitivo | Confirmar las categorías de estado |

##### Preguntas para el profesor sobre oportunidad

1. ¿Qué plazo esperado debe utilizarse para cada fuente?
2. ¿Qué fecha del portal debe considerarse fecha de publicación?
3. ¿Acepta el uso de `provisional_proxy` cuando no exista un plazo publicado?
4. ¿Aprueba registrar fecha, hora, zona horaria, URL y SHA-256 como evidencia mínima?
5. ¿Confirma que la ausencia de evidencia debe clasificarse como “no medible” y no como retraso?

**Estado:** propuesta pendiente de aprobación del plazo, proxy y categorías de resultado.

#### 6. Reproducibilidad y versiones

El criterio de cierre solicita dos descargas. Debe aprobarse obtener una segunda descarga real del portal o usar una segunda copia congelada con fecha y SHA-256 diferentes, declarando que demuestra reproducibilidad técnica pero no estabilidad temporal del portal. También debe aprobarse la política de codificación y fin de línea de los CSV.

**Por qué:** una sola descarga demuestra que el código funciona sobre un archivo, pero no que los resultados se mantienen entre versiones. La segunda versión permite identificar cambios del portal y la política de codificación evita que el mismo archivo produzca hashes diferentes por razones técnicas.

**Estado:** procedimiento en [REPRODUCIBILIDAD_HITO3.md](REFERENCIA_TECNICA.md#doc-cff2689f65ac); segunda versión y política de fin de línea pendientes.

##### Propuesta para reproducibilidad

| Elemento | Propuesta | Por qué es necesario | Confirmación solicitada |
|---|---|---|---|
| Segunda versión | Obtener una segunda descarga real o conservar una segunda copia congelada | Permite comparar versiones y detectar cambios del portal | Aprobar cuál de las dos alternativas se usará |
| Identificación | Registrar fecha de captura, URL, tamaño y SHA-256 | Permite distinguir inequívocamente ambas versiones | Confirmar metadatos obligatorios |
| Codificación | Normalizar lectura a UTF-8 y conservar el archivo original | Evita errores por acentos y separadores sin alterar la evidencia | Aprobar política de codificación |
| Fin de línea | Registrar si el archivo usa LF o CRLF y no cambiarlo silenciosamente | El contenido puede ser igual aunque el hash cambie por formato | Aprobar si se compara el archivo crudo o una representación normalizada |
| Comparación | Reejecutar los mismos controles sobre ambas versiones | Permite distinguir cambios del dato de cambios del código | Confirmar controles mínimos a repetir |
| Conclusión | Declarar “reproducibilidad técnica” sin afirmar estabilidad del portal | Dos copias no demuestran que futuras descargas sean idénticas | Aprobar el alcance de la conclusión |

##### Preguntas para el profesor sobre reproducibilidad

1. ¿Acepta una segunda copia congelada si no es posible obtener una segunda descarga del portal?
2. ¿Qué metadatos deben acompañar cada versión?
3. ¿Debe conservarse y compararse el archivo crudo o una versión normalizada?
4. ¿Qué controles deben repetirse obligatoriamente sobre la segunda versión?
5. ¿Aprueba declarar reproducibilidad técnica sin afirmar estabilidad temporal del portal?

**Estado:** procedimiento definido; segunda versión, codificación y alcance de la conclusión pendientes.

#### 7. Decisiones estadísticas pendientes

- Confirmar que el bootstrap remuestrea series dentro de cada categoría y no filas individuales.
- Aceptar que XM y una categoría de SSPD tienen intervalos degenerados por contar con una sola serie.
- Confirmar que R12 y CART01 se interpretan como advertencias hasta contar con calibración de negocio o evidencia histórica suficiente.
- Confirmar si R10 seguirá medido por fila o se cambiará a celda por columna.

**Estado:** propuesta documentada; aprobación metodológica pendiente.

**Por qué:** estas decisiones cambian la interpretación de las cartas y del bootstrap. Definir la unidad de remuestreo, el tratamiento del MAD cero y la regla R12 evita que se comparen resultados generados con criterios diferentes.

##### Propuesta estadística para aprobar

| Decisión | Propuesta | Por qué es necesario | Confirmación solicitada |
|---|---|---|---|
| Bootstrap | Remuestrear series dentro de cada fuente y categoría, no filas individuales | Las filas no son observaciones independientes y mezclar fuentes distorsiona el intervalo | Aprobar la serie como unidad de remuestreo |
| XM y categorías unitarias | Reportar intervalo degenerado y estado descriptivo/no interpretable | Una sola serie no permite estimar variabilidad entre series | Confirmar que no se inventarán intervalos |
| R12 y CART01 | Mantenerlos como advertencias hasta calibración o evidencia histórica | Una señal estadística no equivale automáticamente a un error | Confirmar que no generan error automático |
| R10 | Mantener medición por fila y documentar la limitación; evaluar celda/columna como sensibilidad | Cambiar el denominador modifica el resultado de completitud | Elegir unidad principal y sensibilidad |
| MAD cero | Mantener regla conservadora sin inventar escala | Una escala arbitraria puede crear señales artificiales | Confirmar señal, exclusión o alternativa |

##### Preguntas para el profesor sobre decisiones estadísticas

1. ¿Aprueba remuestrear series dentro de cada categoría?
2. ¿Acepta reportar XM y categorías unitarias como no interpretables?
3. ¿Confirma que R12 y CART01 serán advertencias y no errores automáticos?
4. ¿Prefiere R10 por fila, por celda/columna o ambos como análisis principal y sensibilidad?
5. ¿Aprueba el tratamiento conservador del MAD igual a cero?

**Estado:** propuesta estadística pendiente de aprobación metodológica.

#### 8. Decisiones adicionales del Hito 4

| Decisión requerida | Propuesta o estado actual | Por qué se necesita | Qué debe confirmar el director |
|---|---|---|---|
| Valor X de la regla sistémica | Se propone `25 %` como valor de trabajo; tres meses no permiten un valor único | X decide cuándo muchas alertas se consideran un fenómeno colectivo; cambiarlo puede reclasificar meses completos. | Aceptar 25 %, elegir otro valor o mantener la regla como exploratoria |
| Prevalencia para precisión y F1 | Se reportan escenarios de 1 %, 5 % y 10 %; no se elige uno como verdad | La precisión depende de cuántos errores se supone que existen; elegir una prevalencia sin justificación puede exagerar o minimizar el resultado. | Decidir si se presenta un escenario principal o todos como sensibilidad |
| Método principal | Se comparan IMR, Z robusto, Isolation Forest, LOF, KNN y R12 | La tesis debe explicar si propone un método principal o un conjunto de métodos complementarios. | Elegir método principal o declarar que el framework conserva varios métodos |
| Etiquetas canónicas de EPM | Equivalencias aprobadas internamente; `EPM_canonicas` es sensibilidad | Las etiquetas fragmentan las series; unirlas cambia el número de series y puede cambiar las alertas. | Confirmar si se aceptan como catálogo oficial y si se repiten 4.1/4.2 |
| MAD igual a cero | Se conserva una regla conservadora: no se inventa escala | Si todos los cambios de referencia son iguales, el MAD es cero y cualquier solución arbitraria alteraría las señales. | Confirmar este tratamiento o definir una alternativa |
| LOF en CHEC | Queda degenerado por duplicados exactos | LOF mide densidad; los duplicados pueden hacer que la densidad deje de representar rareza real. | Aprobar deduplicación, ajuste de vecinos o exclusión justificada |
| Extended Isolation Forest | No implementado; el plan lo dejaba condicionado al tiempo | Se debe evitar que la ausencia de una técnica se interprete como un incumplimiento oculto. | Confirmar que se excluye del alcance final |
| Scorecard 4.5 | Generado para 4 fuentes × 8 dimensiones, pero permanece provisional | El scorecard resume resultados que dependen de umbrales y evidencia aún no aprobados. | Aprobar umbrales y evidencia para convertirlo en definitivo |
| Resultados 4.6 | Niveles explícitos para EPM/CHEC; SSPD y XM quedan `No_aplica` | Forzar una clasificación de nivel donde no existe produciría una comparación artificial. | Aceptar esta delimitación y evitar equivalencias no sustentadas |
| Evidencia regulatoria | Falta lectura completa de CREG 015/2018, 152/2020, 003/2021 y resoluciones particulares de EPM | Una alerta estadística no demuestra una causa regulatoria; se necesita respaldo documental para afirmarlo. | Confirmar alcance documental y si la consulta formal queda para Hito 6 |
| Incorporación en la tesis | El plan exige actualizar los apartados 3.1.5 y 5.6.4 del anteproyecto/metodología; el repositorio contiene la evidencia técnica, pero no el documento oficial editable de la tesis | La evidencia implementada debe reflejarse en el texto que se entregará y sustentará, sin afirmar como aprobado lo que sigue provisional. | Indicar el documento y responsable que integrará el texto, y aprobar su versión final |

Los resultados de 4.2–4.6 no deben presentarse como aprobación de un umbral, método o causa
regulatoria. Son evidencia para tomar estas decisiones.

##### Preguntas integrales sobre el Hito 4

1. ¿Aprueba `X = 25 %` como valor de trabajo o prefiere mantener la regla exploratoria?
2. ¿Debe presentarse una prevalencia principal para precisión/F1 o todos los escenarios como sensibilidad?
3. ¿El framework tendrá un método principal o conservará varios métodos complementarios?
4. ¿Se aceptan las etiquetas `EPM_canonicas` como catálogo oficial o solo como sensibilidad?
5. ¿Se mantiene la regla conservadora de MAD cero?
6. ¿Se excluye Extended Isolation Forest del alcance final?
7. ¿Cómo debe tratarse LOF cuando queda degenerado por duplicados?
8. ¿Se aprueba convertir el scorecard 4.5 en definitivo después de aprobar umbrales y evidencias?
9. ¿Se acepta que SSPD y XM queden como `No_aplica` en el análisis por nivel de 4.6?
10. ¿Qué evidencia regulatoria debe completarse y qué parte se deja para el Hito 6?
11. ¿Quién integrará las decisiones aprobadas en el documento oficial de la tesis?

**Estado:** decisiones del Hito 4 pendientes de confirmación metodológica, documental y de alcance.

#### Registro de aprobación

| Campo | Valor |
|---|---|
| Fecha | Pendiente |
| Director o aprobador | Pendiente |
| Participantes | Pendiente |
| Decisiones aceptadas | Pendiente |
| Cambios solicitados | Pendiente |
| Versión aprobada de la matriz | Pendiente |
| Observaciones | Pendiente |

#### Texto para enviar al director

> Consolidamos en un único documento las decisiones pendientes de los Hitos 3 y 4: responsables, umbrales, catálogos CHEC, evidencia de exactitud y oportunidad, reproducibilidad, método principal, valor X, prevalencia, scorecard y alcance de niveles. Solicitamos confirmar o ajustar cada propuesta y registrar la versión aprobada de la matriz OE1 y del protocolo del Hito 4.


<a id="doc-bfabfa5b4a96"></a>

## desarrollo_puntos/3_documentacion_general/plan_hitos_3-6_detallado.md

### Plan de cierre de brechas · Hitos 3 a 6 (versión detallada)

Trabajo de grado *Framework automatizado para la evaluación de la calidad de datos en registros administrativos del sector energético en Colombia* (Grupo 03; dirección del trabajo).

Sin fechas: la secuencia es la propuesta y el calendario lo fija el director con el programa. Líderes según el reparto del cronograma del anteproyecto (responsable de datos; responsable de métricas y anomalías; responsable de reglas de negocio).

#### Brechas del Hito 2 (revisión del 23 de octubre de 2026, código ejecutado y cifras reproducidas)

- Una sola fuente (EPM)
- Un modelo, sin sensibilidad
- Sin artefacto ni tablero
- Nada confirmado con la entidad
- Hipótesis vs. diseño sin resolver
- OE1 sin métricas definidas

#### Hito 3 · Replicar y formalizar (OE1, OE2) · Lidera: responsable de datos

*Cierra: una sola fuente · trazabilidad por posición · cartas fuera del anteproyecto · OE1 sin entregable*

##### Actividades

1. **Matriz dimensión → métrica → indicador → regla (OE1).**
   - Ocho dimensiones de DAMA-DMBOK2 (2017), cap. 13, obligatorias para EPM y CHEC. Clasificar R01–R12 en la taxonomía de diez tipos; no confundir tipos con número de reglas.
   - Plantilla por indicador: población, numerador, denominador, fórmula como cociente, unidad, umbral y fundamento, severidad, frecuencia, responsable, tendencia y aplicabilidad por fuente.
   - Incluir integridad estructural/referencial y razonabilidad (cartas). **Oportunidad no se excluye**: requiere evidencia de disponibilidad real y plazo esperado. Exactitud requiere contraste documental; las alertas no la sustituyen. Relación conceptual y delimitada con ISO/IEC 25012.
   - Entregable documental del punto 1: [matriz y fichas OE1](REFERENCIA_TECNICA.md#doc-cd000226e09e), [YAML](../Data/gold/outputs/calidad/matriz_oe1.yaml) y [CSV por fuente](../Data/gold/outputs/calidad/matriz_oe1.csv). Incluye R01–R12 y siete controles complementarios. Umbrales propuestos, catálogos y evidencia externa pendientes de validación; no se declara medición de las ocho dimensiones ni cierre del Hito 3.
2. **Ficha de caracterización por fuente (OE2).**
   - EPM sfcd-b3ey: 3.623 filas, 12 columnas, dic-2016 a dic-2021; 202 series posibles, 83 con 49 meses o más.
   - Superservicios vfjy-6fka: 5.396 filas, 16 columnas, 8 períodos. Consumidores del dato, datos críticos, unidades y significado de Rango de Consumo (2.143 ausentes).
3. **Replicar el pipeline en Superservicios.**
   - Reglas transversales R01 a R11 y perfilamiento; las cartas no aplican con 8 períodos y se documenta.
   - Informe de diferencias: qué reglas y umbrales cambian y qué dimensiones quedan sin cubrir en cada fuente.
4. **Decidir la fuente CREG.**
   - Buscar en datos.gov.co un conjunto de la CREG con series mensuales de 48 meses o más. Si no existe, reformular OE2 por escrito: fuentes abiertas del sector con la CREG como referencia regulatoria.
5. **Cartas en cambios logarítmicos y formalizadas.**
   - Sustituir la diferencia absoluta por la diferencia de logaritmos en la carta I, la carta MR y los rasgos del Isolation Forest; recalcular límites.
   - Marco teórico 3.1.5: Jones-Farmer et al. (2014) y DMBOK2 cap. 13, técnica de control estadístico de procesos. Metodología 5.6.4: cartas como método estadístico clásico en lugar de Z-score.
6. **Trazabilidad estable entre descargas.**
   - Descarga por API con identificador de fila; hash SHA-256 y fecha de cada descarga; clave de contenido (categoría, fecha, columna) en hallazgos y alertas.
   - Motivo: los registros 2047, 3131, 3133 y 2348 de la diapositiva 7 cambian de posición en otra descarga del portal.
7. **Cuarentena por valor y remuestreo correcto.**
   - La cuarentena entra en el cálculo de límites: se excluyen los cambios que tocan un valor en cuarentena, sin interpolar. Hoy solo marca la serie como sucia.
   - Bootstrap por categoría (23 del Nivel I y 5 de otros niveles), no por serie. R12 pasa de Error a Advertencia hasta confirmación.

##### Insumos y fundamento

- 03_hallazgos.csv y 05_alertas_imr_reales.csv
- 08_copia_preparada.csv
- Resumen DAMA: secciones 2, 3 y 4
- Anteproyecto: 3.1.5, 5.6.4, 5.8
- Retro de junio: observaciones 5 y 7

##### Entregables

- Notebook replicado en las dos fuentes
- Informe de diferencias entre fuentes
- Matriz OE1 con plantilla llena por regla
- Fichas de caracterización
- Anteproyecto actualizado

##### Criterio de cierre

El pipeline corre sin cambios manuales en las dos fuentes y da los mismos hallazgos con dos descargas distintas. Cada regla tiene dimensión, tipo, fórmula y umbral. El anteproyecto ya nombra las cartas.

##### Riesgo y mitigación

Superservicios tiene 8 períodos: allí solo reglas y métodos transversales. Si la CREG no tiene series largas, la replicación de cartas queda solo en EPM y se declara como limitación.

#### Hito 4 · Comparar con protocolo (OE3, OE4) · Lidera: responsable de métricas y anomalías

*Cierra: un solo modelo · sin sensibilidad · sin precisión ni F1 · n efectivo sobreestimado*

##### Actividades

1. **Técnicas adicionales con el mismo protocolo.**
   - Z-score robusto (mediana y MAD) sobre cambios log como línea base del anteproyecto; LOF o KNN sobre los cuatro rasgos del Isolation Forest; Extended IF si el tiempo alcanza.
   - Entrenamiento solo en referencia, evaluación en vigilancia, umbral por validación cruzada a tasa de alerta igualada, como ya se hace con IF.
2. **Análisis de sensibilidad.**
   - Ventana de referencia de 24, 36 y 48 cambios; constantes 2,66 y 3,267 frente a 3 sigma con MAD; percentil 99 y 99,5; factor de R12 en 5, 10 y 20.
   - Ventana de detección t frente a t y t+1; efecto de la regla de alerta sistémica sobre la tasa de alerta.
3. **Métricas completas y honestas.**
   - Precisión, recall y F1 a tasa de alerta igualada; curvas de detección contra tasa de alerta por método.
   - Reportar pruebas por tipo (hoy entre 760 y 1.540) y meses distintos sorteados (13 de 23 en promedio); sortear sin reemplazo.
4. **Regla de alerta sistémica.**
   - Si más de X % de las series alertan en el mismo mes, se clasifica como cambio regulatorio y no como error de dato; calibrar X con feb-2020 (51 de 83), jul-2020 (24) y jul-2021 (18).
   - Contrastar con resoluciones CREG y publicaciones tarifarias de EPM de esos meses.
5. **Scorecard por dimensión (OE1 en resultados).**
   - Calcular cada indicador de la matriz en ambas fuentes; tabla única con umbral y estado, como pide DMBOK2 para el reporte de calidad.
6. **Resultados por nivel y costo de cómputo.**
   - Separar Nivel I (69 series casi colineales, razones medianas 0,964 y 0,928) de los niveles II a IV (14 series); tiempo de cómputo por etapa y por fuente.

##### Insumos y fundamento

- 06_experimento_inyeccion.csv
- 11_puntajes_limpios_por_serie.csv
- 07_deteccion_por_tipo.csv
- Resumen DAMA: sección 4 (métricas)
- Anteproyecto: 5.6.5 y 5.6.6

##### Entregables

- Tabla comparativa con IC 95 % por técnica y tipo de error
- Figuras de sensibilidad
- Catálogo de alertas sistémicas
- Scorecard por fuente y dimensión
- Sección preliminar de resultados

##### Criterio de cierre

Toda técnica pasó por el mismo protocolo y los mismos errores. Las conclusiones llevan intervalo. La sensibilidad está reportada. El scorecard existe en las dos fuentes.

##### Riesgo y mitigación

Fuera del Nivel I hay 14 series: las conclusiones por nivel se presentan con cautela. La regla sistémica puede ocultar errores masivos reales; dejarlo como limitación.

#### Hito 5 · Construir el artefacto (OE3) · Lidera: responsable de reglas de negocio

*Cierra: no existe el artefacto prometido (paquete, contenedor, tablero) · guion de 1.171 líneas sin dependencias fijadas*

##### Actividades

1. **Paquete Python por componentes.**
   - Módulos cargar, perfilar, reglas, series, cartas, anomalías, evaluar y reportar; sin variables globales compartidas entre partes (hoy df, resumen y meses se redefinen entre el Hito 1 y el 2).
2. **Reglas en configuración, no en código.**
   - Archivo YAML con id, dimensión, tipo, severidad, fórmula, umbral y referencia regulatoria por regla; el motor las lee y las registra en la bitácora.
3. **Línea de comandos y salidas.**
   - descargar → evaluar → reportar; salidas CSV y JSON con metadatos de ejecución: hash, fecha, versión del paquete y semilla.
4. **Reproducibilidad computacional.**
   - pyproject con Poetry y versiones fijadas de pandas, scikit-learn, statsmodels y matplotlib; Dockerfile; pruebas automáticas con un conjunto pequeño y errores inyectados conocidos.
5. **Tablero de monitoreo.**
   - Power BI sobre las salidas: scorecard por dimensión, alertas por fuente y mes, bitácora de incidentes con estado; limitado a las salidas de 5.9.2. Exportar también el scorecard en CSV.
6. **Documentación del artefacto.**
   - Diagrama de componentes 5.9 con entradas y salidas reales; README de reproducción; bitácora de incidentes con estado, responsable y fecha (operación de calidad en DMBOK2).

##### Insumos y fundamento

- Código hasta Hito 2 (1.171 líneas)
- Resumen DAMA: secciones 5 y 6
- Anteproyecto: 5.7 y 5.9
- Retro de junio: observación 6

##### Entregables

- Repositorio etiquetado v1.0
- Imagen Docker
- Tablero de monitoreo
- README de reproducción

##### Criterio de cierre

Otra persona reproduce los resultados desde el contenedor con un solo comando, las pruebas pasan y el resumen JSON coincide con el del Hito 4.

##### Riesgo y mitigación

Power BI no es reproducible por código. Mantener el scorecard en CSV como salida primaria y el tablero como vista.

#### Hito 6 · Validar y sustentar (OE4) · Lidera: equipo

*Cierra: errores sin confirmar · hipótesis incoherente con el diseño · reproducibilidad no medida · observaciones de junio*

##### Actividades

1. **Validación externa.**
   - Consulta formal a EPM o a la CREG sobre los seriales 43.577 y 43.501, el valor 205.151, la mezcla de enero y abril y el cambio de febrero de 2020.
2. **Verificación manual de alertas.**
   - Muestra aleatoria de 50 alertas reales contrastada con la publicación original de EPM; precisión empírica con intervalo.
3. **Resolver hipótesis frente a diseño.**
   - Reglas estáticas como procedimiento tradicional (MinTIC, Deequ); framework como reglas más cartas y ML; contraste de H1 con el bootstrap (hoy 88 % frente a 73 %).
   - Si no se sostiene, reformular bajo Design Science y decirlo en el documento.
4. **Reproducibilidad como resultado.**
   - Misma salida en dos ambientes (Colab y Docker) y con dos descargas distintas; reportarlo como evidencia, no como herramienta, según la nota de dirección de junio.
5. **Documento final.**
   - Problema y pregunta; marco con DMBOK e ISO delimitados; metodología con tipos de regla, ciclo y técnicas; resultados; limitaciones: tamaño efectivo, carácter retrospectivo, una sola fuente con series largas.
   - Depurar referencias, cronograma y resumen (observaciones menores de junio).
6. **Sustentación.**
   - Ensayo con jurado simulado; cada objetivo específico con su evidencia señalada en el documento.

##### Insumos y fundamento

- Retroalimentación de junio
- 05_alertas_imr_reales.csv
- 03_hallazgos.csv
- Anteproyecto completo

##### Entregables

- Documento final
- Anexo de validación externa
- Repositorio final y tablero
- Presentación de sustentación

##### Criterio de cierre

H1 contrastada o reformulada con evidencia. Cada objetivo específico señala el entregable que lo cumple. Las observaciones de junio están cerradas.

##### Riesgo y mitigación

EPM o la CREG no responden a tiempo. Presentar los casos como hipótesis con evidencia interna y dejarlo como limitación explícita.

#### Trazabilidad objetivo → hito → entregable → evidencia

| OE | Objetivo específico | Hitos | Entregable que lo cumple | Dónde queda la evidencia |
|---|---|---|---|---|
| OE1 | Dimensiones, métricas e indicadores (DAMA, ISO) | Hito 3 → Hito 4 | Matriz regla-dimensión-tipo-métrica; scorecard por fuente | Tabla en metodología y tabla de resultados |
| OE2 | Caracterización y reglas de negocio, fuente CREG | Hito 3 → Hito 5 | Fichas por fuente; decisión CREG; reglas en YAML con referencia regulatoria | Sección 5.8 actualizada y archivo de reglas |
| OE3 | Framework: perfilamiento, reglas, anomalías | Hito 4 → Hito 5 | Paquete, contenedor, tablero; técnicas comparadas | Repositorio v1.0 y diagrama 5.9 |
| OE4 | Evaluar frente a procedimientos tradicionales | Hito 4 → Hito 6 | Tabla comparativa con IC; validación externa; reproducibilidad medida | Contraste de H1 y anexo de validación |

#### Dependencias

Hito 3 entrega a Hito 4 las cartas en log, la matriz OE1 y la clave estable. Hito 4 entrega a Hito 5 las técnicas y umbrales definitivos a empaquetar. Hito 5 entrega a Hito 6 el artefacto reproducible con el que se mide la reproducibilidad. Hito 6 cierra con los tres anteriores.

Figura: `plan_hitos_3-6_detallado.svg` (íconos Font Awesome Free 6.5.2, CC BY 4.0).


<a id="doc-393500a1bb5a"></a>

## desarrollo_puntos/3_documentacion_general/README.md

### Hito 3 · Índice de organización

Organización por contenido realizada el 6 de noviembre de 2026. La numeración sigue las
siete actividades del Hito 3 del [plan transcrito del SVG](Antecedentes/plan_hitos_3-6_detallado.txt),
hasta antes del Hito 4. Los documentos existentes reflejan un alcance de fuentes y algunas
decisiones posteriores a ese plan; la clasificación no modifica ni aprueba esas decisiones.

| Punto | Contenido |
|---|---|
| [3.1](REFERENCIA_TECNICA.md#doc-ec2f495b53a8) | Matriz OE1, indicadores, plantillas y evidencia de medición. |
| [3.2](REFERENCIA_TECNICA.md#doc-6d09f59e62b7) | Fichas, semántica y perfiles de caracterización de fuentes. |
| [3.3](REFERENCIA_TECNICA.md#doc-1daec17adf88) | Réplica, adaptadores, diferencias e insumos históricos del pipeline. |
| [3.4](REFERENCIA_TECNICA.md#doc-8c63814239f9) | Evidencia de selección CREG y evaluación de alternativas. |
| [3.5](REFERENCIA_TECNICA.md#doc-6927d6df7ab3) | Cartas logarítmicas y revisión de sus señales. |
| [3.6](REFERENCIA_TECNICA.md#doc-2c881ea64a55) | Trazabilidad estable y reproducibilidad entre versiones. |
| [3.7](REFERENCIA_TECNICA.md#doc-fcfdcb7af446) | Cuarentena y remuestreo/bootstrap. |

Los documentos generales quedan aquí porque abarcan varios puntos:

- [Plan de hitos en Markdown](REFERENCIA_TECNICA.md#doc-bfabfa5b4a96), que incluye también los hitos 4 a 6.
- [Documento de cierre](REFERENCIA_TECNICA.md#doc-f1d8ec2447b1), con sus límites y pendientes existentes.
- [Pendientes de aprobación de Hitos 3 y 4](REFERENCIA_TECNICA.md#doc-349c3e6eb49a).
- [Revisión de integridad de Hitos 3 y 4](REFERENCIA_TECNICA.md#doc-e95ee88a713e), con verificaciones, hallazgos y límites técnicos.
- [Referencia anterior de roles y umbrales](REFERENCIA_TECNICA.md#doc-45878726ae90).
- [Contexto previo](REFERENCIA_TECNICA.md#doc-b2834637e78b), conservado con su contenido histórico.

La revisión cubrió los **76 archivos originales** de las carpetas que empiezan por 3:
8 en 3.1, 22 en 3.2 y 46 en 3.3; 3.4, 3.5 y 3.6 estaban vacías. Se movieron **51**
archivos y se mantuvieron 25 en su ubicación. Se añadieron índices para orientar la lectura.

El [inventario completo](../Data/gold/outputs/organizacion/INVENTARIO_ORGANIZACION.csv) registra, archivo por archivo, origen,
destino, punto asignado, motivo y SHA-256 anterior. Los CSV de datos/resultados, JSON de
evidencia y la especificación YAML se conservan íntegros. Se ajustaron rutas e imports
para mantener las dependencias, incluidos los consumidores existentes del Hito 4.

La [verificación de la organización](REFERENCIA_TECNICA.md#doc-7d24dd3127fd) detalla las once
ejecuciones realizadas en una copia temporal y las comprobaciones de integridad y enlaces.

La clasificación no certifica cumplimiento del Hito 3. En particular, la fuente SSPD actual
no es la del ejemplo original, la matriz incorpora oportunidad y el bootstrap existente
remuestrea series dentro de categorías. Las diferencias del plan y las aprobaciones
pendientes siguen siendo asuntos metodológicos documentados por separado.


<a id="doc-e95ee88a713e"></a>

## desarrollo_puntos/3_documentacion_general/REVISION_HITOS_3_4.md

### Revisión de integridad — Hitos 3 y 4

**Fecha de revisión:** 9 de noviembre de 2026  
**Alcance:** estructura del repositorio, entregables previstos en el plan detallado, enlaces locales,
reproducibilidad básica, pendientes de decisión y guía para el equipo.

#### Resultado ejecutivo

Los Hitos 3 y 4 están **ordenados y documentados como línea base técnica**. Las actividades
3.1 a 3.7 y 4.1 a 4.6 tienen carpeta e índice de lectura; los resultados provisionales están
distinguidos de los resultados medidos y las decisiones metodológicas pendientes están consolidadas
en un único documento para el director.

Esto no equivale a una aprobación formal de ambos hitos. Siguen pendientes evidencia externa,
una segunda descarga independiente, definiciones metodológicas y la incorporación de los resultados
en el documento oficial de tesis.

#### 1. Organización comprobada

| Bloque | Estado | Punto de entrada |
|---|---|---|
| Hito 3: 3.1 a 3.7 | Completo en estructura | [Índice del Hito 3](REFERENCIA_TECNICA.md#doc-393500a1bb5a) |
| Hito 4: 4.1 a 4.6 | Completo en estructura | [Guía, sección 15 en adelante](REFERENCIA_TECNICA.md#doc-b8f4ce33e31c) |
| Matriz OE1 | Disponible en CSV, Markdown y YAML | [3.1](REFERENCIA_TECNICA.md#doc-ec2f495b53a8) |
| Cuatro fuentes y fichas | EPM, CHEC, SSPD y XM | [3.2](REFERENCIA_TECNICA.md#doc-6d09f59e62b7) |
| Trazabilidad, cuarentena y bootstrap | Disponibles y separados de los datos fuente | [3.6](REFERENCIA_TECNICA.md#doc-2c881ea64a55) y [3.7](REFERENCIA_TECNICA.md#doc-fcfdcb7af446) |
| Técnicas, sensibilidad, métricas, regla sistémica, scorecard y niveles | Documentados por actividad | [4.1](REFERENCIA_TECNICA.md#doc-81f243d988ee), [4.2](REFERENCIA_TECNICA.md#doc-15dec98a30e1), [4.3](REFERENCIA_TECNICA.md#doc-a66acf433abb), [4.4](REFERENCIA_TECNICA.md#doc-c26806ebe30e), [4.5](REFERENCIA_TECNICA.md#doc-74d9a3dc3145), [4.6](REFERENCIA_TECNICA.md#doc-dd387e3f4a37) |

No se movieron ni eliminaron datos durante esta revisión. El CSV en `fuentes_datos/datos/Datos_en_revision/`
permanece fuera del alcance de los cuatro datos seleccionados.

#### 2. Verificaciones realizadas

| Verificación | Resultado | Interpretación |
|---|---|---|
| Carpetas e índices | Correcto | Existen los índices 3.1–3.7, 4.1–4.6 y el índice general de Hito 3. |
| Sintaxis de scripts Python | Correcta | Los 39 scripts revisados compilan; esto detecta errores de sintaxis, no valida por sí solo los resultados científicos. |
| Matriz OE1 | Ejecutada | Se regeneraron sus representaciones CSV, Markdown y YAML desde el script de medición. |
| Trazabilidad (3.6) | Ejecutada | Se regeneró el manifiesto de ejecución y las huellas de contenido. |
| Bootstrap (3.7) | Ejecutado | Se generaron resultados para 105 grupos fuente/categoría con semilla fija. |
| Scorecard (4.5) | Ejecutado | Se regeneró el resumen de 4 fuentes × 8 dimensiones (32 combinaciones). Sigue siendo provisional. |
| Niveles y costo (4.6) | Ejecutado | Se regeneraron 36 combinaciones fuente/nivel/método y 47 mediciones de costo. |
| Sensibilidad (4.2) | Validado | 9 pruebas correctas; verificador correcto para 22 escenarios, 39.288 observaciones y 212.497 ensayos. |
| Métricas (4.3) | Validado | 12 pruebas correctas; 720 filas de métricas, 8.328 observaciones y 43.846 casos reconciliados. |
| Regla sistémica (4.4) | Validado | 10 pruebas correctas; 1.272 fracciones mensuales, 9 variantes y 227 filas de catálogo reconciliadas. |
| Enlaces locales de la documentación | Corregidos | Las referencias a figuras no versionadas ahora indican cómo regenerarlas y apuntan a los CSV auditables. |
| Pendientes históricos de 4.1 | Corregidos | Los documentos de cierre ahora indican que las métricas e inyecciones se resolvieron en 4.2/4.3 y remiten al registro único vigente. |

#### 3. Límites técnicos que no deben ocultarse

Los análisis 4.2, 4.3 y 4.4 dependen de bibliotecas científicas (`numpy`, `pandas`,
`scikit-learn` y `matplotlib`). Sus configuraciones registran las versiones usadas, pero el
repositorio no tiene todavía un `pyproject.toml` o contenedor, pero ya incluye los archivos
bloqueados [requirements-hito4-2.txt](../Environment/requirements-hito4-2.txt) y
[requirements-hito4-3-4.txt](../Environment/requirements-hito4-3-4.txt). Esta revisión los
reejecutó en entornos aislados con las versiones registradas
por cada actividad: 4.2 con numpy 2.3.5, pandas 2.3.3 y scikit-learn 1.8.0; 4.3–4.4 con numpy
2.5.4, pandas 2.3.3 y scikit-learn 1.9.1 (Matplotlib 3.11.2 para las figuras). En un entorno
nuevo se puede preparar esa instalación con los comandos de [requirements/README.md](REFERENCIA_TECNICA.md#doc-e050028ca414).

Las figuras de esos puntos tampoco se guardan en Git: son salidas binarias regenerables ignoradas
por diseño. Las tablas CSV, los manifiestos SHA-256 y los scripts sí permanecen disponibles. Esta
decisión evita duplicar archivos derivados, pero exige crear el entorno y ejecutar los scripts para
ver los gráficos. El empaquetado reproducible del entorno es una tarea natural del Hito 5.

#### 4. Pendientes que requieren decisión o aprobación

Todo pendiente que cambia alcance, interpretación o metodología está centralizado en
[PENDIENTES_APROBACION_HITO3.md](REFERENCIA_TECNICA.md#doc-349c3e6eb49a). Incluye:

- roles, umbrales y severidad de reglas;
- catálogos y semántica de CHEC;
- muestra y fuente para exactitud; plazo o proxy para oportunidad;
- segunda versión independiente y política de codificación;
- unidad del bootstrap, R10, R12, CART01 y casos de una sola serie;
- valor X, prevalencia, método principal, etiquetas canónicas, MAD cero, LOF y Extended Isolation Forest;
- condición provisional de los resultados 4.5 y alcance de niveles en 4.6;
- evidencia regulatoria, consulta formal y la incorporación de estos resultados en el documento oficial de tesis.

Nada de esa lista debe presentarse como aprobado mientras no se complete el registro de aprobación
del mismo documento.

#### 5. Conclusión operativa

El repositorio está listo para que el equipo y el director revisen decisiones y evidencia sin
perder la trazabilidad. Antes del cierre formal se debe: (1) obtener y comparar una segunda descarga,
(2) completar evidencia de exactitud y oportunidad, (3) obtener las aprobaciones registradas,
(4) integrar el contenido aprobado en la tesis y (5) preparar un entorno reproducible para los
análisis que usan bibliotecas científicas.


<a id="doc-45878726ae90"></a>

## desarrollo_puntos/3_documentacion_general/VALIDACION_ROLES_UMBRALES.md

### Documento sustituido

Todos los pendientes de aprobación del Hito 3 se consolidaron en:

[PENDIENTES_APROBACION_HITO3.md](REFERENCIA_TECNICA.md#doc-349c3e6eb49a)

Este archivo se conserva como referencia para no romper enlaces previos.


<a id="doc-7d24dd3127fd"></a>

## desarrollo_puntos/3_documentacion_general/VERIFICACION_ORGANIZACION.md

### Verificación de la organización

Verificación realizada el 6 de noviembre de 2026. Se ejecutaron los scripts en una
copia temporal aislada con los datos locales; las tablas y los manifiestos del proyecto
se conservaron. No se realizaron descargas ni se aprobaron decisiones metodológicas.

#### Comprobaciones

- Los 76 archivos originales están localizados en el inventario, sin eliminaciones.
- Los CSV originales de resultados, los JSON de evidencia y `matriz_oe1.yaml`
  conservan su SHA-256 anterior.
- Los enlaces relativos de los documentos del Hito 3 y los índices principales se
  comprobaron contra los destinos existentes.
- Se verificaron la sintaxis Python y los imports de la matriz y sus adaptadores.
- Las cuatro cartas, la tabla de revisión EPM y el bootstrap se regeneraron en la copia
  temporal y coinciden, registro por registro, con las tablas conservadas.
- La matriz pudo regenerar 76 registros para cuatro fuentes desde 3.1, usando los
  adaptadores de 3.3 y las cartas de 3.5.
- El scorecard consumidor del Hito 4 pudo leer la nueva ruta de la matriz y producir
  32 registros en la copia temporal.
- La trazabilidad pudo leer los insumos históricos de 3.3 y escribir el manifiesto
  para cuatro archivos en 3.6, además de las copias enriquecidas de hallazgos y alertas.
- Se ejecutaron los generadores de cuarentena EPM y de las otras fuentes en la copia.

#### Scripts ejecutados en la copia

- `desarrollo_puntos/3.5/EPM/cartas_log_epm.py`
- `desarrollo_puntos/3.5/CHEC/cartas_log_chec.py`
- `desarrollo_puntos/3.5/SSPD/cartas_log_sspd.py`
- `desarrollo_puntos/3.5/XM/cartas_log_xm.py`
- `desarrollo_puntos/3.5/EPM/revision_cartas_epm.py`
- `desarrollo_puntos/3.7/bootstrap_categorias.py`
- `desarrollo_puntos/3.1/medir_matriz_oe1.py`
- `desarrollo_puntos/4.5/generar_scorecard_oe1.py`
- `desarrollo_puntos/3.6/trazabilidad.py`
- `desarrollo_puntos/3.7/EPM/cuarentena.py`
- `desarrollo_puntos/3.7/cuarentena_fuentes.py`

Estas comprobaciones validan las rutas y la ejecución después de organizar. No
certifican la validez estadística de los métodos ni el cierre de los siete puntos.
Los resultados regenerados en la copia no reemplazan los resultados conservados.


<a id="doc-fd8cd320f92a"></a>

## desarrollo_puntos/4.1/CIERRE_VIÑETA_1.md

### Cierre parcial · Hito 4.1, viñeta 1

> **Documento histórico actualizado.** Este cierre describe el estado al terminar la primera
> viñeta de 4.1. Las métricas, la comparación a tasa igualada y los experimentos de inyección
> que aparecían como pendientes se completaron en 4.2 y 4.3. Las decisiones que todavía requieren
> aprobación están en el único registro vigente:
> [PENDIENTES_APROBACION_HITO3.md](REFERENCIA_TECNICA.md#doc-349c3e6eb49a).

#### Puntos cerrados con los archivos disponibles

##### Sensibilidad de umbral

Se ejecutaron de forma separada los umbrales 2.66, 3.0 y 3.267 mediante
`ejecutar_sensibilidad.py`. Cada resultado conserva sus CSV y configuración en
`resultados_umbral_2_66`, `resultados_umbral_3_0` y `resultados_umbral_3_267`.

##### Huecos temporales

El cálculo fue corregido para aceptar únicamente pares de meses consecutivos.
No se imputan meses ni se calcula un cambio que cruce una discontinuidad. Las
series que no alcanzan 36 cambios de referencia más 12 de vigilancia válidos se
excluyen del resumen, conservando el criterio del protocolo.

##### MAD igual a cero

Se generó `auditoria_mad_cero.json`. El tratamiento queda explicitado como
regla conservadora: no se inventa una escala y se marca señal si el cambio es
distinto de la mediana. Esto cierra la trazabilidad computacional, pero no la
aprobación metodológica definitiva de esa política.

#### Pendientes que permanecían al cierre de 4.1

1. **Precisión, recall y F1 del Z-score — resuelto en 4.3:** `06_experimento_inyeccion.csv` y
   `07_deteccion_por_tipo.csv` contienen resultados de reglas, I-MR e Isolation
   Forest, pero no contienen las predicciones del nuevo Z-score. Se requiere
   rerun del experimento de inyección con el nuevo método para calcular sus
   métricas. El experimento nuevo y sus métricas quedaron documentados en 4.2 y 4.3.
2. **Comparación a tasa de alerta igualada — resuelta en 4.3:** se calibró el umbral del
   Z-score contra cada método dentro del mismo protocolo y se guardaron las tablas.
3. **Validación de alertas reales — vigente:** no existe una etiqueta externa confirmada
   para clasificar las señales reales como errores o no errores.
4. **Decisión de negocio sobre MAD cero — vigente:** el análisis está automatizado, pero
   la selección definitiva entre señal, exclusión o escala alternativa requiere
   aprobación metodológica y revisión semántica de SSPD.


<a id="doc-712708a8fc91"></a>

## desarrollo_puntos/4.1/NOTA_SSPD_361_356.md

### Diferencia entre 361 y 356 series SSPD

El Hito 3 reporta 361 series SSPD y 4.332 cambios de vigilancia en la línea
base de cartas. La implementación actual de las viñetas 1 y 2 reporta 356
series y 4.272 observaciones de vigilancia.

La diferencia no proviene de una modificación del archivo fuente. El Hito 4.1
aplica el criterio temporal explícito del plan: solo se calcula un cambio cuando
los dos meses son consecutivos. Cinco series de SSPD no alcanzan 36 cambios de
referencia más 12 cambios de vigilancia bajo ese criterio y se excluyen.

No se imputan meses ni se cruzan discontinuidades. Los resultados del Hito 3 se
conservan como línea base histórica y los resultados de 4.1 como línea base
estricta por meses consecutivos. Las tasas no deben compararse sin declarar esta
diferencia de población.


<a id="doc-e7f9f86a97c5"></a>

## desarrollo_puntos/4.1/PENDIENTES_HITO_4_1_VIÑETAS_1_Y_2.md

### Pendientes · Hito 4.1 · Viñetas 1 y 2

> **Documento histórico actualizado.** Este archivo conserva el diagnóstico con el que terminó
> inicialmente 4.1. Los puntos 1, 2 y 3 fueron resueltos posteriormente en 4.2 y 4.3. Las
> decisiones que siguen vigentes no se aprueban aquí: están consolidadas en
> [PENDIENTES_APROBACION_HITO3.md](REFERENCIA_TECNICA.md#doc-349c3e6eb49a),
> que es el único registro para el director y el equipo.

#### Estado general

Las dos viñetas tienen implementaciones reproducibles dentro de `4.1`:

- Z-score robusto sobre cambios logarítmicos.
- Isolation Forest entrenado con referencia y evaluado en vigilancia.

También se generaron sensibilidad de umbrales, calibración cruzada provisional,
trazabilidad de snapshots, scorecard OE1 provisional y la nota de la diferencia
entre las series SSPD del Hito 3 y Hito 4.1.

#### Actividades realizadas

- Cambios logarítmicos mensuales consecutivos.
- Ventana de 36 cambios de referencia y 12 de vigilancia.
- No se cruzan huecos temporales ni se imputan meses.
- Isolation Forest independiente por fuente.
- Escalamiento del Isolation Forest calculado solo con referencia.
- Calibración cruzada por grupos de series a la tasa histórica de cartas del Hito 3.
- Comparación de señales por método mediante `calibracion_cv_tasa_igualada.csv`.
- Clave estable derivada de fuente, serie, medida y periodo en las alertas de 4.1.
- Hash SHA-256 del snapshot asociado a cada alerta.
- Scorecard provisional por fuente y dimensión.
- Documentación de la diferencia SSPD: 361 series en Hito 3 frente a 356 bajo el
  criterio estricto de meses consecutivos en Hito 4.1.

#### Pendientes que permanecen

##### 1. Repetir el experimento de errores inyectados — resuelto

Los archivos del Hito 2 contienen etiquetas y resultados de reglas, I-MR e
Isolation Forest anterior, pero no predicciones del Z-score robusto ni del nuevo
Isolation Forest logarítmico. Este rerun se realizó en 4.2 para las fuentes y
escenarios definidos allí; sus resultados se evalúan en 4.3.

##### 2. Calcular precisión, recall, F1 e intervalos — resuelto

4.3 calcula estas métricas e intervalos para los errores inyectados. Las alertas
reales siguen sin etiqueta externa confirmada; esa limitación permanece vigente.

##### 3. Comparar detección en t frente a t+1 — resuelto

4.2 ejecuta ambos horizontes para las inyecciones y 4.3 los reporta a tasa de
alerta igualada. No se infiere este resultado desde alertas reales.

##### 4. Resolver el caso XM en validación cruzada

XM tiene una sola serie. Por esa razón se registra como `no_calibrable` en la
validación cruzada de cinco grupos. Puede reportarse su resultado descriptivo,
pero no un intervalo o una validación cruzada entre series.

##### 5. Aprobar el tratamiento de MAD igual a cero

El comportamiento está implementado y auditado en `auditoria_mad_cero.json`,
pero la decisión final —señal, exclusión, IQR o caso degenerado— requiere
aprobación metodológica y revisión semántica de SSPD.

##### 6. Validar alertas reales externamente

No existe una verdad terreno completa para EPM, CHEC, SSPD o XM. Las alertas
reales deben seguir presentándose como señales estadísticas hasta contrastar una
muestra con publicaciones oficiales.

##### 7. Aprobar umbrales y estados del Hito 3

Los umbrales de la matriz OE1, los roles y la severidad permanecen pendientes
en `3_documentacion_general/PENDIENTES_APROBACION_HITO3.md`. El scorecard generado en 4.1 es
provisional y no reemplaza esa aprobación.

##### 8. Segunda descarga para reproducibilidad temporal

Los hashes actuales prueban trazabilidad del snapshot utilizado, pero no que el
portal produzca los mismos resultados en una segunda descarga independiente.

#### Limitación de interpretación

La comparación entre métodos es metodológicamente común, pero las fuentes no
son semánticamente intercambiables: EPM y CHEC contienen tarifas, SSPD contiene
información comercial/consumo y XM contiene demanda. Una señal no equivale por
sí sola a un error de calidad.


<a id="doc-81f243d988ee"></a>

## desarrollo_puntos/4.1/README.md

### Hito 4.1 · Viñeta 1 · Z-score robusto

Este componente implementa una línea base robusta para detectar cambios atípicos
en las series del proyecto. Se aplica sobre cambios logarítmicos y conserva el
mismo protocolo de las cartas del Hito 3:

1. primeros 36 cambios mensuales consecutivos para referencia;
2. siguientes 12 cambios para vigilancia;
3. mediana y MAD calculados solo con referencia;
4. señal cuando `|z_robusto| > umbral`.

La fórmula es `0.6744897501960817 × (cambio_log − mediana) / MAD`.
El umbral predeterminado es `3.267`; también están disponibles `2.66` y `3.0`
para sensibilidad.

#### Ejecución

Desde la raíz del repositorio:

```bash
python desarrollo_puntos/4.1/zscore_robusto.py
python desarrollo_puntos/4.1/zscore_robusto.py --umbral 2.66
python desarrollo_puntos/4.1/zscore_robusto.py --umbral 3.0
```

Procesa EPM, CHEC, SSPD y XM. Solo calcula cambios entre meses consecutivos;
los huecos temporales no se cruzan. En EPM aplica `3.7/EPM/cuarentena_registros.csv`
sin modificar la fuente ni imputar valores.

#### Salidas

- `zscore_robusto_detalle.csv`: cada cambio vigilado y su Z-score robusto.
- `zscore_robusto_resumen.csv`: resultados por serie y medida.
- `configuracion.json`: protocolo, umbral y SHA-256 de las entradas.

Si el MAD es cero, se registra `mad_cero`, no se inventa una escala y se marca
señal solo cuando el cambio difiere de la mediana. Una señal estadística no
prueba por sí sola un error de datos.


<a id="doc-ec554867a4f3"></a>

## desarrollo_puntos/4.1/README_ISOLATION_FOREST.md

### Hito 4.1 · Viñeta 2 · Entrenamiento en referencia y evaluación en vigilancia

#### Implementación

`isolation_forest_referencia_vigilancia.py` es una implementación independiente
del Isolation Forest del Hito 2. No modifica sus scripts, CSV ni resultados.

El protocolo utiliza:

- cambios logarítmicos de meses consecutivos;
- 36 cambios de referencia;
- 12 cambios de vigilancia;
- un modelo independiente por fuente;
- escalamiento robusto calculado solo con referencia;
- umbral definido por el percentil 99,5 de los puntajes de entrenamiento.

Las cuatro características son:

1. cambio logarítmico actual;
2. cambio logarítmico anterior;
3. diferencia absoluta entre ambos cambios;
4. nivel logarítmico relativo a la mediana de referencia.

#### Ejecución

Desde la raíz del repositorio:

```bash
python desarrollo_puntos/4.1/isolation_forest_referencia_vigilancia.py
```

Para sensibilidad del umbral de referencia:

```bash
python desarrollo_puntos/4.1/isolation_forest_referencia_vigilancia.py --percentil 0.99
python desarrollo_puntos/4.1/isolation_forest_referencia_vigilancia.py --percentil 0.9975
```

#### Salidas

- `isolation_forest_referencia_vigilancia_detalle.csv`: puntaje y señal por
  serie y periodo de vigilancia.
- `isolation_forest_referencia_vigilancia_resumen.csv`: resumen por fuente.
- `isolation_forest_referencia_vigilancia_configuracion.json`: configuración,
  hashes de entradas y evidencia de que el entrenamiento usó únicamente la
  referencia.
- `auditoria_cuarentenas_h3.json`: registro de las cuatro cuarentenas heredadas
  del Hito 3. EPM se aplica al construir las series; las otras tres se auditan
  explícitamente y actualmente no contienen filas.

La ejecución no produce todavía precisión, recall o F1: esas métricas requieren
repetir el experimento de errores inyectados con este método.


<a id="doc-6e8fab534d7e"></a>

## desarrollo_puntos/4.2/INFORME_SENSIBILIDAD.md

### Hito 4.2 · Resultados del análisis de sensibilidad

Fecha: 6 de noviembre de 2026. Se ejecutó el punto 2 del Hito 4 del plan local sobre
los snapshots conservados de EPM, CHEC, SSPD y XM. Las salidas de 3.x y 4.1 permanecen intactas.

#### Resultado principal

Se evaluaron 24, 36 y 48 cambios de referencia cuando la longitud lo permite, las
constantes I/MR, límites robustos con MAD, percentiles IF 99 y 99,5, R12 con factores
5, 10 y 20, ambos horizontes de detección y cuatro umbrales de reclasificación sistémica.
Se ejecutaron **22 escenarios fuente/cohorte/ventana**, con
**39,288 observaciones detalladas** y
**212,497 ensayos de inyección detallados**, sumando paneles
y ventanas. Estos conteos incluyen repeticiones deliberadas del mismo caso bajo otros
parámetros; no son tamaños de muestra independientes. El tipo de ensayo distingue
inyecciones individuales y estrés colectivo.

SSPD no permite 48 cambios más 12 de vigilancia: tiene como máximo 59 meses
consecutivos y esa configuración requiere 61. Se registra como **no evaluable**,
sin recortar vigilancia ni rellenar datos. XM conserva una sola serie/categoría;
sus resultados son descriptivos y no reciben un IC entre categorías.

#### 1. Cobertura y comparación de ventanas

| Fuente | Ref. 24 | Ref. 36 | Ref. 48 |
| --- | --- | --- | --- |
| EPM | 121 | 32 | 27 |
| CHEC | 276 | 276 | 276 |
| SSPD | 388 | 321 | 0 |
| XM | 1 | 1 | 1 |

La carga reutiliza `4.1/zscore_robusto.py`. Después se selecciona la racha mensual
consecutiva más larga de cada serie; en empate, la de fin más reciente. Se fija la
vigilancia en sus doce últimos cambios y se toman inmediatamente antes 24, 36 o 48
cambios. No se unen rachas separadas ni se cruza un mes ausente.

El panel `disponible` describe la población elegible de cada ventana. El panel `comun`
mantiene las mismas series, categorías y meses en todas las ventanas factibles de la
fuente. En SSPD compara 24 y 36; en las otras fuentes, 24/36/48. IF también se vuelve
a entrenar dentro de esta cohorte común, evitando que una variación en la población
de entrenamiento se confunda con la longitud de referencia.

Lectura inicial de la cohorte común con referencia 36:

- **EPM:** I/MR clásica genera 5.556 % de alertas reales y MAD 3σ, 3.704 %. IF p99,5 detecta 5.01 % de las inyecciones individuales en t o t+1, sobre 1,617 casos de la mezcla diseñada.
- **CHEC:** I/MR clásica genera 0.000 % de alertas reales y MAD 3σ, 0.000 %. IF p99,5 detecta 63.98 % de las inyecciones individuales en t o t+1, sobre 17,103 casos de la mezcla diseñada.
- **SSPD:** I/MR clásica genera 4.595 % de alertas reales y MAD 3σ, 8.827 %. IF p99,5 detecta 51.31 % de las inyecciones individuales en t o t+1, sobre 20,880 casos de la mezcla diseñada.
- **XM:** I/MR clásica genera 0.000 % de alertas reales y MAD 3σ, 0.000 %. IF p99,5 detecta 72.73 % de las inyecciones individuales en t o t+1, sobre 55 casos de la mezcla diseñada.

Una tasa real de cero significa que estos límites no señalaron esos doce meses;
no demuestra ausencia de errores. La detección artificial también depende del tipo
de perturbación y del umbral: por ejemplo, una configuración IF con pocas alertas
puede tener baja detección de las inyecciones. Se conservan esos resultados sin
ajustar retrospectivamente los percentiles para mejorar la cifra de vigilancia.

Las diferencias siguientes son tasa alternativa menos tasa con referencia 36, en
las mismas series y meses. Sus IC por categorías están en el CSV correspondiente.

| Fuente | Ventana vs. 36 | Método | Series | Cambio (pp) |
| --- | --- | --- | --- | --- |
| EPM | 24 | IMR_clasica | 27 | +0.000 |
| EPM | 24 | MAD_3sigma | 27 | -1.852 |
| EPM | 24 | IF_p99.5 | 27 | +0.000 |
| EPM | 48 | IMR_clasica | 27 | -1.852 |
| EPM | 48 | MAD_3sigma | 27 | +0.000 |
| EPM | 48 | IF_p99.5 | 27 | +0.000 |
| CHEC | 24 | IMR_clasica | 276 | +0.242 |
| CHEC | 24 | MAD_3sigma | 276 | +0.000 |
| CHEC | 24 | IF_p99.5 | 276 | +0.000 |
| CHEC | 48 | IMR_clasica | 276 | +0.000 |
| CHEC | 48 | MAD_3sigma | 276 | +1.389 |
| CHEC | 48 | IF_p99.5 | 276 | +0.000 |
| SSPD | 24 | IMR_clasica | 321 | +0.649 |
| SSPD | 24 | MAD_3sigma | 321 | -0.337 |
| SSPD | 24 | IF_p99.5 | 321 | +0.415 |
| XM | 24 | IMR_clasica | 1 | +0.000 |
| XM | 24 | MAD_3sigma | 1 | +0.000 |
| XM | 24 | IF_p99.5 | 1 | +0.000 |
| XM | 48 | IMR_clasica | 1 | +0.000 |
| XM | 48 | MAD_3sigma | 1 | +0.000 |
| XM | 48 | IF_p99.5 | 1 | +0.000 |

Estos resultados no se comparan directamente con las tasas de 4.1: allí se usaron
los primeros cambios y podían concatenarse parejas consecutivas de distintas rachas.
Aquí la vigilancia es final y toda la partición pertenece a una sola racha continua.

#### 2. Constantes y límites robustos

Las constantes del plan cumplen funciones distintas:

- Carta I: media de cambios ± **2,66 × MR medio de referencia**.
- Carta MR: señal si el rango móvil excede **3,267 × MR medio de referencia**.
- `IMR_clasica` es la unión de ambas señales; el primer MR vigilado usa el último
  cambio de referencia, sin incorporar vigilancia al cálculo de límites.
- `MAD_3sigma`: mediana ± **3 × MAD / 0,6744897501960817**.
  También se examinan multiplicadores 2,66 y 3,267 sobre esta escala robusta como
  sensibilidad adicional; no se presentan como las mismas constantes de la carta I/MR.

Las fórmulas se apoyan en [NIST, cartas individuales](https://www.itl.nist.gov/div898/handbook/pmc/section3/pmc322.htm),
[NIST, constantes I/MR](https://nvlpubs.nist.gov/nistpubs/Legacy/IR/nistir4941.pdf) y
[NIST, MAD escalado](https://www.itl.nist.gov/div898/software/dataplot/refman2/auxillar/mad.htm).
Los multiplicadores explorados proceden del plan y del protocolo del proyecto;
no se atribuye a NIST una recomendación de seleccionar uno de ellos para estas fuentes.

Con MAD igual a cero se conserva el criterio explícito de 4.1: cualquier cambio
distinto de la mediana produce una señal y no se añade una escala artificial.
Series con MAD cero en referencia 36/cohorte común: `{'CHEC': 0, 'EPM': 0, 'SSPD': 18, 'XM': 0}`.
Esto puede hacer que cambiar el multiplicador no tenga efecto; no se interpreta
una tasa idéntica como prueba de robustez del proceso.

Tasas reales bajo referencia 36 y cohorte común:

| Fuente | Método | Series | Alertas (%) | IC95 (%) |
| --- | --- | --- | --- | --- |
| EPM | IMR_clasica | 27 | 5.556 | 0.000–14.086 |
| EPM | MAD_3sigma | 27 | 3.704 | 0.000–9.391 |
| EPM | IF_p99 | 27 | 0.000 | 0.000–0.000 |
| EPM | IF_p99.5 | 27 | 0.000 | 0.000–0.000 |
| EPM | R12_f10 | 27 | 0.000 | 0.000–0.000 |
| CHEC | IMR_clasica | 276 | 0.000 | 0.000–0.000 |
| CHEC | MAD_3sigma | 276 | 0.000 | 0.000–0.000 |
| CHEC | IF_p99 | 276 | 0.000 | 0.000–0.000 |
| CHEC | IF_p99.5 | 276 | 0.000 | 0.000–0.000 |
| CHEC | R12_f10 | 276 | 0.000 | 0.000–0.000 |
| SSPD | IMR_clasica | 321 | 4.595 | 3.264–6.033 |
| SSPD | MAD_3sigma | 321 | 8.827 | 7.017–10.895 |
| SSPD | IF_p99 | 321 | 0.571 | 0.103–1.304 |
| SSPD | IF_p99.5 | 321 | 0.467 | 0.065–1.160 |
| SSPD | R12_f10 | 321 | 0.130 | 0.000–0.304 |
| XM | IMR_clasica | 1 | 0.000 | Sin IC: una categoría |
| XM | MAD_3sigma | 1 | 0.000 | Sin IC: una categoría |
| XM | IF_p99 | 1 | 0.000 | Sin IC: una categoría |
| XM | IF_p99.5 | 1 | 0.000 | Sin IC: una categoría |
| XM | R12_f10 | 1 | 0.000 | Sin IC: una categoría |

Los intervalos son bootstrap descriptivo de **categorías completas**, no de filas
mensuales ni series supuestamente independientes: 1000
repeticiones, razón de numeradores y denominadores remuestreados, semilla fija.
Condicionan a las fuentes y modelos ajustados y no incluyen incertidumbre por reentrenamiento
ni garantizan representatividad poblacional. Se conservan por fuente, método y ventana.

#### 3. Percentiles 99 y 99,5 de Isolation Forest

Se usan 300 árboles por fuente/ventana/cohorte/calendario de vigilancia, con cuatro rasgos: cambio log actual,
cambio anterior, diferencia absoluta entre cambios y nivel log relativo a la mediana
del nivel de referencia. Centros, escalas y percentiles se calculan solo en referencia;
las inyecciones no vuelven a ajustar el modelo. Las series que terminan en meses
distintos tienen modelos separados, para que ninguna referencia termine después
del inicio de vigilancia de otra serie del mismo modelo. `modelos_IF.csv` conserva
los calendarios y umbrales; el submuestreo es el menor de 256 y el número de referencias.
El umbral 99,5 es mayor o igual al 99
y sus alertas son un subconjunto, verificado durante la ejecución.

Los percentiles son de puntajes **de entrenamiento**. No representan una tasa de
falsas alarmas garantizada fuera de muestra ni equivalen a una validación cruzada
a tasa igualada. Se conserva esta distinción frente al componente de calibración 4.1.

#### 4. Sensibilidad de R12 e interacción de parámetros

Se aplica `abs(nivel) > factor × mediana(abs(niveles_referencia))` con factores
5, 10 y 20. El umbral utiliza solo los niveles de referencia; no se estima sobre
la serie completa como ocurría en el Hito 2. R12 se mantiene como advertencia.
En XM se analiza magnitud de demanda, no un importe tarifario ni el valor absoluto
de un cambio logarítmico. Su semántica debe seguir identificada como adaptación.

Además de cada detector aislado, `combinaciones_framework.csv` cruza dos alternativas
de cartas (I/MR clásica o MAD 3σ), dos percentiles IF y tres factores R12, por ventana
y cohorte: doce uniones de señales por escenario. La figura 09 muestra el efecto
conjunto sobre la tasa real de alertas. No se elige una combinación usando la propia
vigilancia como conjunto de validación.

#### 5. Detección en t frente a t o t+1

Se perturba un único nivel positivo en copias de la vigilancia, con referencia y modelo
congelados. Se usan todos los once primeros meses, sin reemplazo; el duodécimo es el
seguimiento del último origen. Los seis tipos son multiplicar/dividir por 1.000,
serial Excel fijo 43.577, aumento de 10 %, valor anterior y otra medida positiva
del mismo grupo/mes. La otra medida se elige por orden de nombre para reproducibilidad.
Si el valor no cambia o no existe otra medida, el caso se omite con motivo explícito.

El serial Excel replica un mecanismo de representación tarifaria; en demanda/consumo
es solo una perturbación numérica de escala, no evidencia de un defecto observado.
Signos negativos, ceros, faltantes y texto quedan fuera de este ensayo logarítmico:
no se convierten en logaritmos ficticios ni se mezclan con reglas de validez.

`t1` en el detalle significa la señal **solo en el mes siguiente**. La métrica
`t_o_t1` es la unión, no la suma; una prueba se cuenta una sola vez. Se conservan
también señales nuevas respecto a la copia sin inyección, para mostrar cuánto
puede inflar el resultado la presencia de alertas naturales previas. Estas señales
nuevas no son una estimación de precisión de alertas reales.

Resumen agregado de tipos para referencia 36/cohorte común:

| Fuente | Método | Casos | Solo t (%) | t o t+1 (%) | Ganancia (pp) | Nueva frente a base (%) |
| --- | --- | --- | --- | --- | --- | --- |
| EPM | IMR_clasica | 1617 | 68.27 | 73.47 | 5.19 | 71.00 |
| EPM | MAD_3sigma | 1617 | 68.95 | 72.79 | 3.83 | 71.30 |
| EPM | IF_p99.5 | 1617 | 5.01 | 5.01 | 0.00 | 5.01 |
| EPM | R12_f10 | 1617 | 36.73 | 36.73 | 0.00 | 36.73 |
| CHEC | IMR_clasica | 17103 | 64.09 | 74.54 | 10.44 | 74.54 |
| CHEC | MAD_3sigma | 17103 | 72.84 | 75.56 | 2.72 | 75.56 |
| CHEC | IF_p99.5 | 17103 | 57.66 | 63.98 | 6.32 | 63.98 |
| CHEC | R12_f10 | 17103 | 35.50 | 35.50 | 0.00 | 35.50 |
| SSPD | IMR_clasica | 20880 | 66.55 | 70.03 | 3.48 | 66.98 |
| SSPD | MAD_3sigma | 20880 | 70.03 | 73.67 | 3.64 | 68.70 |
| SSPD | IF_p99.5 | 20880 | 41.36 | 51.31 | 9.95 | 50.98 |
| SSPD | R12_f10 | 20880 | 23.24 | 23.34 | 0.11 | 23.19 |
| XM | IMR_clasica | 55 | 60.00 | 67.27 | 7.27 | 67.27 |
| XM | MAD_3sigma | 55 | 63.64 | 65.45 | 1.82 | 65.45 |
| XM | IF_p99.5 | 55 | 70.91 | 72.73 | 1.82 | 72.73 |
| XM | R12_f10 | 55 | 20.00 | 20.00 | 0.00 | 20.00 |

En esta comparación, la mayor ganancia entre los métodos mostrados corresponde a
**CHEC / IMR_clasica: 10.44 puntos porcentuales**.
Los CSV por tipo conservan denominadores e IC por categoría. Los porcentajes agregados
describen la mezcla de errores diseñada y no una prevalencia real de errores.

#### 6. Efecto de la regla sistémica

Para cada fuente, método y mes se divide el número de series-medida con señal entre
las series-medida realmente observadas en vigilancia ese mes. Se evalúan X = 10, 25,
50 y 75 %, con desigualdad estricta `fracción > X`. Se exige al menos dos series;
XM no admite una interpretación transversal con una sola serie y conserva sus alertas.
La unidad series-medida es la misma de los detectores; medidas del mismo grupo pueden
estar correlacionadas, por lo que no se interpreta el denominador como independencia.

Se calcula la tasa original y la retenida para revisión individual. Las señales
reclasificadas quedan guardadas en el catálogo mensual: no se eliminan. La etiqueta
es **candidato sistémico**, sin afirmar que sea un cambio regulatorio confirmado.
La calibración regulatoria y el contraste de fechas concretas son materia de 4.4;
esta ejecución 4.2 estudia sensibilidad sobre una grilla explícita, no elige X óptimo.

Ejemplo I/MR, referencia 36/cohorte común, X = 25 %:

| Fuente | Original (%) | Retenida (%) | Reclasificadas |
| --- | --- | --- | --- |
| EPM | 5.556 | 5.556 | 0 |
| CHEC | 0.000 | 0.000 | 0 |
| SSPD | 4.595 | 4.595 | 0 |
| XM | 0.000 | 0.000 | 0 |

Se recalcula el contexto mensual al inyectar: para el error individual se cambia
la señal de esa serie; para un evento colectivo se cambian simultáneamente todas
las series afectadas. El estrés colectivo aplica +10 % o ×1.000 en el mes con más
orígenes disponibles (desempate: el más reciente). Permite medir cuántas detecciones
de errores conocidos se ocultarían al aplicar la reclasificación sin validación.
Los eventos colectivos son ensayos descriptivos únicos y no reciben un IC basado
en fingir que cada serie es un evento independiente.

#### 7. Lectura y límites

- La comparación de ventanas debe partir del panel común y de sus cambios pareados;
  el panel disponible informa cobertura, pero mezcla poblaciones distintas.
- Un percentil o factor mayor reduce o conserva señales para un modelo/referencia
  dados; una tasa menor no demuestra mejor calidad ni mejor sensibilidad.
- Extender detección a t+1 puede recuperar el retorno del pico o un rasgo rezagado;
  también añade un mes de oportunidad de alerta. Se muestran ambos horizontes y
  las señales nuevas respecto a base, sin presentar esa ganancia como gratuita.
- La regla sistémica reduce la cola de revisión individual, pero puede esconder
  errores masivos. Los resultados de estrés cuantifican ese riesgo por configuración.
- Las series ya tienen restricciones de positividad y cuarentena EPM de la carga 4.1;
  esto condiciona el análisis. No constituye una auditoría de todos los registros fuente.
- La cuarentena histórica permanece fija al variar el factor R12. Se estudia su efecto
  como umbral detector; no se simula una nueva política que readmita o excluya registros
  históricos y vuelva a estimar todas las referencias.
- Las inyecciones siguen la mezcla diseñada; no sustituyen etiquetas externas ni
  completan la validación de alertas reales o todos los experimentos de 4.3.
- No se declaran óptimos umbrales ni aprobaciones de negocio. Los modelos se ajustan
  solo con referencias y no se modifican los datos ni resultados anteriores.

#### Reproducir y auditar

Desde la raíz del proyecto:

```powershell
python desarrollo_puntos/4.2/analisis_sensibilidad.py
python -m unittest discover -s desarrollo_puntos/4.2 -p test_sensibilidad.py -v
python desarrollo_puntos/4.2/verificar_resultados.py
```

`configuracion.json` fija versiones, semilla, fuentes, hashes, parámetros y fórmulas.
`manifiesto_resultados.json` permite verificar cada archivo. Las tablas de detalle
comprimidas son CSV UTF-8 legibles con `pandas.read_csv(ruta, compression="gzip")`.
`informe_sensibilidad.py` genera nueve figuras en PNG, SVG y PDF para revisión y exportación.
La carpeta `figuras/` contiene artefactos regenerables y no se versiona; debe reconstruirse en un
entorno que tenga las dependencias fijadas en `configuracion.json`.


<a id="doc-15dec98a30e1"></a>

## desarrollo_puntos/4.2/README.md

### 4.2 · Análisis de sensibilidad

La lectura principal está en [INFORME_SENSIBILIDAD.md](REFERENCIA_TECNICA.md#doc-6e8fab534d7e).
El análisis se ejecutó sobre las cuatro fuentes locales y escribe todas sus salidas aquí.

| Archivo | Contenido |
|---|---|
| [cobertura_ventanas.csv](../Data/gold/outputs/sensibilidad/cobertura_ventanas.csv) | Elegibilidad y configuraciones no evaluables. |
| [tasas_alerta_reales.csv](../Data/gold/outputs/sensibilidad/tasas_alerta_reales.csv) | Alertas e IC descriptivos por ventana, cohorte y método. |
| [comparacion_ventanas_pareada.csv](../Data/gold/outputs/sensibilidad/comparacion_ventanas_pareada.csv) | Diferencias 24/48 frente a 36 sobre las mismas series y meses. |
| [parametros_por_serie.csv](../Data/gold/outputs/sensibilidad/parametros_por_serie.csv) | Períodos de referencia/vigilancia, límites, MAD y mediana para R12. |
| [deteccion_inyecciones.csv](../Data/gold/outputs/sensibilidad/deteccion_inyecciones.csv) | Detección t/t+1, ganancia e IC por tipo; señales nuevas respecto a base. |
| [resumen_horizonte_36.csv](../Data/gold/outputs/sensibilidad/resumen_horizonte_36.csv) | Resumen de horizonte por fuente/método con referencia 36. |
| [inyecciones_omitidas.csv](../Data/gold/outputs/sensibilidad/inyecciones_omitidas.csv) | Casos sin perturbación efectiva o sin otra medida comparable. |
| [combinaciones_framework.csv](../Data/gold/outputs/sensibilidad/combinaciones_framework.csv) | Interacción de cartas, percentil IF y factor R12. |
| [alertas_sistemicas_por_mes.csv](../Data/gold/outputs/sensibilidad/alertas_sistemicas_por_mes.csv) | Catálogo mensual de candidatos para cada X, sin confirmar origen regulatorio. |
| [efecto_regla_sistemica_reales.csv](../Data/gold/outputs/sensibilidad/efecto_regla_sistemica_reales.csv) | Tasa original y tasa retenida por X. |
| [efecto_regla_sistemica_inyecciones.csv](../Data/gold/outputs/sensibilidad/efecto_regla_sistemica_inyecciones.csv) | Detecciones retenidas/enmascaradas en errores individuales y colectivos. |
| [inventario_series.csv](../Data/gold/outputs/sensibilidad/inventario_series.csv) | Rachas y elegibilidad de todas las series candidatas. |
| [ejecuciones.csv](../Data/gold/outputs/sensibilidad/ejecuciones.csv) | Escenarios, modelos, tamaños, umbrales y tiempos. |
| [modelos_IF.csv](../Data/gold/outputs/sensibilidad/modelos_IF.csv) | Modelos separados por calendario, fechas de corte y percentiles de referencia. |
| [alertas_reales_detalle.csv.gz](../Data/gold/outputs/sensibilidad/alertas_reales_detalle.csv.gz) | Una fila por escenario/serie/mes, con las once banderas de señal. |
| [inyecciones_detalle.csv.gz](../Data/gold/outputs/sensibilidad/inyecciones_detalle.csv.gz) | Casos auditables y banderas por método en t, t+1 y nuevas respecto a base. |
| [configuracion.json](../Data/gold/outputs/sensibilidad/configuracion.json) | Protocolo, versiones y huellas de entradas. |
| [manifiesto_resultados.json](../Data/gold/outputs/sensibilidad/manifiesto_resultados.json) | Huellas de los archivos entregados. |
| [analisis_sensibilidad.py](../Code/Modeling/sensibilidad/analisis_sensibilidad.py), [informe_sensibilidad.py](../Code/Modeling/sensibilidad/informe_sensibilidad.py) | Ejecución y generación de informe/figuras. |
| [test_sensibilidad.py](../Code/Modeling/sensibilidad/test_sensibilidad.py) | Pruebas de continuidad, ausencia de fuga temporal, límites y bootstrap. |
| [verificar_resultados.py](../Code/Modeling/sensibilidad/verificar_resultados.py), [verificacion.json](../Data/gold/outputs/sensibilidad/verificacion.json) | Reconciliación del detalle, denominadores, hashes y pruebas automáticas. |

El script `informe_sensibilidad.py` genera nueve gráficos en `figuras/`, en PNG, SVG y PDF.
La carpeta no se versiona porque son artefactos regenerables; se debe ejecutar el script con las
dependencias registradas en `configuracion.json` para visualizarlos.
SSPD con referencia 48 es no evaluable; XM no recibe IC entre categorías.
Los resultados describen sensibilidad, sin aprobar umbrales ni clasificar automáticamente
una señal estadística como error o cambio regulatorio.

```powershell
python desarrollo_puntos/4.2/analisis_sensibilidad.py
```


<a id="doc-7712518cbe50"></a>

## desarrollo_puntos/4.3/INFORME_METRICAS.md

### Hito 4.3 · Métricas completas y honestas

Fecha: 7 de noviembre de 2026. Corresponde a la actividad 3 del Hito 4 del plan: precisión,
recall y F1 a tasa de alerta igualada, curvas de detección contra tasa de alerta por método,
pruebas por tipo, meses distintos sorteados sin reemplazo. Completa además lo que 4.1 dejó
pendiente: métricas del Z-score robusto y del Isolation Forest con rasgos logarítmicos, y LOF/KNN.
No modifica 4.1 ni 4.2.

#### Resultado en cinco frases

1. A tasa de alerta igualada del 5 %, **I-MR, Z-score robusto, Isolation Forest y KNN no se separan de forma
   consistente**: su F1 queda entre 0,49 y 0,52 en EPM,
   entre 0,54 y 0,59 en CHEC y entre
   0,48 y 0,51 en SSPD, con intervalos que se solapan.
   De 18 diferencias pareadas evaluables frente a I-MR, el IC excluye el cero a favor
   de otro método en 1 (sin corrección por comparaciones múltiples): EPM, Z-score robusto (MAD) (Δ F1 = 0,035).
2. **LOF y R12 rinden menos que las cartas** donde se pueden evaluar. El IC de la diferencia excluye el cero para R12 en
   CHEC, SSPD y para LOF en
   SSPD; en EPM la diferencia tiene el mismo signo pero el IC
   la incluye (solo hay 5 categorías). LOF es **numéricamente degenerado en CHEC** (9.936 filas de entrenamiento, 2.126 únicas).
3. **Ningún método estadístico detecta el «valor no actualizado»**: su recall en t va de
   0,00 a 0,08 (de 0,03 a 0,16 si se admite t+1).
   Un valor repetido no es un cambio atípico; se detecta con una regla, no con una carta. Es el argumento a favor de
   «reglas + cartas» frente a cartas solas.
4. **La precisión no es una propiedad del método sino de la prevalencia de errores**, que aquí no se conoce. Por eso se
   reporta con prevalencias supuestas del 1, 5 y 10 %, y la tasa de «falsas alertas» se llama *tasa de alerta en meses reales
   sin error conocido*: no hay etiquetas externas que confirmen que esas alertas sean falsas.
5. **Las conclusiones no dependen de cómo se escriban las etiquetas de EPM.** EPM escribe de varias formas la misma etiqueta y, sin
   normalizar, sus series se fragmentan (27 series en el panel común frente a 69 con las equivalencias aprobadas internamente en el Hito 2).
   Repetido con esas equivalencias, el F1 de I-MR, Z-score, Isolation Forest y KNN queda entre 0,50 y 0,55 (antes entre 0,49 y 0,52),
   con los mismos intervalos solapados; ver la sección 3b.

#### 1. Qué se midió

**Panel.** El escenario principal de 4.2: referencia de 36 cambios, vigilancia de 12, cohorte común
(EPM 27, CHEC 276,
SSPD 321 y XM 1 series).
Las inyecciones y los modelos Isolation Forest son los mismos de 4.2: se verificó que, para cada caso,
las banderas nativas de este experimento coinciden con `4.2/inyecciones_detalle.csv.gz`
([verificacion_contra_4_2.json](../Data/gold/outputs/metricas/verificacion_contra_4_2.json)).

**Seis métodos con puntaje continuo** (más alto = más anómalo, necesario para igualar tasas):

| Método | Puntaje | Umbral nativo |
|---|---|---|
| Cartas I-MR | máx(\|c−media\|/(2,66·MR̄), \|c−anterior\|/(3,267·MR̄)) | puntaje > 1 |
| Z-score robusto | \|c−mediana\|·0,6745/MAD | \|z\| > 3 |
| Isolation Forest | −score_samples, 300 árboles, 4 rasgos | percentil 99,5 de entrenamiento |
| LOF | −score_samples (`novelty=True`, 20 vecinos), mismos rasgos | no tiene |
| KNN | distancia media a los 5 vecinos de referencia, mismos rasgos | no tiene |
| R12 | \|nivel\| / mediana de referencia | factor 5, 10 o 20 |

Modelos y escalas se ajustan solo con la referencia. Cuando MAD o MR valen cero se usa una escala de respaldo
(desviación absoluta media, luego desviación estándar) **solo para ordenar puntajes**; la regla nativa de 4.1
para MAD cero se conserva en la verificación contra 4.2 (sin discrepancias en series con escala positiva).

**Tasa de alerta igualada.** Para cada fuente, método y tasa objetivo (1, 2, 5 y 10 %) el umbral es el puntaje que deja esa
fracción de las observaciones **reales** de vigilancia por encima. No usa etiquetas. Así todos los métodos alertan lo mismo
sobre los datos reales y solo pueden diferenciarse por cuánto detectan de lo inyectado. Los empates pueden dejar la tasa
observada ligeramente por debajo de la objetivo; se reporta en [umbrales_tasa_igualada.csv](../Data/gold/outputs/metricas/umbrales_tasa_igualada.csv).

**Etiquetas.** Positivo: el valor inyectado en el mes t. Negativo: las observaciones reales sin inyección, que incluyen alertas
reales sin error conocido (supuesto conservador: pueden contener errores verdaderos, de modo que la precisión es un límite
inferior). Horizonte *t*: alerta en el mes inyectado; horizonte *t o t+1*: alerta en cualquiera de los dos, con la tasa de
alerta real medida sobre pares de meses consecutivos para que el criterio sea el mismo en positivos y negativos.

**Métricas.** El recall global es **macro**: promedio de los recall de los seis tipos con el mismo peso, de modo que ningún
tipo domine por tener más casos. La precisión se obtiene de recall y tasa de alerta real para una prevalencia supuesta
π: `P = R·π / (R·π + FPR·(1−π))`, y F1 es su media armónica con el recall. Los intervalos son bootstrap de
**categorías completas** (1.000 repeticiones, TPR y tasa de alerta remuestreados juntos); sin IC cuando hay una sola categoría.

#### 2. Pruebas por tipo y meses distintos (observación 6 de la revisión)

La revisión del Hito 2 señaló que 20 sorteos por serie y tipo caían en 13 meses distintos en promedio y que «columna
equivocada» tenía 760 pruebas frente a 1.540 de los otros tipos. Aquí se reportan los denominadores reales y el sorteo se hace
**sin reemplazo**: en cada réplica, cada serie recibe 3 meses de origen distintos y un tipo de
error uniforme entre los disponibles ese mes (500 réplicas). La condición de meses distintos se
verifica con una aserción en cada ejecución y con pruebas unitarias.

| Fuente | Tipo | Casos exhaustivos | Series | Categorías | Meses de calendario distintos | Pruebas por réplica (sorteo) |
|---|---|---|---|---|---|---|
| EPM | decimal_x1000 | 297 | 27 | 5 | 11 | 14,9 |
| EPM | decimal_div1000 | 297 | 27 | 5 | 11 | 14,9 |
| EPM | serial_excel_43577 | 297 | 27 | 5 | 11 | 15,3 |
| EPM | aumento_10pct | 297 | 27 | 5 | 11 | 15,1 |
| EPM | valor_no_actualizado | 297 | 27 | 5 | 11 | 15,0 |
| EPM | otra_medida | 132 | 12 | 4 | 11 | 5,8 |
| CHEC | decimal_x1000 | 3.036 | 276 | 4 | 22 | 147,4 |
| CHEC | decimal_div1000 | 3.036 | 276 | 4 | 22 | 147,9 |
| CHEC | serial_excel_43577 | 3.036 | 276 | 4 | 22 | 147,6 |
| CHEC | aumento_10pct | 3.036 | 276 | 4 | 22 | 148,3 |
| CHEC | valor_no_actualizado | 2.979 | 276 | 4 | 22 | 145,6 |
| CHEC | otra_medida | 1.980 | 180 | 4 | 22 | 91,2 |
| SSPD | decimal_x1000 | 3.531 | 321 | 89 | 19 | 162,8 |
| SSPD | decimal_div1000 | 3.531 | 321 | 89 | 19 | 164,7 |
| SSPD | serial_excel_43577 | 3.531 | 321 | 89 | 19 | 163,1 |
| SSPD | aumento_10pct | 3.531 | 321 | 89 | 19 | 163,2 |
| SSPD | valor_no_actualizado | 3.351 | 315 | 89 | 19 | 153,7 |
| SSPD | otra_medida | 3.405 | 311 | 88 | 19 | 155,4 |
| XM | decimal_x1000 | 11 | 1 | 1 | 11 | 0,6 |
| XM | decimal_div1000 | 11 | 1 | 1 | 11 | 0,6 |
| XM | serial_excel_43577 | 11 | 1 | 1 | 11 | 0,6 |
| XM | aumento_10pct | 11 | 1 | 1 | 11 | 0,6 |
| XM | valor_no_actualizado | 11 | 1 | 1 | 11 | 0,5 |
| XM | otra_medida | 0 | 0 | 0 | 0 | 0,0 |

«Otra medida» solo existe donde la serie tiene otra medida positiva en el mismo grupo y mes (en EPM, 12 de 27 series; en XM
ninguna), y «valor no actualizado» se omite cuando el valor anterior es igual al actual. Omisiones registradas en
[inyecciones_omitidas.csv](../Data/gold/outputs/metricas/inyecciones_omitidas.csv): EPM/otra_medida: 165 (sin otra medida positiva distinta); CHEC/otra_medida: 1056 (sin otra medida positiva distinta); CHEC/valor_no_actualizado: 57 (la alteracion no cambia el valor); SSPD/otra_medida: 126 (sin otra medida positiva distinta); SSPD/valor_no_actualizado: 180 (la alteracion no cambia el valor); XM/otra_medida: 11 (sin otra medida positiva distinta); EPM_canonicas/otra_medida: 363 (sin otra medida positiva distinta).

**Las pruebas siguen sin ser independientes**: los casos de una misma serie comparten referencia, escala y modelo, y las
series de una categoría están correlacionadas. Por eso los intervalos remuestrean categorías completas y no casos.

Consistencia del sorteo con el cálculo exhaustivo (I-MR, 5 %, horizonte t):

| Fuente | Pruebas por réplica | Recall del sorteo (media) | Rango 95 % entre réplicas | Recall exhaustivo macro | Diferencia |
|---|---|---|---|---|---|
| EPM | 81 | 0,678 | 0,574–0,778 | 0,629 | 0,049 |
| CHEC | 828 | 0,775 | 0,749–0,803 | 0,785 | -0,009 |
| SSPD | 963 | 0,668 | 0,641–0,694 | 0,663 | 0,005 |
| XM | 3 | 0,720 | 0,333–1,000 | 0,691 | 0,029 |
| EPM_canonicas | 207 | 0,694 | 0,630–0,754 | 0,654 | 0,040 |

La diferencia absoluta máxima entre el sorteo y el cálculo exhaustivo es de 0,062. Aparece en EPM porque el
sorteo reparte los tipos uniformemente **entre los disponibles de cada mes** y «otra medida» está disponible en menos series;
no es un error de cálculo.

#### 3. Precisión, recall y F1 a tasa de alerta del 5 %

Horizonte t, prevalencia supuesta del 5 %. La fila «Tasa de alerta real» es la tasa observada sobre meses reales tras igualar.

**EPM** (5 categorías; el IC es amplio porque hay pocas):

| Método | Recall macro [IC 95 %] | Tasa de alerta real | Precisión conservadora [IC] | F1 [IC] | Estado |
|---|---|---|---|---|---|
| Cartas I-MR | 0,63 [0,59–0,67] | 4,9 % | 0,40 [0,21–1,00] | 0,49 [0,31–0,80] | evaluable |
| Z-score robusto (MAD) | 0,67 [0,61–0,71] | 4,6 % | 0,43 [0,24–1,00] | 0,52 [0,34–0,82] | evaluable |
| Isolation Forest | 0,62 [0,61–0,67] | 4,6 % | 0,41 [0,24–1,00] | 0,49 [0,35–0,80] | evaluable |
| LOF | 0,54 [0,51–0,63] | 4,9 % | 0,37 [0,15–0,67] | 0,44 [0,23–0,59] | evaluable |
| KNN (distancia media, k=5) | 0,65 [0,62–0,68] | 4,9 % | 0,41 [0,25–1,00] | 0,50 [0,35–0,80] | evaluable |
| R12 (magnitud del nivel) | 0,36 [0,33–0,37] | 4,6 % | 0,29 [0,21–1,00] | 0,32 [0,27–0,52] | evaluable |

**CHEC** (4 categorías):

| Método | Recall macro [IC 95 %] | Tasa de alerta real | Precisión conservadora [IC] | F1 [IC] | Estado |
|---|---|---|---|---|---|
| Cartas I-MR | 0,78 [0,77–0,79] | 4,9 % | 0,46 [0,44–0,51] | 0,58 [0,57–0,62] | evaluable |
| Z-score robusto (MAD) | 0,81 [0,80–0,82] | 5,0 % | 0,46 [0,39–0,88] | 0,59 [0,52–0,85] | evaluable |
| Isolation Forest | 0,70 [0,66–0,72] | 4,8 % | 0,43 [0,35–1,00] | 0,54 [0,47–0,80] | evaluable |
| LOF | 0,01 [0,00–0,02] | 4,8 % | 0,01 [0,01–0,01] | 0,01 [0,01–0,02] | degenerado_por_duplicados |
| KNN (distancia media, k=5) | 0,75 [0,71–0,77] | 5,0 % | 0,44 [0,36–1,00] | 0,56 [0,49–0,84] | evaluable |
| R12 (magnitud del nivel) | 0,44 [0,41–0,45] | 4,8 % | 0,32 [0,25–1,00] | 0,37 [0,32–0,58] | evaluable |

**SSPD** (89 categorías):

| Método | Recall macro [IC 95 %] | Tasa de alerta real | Precisión conservadora [IC] | F1 [IC] | Estado |
|---|---|---|---|---|---|
| Cartas I-MR | 0,66 [0,65–0,68] | 5,0 % | 0,41 [0,36–0,49] | 0,51 [0,46–0,56] | evaluable |
| Z-score robusto (MAD) | 0,67 [0,66–0,69] | 5,0 % | 0,41 [0,36–0,48] | 0,51 [0,47–0,56] | evaluable |
| Isolation Forest | 0,63 [0,62–0,65] | 5,0 % | 0,40 [0,34–0,49] | 0,49 [0,44–0,55] | evaluable |
| LOF | 0,42 [0,37–0,47] | 5,0 % | 0,31 [0,24–0,44] | 0,35 [0,30–0,42] | evaluable |
| KNN (distancia media, k=5) | 0,61 [0,59–0,63] | 5,0 % | 0,39 [0,31–0,50] | 0,48 [0,41–0,55] | evaluable |
| R12 (magnitud del nivel) | 0,28 [0,27–0,29] | 5,0 % | 0,23 [0,16–0,35] | 0,25 [0,21–0,31] | evaluable |

**XM** (una serie y 12 observaciones: con un 5 % de tasa objetivo se esperan 0,6 alertas, por lo que la tasa de alerta real
es 0 % y la precisión sale 100 % por construcción; **no es interpretable**, se conserva solo como evidencia descriptiva):

| Método | Recall macro [IC 95 %] | Tasa de alerta real | Precisión conservadora [IC] | F1 [IC] | Estado |
|---|---|---|---|---|---|
| Cartas I-MR | 0,69 | 0,0 % | — | — | no_interpretable_baja_resolucion |
| Z-score robusto (MAD) | 0,73 | 0,0 % | — | — | no_interpretable_baja_resolucion |
| Isolation Forest | 0,75 | 0,0 % | — | — | no_interpretable_baja_resolucion |
| LOF | 0,78 | 0,0 % | — | — | no_interpretable_baja_resolucion |
| KNN (distancia media, k=5) | 0,80 | 0,0 % | — | — | no_interpretable_baja_resolucion |
| R12 (magnitud del nivel) | 0,40 | 0,0 % | — | — | no_interpretable_baja_resolucion |

*Figura regenerable:* `python desarrollo_puntos/4.3/informe_metricas.py` crea
`figuras/02_f1_por_metodo.png`. Las figuras no se versionan; la tabla anterior contiene sus
valores auditables.

##### Diferencias pareadas frente a I-MR

I-MR es el método clásico del proyecto (el que sustituye a la regla estática). Las diferencias usan las mismas categorías
remuestreadas en ambos métodos, por lo que son más informativas que comparar dos intervalos por separado:

| Fuente | Método | Δ recall | Δ F1 frente a I-MR [IC 95 %] | IC excluye 0 | Estado |
|---|---|---|---|---|---|
| EPM | Z-score robusto (MAD) | 0,039 | 0,035 [0,008; 0,052] | sí | evaluable |
| EPM | Isolation Forest | -0,014 | 0,003 [-0,025; 0,037] | no | evaluable |
| EPM | LOF | -0,087 | -0,053 [-0,557; 0,167] | no | evaluable |
| EPM | KNN (distancia media, k=5) | 0,019 | 0,011 [-0,007; 0,041] | no | evaluable |
| EPM | R12 (magnitud del nivel) | -0,272 | -0,171 [-0,300; 0,208] | no | evaluable |
| CHEC | Z-score robusto (MAD) | 0,024 | 0,007 [-0,044; 0,230] | no | evaluable |
| CHEC | Isolation Forest | -0,080 | -0,042 [-0,096; 0,200] | no | evaluable |
| CHEC | LOF | -0,772 | -0,567 [-0,577; -0,549] | sí | degenerado_por_duplicados |
| CHEC | KNN (distancia media, k=5) | -0,033 | -0,021 [-0,080; 0,234] | no | evaluable |
| CHEC | R12 (magnitud del nivel) | -0,349 | -0,207 [-0,245; -0,015] | sí | evaluable |
| SSPD | Z-score robusto (MAD) | 0,007 | 0,004 [-0,036; 0,039] | no | evaluable |
| SSPD | Isolation Forest | -0,030 | -0,017 [-0,078; 0,039] | no | evaluable |
| SSPD | LOF | -0,245 | -0,155 [-0,225; -0,083] | sí | evaluable |
| SSPD | KNN (distancia media, k=5) | -0,057 | -0,033 [-0,099; 0,038] | no | evaluable |
| SSPD | R12 (magnitud del nivel) | -0,387 | -0,259 [-0,325; -0,190] | sí | evaluable |

Con tan pocas categorías (EPM, CHEC) los intervalos son anchos y apenas permiten rechazar nada; con 89 categorías (SSPD)
sí se distingue que LOF y R12 pierden frente a I-MR y que IF, KNN y Z-score no se distinguen de él.
Son 5 métodos × 3 fuentes por configuración y no se aplicó corrección por comparaciones múltiples; léase como exploración.

##### 3b. Sensibilidad: EPM con etiquetas canónicas

EPM cambia la escritura de varias etiquetas entre meses (p. ej. «Costo compra: Gm, i» y «Costo Compra: Gm, i», o «Rango 0 - CS» y «0-CS»). Si no se
normalizan, una misma serie económica se parte en varias, y el panel común (series con 61 meses continuos) se reduce. Se repitió el experimento completo con las
11 equivalencias del Hito 2 ([02_catalogo_variantes.csv](../Data/silver/outputs/adaptadores/insumos_hito2/02_catalogo_variantes.csv), aprobadas internamente por el equipo, aplicadas en una copia de trabajo) como una
fuente adicional, `EPM_canonicas`. **No sustituye a EPM**: 4.1, 4.2 y la matriz OE1 usan las etiquetas originales y la variante canónica no existe en 4.2, por lo que no se
compara con él.

| | EPM (originales) | EPM (canónicas) |
|---|---|---|
| Series en el panel común | 27 | 69 |
| Categorías | 5 | 6 |
| Observaciones reales de vigilancia | 324 | 828 |
| Casos inyectados | 1.617 | 4.191 |

F1 a tasa del 5 %, prevalencia supuesta del 5 %, horizonte t:

| Método | F1 EPM (etiquetas originales) | F1 EPM (etiquetas canónicas) [IC] | Δ F1 frente a I-MR (canónicas) [IC] | Estado (canónicas) |
|---|---|---|---|---|
| Cartas I-MR | 0,49 | 0,50 [0,44–0,66] | — | evaluable |
| Z-score robusto (MAD) | 0,52 | 0,55 [0,42–0,82] | 0,042 [-0,136; 0,339] | evaluable |
| Isolation Forest | 0,49 | 0,51 [0,42–0,74] | 0,010 [-0,155; 0,242] | evaluable |
| LOF | 0,44 | 0,41 [0,35–0,47] | -0,099 [-0,257; -0,037] | degenerado_por_duplicados |
| KNN (distancia media, k=5) | 0,50 | 0,52 [0,40–0,82] | 0,014 [-0,159; 0,350] | evaluable |
| R12 (magnitud del nivel) | 0,32 | 0,33 [0,27–0,50] | -0,172 [-0,332; 0,025] | evaluable |

- **El orden y las conclusiones se mantienen.** I-MR, Z-score, Isolation Forest y KNN siguen sin separarse (intervalos solapados; las diferencias pareadas frente a I-MR no excluyen el cero para ningún método evaluable); R12 sigue siendo el más bajo.
- **El F1 sube ligeramente** (entre +0,01 y +0,02 según el método) con más series y casos; no se probó la causa del aumento. Con solo 6 categorías los intervalos siguen siendo anchos.
- **LOF pasa a degenerado también en EPM** (2.484 filas de entrenamiento, 1.220 únicas; 3,3 % de los puntajes reales estallan) y se marca como tal.
- Decidir si estas equivalencias se aceptan como oficiales y si hay que repetir 4.1 y 4.2 con ellas es **decisión del equipo y del director**; mientras tanto el resultado principal sigue usando las etiquetas originales.

#### 4. Curvas de detección contra tasa de alerta

*Figura regenerable:* `informe_metricas.py` crea `figuras/01_curvas_deteccion.png`; los datos
auditables permanecen en [curva_deteccion.csv](../Data/gold/outputs/metricas/curva_deteccion.csv).

Datos en [curva_deteccion.csv](../Data/gold/outputs/metricas/curva_deteccion.csv) (40 tasas entre 0,25 y 30 %). Las curvas no tienen IC: son el recall
macro exhaustivo en cada punto. Se omiten los puntos con menos de 5 alertas esperadas y LOF en CHEC.

#### 5. Recall por tipo de error

*Figura regenerable:* `informe_metricas.py` crea `figuras/03_recall_por_tipo.png`; los valores
auditables permanecen en [deteccion_por_tipo_tasa_igualada.csv](../Data/gold/outputs/metricas/deteccion_por_tipo_tasa_igualada.csv).

Tabla comparativa con IC 95 % por técnica y tipo de error (horizonte t, tasa 5 %). El resto de tasas y el horizonte
t o t+1 están en [deteccion_por_tipo_tasa_igualada.csv](../Data/gold/outputs/metricas/deteccion_por_tipo_tasa_igualada.csv).

**EPM**

| Tipo | Cartas I-MR | Z-score robusto (MAD) | Isolation Forest | LOF | KNN (distancia media, k=5) | R12 (magnitud del nivel) |
|---|---|---|---|---|---|---|
| decimal_x1000 | 1,00 [1,00–1,00] | 1,00 [1,00–1,00] | 1,00 [1,00–1,00] | 1,00 [1,00–1,00] | 1,00 [1,00–1,00] | 1,00 [1,00–1,00] |
| decimal_div1000 | 1,00 [1,00–1,00] | 1,00 [1,00–1,00] | 1,00 [1,00–1,00] | 1,00 [1,00–1,00] | 1,00 [1,00–1,00] | 0,00 [0,00–0,00] |
| serial_excel_43577 | 1,00 [1,00–1,00] | 1,00 [1,00–1,00] | 1,00 [1,00–1,00] | 1,00 [1,00–1,00] | 1,00 [1,00–1,00] | 1,00 [1,00–1,00] |
| aumento_10pct | 0,61 [0,44–1,00] | 0,71 [0,55–1,00] | 0,61 [0,44–1,00] | 0,07 [0,00–0,33] | 0,70 [0,56–0,99] | 0,09 [0,00–0,13] |
| valor_no_actualizado | 0,00 [0,00–0,00] | 0,00 [0,00–0,00] | 0,02 [0,00–0,05] | 0,08 [0,02–0,23] | 0,04 [0,00–0,11] | 0,03 [0,00–0,05] |
| otra_medida | 0,17 [0,00–0,50] | 0,30 [0,00–0,64] | 0,06 [0,00–0,18] | 0,10 [0,00–0,20] | 0,15 [0,00–0,45] | 0,02 [0,00–0,07] |

**CHEC**

| Tipo | Cartas I-MR | Z-score robusto (MAD) | Isolation Forest | LOF | KNN (distancia media, k=5) | R12 (magnitud del nivel) |
|---|---|---|---|---|---|---|
| decimal_x1000 | 1,00 [1,00–1,00] | 1,00 [1,00–1,00] | 1,00 [1,00–1,00] | n/d | 1,00 [1,00–1,00] | 1,00 [1,00–1,00] |
| decimal_div1000 | 1,00 [1,00–1,00] | 1,00 [1,00–1,00] | 1,00 [1,00–1,00] | n/d | 1,00 [1,00–1,00] | 0,00 [0,00–0,00] |
| serial_excel_43577 | 1,00 [1,00–1,00] | 1,00 [1,00–1,00] | 1,00 [1,00–1,00] | n/d | 1,00 [1,00–1,00] | 1,00 [1,00–1,00] |
| aumento_10pct | 0,76 [0,62–0,80] | 0,92 [0,83–0,94] | 0,39 [0,12–0,50] | n/d | 0,57 [0,37–0,65] | 0,23 [0,13–0,27] |
| valor_no_actualizado | 0,01 [0,00–0,01] | 0,00 [0,00–0,00] | 0,02 [0,00–0,02] | n/d | 0,03 [0,00–0,05] | 0,03 [0,00–0,04] |
| otra_medida | 0,94 [0,92–0,99] | 0,93 [0,91–1,00] | 0,82 [0,81–0,87] | n/d | 0,91 [0,90–0,92] | 0,36 [0,30–0,38] |

**SSPD**

| Tipo | Cartas I-MR | Z-score robusto (MAD) | Isolation Forest | LOF | KNN (distancia media, k=5) | R12 (magnitud del nivel) |
|---|---|---|---|---|---|---|
| decimal_x1000 | 1,00 [1,00–1,00] | 1,00 [1,00–1,00] | 0,99 [0,98–1,00] | 0,63 [0,56–0,71] | 0,98 [0,97–0,99] | 1,00 [1,00–1,00] |
| decimal_div1000 | 1,00 [1,00–1,00] | 1,00 [1,00–1,00] | 0,99 [0,99–1,00] | 0,74 [0,67–0,81] | 0,97 [0,95–0,99] | 0,00 [0,00–0,00] |
| serial_excel_43577 | 0,89 [0,86–0,92] | 0,89 [0,86–0,92] | 0,81 [0,77–0,85] | 0,50 [0,43–0,57] | 0,75 [0,72–0,80] | 0,22 [0,18–0,25] |
| aumento_10pct | 0,16 [0,12–0,21] | 0,22 [0,17–0,28] | 0,14 [0,10–0,19] | 0,09 [0,05–0,13] | 0,12 [0,08–0,17] | 0,06 [0,03–0,09] |
| valor_no_actualizado | 0,02 [0,01–0,03] | 0,00 [0,00–0,00] | 0,03 [0,02–0,04] | 0,04 [0,02–0,06] | 0,03 [0,02–0,05] | 0,05 [0,03–0,08] |
| otra_medida | 0,91 [0,87–0,94] | 0,91 [0,87–0,94] | 0,84 [0,79–0,89] | 0,52 [0,45–0,60] | 0,79 [0,73–0,84] | 0,33 [0,29–0,38] |

#### 6. Por qué igualar la tasa (puntos operativos nativos frente a tasa igualada)

Con su umbral nativo cada método alerta con una frecuencia distinta; comparar sus F1 así mezcla la calidad del puntaje con
la elección del umbral. Por ejemplo, el Isolation Forest con percentil 99,5 casi no alerta en EPM y por eso detecta poco en 4.2,
pero con la misma tasa de alerta que las cartas su recall es comparable:

| Fuente | Método | Umbral nativo | Tasa de alerta nativa | Recall nativo | F1 nativo | Recall al 5 % | F1 al 5 % |
|---|---|---|---|---|---|---|---|
| EPM | Cartas I-MR | puntaje>1 (2,66 y 3,267 del plan) | 5,56 % | 0,64 | 0,47 | 0,63 | 0,49 |
| EPM | Z-score robusto (MAD) | |z|>3 | 3,70 % | 0,64 | 0,55 | 0,67 | 0,52 |
| EPM | Isolation Forest | percentil 99,5 de entrenamiento | 0,00 % | 0,05 | 0,09 | 0,62 | 0,49 |
| EPM | R12 (magnitud del nivel) | nivel>10 x mediana | 0,00 % | 0,33 | 0,50 | 0,36 | 0,32 |
| CHEC | Cartas I-MR | puntaje>1 (2,66 y 3,267 del plan) | 0,00 % | 0,64 | 0,78 | 0,78 | 0,58 |
| CHEC | Z-score robusto (MAD) | |z|>3 | 0,00 % | 0,73 | 0,85 | 0,81 | 0,59 |
| CHEC | Isolation Forest | percentil 99,5 de entrenamiento | 0,00 % | 0,55 | 0,71 | 0,70 | 0,54 |
| CHEC | R12 (magnitud del nivel) | nivel>10 x mediana | 0,00 % | 0,33 | 0,50 | 0,44 | 0,37 |
| SSPD | Cartas I-MR | puntaje>1 (2,66 y 3,267 del plan) | 4,60 % | 0,66 | 0,52 | 0,66 | 0,51 |
| SSPD | Z-score robusto (MAD) | |z|>3 | 7,24 % | 0,69 | 0,45 | 0,67 | 0,51 |
| SSPD | Isolation Forest | percentil 99,5 de entrenamiento | 0,47 % | 0,41 | 0,55 | 0,63 | 0,49 |
| SSPD | R12 (magnitud del nivel) | nivel>10 x mediana | 0,13 % | 0,23 | 0,37 | 0,28 | 0,25 |

(Prevalencia supuesta 5 %, horizonte t. Los puntos nativos no llevan IC. En CHEC (y en XM, no mostrado) la tasa nativa de
I-MR y Z-score es 0 % sobre meses reales, de modo que su precisión es 100 % por construcción y su F1 nativo no es comparable
con el igualado. Los puntos nativos de todas las fuentes están en [puntos_operativos_nativos.csv](../Data/gold/outputs/metricas/puntos_operativos_nativos.csv).)

#### 7. Lo que no se puede concluir

- **No hay verdad terreno para las alertas reales.** Las inyecciones son artificiales y siguen la mezcla diseñada (seis tipos
  uniformes); no estiman la prevalencia ni el tipo de errores que existe en las fuentes.
- **La precisión depende de la prevalencia supuesta**; el informe no elige una. Con prevalencia baja la precisión de todos los
  métodos cae, porque la tasa de alerta real (5 %) pesa más que los positivos.
- **XM no es evaluable a tasa igualada** (una serie, 12 meses). **CHEC y EPM tienen pocas categorías** (4 y 5): sus IC son
  anchos y los contrastes entre métodos tienen poca potencia.
- **LOF en CHEC está degenerado** por duplicados exactos en el entrenamiento: con más duplicados que vecinos, la densidad local
  diverge y el puntaje estalla (~10⁹–10¹⁰). Se conserva el cálculo y se marca `degenerado_por_duplicados`. Una corrección
  (eliminar duplicados o aumentar vecinos) cambia el significado de densidad y queda como decisión del equipo.
- **El experimento es retrospectivo** (se mira t+1 y los rasgos usan el cambio anterior), válido para auditar datos ya
  publicados y no para vigilancia en tiempo real.
- **Los umbrales por tasa igualada se calibran en los mismos meses reales** donde luego se miden las falsas alertas (sin
  etiquetas, pero sin separación temporal): describe cómo se comportan los métodos a igual tasa, no una tasa futura garantizada.
- **Las equivalencias de etiquetas de EPM son una aprobación interna del equipo**, no una confirmación de EPM (sección 3b).
- **No se aprobó ningún umbral ni método.** Los resultados no confirman que una señal sea un error ni un cambio regulatorio.

#### 8. Qué cierra de los pendientes de 4.1

Quedan resueltos aquí: precisión, recall y F1 del Z-score robusto y del Isolation Forest de 4.2 (rasgos logarítmicos);
LOF y KNN, que el plan pedía y no existían; comparación a tasa igualada **sobre las mismas inyecciones** de 4.2 para los seis
métodos; detección en t frente a t o t+1 con ambos horizontes. **Siguen abiertos**: Extended Isolation Forest
(el plan lo condiciona al tiempo), validación externa de alertas reales y aprobación del tratamiento de MAD igual a cero.

#### Reproducir y auditar

Desde la raíz del proyecto:

```powershell
python desarrollo_puntos/4.3/experimento_tasa_igualada.py
python desarrollo_puntos/4.3/informe_metricas.py
python -m unittest discover -s desarrollo_puntos/4.3 -p test_metricas.py -v
python desarrollo_puntos/4.3/verificar_resultados.py
```

[configuracion.json](../Data/gold/outputs/metricas/configuracion.json) fija semilla, versiones, definiciones y huellas de las entradas;
[manifiesto_resultados.json](../Data/gold/outputs/metricas/manifiesto_resultados.json) lista las huellas de todos los archivos entregados.


<a id="doc-a66acf433abb"></a>

## desarrollo_puntos/4.3/README.md

### 4.3 · Métricas completas y honestas

La lectura principal está en [INFORME_METRICAS.md](REFERENCIA_TECNICA.md#doc-7712518cbe50). Corresponde a la actividad 3 del Hito 4:
precisión, recall y F1 a tasa de alerta igualada, curvas de detección contra tasa de alerta por método, pruebas por tipo
y meses distintos sorteados sin reemplazo. Reutiliza las inyecciones y los modelos de [4.2](REFERENCIA_TECNICA.md#doc-15dec98a30e1) y completa
lo que [4.1](REFERENCIA_TECNICA.md#doc-81f243d988ee) dejó pendiente (métricas del Z-score robusto y del Isolation Forest, LOF y KNN).
No modifica 4.1 ni 4.2; solo escribe en esta carpeta.

| Archivo | Contenido |
|---|---|
| [metricas_globales.csv](../Data/gold/outputs/metricas/metricas_globales.csv) | Recall macro, tasa de alerta real, precisión y F1 con IC 95 % por fuente, método, tasa igualada (1, 2, 5 y 10 %), horizonte (t y t o t+1) y prevalencia supuesta (1, 5 y 10 %). |
| [deteccion_por_tipo_tasa_igualada.csv](../Data/gold/outputs/metricas/deteccion_por_tipo_tasa_igualada.csv) | Recall por tipo de error con casos, series, categorías e IC: la tabla comparativa por técnica y tipo de error. |
| [diferencias_vs_IMR.csv](../Data/gold/outputs/metricas/diferencias_vs_IMR.csv) | Diferencias pareadas de recall y F1 frente a la carta I-MR, con IC por categorías. |
| [curva_deteccion.csv](../Data/gold/outputs/metricas/curva_deteccion.csv) | Recall macro frente a tasa de alerta en 40 tasas (0,25–30 %). |
| [umbrales_tasa_igualada.csv](../Data/gold/outputs/metricas/umbrales_tasa_igualada.csv) | Umbral de cada método y tasa objetivo, alertas reales y tasa observada. |
| [puntos_operativos_nativos.csv](../Data/gold/outputs/metricas/puntos_operativos_nativos.csv) | Cada método con su umbral propio (I-MR > 1, \|z\| > 3, IF p99,5, R12 > 10), para contrastar con la tasa igualada. |
| [pruebas_por_tipo.csv](../Data/gold/outputs/metricas/pruebas_por_tipo.csv), [sorteo_sin_reemplazo.csv](../Data/gold/outputs/metricas/sorteo_sin_reemplazo.csv) | Denominadores reales por tipo y sorteo con meses distintos, frente al cálculo exhaustivo. |
| [cobertura_experimento.csv](../Data/gold/outputs/metricas/cobertura_experimento.csv), [inyecciones_omitidas.csv](../Data/gold/outputs/metricas/inyecciones_omitidas.csv) | Series, categorías, observaciones, duplicados de entrenamiento, estado de LOF y casos omitidos. |
| [puntajes_reales.csv.gz](../Data/gold/outputs/metricas/puntajes_reales.csv.gz), [puntajes_inyecciones.csv.gz](../Data/gold/outputs/metricas/puntajes_inyecciones.csv.gz) | Puntajes continuos de los seis métodos (observaciones reales y casos inyectados): permiten rehacer umbrales y métricas sin reentrenar. |
| [ejecuciones.csv](../Data/gold/outputs/metricas/ejecuciones.csv) | Tiempos por etapa y fuente. |
| [metricas_base.py](../Code/Modeling/metricas/metricas_base.py) | Funciones puras: puntajes, umbral por tasa, precisión, F1 y sorteo sin reemplazo. |
| [experimento_tasa_igualada.py](../Code/Modeling/metricas/experimento_tasa_igualada.py), [informe_metricas.py](../Code/Modeling/metricas/informe_metricas.py) | Ejecución del experimento; generación de figuras e informe desde las tablas. |
| [test_metricas.py](../Code/Modeling/metricas/test_metricas.py) | Doce pruebas de propiedades. |
| [verificar_resultados.py](../Code/Modeling/metricas/verificar_resultados.py), [verificacion.json](../Data/gold/outputs/metricas/verificacion.json), [verificacion_contra_4_2.json](../Data/gold/outputs/metricas/verificacion_contra_4_2.json) | Recalcula umbrales, detecciones, FPR, precisión y F1 desde los puntajes; compara las banderas nativas con las de 4.2. |
| [configuracion.json](../Data/gold/outputs/metricas/configuracion.json), [manifiesto_resultados.json](../Data/gold/outputs/metricas/manifiesto_resultados.json) | Protocolo, semilla, versiones y huellas de entradas y salidas. |

El script `informe_metricas.py` genera tres gráficos en `figuras/`, en PNG, SVG y PDF. La carpeta
no se versiona porque son artefactos regenerables; se debe ejecutar el script con las dependencias
registradas en `configuracion.json` para visualizarlos.
XM tiene una sola serie y 12 observaciones: se reporta como descriptivo y no es interpretable a tasa igualada.
LOF queda marcado como degenerado en CHEC (entrenamiento con muchos duplicados exactos).
La fuente `EPM_canonicas` es una variante de sensibilidad con las equivalencias de etiquetas del Hito 2 (11 equivalencias aprobadas internamente): no sustituye a EPM y no existe en 4.2.
Los resultados no aprueban umbrales ni clasifican una señal real como error.

```powershell
python desarrollo_puntos/4.3/experimento_tasa_igualada.py
python desarrollo_puntos/4.3/informe_metricas.py
python -m unittest discover -s desarrollo_puntos/4.3 -p test_metricas.py -v
python desarrollo_puntos/4.3/verificar_resultados.py
```


<a id="doc-4ce62780cc42"></a>

## desarrollo_puntos/4.4/INFORME_REGLA_SISTEMICA.md

### Hito 4.4 · Regla de alerta sistémica

Fecha: 7 de noviembre de 2026. Corresponde a la actividad 4 del Hito 4: *«Si más de X % de las series alertan en el
mismo mes, se clasifica como cambio regulatorio y no como error de dato; calibrar X con feb-2020 (51 de 83), jul-2020 (24)
y jul-2021 (18). Contrastar con resoluciones CREG y publicaciones tarifarias de EPM de esos meses»*. Entrega el catálogo
de alertas sistémicas del Hito 4. No modifica 4.1, 4.2 ni 4.3.

#### Resultado en seis frases

1. **Se reproducen las cifras del plan** desde los archivos del Hito 2: 51 de 83 series en feb-2020 (61,4 %),
   24 en jul-2020 (28,9 %) y 18 en jul-2021 (21,7 %). Pero provienen de un protocolo distinto
   al del Hito 3 (origen fijo y diferencia absoluta). Con cambios logarítmicos y ventana móvil, **solo febrero de 2020 es sistémico
   en todas las variantes** (49 %–67 % de las series); jul-2020 (6 %–44 %) y
   jul-2021 (0 %–16 %) dependen de la ventana, del método y de las etiquetas.
2. **X no se puede calibrar de forma única con esos tres meses**: en ninguna variante hay un X que capture los tres sin marcar otros.
   Incluso con las cifras del Hito 2, abril de 2020 (24,1 %) supera a jul-2021 (21,7 %): un X por debajo de 21,7 %
   los captura a los tres pero también marca abril. Los tres meses tampoco son del mismo tipo: involucran
   11, 5 y
   3 componentes tarifarios, respectivamente.
3. **Se propone X = 25 % como valor de trabajo, no aprobado.** En las cuatro variantes con etiquetas canónicas solo marca meses del plan (ningún otro mes),
   enmascara como máximo 8,2 % de los errores individuales inyectados (con X = 10 % llega a 26,2 %) y
   reclasifica entre 28 % y 53 % de las alertas reales de EPM (según el método).
4. **Contraste externo.** Las publicaciones oficiales de EPM leídas (ene, feb, jun y jul de 2020; jun y jul de 2021) muestran que los
   componentes que alertan son los que cambiaron: en feb-2020 el costo G,T y pérdidas (+25,8 %) y la distribución (+7,8 %); en
   jul-2020 el transporte STN (−20,3 %), el margen de comercialización (+7,2 %) y la distribución (+5,2 %); en jul-2021 el transporte STN
   (−13,3 %), que es **un solo componente** (con I-MR, las 15 series de ese componente), y Restricciones (+147 %, según el Hito 2). Los valores del CSV
   coinciden con las publicaciones, de modo que no son errores de captura. Además CHEC alerta con **270 de 270 series
   en feb-2020** (I-MR, ref. 36): el fenómeno no es exclusivo de EPM.
5. **La regla no debe descartar alertas, solo reclasificarlas para revisión.** A X = 25 % la simulación de 4.2 oculta
   80 %–100 % de los errores *colectivos* (un error masivo en el mismo mes, p. ej. ×1000 en todas las series, es
   indistinguible de un cambio regulatorio solo por fracción): el rótulo es «candidato sistémico» y confirmarlo exige el contraste con la publicación.
6. **Hallazgo colateral que afecta a 4.1 y 4.2:** EPM cambia la escritura de varias etiquetas entre meses (p. ej. «Costo compra: Gm, i» y
   «Costo Compra: Gm, i») y, sin normalizarlas, una misma serie se parte: 266 series con etiquetas originales frente a
   200 con las equivalencias aprobadas internamente en el Hito 2 ([inventario_series_por_variante.csv](../Data/gold/outputs/regla_sistemica/inventario_series_por_variante.csv)). Aquí se usan las canónicas como variante principal y las originales como sensibilidad.

#### 1. La regla

Para una fuente y un mes: `fracción = series con alerta / series evaluadas ese mes`. El mes es **candidato sistémico** si
`fracción > X` (desigualdad estricta) **y** se evaluaron al menos 10 series. Las alertas de ese mes no se eliminan: pasan a la cola de
«candidatos sistémicos» y se revisan contra la publicación. El mínimo de 10 series evita que dos series que alertan juntas
(100 %) se lean como un cambio de mercado; 4.2 usaba 2 como mínimo técnico para la sensibilidad, aquí se exige un denominador interpretable.
`regla_sistemica.py` implementa la regla y sus pruebas están en `test_regla_sistemica.py`.

**Amplitud (diagnóstico, no parte de la regla).** Las series de EPM están replicadas por columna, nivel de tensión y tipo de tarifa: un solo
componente puede agrupar hasta 15 series, de modo que una fracción alta puede ser «un componente» y no «el mercado». Se reporta, además,
cuántos componentes distintos alertan:

| Mes | Hito 2: series · componentes con alerta | I-MR ref. 36: series · componentes | MAD 3σ ref. 36: series · componentes |
|---|---|---|---|
| feb-2020 | 51 de 83 · 11 componentes | 38 de 69 · 11 de 14 | 45 de 69 · 11 de 14 |
| jul-2020 | 24 de 83 · 5 componentes | 4 de 69 · 2 de 14 | 18 de 69 · 4 de 14 |
| jul-2021 | 18 de 83 · 3 componentes | 15 de 142 · 1 de 17 | 0 de 142 · 0 de 17 |

#### 2. Protocolo

- **Ventana móvil sin fuga de futuro.** El mes *m* se evalúa con los W cambios logarítmicos anteriores (W = 24 y 36), solo entre meses consecutivos y sin
  imputar. Así cualquier mes se puede evaluar sin que el futuro entre en la referencia (prueba automática). Es la extensión natural del protocolo 4.1/4.2,
  cuya vigilancia fija de 12 meses finales no alcanza a cubrir feb-2020 ni jul-2020 en EPM.
- **Dos métodos:** I-MR clásica (2,66 y 3,267) y Z-score robusto con MAD 3σ; con MAD cero, señal si el cambio difiere de la mediana (4.1/4.2).
- **Variantes de EPM:** etiquetas canónicas (principal) y originales; W = 24 y 36; dos métodos; más la **reproducción del Hito 2** (83 series, origen fijo, diferencia absoluta).
- **Cuarentena EPM** de 3.7 aplicada igual que en 4.1. No se modifica ningún CSV fuente.
- **Una limitación del origen móvil:** la referencia de los meses posteriores a feb-2020 contiene su salto, lo que ensancha los límites I-MR;
  puede explicar por qué I-MR ref. 36 no señala jul-2020 (5,8 %) y MAD, más robusto, sí. Es una hipótesis no contrastada
  (no se probó excluir los meses sistémicos de la referencia).

*Figura regenerable:* `python desarrollo_puntos/4.4/informe_regla_sistemica.py` crea
`figuras/01_fraccion_mensual_epm.png`. Los valores auditables están en
[fracciones_mensuales.csv](../Data/gold/outputs/regla_sistemica/fracciones_mensuales.csv).

#### 3. Calibración de X

Para cada variante se calcula la banda de X que capturaría los tres meses del plan sin marcar ningún otro. Si el mayor valor de los otros
meses es mayor o igual que el menor de los tres, la banda no existe:

| Variante (EPM) | feb-2020 | jul-2020 | jul-2021 | X mínimo para no marcar otro mes | X máximo para capturar los tres | ¿Banda factible? | En X = 25 %: eventos · meses marcados |
|---|---|---|---|---|---|---|---|
| I-MR, ref. 36 | 55,1 % | 5,8 % | 10,6 % | 24,6 % | 5,8 % | no | 1 de 3 · 1 |
| MAD 3σ, ref. 36 | 65,2 % | 26,1 % | 0,0 % | 14,5 % | 0,0 % | no | 2 de 3 · 2 |
| I-MR, ref. 24 | 57,0 % | 14,1 % | 0,0 % | 22,5 % | 0,0 % | no | 1 de 3 · 1 |
| MAD 3σ, ref. 24 | 67,1 % | 25,4 % | 0,0 % | 18,8 % | 0,0 % | no | 2 de 3 · 2 |
| Hito 2 (origen fijo, 83 series) | 61,4 % | 28,9 % | 21,7 % | 24,1 % | 21,7 % | no | 2 de 3 · 2 |

(Valores de «X máximo» iguales a 0 % indican que algún mes del plan no tiene ninguna alerta en esa variante.) En ninguna variante la banda es factible.
Variantes con etiquetas originales: ver [calibracion_resumen.csv](../Data/gold/outputs/regla_sistemica/calibracion_resumen.csv); el X que maximiza la exactitud balanceada
va de 5 % a 44 % según la variante: **no es un óptimo estable**.

*Figura regenerable:* `informe_regla_sistemica.py` crea `figuras/03_calibracion_X.png`; los datos
auditables están en [calibracion_X.csv](../Data/gold/outputs/regla_sistemica/calibracion_X.csv).

**Criterio para el valor de trabajo.** Sin etiquetas confirmadas no hay un óptimo; se propone X = 25 % porque (a) captura febrero de 2020 en las 9 variantes (su fracción mínima es 49 %)
y 5 de 9 capturan además jul-2020; jul-2021 no se captura en ninguna;
(b) en las variantes canónicas no marca ningún mes ajeno al plan; (c) su costo para errores individuales es bajo (siguiente sección); y (d) supera lo que aportaría un
solo componente aunque todas sus series alertaran: como máximo 13,0 % (15 de 115 series en 2020-03;
[tamano_componentes_epm.csv](../Data/gold/outputs/regla_sistemica/tamano_componentes_epm.csv)). Con X = 10 % un solo componente ya sería «sistémico». Es un valor de arranque para revisar con el director, no una calibración cerrada.

#### 4. Efecto de X: alertas reales y costo de enmascaramiento

Meses clasificados como sistémicos y fracción de alertas reales que se reclasifican (ventana móvil, referencia 36):

| Fuente | Método | X = 10 %: meses sistémicos · alertas reclasificadas | X = 25 % | X = 50 % |
|---|---|---|---|---|
| EPM | I-MR | 7 meses · 86 % | 1 mes · 28 % | 1 mes · 28 % |
| EPM | MAD 3σ | 5 meses · 82 % | 2 meses · 53 % | 1 mes · 38 % |
| CHEC | I-MR | 28 meses · 96 % | 24 meses · 90 % | 9 meses · 46 % |
| CHEC | MAD 3σ | 40 meses · 94 % | 28 meses · 77 % | 7 meses · 28 % |
| SSPD | I-MR | 3 meses · 14 % | 0 meses · 0 % | 0 meses · 0 % |
| SSPD | MAD 3σ | 9 meses · 51 % | 0 meses · 0 % | 0 meses · 0 % |

En EPM, X = 10 % reclasificaría más del 80 % de las alertas (la regla dejaría de discriminar); X = 25 % reclasifica entre 28 % y 53 % y X = 50 % solo febrero de 2020. En CHEC,
24 de 187 meses evaluables superan el 25 % (I-MR): la mayor parte de sus alertas ocurre en meses en que casi toda la fuente cambia a la vez. En SSPD la fracción mensual
máxima es 14,4 % (referencia 36, ambos métodos): **con X = 25 % la regla no se activa y todas sus alertas siguen en revisión individual**.

*Figura regenerable:* `informe_regla_sistemica.py` crea
`figuras/02_fraccion_mensual_chec_sspd.png`; los valores auditables están en
[fracciones_mensuales.csv](../Data/gold/outputs/regla_sistemica/fracciones_mensuales.csv).

**Costo para detecciones de errores conocidos** (tomado de 4.2, inyecciones, referencia 36, cohorte común, horizonte t o t+1; fracción de detecciones que la regla enmascararía):

| Fuente | Método | Individual X=10 % | X=25 % | X=50 % | Colectivo X=10 % | X=25 % | X=50 % |
|---|---|---|---|---|---|---|---|
| EPM | I-MR | 11,6 % | 8,2 % | 0,0 % | 100,0 % | 100,0 % | 100,0 % |
| EPM | MAD 3σ | 2,8 % | 0,8 % | 0,0 % | 100,0 % | 100,0 % | 100,0 % |
| CHEC | I-MR | 0,0 % | 0,0 % | 0,0 % | 100,0 % | 100,0 % | 85,5 % |
| CHEC | MAD 3σ | 0,0 % | 0,0 % | 0,0 % | 100,0 % | 100,0 % | 100,0 % |
| SSPD | I-MR | 2,7 % | 0,1 % | 0,0 % | 100,0 % | 79,9 % | 79,9 % |
| SSPD | MAD 3σ | 26,2 % | 0,1 % | 0,0 % | 100,0 % | 100,0 % | 74,0 % |

El enmascaramiento de errores individuales es bajo a X ≥ 25 % y crece cuando X baja; el de errores colectivos es de 74 %–100 % incluso con X = 50 %.
Por eso la regla **etiqueta**, no suprime.

#### 5. Contraste con las publicaciones oficiales de EPM

Se leyeron las publicaciones tarifarias de EPM de enero, febrero, junio y julio de 2020 y de junio y julio de 2021 (tabla monomia, nivel I). Su transcripción se verificó de dos maneras:
(1) coincide con el CSV en las 108 celdas (componente × columna × mes) y (2) la suma de componentes reproduce el CU total publicado (tolerancia 0,02) —
[verificacion_transcripcion_pdf.csv](../Data/gold/outputs/regla_sistemica/verificacion_transcripcion_pdf.csv) y [verificacion_suma_componentes.csv](../Data/gold/outputs/regla_sistemica/verificacion_suma_componentes.csv). De paso, esto suma evidencia de exactitud de EPM para cinco
meses nuevos (feb, jun y jul de 2020; jun y jul de 2021) y otras filas de enero (EXA01 usaba seis filas de ene/dic-2020 y abr/dic-2021); la matriz OE1 de 3.1 no se modifica.

**Febrero de 2020 (enero → febrero).** Las alertas «por componente» cuentan todas las series del componente (todos los niveles y tipos de tarifa); el cambio publicado es el de nivel I, columna Propiedad EPM:

| Componente | 2020-01 | 2020-02 | Cambio publicado | Alertas I-MR (ref. 36) | Alertas MAD (ref. 36) | Alertas Hito 2 | Nota |
|---|---|---|---|---|---|---|---|
| Costo compra: Gm, i | 210,50 | 228,24 | 8,4 % | 0/6 | 0/6 | 0 |  |
| Cargo transporte STN: Tm | 33,62 | 35,41 | 5,3 % | 0/6 | 0/6 | 0 |  |
| Cargo transporte SDL: Dn,m | 191,79 | 206,68 | 7,8 % | 2/3 | 1/3 | 6 |  |
| Margen comercialización: CVm,i,j | 45,60 | 46,02 | 0,9 % | 0/9 | 0/9 | 0 |  |
| Costo G,T, pérdidas: PRn,m | 38,93 | 48,98 | 25,8 % | 9/9 | 9/9 | 9 |  |
| Restricciones: Rm | -0,25 | 2,03 | cruza cero | 3/3 | 3/3 | 0 |  |
| CU total (publicado) | 520,20 | 567,36 | 9,1 % | — | — | — |  |

**Julio de 2020 (junio → julio).**

| Componente | 2020-06 | 2020-07 | Cambio publicado | Alertas I-MR (ref. 36) | Alertas MAD (ref. 36) | Alertas Hito 2 | Nota |
|---|---|---|---|---|---|---|---|
| Costo compra: Gm, i | 221,40 | 222,30 | 0,4 % | 0/6 | 0/6 | 0 |  |
| Cargo transporte STN: Tm | 43,10 | 34,33 | -20,3 % | 0/6 | 6/6 | 6 |  |
| Cargo transporte SDL: Dn,m | 206,40 | 217,22 | 5,2 % | 3/3 | 0/3 | 6 |  |
| Margen comercialización: CVm,i,j | 48,55 | 52,03 | 7,2 % | 0/9 | 9/9 | 9 |  |
| Costo G,T, pérdidas: PRn,m | 48,92 | 48,93 | 0,0 % | 0/9 | 0/9 | 0 |  |
| Restricciones: Rm | 4,55 | 6,41 | 40,9 % | 0/3 | 0/3 | 0 |  |
| CU total (publicado) | 572,92 | 581,22 | 1,4 % | — | — | — | fila «CU CREG 012 de 2020»: 567,36 |

**Julio de 2021 (junio → julio).** La publicación de julio no se encontró con las primeras variantes de URL; el enlace real, tomado de la página «Tarifas años anteriores energía» de EPM, incluye el día («16_julio_2021»).

| Componente | 2021-06 | 2021-07 | Cambio publicado | Alertas I-MR (ref. 36) | Alertas MAD (ref. 36) | Alertas Hito 2 | Nota |
|---|---|---|---|---|---|---|---|
| Costo compra: Gm, i | 228,62 | 221,74 | -3,0 % | 0/15 | 0/15 | 0 |  |
| Cargo transporte STN: Tm | 47,93 | 41,57 | -13,3 % | 15/15 | 0/15 | 6 |  |
| Cargo transporte SDL: Dn,m | 236,60 | 231,74 | -2,1 % | 0/15 | 0/15 | 6 |  |
| Margen comercialización: CVm,i,j | 51,20 | 52,72 | 3,0 % | 0/15 | 0/15 | 0 |  |
| Costo G,T, pérdidas: PRn,m | 49,91 | 47,80 | -4,2 % | 0/15 | 0/15 | 0 |  |
| Restricciones: Rm | 11,50 | 28,40 | 147,0 % | 0/6 | 0/6 | 6 |  |
| CU total (publicado) | 625,76 | 623,97 | -0,3 % | — | — | — | fila «CU CREG 012 de 2020»: 593,99 |

*Figura regenerable:* `informe_regla_sistemica.py` crea
`figuras/04_contraste_publicaciones_epm.png`; los valores auditables están en
[contraste_componentes.csv](../Data/gold/outputs/regla_sistemica/contraste_componentes.csv).

Lectura, acotada a lo observado:

- Las alertas caen en componentes que la publicación muestra con cambios apreciables: costo G,T y pérdidas (+25,8 %) y distribución (+7,8 %) en febrero; transporte STN (−20,3 %), margen de comercialización (+7,2 %) y distribución (+5,2 %) en julio de 2020.
  En julio de 2020 **qué componente alerta depende del método** (con I-MR ref. 36 solo la distribución; con MAD, STN y margen; en el Hito 2, los tres). Como los valores del CSV coinciden con la publicación, esas alertas **corresponden a cambios publicados y no a errores de captura**.
- No todo cambio alerta: en febrero el costo de compra (+8,4 %) y el STN (+5,3 %), y en julio de 2020 Restricciones (+40,9 %), no alertan en ninguna variante. Es compatible con una variabilidad histórica alta de esas series; no se verificó.
- **La hipótesis del Hito 2 solo se respalda en parte.** La revisión del Hito 2 atribuye febrero-2020 «probablemente» a la entrada de los cargos de distribución de la CREG 015 de 2018. Aquí la distribución sube +7,8 %, pero el costo G,T y pérdidas sube +25,8 % y el costo de compra +8,4 %:
  el cambio no se limita a los cargos de distribución.
- **Resolución CREG 012 de 2020** (opción tarifaria; expedida el 6 de febrero y publicada en el Diario Oficial el 17 de febrero de 2020): sus considerandos citan la 015 de 2018 como motivo, pero no fijan un mes de aplicación para EPM.
  Los encabezados de enero y febrero no citan ninguna resolución de 2020; los de junio y julio añaden CREG 012, 058 y 104 de 2020 y una fila nueva «CU CREG 012 de 2020» (567,36), igual al CU total de febrero, mientras el «CU total» calculado de julio es 581,22.
  Es coherente con que la opción tarifaria mantuviera la tarifa aplicada mientras los componentes seguían moviéndose, pero **no se probó** el mecanismo.
- Restricciones cruza cero entre enero y febrero (−0,25 → 2,03): el protocolo logarítmico excluye esa serie (solo admite valores positivos); otras series del componente sí alertan.
- **Julio de 2021 es un cambio de un solo componente, no de todo el mercado.** El transporte STN baja 13,3 % y es justo el componente cuyas 15 series alertan con I-MR (ref. 36);
  con MAD no alerta ninguna serie, y en el Hito 2 (cambios absolutos, límites fijos) alertan tres componentes: STN, distribución (−2,1 %) y Restricciones (+147,0 %, que sube de 11,50 a 28,40).
  Con X = 25 % ese mes no es «sistémico»: es coherente con que un solo componente no debe reclasificarse como cambio de mercado, aunque sí es un cambio publicado y no un error.
- **Resoluciones CREG leídas.** La **058 de 2020** (expedida el 14 de abril; Diario Oficial del 15 de abril de 2020) fija pagos diferidos de las facturas de abril a junio durante la emergencia sanitaria,
  permite cobrar menos que el máximo aprobado en los cargos de transmisión, distribución y comercialización y remite a la opción tarifaria de la 012. La **104 de 2020** (5 de junio; Diario Oficial del 7 de junio)
  impide que el consumo de subsistencia de los estratos 1 y 2 varíe con el IPC durante la emergencia. Ninguna de las dos fija los valores de los componentes de EPM, así que **explican el contexto regulatorio, no los cambios
  observados**. De la **015 de 2018** solo se verificó de forma literal que se publicó el 3 de febrero de 2018 y su objeto; las reglas de aplicación de los cargos proceden de un resumen de la herramienta de lectura y no se citan como texto.
  Los encabezados de junio y julio de 2021 citan las CREG 012, 104 y 152 de 2020 y la 003 de 2021 (ya no la 058); estas dos últimas no se leyeron.

Fuentes documentales y su estado:

| Id | Mes | Documento | Estado | Límite |
|---|---|---|---|---|
| R1 | 2020-01 | Tarifas y costo de energía eléctrica, enero de 2020 | leido | Los metadatos del PDF (creación 2020-01-16) no son la fecha oficial de publicación. |
| R2 | 2020-02 | Tarifas y costo de energía eléctrica, febrero de 2020 | leido | Los metadatos del PDF (creación 2020-02-14) no son la fecha oficial de publicación. |
| R3 | 2020-06 | Tarifas y costo de energía eléctrica, junio de 2020 | leido | Mes base para comparar con julio de 2020. |
| R4 | 2020-07 | Tarifas y costo de energía eléctrica, julio de 2020 | leido |  |
| R5 | 2020-02 | Resolución CREG 012 de 2020 (opción tarifaria) | leido | El texto no fija un mes de aplicación para cada comercializador; no prueba que EPM la aplicara en febrero de 2020. Las fórmulas están en imágenes y no se leyeron. |
| R6 | 2018-02 | Resolución CREG 015 de 2018 (remuneración de la distribución) | leido_parcialmente | No se verificó literalmente ningún artículo que fije cuándo entran los nuevos cargos de distribución de EPM en las tarifas al usuario; esa fecha depende de la resolución particular de cada operador de red, que no se consultó. |
| R7 | 2021-06 | Tarifas y costo de energía eléctrica, junio de 2021 | leido | El enlace se tomó de la página «Tarifas años anteriores energía» de EPM. |
| R8 | 2021-07 | Tarifas y costo de energía eléctrica, julio de 2021 | leido | Las variantes de URL probadas en la primera búsqueda no funcionaban porque el nombre real incluye el día («16_julio_2021»). |
| R9 | 2020-04 | Resolución CREG 058 de 2020 (medidas transitorias para el pago de facturas) | leido | No establece por sí sola los valores de los componentes de EPM. |
| R10 | 2020-06 | Resolución CREG 104 de 2020 (consumo de subsistencia) | leido | No trata de los componentes del costo unitario ni de los cargos de distribución. |
| R11 | 2021-07 | Resoluciones CREG 152 de 2020 y 003 de 2021 | no_consultado | No se afirma su contenido. |

#### 6. Qué no se puede concluir

- **«Candidato sistémico» no es «cambio regulatorio confirmado».** El contraste con las publicaciones oficiales de EPM respalda que feb-2020, jul-2020 y jul-2021 son cambios publicados; solo feb-2020 es amplio (11 componentes). Falta confirmar con EPM o la CREG la causa regulatoria de cada uno.
- **Tres meses no bastan para calibrar.** Los resultados dependen del protocolo; el valor de X es una decisión a aprobar, con esta sensibilidad como insumo.
- **Las series no son independientes** (columnas y niveles replicados): una fracción alta puede ser un solo componente. Por eso se reporta la amplitud, y no se interpreta la fracción como una proporción de eventos independientes.
- **Los costos de enmascaramiento vienen de inyecciones artificiales** (4.2) en la cohorte común de 2021; no se recalcularon con la ventana móvil.
- **Las equivalencias de etiquetas son aprobadas internamente** por el equipo; EPM no las ha confirmado.
- **CHEC y SSPD no tienen contraste externo en este punto.** La coincidencia de feb-2020 en CHEC es evidencia interna entre fuentes, no una verificación documental.

#### 7. Qué cierra del plan y qué queda pendiente

Cierra: formalización e implementación de la regla; calibración de X con sensibilidad; catálogo de alertas sistémicas ([catalogo_alertas_sistemicas.csv](../Data/gold/outputs/regla_sistemica/catalogo_alertas_sistemicas.csv),
227 filas); contraste con las publicaciones de EPM de feb-2020, jul-2020 y jul-2021; lectura de las CREG 012, 058 y 104 de 2020 y lectura parcial de la 015 de 2018; verificación de las cifras 51/24/18.
**Pendiente:** lectura completa de la CREG 015 de 2018 y de las resoluciones particulares de EPM; lectura de las CREG 152 de 2020 y 003 de 2021; consulta formal a EPM o CREG sobre la causa de cada cambio (plan, Hito 6);
decisión del director sobre X; revisar 4.1/4.2 con etiquetas canónicas; probar la exclusión de meses sistémicos de la referencia.

#### Reproducir y auditar

```powershell
python desarrollo_puntos/4.4/calibrar_regla_sistemica.py
python desarrollo_puntos/4.4/informe_regla_sistemica.py
python -m unittest discover -s desarrollo_puntos/4.4 -p test_regla_sistemica.py -v
python desarrollo_puntos/4.4/verificar_resultados.py
```

[configuracion.json](../Data/gold/outputs/regla_sistemica/configuracion.json) fija parámetros, versiones y huellas de entradas y de los PDF; [manifiesto_resultados.json](../Data/gold/outputs/regla_sistemica/manifiesto_resultados.json) las de todos los archivos entregados.


<a id="doc-c26806ebe30e"></a>

## desarrollo_puntos/4.4/README.md

### 4.4 · Regla de alerta sistémica

La lectura principal está en [INFORME_REGLA_SISTEMICA.md](REFERENCIA_TECNICA.md#doc-4ce62780cc42). Corresponde a la actividad 4 del
Hito 4: clasificar como candidato sistémico (posible cambio regulatorio) el mes en que más de X % de las series alertan,
calibrar X con feb-2020, jul-2020 y jul-2021, y contrastar con las publicaciones de EPM y las resoluciones de la CREG.
Desarrolla lo que [4.2](REFERENCIA_TECNICA.md#doc-15dec98a30e1) solo exploró como sensibilidad. No modifica 4.1, 4.2 ni 4.3.

| Archivo | Contenido |
|---|---|
| [regla_sistemica.py](../Code/Modeling/regla_sistemica/regla_sistemica.py) | La regla (desigualdad estricta, mínimo de 10 series), el protocolo de ventana móvil sin fuga de futuro, la calibración y la carga de EPM con etiquetas canónicas. |
| [calibrar_regla_sistemica.py](../Code/Modeling/regla_sistemica/calibrar_regla_sistemica.py), [informe_regla_sistemica.py](../Code/Modeling/regla_sistemica/informe_regla_sistemica.py) | Ejecución completa; figuras e informe generados desde las tablas. |
| [fracciones_mensuales.csv](../Data/gold/outputs/regla_sistemica/fracciones_mensuales.csv) | Series evaluadas y con alerta por mes, fuente, ventana y método, con categorías y componentes que alertan. |
| [reproduccion_hito2.csv](../Data/gold/outputs/regla_sistemica/reproduccion_hito2.csv) | Reproducción de 51/83, 24/83 y 18/83 desde los archivos del Hito 2. |
| [calibracion_X.csv](../Data/gold/outputs/regla_sistemica/calibracion_X.csv), [calibracion_resumen.csv](../Data/gold/outputs/regla_sistemica/calibracion_resumen.csv) | Para X de 5 a 80 %: meses del plan capturados, otros meses marcados, banda factible y alertas reclasificadas. |
| [catalogo_alertas_sistemicas.csv](../Data/gold/outputs/regla_sistemica/catalogo_alertas_sistemicas.csv) | Catálogo de meses candidatos con su fracción, amplitud, banderas por X y estado del contraste externo. |
| [efecto_regla_sobre_alertas_reales.csv](../Data/gold/outputs/regla_sistemica/efecto_regla_sobre_alertas_reales.csv), [costo_enmascaramiento_4_2.csv](../Data/gold/outputs/regla_sistemica/costo_enmascaramiento_4_2.csv) | Alertas reales reclasificadas por X; detecciones de errores inyectados que la regla enmascararía (tomado de 4.2). |
| [composicion_alertas_meses_plan.csv](../Data/gold/outputs/regla_sistemica/composicion_alertas_meses_plan.csv), [tamano_componentes_epm.csv](../Data/gold/outputs/regla_sistemica/tamano_componentes_epm.csv), [inventario_series_por_variante.csv](../Data/gold/outputs/regla_sistemica/inventario_series_por_variante.csv) | Componentes que alertan en los meses del plan, cuánto aportaría cada componente a la fracción y cuántas series hay por variante. |
| [contraste_componentes.csv](../Data/gold/outputs/regla_sistemica/contraste_componentes.csv) | Cambio publicado por EPM de cada componente (ene→feb y jun→jul de 2020; jun→jul de 2021) frente a las alertas de cada variante. |
| [verificacion_transcripcion_pdf.csv](../Data/gold/outputs/regla_sistemica/verificacion_transcripcion_pdf.csv), [verificacion_suma_componentes.csv](../Data/gold/outputs/regla_sistemica/verificacion_suma_componentes.csv) | La transcripción de los PDF coincide con el CSV (108 celdas) y la suma de componentes reproduce el CU total. |
| [evidencia_externa/](../Data/gold/outputs/regla_sistemica/evidencia_externa) | Los seis PDF oficiales de EPM leídos (ene, feb, jun y jul de 2020; jun y jul de 2021), su transcripción y el estado de cada referencia documental (CREG 012, 058 y 104 de 2020 leídas; 015 de 2018 leída parcialmente). |
| [test_regla_sistemica.py](../Code/Modeling/regla_sistemica/test_regla_sistemica.py), [verificar_resultados.py](../Code/Modeling/regla_sistemica/verificar_resultados.py), [verificacion.json](../Data/gold/outputs/regla_sistemica/verificacion.json) | Diez pruebas de propiedades y auditoría con recálculo independiente. |
| [configuracion.json](../Data/gold/outputs/regla_sistemica/configuracion.json), [manifiesto_resultados.json](../Data/gold/outputs/regla_sistemica/manifiesto_resultados.json) | Parámetros, versiones y huellas de entradas, PDF y salidas. |

El script `informe_regla_sistemica.py` genera cuatro gráficos en `figuras/`, en PNG, SVG y PDF.
La carpeta no se versiona porque son artefactos regenerables; se debe ejecutar el script con las
dependencias registradas en `configuracion.json` para visualizarlos.
X = 25 % es un **valor de trabajo propuesto, no aprobado**: con tres meses no hay un X único. «Candidato sistémico» no equivale a
«cambio regulatorio confirmado»: el contraste con las publicaciones de EPM muestra que son cambios publicados, pero falta confirmar con EPM o la CREG la causa de cada uno.

```powershell
python desarrollo_puntos/4.4/calibrar_regla_sistemica.py
python desarrollo_puntos/4.4/informe_regla_sistemica.py
python -m unittest discover -s desarrollo_puntos/4.4 -p test_regla_sistemica.py -v
python desarrollo_puntos/4.4/verificar_resultados.py
```


<a id="doc-74d9a3dc3145"></a>

## desarrollo_puntos/4.5/README.md

### Hito 4.5 · Scorecard por dimensión

Este punto resume la matriz OE1 por fuente y dimensión, como solicita DAMA-DMBOK para reportar
calidad de datos.

#### Ejecución

Desde la raíz del repositorio:

```bash
python3 desarrollo_puntos/4.5/generar_scorecard_oe1.py
```

El script lee `desarrollo_puntos/3.1/matriz_oe1.csv` y genera
`scorecard_oe1_provisional.csv` en esta carpeta.

#### Contenido

El scorecard contiene 32 filas: cuatro fuentes por ocho dimensiones. Para cada combinación reporta
controles totales, medidos, provisionales, no medibles, no aplicables y promedio de indicadores.

El estado permanece `provisional` hasta que se aprueben los umbrales, catálogos, evidencia de
exactitud y oportunidad. No debe interpretarse como una calificación final.


<a id="doc-9616b9e5ae82"></a>

## desarrollo_puntos/4.6/INFORME_NIVELES_COSTO.md

### Hito 4.6 · Resultados por nivel y costo computacional

Este informe completa la actividad 6 del Hito 4. El análisis separa niveles únicamente cuando
la fuente tiene un nivel explícito: EPM usa I–IV y CHEC usa los códigos 1–4. SSPD y XM se
reportan como `No_aplica` porque su esquema utilizado en este experimento no contiene un nivel
comparable. No se inventa una equivalencia para esas fuentes.

#### Archivos

- `resultados_por_nivel.csv`: observaciones, detecciones y tasa de alerta por nivel y método.
- `costos_computacionales.csv`: tiempos registrados por etapa, fuente y experimento.
- `analizar_niveles_costos.py`: generación reproducible de ambos archivos.

#### Protocolo de niveles

Se usa la cohorte `comun` y la referencia de 36 cambios del detalle de 4.2. Los métodos resumidos
son IMR, Z-score robusto, Isolation Forest y R12. La tasa es detecciones / observaciones; no es
una medida de exactitud y no debe confundirse con recall de errores inyectados.

Se separan los niveles para evitar que una fuente con muchas series de un solo nivel domine la
interpretación. El plan original menciona 69 series de Nivel I y 14 de niveles II–IV; esa cifra
corresponde a una variante de EPM y no se extrapola automáticamente a SSPD o XM.

#### Costo computacional

Los tiempos se toman de las ejecuciones ya registradas en 4.2 y 4.3. En 4.3 se conservan las
etapas de ajuste, puntuación, tasa igualada/bootstrap, sorteo y total. En 4.2 se conserva el total
por escenario de sensibilidad. Los tiempos dependen del equipo y sirven para comparar escenarios
relativos, no como garantía de tiempo en otro computador.

#### Limitaciones

- Las series dentro de una fuente pueden estar correlacionadas.
- SSPD y XM no tienen un nivel comparable en este corte.
- La variante `EPM_canonicas` es sensibilidad y no reemplaza a EPM.
- El costo por nivel no puede atribuirse causalmente a una sola variable si cambian también el
  número de series, observaciones o métodos.
- La ejecución de los scripts de 4.2–4.4 requiere numpy/pandas/scikit-learn instalados.

Filas generadas: 36 por nivel/método y 47 de costo computacional.


<a id="doc-dd387e3f4a37"></a>

## desarrollo_puntos/4.6/README.md

### Hito 4.6 · Resultados por nivel y costo computacional

Este punto separa los resultados por nivel cuando la fuente tiene una categoría de nivel explícita
y resume los tiempos de ejecución registrados en los experimentos 4.2 y 4.3.

```bash
python3 desarrollo_puntos/4.6/analizar_niveles_costos.py
```

La lectura metodológica está en [INFORME_NIVELES_COSTO.md](REFERENCIA_TECNICA.md#doc-9616b9e5ae82).


<a id="doc-c1f90ad6d430"></a>

## fuentes_datos/datos/Datos_en_revision/CREG_prioridad/README.md

### Anexos eléctricos CREG examinados

Estos cinco libros fueron descargados de publicaciones oficiales de CREG como parte de la búsqueda prioritaria. Se conservan como referencias en revisión; no cuentan como cinco casos aprobados para la tesis.

El panel de la Circular 125 de 2025 contiene 88 registros anuales. Los cuatro anexos de las Circulares 053/064 de 2015 contienen tablas de indicadores y escenarios por empresa, no un histórico mensual crudo validado.

La explicación, procedencia y decisión están en [REVISION_CREG_ELECTRICIDAD.md](REFERENCIA_TECNICA.md#doc-1e1e212fc147). Los hashes se conservan en `desarrollo_puntos/3.4/perfiles/creg_electricidad_anexos.json`.

El conjunto de gas investigado inicialmente fue excluido y su descarga retirada después de que el usuario confirmó el alcance de electricidad.


<a id="doc-e41c39d2c4be"></a>

## fuentes_datos/datos/Datos_seleccionados/CHEC/README.md

### CHEC · c698-wqig

CSV seleccionado para el análisis de costos unitarios y tarifas de energía eléctrica.
La ficha y el análisis de catálogos están en `desarrollo_puntos/3.2/CHEC/`;
la revisión de reglas, en `desarrollo_puntos/3.3/CHEC/`; y las cartas,
en `desarrollo_puntos/3.5/CHEC/`. La matriz está en `desarrollo_puntos/3.1/`.


<a id="doc-4cb35e3c7465"></a>

## fuentes_datos/datos/Datos_seleccionados/EPM/README.md

### EPM · sfcd-b3ey

CSV seleccionado para el análisis de calidad de tarifas de energía eléctrica.
La ficha está en `desarrollo_puntos/3.2/EPM/`; la revisión de reglas, en
`desarrollo_puntos/3.3/EPM/`; las cartas, en `desarrollo_puntos/3.5/EPM/`;
y la cuarentena, en `desarrollo_puntos/3.7/EPM/`. La matriz está en `desarrollo_puntos/3.1/`.


<a id="doc-9f3e7a240956"></a>

## fuentes_datos/datos/Datos_seleccionados/README.md

### Datos seleccionados por fuente

Cada fuente tiene su propia carpeta para localizar rápidamente los archivos usados:

- `EPM/` conceptualmente se documenta en `fuentes_datos/diccionarios/EPM` y sus datos CSV permanecen en la raíz por compatibilidad con el convenio de medición.
- `CHEC/` se documenta en `fuentes_datos/diccionarios/CHEC`; su CSV permanece en la raíz por compatibilidad.
- `SSPD/` contiene el detalle comprimido y el agregado mensual de `ebby-cjha`.
- `XM_piloto/` contiene los archivos de demanda y versiones mensuales.

Los documentos analíticos de EPM y CHEC están agrupados en `desarrollo_puntos/3.3/EPM`
y `desarrollo_puntos/3.3/CHEC`.

La matriz OE1 está en `desarrollo_puntos/3.1/`, las fichas en `3.2`, las cartas en
`3.5`, la trazabilidad en `3.6` y la cuarentena/bootstrap en `3.7`. El índice completo
está en [la documentación general del Hito 3](REFERENCIA_TECNICA.md#doc-393500a1bb5a).


<a id="doc-daeaab5c0588"></a>

## fuentes_datos/datos/Datos_seleccionados/SSPD/README.md

### SSPD · ebby-cjha

Contiene el agregado mensual y el detalle comprimido de la fuente seleccionada.
La ficha está en `desarrollo_puntos/3.2/SSPD/`.


<a id="doc-ebb04b15ad96"></a>

## fuentes_datos/datos/Datos_seleccionados/XM_piloto/README.md

### Piloto de demanda real XM/SIMEM

Descarga y verificación: 4 de noviembre de 2026. Es un candidato en revisión, no una incorporación automática a la matriz medida.

#### Alcance de los archivos

- `xm_demanda_epmc_epmd_str02_202001_202501.csv`: 119.928 registros originales devueltos por la consulta filtrada al agente EPMC, mercado EPMD y sistema STR02, enero de 2020 a enero de 2025. No es el mercado completo ni una muestra aleatoria del mercado. Incluye múltiples versiones por hora.
- `xm_versiones_mensuales_202001_202501.csv`: 161 registros del calendario mensual de versiones de liquidación. Conserva las fechas declaradas de publicación; no son fechas fabricadas por el cliente.
- `xm_demanda_mensual_piloto.csv`: 61 observaciones mensuales derivadas, una por mes. Para cada mes se elige la TX numérica más alta presente en el conjunto de demanda, se excluyen TXF/TXR y se suman sus valores horarios. No se suman versiones entre sí. Esa selección no se presenta como la versión final oficial.

La serie mensual deriva de **44.592 observaciones horarias únicas**. Los 61 meses contienen todas sus horas calendario y tienen suma de demanda positiva. No se interpolaron huecos ni se rellenaron valores faltantes. Esto habilita, en longitud y continuidad, el escenario de 48 cambios de referencia y 12 de vigilancia; todavía falta analizar estabilidad y estacionalidad.

#### Diferencia entre dos políticas de versión

Exigir la versión marcada `esMaximaVersion=1` en el calendario deja 53 meses coincidentes y una racha máxima de 20 meses: no cumple el protocolo mensual. Hay ocho meses donde el conjunto de demanda no ofrece la versión final marcada por ese calendario.

La política alternativa de mayor TX numérica disponible permite 61 meses completos, pero se debe justificar y congelar antes de comparar técnicas. Permite una evaluación retrospectiva sobre el conjunto publicado, no certificar la última liquidación final del mercado.

Se vincula fecha de publicación declarada para 60 de las 61 versiones mensuales seleccionadas. Falta junio de 2021. Por ello **oportunidad no está cerrada**: falta ese vínculo y definir plazos y alcance de cada versión. No se convierte la ausencia de evidencia en retraso ni cumplimiento. Tampoco se interpreta la fecha de una revisión como primera publicación.

#### Reproducibilidad y pendientes

Los parámetros exactos, filtros y hashes están en `desarrollo_puntos/3.2/perfiles/xm_piloto_cobertura.json`. La consulta usa el conjunto histórico `c1b851`, retirado de actualización, con corte declarado de junio de 2026.

Faltan el contraste de exactitud con referencia equivalente, maestras, adaptación de reglas por dominio, evaluación de oportunidad y el experimento de cartas. No aplicar las reglas de propiedad de EPM literalmente a demanda.


<a id="doc-e81c2bcf3ffb"></a>

## fuentes_datos/DECISION_FUENTES_PRINCIPALES.md

### Decisión de fuentes principales del proyecto

#### Decisión

Para el desarrollo de los Hitos 3 a 6 se trabajará con cuatro fuentes eléctricas:

1. EPM — `sfcd-b3ey`.
2. CHEC — `c698-wqig`.
3. Superservicios — Información comercial residencial y no residencial ZNI, `ebby-cjha`.
4. XM/SIMEM — Demanda real histórica, `c1b851`.

La decisión se toma porque las cuatro permiten evaluar el framework en registros energéticos con estructuras distintas: tarifas, costos unitarios, facturación/consumo y demanda horaria agregada.

#### Justificación

| Fuente | Función en el proyecto |
|---|---|
| EPM | Mantiene la continuidad con el Hito 2 y permite reproducir el caso tarifario original. |
| CHEC | Comprueba la transferencia del framework a otro publicador tarifario con historia extensa. |
| Superservicios ZNI | Aporta consumo observado y 59 períodos mensuales para series de operadores ZNI. |
| XM/SIMEM | Aporta demanda horaria y 61 meses derivados con trazabilidad de versiones. |

#### Alcance metodológico

Las doce reglas originales se mantienen, pero no todas tienen el mismo significado en las cuatro fuentes. En SSPD ZNI y XM deben utilizarse adaptadores documentados por dominio. En particular, R08 y R09 no se pueden copiar literalmente desde EPM porque ZNI y demanda XM no son tablas de tarifas con propiedad y modalidad equivalentes.

La matriz OE1 conserva 19 controles por fuente. Los controles de XM se incorporan como `pendiente_implementacion` hasta que se ejecute su adaptador y se verifique la política de versiones.

#### Fuentes que no forman parte del conjunto principal

- `bnkp-xdb7`: fuente no residencial de Superservicios; tiene consumo y tarifa aplicada, pero solo 12 meses y una caída importante de volumen.
- `supers_icnr-l4iw`: extracción relacionada con información comercial; no se cuenta como dataset independiente y sus identificadores presentan notación científica.
- Anexos eléctricos CREG: sirven como referencia regulatoria, pero son paneles anuales o tablas de indicadores y escenarios, no microdatos mensuales suficientes para cartas.
- `ek3f-5wn4`: fuente de gas natural excluida porque el alcance del proyecto es únicamente electricidad.

#### Condición de cierre

La selección no significa que las ocho dimensiones ya estén demostradas. Para cerrar el Hito 3 se deben ejecutar los 19 controles en las cuatro fuentes, completar la evidencia de exactitud y oportunidad y conservar hashes, versión, política de transformación y fecha de cada ejecución.


<a id="doc-df3b3bd5e550"></a>

## fuentes_datos/FUENTES_PROBABLES_EN_REVISION.md

### Fuentes probables o en revisión

La selección principal queda fijada en cuatro fuentes eléctricas: EPM, CHEC, Superservicios ZNI (`ebby-cjha`) y XM/SIMEM (`c1b851`). Las siguientes fuentes se conservan porque pueden aportar contexto, variables o una futura ampliación, pero no se cuentan como casos principales del protocolo.

| Fuente | Estado | Motivo de no incorporación principal |
|---|---|---|
| Superservicios no residencial `bnkp-xdb7` | En revisión | Tiene 402.500 filas y consumo/tarifa aplicada, pero solo 12 meses y una caída fuerte de registros; no permite cartas mensuales con el protocolo de 49 observaciones. |
| CSV extraído `supers_icnr-l4iw` | En revisión, sin ficha vigente | Es una extracción relacionada con información comercial; tiene 12 meses y sus identificadores aparecen en notación científica. Se conserva como evidencia, pero no se cuenta como fuente independiente de `bnkp-xdb7`. |
| CREG, Circular 125 de 2025 | Referencia regulatoria | Es eléctrica y contiene EPM, CHEC, ESSA y EDEQ, pero solo tiene 88 registros anuales y 11 columnas. No alcanza el volumen ni la continuidad mensual. |
| CREG, Circulares 053/064 de 2015 | Referencia regulatoria | Son tablas de indicadores y escenarios de calidad, no microdatos mensuales crudos. No deben tratarse como observaciones para cartas. |
| CREG `ek3f-5wn4` | Descartada por alcance | Es una fuente amplia de gas natural. El proyecto quedó limitado a electricidad, por lo que no se incorpora. |
| Antigua fuente SSPD `vfjy-6fka` | Sustituida | Era la fuente indicada en una versión anterior del plan, pero fue reemplazada por `ebby-cjha`, que tiene mayor cobertura y consumo. |

Los archivos de estas fuentes se conservan en `fuentes_datos/datos/Datos_en_revision/` y los motivos detallados están en [`REVISION_CREG_ELECTRICIDAD.md`](REFERENCIA_TECNICA.md#doc-1e1e212fc147) y [`PROPUESTA_CUATRO_FUENTES.md`](REFERENCIA_TECNICA.md#doc-0f3a50ee68a6).

No se consideran fuentes diferentes las copias agregadas, los archivos comprimidos o las vistas derivadas del mismo identificador de portal. Tampoco se cuentan los anexos CREG como cuatro datasets independientes.


<a id="doc-49ce02ddaa81"></a>

## fuentes_datos/JUSTIFICACION_SELECCION.md

### Justificación de selección: EPM y CHEC

Fecha de organización: 27 de octubre de 2026.

Se seleccionan dos casos de registros administrativos tarifarios de energía eléctrica en Colombia. El usuario permitió conservar EPM aunque no alcanza las 10.000 filas. La exigencia del profesor de evaluar las ocho dimensiones se mantiene para ambas fuentes. Esta selección no demuestra que esa evaluación ya esté completa.

#### EPM — Histórico de tarifas de energía eléctrica

- Portal: https://www.datos.gov.co/d/sfcd-b3ey
- CSV: `datos/epm_sfcd-b3ey.csv`. Diccionario: `diccionarios/EPM/epm.yaml`.
- Volumen comprobado: **3.623 filas y 12 columnas**.
- Cobertura descrita por el publicador: **diciembre de 2016 a diciembre de 2021**.

Se selecciona por continuidad metodológica: es el caso con el que se desarrollaron perfilamiento, reglas, cartas y experimentos del Hito 2. Permite conservar una referencia para comprobar las correcciones del framework. Sus categorías tarifarias, nivel de tensión, propiedad y franjas horarias permiten formular controles de negocio concretos.

La revisión local del Hito 2 reporta 83 series con al menos 49 meses y 77 clasificadas como limpias por el código de esa entrega. Varias series por propiedad están fuertemente relacionadas; no son réplicas independientes. Esas cifras son evidencia previa, no una nueva ejecución sobre el CSV ahora conservado.

Se acepta la excepción de tamaño para este caso: longitud temporal y validación rigurosa sustentan su utilidad. No tiene consumo observado; el rango de consumo es una categoría. Los importes pueden representar diferentes conceptos y sus unidades deben confirmarse por concepto.

#### CHEC — Información de costo unitario de tarifas de energía

- Portal: https://www.datos.gov.co/d/c698-wqig
- CSV: `datos/chec_c698-wqig.csv`. Diccionario: `diccionarios/CHEC/chec.yaml`.
- Volumen comprobado: **40.609 filas y 24 columnas**.
- Cobertura global: **enero de 2008 a septiembre de 2026**, 225 meses.

Se selecciona para evaluar transferencia a otro publicador y estructura manteniendo el dominio tarifario. Supera el volumen solicitado y aporta comercializador, mercado, nivel, propiedad, clase de servicio, estrato, rango y componentes del costo unitario.

La validación local encontró, para cada variable costo unitario y valor de tarifa, **180 grupos con al menos 61 meses consecutivos con un registro único por mes y valores positivos y finitos**. Se agruparon las 12 columnas categóricas y se exigió variación en los valores del grupo. La mayor racha bajo estas condiciones fue de 201 meses. Estas dos variables no constituyen réplicas independientes de una misma categoría.

Con 61 observaciones se pueden reservar 48 cambios de referencia y 12 de vigilancia. Esa longitud habilita diseñar el experimento; todavía hay que verificar supuestos y ejecutar el protocolo. Existen 1.398 claves categoría-mes repetidas que requieren revisión, no eliminación automática. El resumen está en `verificaciones/CHEC/chec_validacion_series.json`.

CHEC tampoco contiene consumo observado. Las medidas están declaradas como texto en el esquema; definiciones como `tipomed`, `cureal` y `subcon` requieren confirmación. El diccionario no inventa catálogos ni unidades faltantes.

#### SSPD — Información comercial residencial y no residencial

- Portal: https://www.datos.gov.co/d/ebby-cjha
- CSV: `datos/Datos_seleccionados/SSPD/sspd_ebby-cjha_mensual.csv` y el detalle comprimido.
  Diccionario: `diccionarios/SSPD/sspd.yaml`.
- Volumen en origen: **11.905.557 filas y 29 columnas**.
- Cobertura: **julio de 2017 a mayo de 2022, 59 períodos mensuales consecutivos.**

Se incorpora por una razón explícita: este mismo documento y el README declaraban que EPM y
CHEC **no contienen consumo observado**. Esta fuente lo aporta, en `consumo_basico`,
`consumo_complementario` y `consumo_reside_mayor800`.

Se evaluaron todas las alternativas del catálogo nacional antes de elegirla. De 2.138 fichas
revisadas, 128 de energía y 24 con alguna columna de consumo, **es la única con profundidad
mensual suficiente para cartas de control**: las demás tienen once o doce períodos. Con 59
meses caben 36 cambios de referencia y 23 de vigilancia, y 136 de sus 207 series
empresa-estrato alcanzan el mínimo de 49.

**Se relaja un criterio y se declara.** La fuente no se actualiza desde el 28 de octubre de
2023 y declara periodicidad anual. Se aceptó porque las cartas requieren una serie mensual
histórica, no un flujo vivo: que no lleguen períodos nuevos no afecta un análisis sobre 59
meses ya publicados. Además, una fuente que declara una frecuencia y no la cumple es materia
de la dimensión de oportunidad, no una razón para descartarla.

**Dos limitaciones que no se ocultan.** La primera: es de **Zonas No Interconectadas**. Se
verificaron las 91 empresas contra el directorio de Superservicios y ninguna es del Sistema
Interconectado Nacional, de modo que no aplica la fórmula de la Resolución CREG 119 de 2007
ni comparte los ejes tarifarios de EPM y CHEC. Por eso R08, R09 e INT02 quedan `no_aplica`.
La segunda: en origen pesa unos 9,7 GB, así que se conservan dos censos declarados en lugar
del conjunto íntegro, con su universo escrito en el diccionario.

A cambio aporta algo que las otras dos no tienen: **91 publicadores en un mismo esquema**.
Validar el framework en dos empresas grandes y después en 91 operadores pequeños con poca
capacidad de reporte es un argumento de transferibilidad bastante más fuerte.

#### SSPD-NR — Información comercial no residencial

- Portal: https://www.datos.gov.co/d/bnkp-xdb7
- Archivo en revisión: `datos/Datos_en_revision/sspd_bnkp-xdb7-compressed.zip`.
  Diccionario: `diccionarios/sspd_nr.yaml`.
- Volumen: **402.500 filas y 48 columnas**, conservadas íntegras.
- Cobertura: **julio de 2021 a junio de 2022, 12 períodos mensuales.**

Entra para resolver la limitación declarada de la fuente anterior. SSPD aporta los 59 meses
que las cartas necesitan pero es de Zonas No Interconectadas; esta es del **Sistema
Interconectado Nacional** —32 prestadores en Meta, Casanare, Huila, Putumayo, Guaviare y
Caquetá, encabezados por Electrificadora del Meta y Electrificadora del Huila—, de modo que
le aplica el mismo régimen regulatorio que a EPM y CHEC.

Aporta además tres cosas que ninguna otra fuente del proyecto tiene:

1. **`tarifa_aplicada`**, con promedio de 758,98 $/kWh. Es el costo unitario que EPM y CHEC
   publican como especificación, aquí aplicado a una factura concreta. Es el puente entre el
   dominio tarifario y el consumo observado.
2. **`car_t440_car_inver` con valores 100, 50 y 0**: el eje de propiedad del activo. Por eso
   **R08 y R09 vuelven a ser aplicables**, cuando en la fuente ZNI quedaron `no_aplica`.
3. **Energía reactiva** y **pares código-nombre** (empresa y mercado), que devuelven a INT02
   un caso donde medirse.

**Su limitación es el espejo de la anterior.** Solo tiene 12 períodos, por debajo de los 49
que exige el protocolo, así que CART01 no es ejecutable sobre ella. Y el volumen se desploma
dentro de la propia ventana: 101.608 registros en 2021-07 frente a 977 en 2022-05, de modo
que los períodos útiles son unos nueve. Eso es un defecto de completitud de la fuente y está
declarado como tal, no disimulado.

**Sobre la oportunidad, una precisión que conviene no perder.** La fuente trae
`car_t440_fec_exp`, fecha de expedición de la factura. Permite medir el rezago entre el
período facturado y la emisión, pero eso es **oportunidad del servicio, no del dato**. OPO01
está especificado sobre la disponibilidad de la publicación, así que esta evidencia no lo
cierra tal como está escrito: habría que reespecificar el control o registrarlo como un
indicador distinto. No se fuerza.

#### Por qué cuatro fuentes y no tres

Las dos fuentes de consumo cubren huecos opuestos y ninguna sola basta:

| | SSPD (ZNI) | SSPD-NR (interconectado) |
|---|---|---|
| Períodos mensuales | **59** | 12 |
| Régimen | Zonas No Interconectadas | **Sistema Interconectado** |
| Tarifa aplicada | no | **sí** |
| Eje de propiedad | no | **sí** |
| Pares código-nombre | no | **sí** |
| Energía reactiva | no | **sí** |

Con la primera se pueden construir las series que exigen las cartas; con la segunda se
sostiene que el framework se aplicó al mismo régimen regulatorio de EPM y CHEC. El costo es
real y conviene decirlo: cada fuente añadida arrastra la obligación de evaluarle las ocho
dimensiones, y esa obligación todavía no está cerrada en ninguna.

#### Utilidad de la pareja

Mantiene el dominio del trabajo realizado y permite contrastar dos estructuras tarifarias. Se propone un núcleo común y adaptadores por fuente. R08 y R09 deben traducirse al esquema de CHEC: copiar literalmente el código EPM no sería una réplica válida.

Permite desarrollar perfilamiento, reglas, cartas, comparación de detectores, scorecards y un artefacto reproducible. La solidez de la tesis dependerá de verdad de referencia, métricas, sensibilidad, intervalos e independencia de las unidades de evaluación; la selección por sí sola no garantiza esos resultados.

#### Condición obligatoria: ocho dimensiones por dataset

| Dimensión | Control/evidencia prevista | Pendiente |
|---|---|---|
| Completitud | Campos obligatorios y cobertura esperada | Aplicabilidad y denominadores; cero no equivale a faltante |
| Validez | Tipos, formatos, períodos, dominios y signos | Confirmar unidades y excepciones por concepto |
| Unicidad | Duplicados exactos y claves repetidas | Cerrar claves y distinguir conflictos |
| Consistencia | Etiquetas y relaciones por propiedad, nivel y concepto | Adaptar R08/R09 a CHEC |
| Integridad | Estructura y correspondencia con catálogos/código-nombre | Especificar e implementar INT01; distinguirlo de unicidad |
| Razonabilidad | R12, cartas y modelos | Protocolo temporal, cuarentena y dependencia entre series |
| Exactitud | Muestra contrastada con documentos tarifarios originales | Obtener referencias, definir muestreo y medir concordancia |
| Oportunidad | Disponibilidad real frente a plazo esperado | Conseguir evidencia histórica o diseñar seguimiento prospectivo con alcance explícito |

**“No evaluable” no cumple el requisito final del profesor.** La selección queda condicionada a obtener evidencia para exactitud y oportunidad en cada fuente. Si falta, será necesario complementar las fuentes o revisar la selección con el director.

Vigencia, fecha de descarga y modificación global del portal no equivalen a disponibilidad real por período. Un seguimiento futuro no demuestra oportunidad histórica.

Las doce reglas base no cubren por sí solas las ocho dimensiones. Se proponen controles complementarios INT01, EXA01 y OPO01 en el YAML, sin presentarlos como implementados. También se propone distinguir R11/validez y R12/razonabilidad de exactitud; el código existente conserva sus etiquetas y no fue modificado.

#### Trazabilidad y alcance documental

Metadatos originales en `metadatos/`; CSV sin modificación en `datos/`; hashes y tamaños en `verificaciones/manifiesto_archivos.json`. La fecha del manifiesto no se presenta como fecha de descarga original ni de publicación.

Fundamento: anteproyecto y retroalimentación de junio de 2026 en `Entregables_pdf/`, revisión técnica del Hito 2 en `0_Recomendaciones_profesor/` y exigencia adicional del profesor comunicada por el usuario. La revisión técnica es un borrador local, no un concepto oficial del profesor. No se modificó el anteproyecto; queda pendiente actualizar publicadores, población/muestra y alcance de ocho dimensiones.


<a id="doc-0f3a50ee68a6"></a>

## fuentes_datos/PROPUESTA_CUATRO_FUENTES.md

### Cuatro fuentes para validar el proyecto: propuesta y requisitos de aceptación

Revisión del 4 de noviembre de 2026. El requisito es disponer de al menos cuatro datasets útiles para el estudio, con evaluación de las ocho dimensiones en cada uno. Las doce reglas del proyecto deben revisarse por aplicabilidad real; no se cambian silenciosamente sus significados para completar una tabla.

**Prioridad y alcance confirmados:** buscar primero publicaciones directas de CREG y mantener exclusivamente electricidad. La [revisión CREG](REFERENCIA_TECNICA.md#doc-1e1e212fc147) encontró bases eléctricas anuales y cuadros de escenarios, que no superan los criterios temporales del protocolo. Gas queda excluido. La siguiente propuesta se conserva mientras no se verifique una candidata eléctrica de CREG adecuada.

#### Selección propuesta para el piloto

| Fuente | Aporte | Evidencia disponible | Estado |
|---|---|---|---|
| EPM `sfcd-b3ey` | Caso tarifario inicial y comparación con resultados del Hito 2 | 3.623 filas; 61 meses globales; 83 series con al menos 49 meses según revisión previa | Conservar; excepción de tamaño aceptada. Falta evidencia de oportunidad y completar exactitud |
| CHEC `c698-wqig` | Segundo publicador tarifario, componentes y categorías | 40.609 filas; 180 grupos con al menos 61 meses positivos y únicos por mes en CU/tarifa | Conservar; falta cerrar catálogos, exactitud y oportunidad |
| Superservicios `ebby-cjha` | Consumo/facturación de operadores ZNI | 11.905.557 filas en origen; copia mensual de 15.075 filas y censo de 91.840 filas de una empresa; 59 meses globales | Candidato temporalmente útil; exige adaptar reglas de dominio y completar evidencia externa |
| XM/SIMEM `c1b851` | Demanda eléctrica del SIN y versiones de liquidación | Piloto descargado: 119.928 registros para un grupo fijo; serie derivada de 61 meses positivos con todas sus horas | Cuarto candidato con longitud comprobada bajo política de versión explícita; faltan adaptación, exactitud y cierre de oportunidad |

Estas cuatro son **datasets diferentes, de cuatro publicadores o sistemas de publicación**, no cuatro instituciones regulatorias independientes. Los dos CSV agregado/detalle de `ebby-cjha` son representaciones de una misma fuente y no cuentan como dos fuentes. Los dos cortes consultados de XM tampoco cuentan como fuentes diferentes.

Enlaces:

- EPM: https://www.datos.gov.co/d/sfcd-b3ey
- CHEC: https://www.datos.gov.co/d/c698-wqig
- Superservicios: https://www.datos.gov.co/d/ebby-cjha
- XM: https://www.simem.co/ ; API/documentación: https://github.com/EquipoAnaliticaXM/API_XM . Detalle de consultas y limitaciones en `desarrollo_puntos/3.4/Evaluacion_fuente_alternativa_XM.md`.

#### Verificación adicional de la fuente ZNI

Se recalculó cobertura sobre la copia mensual local, agrupando por empresa y estrato/sector y sumando `consumo_basico_sum` entre las demás categorías:

- 207 grupos distintos.
- **120 grupos con presencia durante al menos 49 meses consecutivos.**
- **117 grupos con suma de consumo básico positiva durante al menos 49 meses consecutivos.**
- Máxima racha positiva: 59 meses.

La nota de incorporación anterior menciona 136 series con al menos 49 meses. Ese conteo no se reproduce con este criterio de consecutividad; no debe usarse como cifra validada del protocolo sin reconciliar definiciones. La presencia temporal no demuestra composición estable, cobertura completa ni meses individuales de cada usuario. El detalle está en `desarrollo_puntos/3.2/perfiles/sspd_verificacion_cobertura_seleccion.json`.

Con 36 cambios de referencia y 12 de vigilancia se requieren 49 observaciones. Una serie completa de 59 observaciones ofrece 58 cambios: 36 de referencia y 22 de vigilancia, no 23. Si se requieren 48 cambios de referencia y 12 de vigilancia, hacen falta 61 observaciones; la fuente ZNI no cumple ese escenario.

#### Fuentes que no cuentan como cuarto caso completo para cartas mensuales

`bnkp-xdb7` y el CSV extraído `supers_icnr-l4iw.csv` tienen estructura no residencial y 12 meses de reporte. El archivo extraído además representa identificadores en notación científica. Se conservan como evidencia de facturación en revisión; no solucionan el cuarto caso completo bajo el protocolo temporal actual. No se suman como fuentes independientes solo por tener nombres de archivo distintos.

No se eliminó ni se alteró la cuarta fuente incorporada por el equipo ni sus resultados de medición. Esta propuesta señala por qué esa selección anterior no acredita cartas en las cuatro fuentes.

#### Condiciones de aceptación antes de afirmar que sirven para todo el proyecto

1. **Historia:** cada fuente debe aportar un conjunto de series homogéneas con meses consecutivos suficientes y datos positivos cuando se utilicen cambios logarítmicos. No confundir número de filas, antigüedad global y longitud por grupo.
2. **Exactitud:** referencia documental verificable y muestra con categorías, unidades, período y versión equivalentes. No sustituir contraste por un detector de valores atípicos.
3. **Oportunidad:** fecha real de disponibilidad y plazo esperado documentado para un alcance explícito. No usar la última carga global o la fecha de factura como sustitutos automáticos.
4. **Reglas:** en ZNI y XM no existen todos los ejes tarifarios de R08/R09 de EPM. Si se permite transferencia mediante adaptadores, definir controles equivalentes por propósito y justificar cada cambio. Si se exigen literalmente las doce reglas tarifarias sin cambios en cada dataset, **esta pareja adicional no cumple** y se necesitan otras dos bases tarifarias.
5. **Integridad:** catálogos autorizados y vigentes por dominio; la ausencia de una columna nombre no elimina la dimensión. Puede contrastarse un código con una maestra externa adecuada.
6. **Validación del framework:** misma política de partición temporal, comparación con línea base, errores conocidos/inyección, precisión, recall, F1, intervalos, costo y reproducibilidad. Las unidades de evaluación y reglas pueden diferir por dominio sin mezclar resultados no comparables.

Las ocho dimensiones siguen siendo obligatorias. Un resultado de calidad bajo es admisible si se puede medir; una dimensión pendiente de evidencia no equivale a un resultado bajo medido ni cumple el requisito.

#### Trabajo para concretar el cuarto caso

- Se descargó un subconjunto filtrado al grupo EPMC/EPMD/STR02, enero de 2020 a enero de 2025, con todas las versiones disponibles. Se conserva en `datos/Datos_seleccionados/XM_piloto/`.
- Se comprobaron 61 meses completos y positivos al seleccionar por mes la TX numérica más alta disponible y sumar horas únicas: 44.592 horas en total. Esta política debe justificarse; no equivale a última versión oficial. Exigir la versión final marcada en el calendario deja solo 53 meses coincidentes y una racha máxima de 20, que no sirve para este protocolo.
- Se vincularon fechas de publicación declaradas de 60 de 61 versiones seleccionadas. Falta junio de 2021 y definir los plazos de cada versión; oportunidad no se declara completa. No se suman revisiones como energía adicional.
- Obtener maestras y un contraste oficial de valores; definir las adaptaciones R08/R09 y el uso de demanda frente a tarifa.
- Completar las evidencias faltantes en EPM, CHEC y ZNI en paralelo al piloto de XM.

**Estado final de esta revisión:** hay una propuesta concreta de cuatro casos con datos locales y longitud temporal utilizable, en XM bajo una política alternativa de versión explícita. Todavía no hay cuatro fuentes validadas para todas las condiciones. No se modifica el catálogo definitivo ni se afirma que el profesor haya aprobado las adaptaciones.


<a id="doc-8b50327833d5"></a>

## fuentes_datos/README.md

### Fuentes seleccionadas: EPM, CHEC, SSPD ZNI y XM/SIMEM

Esta carpeta conserva las dos fuentes tarifarias eléctricas acordadas y dos de facturación,
incorporadas para cubrir el consumo observado que a las dos primeras les falta.

**Revisión del 4 de noviembre:** la fuente SSPD-NR queda en revisión porque solo aporta 12 meses y no cubre las cartas mensuales actuales. La selección principal pasa a ser EPM, CHEC, SSPD ZNI y un piloto histórico de XM. Esta decisión no declara completada la evaluación de las ocho dimensiones ni sustituye automáticamente la matriz medida.

| Fuente | Qué aporta | CSV | Diccionario | Portal |
|---|---|---|---|---|
| **EPM** · 3.623 filas, 12 col. | Tarifa, forma larga | [csv](../Data/bronze/datos/Datos_seleccionados/EPM/epm_sfcd-b3ey.csv) | [epm.yaml](../Data/silver/diccionarios/EPM/epm.yaml) | https://www.datos.gov.co/d/sfcd-b3ey |
| **CHEC** · 40.609 filas, 24 col. | Tarifa, forma ancha | [csv](../Data/bronze/datos/Datos_seleccionados/CHEC/chec_c698-wqig.csv) | [chec.yaml](../Data/silver/diccionarios/CHEC/chec.yaml) | https://www.datos.gov.co/d/c698-wqig |

Los documentos específicos de cada fuente están agrupados en carpetas por dataset dentro de `diccionarios`, `catalogos`, `metadatos` y `verificaciones`.
| **SSPD** · 11.905.557 filas en origen, 29 col. | Consumo y **59 meses** para las cartas | [mensual](../Data/silver/datos/Datos_seleccionados/SSPD/sspd_ebby-cjha_mensual.csv) · [detalle .zip](../Data/bronze/datos/Datos_seleccionados/SSPD/sspd_ebby-cjha_detalle-compressed.zip) | [sspd.yaml](../Data/silver/diccionarios/SSPD/sspd.yaml) | https://www.datos.gov.co/d/ebby-cjha |
| **XM/SIMEM** · 119.928 registros crudos, 61 meses derivados | Demanda horaria y versiones de publicación | [piloto](../Data/silver/datos/Datos_seleccionados/XM_piloto/xm_demanda_mensual_piloto.csv) · [crudo](../Data/bronze/datos/Datos_seleccionados/XM_piloto/xm_demanda_epmc_epmd_str02_202001_202501.csv) | [xm.yaml](../Data/silver/diccionarios/XM/xm.yaml) | https://www.simem.co/ |

#### Por qué hay archivos comprimidos

GitHub avisa sobre los 50 MB y bloquea sobre los 100 MB, así que los dos CSV grandes se
conservan como `.zip`, siguiendo el convenio que ya usaba `supers_icnr-l4iw-compressed.zip`:

| Archivo | Sin comprimir | Comprimido |
|---|---|---|
| `sspd_bnkp-xdb7-compressed.zip` | 74,1 MB | **17,6 MB** |
| `sspd_ebby-cjha_detalle-compressed.zip` | 18,5 MB | **2,7 MB** |

**No hay que descomprimirlos a mano.** Los scripts de medición los leen directamente: el
módulo `desarrollo_puntos/3.3/lector_datos.py` busca cada archivo por nombre y acepta tanto
el CSV suelto como el ZIP que lo contiene. Verificado: las 76 cifras de la matriz son
idénticas antes y después de comprimir.

Para leer los datos **en el navegador**, sin descargar nada, están estos dos, que GitHub
renderiza como tabla:

- [`sspd_bnkp-xdb7_resumen.csv`](../Data/silver/datos/Datos_en_revision/sspd_bnkp-xdb7_resumen.csv) · 885
  filas: consumo, energía reactiva, facturación y tarifa promedio por empresa, período,
  sector, tipo de tarifa y porcentaje de propiedad.
- [`sspd_bnkp-xdb7_catalogos.csv`](../Data/silver/datos/Datos_en_revision/sspd_bnkp-xdb7_catalogos.csv) ·
  569 pares código-nombre, donde se ven las siete claves con el nombre corrupto.

**Las fuentes de consumo se mantienen diferenciadas.** SSPD ZNI aporta la profundidad
temporal —59 períodos consecutivos— y se selecciona para las cartas. SSPD-NR queda en
revisión porque aporta tarifa aplicada, propiedad y régimen interconectado, pero solo tiene
12 períodos. XM se incorpora como cuarto caso histórico de demanda, con 61 meses derivados
mediante una política de selección de versiones documentada.

**La fuente SSPD ZNI no se conserva íntegra.** Pesa unos 9,7 GB en origen, que no es
versionable. En su lugar se conservan **dos censos declarados, no muestras**: uno mensual
agregado que cubre las 91 empresas y los 59 períodos (15.075 filas), y uno de detalle con
todos los registros de la empresa 28111 (91.840 filas). El alcance de cada uno está escrito
en `diccionarios/SSPD/sspd.yaml` y se repite en cada resultado que lo use.

#### Cómo consultar la información

- **Datos:** abrir los CSV con Excel usando UTF-8 y delimitador coma, o leerlos con Python. Conservan las columnas originales. Los importes CHEC necesitan conversión y validación explícitas.
- **Justificación:** [JUSTIFICACION_SELECCION.md](REFERENCIA_TECNICA.md#doc-49ce02ddaa81) explica la selección, las limitaciones y la cobertura prevista por dimensión.
- **Variables:** los YAML explican todas las columnas, tipo oficial, significado, unidad o incertidumbre, rol, reglas relacionadas y uso para series.
- **Dimensiones y reglas:** [dimensiones_reglas.yaml](../Data/silver/diccionarios/dimensiones_reglas.yaml) distingue las doce reglas base de los controles complementarios. Es una especificación documental, no un motor ejecutado.
- **Matriz OE1 del Hito 3:** [Markdown](REFERENCIA_TECNICA.md#doc-cd000226e09e), [CSV para Excel](../Data/gold/outputs/calidad/matriz_oe1.csv) y [YAML](../Data/gold/outputs/calidad/matriz_oe1.yaml). Incluye 19 indicadores por cada una de las cuatro fuentes; XM queda pendiente de medición específica.
- **Metadatos:** `metadatos/` contiene los esquemas y descripciones del portal.
- **Verificaciones:** `verificaciones/` conserva cobertura y validación de CHEC, además de hashes de ambos archivos.
- **Catálogo:** `catalogos/busqueda_tarifas_energia.json` contiene solo EPM y CHEC; es un catálogo curado, no la búsqueda íntegra original.

#### Estado

EPM se conserva con la excepción de tamaño aceptada por el usuario. EPM y CHEC contienen
tarifas y costos, no consumo observado; esa carencia la cubren SSPD ZNI y XM desde dominios
complementarios: consumo/facturación y demanda eléctrica.

**SSPD es de Zonas No Interconectadas.** Sus 91 empresas se verificaron una por una contra
el directorio de Superservicios y ninguna pertenece al Sistema Interconectado Nacional, de
modo que no comparte el régimen tarifario de EPM y CHEC. Se incorpora por el consumo
observado y por la profundidad mensual, no como par tarifario; la matriz OE1 marca
`no_aplica` los controles cuyo concepto no existe en su esquema.

**Es obligatorio evaluar las ocho dimensiones por fuente.** Todavía falta evidencia externa para exactitud y oportunidad. No se afirma cobertura completa ni se considera “no evaluable” cumplimiento final. Los YAML identifican esas brechas y las definiciones pendientes.

Se eliminaron los datasets descartados, muestras y documentos de recomendaciones anteriores de esta carpeta. El código y los documentos del proyecto fuera de `fuentes_datos/` no fueron modificados.


<a id="doc-1e1e212fc147"></a>

## fuentes_datos/REVISION_CREG_ELECTRICIDAD.md

### Prioridad CREG: búsqueda de fuentes eléctricas

Revisión: 4 de noviembre de 2026. El usuario confirmó **mantener solo electricidad**. La CREG tiene prioridad como publicador, siempre que el conjunto permita cumplir la metodología. No se reduce el requisito de ocho dimensiones ni se cuentan anexos y vistas como casos completos solo para alcanzar cuatro fuentes.

#### 1. Electricidad: panel de comercializadores, Circular 125 de 2025

Publicación oficial: https://gestornormativo.creg.gov.co/gestor/entorno/docs/circular_creg_0125_2025.htm

Excel oficial: https://gestornormativo.creg.gov.co/gestor/entorno/docs/originales/Circular_CREG_125_2025/Datos%20panel-IPC-empresas.xlsx

Archivo local: `datos/Datos_en_revision/CREG_prioridad/creg_panel_electrico_circular125_2025.xlsx`.

Se descargó el Excel y se inspeccionó su hoja:

- **88 registros de datos, 11 columnas y 23 empresas**.
- **Cinco períodos anuales: 2019, 2020, 2021, 2022 y 2023**; no todas las empresas tienen necesariamente los cinco.
- Columnas originales: `Empresa`, `Periodo`, `CG`, `EmpSer`, `DepAmo`, `GenMan`, `UsuRur`, `UsuUrb`, `Usu`, `RedUrb`, `RedRur`.
- Entre las empresas figuran EPM, CHEC, ESSA y EDEQ. Se conservaron los nombres observados; no se interpretan las siglas de costos sin revisar el informe técnico.
- El archivo contiene celdas vacías, coherentes con la necesidad de estudiar el alcance de información publicada. La circular advierte exclusión de información cuya divulgación no fue autorizada; no se infiere que cada vacío tenga esa causa.

**Decisión:** referencia sectorial prioritaria por ser CREG y electricidad, pero **no apta como caso completo del protocolo actual**: no cumple 10.000 registros ni longitud mensual de 49/61 observaciones. Tener fecha de la circular no equivale a contar con historia de disponibilidad mensual. No se transforman los cinco años en meses ficticios ni se multiplican filas por variables para cumplir volumen.

#### 2. Electricidad: calidad de distribución, Circulares 053 y 064 de 2015

Publicaciones oficiales:

- https://gestornormativo.creg.gov.co/gestor/entorno/docs/circular_creg_0053_2015.htm
- https://gestornormativo.creg.gov.co/gestor/entorno/docs/circular_creg_0064_2015.htm

Se descargaron cuatro libros oficiales en `datos/Datos_en_revision/CREG_prioridad/`:

- `creg_calidad_sdl_053_2015_anexo.xlsx`.
- `creg_calidad_sdl_053_2015_anexo2.xlsx`.
- `creg_calidad_sdl_064_2015_anexo2.xlsx`.
- `creg_calidad_sdl_064_2015_anexo3.xlsx`.

Se inspeccionaron sus hojas por empresa, incluidas EPM, CHEC, ESSA y EDEQ. Contienen cuadros de frecuencia/duración, objetivos, ajustes y escenarios por año. Por ejemplo, en el anexo 2 de la Circular 064, la hoja EPM muestra indicadores reales y proyecciones «Año 0» a «Año 4». **Son resultados y escenarios de un estudio, no una serie mensual cruda verificada.**

Las hojas tienen aproximadamente 46–47 filas XML, que también incluyen etiquetas, fórmulas y formato; ese conteo no representa registros de interrupciones. Las celdas con años de escenario no se pueden tratar como observaciones históricas para cartas.

El informe del estudio menciona bases masivas utilizadas en el análisis. **Eso no demuestra que los anexos descargados contengan o hagan descargables esos microdatos.** No se verificó acceso a los archivos por transformador/evento mencionados en el informe ni su longitud temporal.

**Decisión:** conservar como referencias técnicas CREG, no contar estos cuatro archivos como cuatro datasets independientes aptos para todo el proyecto.

#### 3. Estadísticas históricas eléctricas

ARIAE referencia estadísticas del sector eléctrico con autor/editor CREG:
https://www.ariae.org/servicio-documental/estadisticas-del-sector-electrico-de-colombia

La referencia es una pista de localización, no evidencia suficiente de un conjunto actualmente descargable. No se ha validado archivo, volumen, periodicidad ni continuidad por grupo para contarlo como caso completo.

#### 4. Gas: excluido por decisión de alcance

El catálogo sí ofrece `ek3f-5wn4`, tarifas de gas publicadas por CREG. Se verificaron 165.360 filas y 238 meses, pero **no se incorpora porque el usuario decidió mantener solo electricidad**. Se retiró el CSV descargado del área de candidatos; quedan metadatos y un perfil pequeño como evidencia del descarte.

Las entradas `mbkj-hd98`, `f8zf-xyx8`, `duwb-pa7h`, `79rk-nbgs` y `qzkz-3vyk` son filtros o visualizaciones derivados de `ek3f-5wn4` según el catálogo consultado. No son cinco fuentes independientes. La consulta `q=CREG` devolvió 62 resultados; no se presenta como un censo de todo lo que la entidad podría publicar fuera de ese catálogo.

#### Conclusión operativa

La prioridad CREG se mantiene, pero **esta revisión no identificó una fuente eléctrica publicada directamente por CREG que pueda declararse apta para todo el protocolo actual**. No es una afirmación de inexistencia: se documentan las publicaciones examinadas y sus limitaciones concretas.

Hasta disponer de una candidata CREG que supere esas pruebas, la propuesta de cuatro casos de electricidad sigue siendo **EPM, CHEC, Superservicios ZNI y XM**, con los pendientes de ocho dimensiones y reglas ya declarados. Los datos de XM están regulados por CREG, pero su publicador es XM; no se cambia su atribución.

Las bases CREG se pueden utilizar para fundamentar variables y contextualizar resultados, sin presentarlas como cumplimiento del cuarto caso ni usar valores de otra unidad/período como verdad de referencia automáticamente. No se modifica el catálogo definitivo ni se sustituyen los datasets medidos.

#### Evidencia local

- `metadatos/candidatos_creg/catalogo_creg_2026-11-04.json`: respuesta de catálogo y relaciones entre vistas.
- `desarrollo_puntos/3.4/perfiles/creg_electricidad_anexos.json`: archivos, hojas, conteos XML y hashes de los libros eléctricos.
- `desarrollo_puntos/3.4/perfiles/creg_prioridad_perfil.json`: perfil del conjunto de gas descartado; no es una fuente seleccionada.

La fecha y los hashes registran la revisión/descarga; no prueban por sí solos oportunidad histórica por período.


<a id="doc-f87bbef16802"></a>

## fuentes_datos/verificaciones/SOLICITUD_VALIDACION_EPM.md

### Solicitud de validación semántica EPM

Este documento registra las confirmaciones que faltan para cerrar completamente
`MAP01`, `DEF01` y `OPO01` sin inferir significados a partir de nombres.

1. ¿`No Residencial` y `No residencial` representan exactamente la misma categoría?
2. ¿`0-CS` equivale a `Rango 0 - CS` y `Mayor CS` equivale a `Rango > CS`?
3. ¿Qué unidad tiene cada importe (`propiedadepm`, `compartido`,
   `propiedaddelcliente`, `punta` y `fueradepunta`) según `tipodedato` y `nivel`?
4. ¿Qué significa `N/A` en `rangodeconsumo` y cuándo es aplicable cada franja?
5. ¿Cuál era la fecha límite y cuál fue la fecha real de publicación de cada tarifa
   mensual de diciembre de 2016 a diciembre de 2021?

Hasta recibir esta confirmación, la matriz debe conservar los estados `provisional`
o `no_medible`; no deben convertirse en 100 % por similitud textual.


<a id="doc-351c00955bb1"></a>

## fuentes_datos/verificaciones/trazabilidad_filas/README.md

### Trazabilidad estable del Hito 3

La ejecución de `python3 desarrollo_puntos/3.6/trazabilidad.py` produce:

- Un archivo de correspondencia por dataset con posición física, `clave_contenido` e
  `id_fila_estable`.
- SHA-256, tamaño, filas, columnas y fecha de ejecución en
  `desarrollo_puntos/3.6/trazabilidad/manifiesto_ejecucion.json`.
- Copias enriquecidas de los hallazgos y alertas históricas del Hito 2 con
  `clave_contenido`, sin modificar los archivos originales.

La `clave_contenido` se calcula sobre todas las columnas de la fila, serializadas como
JSON UTF-8 canónico y ordenadas por nombre. Por tanto, no cambia si el portal devuelve
las mismas filas en otro orden. En copias exactas, `id_fila_estable` añade la ocurrencia
ordenada para distinguir instancias sin confundirlas con filas diferentes.

La posición de fila se conserva solo como referencia de lectura; no es la identidad del
registro.

#### Cuarentena por fuente

`desarrollo_puntos/3.7/cuarentena_fuentes.py` genera los archivos `*_cuarentena.csv`
para CHEC, SSPD y XM. Actualmente tienen cero filas: no se encontraron valores no
numéricos o negativos en medidas que el catálogo permita declarar estrictamente no
negativas. Los negativos de CHEC se conservan porque pueden corresponder a restricciones,
subsidios o ajustes; no se clasifican como error sin semántica aprobada. La cuarentena de
EPM sí contiene registros y se integra a sus cartas mediante
`desarrollo_puntos/3.7/EPM/cuarentena.py`.


<a id="doc-e050028ca414"></a>

## requirements/README.md

### Entornos reproducibles del Hito 4

Los análisis 4.2 y 4.3–4.4 usan versiones diferentes de `numpy` y `scikit-learn`.
Por eso se entregan dos archivos bloqueados y no un único `requirements.txt`: mezclarlos
alteraría el entorno que produjo los resultados validados.

Las versiones se validaron con **Python 3.14.6** en macOS arm64. En otro sistema puede
funcionar con una versión compatible de Python, pero esa ejecución debe registrarse como
una nueva validación, no como una reproducción idéntica del entorno.

#### Hito 4.2

Desde la raíz del repositorio:

```bash
python3 -m venv .venv-hito42
.venv-hito42/bin/python -m pip install -r requirements/requirements-hito4-2.txt
.venv-hito42/bin/python desarrollo_puntos/4.2/analisis_sensibilidad.py
.venv-hito42/bin/python desarrollo_puntos/4.2/informe_sensibilidad.py
.venv-hito42/bin/python -m unittest discover -s desarrollo_puntos/4.2 -p test_sensibilidad.py -v
.venv-hito42/bin/python desarrollo_puntos/4.2/verificar_resultados.py
```

#### Hitos 4.3 y 4.4

```bash
python3 -m venv .venv-hito43_44
.venv-hito43_44/bin/python -m pip install -r requirements/requirements-hito4-3-4.txt

.venv-hito43_44/bin/python desarrollo_puntos/4.3/experimento_tasa_igualada.py
.venv-hito43_44/bin/python desarrollo_puntos/4.3/informe_metricas.py
.venv-hito43_44/bin/python -m unittest discover -s desarrollo_puntos/4.3 -p test_metricas.py -v
.venv-hito43_44/bin/python desarrollo_puntos/4.3/verificar_resultados.py

.venv-hito43_44/bin/python desarrollo_puntos/4.4/calibrar_regla_sistemica.py
.venv-hito43_44/bin/python desarrollo_puntos/4.4/informe_regla_sistemica.py
.venv-hito43_44/bin/python -m unittest discover -s desarrollo_puntos/4.4 -p test_regla_sistemica.py -v
.venv-hito43_44/bin/python desarrollo_puntos/4.4/verificar_resultados.py
```

Las carpetas `.venv-hito42/` y `.venv-hito43_44/` están ignoradas por Git. Las figuras se
generan localmente desde los CSV y tampoco se versionan; los resultados tabulares, scripts,
configuraciones y manifiestos SHA-256 sí permanecen en el repositorio.


<a id="doc-b8f4ce33e31c"></a>

## Guía explicativa histórica del proyecto

### Guía explicativa del proyecto

> **Cómo leer esta guía.** Las secciones 1 a 14 explican la base del proyecto y el Hito 3. Las secciones 15 a 23
> explican el Hito 4 (puntos 4.1 a 4.6): qué se hizo, cómo, por qué se hizo así, qué se encontró y qué sigue
> pendiente. Si solo necesitas saber qué está terminado, ve directo a la [sección 21](#21-están-completos-43-y-44).

#### 1. ¿Qué estamos haciendo?

El proyecto construye un framework para evaluar la calidad de datos del sector energético. En
palabras sencillas, queremos responder:

> ¿Podemos confiar en estos datos para analizarlos, compararlos y tomar decisiones?

La calidad de datos no significa solamente que un archivo abra o tenga muchas filas. También hay
que revisar si:

- faltan datos;
- las fechas son válidas;
- los importes tienen formato correcto;
- existen filas duplicadas;
- los códigos y nombres son coherentes;
- los valores están dentro de rangos razonables;
- los datos corresponden con una fuente externa;
- los datos fueron publicados oportunamente;
- las series temporales tienen un comportamiento estable.

El proyecto usa DAMA-DMBOK como marco de dimensiones de calidad y agrega reglas estadísticas para
revisar el comportamiento temporal de las tarifas, costos y demanda eléctrica.

#### 2. ¿Qué significa Hito 3?

El Hito 3 es la etapa en la que se formaliza la evaluación. Aquí no se intenta todavía construir
el tablero final ni comparar todos los modelos. Primero se deja claro:

1. qué fuentes se van a estudiar;
2. qué significa cada columna importante;
3. qué reglas se aplican;
4. cómo se calcula cada indicador;
5. cómo se conservan las evidencias;
6. cómo se identifican anomalías;
7. qué resultados son definitivos y cuáles son provisionales.

El Hito 3 funciona como una línea base. El Hito 4 utilizará esa línea base para crear scorecards,
comparar técnicas y hacer análisis de sensibilidad.

#### 3. Las cuatro fuentes seleccionadas

##### EPM — `sfcd-b3ey`

Es un histórico de tarifas de energía eléctrica. Tiene 3.623 filas y 12 columnas, con información
mensual de tarifas y categorías. Permite construir series por combinación tarifaria y aplicar
cartas de control.

##### CHEC — `c698-wqig`

Es un conjunto de costos unitarios y tarifas de energía. Tiene 40.609 filas y 24 columnas, con
cobertura aproximada de 2008 a 2026. Contiene componentes como generación, transmisión,
distribución, comercialización, pérdidas, restricciones y valores agregados.

CHEC es útil para estudiar tarifas, pero varios códigos requieren confirmación documental. Por
eso algunas reglas están marcadas como provisionales.

##### Superservicios — `ebby-cjha`

Es información comercial residencial y no residencial. El proyecto conserva un agregado mensual
de 15.075 filas y un detalle comprimido. Permite analizar consumo, facturación y variables
comerciales por periodo y categoría.

##### XM/SIMEM — `c1b851`

Es un piloto de demanda eléctrica. La consulta original contiene 119.928 registros horarios y
se derivó una serie mensual de 61 observaciones. No representa todo el mercado XM: corresponde a
un grupo filtrado de agente, mercado y sistema de transmisión.

XM se usa como fuente operativa de demanda, no como fuente tarifaria. Por ello algunas reglas
originalmente diseñadas para tarifas se adaptaron y se marcaron como provisionales.

#### 4. ¿Dónde están los archivos?

##### Datos originales seleccionados

`fuentes_datos/datos/Datos_seleccionados/`

Contiene los CSV y archivos asociados de EPM, CHEC, SSPD y XM. Estos archivos no deben modificarse
manualmente porque son la base de la trazabilidad.

##### Diccionarios

`fuentes_datos/diccionarios/`

Explican las columnas: nombre, tipo de dato, significado, unidad, reglas relacionadas y
limitaciones conocidas.

##### Catálogos

`fuentes_datos/catalogos/`

Contienen equivalencias, dominios y definiciones operativas. Un catálogo sirve para saber, por
ejemplo, qué códigos son válidos o qué nombre corresponde a un código.

##### Fichas de caracterización

`desarrollo_puntos/3.2/`

Cada ficha describe una fuente: quién la publica, qué contiene, cuál es su cobertura, quién podría
usar los datos, cuáles son sus variables críticas y qué limitaciones tiene.

##### Resultados del Hito 3

Los resultados se distribuyen según las actividades del plan:

- `desarrollo_puntos/3.1/`: matriz OE1, indicadores y evidencia de medición.
- `desarrollo_puntos/3.2/`: fichas y perfiles de caracterización.
- `desarrollo_puntos/3.3/`: adaptadores, revisión de reglas e informe de diferencias.
- `desarrollo_puntos/3.4/`: evaluación de fuentes CREG y alternativas.
- `desarrollo_puntos/3.5/`: cartas logarítmicas y señales.
- `desarrollo_puntos/3.6/`: trazabilidad y reproducibilidad.
- `desarrollo_puntos/3.7/`: cuarentena y bootstrap.

El [índice general](REFERENCIA_TECNICA.md#doc-393500a1bb5a) reúne enlaces,
criterios y el inventario de movimientos. El plan, cierre y pendientes generales están
en esa misma carpeta. Los resultados históricos del Hito 2 se conservan como insumos en
`desarrollo_puntos/3.3/insumos_hito2/`.

##### Resultados del Hito 4

Cada punto del plan tiene su carpeta, con un README que indica qué archivo contiene qué:

- `desarrollo_puntos/4.1/`: Z-score robusto, Isolation Forest con entrenamiento solo en referencia y
  calibración a tasa de alerta igualada.
- `desarrollo_puntos/4.2/`: análisis de sensibilidad. Informe en
  [INFORME_SENSIBILIDAD.md](REFERENCIA_TECNICA.md#doc-6e8fab534d7e).
- `desarrollo_puntos/4.3/`: precisión, recall y F1 a tasa de alerta igualada. Informe en
  [INFORME_METRICAS.md](REFERENCIA_TECNICA.md#doc-7712518cbe50).
- `desarrollo_puntos/4.4/`: regla de alerta sistémica, catálogo y contraste con publicaciones de EPM. Informe en
  [INFORME_REGLA_SISTEMICA.md](REFERENCIA_TECNICA.md#doc-4ce62780cc42). La subcarpeta
  `evidencia_externa/` guarda los PDF oficiales de EPM que se leyeron.
- `desarrollo_puntos/4.5/`: scorecard por fuente y dimensión. El resultado actual es provisional y está en
  [scorecard_oe1_provisional.csv](../Data/gold/outputs/scorecard/scorecard_oe1_provisional.csv).
- `desarrollo_puntos/4.6/`: resultados separados por nivel y costos computacionales. La explicación está en
  [INFORME_NIVELES_COSTO.md](REFERENCIA_TECNICA.md#doc-9616b9e5ae82).

#### 5. Las ocho dimensiones de calidad

La matriz revisa las ocho dimensiones exigidas por el proyecto:

| Dimensión | Pregunta sencilla |
|---|---|
| Completitud | ¿Están presentes los datos que deberían existir? |
| Validez | ¿Los valores cumplen el formato y dominio permitido? |
| Unicidad | ¿Hay duplicados o varias filas para la misma clave? |
| Consistencia | ¿Los valores y relaciones son coherentes entre sí? |
| Integridad | ¿Se conservan las relaciones y el contrato estructural? |
| Exactitud | ¿El dato coincide con una fuente confiable? |
| Oportunidad | ¿El dato estuvo disponible dentro del plazo esperado? |
| Razonabilidad | ¿El comportamiento del dato es esperable y estable? |

Una fuente puede tener una dimensión aplicable aunque su resultado sea provisional. Si el concepto
no existe en el esquema, se marca `no_aplica`. Si existe pero no hay evidencia para calcularlo, se
marca `no_medible`.

#### 6. Las reglas y los controles

La matriz contiene 19 controles para cada fuente, es decir, 76 filas en total. Incluye las reglas
R01–R12 y controles complementarios:

- R01–R02: periodos informados y válidos;
- R03: importes numéricos y finitos;
- R04–R05: duplicados y multiplicidad de claves;
- R06: representación canónica de categorías;
- R07: signos y rangos por concepto;
- R08–R09: relaciones entre tarifas y categorías;
- R10: importes requeridos disponibles;
- R11: detección de posibles fechas almacenadas como importes;
- R12: prevalencia de magnitudes atípicas;
- INT01–INT02: integridad estructural y referencial;
- EXA01: contraste documental de exactitud;
- OPO01: disponibilidad dentro del plazo;
- MAP01: equivalencias de etiquetas;
- DEF01: documentación de variables críticas;
- CART01: señales de cartas de control.

Cada control tiene población, numerador, denominador, fórmula, unidad, umbral, severidad,
frecuencia, responsable, aplicabilidad y nota metodológica.

Por ejemplo, R01 calcula:

`filas con periodo informado / total de filas × 100`

El resultado es un porcentaje. El porcentaje no se interpreta correctamente si no se conoce qué
filas entraron al denominador.

#### 7. ¿Qué significa que un resultado sea provisional?

Los estados de la matriz son importantes:

- `medido`: el control se pudo calcular con la definición actual sin supuestos adicionales.
- `provisional`: hay un valor, pero falta aprobar una decisión documental o de negocio.
- `provisional_interno`: el cálculo depende de una decisión interna todavía no aprobada.
- `provisional_proxy`: se utilizó una medida indirecta porque no existe la evidencia ideal.
- `no_medible`: el control está definido, pero no hay datos suficientes para calcularlo.
- `no_aplica`: el concepto no existe en esa fuente.

Estos estados evitan presentar una cifra provisional como si fuera una verdad definitiva.

#### 8. Cartas de control

Una carta de control observa una serie temporal y ayuda a detectar cambios inusuales. En este
proyecto se usan cartas I-MR:

- carta I: observa los valores individuales;
- carta MR: observa el cambio entre valores consecutivos.

Se utilizaron cambios logarítmicos para comparar variaciones relativas. Esto es más adecuado que
comparar únicamente diferencias absolutas cuando las tarifas o demandas tienen escalas distintas.

Una señal significa que una observación merece revisión. No significa automáticamente que el dato
sea incorrecto.

Las cartas se guardan por fuente en:

`desarrollo_puntos/3.5/EPM/`, `CHEC/`, `SSPD/` y `XM/`.

#### 9. Cuarentena

La cuarentena es una lista separada de registros que deben excluirse del cálculo de límites porque
ya existe evidencia de que pueden distorsionar la carta.

La cuarentena no borra filas del dataset y no interpola valores. Solo evita que esos cambios se
usen para calcular los límites estadísticos. El registro original permanece intacto.

EPM tiene una cuarentena trazable con 9 registros. Para las demás fuentes se aplicó una política
conservadora y no se identificaron valores que justificaran excluirlos automáticamente.

#### 10. Trazabilidad

La trazabilidad permite responder:

> ¿De qué archivo salió este resultado y cómo sé que no cambió?

Para cada fuente se conserva:

- SHA-256 del archivo;
- tamaño y número de filas;
- número de columnas;
- fecha de ejecución;
- clave estable de contenido;
- identificador de cada fila;
- vínculo entre hallazgos y filas originales.

El manifiesto está en:

`desarrollo_puntos/3.6/trazabilidad/manifiesto_ejecucion.json`

El SHA-256 es una huella digital del archivo. Si cambia un carácter, la huella normalmente cambia.
No es un método de cifrado ni muestra el contenido del archivo.

#### 11. Bootstrap

El bootstrap se usa para estimar la variabilidad de la tasa de señales de CART01. En lugar de
tratar cada fila horaria o mensual como independiente, se remuestrean series completas dentro de
su categoría.

La ejecución actual usa:

- 2.000 repeticiones;
- semilla `20261105`;
- 105 categorías;
- intervalos de confianza del 95 %.

Resultados por fuente:

- EPM: 8 categorías y 60 series;
- CHEC: 4 categorías y 276 series;
- SSPD: 92 categorías y 361 series;
- XM: 1 categoría y 1 serie.

Si una categoría tiene una sola serie, el intervalo resulta degenerado. Eso no es un error del
programa; significa que no hay suficiente variación entre series para estimar incertidumbre.

#### 12. Qué se ha validado técnicamente

Se ejecutaron correctamente:

```bash
python3 desarrollo_puntos/3.1/medir_matriz_oe1.py
python3 desarrollo_puntos/3.7/bootstrap_categorias.py
python3 desarrollo_puntos/3.6/trazabilidad.py
```

La ejecución genera:

- 76 filas de matriz;
- 105 resultados de bootstrap;
- manifiesto de trazabilidad para cuatro archivos fuente.

#### 13. Qué todavía no está aprobado

Los pendientes están reunidos en:

[PENDIENTES_APROBACION_HITO3.md](REFERENCIA_TECNICA.md#doc-349c3e6eb49a)

En resumen:

- nombres de los responsables y aprobador final;
- umbrales y severidad;
- catálogos oficiales de CHEC;
- fuente y muestra para exactitud;
- plazos oficiales para oportunidad;
- segunda descarga independiente;
- decisión final sobre R10, R12 y CART01.

No se deben inventar estas aprobaciones. Mientras no existan, los resultados correspondientes
deben permanecer identificados como provisionales, proxy o pendientes.

#### 14. Qué significa estar listos para el Hito 4

> Esta sección se escribió al cerrar el Hito 3. El estado actual del Hito 4 está en las secciones 15 a 24.

La línea base del Hito 3 ya se utilizó para construir los entregables del Hito 4. El Hito 4 contiene:

1. scorecards por fuente y dimensión;
2. comparación de técnicas bajo el mismo protocolo;
3. análisis de sensibilidad;
4. comparación con procedimientos tradicionales;
5. conclusiones usando intervalos y estados de evidencia.

El Hito 4 no debe ocultar los estados provisionales ni comparar porcentajes sin revisar población,
unidad, aplicabilidad y evidencia.

#### 15. Qué se ha hecho del Hito 4

El Hito 4 compara técnicas bajo el mismo protocolo. Su plan tiene seis puntos:

| Punto | Qué pide el plan | Estado | Dónde |
|---|---|---|---|
| 4.1 Técnicas adicionales | Z-score robusto, LOF o KNN, Extended Isolation Forest | **Parcial.** Z-score robusto e Isolation Forest en 4.1; LOF y KNN se agregaron en 4.3; Extended IF no se hizo | `4.1/`, `4.3/` |
| 4.2 Sensibilidad | Ventanas, constantes, percentiles, R12, detección en t y t+1, regla sistémica | **Hecho** | `4.2/` |
| 4.3 Métricas completas y honestas | Precisión, recall y F1 a tasa igualada, curvas, pruebas por tipo, sorteo sin reemplazo | **Hecho, con límites** (sección 21) | `4.3/` |
| 4.4 Regla de alerta sistémica | Definir X, calibrarlo con tres meses, contrastar con la CREG y EPM | **Hecho, con pendientes** (sección 21) | `4.4/` |
| 4.5 Scorecard por dimensión | Tabla única con umbral y estado por indicador y fuente | **Solo provisional** | `4.5/` |
| 4.6 Resultados por nivel y costo de cómputo | Separar el Nivel I de los niveles II a IV; tiempos por etapa | **Hecho con alcance explícito**: niveles donde existen y `No_aplica` en SSPD/XM | `4.6/` |

Los Hitos 5 (artefacto: paquete, contenedor, tablero) y 6 (validación y sustentación) todavía no tienen trabajo.

#### 16. Hito 4.1 y 4.2 en lenguaje sencillo

##### El protocolo común

Todas las técnicas se miden igual, para que la comparación sea justa:

1. Se trabaja con **cambios logarítmicos** mes a mes (una variación relativa, no una diferencia en pesos).
2. Los **36 primeros cambios** de cada serie son la **referencia**: lo que se considera “normal”.
3. Los **12 siguientes** son la **vigilancia**: ahí se busca lo anormal.
4. Solo se comparan **meses consecutivos**; si falta un mes no se inventa ni se cruza el hueco.

##### Qué es cada técnica

- **Carta I-MR.** Marca un mes si su cambio cae fuera de unos límites calculados con el promedio de los cambios de
  referencia (carta I, constante 2,66) o si el salto respecto al mes anterior es demasiado grande (carta MR,
  constante 3,267). Es el método estadístico clásico de control de procesos.
- **Z-score robusto.** Mide cuántas “desviaciones robustas” se aleja un cambio de lo habitual. Usa la **mediana** y el
  **MAD** (desviación absoluta de la mediana) en lugar del promedio y la desviación estándar, porque unos pocos valores
  extremos no los distorsionan. Fórmula: `0,6745 × (cambio − mediana) / MAD`. Señal si el valor absoluto supera 3.
- **Isolation Forest.** Un conjunto de árboles que intenta “aislar” cada observación. Las más fáciles de aislar son las
  más raras. Se entrena **solo con la referencia** y se evalúa en la vigilancia, para que no “vea el futuro”.
- **LOF y KNN** (agregados en 4.3). Comparan cada observación con las observaciones normales más cercanas: si está muy
  lejos de ellas, es rara.
- **R12.** No es una técnica estadística sino una regla: marca un valor si supera 5, 10 o 20 veces la mediana de su serie.

##### Qué mostró la sensibilidad (4.2)

Se repitió el análisis variando una cosa a la vez: ventana de referencia (24, 36 y 48 cambios), constantes de las cartas,
percentil del Isolation Forest (99 y 99,5), factor de R12 (5, 10 y 20), detección en el mes del error o hasta el
siguiente, y el efecto de la regla sistémica. En total fueron 22 escenarios. Dos aprendizajes:

- **SSPD no permite ventana de 48**: necesitaría 61 meses y solo hay 59. Se declara “no evaluable” en lugar de recortar.
- **Una tasa de alerta baja no significa mejor calidad.** Un método que casi no alerta también detecta poco.

#### 17. Hito 4.3: métricas completas y honestas

##### La pregunta

¿Qué técnica detecta mejor los errores, **en igualdad de condiciones**? Hasta 4.2 cada método alertaba con su propia
frecuencia, así que no se podían comparar de forma justa. Además faltaban precisión y F1, que el anteproyecto promete.

##### Palabras que conviene entender

- **Tasa de alerta:** de cada 100 meses reales vigilados, cuántos dispara un método. Ejemplo: 5 de cada 100 = 5 %.
- **Tasa de alerta igualada:** se ajusta el umbral de cada método para que todos alerten lo mismo (por ejemplo, 5 %) sobre
  los datos reales. Así solo pueden diferenciarse por **cuánto detectan de lo inyectado**.
- **Error inyectado:** se altera a propósito un valor conocido para ver si el método lo atrapa. Hay seis tipos: decimal ×1000,
  decimal ÷1000, serial de fecha de Excel (43.577), aumento del 10 %, valor no actualizado (igual al mes anterior) y valor
  de otra medida.
- **Recall (sensibilidad):** de los errores inyectados, qué fracción se detectó.
- **Precisión:** de las alertas disparadas, qué fracción corresponde a un error de verdad.
- **F1:** un solo número que combina precisión y recall (media armónica).
- **Prevalencia:** qué proporción de los datos tiene errores. **No se conoce.** La precisión depende de ella: con pocos
  errores reales, hasta un buen detector acierta poco entre sus alertas. Por eso se reporta con prevalencias supuestas del
  1, 5 y 10 %.
- **“Alerta sin error conocido”:** en los datos reales no hay etiquetas que confirmen cuáles alertas son falsas. Por honestidad
  no se las llama “falsas alarmas”: son alertas cuyo origen no está confirmado.
- **Recall macro:** promedio de los recall de los seis tipos, con el mismo peso, para que ningún tipo domine.
- **Bootstrap por categoría:** para medir la incertidumbre se remuestrean categorías completas (no filas sueltas), porque las
  series de una misma categoría se parecen entre sí y no son independientes.
- **Sorteo sin reemplazo:** al elegir los meses de prueba, un mes no se puede repetir dentro de la misma serie.

##### Cómo se hizo, paso a paso

1. Se tomaron los mismos datos, modelos y errores inyectados de 4.2 (EPM 27 series, CHEC 276, SSPD 321 y XM 1).
2. Cada uno de **seis métodos** (cartas I-MR, Z-score robusto, Isolation Forest, LOF, KNN y R12) produce un **puntaje continuo**:
   cuanto más alto, más anómalo.
3. Para cada fuente se fija el umbral de cada método de modo que deje por encima el 1, 2, 5 o 10 % de los meses reales.
4. Se cuenta qué fracción de los errores inyectados supera ese umbral: recall por tipo y recall macro.
5. Con el recall y la tasa de alerta se calcula la precisión para cada prevalencia supuesta, y de ahí el F1.
6. La incertidumbre (intervalo de confianza al 95 %) sale de 1.000 remuestreos por categorías.
7. Como comprobación, se hizo un **sorteo sin reemplazo** (500 réplicas, 3 meses distintos por serie) que reproduce el
   cálculo completo con una diferencia máxima de 6 puntos porcentuales (EPM).
8. Un verificador recalcula los umbrales, las detecciones, la precisión y el F1 desde los puntajes guardados y los compara con
   las tablas.

##### Por qué se hizo así

- **Igualar la tasa** evita la trampa de comparar un método que alerta mucho con otro que alerta poco.
- **Puntajes continuos** hacen posible esa igualación; con reglas de sí/no no se podría.
- **Prevalencias supuestas** en lugar de una sola prevalencia inventada: así no se fabrica una precisión que los datos no
  respaldan.
- **Bootstrap por categorías** corrige el problema señalado en la revisión del Hito 2: contar series casi idénticas como
  independientes hace que los intervalos parezcan más estrechos de lo que son.
- **Sorteo sin reemplazo y denominadores a la vista** responden a la observación de esa revisión sobre meses repetidos y
  números de pruebas distintos por tipo.
- **LOF y KNN** se agregaron porque el plan los pedía en 4.1 y no existían; sin ellos la comparación quedaba incompleta.

##### Resultados (F1 a tasa de alerta del 5 %, prevalencia supuesta del 5 %, detección en el mes del error)

| Método | EPM | CHEC | SSPD |
|---|---|---|---|
| Cartas I-MR | 0,49 | 0,58 | 0,51 |
| Z-score robusto | 0,52 | 0,59 | 0,51 |
| Isolation Forest | 0,49 | 0,54 | 0,49 |
| LOF | 0,44 | no aplicable (degenerado) | 0,35 |
| KNN | 0,50 | 0,56 | 0,48 |
| R12 | 0,32 | 0,37 | 0,25 |

Cómo leerlo:

- **I-MR, Z-score robusto, Isolation Forest y KNN no se distinguen de forma consistente:** sus intervalos se solapan. De
  14 comparaciones pareadas frente a I-MR, solo una excluye el cero a favor de otro método (Z-score en EPM, +0,035).
- **LOF y R12 rinden menos que las cartas**, con claridad en SSPD (89 categorías, intervalos estrechos). En EPM y CHEC hay
  pocas categorías (5 y 4) y los intervalos son demasiado anchos para afirmarlo.
- **Los errores groseros se detectan casi siempre** (decimal ×1000, ÷1000 y serial de Excel, con recall cercano a 1 en EPM y CHEC).
  **El aumento del 10 % solo se detecta bien en EPM y CHEC** (0,6 a 0,9 con I-MR o Z-score) y poco en SSPD (0,1 a 0,2).
- **Ningún método estadístico detecta el “valor no actualizado”** (recall entre 0,00 y 0,08): un valor repetido no es un cambio
  raro. Se atrapa con una regla, no con una carta. Es un argumento a favor del framework “reglas + cartas”.

##### Sensibilidad a las etiquetas de EPM

EPM escribe de varias formas la misma etiqueta según el mes (por ejemplo “Costo compra: Gm, i” y “Costo Compra: Gm, i”). Sin normalizarlas,
una misma serie económica se parte y el panel común de EPM queda en **27 series**. Se repitió todo el experimento con las 11 equivalencias
aprobadas internamente en el Hito 2 como una fuente adicional (`EPM_canonicas`): el panel pasa a **69 series** y 4.191 casos. Resultado:
**las conclusiones no cambian.** I-MR, Z-score, Isolation Forest y KNN siguen sin separarse (F1 entre 0,50 y 0,55, antes entre 0,49 y 0,52),
R12 sigue siendo el más bajo y LOF pasa también a degenerado. No sustituye al resultado principal: 4.1, 4.2 y la matriz de indicadores usan las
etiquetas originales, y aceptar las equivalencias como oficiales es una decisión del equipo y del director.

##### Límites que hay que decir en voz alta

- **XM** tiene una serie y 12 observaciones: a tasa del 5 % se esperan 0,6 alertas. Sus resultados son descriptivos y **no
  interpretables** (su precisión sale 100 % solo porque no hay alertas).
- **LOF en CHEC es numéricamente degenerado**: el entrenamiento tiene 9.936 filas pero solo 2.126 distintas, y LOF se rompe
  con duplicados exactos. Se conserva el cálculo marcado como degenerado, no se oculta. Con etiquetas canónicas le pasa lo mismo a EPM.
- Los umbrales se calibran con los mismos meses reales donde luego se mide la tasa de alerta (sin etiquetas, pero sin
  separación temporal).
- El experimento es **retrospectivo** (mira un mes adelante): sirve para auditar datos ya publicados, no para vigilar en
  tiempo real.
- Los errores son inyecciones artificiales; no estiman qué errores existen realmente en las fuentes.

#### 18. Hito 4.4: regla de alerta sistémica

##### La pregunta

Cuando **muchas series cambian el mismo mes**, lo más probable es que haya cambiado algo general (una resolución, una nueva
publicación de tarifas) y no que haya miles de errores de captura simultáneos. La regla del plan dice: *“si más de X % de las
series alertan en el mismo mes, se clasifica como cambio regulatorio y no como error de dato”*. Hay que definir X, calibrarlo
con febrero de 2020 (51 de 83 series), julio de 2020 (24) y julio de 2021 (18), y contrastarlo con la CREG y con EPM.

##### Palabras que conviene entender

- **Fracción mensual:** series con alerta / series evaluadas ese mes.
- **Candidato sistémico:** mes cuya fracción supera X (desigualdad estricta) y en el que se evaluaron al menos 10 series. Se
  llama *candidato* porque confirmarlo exige comparar con la publicación real. **Las alertas no se borran**: pasan a una cola
  de revisión.
- **Ventana móvil:** para evaluar el mes *m* se usan los 24 o 36 cambios anteriores, nunca los posteriores. Así se puede
  evaluar cualquier mes sin “mirar el futuro”.
- **Componente:** cada pieza del costo unitario de EPM (compra de energía, transporte STN, distribución SDL, comercialización,
  pérdidas, restricciones). Las series de EPM están repetidas por columna y por nivel de tensión, así que un solo componente
  puede mover varias series a la vez.
- **Amplitud:** cuántos componentes distintos alertan un mes. Distingue un cambio general (muchos componentes) de uno que
  afecta a una pieza.
- **Etiquetas canónicas:** EPM escribe de varias formas la misma etiqueta según el mes (por ejemplo, “Costo compra: Gm, i” y
  “Costo Compra: Gm, i”). Las equivalencias aprobadas internamente en el Hito 2 las reúnen en una sola.
- **Banda factible:** el rango de X que captura los tres meses del plan sin marcar ningún otro. Si no existe, X no se puede
  fijar con esos tres meses.
- **Enmascaramiento:** errores reales que la regla escondería al reclasificarlos como “sistémicos”.

##### Cómo se hizo, paso a paso

1. **Se reprodujeron las cifras del plan** desde los archivos del Hito 2: 51/83 (61,4 %), 24/83 (28,9 %) y 18/83 (21,7 %).
2. **Se aplicó el protocolo del proyecto** (cambios logarítmicos, ventana móvil de 24 y 36, métodos I-MR y MAD 3σ), porque las
   cifras del Hito 2 vienen de otro protocolo (límites fijos y diferencias absolutas).
3. **Se probaron nueve variantes** de EPM (etiquetas canónicas y originales, dos ventanas, dos métodos, más la reproducción del
   Hito 2). Para cada una se midió la banda factible y qué pasa con cada X entre 5 % y 80 %.
4. **Se midió el costo**: qué fracción de las alertas reales se reclasifica y qué fracción de los errores inyectados (tomados
   de 4.2) quedaría escondida.
5. **Se generó el catálogo** de meses candidatos para EPM, CHEC y SSPD (227 filas), con su fracción y su amplitud.
6. **Se contrastó con fuentes externas**: se leyeron los seis PDF oficiales de tarifas de EPM (enero, febrero, junio y julio
   de 2020; junio y julio de 2021); se verificó que coinciden con el CSV en las 108 celdas comparadas y que la suma de
   componentes reproduce el costo unitario publicado; y se leyeron las resoluciones CREG 012, 058 y 104 de 2020 (la 015 de
   2018, de forma parcial).

##### Por qué se hizo así

- **Reproducir primero** las cifras del plan evita discutir un número que no se pudo rehacer.
- **Varias variantes** porque con solo tres meses un resultado puede deberse al protocolo y no al fenómeno.
- **Etiquetas canónicas como variante principal** porque sin ellas la misma serie se parte y los denominadores mensuales cambian.
- **Reportar el costo de enmascarar** porque una regla que reclasifica demasiado esconde errores reales.
- **Evidencia externa guardada** (PDF con su huella digital) para que el contraste se pueda auditar.

##### Resultados

| Pregunta | Respuesta |
|---|---|
| ¿Se reproducen 51/24/18? | Sí, exactamente, desde los archivos del Hito 2 |
| ¿Se mantienen con el protocolo logarítmico? | **Solo febrero de 2020** (49 % a 67 % de las series en todas las variantes). Julio de 2020 (6 % a 44 %) y julio de 2021 (0 % a 16 %) dependen de la ventana, el método y las etiquetas |
| ¿Existe un X que capture los tres meses sin marcar otros? | **No, en ninguna variante.** Con las cifras del Hito 2, abril de 2020 (24,1 %) supera a julio de 2021 (21,7 %) |
| ¿Los tres meses son del mismo tipo? | No: involucran 11, 5 y 3 componentes tarifarios |
| ¿Qué X se propone? | **25 %, como valor de trabajo, sin aprobar** |
| ¿Cuánto cuesta X = 25 %? | Esconde como máximo 8,2 % de los errores individuales inyectados (con X = 10 % llega a 26,2 %), pero esconde 80 % a 100 % de los errores colectivos |
| ¿Funciona en otras fuentes? | En CHEC, 270 de 270 series alertan en febrero de 2020; en SSPD la fracción mensual máxima es 14,4 % y con X = 25 % la regla no se activa |
| ¿Qué muestran las publicaciones de EPM? | Los tres meses son **cambios publicados, no errores de captura**: febrero es amplio (11 componentes); julio de 2020 y julio de 2021 involucran pocos componentes |

**Por qué 25 %:** en las variantes con etiquetas canónicas solo marca meses del plan; un solo componente aunque alertara con
todas sus series aportaría como máximo 13 % de la fracción, y 25 % lo supera; y su costo para errores individuales es bajo. Es un
valor de arranque, no una calibración cerrada.

##### Qué mostraron las publicaciones de EPM

Variación publicada de cada componente (nivel de tensión I) frente a las alertas:

| Componente | Ene → feb 2020 | Jun → jul 2020 | Jun → jul 2021 |
|---|---|---|---|
| Costo G,T y pérdidas | **+25,8 %** (alerta en todas las series) | 0,0 % | −4,2 % |
| Distribución (SDL) | +7,8 % (alerta en parte de las series) | +5,2 % (alerta con I-MR) | −2,1 % (alerta solo en el Hito 2) |
| Compra de energía | +8,4 % (no alerta) | +0,4 % | −3,0 % |
| Transporte STN | +5,3 % (no alerta) | **−20,3 %** (alerta con MAD) | **−13,3 %** (alerta con I-MR, las 15 series) |
| Comercialización | +0,9 % | +7,2 % (alerta con MAD) | +3,0 % |
| Restricciones | cruza cero (−0,25 → 2,03) | +40,9 % (no alerta) | **+147,0 %** (11,50 → 28,40; alerta solo en el Hito 2) |

Lectura prudente:

- Las alertas caen en componentes que **sí cambiaron según la publicación oficial**, y como los valores del CSV coinciden con
  esa publicación, **no son errores de captura**. Son cambios publicados. Esa es justo la distinción que la regla busca.
- **Qué componente alerta en julio de 2020 depende del método**: con I-MR solo la distribución, con MAD el transporte STN y la
  comercialización, en el Hito 2 los tres.
- **Julio de 2021 es un cambio de un solo componente, no de todo el mercado.** El transporte STN baja 13,3 % y son justo sus 15 series
  las que alertan con I-MR. Con X = 25 % ese mes no es “sistémico”, lo cual es coherente: un solo componente no debe reclasificarse
  como cambio de mercado, aunque sí es un cambio publicado y no un error.
- **La hipótesis del Hito 2 solo se respalda en parte.** La revisión atribuía febrero de 2020 “probablemente” a los cargos de
  distribución de la CREG 015 de 2018. La distribución sube 7,8 %, pero el costo de pérdidas sube 25,8 % y el de compra 8,4 %: el
  cambio no se limita a la distribución.
- La **Resolución CREG 012 de 2020** (opción tarifaria; expedida el 6 de febrero y publicada el 17 de febrero de 2020) cita la
  015 de 2018 como motivo, pero no fija un mes de aplicación para EPM. Los encabezados de las publicaciones de junio y julio de
  2020 sí la citan y traen una fila nueva “CU CREG 012 de 2020”; los de enero y febrero no. Es coherente con que la opción
  tarifaria sostuviera la tarifa aplicada, pero **no se probó el mecanismo**.
- La **Resolución CREG 058 de 2020** (14 de abril; Diario Oficial del 15 de abril de 2020) fija pagos diferidos de las facturas de
  abril a junio por la emergencia sanitaria, permite cobrar menos que el máximo aprobado en transmisión, distribución y
  comercialización, y remite a la opción tarifaria. La **104 de 2020** (5 de junio) impide que el consumo de subsistencia de los
  estratos 1 y 2 varíe con el IPC durante la emergencia. Ninguna fija los valores de los componentes de EPM: **explican el contexto,
  no los cambios observados**. De la **015 de 2018** solo se verificó de forma literal que se publicó el 3 de febrero de 2018 y su
  objeto; sus reglas de aplicación de los cargos no se pudieron citar como texto.

##### Límites que hay que decir en voz alta

- **“Candidato sistémico” no es “cambio regulatorio confirmado”.** El contraste con las publicaciones respalda que febrero y julio
  de 2020 y julio de 2021 son cambios publicados; falta confirmar con EPM o la CREG la causa de cada uno.
- **Tres meses no bastan para calibrar X.** Es una decisión que debe aprobar el director, con este análisis como insumo.
- Las series **no son independientes**; una fracción alta puede ser un solo componente. Por eso se reporta la amplitud.
- El costo de enmascaramiento sale de inyecciones artificiales de 4.2, no se recalculó con la ventana móvil.
- Las equivalencias de etiquetas son una aprobación interna del equipo, no una confirmación de EPM.

#### 19. Hito 4.5: scorecard por dimensión

El scorecard es una tabla de resumen. No vuelve a medir los datos; organiza los resultados de la
matriz OE1 para que sea posible leerlos por fuente y dimensión.

El archivo `4.5/scorecard_oe1_provisional.csv` tiene 32 filas: cuatro fuentes por ocho
dimensiones. Cada fila indica cuántos controles hay, cuántos fueron medidos, cuántos son
provisionales, cuántos no se pudieron medir y cuántos no aplican.

Por ejemplo, una fila de EPM para completitud no significa que “EPM tenga 90 % de calidad”. Significa
que resume los controles de completitud definidos para EPM y conserva sus estados y limitaciones.
El scorecard seguirá llamándose provisional hasta que se aprueben umbrales, catálogos y evidencia
externa.

Para regenerarlo:

```bash
python3 desarrollo_puntos/4.5/generar_scorecard_oe1.py
```

#### 20. Hito 4.6: niveles y costo computacional

Este punto responde dos preguntas:

1. ¿Las alertas se comportan distinto en los diferentes niveles tarifarios?
2. ¿Cuánto tiempo tarda cada etapa del análisis?

Se generaron dos archivos en `4.6/`:

- `resultados_por_nivel.csv`: observaciones, series, detecciones y tasa de alerta por método y nivel.
- `costos_computacionales.csv`: tiempos registrados por fuente, escenario y etapa.

EPM se separa por niveles I, II y III en el panel común utilizado. CHEC se separa por sus códigos
de nivel 1 a 4. SSPD y XM se reportan como `No_aplica`, porque el esquema utilizado no tiene un
nivel comparable. Esto es una decisión de honestidad: no se inventa una equivalencia entre
estrato, categoría comercial o grupo operativo y nivel tarifario.

Los tiempos se toman de las ejecuciones de 4.2 y 4.3. Permiten comparar el costo relativo entre
fuentes y etapas, pero no garantizan el mismo tiempo en otro computador.

Para reproducirlo:

```bash
python3 desarrollo_puntos/4.6/analizar_niveles_costos.py
```

#### 21. ¿Están completos 4.3 y 4.4?

**Sí en lo que se puede hacer con los datos y archivos disponibles; no en su totalidad.** Quedan pendientes que dependen de
decisiones, de documentos que no se localizaron o de etapas posteriores del plan.

##### 4.3

| Elemento del plan | Estado |
|---|---|
| Precisión, recall y F1 a tasa de alerta igualada | **Hecho** (tres fuentes interpretables; XM solo descriptivo) |
| Curvas de detección contra tasa de alerta por método | **Hecho** |
| Pruebas por tipo con su denominador | **Hecho** |
| Meses distintos sorteados, sin reemplazo | **Hecho** |
| Tabla comparativa con IC 95 % por técnica y tipo de error | **Hecho** (XM sin IC: una sola categoría) |
| LOF o KNN (pendiente de 4.1) | **Hecho**; LOF degenerado en CHEC (y en EPM con etiquetas canónicas) |
| Sensibilidad a las etiquetas de EPM | **Hecho**: las conclusiones no cambian |
| Extended Isolation Forest (pendiente de 4.1) | **No hecho** (el plan lo condiciona al tiempo) |
| Validación de las alertas reales con una fuente externa | **No hecho** (corresponde al Hito 6) |
| Aprobación de umbrales y de la prevalencia | **No hecho** (depende del director) |

##### 4.4

| Elemento del plan | Estado |
|---|---|
| Formalizar e implementar la regla | **Hecho** |
| Calibrar X con feb-2020, jul-2020 y jul-2021 | **Hecho como análisis, sin valor único**: no hay banda factible; se propone 25 % sin aprobar |
| Catálogo de alertas sistémicas | **Hecho** (227 filas) |
| Contrastar con publicaciones tarifarias de EPM | **Hecho**: enero, febrero, junio y julio de 2020 y junio y julio de 2021 (seis PDF) |
| Contrastar con resoluciones de la CREG | **Parcial**: leídas la 012, 058 y 104 de 2020; la 015 de 2018 solo en parte; la 152 de 2020 y la 003 de 2021 (citadas en los encabezados de 2021) no se consultaron |
| Consulta formal a EPM o a la CREG | **No hecho** (el plan la ubica en el Hito 6) |

#### 22. Hallazgos que afectan al trabajo anterior

1. **Las etiquetas de EPM fragmentan las series.** Sin normalizarlas hay 266 series; con las equivalencias del Hito 2, 200.
   En el panel común de 4.3 pasan de 27 a 69 series. 4.1 y 4.2 usaron las etiquetas originales y no se modificaron; 4.3 se
   repitió como sensibilidad y sus conclusiones no cambian. Falta decidir si se repiten 4.1 y 4.2.
2. **Febrero de 2020 también aparece en CHEC** (270 de 270 series). Es evidencia de que el fenómeno no es exclusivo de EPM.
3. **La hipótesis de la CREG 015 de 2018 se respalda solo en parte** (sección 18).
4. **Las cartas I-MR de ventana móvil pierden sensibilidad después de un salto grande**, porque la referencia posterior
   incluye ese salto. Puede explicar por qué I-MR no señala julio de 2020 mientras MAD, más robusto, sí. Es una hipótesis que
   no se probó.
5. **Un valor repetido no lo detecta ninguna carta.** Refuerza la idea de combinar reglas y cartas.

#### 23. Cómo reproducir y verificar el Hito 4

Desde la raíz del proyecto:

```powershell
### 4.5
python desarrollo_puntos/4.5/generar_scorecard_oe1.py

### 4.6
python desarrollo_puntos/4.6/analizar_niveles_costos.py

### 4.3
python desarrollo_puntos/4.3/experimento_tasa_igualada.py
python desarrollo_puntos/4.3/informe_metricas.py
python -m unittest discover -s desarrollo_puntos/4.3 -p test_metricas.py -v
python desarrollo_puntos/4.3/verificar_resultados.py

### 4.4
python desarrollo_puntos/4.4/calibrar_regla_sistemica.py
python desarrollo_puntos/4.4/informe_regla_sistemica.py
python -m unittest discover -s desarrollo_puntos/4.4 -p test_regla_sistemica.py -v
python desarrollo_puntos/4.4/verificar_resultados.py
```

Qué comprueban las verificaciones:

- que los datos de entrada y los PDF conservan su huella digital (SHA-256);
- que las cifras de las tablas se recalculan por otra vía (4.3 desde los puntajes guardados; 4.4 con una implementación distinta
  de la usada para generarlas);
- que las banderas de 4.3 coinciden con las de 4.2 caso por caso;
- que las cifras 51, 24 y 18 del plan se reproducen;
- que la transcripción de los PDF coincide con el CSV y con la suma de componentes;
- pruebas automáticas: 12 en 4.3 y 10 en 4.4 (entre otras, que el futuro no influye en las señales pasadas y que el sorteo
  nunca repite un mes dentro de una serie).

Ejecutar dos veces da las mismas cifras; solo cambian los tiempos de cómputo guardados.

#### 24. Qué todavía no está aprobado o resuelto en el Hito 4

1. **Valor de X** de la regla sistémica (se propone 25 %, sin aprobar).
2. **Prevalencia de errores** a usar para presentar la precisión.
3. **Repetir 4.1 y 4.2 con etiquetas canónicas** de EPM (4.3 ya se repitió) y decidir si esas equivalencias se aceptan como oficiales.
4. **Contraste documental restante**: leer completa la CREG 015 de 2018 y las resoluciones particulares de EPM, y las CREG 152 de 2020 y 003 de 2021.
5. **Consulta formal a EPM o a la CREG** sobre los cambios detectados (Hito 6).
6. **Extended Isolation Forest**, que el plan dejaba condicionado al tiempo disponible.
7. **Tratamiento de MAD igual a cero**, que sigue con la regla conservadora de 4.1.
8. **Decidir qué hacer con LOF** (CHEC y EPM con etiquetas canónicas): quitar duplicados o aumentar vecinos cambia el significado de la densidad.
9. **Scorecard 4.5:** está generado, pero permanece provisional hasta aprobar umbrales y evidencia externa.
10. **4.6:** la separación por nivel solo es interpretable para EPM y CHEC; SSPD y XM quedan como `No_aplica` por diseño.

No se deben presentar como aprobados ni los umbrales ni los resultados de estos puntos hasta que el director los confirme.

#### 25. Idea principal para recordar

El proyecto no consiste en producir un único porcentaje de “calidad”. Consiste en construir una
evaluación explicable y reproducible: cada resultado debe indicar qué se midió, con qué datos, con
qué fórmula, bajo qué supuestos, con qué evidencia y con qué limitaciones.

El Hito 4 añade dos reglas de honestidad: **una señal estadística no es un error de dato**, y **un mes con muchas alertas no es un
cambio regulatorio hasta compararlo con la publicación real**. Por eso el proyecto reporta alertas “sin error conocido”,
prevalencias supuestas, intervalos por categorías y el estado de cada pieza de evidencia (leída, no verificada, no localizada).

#### 26. Revisión de integridad de los Hitos 3 y 4

La revisión más reciente está en [REVISION_HITOS_3_4.md](REFERENCIA_TECNICA.md#doc-e95ee88a713e).
Comprueba que la estructura sigue las actividades 3.1–3.7 y 4.1–4.6, que los entregables tienen índice y que la
documentación no presenta como definitivos los resultados provisionales.

Hay dos ideas prácticas importantes:

1. Las decisiones que requieren director o equipo están reunidas únicamente en
   [PENDIENTES_APROBACION_HITO3.md](REFERENCIA_TECNICA.md#doc-349c3e6eb49a),
   incluido el texto que falta incorporar en el documento oficial de tesis.
2. Las figuras de 4.2, 4.3 y 4.4 se generan desde los CSV y scripts, pero no se almacenan en Git. La revisión ejecutó y
   validó 4.2 (9 pruebas), 4.3 (12) y 4.4 (10) con sus librerías científicas; para abrir las figuras en otro equipo hay que
   volver a ejecutar los scripts. Esta es una limitación técnica de reproducibilidad del entorno, no una decisión
   metodológica pendiente del director. Los entornos para reproducirlos están formalizados en
   [requirements/README.md](REFERENCIA_TECNICA.md#doc-e050028ca414); un contenedor o `pyproject.toml` puede añadirse en el Hito 5.
