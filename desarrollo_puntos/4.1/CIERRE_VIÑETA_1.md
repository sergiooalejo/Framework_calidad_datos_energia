# Cierre parcial · Hito 4.1, viñeta 1

> **Documento histórico actualizado.** Este cierre describe el estado al terminar la primera
> viñeta de 4.1. Las métricas, la comparación a tasa igualada y los experimentos de inyección
> que aparecían como pendientes se completaron en 4.2 y 4.3. Las decisiones que todavía requieren
> aprobación están en el único registro vigente:
> [PENDIENTES_APROBACION_HITO3.md](../3_documentacion_general/PENDIENTES_APROBACION_HITO3.md).

## Puntos cerrados con los archivos disponibles

### Sensibilidad de umbral

Se ejecutaron de forma separada los umbrales 2.66, 3.0 y 3.267 mediante
`ejecutar_sensibilidad.py`. Cada resultado conserva sus CSV y configuración en
`resultados_umbral_2_66`, `resultados_umbral_3_0` y `resultados_umbral_3_267`.

### Huecos temporales

El cálculo fue corregido para aceptar únicamente pares de meses consecutivos.
No se imputan meses ni se calcula un cambio que cruce una discontinuidad. Las
series que no alcanzan 36 cambios de referencia más 12 de vigilancia válidos se
excluyen del resumen, conservando el criterio del protocolo.

### MAD igual a cero

Se generó `auditoria_mad_cero.json`. El tratamiento queda explicitado como
regla conservadora: no se inventa una escala y se marca señal si el cambio es
distinto de la mediana. Esto cierra la trazabilidad computacional, pero no la
aprobación metodológica definitiva de esa política.

## Pendientes que permanecían al cierre de 4.1

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
