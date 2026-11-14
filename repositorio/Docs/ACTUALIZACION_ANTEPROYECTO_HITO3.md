# Actualización del anteproyecto · Hito 3

Texto de integración preparado dentro del repositorio. No sustituye ni acredita
la edición/aprobación del documento oficial de tesis, que no está incluido aquí.
Las decisiones operativas siguientes se implementan en `Code/hito3/`; su ejecución
no equivale a aceptación del director ni a validación del publicador.

## OE2 reformulado y decisión sobre CREG

Caracterizar fuentes abiertas de registros del sector eléctrico colombiano,
identificar sus consumidores, variables críticas y reglas de negocio, y delimitar
la CREG como referencia regulatoria cuando no se haya identificado un conjunto
eléctrico publicado por ella que satisfaga el protocolo temporal.

Se conservan EPM (`sfcd-b3ey`) y CHEC (`c698-wqig`) para tarifas/componentes;
Superservicios ZNI (`ebby-cjha`) para consumo y facturación; y XM/SIMEM (`c1b851`)
para demanda. XM es el publicador de su conjunto: no se atribuye a CREG. La búsqueda
CREG conservada en REFERENCIA_TECNICA.md y en perfiles de selección examinó anexos
eléctricos sin verificar una historia mensual apta, y descartó una fuente de gas
por el alcance eléctrico. No demuestra que ninguna otra fuente pueda existir.

Se incorpora además `vfjy-6fka`, fuente literal del plan, como réplica transversal
de ocho períodos. La API la identifica como **Subsidios, Contribuciones y FOES
Energia**, con 5.396 filas y 16 columnas. No contiene Rango de Consumo; no se le
atribuyen las 2.143 ausencias mencionadas en el plan. El reemplazo por ZNI queda
así distinguido de la comprobación literal del conjunto original.

## 3.1.5 · Control estadístico y calidad de datos

El control estadístico de procesos permite investigar cambios del comportamiento
de una serie y estimar parámetros de referencia antes del monitoreo. Jones-Farmer,
Woodall, Steiner y Champ (2014) revisan la fase I de análisis y la evaluación de
estabilidad para construir el esquema posterior de monitoreo. Aquí esa distinción
fundamenta la separación entre referencia y vigilancia; no constituye prueba de
que los registros administrativos cumplan los supuestos de independencia o estabilidad.

Se adopta DAMA-DMBOK2 (2017), capítulo 13, como marco de calidad y como ubicación
conceptual de la técnica de control estadístico, de acuerdo con el resumen
documental incorporado al proyecto. La matriz operacionaliza ocho dimensiones:
completitud, validez, unicidad, consistencia, integridad, exactitud, oportunidad y
razonabilidad. Los diez tipos de regla son una taxonomía distinta de las doce reglas
R01–R12 y siete controles complementarios. Las definiciones y metas concretas son
del proyecto, no obligaciones normativas atribuidas a DAMA.

ISO/IEC 25012 aporta una relación conceptual parcial; no se afirma equivalencia
entre sus características y las ocho dimensiones adoptadas, ni certificación de
cumplimiento de la norma. La presencia de un período no demuestra disponibilidad
oportuna, y una alerta estadística no prueba inexactitud. Exactitud requiere
contraste documental; oportunidad requiere disponibilidad verificable y plazo esperado.

## 5.6.4 · Método estadístico clásico: cartas I-MR en cambios logarítmicos

Las cartas I-MR sustituyen el Z-score como método estadístico clásico de este
apartado. El Z-score robusto se conserva como comparador del Hito 4, no como una
denominación alternativa de la carta. Para cada categoría homogénea y medida
positiva se define `d_t = ln(x_t) - ln(x_(t-1))`, únicamente entre meses consecutivos.
El rango móvil es `MR_t = abs(d_t - d_(t-1))`, entre cambios consecutivos válidos.

Los primeros 36 cambios **de calendario** de la racha mensual más larga fijan la
referencia; en empate se usa la racha más antigua. Los doce siguientes fijan la
vigilancia. La elegibilidad requiere al menos 49 meses consecutivos observados.
Las exclusiones no desplazan la frontera temporal: se informa cuántas de las 36
posiciones permanecen válidas y cuántos rangos móviles se utilizan. Se requiere
al menos dos cambios válidos y un rango móvil de referencia; las referencias
pequeñas deben interpretarse con cautela, sin afirmar una fase I estable por construcción.

En referencia se calculan la media de los cambios y MR media. La carta I usa
límites `media(d) ± 2,66 * MR_media`; la carta MR usa límite inferior cero y superior
`3,267 * MR_media`. La señal es la unión de I o MR en vigilancia, sin modificar los
límites con esa vigilancia. MR igual a cero se identifica expresamente; un cambio
que abandona el nivel constante genera señal, sin fabricar una escala positiva.
Una señal se registra como pendiente de revisión, nunca como error confirmado.

La cuarentena se aplica por **celda**, conservando la fila y los valores originales.
Se excluyen ambos cambios que tocan una celda apartada y cualquier MR o rasgo que
dependa de esos cambios; no se interpola. Cuando R08 solo identifica una relación
de orden rota se apartan las tres propiedades de esa fila por ambigüedad, sin
afectar punta/fuera de punta. Duplicados idénticos aportan un único valor al mes;
duplicados conflictivos no se promedian y quedan excluidos con motivo explícito.

R12 genera Advertencia hasta confirmación. Usa el factor de trabajo 10 sobre la
mediana absoluta de niveles de referencia, no sobre la serie completa. El factor
sigue sujeto a la sensibilidad y validación de negocio del Hito 4.

Isolation Forest emplea cambio logarítmico actual, cambio previo, diferencia
absoluta entre ambos y logaritmo del nivel relativo a la mediana de referencia.
Los parámetros de escala, entrenamiento y percentil 99,5 se estiman exclusivamente
en referencia. Se entrena por fuente y fecha de corte para no incorporar meses
posteriores a la primera vigilancia del modelo. El primer rezago vale cero; después
de un hueco se excluye la observación cuyo rasgo previo no esté disponible.

El bootstrap usa categorías completas de negocio como conglomerados. Todas sus
medidas se conservan juntas y se remuestrean numeradores y denominadores
simultáneamente, con 2.000 réplicas y semilla 20261105. No se presentan propiedades
EPM como réplicas independientes. Los conglomerados elegibles y sus tamaños se
enumeran en el inventario; la muestra filtrada no tiene que conservar los 28
grupos del Hito 2. Con una categoría no se publica IC inferencial.

## 5.8 · Población, fuentes y trazabilidad

El estudio es retrospectivo sobre versiones congeladas de las fuentes. La población
operativa, el número de registros, períodos y series elegibles se reportan por fuente
en FICHAS_FUENTES_HITO3.md y los perfiles JSON; no se extrapolan los 83 casos
históricos a poblaciones con otras reglas de continuidad y exclusión.

Se ejecuta el mismo pipeline sin edición manual sobre los snapshots versionados.
La réplica `vfjy-6fka` se limita a reglas transversales y perfilamiento; ocho
períodos no satisfacen la referencia/vigilancia y no se fabrican meses intermedios.
Las reglas de propiedad, nivel de tensión y franjas EPM no se trasladan a sus
registros contables. La matriz complementaria registra no aplica y no medible
con motivos distintos.

Las descargas Socrata conservan `:id`, páginas originales, metadatos, UTC y SHA-256,
sin sobrescribir capturas. Se comparan multiconjuntos de filas para conservar la
multiplicidad de duplicados y tolerar cambios de orden. Hallazgos y alertas incluyen
identidad de contenido y/o clave de negocio de categoría, período y medida.
Las dos capturas reales conservadas de EPM/CHEC/vfjy-6fka permiten verificar la
igualdad de registros, hallazgos y cartas en esos cortes. No garantizan estabilidad
futura ni permiten retrotraer la fecha de captura a la fecha de publicación.

## Limitaciones y aceptación

La documentación de fórmulas y el funcionamiento del pipeline no cierran por sí
solos las ocho dimensiones. OPO01 queda no medible sin evidencia temporal y plazo;
EXA01 tiene cobertura parcial; los catálogos externos, responsables nominales y
umbrales deben ser confirmados. Los experimentos históricos del Hito 4 deben
reevaluarse antes de atribuirles resultados del protocolo corregido.

La integración de este texto en el anteproyecto oficial y la aceptación del
director deben registrarse explícitamente. No se inventan aprobación ni respuesta
de EPM/CREG. La validación externa formal y el contraste de H1 corresponden al Hito 6.

## Referencias

- Jones-Farmer, L. A., Woodall, W. H., Steiner, S. H. y Champ, C. W. (2014).
  *An Overview of Phase I Analysis for Process Improvement and Monitoring*.
  Journal of Quality Technology, 46(3), 265–280.
  [DOI y ficha editorial](https://doi.org/10.1080/00224065.2014.11917969).
- DAMA International (2017). *DAMA-DMBOK: Data Management Body of Knowledge*,
  segunda edición, capítulo 13. Aplicación y límites según el resumen conservado
  en REFERENCIA_TECNICA.md; no se atribuyen umbrales propios del proyecto a la obra.
- NIST/SEMATECH. [Individuals Control Charts](https://www.itl.nist.gov/div898/handbook/pmc/section3/pmc322.htm).
  Fórmulas I-MR; las constantes redondeadas 2,66 y 3,267 siguen el plan del proyecto.
- ISO/IEC 25012:2008. [Ficha de la norma](https://www.iso.org/standard/35736.html).
  Relación conceptual delimitada; no se declara certificación ni equivalencia literal.
