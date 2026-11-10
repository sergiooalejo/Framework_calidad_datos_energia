# Hito 4.6 · Resultados por nivel y costo computacional

Este informe completa la actividad 6 del Hito 4. El análisis separa niveles únicamente cuando
la fuente tiene un nivel explícito: EPM usa I–IV y CHEC usa los códigos 1–4. SSPD y XM se
reportan como `No_aplica` porque su esquema utilizado en este experimento no contiene un nivel
comparable. No se inventa una equivalencia para esas fuentes.

## Archivos

- `resultados_por_nivel.csv`: observaciones, detecciones y tasa de alerta por nivel y método.
- `costos_computacionales.csv`: tiempos registrados por etapa, fuente y experimento.
- `analizar_niveles_costos.py`: generación reproducible de ambos archivos.

## Protocolo de niveles

Se usa la cohorte `comun` y la referencia de 36 cambios del detalle de 4.2. Los métodos resumidos
son IMR, Z-score robusto, Isolation Forest y R12. La tasa es detecciones / observaciones; no es
una medida de exactitud y no debe confundirse con recall de errores inyectados.

Se separan los niveles para evitar que una fuente con muchas series de un solo nivel domine la
interpretación. El plan original menciona 69 series de Nivel I y 14 de niveles II–IV; esa cifra
corresponde a una variante de EPM y no se extrapola automáticamente a SSPD o XM.

## Costo computacional

Los tiempos se toman de las ejecuciones ya registradas en 4.2 y 4.3. En 4.3 se conservan las
etapas de ajuste, puntuación, tasa igualada/bootstrap, sorteo y total. En 4.2 se conserva el total
por escenario de sensibilidad. Los tiempos dependen del equipo y sirven para comparar escenarios
relativos, no como garantía de tiempo en otro computador.

## Limitaciones

- Las series dentro de una fuente pueden estar correlacionadas.
- SSPD y XM no tienen un nivel comparable en este corte.
- La variante `EPM_canonicas` es sensibilidad y no reemplaza a EPM.
- El costo por nivel no puede atribuirse causalmente a una sola variable si cambian también el
  número de series, observaciones o métodos.
- La ejecución de los scripts de 4.2–4.4 requiere numpy/pandas/scikit-learn instalados.

Filas generadas: 36 por nivel/método y 47 de costo computacional.
