# Guía explicativa del proyecto

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

Estamos técnicamente preparados para iniciar el Hito 4 porque ya existe una línea base comparable.
El Hito 4 debe construir:

1. scorecards por fuente y dimensión;
2. comparación de técnicas bajo el mismo protocolo;
3. análisis de sensibilidad;
4. comparación con procedimientos tradicionales;
5. conclusiones usando intervalos y estados de evidencia.

El Hito 4 no debe ocultar los estados provisionales ni comparar porcentajes sin revisar población,
unidad, aplicabilidad y evidencia.

## 15. Idea principal para recordar

El proyecto no consiste en producir un único porcentaje de “calidad”. Consiste en construir una
evaluación explicable y reproducible: cada resultado debe indicar qué se midió, con qué datos, con
qué fórmula, bajo qué supuestos, con qué evidencia y con qué limitaciones.
