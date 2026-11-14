# Registro de decisiones — Hitos 3 y 4

## Actualización operativa del Hito 4 · protocolo v2

Prevalecen [VERIFICACION_HITO4.md](VERIFICACION_HITO4.md) y
[RESULTADOS_HITO4.md](RESULTADOS_HITO4.md) para la comparación vigente. La
calibración de las seis técnicas se hace por folds temporales dentro de referencia,
sin utilizar vigilancia para ajustar umbrales. Se adopta como política técnica
la deduplicación exacta de rasgos de entrenamiento, igual para IF/LOF/KNN; si
LOF no es interpretable, el banco no entra al panel común.

El scorecard distingue umbral propuesto, resultado observado y decisión pendiente.
Las figuras están incluidas. Se verifican los apartados pertinentes de CREG
015/2018, 078/2019, 156/2019, 012/2020, 152/2020 y 003/2021, sin afirmar que
expliquen por sí solos cada cambio. Faltan notificación/firmeza y conciliación
LAC o respuesta del publicador para confirmar la causa concreta de los meses EPM.

Estas decisiones de implementación no son aprobación académica. Continúan
pendientes umbrales de calidad, responsables, política operativa de X/método
principal, evidencia de dimensiones y validación externa/precisión empírica.

## Actualización operativa del Hito 3 · 13 de noviembre de 2026

Las dos descargas reales de EPM, CHEC y vfjy-6fka, la corrección de I-MR,
la cuarentena por celda, el bootstrap por categorías completas y R12 como
Advertencia están implementados. Véase [VERIFICACION_HITO3.md](VERIFICACION_HITO3.md).
No se somete a aprobación el algoritmo anterior de remuestrear series dentro de
categorías: se corrigió para cumplir el plan. La población elegible y las
exclusiones quedan documentadas, sin forzar los conteos del Hito 2.

Siguen pendientes evidencia temporal de oportunidad, catálogos/semántica
autorizados, responsables nominales, aceptación de umbrales y la incorporación
del texto preparado al anteproyecto oficial. El registro siguiente conserva la
discusión histórica; sus propuestas no equivalen a aprobación.

**Consolidación: 9 de noviembre de 2026.** Estado y plan general en [PROYECTO.md](PROYECTO.md).
Se preservan las propuestas para revisión del profesor; ninguna se declara aprobada.

Este es el documento único para registrar las decisiones metodológicas y de negocio que todavía requieren aprobación del director o del equipo. Incluye las decisiones heredadas del Hito 3 y las nuevas decisiones del Hito 4. En cada apartado se explica qué se debe decidir y por qué es necesario hacerlo. Los scripts y resultados ya ejecutados no deben modificarse hasta cerrar estas decisiones.

## Estado general

La matriz OE1, las fichas, las cartas, la trazabilidad, la cuarentena, el bootstrap, las técnicas comparadas, el análisis de sensibilidad, el scorecard provisional y el análisis de niveles/costos ya están implementados. Permanecen pendientes las decisiones que afectan interpretación, umbrales, catálogos, evidencia externa y selección del método final.

## 1. Roles y gobernanza

**Propuesta de gobernanza del equipo:** tres integrantes comparten la ejecución técnica y el
profesor actúa como aprobador final. La distribución queda pendiente de confirmación nominal.

| Decisión requerida | Propuesta inicial | Por qué se necesita | Estado |
|---|---|---|---|
| Integrante 1 | Datos y reglas de negocio | Conserva datasets, hashes, diccionarios, etiquetas y reglas. | Propuesta; falta nombre |
| Integrante 2 | Métricas y anomalías | Ejecuta cartas, bootstrap, detectores, sensibilidad, métricas y scorecard. | Propuesta; falta nombre |
| Integrante 3 | Validación y documentación | Revisa alertas, organiza evidencias, mantiene bitácora y documenta limitaciones. | Propuesta; falta nombre |
| Profesor | Aprobador final | Confirma umbrales, métodos, alcance, interpretación y conclusiones. | Pendiente de confirmación |

### Propuesta de distribución para validar con el profesor

La tabla siguiente conserva el detalle histórico de responsabilidades para trazabilidad documental;
la distribución vigente del equipo es la de Integrante 1, Integrante 2, Integrante 3 y Profesor
definida arriba.

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

### Preguntas para el profesor

1. ¿Está de acuerdo con estos cinco roles y con la distribución propuesta?
2. ¿Una misma persona puede asumir simultáneamente los roles de responsable de datos, métricas,
   reglas de negocio o validación?
3. ¿Es necesario registrar nombres propios o es suficiente indicar el cargo o la responsabilidad?
4. ¿Confirma que el director será el aprobador final de umbrales, métodos, catálogos y alcance?

**Estado:** propuesta pendiente de revisión y aprobación. No se deben inventar nombres ni declarar
un experto externo hasta contar con una confirmación explícita.

## 2. Umbrales y severidad

| Grupo | Controles | Propuesta | Por qué se necesita | Estado |
|---|---|---|---|---|
| Integridad mínima | R01–R04, R07, INT01, INT02, MAP01 | Meta de 100 % | Estos controles representan condiciones básicas del archivo; una tolerancia podría ocultar filas imposibles de relacionar o interpretar. | Pendiente de aprobación |
| Completitud y consistencia | R05, R06, R08–R10, DEF01 | Meta de 100 %, reportada como tasa continua; advertencia cuando corresponda | El equipo debe decidir qué faltantes o variantes son aceptables para el uso energético previsto. | Pendiente de aprobación |
| Exactitud | EXA01 | 100 % en la muestra validada | Un porcentaje de coincidencia solo tiene sentido si se define la fuente de verdad, la muestra y la tolerancia de redondeo. | Pendiente de aprobar muestra y fuente |
| Oportunidad | OPO01 | Medir retraso publicación-descarga; usar proxy si no existe plazo publicado | Sin plazo esperado no se puede saber si una publicación fue tardía; el proxy debe reconocerse como indirecto. | Pendiente de aprobar plazo/proxy |
| Estadística | R11, R12, CART01 | Advertencia; no convertir señal automáticamente en error | Una señal identifica un comportamiento atípico, pero puede corresponder a un cambio real de tarifa o demanda. | Pendiente de calibración |

El 100 % es una meta del proyecto, no un umbral impuesto por DAMA-DMBOK ni ISO. Si el director aprueba tolerancias diferentes, deben registrarse junto con su justificación.

### Propuesta resumida para aprobar

| Tipo de control | Propuesta | Interpretación del resultado | Decisión solicitada |
|---|---|---|---|
| Integridad mínima | 100 % | Un incumplimiento se reporta como error porque impide interpretar o relacionar correctamente el dato | Confirmar si la meta debe ser estrictamente 100 % |
| Completitud y consistencia | Meta de 100 %, con tasa continua y advertencia | Un valor menor muestra una desviación que debe analizarse; no se elimina automáticamente el registro | Confirmar qué porcentaje o casos son aceptables como advertencia |
| Exactitud | 100 % de coincidencia en la muestra validada, con tolerancia de redondeo previamente definida | Solo se evalúan registros contrastados contra una fuente oficial aprobada | Aprobar muestra, fuente de verdad y tolerancia numérica |
| Oportunidad | Medir el retraso real cuando exista fecha y plazo; utilizar `provisional_proxy` cuando no exista plazo publicado | Un proxy no demuestra el plazo real, solo aproxima la disponibilidad | Aprobar el plazo esperado o aceptar explícitamente el proxy |
| Señales estadísticas | Advertencia, nunca error automático | Una alerta puede representar un cambio real de tarifa, demanda o regulación | Confirmar que toda alerta requiere revisión antes de clasificarse como error |

### Preguntas para el profesor sobre los umbrales

1. ¿Aprueba una meta del 100 % para integridad, completitud y consistencia, o propone tolerancias?
2. ¿Qué nivel de incumplimiento debe generar advertencia y cuál debe considerarse error?
3. ¿Aprueba la muestra de 30 registros por fuente para exactitud?
4. ¿Qué fuente oficial y qué tolerancia de redondeo deben utilizarse para validar importes?
5. ¿Acepta que la oportunidad se reporte como `provisional_proxy` cuando el portal no publique un plazo?
6. ¿Confirma que las alertas estadísticas no se convierten automáticamente en errores de calidad?

**Estado:** propuesta pendiente de revisión y aprobación. Los porcentajes calculados actualmente son
resultados de medición; no constituyen por sí mismos umbrales aprobados.

## 3. Catálogos y semántica de CHEC

Se debe aprobar el significado de categorías, niveles, unidades y conceptos tarifarios; el catálogo canónico y las equivalencias; la unidad de cada importe y el tratamiento de valores negativos; la clave candidata para identificar una tarifa por período; la aplicación definitiva de R08 y R09; y el responsable de mantener los catálogos.

**Por qué:** CHEC contiene códigos cuyo significado no está completamente explícito en el archivo. Si se interpretan sin catálogo, se podrían marcar como errores valores válidos o comparar conceptos que no tienen la misma unidad. La clave también debe aprobarse porque existen multiplicidades y no es seguro eliminar filas repetidas automáticamente.

**Estado:** análisis técnico en [DECISION_CATALOGOS_CHEC.md](REFERENCIA_TECNICA.md#doc-cd7e104c7bc9); aprobación documental pendiente.

### Propuesta de decisiones para CHEC

| Aspecto | Propuesta técnica | Por qué es necesario | Confirmación solicitada |
|---|---|---|---|
| Categorías y códigos | Mantener los valores originales y construir un catálogo canónico versionado | Evita modificar la fuente y permite distinguir variantes de escritura | Confirmar qué equivalencias representan el mismo concepto |
| Niveles tarifarios | Conservar los niveles 1–4 como categorías independientes | Agruparlos podría mezclar tarifas con comportamientos y unidades diferentes | Confirmar que los niveles 1–4 no deben combinarse |
| Unidades | Registrar explícitamente la unidad de cada componente e importe antes de comparar | Dos valores numéricamente similares pueden estar expresados en unidades distintas | Aprobar el catálogo de unidades y conversiones permitidas |
| Valores negativos | No marcar automáticamente valores negativos; revisar su significado por concepto, especialmente restricciones | Un valor negativo puede ser válido según el componente tarifario | Confirmar qué conceptos admiten valores negativos |
| Clave de tarifa | Usar una clave compuesta por período, categoría, nivel y concepto, sin eliminar duplicados automáticamente | Las multiplicidades pueden representar registros distintos o conflictos que requieren revisión | Aprobar la clave candidata y la política frente a duplicados |
| R08 y R09 | Aplicar las reglas solo cuando exista una matriz de aplicabilidad documentada | Sin conocer qué campos aplican a cada nivel, un supuesto puede generar falsos errores | Confirmar la matriz de aplicabilidad y la interpretación de ceros |
| Mantenimiento | Asignar un responsable para versionar el catálogo cuando cambie la fuente | Un catálogo sin control de versiones puede cambiar los resultados históricos | Confirmar responsable y frecuencia de actualización |

### Preguntas para el profesor sobre CHEC

1. ¿Aprueba construir un catálogo canónico sin alterar los valores originales?
2. ¿Confirma que los niveles 1–4 deben analizarse por separado?
3. ¿Quién puede validar el significado de los códigos, unidades y conceptos tarifarios?
4. ¿Qué conceptos pueden tener valores negativos válidos?
5. ¿Aprueba la clave compuesta propuesta y la decisión de no eliminar duplicados automáticamente?
6. ¿Confirma que R08 y R09 deben quedar como provisionales hasta aprobar la matriz de aplicabilidad?
7. ¿Quién será responsable de mantener y aprobar futuras versiones del catálogo?

**Estado:** propuesta técnica pendiente de validación semántica y aprobación documental. Hasta entonces,
las equivalencias y reglas CHEC deben presentarse como provisionales.

## 4. Evidencia de exactitud

Se propone contrastar 30 registros por fuente, estratificados por período y categoría, contra una fuente oficial independiente o una publicación oficial del mismo período. Debe aprobarse la fuente, el tamaño y método de selección, los campos comparados, la tolerancia numérica y el tratamiento de diferencias por redondeo o unidad.

**Por qué:** una carta de control o una regla de formato solo muestra coherencia interna. EXA01 necesita una fuente externa que permita afirmar si el valor publicado coincide con una referencia confiable. Sin aprobar la muestra y la tolerancia, el porcentaje de exactitud no sería reproducible.

**Estado:** procedimiento y plantilla en [EVIDENCIA_EXACTITUD_OPORTUNIDAD.md](REFERENCIA_TECNICA.md#doc-dfcefa4bff36); la muestra y la fuente no están aprobadas.

### Propuesta para evaluar exactitud

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

### Preguntas para el profesor sobre exactitud

1. ¿Aprueba utilizar 30 registros por fuente con selección estratificada?
2. ¿Qué fuente debe considerarse referencia oficial para cada dataset?
3. ¿Cuándo debe exigirse una fuente independiente y cuándo basta una publicación oficial del mismo proveedor?
4. ¿Aprueba la tolerancia inicial de 0,01 o establece otra según la unidad y precisión de cada fuente?
5. ¿Aprueba reportar EXA01 como concordancia de la muestra, sin generalizarlo a todo el dataset?
6. ¿Qué tratamiento debe darse a diferencias causadas por redondeo, unidad, transcripción o actualización?

**Estado:** procedimiento definido, pero fuente, muestra, tolerancia y alcance requieren aprobación.

## 5. Evidencia de oportunidad

Se propone registrar fecha de publicación o actualización, fecha de descarga, frecuencia esperada, retraso calculado y evidencia de la URL o metadato. Si el publicador no declara un plazo esperado, debe aprobarse el uso de un proxy y reportarse como `provisional_proxy`.

**Por qué:** la fecha de descarga no indica cuándo el dato estuvo disponible para los usuarios. Se necesita un plazo esperado para distinguir una publicación oportuna de una tardía. Si el portal no publica ese plazo, el director debe aceptar expresamente una medición indirecta.

**Estado:** procedimiento en [EVIDENCIA_EXACTITUD_OPORTUNIDAD.md](REFERENCIA_TECNICA.md#doc-dfcefa4bff36); pendiente de aprobar el plazo o proxy por fuente.

### Propuesta para evaluar oportunidad

| Elemento | Propuesta | Por qué es necesario | Confirmación solicitada |
|---|---|---|---|
| Fecha de publicación | Usar la fecha declarada por el portal o el publicador | El período del dato no equivale a la fecha en que se publicó | Confirmar qué metadato tiene prioridad |
| Fecha de descarga | Registrar fecha, hora y zona horaria de cada captura | Permite calcular el retraso observado y repetir la medición | Aprobar formato y zona horaria |
| Plazo esperado | Usar el plazo oficial del publicador o la obligación aplicable | Sin plazo no se puede clasificar puntualidad o retraso | Definir plazo por fuente |
| Proxy | Usar disponibilidad del período como `provisional_proxy` cuando no exista plazo | Es una aproximación y no una medición directa del retraso | Aceptar o rechazar el proxy por fuente |
| Evidencia | Conservar URL, metadatos, fecha de consulta y SHA-256 | Permite demostrar qué estaba disponible en la fecha observada | Aprobar elementos mínimos |
| Interpretación | Reportar “medible”, “provisional_proxy” o “no medible” | Evita presentar una aproximación como resultado definitivo | Confirmar las categorías de estado |

### Preguntas para el profesor sobre oportunidad

1. ¿Qué plazo esperado debe utilizarse para cada fuente?
2. ¿Qué fecha del portal debe considerarse fecha de publicación?
3. ¿Acepta el uso de `provisional_proxy` cuando no exista un plazo publicado?
4. ¿Aprueba registrar fecha, hora, zona horaria, URL y SHA-256 como evidencia mínima?
5. ¿Confirma que la ausencia de evidencia debe clasificarse como “no medible” y no como retraso?

**Estado:** propuesta pendiente de aprobación del plazo, proxy y categorías de resultado.

## 6. Reproducibilidad y versiones

El criterio de cierre solicita dos descargas. Debe aprobarse obtener una segunda descarga real del portal o usar una segunda copia congelada con fecha y SHA-256 diferentes, declarando que demuestra reproducibilidad técnica pero no estabilidad temporal del portal. También debe aprobarse la política de codificación y fin de línea de los CSV.

**Por qué:** una sola descarga demuestra que el código funciona sobre un archivo, pero no que los resultados se mantienen entre versiones. La segunda versión permite identificar cambios del portal y la política de codificación evita que el mismo archivo produzca hashes diferentes por razones técnicas.

**Estado:** procedimiento en [REPRODUCIBILIDAD_HITO3.md](REFERENCIA_TECNICA.md#doc-cff2689f65ac); segunda versión y política de fin de línea pendientes.

### Propuesta para reproducibilidad

| Elemento | Propuesta | Por qué es necesario | Confirmación solicitada |
|---|---|---|---|
| Segunda versión | Obtener una segunda descarga real o conservar una segunda copia congelada | Permite comparar versiones y detectar cambios del portal | Aprobar cuál de las dos alternativas se usará |
| Identificación | Registrar fecha de captura, URL, tamaño y SHA-256 | Permite distinguir inequívocamente ambas versiones | Confirmar metadatos obligatorios |
| Codificación | Normalizar lectura a UTF-8 y conservar el archivo original | Evita errores por acentos y separadores sin alterar la evidencia | Aprobar política de codificación |
| Fin de línea | Registrar si el archivo usa LF o CRLF y no cambiarlo silenciosamente | El contenido puede ser igual aunque el hash cambie por formato | Aprobar si se compara el archivo crudo o una representación normalizada |
| Comparación | Reejecutar los mismos controles sobre ambas versiones | Permite distinguir cambios del dato de cambios del código | Confirmar controles mínimos a repetir |
| Conclusión | Declarar “reproducibilidad técnica” sin afirmar estabilidad del portal | Dos copias no demuestran que futuras descargas sean idénticas | Aprobar el alcance de la conclusión |

### Preguntas para el profesor sobre reproducibilidad

1. ¿Acepta una segunda copia congelada si no es posible obtener una segunda descarga del portal?
2. ¿Qué metadatos deben acompañar cada versión?
3. ¿Debe conservarse y compararse el archivo crudo o una versión normalizada?
4. ¿Qué controles deben repetirse obligatoriamente sobre la segunda versión?
5. ¿Aprueba declarar reproducibilidad técnica sin afirmar estabilidad temporal del portal?

**Estado:** procedimiento definido; segunda versión, codificación y alcance de la conclusión pendientes.

## 7. Decisiones estadísticas pendientes

- Confirmar que el bootstrap remuestrea series dentro de cada categoría y no filas individuales.
- Aceptar que XM y una categoría de SSPD tienen intervalos degenerados por contar con una sola serie.
- Confirmar que R12 y CART01 se interpretan como advertencias hasta contar con calibración de negocio o evidencia histórica suficiente.
- Confirmar si R10 seguirá medido por fila o se cambiará a celda por columna.

**Estado:** propuesta documentada; aprobación metodológica pendiente.

**Por qué:** estas decisiones cambian la interpretación de las cartas y del bootstrap. Definir la unidad de remuestreo, el tratamiento del MAD cero y la regla R12 evita que se comparen resultados generados con criterios diferentes.

### Propuesta estadística para aprobar

| Decisión | Propuesta | Por qué es necesario | Confirmación solicitada |
|---|---|---|---|
| Bootstrap | Remuestrear series dentro de cada fuente y categoría, no filas individuales | Las filas no son observaciones independientes y mezclar fuentes distorsiona el intervalo | Aprobar la serie como unidad de remuestreo |
| XM y categorías unitarias | Reportar intervalo degenerado y estado descriptivo/no interpretable | Una sola serie no permite estimar variabilidad entre series | Confirmar que no se inventarán intervalos |
| R12 y CART01 | Mantenerlos como advertencias hasta calibración o evidencia histórica | Una señal estadística no equivale automáticamente a un error | Confirmar que no generan error automático |
| R10 | Mantener medición por fila y documentar la limitación; evaluar celda/columna como sensibilidad | Cambiar el denominador modifica el resultado de completitud | Elegir unidad principal y sensibilidad |
| MAD cero | Mantener regla conservadora sin inventar escala | Una escala arbitraria puede crear señales artificiales | Confirmar señal, exclusión o alternativa |

### Preguntas para el profesor sobre decisiones estadísticas

1. ¿Aprueba remuestrear series dentro de cada categoría?
2. ¿Acepta reportar XM y categorías unitarias como no interpretables?
3. ¿Confirma que R12 y CART01 serán advertencias y no errores automáticos?
4. ¿Prefiere R10 por fila, por celda/columna o ambos como análisis principal y sensibilidad?
5. ¿Aprueba el tratamiento conservador del MAD igual a cero?

**Estado:** propuesta estadística pendiente de aprobación metodológica.

## 8. Decisiones adicionales del Hito 4

| Decisión requerida | Propuesta o estado actual | Por qué se necesita | Qué debe confirmar el director |
|---|---|---|---|
| Valor X de la regla sistémica | Se propone `25 %` como valor de trabajo; tres meses no permiten un valor único | X decide cuándo muchas alertas se consideran un fenómeno colectivo; cambiarlo puede reclasificar meses completos. | Aceptar 25 %, elegir otro valor o mantener la regla como exploratoria |
| Prevalencia para precisión y F1 | Se reportan escenarios de 1 %, 5 % y 10 %; no se elige uno como verdad | La precisión depende de cuántos errores se supone que existen; elegir una prevalencia sin justificación puede exagerar o minimizar el resultado. | Decidir si se presenta un escenario principal o todos como sensibilidad |
| Método principal | Se comparan IMR, Z robusto, Isolation Forest, LOF, KNN y R12 | La tesis debe explicar si propone un método principal o un conjunto de métodos complementarios. | Elegir método principal o declarar que el framework conserva varios métodos |
| Etiquetas canónicas de EPM | Se conservan las etiquetas actuales y `EPM_canonicas` como catálogo operativo | No existe una fuente externa disponible para validar las equivalencias; cambiar los valores originales afectaría la trazabilidad. | Aceptadas como decisión operativa del equipo; limitación documentada |
| MAD igual a cero | Se conserva una regla conservadora: no se inventa escala | Si todos los cambios de referencia son iguales, el MAD es cero y cualquier solución arbitraria alteraría las señales. | Confirmar este tratamiento o definir una alternativa |
| LOF en CHEC | Queda degenerado por duplicados exactos | LOF mide densidad; los duplicados pueden hacer que la densidad deje de representar rareza real. | Aprobar deduplicación, ajuste de vecinos o exclusión justificada |
| Extended Isolation Forest | No implementado; el plan lo dejaba condicionado al tiempo | Se debe evitar que la ausencia de una técnica se interprete como un incumplimiento oculto. | Confirmar que se excluye del alcance final |
| Scorecard 4.5 | El resumen vigente conserva 4 fuentes × 8 dimensiones y deja el promedio vacío | Se mezclaban tasas de cumplimiento e incumplimiento sin una normalización aprobada. | Definir si se agrega y aprobar dirección, ponderaciones, poblaciones y tratamiento de estados |
| Resultados 4.6 | Niveles explícitos para EPM/CHEC; SSPD y XM quedan `No_aplica` | Forzar una clasificación de nivel donde no existe produciría una comparación artificial. | Aceptar esta delimitación y evitar equivalencias no sustentadas |
| Evidencia regulatoria | Falta lectura completa de CREG 015/2018, 152/2020, 003/2021 y resoluciones particulares de EPM | Una alerta estadística no demuestra una causa regulatoria; se necesita respaldo documental para afirmarlo. | Confirmar alcance documental y si la consulta formal queda para Hito 6 |
| Incorporación en la tesis | El plan exige actualizar los apartados 3.1.5 y 5.6.4 del anteproyecto/metodología; el repositorio contiene la evidencia técnica, pero no el documento oficial editable de la tesis | La evidencia implementada debe reflejarse en el texto que se entregará y sustentará, sin afirmar como aprobado lo que sigue provisional. | Indicar el documento y responsable que integrará el texto, y aprobar su versión final |

Los resultados de 4.2–4.6 no deben presentarse como aprobación de un umbral, método o causa
regulatoria. Son evidencia para tomar estas decisiones.

### Preguntas integrales sobre el Hito 4

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

## Registro de aprobación

| Campo | Valor |
|---|---|
| Fecha | Pendiente |
| Director o aprobador | Pendiente |
| Participantes | Pendiente |
| Decisiones aceptadas | Pendiente |
| Cambios solicitados | Pendiente |
| Versión aprobada de la matriz | Pendiente |
| Observaciones | Pendiente |

## Texto para enviar al director

> Consolidamos en un único documento las decisiones pendientes de los Hitos 3 y 4: responsables, umbrales, catálogos CHEC, evidencia de exactitud y oportunidad, reproducibilidad, método principal, valor X, prevalencia, scorecard y alcance de niveles. Solicitamos confirmar o ajustar cada propuesta y registrar la versión aprobada de la matriz OE1 y del protocolo del Hito 4.

## 9. Artefacto del Hito 5: Streamlit

| Decisión | Propuesta | Motivo | Estado |
|---|---|---|---|
| Tecnología del tablero | Streamlit | Fue sugerida por el profesor y permite mantener la visualización junto al código y las salidas reproducibles. | Adoptada para la primera versión |
| Fuente de visualización | `repositorio/Data/gold/outputs/` | Evita recalcular o alterar los experimentos mientras se valida el artefacto. | Adoptada |
| Alcance inicial | Resumen, dimensiones DAMA-DMBOK, alertas sistémicas, métricas y trazabilidad | Cubre las salidas disponibles de los Hitos 3 y 4 sin inventar resultados nuevos. | Adoptado |
| Límites | No descarga, no modifica fuentes y no confirma por sí sola una alerta como error | Una señal estadística requiere revisión y evidencia antes de convertirse en incidente confirmado. | Adoptado |

La primera implementación está en `repositorio/app_streamlit.py` y su entorno en
`repositorio/Environment/requirements-streamlit.txt`. Quedan pendientes el empaquetado final,
Docker, la bitácora operativa de incidentes y la aprobación metodológica de umbrales y reglas.

## 10. Formalización del paquete Python

Se creó `Code/framework_calidad` como API reutilizable para carga, perfilamiento, evaluación de
reglas, detectores y reportes. Los scripts históricos permanecen intactos para conservar la
trazabilidad de los resultados de Hitos 3 y 4; la migración de cada experimento al paquete será
gradual y se aceptará únicamente si reproduce sus salidas.

La configuración utilizada para esta primera formalización es `Data/gold/outputs/calidad/matriz_oe1.yaml`.
Sus umbrales conservan el estado `propuesta_metodologica_no_aprobada` cuando corresponde; el
hecho de mover una regla a YAML no significa que el profesor ya la haya aprobado.

La revisión de cartas se generalizó con un control estructural para EPM, CHEC, SSPD y XM. El
análisis detallado de señales de EPM se conserva como complemento; no se extrapolan sus criterios
a las demás fuentes sin una validación específica.

## 11. Metadatos de ejecución

La CLI conserva el comando existente y ahora genera un manifiesto JSON por etapa en
`Data/gold/outputs/ejecuciones/`. Los manifiestos nuevos incluyen fecha UTC, etapa, versión del paquete,
semillas base fijadas por método, versión de Python y SHA-256 de las entradas. Los anteriores con
`semilla: 42` registraban la declaración de la interfaz, no necesariamente la semilla efectiva.
Esto permite saber con qué archivos se produjo una
salida sin alterar los datos originales.

### Agregación del scorecard pendiente de aprobación

El scorecard vigente conserva conteos por fuente, dimensión y estado, pero deja vacía la columna
`promedio_indicadores`. Algunas reglas miden incumplimientos y otras cumplimiento, por lo que un
promedio sin normalización ni definición de poblaciones no es interpretable como calidad. Se pide
al profesor aprobar, si se desea una puntuación agregada, la dirección de cada indicador, sus
ponderaciones, la población y el tratamiento de valores provisionales y no medibles. Hasta entonces
se muestran los indicadores individualmente y no se publica un porcentaje global de calidad.

## 12. Bitácora de incidentes

Se creó una bitácora inicial vacía con campos para fuente, período, regla, dimensión, descripción,
severidad, responsable, estado, evidencia, acción y fechas. Se evita precargar incidentes no
confirmados para no presentar alertas estadísticas como errores probados.
