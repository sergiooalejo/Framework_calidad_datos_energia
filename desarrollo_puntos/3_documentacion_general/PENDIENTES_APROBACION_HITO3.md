# Pendientes de aprobación — Hitos 3 y 4

Este es el documento único para registrar las decisiones metodológicas y de negocio que todavía requieren aprobación del director o del equipo. Incluye las decisiones heredadas del Hito 3 y las nuevas decisiones del Hito 4. En cada apartado se explica qué se debe decidir y por qué es necesario hacerlo. Los scripts y resultados ya ejecutados no deben modificarse hasta cerrar estas decisiones.

## Estado general

La matriz OE1, las fichas, las cartas, la trazabilidad, la cuarentena, el bootstrap, las técnicas comparadas, el análisis de sensibilidad, el scorecard provisional y el análisis de niveles/costos ya están implementados. Permanecen pendientes las decisiones que afectan interpretación, umbrales, catálogos, evidencia externa y selección del método final.

## 1. Roles y gobernanza

| Decisión requerida | Propuesta inicial | Por qué se necesita | Estado |
|---|---|---|---|
| Responsable de reglas de negocio | Persona que conoce tarifas, consumo y categorías | Las reglas dependen del significado del negocio; sin esta persona, un código podría interpretarse de forma incorrecta. | Pendiente de asignar nombre o cargo |
| Responsable de datos | Persona que descarga, versiona y conserva archivos | Alguien debe garantizar que se usa el archivo correcto y que los hashes y versiones se conservan. | Pendiente de asignar nombre o cargo |
| Responsable de métricas y anomalías | Persona que ejecuta cartas, bootstrap y scripts | La medición debe poder repetirse y tener un responsable técnico. | Pendiente de asignar nombre o cargo |
| Responsable de validación | Director o persona que revisa la muestra externa | Las alertas estadísticas no prueban exactitud; alguien debe contrastar los valores con evidencia externa. | Pendiente de confirmar |
| Aprobador final | Director del proyecto | La tesis necesita una autoridad que confirme que los criterios son aceptables metodológicamente. | Pendiente de confirmar |

## 2. Umbrales y severidad

| Grupo | Controles | Propuesta | Por qué se necesita | Estado |
|---|---|---|---|---|
| Integridad mínima | R01–R04, R07, INT01, INT02, MAP01 | Meta de 100 % | Estos controles representan condiciones básicas del archivo; una tolerancia podría ocultar filas imposibles de relacionar o interpretar. | Pendiente de aprobación |
| Completitud y consistencia | R05, R06, R08–R10, DEF01 | Meta de 100 %, reportada como tasa continua; advertencia cuando corresponda | El equipo debe decidir qué faltantes o variantes son aceptables para el uso energético previsto. | Pendiente de aprobación |
| Exactitud | EXA01 | 100 % en la muestra validada | Un porcentaje de coincidencia solo tiene sentido si se define la fuente de verdad, la muestra y la tolerancia de redondeo. | Pendiente de aprobar muestra y fuente |
| Oportunidad | OPO01 | Medir retraso publicación-descarga; usar proxy si no existe plazo publicado | Sin plazo esperado no se puede saber si una publicación fue tardía; el proxy debe reconocerse como indirecto. | Pendiente de aprobar plazo/proxy |
| Estadística | R11, R12, CART01 | Advertencia; no convertir señal automáticamente en error | Una señal identifica un comportamiento atípico, pero puede corresponder a un cambio real de tarifa o demanda. | Pendiente de calibración |

El 100 % es una meta del proyecto, no un umbral impuesto por DAMA-DMBOK ni ISO. Si el director aprueba tolerancias diferentes, deben registrarse junto con su justificación.

## 3. Catálogos y semántica de CHEC

Se debe aprobar el significado de categorías, niveles, unidades y conceptos tarifarios; el catálogo canónico y las equivalencias; la unidad de cada importe y el tratamiento de valores negativos; la clave candidata para identificar una tarifa por período; la aplicación definitiva de R08 y R09; y el responsable de mantener los catálogos.

**Por qué:** CHEC contiene códigos cuyo significado no está completamente explícito en el archivo. Si se interpretan sin catálogo, se podrían marcar como errores valores válidos o comparar conceptos que no tienen la misma unidad. La clave también debe aprobarse porque existen multiplicidades y no es seguro eliminar filas repetidas automáticamente.

**Estado:** análisis técnico en [DECISION_CATALOGOS_CHEC.md](../3.2/CHEC/DECISION_CATALOGOS_CHEC.md); aprobación documental pendiente.

## 4. Evidencia de exactitud

Se propone contrastar 30 registros por fuente, estratificados por período y categoría, contra una fuente oficial independiente o una publicación oficial del mismo período. Debe aprobarse la fuente, el tamaño y método de selección, los campos comparados, la tolerancia numérica y el tratamiento de diferencias por redondeo o unidad.

**Por qué:** una carta de control o una regla de formato solo muestra coherencia interna. EXA01 necesita una fuente externa que permita afirmar si el valor publicado coincide con una referencia confiable. Sin aprobar la muestra y la tolerancia, el porcentaje de exactitud no sería reproducible.

**Estado:** procedimiento y plantilla en [EVIDENCIA_EXACTITUD_OPORTUNIDAD.md](../3.1/EVIDENCIA_EXACTITUD_OPORTUNIDAD.md); la muestra y la fuente no están aprobadas.

## 5. Evidencia de oportunidad

Se propone registrar fecha de publicación o actualización, fecha de descarga, frecuencia esperada, retraso calculado y evidencia de la URL o metadato. Si el publicador no declara un plazo esperado, debe aprobarse el uso de un proxy y reportarse como `provisional_proxy`.

**Por qué:** la fecha de descarga no indica cuándo el dato estuvo disponible para los usuarios. Se necesita un plazo esperado para distinguir una publicación oportuna de una tardía. Si el portal no publica ese plazo, el director debe aceptar expresamente una medición indirecta.

**Estado:** procedimiento en [EVIDENCIA_EXACTITUD_OPORTUNIDAD.md](../3.1/EVIDENCIA_EXACTITUD_OPORTUNIDAD.md); pendiente de aprobar el plazo o proxy por fuente.

## 6. Reproducibilidad y versiones

El criterio de cierre solicita dos descargas. Debe aprobarse obtener una segunda descarga real del portal o usar una segunda copia congelada con fecha y SHA-256 diferentes, declarando que demuestra reproducibilidad técnica pero no estabilidad temporal del portal. También debe aprobarse la política de codificación y fin de línea de los CSV.

**Por qué:** una sola descarga demuestra que el código funciona sobre un archivo, pero no que los resultados se mantienen entre versiones. La segunda versión permite identificar cambios del portal y la política de codificación evita que el mismo archivo produzca hashes diferentes por razones técnicas.

**Estado:** procedimiento en [REPRODUCIBILIDAD_HITO3.md](../3.6/REPRODUCIBILIDAD_HITO3.md); segunda versión y política de fin de línea pendientes.

## 7. Decisiones estadísticas pendientes

- Confirmar que el bootstrap remuestrea series dentro de cada categoría y no filas individuales.
- Aceptar que XM y una categoría de SSPD tienen intervalos degenerados por contar con una sola serie.
- Confirmar que R12 y CART01 se interpretan como advertencias hasta contar con calibración de negocio o evidencia histórica suficiente.
- Confirmar si R10 seguirá medido por fila o se cambiará a celda por columna.

**Estado:** propuesta documentada; aprobación metodológica pendiente.

**Por qué:** estas decisiones cambian la interpretación de las cartas y del bootstrap. Definir la unidad de remuestreo, el tratamiento del MAD cero y la regla R12 evita que se comparen resultados generados con criterios diferentes.

## 8. Decisiones adicionales del Hito 4

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

Los resultados de 4.2–4.6 no deben presentarse como aprobación de un umbral, método o causa
regulatoria. Son evidencia para tomar estas decisiones.

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
