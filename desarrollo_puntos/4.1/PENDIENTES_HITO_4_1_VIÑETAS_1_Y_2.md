# Pendientes · Hito 4.1 · Viñetas 1 y 2

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

### 1. Repetir el experimento de errores inyectados

Los archivos del Hito 2 contienen etiquetas y resultados de reglas, I-MR e
Isolation Forest anterior, pero no predicciones del Z-score robusto ni del nuevo
Isolation Forest logarítmico. Es necesario repetir la inyección, al menos sobre
el dataset EPM compatible, para producir resultados propios de 4.1.

### 2. Calcular precisión, recall, F1 e intervalos

Estas métricas dependen de la nueva ejecución de inyecciones. Pueden calcularse
para errores inyectados, pero no para alertas reales sin una etiqueta externa de
error confirmado.

### 3. Comparar detección en t frente a t+1

La estructura del experimento permite hacerlo, pero requiere la nueva ejecución
de inyecciones para ambos métodos. No debe inferirse desde las alertas reales.

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
