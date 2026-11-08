# Guía explicativa del proyecto

> **Cómo leer esta guía.** Las secciones 1 a 14 explican la base del proyecto y el Hito 3. Las secciones 15 a 23
> explican el Hito 4 (puntos 4.1 a 4.4): qué se hizo, cómo, por qué se hizo así, qué se encontró y qué sigue
> pendiente. Si solo necesitas saber qué está terminado, ve directo a la [sección 19](#19-están-completos-43-y-44).

## 1. ¿Qué estamos haciendo?

El proyecto construye un framework para evaluar la calidad de datos del sector energético. En
palabras sencillas, queremos responder:

> ¿Podemos confiar en estos datos para analizarlos, compararlos y tomar decisiones?

La calidad de datos no significa solamente que un archivo abra o tenga muchas filas. También hay
que revisar si:

- faltan datos;
- las fechas son válidas;
- los importes tienen formato correcto;
- existen filas duplicadas;
- los códigos y nombres son coherentes;
- los valores están dentro de rangos razonables;
- los datos corresponden con una fuente externa;
- los datos fueron publicados oportunamente;
- las series temporales tienen un comportamiento estable.

El proyecto usa DAMA-DMBOK como marco de dimensiones de calidad y agrega reglas estadísticas para
revisar el comportamiento temporal de las tarifas, costos y demanda eléctrica.

## 2. ¿Qué significa Hito 3?

El Hito 3 es la etapa en la que se formaliza la evaluación. Aquí no se intenta todavía construir
el tablero final ni comparar todos los modelos. Primero se deja claro:

1. qué fuentes se van a estudiar;
2. qué significa cada columna importante;
3. qué reglas se aplican;
4. cómo se calcula cada indicador;
5. cómo se conservan las evidencias;
6. cómo se identifican anomalías;
7. qué resultados son definitivos y cuáles son provisionales.

El Hito 3 funciona como una línea base. El Hito 4 utilizará esa línea base para crear scorecards,
comparar técnicas y hacer análisis de sensibilidad.

## 3. Las cuatro fuentes seleccionadas

### EPM — `sfcd-b3ey`

Es un histórico de tarifas de energía eléctrica. Tiene 3.623 filas y 12 columnas, con información
mensual de tarifas y categorías. Permite construir series por combinación tarifaria y aplicar
cartas de control.

### CHEC — `c698-wqig`

Es un conjunto de costos unitarios y tarifas de energía. Tiene 40.609 filas y 24 columnas, con
cobertura aproximada de 2008 a 2026. Contiene componentes como generación, transmisión,
distribución, comercialización, pérdidas, restricciones y valores agregados.

CHEC es útil para estudiar tarifas, pero varios códigos requieren confirmación documental. Por
eso algunas reglas están marcadas como provisionales.

### Superservicios — `ebby-cjha`

Es información comercial residencial y no residencial. El proyecto conserva un agregado mensual
de 15.075 filas y un detalle comprimido. Permite analizar consumo, facturación y variables
comerciales por periodo y categoría.

### XM/SIMEM — `c1b851`

Es un piloto de demanda eléctrica. La consulta original contiene 119.928 registros horarios y
se derivó una serie mensual de 61 observaciones. No representa todo el mercado XM: corresponde a
un grupo filtrado de agente, mercado y sistema de transmisión.

XM se usa como fuente operativa de demanda, no como fuente tarifaria. Por ello algunas reglas
originalmente diseñadas para tarifas se adaptaron y se marcaron como provisionales.

## 4. ¿Dónde están los archivos?

### Datos originales seleccionados

`fuentes_datos/datos/Datos_seleccionados/`

Contiene los CSV y archivos asociados de EPM, CHEC, SSPD y XM. Estos archivos no deben modificarse
manualmente porque son la base de la trazabilidad.

### Diccionarios

`fuentes_datos/diccionarios/`

Explican las columnas: nombre, tipo de dato, significado, unidad, reglas relacionadas y
limitaciones conocidas.

### Catálogos

`fuentes_datos/catalogos/`

Contienen equivalencias, dominios y definiciones operativas. Un catálogo sirve para saber, por
ejemplo, qué códigos son válidos o qué nombre corresponde a un código.

### Fichas de caracterización

`desarrollo_puntos/3.2/`

Cada ficha describe una fuente: quién la publica, qué contiene, cuál es su cobertura, quién podría
usar los datos, cuáles son sus variables críticas y qué limitaciones tiene.

### Resultados del Hito 3

Los resultados se distribuyen según las actividades del plan:

- `desarrollo_puntos/3.1/`: matriz OE1, indicadores y evidencia de medición.
- `desarrollo_puntos/3.2/`: fichas y perfiles de caracterización.
- `desarrollo_puntos/3.3/`: adaptadores, revisión de reglas e informe de diferencias.
- `desarrollo_puntos/3.4/`: evaluación de fuentes CREG y alternativas.
- `desarrollo_puntos/3.5/`: cartas logarítmicas y señales.
- `desarrollo_puntos/3.6/`: trazabilidad y reproducibilidad.
- `desarrollo_puntos/3.7/`: cuarentena y bootstrap.

El [índice general](desarrollo_puntos/3_documentacion_general/README.md) reúne enlaces,
criterios y el inventario de movimientos. El plan, cierre y pendientes generales están
en esa misma carpeta. Los resultados históricos del Hito 2 se conservan como insumos en
`desarrollo_puntos/3.3/insumos_hito2/`.

### Resultados del Hito 4

Cada punto del plan tiene su carpeta, con un README que indica qué archivo contiene qué:

- `desarrollo_puntos/4.1/`: Z-score robusto, Isolation Forest con entrenamiento solo en referencia y
  calibración a tasa de alerta igualada.
- `desarrollo_puntos/4.2/`: análisis de sensibilidad. Informe en
  [INFORME_SENSIBILIDAD.md](desarrollo_puntos/4.2/INFORME_SENSIBILIDAD.md).
- `desarrollo_puntos/4.3/`: precisión, recall y F1 a tasa de alerta igualada. Informe en
  [INFORME_METRICAS.md](desarrollo_puntos/4.3/INFORME_METRICAS.md).
- `desarrollo_puntos/4.4/`: regla de alerta sistémica, catálogo y contraste con publicaciones de EPM. Informe en
  [INFORME_REGLA_SISTEMICA.md](desarrollo_puntos/4.4/INFORME_REGLA_SISTEMICA.md). La subcarpeta
  `evidencia_externa/` guarda los PDF oficiales de EPM que se leyeron.

## 5. Las ocho dimensiones de calidad

La matriz revisa las ocho dimensiones exigidas por el proyecto:

| Dimensión | Pregunta sencilla |
|---|---|
| Completitud | ¿Están presentes los datos que deberían existir? |
| Validez | ¿Los valores cumplen el formato y dominio permitido? |
| Unicidad | ¿Hay duplicados o varias filas para la misma clave? |
| Consistencia | ¿Los valores y relaciones son coherentes entre sí? |
| Integridad | ¿Se conservan las relaciones y el contrato estructural? |
| Exactitud | ¿El dato coincide con una fuente confiable? |
| Oportunidad | ¿El dato estuvo disponible dentro del plazo esperado? |
| Razonabilidad | ¿El comportamiento del dato es esperable y estable? |

Una fuente puede tener una dimensión aplicable aunque su resultado sea provisional. Si el concepto
no existe en el esquema, se marca `no_aplica`. Si existe pero no hay evidencia para calcularlo, se
marca `no_medible`.

## 6. Las reglas y los controles

La matriz contiene 19 controles para cada fuente, es decir, 76 filas en total. Incluye las reglas
R01–R12 y controles complementarios:

- R01–R02: periodos informados y válidos;
- R03: importes numéricos y finitos;
- R04–R05: duplicados y multiplicidad de claves;
- R06: representación canónica de categorías;
- R07: signos y rangos por concepto;
- R08–R09: relaciones entre tarifas y categorías;
- R10: importes requeridos disponibles;
- R11: detección de posibles fechas almacenadas como importes;
- R12: prevalencia de magnitudes atípicas;
- INT01–INT02: integridad estructural y referencial;
- EXA01: contraste documental de exactitud;
- OPO01: disponibilidad dentro del plazo;
- MAP01: equivalencias de etiquetas;
- DEF01: documentación de variables críticas;
- CART01: señales de cartas de control.

Cada control tiene población, numerador, denominador, fórmula, unidad, umbral, severidad,
frecuencia, responsable, aplicabilidad y nota metodológica.

Por ejemplo, R01 calcula:

`filas con periodo informado / total de filas × 100`

El resultado es un porcentaje. El porcentaje no se interpreta correctamente si no se conoce qué
filas entraron al denominador.

## 7. ¿Qué significa que un resultado sea provisional?

Los estados de la matriz son importantes:

- `medido`: el control se pudo calcular con la definición actual sin supuestos adicionales.
- `provisional`: hay un valor, pero falta aprobar una decisión documental o de negocio.
- `provisional_interno`: el cálculo depende de una decisión interna todavía no aprobada.
- `provisional_proxy`: se utilizó una medida indirecta porque no existe la evidencia ideal.
- `no_medible`: el control está definido, pero no hay datos suficientes para calcularlo.
- `no_aplica`: el concepto no existe en esa fuente.

Estos estados evitan presentar una cifra provisional como si fuera una verdad definitiva.

## 8. Cartas de control

Una carta de control observa una serie temporal y ayuda a detectar cambios inusuales. En este
proyecto se usan cartas I-MR:

- carta I: observa los valores individuales;
- carta MR: observa el cambio entre valores consecutivos.

Se utilizaron cambios logarítmicos para comparar variaciones relativas. Esto es más adecuado que
comparar únicamente diferencias absolutas cuando las tarifas o demandas tienen escalas distintas.

Una señal significa que una observación merece revisión. No significa automáticamente que el dato
sea incorrecto.

Las cartas se guardan por fuente en:

`desarrollo_puntos/3.5/EPM/`, `CHEC/`, `SSPD/` y `XM/`.

## 9. Cuarentena

La cuarentena es una lista separada de registros que deben excluirse del cálculo de límites porque
ya existe evidencia de que pueden distorsionar la carta.

La cuarentena no borra filas del dataset y no interpola valores. Solo evita que esos cambios se
usen para calcular los límites estadísticos. El registro original permanece intacto.

EPM tiene una cuarentena trazable con 9 registros. Para las demás fuentes se aplicó una política
conservadora y no se identificaron valores que justificaran excluirlos automáticamente.

## 10. Trazabilidad

La trazabilidad permite responder:

> ¿De qué archivo salió este resultado y cómo sé que no cambió?

Para cada fuente se conserva:

- SHA-256 del archivo;
- tamaño y número de filas;
- número de columnas;
- fecha de ejecución;
- clave estable de contenido;
- identificador de cada fila;
- vínculo entre hallazgos y filas originales.

El manifiesto está en:

`desarrollo_puntos/3.6/trazabilidad/manifiesto_ejecucion.json`

El SHA-256 es una huella digital del archivo. Si cambia un carácter, la huella normalmente cambia.
No es un método de cifrado ni muestra el contenido del archivo.

## 11. Bootstrap

El bootstrap se usa para estimar la variabilidad de la tasa de señales de CART01. En lugar de
tratar cada fila horaria o mensual como independiente, se remuestrean series completas dentro de
su categoría.

La ejecución actual usa:

- 2.000 repeticiones;
- semilla `20261105`;
- 105 categorías;
- intervalos de confianza del 95 %.

Resultados por fuente:

- EPM: 8 categorías y 60 series;
- CHEC: 4 categorías y 276 series;
- SSPD: 92 categorías y 361 series;
- XM: 1 categoría y 1 serie.

Si una categoría tiene una sola serie, el intervalo resulta degenerado. Eso no es un error del
programa; significa que no hay suficiente variación entre series para estimar incertidumbre.

## 12. Qué se ha validado técnicamente

Se ejecutaron correctamente:

```bash
python3 desarrollo_puntos/3.1/medir_matriz_oe1.py
python3 desarrollo_puntos/3.7/bootstrap_categorias.py
python3 desarrollo_puntos/3.6/trazabilidad.py
```

La ejecución genera:

- 76 filas de matriz;
- 105 resultados de bootstrap;
- manifiesto de trazabilidad para cuatro archivos fuente.

## 13. Qué todavía no está aprobado

Los pendientes están reunidos en:

[PENDIENTES_APROBACION_HITO3.md](desarrollo_puntos/3_documentacion_general/PENDIENTES_APROBACION_HITO3.md)

En resumen:

- nombres de los responsables y aprobador final;
- umbrales y severidad;
- catálogos oficiales de CHEC;
- fuente y muestra para exactitud;
- plazos oficiales para oportunidad;
- segunda descarga independiente;
- decisión final sobre R10, R12 y CART01.

No se deben inventar estas aprobaciones. Mientras no existan, los resultados correspondientes
deben permanecer identificados como provisionales, proxy o pendientes.

## 14. Qué significa estar listos para el Hito 4

> Esta sección se escribió al cerrar el Hito 3. El estado actual del Hito 4 está en las secciones 15 a 22.

Estamos técnicamente preparados para iniciar el Hito 4 porque ya existe una línea base comparable.
El Hito 4 debe construir:

1. scorecards por fuente y dimensión;
2. comparación de técnicas bajo el mismo protocolo;
3. análisis de sensibilidad;
4. comparación con procedimientos tradicionales;
5. conclusiones usando intervalos y estados de evidencia.

El Hito 4 no debe ocultar los estados provisionales ni comparar porcentajes sin revisar población,
unidad, aplicabilidad y evidencia.

## 15. Qué se ha hecho del Hito 4

El Hito 4 compara técnicas bajo el mismo protocolo. Su plan tiene seis puntos:

| Punto | Qué pide el plan | Estado | Dónde |
|---|---|---|---|
| 4.1 Técnicas adicionales | Z-score robusto, LOF o KNN, Extended Isolation Forest | **Parcial.** Z-score robusto e Isolation Forest en 4.1; LOF y KNN se agregaron en 4.3; Extended IF no se hizo | `4.1/`, `4.3/` |
| 4.2 Sensibilidad | Ventanas, constantes, percentiles, R12, detección en t y t+1, regla sistémica | **Hecho** | `4.2/` |
| 4.3 Métricas completas y honestas | Precisión, recall y F1 a tasa igualada, curvas, pruebas por tipo, sorteo sin reemplazo | **Hecho, con límites** (sección 19) | `4.3/` |
| 4.4 Regla de alerta sistémica | Definir X, calibrarlo con tres meses, contrastar con la CREG y EPM | **Hecho, con pendientes** (sección 19) | `4.4/` |
| 4.5 Scorecard por dimensión | Tabla única con umbral y estado por indicador y fuente | **Solo provisional** (generado en 4.1) | `4.1/` |
| 4.6 Resultados por nivel y costo de cómputo | Separar el Nivel I de los niveles II a IV; tiempos por etapa | **No iniciado.** Los tiempos por etapa ya se guardan en `ejecuciones.csv` de 4.2 y 4.3 | — |

Los Hitos 5 (artefacto: paquete, contenedor, tablero) y 6 (validación y sustentación) todavía no tienen trabajo.

## 16. Hito 4.1 y 4.2 en lenguaje sencillo

### El protocolo común

Todas las técnicas se miden igual, para que la comparación sea justa:

1. Se trabaja con **cambios logarítmicos** mes a mes (una variación relativa, no una diferencia en pesos).
2. Los **36 primeros cambios** de cada serie son la **referencia**: lo que se considera “normal”.
3. Los **12 siguientes** son la **vigilancia**: ahí se busca lo anormal.
4. Solo se comparan **meses consecutivos**; si falta un mes no se inventa ni se cruza el hueco.

### Qué es cada técnica

- **Carta I-MR.** Marca un mes si su cambio cae fuera de unos límites calculados con el promedio de los cambios de
  referencia (carta I, constante 2,66) o si el salto respecto al mes anterior es demasiado grande (carta MR,
  constante 3,267). Es el método estadístico clásico de control de procesos.
- **Z-score robusto.** Mide cuántas “desviaciones robustas” se aleja un cambio de lo habitual. Usa la **mediana** y el
  **MAD** (desviación absoluta de la mediana) en lugar del promedio y la desviación estándar, porque unos pocos valores
  extremos no los distorsionan. Fórmula: `0,6745 × (cambio − mediana) / MAD`. Señal si el valor absoluto supera 3.
- **Isolation Forest.** Un conjunto de árboles que intenta “aislar” cada observación. Las más fáciles de aislar son las
  más raras. Se entrena **solo con la referencia** y se evalúa en la vigilancia, para que no “vea el futuro”.
- **LOF y KNN** (agregados en 4.3). Comparan cada observación con las observaciones normales más cercanas: si está muy
  lejos de ellas, es rara.
- **R12.** No es una técnica estadística sino una regla: marca un valor si supera 5, 10 o 20 veces la mediana de su serie.

### Qué mostró la sensibilidad (4.2)

Se repitió el análisis variando una cosa a la vez: ventana de referencia (24, 36 y 48 cambios), constantes de las cartas,
percentil del Isolation Forest (99 y 99,5), factor de R12 (5, 10 y 20), detección en el mes del error o hasta el
siguiente, y el efecto de la regla sistémica. En total fueron 22 escenarios. Dos aprendizajes:

- **SSPD no permite ventana de 48**: necesitaría 61 meses y solo hay 59. Se declara “no evaluable” en lugar de recortar.
- **Una tasa de alerta baja no significa mejor calidad.** Un método que casi no alerta también detecta poco.

## 17. Hito 4.3: métricas completas y honestas

### La pregunta

¿Qué técnica detecta mejor los errores, **en igualdad de condiciones**? Hasta 4.2 cada método alertaba con su propia
frecuencia, así que no se podían comparar de forma justa. Además faltaban precisión y F1, que el anteproyecto promete.

### Palabras que conviene entender

- **Tasa de alerta:** de cada 100 meses reales vigilados, cuántos dispara un método. Ejemplo: 5 de cada 100 = 5 %.
- **Tasa de alerta igualada:** se ajusta el umbral de cada método para que todos alerten lo mismo (por ejemplo, 5 %) sobre
  los datos reales. Así solo pueden diferenciarse por **cuánto detectan de lo inyectado**.
- **Error inyectado:** se altera a propósito un valor conocido para ver si el método lo atrapa. Hay seis tipos: decimal ×1000,
  decimal ÷1000, serial de fecha de Excel (43.577), aumento del 10 %, valor no actualizado (igual al mes anterior) y valor
  de otra medida.
- **Recall (sensibilidad):** de los errores inyectados, qué fracción se detectó.
- **Precisión:** de las alertas disparadas, qué fracción corresponde a un error de verdad.
- **F1:** un solo número que combina precisión y recall (media armónica).
- **Prevalencia:** qué proporción de los datos tiene errores. **No se conoce.** La precisión depende de ella: con pocos
  errores reales, hasta un buen detector acierta poco entre sus alertas. Por eso se reporta con prevalencias supuestas del
  1, 5 y 10 %.
- **“Alerta sin error conocido”:** en los datos reales no hay etiquetas que confirmen cuáles alertas son falsas. Por honestidad
  no se las llama “falsas alarmas”: son alertas cuyo origen no está confirmado.
- **Recall macro:** promedio de los recall de los seis tipos, con el mismo peso, para que ningún tipo domine.
- **Bootstrap por categoría:** para medir la incertidumbre se remuestrean categorías completas (no filas sueltas), porque las
  series de una misma categoría se parecen entre sí y no son independientes.
- **Sorteo sin reemplazo:** al elegir los meses de prueba, un mes no se puede repetir dentro de la misma serie.

### Cómo se hizo, paso a paso

1. Se tomaron los mismos datos, modelos y errores inyectados de 4.2 (EPM 27 series, CHEC 276, SSPD 321 y XM 1).
2. Cada uno de **seis métodos** (cartas I-MR, Z-score robusto, Isolation Forest, LOF, KNN y R12) produce un **puntaje continuo**:
   cuanto más alto, más anómalo.
3. Para cada fuente se fija el umbral de cada método de modo que deje por encima el 1, 2, 5 o 10 % de los meses reales.
4. Se cuenta qué fracción de los errores inyectados supera ese umbral: recall por tipo y recall macro.
5. Con el recall y la tasa de alerta se calcula la precisión para cada prevalencia supuesta, y de ahí el F1.
6. La incertidumbre (intervalo de confianza al 95 %) sale de 1.000 remuestreos por categorías.
7. Como comprobación, se hizo un **sorteo sin reemplazo** (500 réplicas, 3 meses distintos por serie) que reproduce el
   cálculo completo con una diferencia máxima de 6 puntos porcentuales (EPM).
8. Un verificador recalcula los umbrales, las detecciones, la precisión y el F1 desde los puntajes guardados y los compara con
   las tablas.

### Por qué se hizo así

- **Igualar la tasa** evita la trampa de comparar un método que alerta mucho con otro que alerta poco.
- **Puntajes continuos** hacen posible esa igualación; con reglas de sí/no no se podría.
- **Prevalencias supuestas** en lugar de una sola prevalencia inventada: así no se fabrica una precisión que los datos no
  respaldan.
- **Bootstrap por categorías** corrige el problema señalado en la revisión del Hito 2: contar series casi idénticas como
  independientes hace que los intervalos parezcan más estrechos de lo que son.
- **Sorteo sin reemplazo y denominadores a la vista** responden a la observación de esa revisión sobre meses repetidos y
  números de pruebas distintos por tipo.
- **LOF y KNN** se agregaron porque el plan los pedía en 4.1 y no existían; sin ellos la comparación quedaba incompleta.

### Resultados (F1 a tasa de alerta del 5 %, prevalencia supuesta del 5 %, detección en el mes del error)

| Método | EPM | CHEC | SSPD |
|---|---|---|---|
| Cartas I-MR | 0,49 | 0,58 | 0,51 |
| Z-score robusto | 0,52 | 0,59 | 0,51 |
| Isolation Forest | 0,49 | 0,54 | 0,49 |
| LOF | 0,44 | no aplicable (degenerado) | 0,35 |
| KNN | 0,50 | 0,56 | 0,48 |
| R12 | 0,32 | 0,37 | 0,25 |

Cómo leerlo:

- **I-MR, Z-score robusto, Isolation Forest y KNN no se distinguen de forma consistente:** sus intervalos se solapan. De
  14 comparaciones pareadas frente a I-MR, solo una excluye el cero a favor de otro método (Z-score en EPM, +0,035).
- **LOF y R12 rinden menos que las cartas**, con claridad en SSPD (89 categorías, intervalos estrechos). En EPM y CHEC hay
  pocas categorías (5 y 4) y los intervalos son demasiado anchos para afirmarlo.
- **Los errores groseros se detectan casi siempre** (decimal ×1000, ÷1000 y serial de Excel, con recall cercano a 1 en EPM y CHEC).
  **El aumento del 10 % solo se detecta bien en EPM y CHEC** (0,6 a 0,9 con I-MR o Z-score) y poco en SSPD (0,1 a 0,2).
- **Ningún método estadístico detecta el “valor no actualizado”** (recall entre 0,00 y 0,08): un valor repetido no es un cambio
  raro. Se atrapa con una regla, no con una carta. Es un argumento a favor del framework “reglas + cartas”.

### Sensibilidad a las etiquetas de EPM

EPM escribe de varias formas la misma etiqueta según el mes (por ejemplo “Costo compra: Gm, i” y “Costo Compra: Gm, i”). Sin normalizarlas,
una misma serie económica se parte y el panel común de EPM queda en **27 series**. Se repitió todo el experimento con las 11 equivalencias
aprobadas internamente en el Hito 2 como una fuente adicional (`EPM_canonicas`): el panel pasa a **69 series** y 4.191 casos. Resultado:
**las conclusiones no cambian.** I-MR, Z-score, Isolation Forest y KNN siguen sin separarse (F1 entre 0,50 y 0,55, antes entre 0,49 y 0,52),
R12 sigue siendo el más bajo y LOF pasa también a degenerado. No sustituye al resultado principal: 4.1, 4.2 y la matriz de indicadores usan las
etiquetas originales, y aceptar las equivalencias como oficiales es una decisión del equipo y del director.

### Límites que hay que decir en voz alta

- **XM** tiene una serie y 12 observaciones: a tasa del 5 % se esperan 0,6 alertas. Sus resultados son descriptivos y **no
  interpretables** (su precisión sale 100 % solo porque no hay alertas).
- **LOF en CHEC es numéricamente degenerado**: el entrenamiento tiene 9.936 filas pero solo 2.126 distintas, y LOF se rompe
  con duplicados exactos. Se conserva el cálculo marcado como degenerado, no se oculta. Con etiquetas canónicas le pasa lo mismo a EPM.
- Los umbrales se calibran con los mismos meses reales donde luego se mide la tasa de alerta (sin etiquetas, pero sin
  separación temporal).
- El experimento es **retrospectivo** (mira un mes adelante): sirve para auditar datos ya publicados, no para vigilar en
  tiempo real.
- Los errores son inyecciones artificiales; no estiman qué errores existen realmente en las fuentes.

## 18. Hito 4.4: regla de alerta sistémica

### La pregunta

Cuando **muchas series cambian el mismo mes**, lo más probable es que haya cambiado algo general (una resolución, una nueva
publicación de tarifas) y no que haya miles de errores de captura simultáneos. La regla del plan dice: *“si más de X % de las
series alertan en el mismo mes, se clasifica como cambio regulatorio y no como error de dato”*. Hay que definir X, calibrarlo
con febrero de 2020 (51 de 83 series), julio de 2020 (24) y julio de 2021 (18), y contrastarlo con la CREG y con EPM.

### Palabras que conviene entender

- **Fracción mensual:** series con alerta / series evaluadas ese mes.
- **Candidato sistémico:** mes cuya fracción supera X (desigualdad estricta) y en el que se evaluaron al menos 10 series. Se
  llama *candidato* porque confirmarlo exige comparar con la publicación real. **Las alertas no se borran**: pasan a una cola
  de revisión.
- **Ventana móvil:** para evaluar el mes *m* se usan los 24 o 36 cambios anteriores, nunca los posteriores. Así se puede
  evaluar cualquier mes sin “mirar el futuro”.
- **Componente:** cada pieza del costo unitario de EPM (compra de energía, transporte STN, distribución SDL, comercialización,
  pérdidas, restricciones). Las series de EPM están repetidas por columna y por nivel de tensión, así que un solo componente
  puede mover varias series a la vez.
- **Amplitud:** cuántos componentes distintos alertan un mes. Distingue un cambio general (muchos componentes) de uno que
  afecta a una pieza.
- **Etiquetas canónicas:** EPM escribe de varias formas la misma etiqueta según el mes (por ejemplo, “Costo compra: Gm, i” y
  “Costo Compra: Gm, i”). Las equivalencias aprobadas internamente en el Hito 2 las reúnen en una sola.
- **Banda factible:** el rango de X que captura los tres meses del plan sin marcar ningún otro. Si no existe, X no se puede
  fijar con esos tres meses.
- **Enmascaramiento:** errores reales que la regla escondería al reclasificarlos como “sistémicos”.

### Cómo se hizo, paso a paso

1. **Se reprodujeron las cifras del plan** desde los archivos del Hito 2: 51/83 (61,4 %), 24/83 (28,9 %) y 18/83 (21,7 %).
2. **Se aplicó el protocolo del proyecto** (cambios logarítmicos, ventana móvil de 24 y 36, métodos I-MR y MAD 3σ), porque las
   cifras del Hito 2 vienen de otro protocolo (límites fijos y diferencias absolutas).
3. **Se probaron nueve variantes** de EPM (etiquetas canónicas y originales, dos ventanas, dos métodos, más la reproducción del
   Hito 2). Para cada una se midió la banda factible y qué pasa con cada X entre 5 % y 80 %.
4. **Se midió el costo**: qué fracción de las alertas reales se reclasifica y qué fracción de los errores inyectados (tomados
   de 4.2) quedaría escondida.
5. **Se generó el catálogo** de meses candidatos para EPM, CHEC y SSPD (227 filas), con su fracción y su amplitud.
6. **Se contrastó con fuentes externas**: se leyeron los seis PDF oficiales de tarifas de EPM (enero, febrero, junio y julio
   de 2020; junio y julio de 2021); se verificó que coinciden con el CSV en las 108 celdas comparadas y que la suma de
   componentes reproduce el costo unitario publicado; y se leyeron las resoluciones CREG 012, 058 y 104 de 2020 (la 015 de
   2018, de forma parcial).

### Por qué se hizo así

- **Reproducir primero** las cifras del plan evita discutir un número que no se pudo rehacer.
- **Varias variantes** porque con solo tres meses un resultado puede deberse al protocolo y no al fenómeno.
- **Etiquetas canónicas como variante principal** porque sin ellas la misma serie se parte y los denominadores mensuales cambian.
- **Reportar el costo de enmascarar** porque una regla que reclasifica demasiado esconde errores reales.
- **Evidencia externa guardada** (PDF con su huella digital) para que el contraste se pueda auditar.

### Resultados

| Pregunta | Respuesta |
|---|---|
| ¿Se reproducen 51/24/18? | Sí, exactamente, desde los archivos del Hito 2 |
| ¿Se mantienen con el protocolo logarítmico? | **Solo febrero de 2020** (49 % a 67 % de las series en todas las variantes). Julio de 2020 (6 % a 44 %) y julio de 2021 (0 % a 16 %) dependen de la ventana, el método y las etiquetas |
| ¿Existe un X que capture los tres meses sin marcar otros? | **No, en ninguna variante.** Con las cifras del Hito 2, abril de 2020 (24,1 %) supera a julio de 2021 (21,7 %) |
| ¿Los tres meses son del mismo tipo? | No: involucran 11, 5 y 3 componentes tarifarios |
| ¿Qué X se propone? | **25 %, como valor de trabajo, sin aprobar** |
| ¿Cuánto cuesta X = 25 %? | Esconde como máximo 8,2 % de los errores individuales inyectados (con X = 10 % llega a 26,2 %), pero esconde 80 % a 100 % de los errores colectivos |
| ¿Funciona en otras fuentes? | En CHEC, 270 de 270 series alertan en febrero de 2020; en SSPD la fracción mensual máxima es 14,4 % y con X = 25 % la regla no se activa |
| ¿Qué muestran las publicaciones de EPM? | Los tres meses son **cambios publicados, no errores de captura**: febrero es amplio (11 componentes); julio de 2020 y julio de 2021 involucran pocos componentes |

**Por qué 25 %:** en las variantes con etiquetas canónicas solo marca meses del plan; un solo componente aunque alertara con
todas sus series aportaría como máximo 13 % de la fracción, y 25 % lo supera; y su costo para errores individuales es bajo. Es un
valor de arranque, no una calibración cerrada.

### Qué mostraron las publicaciones de EPM

Variación publicada de cada componente (nivel de tensión I) frente a las alertas:

| Componente | Ene → feb 2020 | Jun → jul 2020 | Jun → jul 2021 |
|---|---|---|---|
| Costo G,T y pérdidas | **+25,8 %** (alerta en todas las series) | 0,0 % | −4,2 % |
| Distribución (SDL) | +7,8 % (alerta en parte de las series) | +5,2 % (alerta con I-MR) | −2,1 % (alerta solo en el Hito 2) |
| Compra de energía | +8,4 % (no alerta) | +0,4 % | −3,0 % |
| Transporte STN | +5,3 % (no alerta) | **−20,3 %** (alerta con MAD) | **−13,3 %** (alerta con I-MR, las 15 series) |
| Comercialización | +0,9 % | +7,2 % (alerta con MAD) | +3,0 % |
| Restricciones | cruza cero (−0,25 → 2,03) | +40,9 % (no alerta) | **+147,0 %** (11,50 → 28,40; alerta solo en el Hito 2) |

Lectura prudente:

- Las alertas caen en componentes que **sí cambiaron según la publicación oficial**, y como los valores del CSV coinciden con
  esa publicación, **no son errores de captura**. Son cambios publicados. Esa es justo la distinción que la regla busca.
- **Qué componente alerta en julio de 2020 depende del método**: con I-MR solo la distribución, con MAD el transporte STN y la
  comercialización, en el Hito 2 los tres.
- **Julio de 2021 es un cambio de un solo componente, no de todo el mercado.** El transporte STN baja 13,3 % y son justo sus 15 series
  las que alertan con I-MR. Con X = 25 % ese mes no es “sistémico”, lo cual es coherente: un solo componente no debe reclasificarse
  como cambio de mercado, aunque sí es un cambio publicado y no un error.
- **La hipótesis del Hito 2 solo se respalda en parte.** La revisión atribuía febrero de 2020 “probablemente” a los cargos de
  distribución de la CREG 015 de 2018. La distribución sube 7,8 %, pero el costo de pérdidas sube 25,8 % y el de compra 8,4 %: el
  cambio no se limita a la distribución.
- La **Resolución CREG 012 de 2020** (opción tarifaria; expedida el 6 de febrero y publicada el 17 de febrero de 2020) cita la
  015 de 2018 como motivo, pero no fija un mes de aplicación para EPM. Los encabezados de las publicaciones de junio y julio de
  2020 sí la citan y traen una fila nueva “CU CREG 012 de 2020”; los de enero y febrero no. Es coherente con que la opción
  tarifaria sostuviera la tarifa aplicada, pero **no se probó el mecanismo**.
- La **Resolución CREG 058 de 2020** (14 de abril; Diario Oficial del 15 de abril de 2020) fija pagos diferidos de las facturas de
  abril a junio por la emergencia sanitaria, permite cobrar menos que el máximo aprobado en transmisión, distribución y
  comercialización, y remite a la opción tarifaria. La **104 de 2020** (5 de junio) impide que el consumo de subsistencia de los
  estratos 1 y 2 varíe con el IPC durante la emergencia. Ninguna fija los valores de los componentes de EPM: **explican el contexto,
  no los cambios observados**. De la **015 de 2018** solo se verificó de forma literal que se publicó el 3 de febrero de 2018 y su
  objeto; sus reglas de aplicación de los cargos no se pudieron citar como texto.

### Límites que hay que decir en voz alta

- **“Candidato sistémico” no es “cambio regulatorio confirmado”.** El contraste con las publicaciones respalda que febrero y julio
  de 2020 y julio de 2021 son cambios publicados; falta confirmar con EPM o la CREG la causa de cada uno.
- **Tres meses no bastan para calibrar X.** Es una decisión que debe aprobar el director, con este análisis como insumo.
- Las series **no son independientes**; una fracción alta puede ser un solo componente. Por eso se reporta la amplitud.
- El costo de enmascaramiento sale de inyecciones artificiales de 4.2, no se recalculó con la ventana móvil.
- Las equivalencias de etiquetas son una aprobación interna del equipo, no una confirmación de EPM.

## 19. ¿Están completos 4.3 y 4.4?

**Sí en lo que se puede hacer con los datos y archivos disponibles; no en su totalidad.** Quedan pendientes que dependen de
decisiones, de documentos que no se localizaron o de etapas posteriores del plan.

### 4.3

| Elemento del plan | Estado |
|---|---|
| Precisión, recall y F1 a tasa de alerta igualada | **Hecho** (tres fuentes interpretables; XM solo descriptivo) |
| Curvas de detección contra tasa de alerta por método | **Hecho** |
| Pruebas por tipo con su denominador | **Hecho** |
| Meses distintos sorteados, sin reemplazo | **Hecho** |
| Tabla comparativa con IC 95 % por técnica y tipo de error | **Hecho** (XM sin IC: una sola categoría) |
| LOF o KNN (pendiente de 4.1) | **Hecho**; LOF degenerado en CHEC (y en EPM con etiquetas canónicas) |
| Sensibilidad a las etiquetas de EPM | **Hecho**: las conclusiones no cambian |
| Extended Isolation Forest (pendiente de 4.1) | **No hecho** (el plan lo condiciona al tiempo) |
| Validación de las alertas reales con una fuente externa | **No hecho** (corresponde al Hito 6) |
| Aprobación de umbrales y de la prevalencia | **No hecho** (depende del director) |

### 4.4

| Elemento del plan | Estado |
|---|---|
| Formalizar e implementar la regla | **Hecho** |
| Calibrar X con feb-2020, jul-2020 y jul-2021 | **Hecho como análisis, sin valor único**: no hay banda factible; se propone 25 % sin aprobar |
| Catálogo de alertas sistémicas | **Hecho** (227 filas) |
| Contrastar con publicaciones tarifarias de EPM | **Hecho**: enero, febrero, junio y julio de 2020 y junio y julio de 2021 (seis PDF) |
| Contrastar con resoluciones de la CREG | **Parcial**: leídas la 012, 058 y 104 de 2020; la 015 de 2018 solo en parte; la 152 de 2020 y la 003 de 2021 (citadas en los encabezados de 2021) no se consultaron |
| Consulta formal a EPM o a la CREG | **No hecho** (el plan la ubica en el Hito 6) |

## 20. Hallazgos que afectan al trabajo anterior

1. **Las etiquetas de EPM fragmentan las series.** Sin normalizarlas hay 266 series; con las equivalencias del Hito 2, 200.
   En el panel común de 4.3 pasan de 27 a 69 series. 4.1 y 4.2 usaron las etiquetas originales y no se modificaron; 4.3 se
   repitió como sensibilidad y sus conclusiones no cambian. Falta decidir si se repiten 4.1 y 4.2.
2. **Febrero de 2020 también aparece en CHEC** (270 de 270 series). Es evidencia de que el fenómeno no es exclusivo de EPM.
3. **La hipótesis de la CREG 015 de 2018 se respalda solo en parte** (sección 18).
4. **Las cartas I-MR de ventana móvil pierden sensibilidad después de un salto grande**, porque la referencia posterior
   incluye ese salto. Puede explicar por qué I-MR no señala julio de 2020 mientras MAD, más robusto, sí. Es una hipótesis que
   no se probó.
5. **Un valor repetido no lo detecta ninguna carta.** Refuerza la idea de combinar reglas y cartas.

## 21. Cómo reproducir y verificar el Hito 4

Desde la raíz del proyecto:

```powershell
# 4.3
python desarrollo_puntos/4.3/experimento_tasa_igualada.py
python desarrollo_puntos/4.3/informe_metricas.py
python -m unittest discover -s desarrollo_puntos/4.3 -p test_metricas.py -v
python desarrollo_puntos/4.3/verificar_resultados.py

# 4.4
python desarrollo_puntos/4.4/calibrar_regla_sistemica.py
python desarrollo_puntos/4.4/informe_regla_sistemica.py
python -m unittest discover -s desarrollo_puntos/4.4 -p test_regla_sistemica.py -v
python desarrollo_puntos/4.4/verificar_resultados.py
```

Qué comprueban las verificaciones:

- que los datos de entrada y los PDF conservan su huella digital (SHA-256);
- que las cifras de las tablas se recalculan por otra vía (4.3 desde los puntajes guardados; 4.4 con una implementación distinta
  de la usada para generarlas);
- que las banderas de 4.3 coinciden con las de 4.2 caso por caso;
- que las cifras 51, 24 y 18 del plan se reproducen;
- que la transcripción de los PDF coincide con el CSV y con la suma de componentes;
- pruebas automáticas: 12 en 4.3 y 10 en 4.4 (entre otras, que el futuro no influye en las señales pasadas y que el sorteo
  nunca repite un mes dentro de una serie).

Ejecutar dos veces da las mismas cifras; solo cambian los tiempos de cómputo guardados.

## 22. Qué todavía no está aprobado o resuelto en el Hito 4

1. **Valor de X** de la regla sistémica (se propone 25 %, sin aprobar).
2. **Prevalencia de errores** a usar para presentar la precisión.
3. **Repetir 4.1 y 4.2 con etiquetas canónicas** de EPM (4.3 ya se repitió) y decidir si esas equivalencias se aceptan como oficiales.
4. **Contraste documental restante**: leer completa la CREG 015 de 2018 y las resoluciones particulares de EPM, y las CREG 152 de 2020 y 003 de 2021.
5. **Consulta formal a EPM o a la CREG** sobre los cambios detectados (Hito 6).
6. **Extended Isolation Forest**, **scorecard definitivo** (4.5) y **resultados por nivel** (4.6).
7. **Tratamiento de MAD igual a cero**, que sigue con la regla conservadora de 4.1.
8. **Decidir qué hacer con LOF** (CHEC y EPM con etiquetas canónicas): quitar duplicados o aumentar vecinos cambia el significado de la densidad.

No se deben presentar como aprobados ni los umbrales ni los resultados de estos puntos hasta que el director los confirme.

## 23. Idea principal para recordar

El proyecto no consiste en producir un único porcentaje de “calidad”. Consiste en construir una
evaluación explicable y reproducible: cada resultado debe indicar qué se midió, con qué datos, con
qué fórmula, bajo qué supuestos, con qué evidencia y con qué limitaciones.

El Hito 4 añade dos reglas de honestidad: **una señal estadística no es un error de dato**, y **un mes con muchas alertas no es un
cambio regulatorio hasta compararlo con la publicación real**. Por eso el proyecto reporta alertas “sin error conocido”,
prevalencias supuestas, intervalos por categorías y el estado de cada pieza de evidencia (leída, no verificada, no localizada).
