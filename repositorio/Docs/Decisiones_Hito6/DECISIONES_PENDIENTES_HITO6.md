# Decisiones pendientes de aprobación · Hito 6

**Propósito:** reunir en un solo documento las decisiones metodológicas que deben confirmar el
equipo y el profesor antes de cerrar el Hito 6. Las propuestas no se consideran aprobadas hasta
recibir una confirmación explícita.

## Estado general

La implementación técnica y la muestra reproducible de 50 alertas ya están preparadas. Falta
definir cómo se interpretan, validan y presentan los resultados. Una alerta es una señal para
revisión; no equivale automáticamente a un error confirmado.

## Decisiones para aprobación

| Nº | Decisión | Propuesta de trabajo | Por qué es necesaria | Estado |
|---:|---|---|---|---|
| 1 | Fuente de verdad para exactitud | Usar la publicación oficial del portal o una respuesta formal del publicador. | Sin una referencia independiente no se puede afirmar que un valor sea correcto. | Pendiente |
| 2 | Muestra de validación | Decidir entre la muestra de 50 alertas de EPM solicitada en el plan y la propuesta existente de 15 EPM, 15 CHEC y 20 SSPD. | Son diseños distintos; la muestra existente tiene 47 combinaciones únicas fuente/serie/período porque tres se repiten en distintos escenarios. | Pendiente |
| 3 | Tolerancia numérica | Definir antes de comparar si se acepta redondeo y cuál es su margen. | Las diferencias de formato o decimales no deben confundirse con errores. | Pendiente |
| 4 | Clasificación de alertas | Usar: confirmada, descartada, no concluyente o pendiente. | Separa la evidencia observada de una conclusión definitiva. | Pendiente |
| 5 | Falta de respuesta externa | Si EPM/CREG no responden, reportar validación interna y limitación explícita. | El silencio del publicador no demuestra que el dato sea correcto o incorrecto. | Pendiente |
| 6 | Casos prioritarios EPM | Mantener como hipótesis los casos 43.577, 43.501, 205.151, mezcla enero/abril y cambio de febrero de 2020 hasta obtener evidencia. | Son señales relevantes, pero requieren contexto tarifario para interpretarse. | Pendiente |
| 7 | Hipótesis H1 | Comparar el framework con cartas de control, reglas estadísticas y métodos de ML; decidir si H1 se mantiene o se reformula. | La decisión debe basarse en precisión, recall, F1 e intervalos, no solo en el número de alertas. | Pendiente |
| 8 | Alcance de reproducibilidad | Declarar reproducibilidad técnica en Docker y en un segundo equipo; no afirmar estabilidad futura del portal. | Dos ejecuciones prueban el procedimiento, pero no garantizan que las fuentes no cambien. | Pendiente |
| 9 | Presentación de resultados | Usar “alerta”, “señal” o “hipótesis de inconsistencia” cuando no exista confirmación externa. | Evita presentar una detección estadística como un error probado. | Pendiente |

## Decisión sobre la muestra manual

El archivo `Data/gold/outputs/hito6/muestra_alertas_50.csv` contiene la muestra inicial. Para cada fila deben
completarse la evidencia consultada, la clasificación, el revisor, la fecha y las observaciones.
La revisión puede quedar pendiente sin invalidar la ejecución técnica, pero debe declararse como
limitación del Hito 6.

La columna LOF de la muestra existente está vacía porque la entrada utilizada no contiene ese
método; no representa una medición de LOF. Una nueva generación crea otro archivo y no sustituye
las clasificaciones existentes. Debe decidirse si la unidad de revisión será la observación
única o cada combinación de observación y escenario, y cómo se calculará el intervalo de precisión.

## Aprobación solicitada al profesor

Se solicita confirmar:

1. la fuente de verdad y la tolerancia para EXA01;
2. la muestra de 50 alertas y su método de selección;
3. la clasificación propuesta y el tratamiento de casos no concluyentes;
4. el tratamiento de la falta de respuesta de EPM/CREG;
5. el alcance de la conclusión sobre H1;
6. la redacción de reproducibilidad técnica y de las limitaciones.

**Respuesta del profesor:** pendiente.

**Fecha de aprobación:** pendiente.

**Observaciones:** pendiente.

## Documentos relacionados

- [Plan de trabajo del Hito 6](../PLAN_TRABAJO_HITO6.md)
- [Anexo de validación externa](../ANEXO_VALIDACION_EXTERNA_HITO6.md)
- [Registro general de decisiones](../DECISIONES.md)
- [Muestra reproducible de alertas](../../Data/gold/outputs/hito6/muestra_alertas_50.csv)
