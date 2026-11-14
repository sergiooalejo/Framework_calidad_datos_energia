# Verificación del Hito 4 · protocolo v2

La implementación se ejecuta con `python pipeline.py ejecutar hito4`. Conserva las
salidas históricas 4.2–4.4 y genera el protocolo corregido en `Data/gold/outputs/hito4/`.
No declara validación externa ni aprobación académica.

## Protocolo comparativo

Se usan las fuentes y cuarentenas por celda del Hito 3 corregido. La racha mensual
se fija antes de excluir valores; duplicados conflictivos, huecos y valores no
positivos invalidan cambios o rasgos. El análisis es retrospectivo: los doce meses
finales forman vigilancia y los 24/36/48 cambios anteriores forman referencia.
Esto delimita una población distinta del origen inicial del Hito 3.

Cada fuente y fecha de fin de referencia define un banco. Tres folds temporales
expansivos emplean la mitad inicial como primer entrenamiento y validan los tres
bloques siguientes, siempre dentro de referencia. Se recalculan estadísticas,
escalas y modelos en cada fold. Los umbrales por método/tasa se calculan con esos
puntajes fuera de muestra; luego se ajusta el modelo final solo con referencia y
se congelan los umbrales antes de puntuar vigilancia e inyecciones.

Se comparan I-MR, Z robusto, IF, LOF, KNN y R12 sobre los mismos casos en cada banco
común. La tasa se iguala en calibración hasta la resolución de empates; **no se
fuerza igualdad de tasas observadas en vigilancia**. Su diferencia es un resultado,
no un motivo para recalibrar con la prueba. Hay 840 filas de calibración con
menos de cinco alertas esperadas; esa baja resolución se identifica explícitamente.
Los IC son bootstrap pareado de categorías completas, 1.000 repeticiones.

## Tratamiento de LOF

La política técnica fijada antes de evaluar vigilancia elimina duplicados exactos
de los cuatro rasgos estandarizados **solo en referencia**. IF, LOF y KNN reciben
la misma geometría deduplicada. No se eliminan observaciones de prueba ni se cambia
la frecuencia publicada en Bronze. Se registran filas originales, vectores únicos,
vecinos y huella de geometría para cada fold y ajuste final.

Con menos de tres vectores o geometría de referencia numéricamente degenerada, LOF
se declara no interpretable. El banco completo se excluye del panel principal de
seis métodos, sin comparar poblaciones distintas ni inventar puntajes. Se excluyeron
0 bancos por referencia insuficiente o ausencia de calibración/geometría
común. La deduplicación cambia la ponderación de frecuencias de entrenamiento;
esa limitación permanece y no se presenta como aprobación del director.

## Métricas, sensibilidad y población

Los seis tipos de inyección se generan una vez y se comparten entre técnicas.
`tipos.csv` conserva denominadores por tipo; `sorteo.csv` registra 500 réplicas con
tres meses distintos por serie y sin reemplazo dentro de réplica. Esas repeticiones
no aumentan el número de meses independientes. Se reportan t y t o t+1.

Precisión y F1 se calculan para prevalencias **supuestas** de 1 %, 5 % y 10 %.
La tasa de alerta sobre registros reales sin verdad terreno es un proxy; estas
columnas no son precisión empírica. XM no recibe un IC inferencial con una categoría.
No se extrapolan las inyecciones a prevalencia real de errores.

`sensibilidad_pareada.csv` y `cohorte_pareada.csv` usan los mismos casos y
observaciones de vigilancia en las ventanas disponibles por fuente. Las tablas
generales conservan también el panel disponible, que tiene distinta cobertura.
`nativos.csv` contrasta constantes 2,66/3,267 y MAD 2,66/3/3,267, IF 99/99,5 y
R12 5/10/20 sin confundir sensibilidad nativa con la comparación a tasa calibrada.
Los costos por banco/etapa están en `costos.csv` y los niveles en `niveles.csv`.

## Scorecard

Se exportan 76 indicadores con fórmula, numerador, denominador,
umbral propuesto, estado de medición, resultado frente al umbral y decisión final;
32 filas resumen fuente/dimensión. Se distingue satisfacer una meta
propuesta de tenerla aprobada. No se promedian tasas con sentidos/poblaciones
distintas ni se publica un porcentaje global de calidad sin metodología acordada.
Oportunidad y exactitud/catálogos conservan sus limitaciones del Hito 3.

## Regla sistémica y contraste regulatorio

X=10/25/50/75 % son escenarios exploratorios, con desigualdad estricta y mínimo
dos series. Las alertas se conservan y se identifican como candidatas, sin convertir
la coincidencia mensual en cambio regulatorio confirmado. Se recalcula el contexto
tras inyecciones individuales y colectivas y se cuantifica el enmascaramiento.

Se capturaron seis documentos oficiales completos y se verificaron apartados
específicos; el registro está en `contraste_regulatorio.csv`, con hashes, fechas,
localizadores y límites. La 015/2018 enlaza la aplicación de ingresos con la
resolución particular; 078/2019 y 156/2019 son las de EPM. Falta constancia de
notificación/firmeza y conciliación con la liquidación LAC para demostrar el
mecanismo de febrero de 2020. La 152/2020 modifica medidas de pago/opción tarifaria;
la 003/2021 trata subsidios de estratos 1 y 2. Una cita en el encabezado de un PDF
no demuestra que esas normas causaran cada componente observado. Los valores
publicados por EPM se conservan junto a la procedencia del contraste numérico.

La calibración exploratoria de X vuelve a calcular con las entradas y cuarentenas
vigentes una carta móvil nativa I-MR y MAD para 24/36/48 cambios. No reemplaza la
comparación CV de las seis técnicas. `meses_plan_epm.csv`, `calibracion_X.csv` y
`composicion_meses_plan.csv` muestran los tres meses solicitados y la posibilidad
o imposibilidad de separarlos de otros meses. Esos otros meses no se etiquetan como
errores. Se reconciliaron 108 celdas transcritas con el CSV
EPM y 18 sumas de componentes con el CU total, tolerancia
de redondeo 0,02; esto verifica concordancia numérica, no causalidad regulatoria.

## Figuras incluidas

Se generaron 16 archivos PNG/SVG, versionables y con huella en el manifiesto:
comparación, curva detección/alerta, ventanas pareadas, constantes/percentiles/factores,
horizontes, riesgo de regla sistémica, evidencia del scorecard y componentes EPM. Sus datos son los
CSV del protocolo v2. Las figuras históricas no se presentan como resultados nuevos.

## Pendientes explícitos para cierre integral

1. Validación externa de alertas reales y precisión empírica, que corresponden al Hito 6.
2. Confirmar la causa concreta de los meses EPM con notificación/firmeza, cálculo LAC
   y/o respuesta del publicador; el contraste normativo por sí solo no la demuestra.
3. Aprobar umbrales de calidad, responsables, prevalencia/método principal y política
   operativa de X y LOF; las decisiones técnicas aquí adoptadas no son esa aprobación.
4. Resolver la evidencia de dimensiones todavía no medibles/provisionales heredada
   del Hito 3 e integrar estos resultados en el documento académico oficial.

No se marca completo el cierre académico mientras esos puntos sigan pendientes.

## Fuentes metodológicas y normativas

- [scikit-learn: validación temporal](https://scikit-learn.org/stable/modules/cross_validation.html#time-series-split).
- [scikit-learn: LOF con novelty=True y observaciones nuevas](https://scikit-learn.org/stable/modules/outlier_detection.html#novelty-detection-with-local-outlier-factor).
- [CREG 0015_2018](https://gestornormativo.creg.gov.co/gestor/entorno/docs/resolucion_creg_0015_2018.htm): 1.3.3 y 1.3.4.
- [CREG 0078_2019](https://gestornormativo.creg.gov.co/gestor/entorno/docs/resolucion_creg_0078_2019.htm): artículos 1 y 19.
- [CREG 0156_2019](https://gestornormativo.creg.gov.co/gestor/entorno/docs/resolucion_creg_0156_2019.htm): considerandos y artículo 12.
- [CREG 0012_2020](https://gestornormativo.creg.gov.co/gestor/entorno/docs/resolucion_creg_0012_2020.htm): considerandos y artículo 4.
- [CREG 0152_2020](https://gestornormativo.creg.gov.co/gestor/entorno/docs/resolucion_creg_0152_2020.htm): artículos 2, 3, 4 y 5.
- [CREG 0003_2021](https://gestornormativo.creg.gov.co/gestor/entorno/docs/resolucion_creg_0003_2021.htm): artículos 1, 9 y 11.
