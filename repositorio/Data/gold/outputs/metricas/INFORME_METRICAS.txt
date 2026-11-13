# Hito 4.3 · Métricas completas y honestas

Fecha: 7 de noviembre de 2026. Corresponde a la actividad 3 del Hito 4 del plan: precisión,
recall y F1 a tasa de alerta igualada, curvas de detección contra tasa de alerta por método,
pruebas por tipo, meses distintos sorteados sin reemplazo. Completa además lo que 4.1 dejó
pendiente: métricas del Z-score robusto y del Isolation Forest con rasgos logarítmicos, y LOF/KNN.
No modifica 4.1 ni 4.2.

## Resultado en cinco frases

1. A tasa de alerta igualada del 5 %, **I-MR, Z-score robusto, Isolation Forest y KNN no se separan de forma
   consistente**: su F1 queda entre 0,49 y 0,52 en EPM,
   entre 0,54 y 0,59 en CHEC y entre
   0,48 y 0,51 en SSPD, con intervalos que se solapan.
   De 18 diferencias pareadas evaluables frente a I-MR, el IC excluye el cero a favor
   de otro método en 1 (sin corrección por comparaciones múltiples): EPM, Z-score robusto (MAD) (Δ F1 = 0,035).
2. **LOF y R12 rinden menos que las cartas** donde se pueden evaluar. El IC de la diferencia excluye el cero para R12 en
   CHEC, SSPD y para LOF en
   SSPD; en EPM la diferencia tiene el mismo signo pero el IC
   la incluye (solo hay 5 categorías). LOF es **numéricamente degenerado en CHEC** (9.936 filas de entrenamiento, 2.126 únicas).
3. **Ningún método estadístico detecta el «valor no actualizado»**: su recall en t va de
   0,00 a 0,08 (de 0,03 a 0,16 si se admite t+1).
   Un valor repetido no es un cambio atípico; se detecta con una regla, no con una carta. Es el argumento a favor de
   «reglas + cartas» frente a cartas solas.
4. **La precisión no es una propiedad del método sino de la prevalencia de errores**, que aquí no se conoce. Por eso se
   reporta con prevalencias supuestas del 1, 5 y 10 %, y la tasa de «falsas alertas» se llama *tasa de alerta en meses reales
   sin error conocido*: no hay etiquetas externas que confirmen que esas alertas sean falsas.
5. **Las conclusiones no dependen de cómo se escriban las etiquetas de EPM.** EPM escribe de varias formas la misma etiqueta y, sin
   normalizar, sus series se fragmentan (27 series en el panel común frente a 69 con las equivalencias aprobadas internamente en el Hito 2).
   Repetido con esas equivalencias, el F1 de I-MR, Z-score, Isolation Forest y KNN queda entre 0,50 y 0,55 (antes entre 0,49 y 0,52),
   con los mismos intervalos solapados; ver la sección 3b.

## 1. Qué se midió

**Panel.** El escenario principal de 4.2: referencia de 36 cambios, vigilancia de 12, cohorte común
(EPM 27, CHEC 276,
SSPD 321 y XM 1 series).
Las inyecciones y los modelos Isolation Forest son los mismos de 4.2: se verificó que, para cada caso,
las banderas nativas de este experimento coinciden con `4.2/inyecciones_detalle.csv.gz`
([verificacion_contra_4_2.json](verificacion_contra_4_2.json)).

**Seis métodos con puntaje continuo** (más alto = más anómalo, necesario para igualar tasas):

| Método | Puntaje | Umbral nativo |
|---|---|---|
| Cartas I-MR | máx(\|c−media\|/(2,66·MR̄), \|c−anterior\|/(3,267·MR̄)) | puntaje > 1 |
| Z-score robusto | \|c−mediana\|·0,6745/MAD | \|z\| > 3 |
| Isolation Forest | −score_samples, 300 árboles, 4 rasgos | percentil 99,5 de entrenamiento |
| LOF | −score_samples (`novelty=True`, 20 vecinos), mismos rasgos | no tiene |
| KNN | distancia media a los 5 vecinos de referencia, mismos rasgos | no tiene |
| R12 | \|nivel\| / mediana de referencia | factor 5, 10 o 20 |

Modelos y escalas se ajustan solo con la referencia. Cuando MAD o MR valen cero se usa una escala de respaldo
(desviación absoluta media, luego desviación estándar) **solo para ordenar puntajes**; la regla nativa de 4.1
para MAD cero se conserva en la verificación contra 4.2 (sin discrepancias en series con escala positiva).

**Tasa de alerta igualada.** Para cada fuente, método y tasa objetivo (1, 2, 5 y 10 %) el umbral es el puntaje que deja esa
fracción de las observaciones **reales** de vigilancia por encima. No usa etiquetas. Así todos los métodos alertan lo mismo
sobre los datos reales y solo pueden diferenciarse por cuánto detectan de lo inyectado. Los empates pueden dejar la tasa
observada ligeramente por debajo de la objetivo; se reporta en [umbrales_tasa_igualada.csv](umbrales_tasa_igualada.csv).

**Etiquetas.** Positivo: el valor inyectado en el mes t. Negativo: las observaciones reales sin inyección, que incluyen alertas
reales sin error conocido (supuesto conservador: pueden contener errores verdaderos, de modo que la precisión es un límite
inferior). Horizonte *t*: alerta en el mes inyectado; horizonte *t o t+1*: alerta en cualquiera de los dos, con la tasa de
alerta real medida sobre pares de meses consecutivos para que el criterio sea el mismo en positivos y negativos.

**Métricas.** El recall global es **macro**: promedio de los recall de los seis tipos con el mismo peso, de modo que ningún
tipo domine por tener más casos. La precisión se obtiene de recall y tasa de alerta real para una prevalencia supuesta
π: `P = R·π / (R·π + FPR·(1−π))`, y F1 es su media armónica con el recall. Los intervalos son bootstrap de
**categorías completas** (1.000 repeticiones, TPR y tasa de alerta remuestreados juntos); sin IC cuando hay una sola categoría.

## 2. Pruebas por tipo y meses distintos (observación 6 de la revisión)

La revisión del Hito 2 señaló que 20 sorteos por serie y tipo caían en 13 meses distintos en promedio y que «columna
equivocada» tenía 760 pruebas frente a 1.540 de los otros tipos. Aquí se reportan los denominadores reales y el sorteo se hace
**sin reemplazo**: en cada réplica, cada serie recibe 3 meses de origen distintos y un tipo de
error uniforme entre los disponibles ese mes (500 réplicas). La condición de meses distintos se
verifica con una aserción en cada ejecución y con pruebas unitarias.

| Fuente | Tipo | Casos exhaustivos | Series | Categorías | Meses de calendario distintos | Pruebas por réplica (sorteo) |
|---|---|---|---|---|---|---|
| EPM | decimal_x1000 | 297 | 27 | 5 | 11 | 14,9 |
| EPM | decimal_div1000 | 297 | 27 | 5 | 11 | 14,9 |
| EPM | serial_excel_43577 | 297 | 27 | 5 | 11 | 15,3 |
| EPM | aumento_10pct | 297 | 27 | 5 | 11 | 15,1 |
| EPM | valor_no_actualizado | 297 | 27 | 5 | 11 | 15,0 |
| EPM | otra_medida | 132 | 12 | 4 | 11 | 5,8 |
| CHEC | decimal_x1000 | 3.036 | 276 | 4 | 22 | 147,4 |
| CHEC | decimal_div1000 | 3.036 | 276 | 4 | 22 | 147,9 |
| CHEC | serial_excel_43577 | 3.036 | 276 | 4 | 22 | 147,6 |
| CHEC | aumento_10pct | 3.036 | 276 | 4 | 22 | 148,3 |
| CHEC | valor_no_actualizado | 2.979 | 276 | 4 | 22 | 145,6 |
| CHEC | otra_medida | 1.980 | 180 | 4 | 22 | 91,2 |
| SSPD | decimal_x1000 | 3.531 | 321 | 89 | 19 | 162,8 |
| SSPD | decimal_div1000 | 3.531 | 321 | 89 | 19 | 164,7 |
| SSPD | serial_excel_43577 | 3.531 | 321 | 89 | 19 | 163,1 |
| SSPD | aumento_10pct | 3.531 | 321 | 89 | 19 | 163,2 |
| SSPD | valor_no_actualizado | 3.351 | 315 | 89 | 19 | 153,7 |
| SSPD | otra_medida | 3.405 | 311 | 88 | 19 | 155,4 |
| XM | decimal_x1000 | 11 | 1 | 1 | 11 | 0,6 |
| XM | decimal_div1000 | 11 | 1 | 1 | 11 | 0,6 |
| XM | serial_excel_43577 | 11 | 1 | 1 | 11 | 0,6 |
| XM | aumento_10pct | 11 | 1 | 1 | 11 | 0,6 |
| XM | valor_no_actualizado | 11 | 1 | 1 | 11 | 0,5 |
| XM | otra_medida | 0 | 0 | 0 | 0 | 0,0 |

«Otra medida» solo existe donde la serie tiene otra medida positiva en el mismo grupo y mes (en EPM, 12 de 27 series; en XM
ninguna), y «valor no actualizado» se omite cuando el valor anterior es igual al actual. Omisiones registradas en
[inyecciones_omitidas.csv](inyecciones_omitidas.csv): EPM/otra_medida: 165 (sin otra medida positiva distinta); CHEC/otra_medida: 1056 (sin otra medida positiva distinta); CHEC/valor_no_actualizado: 57 (la alteracion no cambia el valor); SSPD/otra_medida: 126 (sin otra medida positiva distinta); SSPD/valor_no_actualizado: 180 (la alteracion no cambia el valor); XM/otra_medida: 11 (sin otra medida positiva distinta); EPM_canonicas/otra_medida: 363 (sin otra medida positiva distinta).

**Las pruebas siguen sin ser independientes**: los casos de una misma serie comparten referencia, escala y modelo, y las
series de una categoría están correlacionadas. Por eso los intervalos remuestrean categorías completas y no casos.

Consistencia del sorteo con el cálculo exhaustivo (I-MR, 5 %, horizonte t):

| Fuente | Pruebas por réplica | Recall del sorteo (media) | Rango 95 % entre réplicas | Recall exhaustivo macro | Diferencia |
|---|---|---|---|---|---|
| EPM | 81 | 0,678 | 0,574–0,778 | 0,629 | 0,049 |
| CHEC | 828 | 0,775 | 0,749–0,803 | 0,785 | -0,009 |
| SSPD | 963 | 0,668 | 0,641–0,694 | 0,663 | 0,005 |
| XM | 3 | 0,720 | 0,333–1,000 | 0,691 | 0,029 |
| EPM_canonicas | 207 | 0,694 | 0,630–0,754 | 0,654 | 0,040 |

La diferencia absoluta máxima entre el sorteo y el cálculo exhaustivo es de 0,062. Aparece en EPM porque el
sorteo reparte los tipos uniformemente **entre los disponibles de cada mes** y «otra medida» está disponible en menos series;
no es un error de cálculo.

## 3. Precisión, recall y F1 a tasa de alerta del 5 %

Horizonte t, prevalencia supuesta del 5 %. La fila «Tasa de alerta real» es la tasa observada sobre meses reales tras igualar.

**EPM** (5 categorías; el IC es amplio porque hay pocas):

| Método | Recall macro [IC 95 %] | Tasa de alerta real | Precisión conservadora [IC] | F1 [IC] | Estado |
|---|---|---|---|---|---|
| Cartas I-MR | 0,63 [0,59–0,67] | 4,9 % | 0,40 [0,21–1,00] | 0,49 [0,31–0,80] | evaluable |
| Z-score robusto (MAD) | 0,67 [0,61–0,71] | 4,6 % | 0,43 [0,24–1,00] | 0,52 [0,34–0,82] | evaluable |
| Isolation Forest | 0,62 [0,61–0,67] | 4,6 % | 0,41 [0,24–1,00] | 0,49 [0,35–0,80] | evaluable |
| LOF | 0,54 [0,51–0,63] | 4,9 % | 0,37 [0,15–0,67] | 0,44 [0,23–0,59] | evaluable |
| KNN (distancia media, k=5) | 0,65 [0,62–0,68] | 4,9 % | 0,41 [0,25–1,00] | 0,50 [0,35–0,80] | evaluable |
| R12 (magnitud del nivel) | 0,36 [0,33–0,37] | 4,6 % | 0,29 [0,21–1,00] | 0,32 [0,27–0,52] | evaluable |

**CHEC** (4 categorías):

| Método | Recall macro [IC 95 %] | Tasa de alerta real | Precisión conservadora [IC] | F1 [IC] | Estado |
|---|---|---|---|---|---|
| Cartas I-MR | 0,78 [0,77–0,79] | 4,9 % | 0,46 [0,44–0,51] | 0,58 [0,57–0,62] | evaluable |
| Z-score robusto (MAD) | 0,81 [0,80–0,82] | 5,0 % | 0,46 [0,39–0,88] | 0,59 [0,52–0,85] | evaluable |
| Isolation Forest | 0,70 [0,66–0,72] | 4,8 % | 0,43 [0,35–1,00] | 0,54 [0,47–0,80] | evaluable |
| LOF | 0,01 [0,00–0,02] | 4,8 % | 0,01 [0,01–0,01] | 0,01 [0,01–0,02] | degenerado_por_duplicados |
| KNN (distancia media, k=5) | 0,75 [0,71–0,77] | 5,0 % | 0,44 [0,36–1,00] | 0,56 [0,49–0,84] | evaluable |
| R12 (magnitud del nivel) | 0,44 [0,41–0,45] | 4,8 % | 0,32 [0,25–1,00] | 0,37 [0,32–0,58] | evaluable |

**SSPD** (89 categorías):

| Método | Recall macro [IC 95 %] | Tasa de alerta real | Precisión conservadora [IC] | F1 [IC] | Estado |
|---|---|---|---|---|---|
| Cartas I-MR | 0,66 [0,65–0,68] | 5,0 % | 0,41 [0,36–0,49] | 0,51 [0,46–0,56] | evaluable |
| Z-score robusto (MAD) | 0,67 [0,66–0,69] | 5,0 % | 0,41 [0,36–0,48] | 0,51 [0,47–0,56] | evaluable |
| Isolation Forest | 0,63 [0,62–0,65] | 5,0 % | 0,40 [0,34–0,49] | 0,49 [0,44–0,55] | evaluable |
| LOF | 0,42 [0,37–0,47] | 5,0 % | 0,31 [0,24–0,44] | 0,35 [0,30–0,42] | evaluable |
| KNN (distancia media, k=5) | 0,61 [0,59–0,63] | 5,0 % | 0,39 [0,31–0,50] | 0,48 [0,41–0,55] | evaluable |
| R12 (magnitud del nivel) | 0,28 [0,27–0,29] | 5,0 % | 0,23 [0,16–0,35] | 0,25 [0,21–0,31] | evaluable |

**XM** (una serie y 12 observaciones: con un 5 % de tasa objetivo se esperan 0,6 alertas, por lo que la tasa de alerta real
es 0 % y la precisión sale 100 % por construcción; **no es interpretable**, se conserva solo como evidencia descriptiva):

| Método | Recall macro [IC 95 %] | Tasa de alerta real | Precisión conservadora [IC] | F1 [IC] | Estado |
|---|---|---|---|---|---|
| Cartas I-MR | 0,69 | 0,0 % | — | — | no_interpretable_baja_resolucion |
| Z-score robusto (MAD) | 0,73 | 0,0 % | — | — | no_interpretable_baja_resolucion |
| Isolation Forest | 0,75 | 0,0 % | — | — | no_interpretable_baja_resolucion |
| LOF | 0,78 | 0,0 % | — | — | no_interpretable_baja_resolucion |
| KNN (distancia media, k=5) | 0,80 | 0,0 % | — | — | no_interpretable_baja_resolucion |
| R12 (magnitud del nivel) | 0,40 | 0,0 % | — | — | no_interpretable_baja_resolucion |

*Figura regenerable:* `python desarrollo_puntos/4.3/informe_metricas.py` crea
`figuras/02_f1_por_metodo.png`. Las figuras no se versionan; la tabla anterior contiene sus
valores auditables.

### Diferencias pareadas frente a I-MR

I-MR es el método clásico del proyecto (el que sustituye a la regla estática). Las diferencias usan las mismas categorías
remuestreadas en ambos métodos, por lo que son más informativas que comparar dos intervalos por separado:

| Fuente | Método | Δ recall | Δ F1 frente a I-MR [IC 95 %] | IC excluye 0 | Estado |
|---|---|---|---|---|---|
| EPM | Z-score robusto (MAD) | 0,039 | 0,035 [0,008; 0,052] | sí | evaluable |
| EPM | Isolation Forest | -0,014 | 0,003 [-0,025; 0,037] | no | evaluable |
| EPM | LOF | -0,087 | -0,053 [-0,557; 0,167] | no | evaluable |
| EPM | KNN (distancia media, k=5) | 0,019 | 0,011 [-0,007; 0,041] | no | evaluable |
| EPM | R12 (magnitud del nivel) | -0,272 | -0,171 [-0,300; 0,208] | no | evaluable |
| CHEC | Z-score robusto (MAD) | 0,024 | 0,007 [-0,044; 0,230] | no | evaluable |
| CHEC | Isolation Forest | -0,080 | -0,042 [-0,096; 0,200] | no | evaluable |
| CHEC | LOF | -0,772 | -0,567 [-0,577; -0,549] | sí | degenerado_por_duplicados |
| CHEC | KNN (distancia media, k=5) | -0,033 | -0,021 [-0,080; 0,234] | no | evaluable |
| CHEC | R12 (magnitud del nivel) | -0,349 | -0,207 [-0,245; -0,015] | sí | evaluable |
| SSPD | Z-score robusto (MAD) | 0,007 | 0,004 [-0,036; 0,039] | no | evaluable |
| SSPD | Isolation Forest | -0,030 | -0,017 [-0,078; 0,039] | no | evaluable |
| SSPD | LOF | -0,245 | -0,155 [-0,225; -0,083] | sí | evaluable |
| SSPD | KNN (distancia media, k=5) | -0,057 | -0,033 [-0,099; 0,038] | no | evaluable |
| SSPD | R12 (magnitud del nivel) | -0,387 | -0,259 [-0,325; -0,190] | sí | evaluable |

Con tan pocas categorías (EPM, CHEC) los intervalos son anchos y apenas permiten rechazar nada; con 89 categorías (SSPD)
sí se distingue que LOF y R12 pierden frente a I-MR y que IF, KNN y Z-score no se distinguen de él.
Son 5 métodos × 3 fuentes por configuración y no se aplicó corrección por comparaciones múltiples; léase como exploración.

### 3b. Sensibilidad: EPM con etiquetas canónicas

EPM cambia la escritura de varias etiquetas entre meses (p. ej. «Costo compra: Gm, i» y «Costo Compra: Gm, i», o «Rango 0 - CS» y «0-CS»). Si no se
normalizan, una misma serie económica se parte en varias, y el panel común (series con 61 meses continuos) se reduce. Se repitió el experimento completo con las
11 equivalencias del Hito 2 ([02_catalogo_variantes.csv](../3.3/insumos_hito2/02_catalogo_variantes.csv), aprobadas internamente por el equipo, aplicadas en una copia de trabajo) como una
fuente adicional, `EPM_canonicas`. **No sustituye a EPM**: 4.1, 4.2 y la matriz OE1 usan las etiquetas originales y la variante canónica no existe en 4.2, por lo que no se
compara con él.

| | EPM (originales) | EPM (canónicas) |
|---|---|---|
| Series en el panel común | 27 | 69 |
| Categorías | 5 | 6 |
| Observaciones reales de vigilancia | 324 | 828 |
| Casos inyectados | 1.617 | 4.191 |

F1 a tasa del 5 %, prevalencia supuesta del 5 %, horizonte t:

| Método | F1 EPM (etiquetas originales) | F1 EPM (etiquetas canónicas) [IC] | Δ F1 frente a I-MR (canónicas) [IC] | Estado (canónicas) |
|---|---|---|---|---|
| Cartas I-MR | 0,49 | 0,50 [0,44–0,66] | — | evaluable |
| Z-score robusto (MAD) | 0,52 | 0,55 [0,42–0,82] | 0,042 [-0,136; 0,339] | evaluable |
| Isolation Forest | 0,49 | 0,51 [0,42–0,74] | 0,010 [-0,155; 0,242] | evaluable |
| LOF | 0,44 | 0,41 [0,35–0,47] | -0,099 [-0,257; -0,037] | degenerado_por_duplicados |
| KNN (distancia media, k=5) | 0,50 | 0,52 [0,40–0,82] | 0,014 [-0,159; 0,350] | evaluable |
| R12 (magnitud del nivel) | 0,32 | 0,33 [0,27–0,50] | -0,172 [-0,332; 0,025] | evaluable |

- **El orden y las conclusiones se mantienen.** I-MR, Z-score, Isolation Forest y KNN siguen sin separarse (intervalos solapados; las diferencias pareadas frente a I-MR no excluyen el cero para ningún método evaluable); R12 sigue siendo el más bajo.
- **El F1 sube ligeramente** (entre +0,01 y +0,02 según el método) con más series y casos; no se probó la causa del aumento. Con solo 6 categorías los intervalos siguen siendo anchos.
- **LOF pasa a degenerado también en EPM** (2.484 filas de entrenamiento, 1.220 únicas; 3,3 % de los puntajes reales estallan) y se marca como tal.
- Decidir si estas equivalencias se aceptan como oficiales y si hay que repetir 4.1 y 4.2 con ellas es **decisión del equipo y del director**; mientras tanto el resultado principal sigue usando las etiquetas originales.

## 4. Curvas de detección contra tasa de alerta

*Figura regenerable:* `informe_metricas.py` crea `figuras/01_curvas_deteccion.png`; los datos
auditables permanecen en [curva_deteccion.csv](curva_deteccion.csv).

Datos en [curva_deteccion.csv](curva_deteccion.csv) (40 tasas entre 0,25 y 30 %). Las curvas no tienen IC: son el recall
macro exhaustivo en cada punto. Se omiten los puntos con menos de 5 alertas esperadas y LOF en CHEC.

## 5. Recall por tipo de error

*Figura regenerable:* `informe_metricas.py` crea `figuras/03_recall_por_tipo.png`; los valores
auditables permanecen en [deteccion_por_tipo_tasa_igualada.csv](deteccion_por_tipo_tasa_igualada.csv).

Tabla comparativa con IC 95 % por técnica y tipo de error (horizonte t, tasa 5 %). El resto de tasas y el horizonte
t o t+1 están en [deteccion_por_tipo_tasa_igualada.csv](deteccion_por_tipo_tasa_igualada.csv).

**EPM**

| Tipo | Cartas I-MR | Z-score robusto (MAD) | Isolation Forest | LOF | KNN (distancia media, k=5) | R12 (magnitud del nivel) |
|---|---|---|---|---|---|---|
| decimal_x1000 | 1,00 [1,00–1,00] | 1,00 [1,00–1,00] | 1,00 [1,00–1,00] | 1,00 [1,00–1,00] | 1,00 [1,00–1,00] | 1,00 [1,00–1,00] |
| decimal_div1000 | 1,00 [1,00–1,00] | 1,00 [1,00–1,00] | 1,00 [1,00–1,00] | 1,00 [1,00–1,00] | 1,00 [1,00–1,00] | 0,00 [0,00–0,00] |
| serial_excel_43577 | 1,00 [1,00–1,00] | 1,00 [1,00–1,00] | 1,00 [1,00–1,00] | 1,00 [1,00–1,00] | 1,00 [1,00–1,00] | 1,00 [1,00–1,00] |
| aumento_10pct | 0,61 [0,44–1,00] | 0,71 [0,55–1,00] | 0,61 [0,44–1,00] | 0,07 [0,00–0,33] | 0,70 [0,56–0,99] | 0,09 [0,00–0,13] |
| valor_no_actualizado | 0,00 [0,00–0,00] | 0,00 [0,00–0,00] | 0,02 [0,00–0,05] | 0,08 [0,02–0,23] | 0,04 [0,00–0,11] | 0,03 [0,00–0,05] |
| otra_medida | 0,17 [0,00–0,50] | 0,30 [0,00–0,64] | 0,06 [0,00–0,18] | 0,10 [0,00–0,20] | 0,15 [0,00–0,45] | 0,02 [0,00–0,07] |

**CHEC**

| Tipo | Cartas I-MR | Z-score robusto (MAD) | Isolation Forest | LOF | KNN (distancia media, k=5) | R12 (magnitud del nivel) |
|---|---|---|---|---|---|---|
| decimal_x1000 | 1,00 [1,00–1,00] | 1,00 [1,00–1,00] | 1,00 [1,00–1,00] | n/d | 1,00 [1,00–1,00] | 1,00 [1,00–1,00] |
| decimal_div1000 | 1,00 [1,00–1,00] | 1,00 [1,00–1,00] | 1,00 [1,00–1,00] | n/d | 1,00 [1,00–1,00] | 0,00 [0,00–0,00] |
| serial_excel_43577 | 1,00 [1,00–1,00] | 1,00 [1,00–1,00] | 1,00 [1,00–1,00] | n/d | 1,00 [1,00–1,00] | 1,00 [1,00–1,00] |
| aumento_10pct | 0,76 [0,62–0,80] | 0,92 [0,83–0,94] | 0,39 [0,12–0,50] | n/d | 0,57 [0,37–0,65] | 0,23 [0,13–0,27] |
| valor_no_actualizado | 0,01 [0,00–0,01] | 0,00 [0,00–0,00] | 0,02 [0,00–0,02] | n/d | 0,03 [0,00–0,05] | 0,03 [0,00–0,04] |
| otra_medida | 0,94 [0,92–0,99] | 0,93 [0,91–1,00] | 0,82 [0,81–0,87] | n/d | 0,91 [0,90–0,92] | 0,36 [0,30–0,38] |

**SSPD**

| Tipo | Cartas I-MR | Z-score robusto (MAD) | Isolation Forest | LOF | KNN (distancia media, k=5) | R12 (magnitud del nivel) |
|---|---|---|---|---|---|---|
| decimal_x1000 | 1,00 [1,00–1,00] | 1,00 [1,00–1,00] | 0,99 [0,98–1,00] | 0,63 [0,56–0,71] | 0,98 [0,97–0,99] | 1,00 [1,00–1,00] |
| decimal_div1000 | 1,00 [1,00–1,00] | 1,00 [1,00–1,00] | 0,99 [0,99–1,00] | 0,74 [0,67–0,81] | 0,97 [0,95–0,99] | 0,00 [0,00–0,00] |
| serial_excel_43577 | 0,89 [0,86–0,92] | 0,89 [0,86–0,92] | 0,81 [0,77–0,85] | 0,50 [0,43–0,57] | 0,75 [0,72–0,80] | 0,22 [0,18–0,25] |
| aumento_10pct | 0,16 [0,12–0,21] | 0,22 [0,17–0,28] | 0,14 [0,10–0,19] | 0,09 [0,05–0,13] | 0,12 [0,08–0,17] | 0,06 [0,03–0,09] |
| valor_no_actualizado | 0,02 [0,01–0,03] | 0,00 [0,00–0,00] | 0,03 [0,02–0,04] | 0,04 [0,02–0,06] | 0,03 [0,02–0,05] | 0,05 [0,03–0,08] |
| otra_medida | 0,91 [0,87–0,94] | 0,91 [0,87–0,94] | 0,84 [0,79–0,89] | 0,52 [0,45–0,60] | 0,79 [0,73–0,84] | 0,33 [0,29–0,38] |

## 6. Por qué igualar la tasa (puntos operativos nativos frente a tasa igualada)

Con su umbral nativo cada método alerta con una frecuencia distinta; comparar sus F1 así mezcla la calidad del puntaje con
la elección del umbral. Por ejemplo, el Isolation Forest con percentil 99,5 casi no alerta en EPM y por eso detecta poco en 4.2,
pero con la misma tasa de alerta que las cartas su recall es comparable:

| Fuente | Método | Umbral nativo | Tasa de alerta nativa | Recall nativo | F1 nativo | Recall al 5 % | F1 al 5 % |
|---|---|---|---|---|---|---|---|
| EPM | Cartas I-MR | puntaje>1 (2,66 y 3,267 del plan) | 5,56 % | 0,64 | 0,47 | 0,63 | 0,49 |
| EPM | Z-score robusto (MAD) | |z|>3 | 3,70 % | 0,64 | 0,55 | 0,67 | 0,52 |
| EPM | Isolation Forest | percentil 99,5 de entrenamiento | 0,00 % | 0,05 | 0,09 | 0,62 | 0,49 |
| EPM | R12 (magnitud del nivel) | nivel>10 x mediana | 0,00 % | 0,33 | 0,50 | 0,36 | 0,32 |
| CHEC | Cartas I-MR | puntaje>1 (2,66 y 3,267 del plan) | 0,00 % | 0,64 | 0,78 | 0,78 | 0,58 |
| CHEC | Z-score robusto (MAD) | |z|>3 | 0,00 % | 0,73 | 0,85 | 0,81 | 0,59 |
| CHEC | Isolation Forest | percentil 99,5 de entrenamiento | 0,00 % | 0,55 | 0,71 | 0,70 | 0,54 |
| CHEC | R12 (magnitud del nivel) | nivel>10 x mediana | 0,00 % | 0,33 | 0,50 | 0,44 | 0,37 |
| SSPD | Cartas I-MR | puntaje>1 (2,66 y 3,267 del plan) | 4,60 % | 0,66 | 0,52 | 0,66 | 0,51 |
| SSPD | Z-score robusto (MAD) | |z|>3 | 7,24 % | 0,69 | 0,45 | 0,67 | 0,51 |
| SSPD | Isolation Forest | percentil 99,5 de entrenamiento | 0,47 % | 0,41 | 0,55 | 0,63 | 0,49 |
| SSPD | R12 (magnitud del nivel) | nivel>10 x mediana | 0,13 % | 0,23 | 0,37 | 0,28 | 0,25 |

(Prevalencia supuesta 5 %, horizonte t. Los puntos nativos no llevan IC. En CHEC (y en XM, no mostrado) la tasa nativa de
I-MR y Z-score es 0 % sobre meses reales, de modo que su precisión es 100 % por construcción y su F1 nativo no es comparable
con el igualado. Los puntos nativos de todas las fuentes están en [puntos_operativos_nativos.csv](puntos_operativos_nativos.csv).)

## 7. Lo que no se puede concluir

- **No hay verdad terreno para las alertas reales.** Las inyecciones son artificiales y siguen la mezcla diseñada (seis tipos
  uniformes); no estiman la prevalencia ni el tipo de errores que existe en las fuentes.
- **La precisión depende de la prevalencia supuesta**; el informe no elige una. Con prevalencia baja la precisión de todos los
  métodos cae, porque la tasa de alerta real (5 %) pesa más que los positivos.
- **XM no es evaluable a tasa igualada** (una serie, 12 meses). **CHEC y EPM tienen pocas categorías** (4 y 5): sus IC son
  anchos y los contrastes entre métodos tienen poca potencia.
- **LOF en CHEC está degenerado** por duplicados exactos en el entrenamiento: con más duplicados que vecinos, la densidad local
  diverge y el puntaje estalla (~10⁹–10¹⁰). Se conserva el cálculo y se marca `degenerado_por_duplicados`. Una corrección
  (eliminar duplicados o aumentar vecinos) cambia el significado de densidad y queda como decisión del equipo.
- **El experimento es retrospectivo** (se mira t+1 y los rasgos usan el cambio anterior), válido para auditar datos ya
  publicados y no para vigilancia en tiempo real.
- **Los umbrales por tasa igualada se calibran en los mismos meses reales** donde luego se miden las falsas alertas (sin
  etiquetas, pero sin separación temporal): describe cómo se comportan los métodos a igual tasa, no una tasa futura garantizada.
- **Las equivalencias de etiquetas de EPM son una aprobación interna del equipo**, no una confirmación de EPM (sección 3b).
- **No se aprobó ningún umbral ni método.** Los resultados no confirman que una señal sea un error ni un cambio regulatorio.

## 8. Qué cierra de los pendientes de 4.1

Quedan resueltos aquí: precisión, recall y F1 del Z-score robusto y del Isolation Forest de 4.2 (rasgos logarítmicos);
LOF y KNN, que el plan pedía y no existían; comparación a tasa igualada **sobre las mismas inyecciones** de 4.2 para los seis
métodos; detección en t frente a t o t+1 con ambos horizontes. **Siguen abiertos**: Extended Isolation Forest
(el plan lo condiciona al tiempo), validación externa de alertas reales y aprobación del tratamiento de MAD igual a cero.

## Reproducir y auditar

Desde la raíz del proyecto:

```powershell
python desarrollo_puntos/4.3/experimento_tasa_igualada.py
python desarrollo_puntos/4.3/informe_metricas.py
python -m unittest discover -s desarrollo_puntos/4.3 -p test_metricas.py -v
python desarrollo_puntos/4.3/verificar_resultados.py
```

[configuracion.json](configuracion.json) fija semilla, versiones, definiciones y huellas de las entradas;
[manifiesto_resultados.json](manifiesto_resultados.json) lista las huellas de todos los archivos entregados.
