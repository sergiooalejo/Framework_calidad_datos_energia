# Pendientes · Hito 4.1 · Viñetas 1 y 2

> **Documento histórico actualizado.** Este archivo conserva el diagnóstico con el que terminó
> inicialmente 4.1. Los puntos 1, 2 y 3 fueron resueltos posteriormente en 4.2 y 4.3. Las
> decisiones que siguen vigentes no se aprueban aquí: están consolidadas en
> [PENDIENTES_APROBACION_HITO3.md](../3_documentacion_general/PENDIENTES_APROBACION_HITO3.md),
> que es el único registro para el director y el equipo.

## Estado general

Las dos viñetas tienen implementaciones reproducibles dentro de `4.1`:

- Z-score robusto sobre cambios logarítmicos.
- Isolation Forest entrenado con referencia y evaluado en vigilancia.

También se generaron sensibilidad de umbrales, calibración cruzada provisional,
trazabilidad de snapshots, scorecard OE1 provisional y la nota de la diferencia
entre las series SSPD del Hito 3 y Hito 4.1.

## Actividades realizadas

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

## Pendientes que permanecen

### 1. Repetir el experimento de errores inyectados — resuelto

Los archivos del Hito 2 contienen etiquetas y resultados de reglas, I-MR e
Isolation Forest anterior, pero no predicciones del Z-score robusto ni del nuevo
Isolation Forest logarítmico. Este rerun se realizó en 4.2 para las fuentes y
escenarios definidos allí; sus resultados se evalúan en 4.3.

### 2. Calcular precisión, recall, F1 e intervalos — resuelto

4.3 calcula estas métricas e intervalos para los errores inyectados. Las alertas
reales siguen sin etiqueta externa confirmada; esa limitación permanece vigente.

### 3. Comparar detección en t frente a t+1 — resuelto

4.2 ejecuta ambos horizontes para las inyecciones y 4.3 los reporta a tasa de
alerta igualada. No se infiere este resultado desde alertas reales.

### 4. Resolver el caso XM en validación cruzada

XM tiene una sola serie. Por esa razón se registra como `no_calibrable` en la
validación cruzada de cinco grupos. Puede reportarse su resultado descriptivo,
pero no un intervalo o una validación cruzada entre series.

### 5. Aprobar el tratamiento de MAD igual a cero

El comportamiento está implementado y auditado en `auditoria_mad_cero.json`,
pero la decisión final —señal, exclusión, IQR o caso degenerado— requiere
aprobación metodológica y revisión semántica de SSPD.

### 6. Validar alertas reales externamente

No existe una verdad terreno completa para EPM, CHEC, SSPD o XM. Las alertas
reales deben seguir presentándose como señales estadísticas hasta contrastar una
muestra con publicaciones oficiales.

### 7. Aprobar umbrales y estados del Hito 3

Los umbrales de la matriz OE1, los roles y la severidad permanecen pendientes
en `3_documentacion_general/PENDIENTES_APROBACION_HITO3.md`. El scorecard generado en 4.1 es
provisional y no reemplaza esa aprobación.

### 8. Segunda descarga para reproducibilidad temporal

Los hashes actuales prueban trazabilidad del snapshot utilizado, pero no que el
portal produzca los mismos resultados en una segunda descarga independiente.

## Limitación de interpretación

La comparación entre métodos es metodológicamente común, pero las fuentes no
son semánticamente intercambiables: EPM y CHEC contienen tarifas, SSPD contiene
información comercial/consumo y XM contiene demanda. Una señal no equivale por
sí sola a un error de calidad.
