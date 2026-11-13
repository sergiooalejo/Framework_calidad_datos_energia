# Plan de trabajo del Hito 6

El Hito 6 valida, contrasta y sustenta lo construido en los Hitos 3–5. No debe presentar una
alerta estadística como error confirmado sin evidencia independiente.

## Orden de trabajo

1. **Congelar la línea base:** conservar commit, manifiestos, versión de Docker y resultados
   auditados de Hito 5.
2. **Validación externa:** documentar los casos prioritarios de EPM y la respuesta de EPM/CREG,
   si se obtiene. Si no hay respuesta, mantenerlos como hipótesis internas.
3. **Muestra manual:** seleccionar y registrar una muestra reproducible de 50 alertas reales,
   con fuente, período, regla, evidencia consultada y clasificación.
4. **Contraste de hipótesis:** comparar el framework con reglas estáticas y reportar recall,
   precisión, F1 e intervalos, indicando las prevalencias supuestas.
5. **Reproducibilidad:** repetir una ejecución en Docker y en un segundo ambiente; conservar
   comandos, versiones, hashes y diferencias.
6. **Documento final y sustentación:** integrar metodología, resultados, limitaciones, objetivos
   y evidencias; preparar preguntas y respuestas para el jurado.

## Estado inicial

| Actividad | Estado | Evidencia o siguiente acción |
|---|---|---|
| Línea base Hito 5 | Completada técnicamente | `Docs/INFORME_VALIDACION_HITO5.md` |
| Consulta externa | Pendiente | Usar `ANEXO_VALIDACION_EXTERNA_HITO6.md` |
| Muestra manual de 50 alertas | Preparada; pendiente de revisión | `Data/gold/outputs/hito6/muestra_alertas_50.csv` |
| Hipótesis H1 | Pendiente de decisión | Comparar con bootstrap y procedimientos tradicionales |
| Reproducción en segundo ambiente | Parcial | Docker validado localmente; falta evidencia de otro equipo |
| Documento final | Pendiente | Integrar resultados aprobados |
| Sustentación | Pendiente | Preparar presentación y ensayo |

La muestra fue seleccionada con semilla `42`: 15 alertas de EPM, 15 de CHEC y 20 de SSPD.
XM no tiene alertas reales elegibles en este corte; se documenta como no aplicable para esta
muestra y no se inventan registros para completar cuotas.
El plan original solicita 50 alertas de EPM: el diseño de la muestra propuesta y el tratamiento de
sus tres observaciones repetidas entre escenarios deben ser aprobados antes de calcular precisión.

## Regla de interpretación

Cuando no exista confirmación externa, la redacción debe usar “alerta”, “señal” o “hipótesis de
inconsistencia”, nunca “error confirmado”.

