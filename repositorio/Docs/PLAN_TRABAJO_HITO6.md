# Plan de trabajo del Hito 6

El Hito 6 valida, contrasta y sustenta lo construido en los Hitos 3–5. No debe presentar una
alerta estadística como error confirmado sin evidencia independiente.

## Implementación vigente

El código está en `Code/hito6/`. `python pipeline.py ejecutar muestra-h6` genera
50 observaciones únicas de EPM con alerta del H4-v2 vigente, referencia 36,
horizonte `t`, tasa objetivo de calibración 5 % y semilla 42. Conserva los seis
métodos (IMR, Z robusto, IF, LOF, KNN y R12), sus umbrales y puntajes.
El manifiesto específico verifica y registra la procedencia del H4. También se
puede ejecutar `python -m Code.hito6.run`; el acceso de compatibilidad permanece.
No se modifican las muestras anteriores ni sus revisiones.

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
| Muestra vigente de 50 alertas EPM | Generador alineado con H4-v2; revisión externa pendiente | `Data/gold/outputs/hito6/muestra_alertas_h4_v2_epm_50.csv` y su manifiesto |
| Hipótesis H1 | Pendiente de decisión | Comparar con bootstrap y procedimientos tradicionales |
| Reproducción en segundo ambiente | Parcial | Docker validado localmente; falta evidencia de otro equipo |
| Documento final | Pendiente | Integrar resultados aprobados |
| Sustentación | Pendiente | Preparar presentación y ensayo |

La muestra vigente sigue la solicitud original de 50 alertas de EPM y no duplica
observaciones entre escenarios. La muestra anterior de 15 EPM, 15 CHEC y 20 SSPD
permanece como antecedente histórico; no debe usarse para validar el H4 corregido.
La aprobación metodológica y la revisión externa siguen pendientes. La muestra
solo de alertas no basta para estimar recall ni calidad de todas las fuentes.

## Regla de interpretación

Cuando no exista confirmación externa, la redacción debe usar “alerta”, “señal” o “hipótesis de
inconsistencia”, nunca “error confirmado”.

