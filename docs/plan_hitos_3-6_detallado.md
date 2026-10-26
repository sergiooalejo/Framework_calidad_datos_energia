# Plan de cierre de brechas · Hitos 3 a 6 (versión detallada)

Trabajo de grado *Framework automatizado para la evaluación de la calidad de datos en registros administrativos del sector energético en Colombia* (Grupo 03; dirección del trabajo).

Sin fechas: la secuencia es la propuesta y el calendario lo fija el director con el programa. Líderes según el reparto del cronograma del anteproyecto (responsable de datos; responsable de métricas y anomalías; responsable de reglas de negocio).

## Brechas del Hito 2 (revisión del 23 de octubre de 2026, código ejecutado y cifras reproducidas)

- Una sola fuente (EPM)
- Un modelo, sin sensibilidad
- Sin artefacto ni tablero
- Nada confirmado con la entidad
- Hipótesis vs. diseño sin resolver
- OE1 sin métricas definidas

## Hito 3 · Replicar y formalizar (OE1, OE2) · Lidera: responsable de datos

*Cierra: una sola fuente · trazabilidad por posición · cartas fuera del anteproyecto · OE1 sin entregable*

### Actividades

1. **Matriz dimensión → métrica → indicador → regla (OE1).**
   - Ocho dimensiones de DMBOK2 cap. 13 con definición propia para tarifas; las 12 reglas clasificadas en los 10 tipos de regla.
   - Plantilla por indicador: fórmula como cociente, unidad, umbral, severidad, frecuencia, responsable y tendencia.
   - Añadir integridad (clave categoría + período) y razonabilidad (cartas); excluir oportunidad por escrito. Relación explícita con ISO/IEC 25012.
2. **Ficha de caracterización por fuente (OE2).**
   - EPM sfcd-b3ey: 3.623 filas, 12 columnas, dic-2016 a dic-2021; 202 series posibles, 83 con 49 meses o más.
   - Superservicios vfjy-6fka: 5.396 filas, 16 columnas, 8 períodos. Consumidores del dato, datos críticos, unidades y significado de Rango de Consumo (2.143 ausentes).
3. **Replicar el pipeline en Superservicios.**
   - Reglas transversales R01 a R11 y perfilamiento; las cartas no aplican con 8 períodos y se documenta.
   - Informe de diferencias: qué reglas y umbrales cambian y qué dimensiones quedan sin cubrir en cada fuente.
4. **Decidir la fuente CREG.**
   - Buscar en datos.gov.co un conjunto de la CREG con series mensuales de 48 meses o más. Si no existe, reformular OE2 por escrito: fuentes abiertas del sector con la CREG como referencia regulatoria.
5. **Cartas en cambios logarítmicos y formalizadas.**
   - Sustituir la diferencia absoluta por la diferencia de logaritmos en la carta I, la carta MR y los rasgos del Isolation Forest; recalcular límites.
   - Marco teórico 3.1.5: Jones-Farmer et al. (2014) y DMBOK2 cap. 13, técnica de control estadístico de procesos. Metodología 5.6.4: cartas como método estadístico clásico en lugar de Z-score.
6. **Trazabilidad estable entre descargas.**
   - Descarga por API con identificador de fila; hash SHA-256 y fecha de cada descarga; clave de contenido (categoría, fecha, columna) en hallazgos y alertas.
   - Motivo: los registros 2047, 3131, 3133 y 2348 de la diapositiva 7 cambian de posición en otra descarga del portal.
7. **Cuarentena por valor y remuestreo correcto.**
   - La cuarentena entra en el cálculo de límites: se excluyen los cambios que tocan un valor en cuarentena, sin interpolar. Hoy solo marca la serie como sucia.
   - Bootstrap por categoría (23 del Nivel I y 5 de otros niveles), no por serie. R12 pasa de Error a Advertencia hasta confirmación.

### Insumos y fundamento

- 03_hallazgos.csv y 05_alertas_imr_reales.csv
- 08_copia_preparada.csv
- Resumen DAMA: secciones 2, 3 y 4
- Anteproyecto: 3.1.5, 5.6.4, 5.8
- Retro de junio: observaciones 5 y 7

### Entregables

- Notebook replicado en las dos fuentes
- Informe de diferencias entre fuentes
- Matriz OE1 con plantilla llena por regla
- Fichas de caracterización
- Anteproyecto actualizado

### Criterio de cierre

El pipeline corre sin cambios manuales en las dos fuentes y da los mismos hallazgos con dos descargas distintas. Cada regla tiene dimensión, tipo, fórmula y umbral. El anteproyecto ya nombra las cartas.

### Riesgo y mitigación

Superservicios tiene 8 períodos: allí solo reglas y métodos transversales. Si la CREG no tiene series largas, la replicación de cartas queda solo en EPM y se declara como limitación.

## Hito 4 · Comparar con protocolo (OE3, OE4) · Lidera: responsable de métricas y anomalías

*Cierra: un solo modelo · sin sensibilidad · sin precisión ni F1 · n efectivo sobreestimado*

### Actividades

1. **Técnicas adicionales con el mismo protocolo.**
   - Z-score robusto (mediana y MAD) sobre cambios log como línea base del anteproyecto; LOF o KNN sobre los cuatro rasgos del Isolation Forest; Extended IF si el tiempo alcanza.
   - Entrenamiento solo en referencia, evaluación en vigilancia, umbral por validación cruzada a tasa de alerta igualada, como ya se hace con IF.
2. **Análisis de sensibilidad.**
   - Ventana de referencia de 24, 36 y 48 cambios; constantes 2,66 y 3,267 frente a 3 sigma con MAD; percentil 99 y 99,5; factor de R12 en 5, 10 y 20.
   - Ventana de detección t frente a t y t+1; efecto de la regla de alerta sistémica sobre la tasa de alerta.
3. **Métricas completas y honestas.**
   - Precisión, recall y F1 a tasa de alerta igualada; curvas de detección contra tasa de alerta por método.
   - Reportar pruebas por tipo (hoy entre 760 y 1.540) y meses distintos sorteados (13 de 23 en promedio); sortear sin reemplazo.
4. **Regla de alerta sistémica.**
   - Si más de X % de las series alertan en el mismo mes, se clasifica como cambio regulatorio y no como error de dato; calibrar X con feb-2020 (51 de 83), jul-2020 (24) y jul-2021 (18).
   - Contrastar con resoluciones CREG y publicaciones tarifarias de EPM de esos meses.
5. **Scorecard por dimensión (OE1 en resultados).**
   - Calcular cada indicador de la matriz en ambas fuentes; tabla única con umbral y estado, como pide DMBOK2 para el reporte de calidad.
6. **Resultados por nivel y costo de cómputo.**
   - Separar Nivel I (69 series casi colineales, razones medianas 0,964 y 0,928) de los niveles II a IV (14 series); tiempo de cómputo por etapa y por fuente.

### Insumos y fundamento

- 06_experimento_inyeccion.csv
- 11_puntajes_limpios_por_serie.csv
- 07_deteccion_por_tipo.csv
- Resumen DAMA: sección 4 (métricas)
- Anteproyecto: 5.6.5 y 5.6.6

### Entregables

- Tabla comparativa con IC 95 % por técnica y tipo de error
- Figuras de sensibilidad
- Catálogo de alertas sistémicas
- Scorecard por fuente y dimensión
- Sección preliminar de resultados

### Criterio de cierre

Toda técnica pasó por el mismo protocolo y los mismos errores. Las conclusiones llevan intervalo. La sensibilidad está reportada. El scorecard existe en las dos fuentes.

### Riesgo y mitigación

Fuera del Nivel I hay 14 series: las conclusiones por nivel se presentan con cautela. La regla sistémica puede ocultar errores masivos reales; dejarlo como limitación.

## Hito 5 · Construir el artefacto (OE3) · Lidera: responsable de reglas de negocio

*Cierra: no existe el artefacto prometido (paquete, contenedor, tablero) · guion de 1.171 líneas sin dependencias fijadas*

### Actividades

1. **Paquete Python por componentes.**
   - Módulos cargar, perfilar, reglas, series, cartas, anomalías, evaluar y reportar; sin variables globales compartidas entre partes (hoy df, resumen y meses se redefinen entre el Hito 1 y el 2).
2. **Reglas en configuración, no en código.**
   - Archivo YAML con id, dimensión, tipo, severidad, fórmula, umbral y referencia regulatoria por regla; el motor las lee y las registra en la bitácora.
3. **Línea de comandos y salidas.**
   - descargar → evaluar → reportar; salidas CSV y JSON con metadatos de ejecución: hash, fecha, versión del paquete y semilla.
4. **Reproducibilidad computacional.**
   - pyproject con Poetry y versiones fijadas de pandas, scikit-learn, statsmodels y matplotlib; Dockerfile; pruebas automáticas con un conjunto pequeño y errores inyectados conocidos.
5. **Tablero de monitoreo.**
   - Power BI sobre las salidas: scorecard por dimensión, alertas por fuente y mes, bitácora de incidentes con estado; limitado a las salidas de 5.9.2. Exportar también el scorecard en CSV.
6. **Documentación del artefacto.**
   - Diagrama de componentes 5.9 con entradas y salidas reales; README de reproducción; bitácora de incidentes con estado, responsable y fecha (operación de calidad en DMBOK2).

### Insumos y fundamento

- Código hasta Hito 2 (1.171 líneas)
- Resumen DAMA: secciones 5 y 6
- Anteproyecto: 5.7 y 5.9
- Retro de junio: observación 6

### Entregables

- Repositorio etiquetado v1.0
- Imagen Docker
- Tablero de monitoreo
- README de reproducción

### Criterio de cierre

Otra persona reproduce los resultados desde el contenedor con un solo comando, las pruebas pasan y el resumen JSON coincide con el del Hito 4.

### Riesgo y mitigación

Power BI no es reproducible por código. Mantener el scorecard en CSV como salida primaria y el tablero como vista.

## Hito 6 · Validar y sustentar (OE4) · Lidera: equipo

*Cierra: errores sin confirmar · hipótesis incoherente con el diseño · reproducibilidad no medida · observaciones de junio*

### Actividades

1. **Validación externa.**
   - Consulta formal a EPM o a la CREG sobre los seriales 43.577 y 43.501, el valor 205.151, la mezcla de enero y abril y el cambio de febrero de 2020.
2. **Verificación manual de alertas.**
   - Muestra aleatoria de 50 alertas reales contrastada con la publicación original de EPM; precisión empírica con intervalo.
3. **Resolver hipótesis frente a diseño.**
   - Reglas estáticas como procedimiento tradicional (MinTIC, Deequ); framework como reglas más cartas y ML; contraste de H1 con el bootstrap (hoy 88 % frente a 73 %).
   - Si no se sostiene, reformular bajo Design Science y decirlo en el documento.
4. **Reproducibilidad como resultado.**
   - Misma salida en dos ambientes (Colab y Docker) y con dos descargas distintas; reportarlo como evidencia, no como herramienta, según la nota de dirección de junio.
5. **Documento final.**
   - Problema y pregunta; marco con DMBOK e ISO delimitados; metodología con tipos de regla, ciclo y técnicas; resultados; limitaciones: tamaño efectivo, carácter retrospectivo, una sola fuente con series largas.
   - Depurar referencias, cronograma y resumen (observaciones menores de junio).
6. **Sustentación.**
   - Ensayo con jurado simulado; cada objetivo específico con su evidencia señalada en el documento.

### Insumos y fundamento

- Retroalimentación de junio
- 05_alertas_imr_reales.csv
- 03_hallazgos.csv
- Anteproyecto completo

### Entregables

- Documento final
- Anexo de validación externa
- Repositorio final y tablero
- Presentación de sustentación

### Criterio de cierre

H1 contrastada o reformulada con evidencia. Cada objetivo específico señala el entregable que lo cumple. Las observaciones de junio están cerradas.

### Riesgo y mitigación

EPM o la CREG no responden a tiempo. Presentar los casos como hipótesis con evidencia interna y dejarlo como limitación explícita.

## Trazabilidad objetivo → hito → entregable → evidencia

| OE | Objetivo específico | Hitos | Entregable que lo cumple | Dónde queda la evidencia |
|---|---|---|---|---|
| OE1 | Dimensiones, métricas e indicadores (DAMA, ISO) | Hito 3 → Hito 4 | Matriz regla-dimensión-tipo-métrica; scorecard por fuente | Tabla en metodología y tabla de resultados |
| OE2 | Caracterización y reglas de negocio, fuente CREG | Hito 3 → Hito 5 | Fichas por fuente; decisión CREG; reglas en YAML con referencia regulatoria | Sección 5.8 actualizada y archivo de reglas |
| OE3 | Framework: perfilamiento, reglas, anomalías | Hito 4 → Hito 5 | Paquete, contenedor, tablero; técnicas comparadas | Repositorio v1.0 y diagrama 5.9 |
| OE4 | Evaluar frente a procedimientos tradicionales | Hito 4 → Hito 6 | Tabla comparativa con IC; validación externa; reproducibilidad medida | Contraste de H1 y anexo de validación |

## Dependencias

Hito 3 entrega a Hito 4 las cartas en log, la matriz OE1 y la clave estable. Hito 4 entrega a Hito 5 las técnicas y umbrales definitivos a empaquetar. Hito 5 entrega a Hito 6 el artefacto reproducible con el que se mide la reproducibilidad. Hito 6 cierra con los tres anteriores.

Figura: `plan_hitos_3-6_detallado.svg` (íconos Font Awesome Free 6.5.2, CC BY 4.0).