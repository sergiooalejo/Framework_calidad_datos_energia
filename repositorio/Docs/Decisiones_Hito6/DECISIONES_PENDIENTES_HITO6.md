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
| 2 | Muestra de validación | Revisar 50 observaciones únicas EPM del H4-v2 vigente, según el plan original. | La muestra histórica multifuente queda como antecedente; confirmar interpretación, denominadores e intervalos del diseño vigente. | Pendiente |
| 3 | Tolerancia numérica | Definir antes de comparar si se acepta redondeo y cuál es su margen. | Las diferencias de formato o decimales no deben confundirse con errores. | Pendiente |
| 4 | Clasificación de alertas | Usar: confirmada, descartada, no concluyente o pendiente. | Separa la evidencia observada de una conclusión definitiva. | Pendiente |
| 5 | Falta de respuesta externa | Si EPM/CREG no responden, reportar validación interna y limitación explícita. | El silencio del publicador no demuestra que el dato sea correcto o incorrecto. | Pendiente |
| 6 | Casos prioritarios EPM | Mantener como hipótesis los casos 43.577, 43.501, 205.151, mezcla enero/abril y cambio de febrero de 2020 hasta obtener evidencia. | Son señales relevantes, pero requieren contexto tarifario para interpretarse. | Pendiente |
| 7 | Hipótesis H1 | Comparar el framework con cartas de control, reglas estadísticas y métodos de ML; decidir si H1 se mantiene o se reformula. | La decisión debe basarse en precisión, recall, F1 e intervalos, no solo en el número de alertas. | Pendiente |
| 8 | Alcance de reproducibilidad | Declarar reproducibilidad técnica en Docker y en un segundo equipo; no afirmar estabilidad futura del portal. | Dos ejecuciones prueban el procedimiento, pero no garantizan que las fuentes no cambien. | Pendiente |
| 9 | Presentación de resultados | Usar “alerta”, “señal” o “hipótesis de inconsistencia” cuando no exista confirmación externa. | Evita presentar una detección estadística como un error probado. | Pendiente |

## Decisión sobre la muestra manual

La muestra vigente es `Data/gold/outputs/hito6/muestra_alertas_h4_v2_epm_50.csv`,
acompañada de su manifiesto. Reúne 50 observaciones únicas EPM, referencia 36,
horizonte `t` y tasa objetivo de calibración 5 % del H4-v2. Registra los seis métodos,
incluidos LOF y KNN. Cada observación aparece una vez aunque alerten varios métodos.

Completar evidencia, clasificación, revisor, fecha y observaciones. La revisión
pendiente limita la conclusión científica. Se debe aprobar cómo tratar los casos
no concluyentes y calcular precisión e intervalos; la muestra por sí sola no estima
recall ni permite generalizar a todas las fuentes.

La muestra inicial `muestra_alertas_50.csv` se conserva: 15 EPM, 15 CHEC y 20 SSPD,
47 observaciones únicas y LOF no medido. Sus revisiones no se trasladan automáticamente.
Una nueva generación nunca sustituye clasificaciones existentes.

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
- [Muestra vigente de alertas](../../Data/gold/outputs/hito6/muestra_alertas_h4_v2_epm_50.csv)
