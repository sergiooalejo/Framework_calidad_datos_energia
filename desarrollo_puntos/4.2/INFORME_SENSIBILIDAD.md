# Hito 4.2 · Resultados del análisis de sensibilidad

Fecha: 6 de noviembre de 2026. Se ejecutó el punto 2 del Hito 4 del plan local sobre
los snapshots conservados de EPM, CHEC, SSPD y XM. Las salidas de 3.x y 4.1 permanecen intactas.

## Resultado principal

Se evaluaron 24, 36 y 48 cambios de referencia cuando la longitud lo permite, las
constantes I/MR, límites robustos con MAD, percentiles IF 99 y 99,5, R12 con factores
5, 10 y 20, ambos horizontes de detección y cuatro umbrales de reclasificación sistémica.
Se ejecutaron **22 escenarios fuente/cohorte/ventana**, con
**39,288 observaciones detalladas** y
**212,497 ensayos de inyección detallados**, sumando paneles
y ventanas. Estos conteos incluyen repeticiones deliberadas del mismo caso bajo otros
parámetros; no son tamaños de muestra independientes. El tipo de ensayo distingue
inyecciones individuales y estrés colectivo.

SSPD no permite 48 cambios más 12 de vigilancia: tiene como máximo 59 meses
consecutivos y esa configuración requiere 61. Se registra como **no evaluable**,
sin recortar vigilancia ni rellenar datos. XM conserva una sola serie/categoría;
sus resultados son descriptivos y no reciben un IC entre categorías.

## 1. Cobertura y comparación de ventanas

| Fuente | Ref. 24 | Ref. 36 | Ref. 48 |
| --- | --- | --- | --- |
| EPM | 121 | 32 | 27 |
| CHEC | 276 | 276 | 276 |
| SSPD | 388 | 321 | 0 |
| XM | 1 | 1 | 1 |

La carga reutiliza `4.1/zscore_robusto.py`. Después se selecciona la racha mensual
consecutiva más larga de cada serie; en empate, la de fin más reciente. Se fija la
vigilancia en sus doce últimos cambios y se toman inmediatamente antes 24, 36 o 48
cambios. No se unen rachas separadas ni se cruza un mes ausente.

El panel `disponible` describe la población elegible de cada ventana. El panel `comun`
mantiene las mismas series, categorías y meses en todas las ventanas factibles de la
fuente. En SSPD compara 24 y 36; en las otras fuentes, 24/36/48. IF también se vuelve
a entrenar dentro de esta cohorte común, evitando que una variación en la población
de entrenamiento se confunda con la longitud de referencia.

Lectura inicial de la cohorte común con referencia 36:

- **EPM:** I/MR clásica genera 5.556 % de alertas reales y MAD 3σ, 3.704 %. IF p99,5 detecta 5.01 % de las inyecciones individuales en t o t+1, sobre 1,617 casos de la mezcla diseñada.
- **CHEC:** I/MR clásica genera 0.000 % de alertas reales y MAD 3σ, 0.000 %. IF p99,5 detecta 63.98 % de las inyecciones individuales en t o t+1, sobre 17,103 casos de la mezcla diseñada.
- **SSPD:** I/MR clásica genera 4.595 % de alertas reales y MAD 3σ, 8.827 %. IF p99,5 detecta 51.31 % de las inyecciones individuales en t o t+1, sobre 20,880 casos de la mezcla diseñada.
- **XM:** I/MR clásica genera 0.000 % de alertas reales y MAD 3σ, 0.000 %. IF p99,5 detecta 72.73 % de las inyecciones individuales en t o t+1, sobre 55 casos de la mezcla diseñada.

Una tasa real de cero significa que estos límites no señalaron esos doce meses;
no demuestra ausencia de errores. La detección artificial también depende del tipo
de perturbación y del umbral: por ejemplo, una configuración IF con pocas alertas
puede tener baja detección de las inyecciones. Se conservan esos resultados sin
ajustar retrospectivamente los percentiles para mejorar la cifra de vigilancia.

Las diferencias siguientes son tasa alternativa menos tasa con referencia 36, en
las mismas series y meses. Sus IC por categorías están en el CSV correspondiente.

| Fuente | Ventana vs. 36 | Método | Series | Cambio (pp) |
| --- | --- | --- | --- | --- |
| EPM | 24 | IMR_clasica | 27 | +0.000 |
| EPM | 24 | MAD_3sigma | 27 | -1.852 |
| EPM | 24 | IF_p99.5 | 27 | +0.000 |
| EPM | 48 | IMR_clasica | 27 | -1.852 |
| EPM | 48 | MAD_3sigma | 27 | +0.000 |
| EPM | 48 | IF_p99.5 | 27 | +0.000 |
| CHEC | 24 | IMR_clasica | 276 | +0.242 |
| CHEC | 24 | MAD_3sigma | 276 | +0.000 |
| CHEC | 24 | IF_p99.5 | 276 | +0.000 |
| CHEC | 48 | IMR_clasica | 276 | +0.000 |
| CHEC | 48 | MAD_3sigma | 276 | +1.389 |
| CHEC | 48 | IF_p99.5 | 276 | +0.000 |
| SSPD | 24 | IMR_clasica | 321 | +0.649 |
| SSPD | 24 | MAD_3sigma | 321 | -0.337 |
| SSPD | 24 | IF_p99.5 | 321 | +0.415 |
| XM | 24 | IMR_clasica | 1 | +0.000 |
| XM | 24 | MAD_3sigma | 1 | +0.000 |
| XM | 24 | IF_p99.5 | 1 | +0.000 |
| XM | 48 | IMR_clasica | 1 | +0.000 |
| XM | 48 | MAD_3sigma | 1 | +0.000 |
| XM | 48 | IF_p99.5 | 1 | +0.000 |

Estos resultados no se comparan directamente con las tasas de 4.1: allí se usaron
los primeros cambios y podían concatenarse parejas consecutivas de distintas rachas.
Aquí la vigilancia es final y toda la partición pertenece a una sola racha continua.

## 2. Constantes y límites robustos

Las constantes del plan cumplen funciones distintas:

- Carta I: media de cambios ± **2,66 × MR medio de referencia**.
- Carta MR: señal si el rango móvil excede **3,267 × MR medio de referencia**.
- `IMR_clasica` es la unión de ambas señales; el primer MR vigilado usa el último
  cambio de referencia, sin incorporar vigilancia al cálculo de límites.
- `MAD_3sigma`: mediana ± **3 × MAD / 0,6744897501960817**.
  También se examinan multiplicadores 2,66 y 3,267 sobre esta escala robusta como
  sensibilidad adicional; no se presentan como las mismas constantes de la carta I/MR.

Las fórmulas se apoyan en [NIST, cartas individuales](https://www.itl.nist.gov/div898/handbook/pmc/section3/pmc322.htm),
[NIST, constantes I/MR](https://nvlpubs.nist.gov/nistpubs/Legacy/IR/nistir4941.pdf) y
[NIST, MAD escalado](https://www.itl.nist.gov/div898/software/dataplot/refman2/auxillar/mad.htm).
Los multiplicadores explorados proceden del plan y del protocolo del proyecto;
no se atribuye a NIST una recomendación de seleccionar uno de ellos para estas fuentes.

Con MAD igual a cero se conserva el criterio explícito de 4.1: cualquier cambio
distinto de la mediana produce una señal y no se añade una escala artificial.
Series con MAD cero en referencia 36/cohorte común: `{'CHEC': 0, 'EPM': 0, 'SSPD': 18, 'XM': 0}`.
Esto puede hacer que cambiar el multiplicador no tenga efecto; no se interpreta
una tasa idéntica como prueba de robustez del proceso.

Tasas reales bajo referencia 36 y cohorte común:

| Fuente | Método | Series | Alertas (%) | IC95 (%) |
| --- | --- | --- | --- | --- |
| EPM | IMR_clasica | 27 | 5.556 | 0.000–14.086 |
| EPM | MAD_3sigma | 27 | 3.704 | 0.000–9.391 |
| EPM | IF_p99 | 27 | 0.000 | 0.000–0.000 |
| EPM | IF_p99.5 | 27 | 0.000 | 0.000–0.000 |
| EPM | R12_f10 | 27 | 0.000 | 0.000–0.000 |
| CHEC | IMR_clasica | 276 | 0.000 | 0.000–0.000 |
| CHEC | MAD_3sigma | 276 | 0.000 | 0.000–0.000 |
| CHEC | IF_p99 | 276 | 0.000 | 0.000–0.000 |
| CHEC | IF_p99.5 | 276 | 0.000 | 0.000–0.000 |
| CHEC | R12_f10 | 276 | 0.000 | 0.000–0.000 |
| SSPD | IMR_clasica | 321 | 4.595 | 3.264–6.033 |
| SSPD | MAD_3sigma | 321 | 8.827 | 7.017–10.895 |
| SSPD | IF_p99 | 321 | 0.571 | 0.103–1.304 |
| SSPD | IF_p99.5 | 321 | 0.467 | 0.065–1.160 |
| SSPD | R12_f10 | 321 | 0.130 | 0.000–0.304 |
| XM | IMR_clasica | 1 | 0.000 | Sin IC: una categoría |
| XM | MAD_3sigma | 1 | 0.000 | Sin IC: una categoría |
| XM | IF_p99 | 1 | 0.000 | Sin IC: una categoría |
| XM | IF_p99.5 | 1 | 0.000 | Sin IC: una categoría |
| XM | R12_f10 | 1 | 0.000 | Sin IC: una categoría |

Los intervalos son bootstrap descriptivo de **categorías completas**, no de filas
mensuales ni series supuestamente independientes: 1000
repeticiones, razón de numeradores y denominadores remuestreados, semilla fija.
Condicionan a las fuentes y modelos ajustados y no incluyen incertidumbre por reentrenamiento
ni garantizan representatividad poblacional. Se conservan por fuente, método y ventana.

## 3. Percentiles 99 y 99,5 de Isolation Forest

Se usan 300 árboles por fuente/ventana/cohorte/calendario de vigilancia, con cuatro rasgos: cambio log actual,
cambio anterior, diferencia absoluta entre cambios y nivel log relativo a la mediana
del nivel de referencia. Centros, escalas y percentiles se calculan solo en referencia;
las inyecciones no vuelven a ajustar el modelo. Las series que terminan en meses
distintos tienen modelos separados, para que ninguna referencia termine después
del inicio de vigilancia de otra serie del mismo modelo. `modelos_IF.csv` conserva
los calendarios y umbrales; el submuestreo es el menor de 256 y el número de referencias.
El umbral 99,5 es mayor o igual al 99
y sus alertas son un subconjunto, verificado durante la ejecución.

Los percentiles son de puntajes **de entrenamiento**. No representan una tasa de
falsas alarmas garantizada fuera de muestra ni equivalen a una validación cruzada
a tasa igualada. Se conserva esta distinción frente al componente de calibración 4.1.

## 4. Sensibilidad de R12 e interacción de parámetros

Se aplica `abs(nivel) > factor × mediana(abs(niveles_referencia))` con factores
5, 10 y 20. El umbral utiliza solo los niveles de referencia; no se estima sobre
la serie completa como ocurría en el Hito 2. R12 se mantiene como advertencia.
En XM se analiza magnitud de demanda, no un importe tarifario ni el valor absoluto
de un cambio logarítmico. Su semántica debe seguir identificada como adaptación.

Además de cada detector aislado, `combinaciones_framework.csv` cruza dos alternativas
de cartas (I/MR clásica o MAD 3σ), dos percentiles IF y tres factores R12, por ventana
y cohorte: doce uniones de señales por escenario. La figura 09 muestra el efecto
conjunto sobre la tasa real de alertas. No se elige una combinación usando la propia
vigilancia como conjunto de validación.

## 5. Detección en t frente a t o t+1

Se perturba un único nivel positivo en copias de la vigilancia, con referencia y modelo
congelados. Se usan todos los once primeros meses, sin reemplazo; el duodécimo es el
seguimiento del último origen. Los seis tipos son multiplicar/dividir por 1.000,
serial Excel fijo 43.577, aumento de 10 %, valor anterior y otra medida positiva
del mismo grupo/mes. La otra medida se elige por orden de nombre para reproducibilidad.
Si el valor no cambia o no existe otra medida, el caso se omite con motivo explícito.

El serial Excel replica un mecanismo de representación tarifaria; en demanda/consumo
es solo una perturbación numérica de escala, no evidencia de un defecto observado.
Signos negativos, ceros, faltantes y texto quedan fuera de este ensayo logarítmico:
no se convierten en logaritmos ficticios ni se mezclan con reglas de validez.

`t1` en el detalle significa la señal **solo en el mes siguiente**. La métrica
`t_o_t1` es la unión, no la suma; una prueba se cuenta una sola vez. Se conservan
también señales nuevas respecto a la copia sin inyección, para mostrar cuánto
puede inflar el resultado la presencia de alertas naturales previas. Estas señales
nuevas no son una estimación de precisión de alertas reales.

Resumen agregado de tipos para referencia 36/cohorte común:

| Fuente | Método | Casos | Solo t (%) | t o t+1 (%) | Ganancia (pp) | Nueva frente a base (%) |
| --- | --- | --- | --- | --- | --- | --- |
| EPM | IMR_clasica | 1617 | 68.27 | 73.47 | 5.19 | 71.00 |
| EPM | MAD_3sigma | 1617 | 68.95 | 72.79 | 3.83 | 71.30 |
| EPM | IF_p99.5 | 1617 | 5.01 | 5.01 | 0.00 | 5.01 |
| EPM | R12_f10 | 1617 | 36.73 | 36.73 | 0.00 | 36.73 |
| CHEC | IMR_clasica | 17103 | 64.09 | 74.54 | 10.44 | 74.54 |
| CHEC | MAD_3sigma | 17103 | 72.84 | 75.56 | 2.72 | 75.56 |
| CHEC | IF_p99.5 | 17103 | 57.66 | 63.98 | 6.32 | 63.98 |
| CHEC | R12_f10 | 17103 | 35.50 | 35.50 | 0.00 | 35.50 |
| SSPD | IMR_clasica | 20880 | 66.55 | 70.03 | 3.48 | 66.98 |
| SSPD | MAD_3sigma | 20880 | 70.03 | 73.67 | 3.64 | 68.70 |
| SSPD | IF_p99.5 | 20880 | 41.36 | 51.31 | 9.95 | 50.98 |
| SSPD | R12_f10 | 20880 | 23.24 | 23.34 | 0.11 | 23.19 |
| XM | IMR_clasica | 55 | 60.00 | 67.27 | 7.27 | 67.27 |
| XM | MAD_3sigma | 55 | 63.64 | 65.45 | 1.82 | 65.45 |
| XM | IF_p99.5 | 55 | 70.91 | 72.73 | 1.82 | 72.73 |
| XM | R12_f10 | 55 | 20.00 | 20.00 | 0.00 | 20.00 |

En esta comparación, la mayor ganancia entre los métodos mostrados corresponde a
**CHEC / IMR_clasica: 10.44 puntos porcentuales**.
Los CSV por tipo conservan denominadores e IC por categoría. Los porcentajes agregados
describen la mezcla de errores diseñada y no una prevalencia real de errores.

## 6. Efecto de la regla sistémica

Para cada fuente, método y mes se divide el número de series-medida con señal entre
las series-medida realmente observadas en vigilancia ese mes. Se evalúan X = 10, 25,
50 y 75 %, con desigualdad estricta `fracción > X`. Se exige al menos dos series;
XM no admite una interpretación transversal con una sola serie y conserva sus alertas.
La unidad series-medida es la misma de los detectores; medidas del mismo grupo pueden
estar correlacionadas, por lo que no se interpreta el denominador como independencia.

Se calcula la tasa original y la retenida para revisión individual. Las señales
reclasificadas quedan guardadas en el catálogo mensual: no se eliminan. La etiqueta
es **candidato sistémico**, sin afirmar que sea un cambio regulatorio confirmado.
La calibración regulatoria y el contraste de fechas concretas son materia de 4.4;
esta ejecución 4.2 estudia sensibilidad sobre una grilla explícita, no elige X óptimo.

Ejemplo I/MR, referencia 36/cohorte común, X = 25 %:

| Fuente | Original (%) | Retenida (%) | Reclasificadas |
| --- | --- | --- | --- |
| EPM | 5.556 | 5.556 | 0 |
| CHEC | 0.000 | 0.000 | 0 |
| SSPD | 4.595 | 4.595 | 0 |
| XM | 0.000 | 0.000 | 0 |

Se recalcula el contexto mensual al inyectar: para el error individual se cambia
la señal de esa serie; para un evento colectivo se cambian simultáneamente todas
las series afectadas. El estrés colectivo aplica +10 % o ×1.000 en el mes con más
orígenes disponibles (desempate: el más reciente). Permite medir cuántas detecciones
de errores conocidos se ocultarían al aplicar la reclasificación sin validación.
Los eventos colectivos son ensayos descriptivos únicos y no reciben un IC basado
en fingir que cada serie es un evento independiente.

## 7. Lectura y límites

- La comparación de ventanas debe partir del panel común y de sus cambios pareados;
  el panel disponible informa cobertura, pero mezcla poblaciones distintas.
- Un percentil o factor mayor reduce o conserva señales para un modelo/referencia
  dados; una tasa menor no demuestra mejor calidad ni mejor sensibilidad.
- Extender detección a t+1 puede recuperar el retorno del pico o un rasgo rezagado;
  también añade un mes de oportunidad de alerta. Se muestran ambos horizontes y
  las señales nuevas respecto a base, sin presentar esa ganancia como gratuita.
- La regla sistémica reduce la cola de revisión individual, pero puede esconder
  errores masivos. Los resultados de estrés cuantifican ese riesgo por configuración.
- Las series ya tienen restricciones de positividad y cuarentena EPM de la carga 4.1;
  esto condiciona el análisis. No constituye una auditoría de todos los registros fuente.
- La cuarentena histórica permanece fija al variar el factor R12. Se estudia su efecto
  como umbral detector; no se simula una nueva política que readmita o excluya registros
  históricos y vuelva a estimar todas las referencias.
- Las inyecciones siguen la mezcla diseñada; no sustituyen etiquetas externas ni
  completan la validación de alertas reales o todos los experimentos de 4.3.
- No se declaran óptimos umbrales ni aprobaciones de negocio. Los modelos se ajustan
  solo con referencias y no se modifican los datos ni resultados anteriores.

## Reproducir y auditar

Desde la raíz del proyecto:

```powershell
python desarrollo_puntos/4.2/analisis_sensibilidad.py
python -m unittest discover -s desarrollo_puntos/4.2 -p test_sensibilidad.py -v
python desarrollo_puntos/4.2/verificar_resultados.py
```

`configuracion.json` fija versiones, semilla, fuentes, hashes, parámetros y fórmulas.
`manifiesto_resultados.json` permite verificar cada archivo. Las tablas de detalle
comprimidas son CSV UTF-8 legibles con `pandas.read_csv(ruta, compression="gzip")`.
Las nueve figuras se entregan en PNG, SVG y PDF para revisión y exportación.
