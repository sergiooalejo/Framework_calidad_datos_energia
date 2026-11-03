# Hito 3 · Punto 2 · Fichas de caracterización por fuente

Entregable del objetivo específico 2 (OE2). Una ficha por cada fuente seleccionada: EPM y
CHEC.

## Para qué sirve una ficha de caracterización

No es un diccionario de datos. Los diccionarios de columnas ya están en
`fuentes_datos/diccionarios/`.

El DAMA-DMBOK define la calidad de datos como **aptitud para el uso**: un dato no es bueno
o malo en abstracto, lo es respecto de quien lo necesita y de para qué lo necesita. Un
regulador que vigila cumplimiento tarifario no tolera un importe mal registrado; un
analista que estudia tendencias sí tolera ruido puntual, pero no tolera que falten meses.

De ahí se sigue lo esencial: **sin identificar al consumidor del dato no se puede
justificar ningún umbral de aceptación**. La pregunta «¿por qué 99,5 % y no 95 %?» solo
tiene respuesta si antes se dijo quién usa el dato.

Por eso esta ficha es condición de la matriz OE1 y no al revés: los umbrales de
[`matriz_oe1.md`](matriz_oe1.md) se sostienen sobre lo que aquí se declare.

El resumen DAMA del proyecto ya señalaba esta carencia: *«nunca se dice quién consume las
tarifas de EPM ni para qué. Sin ese consumidor no se puede justificar qué dimensiones
importan ni qué umbral es aceptable»*.

## Estructura de cada ficha

Cada ficha responde cinco bloques, en este orden:

| Bloque | Pregunta | Cómo se obtiene |
|---|---|---|
| 1 | Identificación y estructura | Medido sobre el CSV |
| 2 | Cobertura temporal y series | Medido sobre el CSV |
| 3 | Datos críticos | Medido y argumentado |
| 4 | Unidades y significado | Metadato oficial del publicador |
| 5 | Consumidor del dato | **Decisión del equipo** |

Los cuatro primeros se miden. El quinto se decide, y de él cuelgan los umbrales.

**Procedencia de las cifras.** Todo lo medido proviene de los CSV conservados en
`fuentes_datos/datos/`. Las cifras de series de EPM provienen del pipeline del Hito 2
(`codigo/salida_hito2/`). Las de series consecutivas de CHEC provienen de
`fuentes_datos/verificaciones/chec_validacion_series.json`. Las definiciones oficiales
provienen de `fuentes_datos/metadatos/`.

---

# Ficha 1 · EPM — Histórico de tarifas de energía eléctrica

## Bloque 1 · Identificación y estructura

| Campo | Valor |
|---|---|
| Conjunto | `sfcd-b3ey` |
| Nombre | Histórico de Tarifas de Energía Eléctrica – EPM (2016-2021) |
| Publicador | E.S.P. Empresas Públicas de Medellín, Antioquia |
| Orden | Territorial · Cobertura departamental |
| Portal | https://www.datos.gov.co/d/sfcd-b3ey |
| Licencia | CC BY-SA 4.0 |
| Archivo conservado | `fuentes_datos/datos/epm_sfcd-b3ey.csv` |
| Tamaño | **3.623 filas × 12 columnas** |
| Granularidad | Un registro tarifario por categoría y mes |

**Clave candidata:** `tipodeinformacion` + `tipodetarifa` + `tipodedato` + `rangodeconsumo`
+ `nivel` + `year` + `mes`. Evaluada: no presenta conflictos una vez retiradas las copias
exactas.

**Estructura de categorías**

| Nivel de tensión | Filas |
|---|---|
| I | 2.154 |
| II | 489 |
| III | 493 |
| IV | 487 |

## Bloque 2 · Cobertura temporal y series

| Campo | Valor |
|---|---|
| Ventana declarada | diciembre de 2016 a diciembre de 2021 |
| Meses esperados en la ventana | 61 |
| Meses presentes | **61** |
| Períodos faltantes | **ninguno** |
| Series posibles | 202 |
| Series con 49 meses o más | **83** |
| Series clasificadas como limpias | 77 |

La continuidad es total: no falta un solo mes de la ventana. Esta observación **no acredita
la dimensión de oportunidad**, que exige conocer la fecha real de publicación de cada
período; solo establece que la serie no tiene interrupciones.

El mínimo de 49 meses no es arbitrario: proviene del diseño de las cartas de control, que
reservan 36 cambios de referencia más al menos 12 meses de vigilancia.

## Bloque 3 · Datos críticos

**Críticos.** Son el objeto de la auditoría y su defecto invalida el registro:

- Las cinco columnas de importe: `propiedadepm`, `compartido`, `propiedaddelcliente`,
  `punta`, `fueradepunta`.
- Las cinco categorías y el período, porque constituyen la clave y sin ellas no hay serie.

**De apoyo.** `tipodeinformacion` aporta contexto de modalidad tarifaria pero no se audita
como valor.

**Un hallazgo que condiciona la regla R10.** Las columnas de importe se usan por mitades:

| Columna | Filas con valor distinto de cero | Proporción |
|---|---|---|
| `propiedadepm` | 2.151 | 59,4 % |
| `compartido` | 2.151 | 59,4 % |
| `propiedaddelcliente` | 2.152 | 59,4 % |
| `punta` | 1.469 | 40,5 % |
| `fueradepunta` | 1.462 | 40,4 % |

Las tres primeras aplican al Nivel I; las dos últimas a los niveles II a IV. **Ninguna fila
usa las cinco.** En consecuencia, exigir las cinco columnas en toda fila marcaría como
incompleto el 100 % del conjunto. La matriz de aplicabilidad por nivel es condición previa
para que R10 signifique algo.

## Bloque 4 · Unidades y significado

### Lo que el publicador sí define

Tomado de las descripciones oficiales del portal:

- **B.T.** = Baja Tensión (Nivel 1, menor a 1 kV).
- **C.S.** = Consumo Subsidiado.
- **Franjas horarias:** horas de punta de 9 a. m. a 12 m. y de 6 p. m. a 9 p. m.; horas
  fuera de punta de 12 p. m. a 9 a. m., de 12 m. a 6 p. m. y de 9 p. m. a 12 p. m.

La definición de **C.S.** da respaldo documental a las equivalencias de etiquetas que el
proyecto tenía solo como propuesta:

| Variante | Filas | Equivalente propuesto | Filas |
|---|---|---|---|
| `0-CS` | 43 | `Rango 0 - CS` | 144 |
| `Mayor CS` | 42 | `Rango > CS` | 144 |

Ambos pares refieren al mismo umbral de consumo subsidiado. Es evidencia documental, no
una confirmación firmada por la entidad; el control MAP01 sigue requiriendo validación
escrita.

### Lo que el publicador no define

**La unidad de los importes.** El metadato no declara si los valores están en pesos por
kilovatio-hora, por factura o por kilovatio. Es la carencia más grave de esta fuente, y
afecta a toda comparación entre conceptos.

**Cinco columnas sin descripción alguna:** `tipodetarifa`, `nivel`, `propiedadepm`,
`compartido` y `propiedaddelcliente`.

Que las tres columnas de propiedad de red carezcan de definición oficial es relevante
porque **son exactamente las que compara la regla R08** (orden Propiedad EPM ≥ Compartido ≥
Propiedad del Cliente). La regla se aplica hoy sobre un fundamento no documentado.

### Un defecto entre metadato y dato

La descripción oficial de `tipodedato` declara el concepto **Cfm,j ($/factura)** y aporta
cinco valores mensuales: diciembre 2016 = 5.660; enero 2017 = 5.642; febrero 2017 = 5.699;
marzo 2017 = 5.757; abril 2017 = 5.784.

**Ese concepto no aparece en ninguna fila del conjunto publicado.** Se verificó recorriendo
los 28 valores distintos de `tipodedato`: ninguno corresponde a Cfm,j.

El publicador documenta una variable que no publica. Es un defecto de integridad entre
metadato y dato, y priva al proyecto de cinco valores de referencia que habrían servido
para el control de exactitud.

### El significado de «Rango de Consumo»

El plan de hitos describe este punto como *«significado de Rango de Consumo (2.143
ausentes)»*. La medición muestra que **no se trata de ausencias**.

Los 2.143 registros con valor `N/A` se distribuyen así:

| Nivel | Filas con `N/A` | Del total del nivel | Interpretación |
|---|---|---|---|
| II | 489 | **100 %** | Estructural |
| III | 493 | **100 %** | Estructural |
| IV | 487 | **100 %** | Estructural |
| I | 674 | 31,3 % | **Requiere explicación** |

**1.469 de los 2.143 son estructurales.** Los niveles II, III y IV no se tarifan por rango
de consumo sino por franja horaria, de modo que «no aplica» es la respuesta correcta y no
un dato faltante. Registrarlos como ausencias hunde el indicador de completitud sin
fundamento.

Los **674 restantes, todos del Nivel I, sí constituyen un hallazgo**: dentro de ese nivel el
mismo concepto aparece unas veces con rango de consumo y otras con `N/A`. Por ejemplo,
«Cargo transporte STN: Tm» aparece 121 veces con rango y 61 veces sin él. Eso no es
estructura, es inconsistencia de registro, y debe reportarse como tal.

**Consecuencia para la matriz:** el denominador de completitud debe excluir los casos no
aplicables por nivel y conservar los 674 como incidencia.

## Bloque 5 · Consumidor del dato

**Pendiente de decisión del equipo.** Ver la sección común al final de este documento.

---

# Ficha 2 · CHEC — Información de costo unitario de tarifas

## Bloque 1 · Identificación y estructura

| Campo | Valor |
|---|---|
| Conjunto | `c698-wqig` |
| Nombre | Información Costo unitario de tarifas de energía CHEC |
| Publicador | E.S.P. Central Hidroeléctrica de Caldas |
| Orden | Territorial · Cobertura departamental |
| Portal | https://www.datos.gov.co/d/c698-wqig |
| Archivo conservado | `fuentes_datos/datos/chec_c698-wqig.csv` |
| Tamaño | **40.609 filas × 24 columnas** |
| Granularidad | Costo unitario por categoría tarifaria y mes |

**Estructura de categorías**

| Campo | Valores distintos | Detalle |
|---|---|---|
| `comercializador_codigo` | **1** | `CHCC` |
| `mercado_codigo` | **2** | PEREIRA y CHEC |
| `nivel_tension_codigo` | 4 | 1, 2, 3, 4 |
| `modalidadcobro_propiedad` | 4 | 0 % OR, 0 % OR SIN AOM, 50 % OR, 100 % OR |
| `costounitariotarifa_tipomed` | 3 | S (28.875), HP (5.867), HM (5.867) |

**Clave candidata:** las doce categorías más año y mes. Estado: provisional. Presenta
**1.398 claves repetidas de 37.312**, que afectan a 4.695 filas. No deben eliminarse de
forma automática: hasta conocer su causa, suprimirlas destruiría evidencia.

## Bloque 2 · Cobertura temporal y series

| Campo | Valor |
|---|---|
| Ventana | enero de 2008 a septiembre de 2026 |
| Meses esperados | 225 |
| Meses presentes | **225** |
| Períodos faltantes | **ninguno** |
| Series con 49 meses consecutivos | **183** |
| Series con 61 meses consecutivos | 180 |
| Racha máxima | 201 meses |

Las cifras de series provienen de la validación del equipo, que exige registro único por
mes, valores positivos y finitos, y variación dentro del grupo.

### Advertencia sobre la independencia de esas series

Las 183 series **no son 183 unidades independientes**. Proceden de un solo comercializador,
dos mercados y cuatro niveles de tensión. Además, dado que el costo unitario es la suma de
componentes fijados a nivel de empresa y mercado, las series son transformaciones casi
deterministas unas de otras.

El tamaño efectivo está más cerca de las combinaciones de mercado y nivel —del orden de
ocho— que de 183.

Esta es la misma objeción que la revisión del Hito 2 planteó para EPM (observación mayor 3:
«no son 83 series independientes»). **Debe declararse por escrito en los resultados**, y el
remuestreo para intervalos de confianza debe hacerse por mercado y nivel, no por serie.

## Bloque 3 · Datos críticos

**Críticos.** Las doce categorías de la clave, el período, y las columnas de medida con
cobertura completa:

| Columna | Filas con valor distinto de cero | Proporción |
|---|---|---|
| `costounitariotarifa_cu` | 40.609 | **100 %** |
| `costounitariotarifa_valor_tarifa` | 40.609 | **100 %** |
| `costounitariotarifa_transmision` | 40.609 | **100 %** |
| `costounitariotarifa_generacion` | 40.598 | 100,0 % |
| `costounitariotarifa_distribucion` | 40.598 | 100,0 % |
| `costounitariotarifa_comercializacion` | 40.598 | 100,0 % |
| `costounitariotarifa_perdidas` | 40.598 | 100,0 % |
| `costounitariotarifa_restricciones` | 40.598 | 100,0 % |

**Dudosas.** Dos columnas presentan cobertura parcial y carecen de definición:

| Columna | Filas con valor distinto de cero | Proporción | Ceros |
|---|---|---|---|
| `costounitariotarifa_subcon` | 23.744 | 58,5 % | 16.854 |
| `costounitariotarifa_cureal` | **6.738** | **16,6 %** | **33.871** |

Que el 83,4 % de `cureal` sean ceros no permite por sí mismo concluir que falte el dato: sin
saber qué representa la variable, no se puede distinguir un cero legítimo de una ausencia
disfrazada. Es la entrada natural del control DEF01.

**Un invariante verificado.** El costo unitario es igual a la suma de sus seis componentes
—generación, transmisión, distribución, comercialización, pérdidas y restricciones— en
**40.598 de 40.598 filas aplicables**. Aunque las unidades no estén declaradas, la relación
entre ellas sí es verificable y se cumple sin excepción. Esto proporciona un indicador de
exactitud con umbral natural del 100 %, que no requiere justificar una cifra arbitraria.

## Bloque 4 · Unidades y significado

### El publicador no define sus variables

Las veinticuatro descripciones oficiales del portal se limitan, en su mayoría, a repetir el
nombre de la columna. Para las tres variables que el proyecto necesita precisar:

| Variable | Descripción oficial completa |
|---|---|
| `costounitariotarifa_tipomed` | «tipomed» |
| `costounitariotarifa_subcon` | «Subcon» |
| `costounitariotarifa_cureal` | «Costo unitario real» |

Las dos primeras son circulares: repiten el nombre del campo sin aportar significado.

**Esto es un hallazgo, no una carencia del equipo.** La ambigüedad que el control DEF01
señala reside en la fuente, y así debe reportarse: el publicador no documenta tres de sus
propias variables, dos de ellas con cobertura parcial de los datos.

### Tipado de las medidas

Las veinticuatro columnas están declaradas como **texto** en el esquema del portal,
incluidas las diez de medida. Se observan además formatos con decimal sin cero inicial, del
tipo `.0000` y `-.5972509`. La conversión a número debe hacerse con convención explícita y
conservando el texto original.

### Una referencia regulatoria disponible

La estructura del costo unitario corresponde a la fórmula de la Resolución CREG 119 de
2007: CU = Gm + Tm + Dn,m + Cvm + PRn,m + Rm. El propio conjunto de EPM incluye un concepto
denominado `CU CREG 158-2015`, que remite a otra resolución. Ambas son públicas y permiten
documentar el significado de los componentes sin esperar respuesta de la entidad.

### Integridad entre código y descripción

El código `claseservicio_codigo = 'RS'` resuelve a **siete descripciones distintas**:

| Filas | Descripción |
|---|---|
| 4.560 | Residencial Estrato 4 |
| 2.955 | Residencial Estrato 5 |
| 2.907 | Residencial Estrato 6 |
| **1.800** | **Residencial** |
| 1.092 | Residencial Estrato 2 |
| 1.073 | Residencial Estrato 3 |
| 956 | Residencial Estrato 1 |

La relación código → descripción no es funcional. La causa es diagnosticable: el estrato ya
viaja en `claseservicio_estrato` y la descripción lo duplica, pero en 1.800 filas esa
duplicación no se realizó. Es denormalización inconsistente, y constituye el primer caso
documentado del control INT02.

## Bloque 5 · Consumidor del dato

**Pendiente de decisión del equipo.** Ver la sección siguiente.

---

# Ficha 3 · SSPD — Información comercial residencial y no residencial

Esta ficha cubre la tercera fuente, incorporada para cerrar la carencia que el propio
`fuentes_datos/README.md` declaraba: *«Ambos contienen tarifas/costos, no consumo
observado»*. Es la única fuente del proyecto con consumo medido.

## Bloque 1 · Identificación y estructura

| | |
|---|---|
| Conjunto | `ebby-cjha` |
| Publicador | Superintendencia de Servicios Públicos Domiciliarios |
| Portal | https://www.datos.gov.co/d/ebby-cjha |
| Filas en origen | **11.905.557** |
| Columnas | 29 |
| Naturaleza | Registro de **facturación**, no tarifario |
| Ámbito | **Zonas No Interconectadas.** 91 empresas; ninguna del Sistema Interconectado Nacional |
| Periodicidad declarada | Anual |
| Última carga de datos | 28 de octubre de 2023 |

**Por qué no se conserva íntegro.** En origen pesa unos 9,7 GB, que no es versionable. Se
conservan dos **censos declarados**, no muestras aleatorias:

| Archivo | Filas | Universo |
|---|---|---|
| `sspd_ebby-cjha_mensual.csv` | 15.075 | Las 91 empresas y los 59 períodos, agregados por ocho dimensiones |
| `sspd_ebby-cjha_detalle.csv` | 91.840 | Todos los registros de la empresa 28111, en sus 57 períodos |

El agregado sostiene cobertura, dominios y series; el detalle sostiene las reglas de fila.
Cada uno declara su universo, de modo que ningún resultado se presenta como si cubriera
algo que no cubre.

**Diferencia estructural con EPM y CHEC.** Las dos fuentes anteriores publican el costo
unitario por categoría tarifaria. Esta publica la factura por usuario y período. No comparte
los ejes de propiedad del activo ni los componentes de la Resolución CREG 119 de 2007, y por
eso los controles R08, R09 e INT02 quedan marcados `no_aplica` en la matriz: el concepto no
existe en su esquema, que es distinto de faltar evidencia.

## Bloque 2 · Cobertura temporal y series

| | |
|---|---|
| Ventana | julio 2017 a mayo 2022 |
| Períodos presentes | **59** |
| Períodos esperados en la ventana | 59 |
| Huecos internos | **ninguno** |
| Series empresa × estrato | 207 |
| Series con 49 meses o más | **136** |

Los 59 períodos son consecutivos. Antes de julio de 2017 el conjunto no publica: los seis
primeros meses de 2017 no existen, de modo que la ventana empieza ahí y no se cruza ese
hueco al construir series.

Con 59 meses caben 36 cambios de referencia y 23 de vigilancia, por encima del mínimo de 49
que exige el protocolo de cartas. Las 136 series aptas son material suficiente para la
actividad 5, aunque las cartas todavía no se han ejecutado y CART01 sigue en `no_medible`.

**Advertencia de independencia.** Las 207 series no son réplicas independientes: comparten
empresa, y las empresas comparten régimen regulatorio y operador. Vale la misma precaución
que ya se declaró para CHEC.

## Bloque 3 · Datos críticos

Las medidas de consumo, que son la razón de incorporar esta fuente:

| Variable | Qué aporta |
|---|---|
| `consumo_basico` | Consumo del rango básico o de subsistencia |
| `consumo_complementario` | Consumo por encima del rango básico |
| `consumo_reside_mayor800` | Consumo residencial superior a 800 kWh |
| `facturacion_consumo_basico` | Valor facturado por ese consumo |
| `valor_total` | Valor total de la factura |
| `valor_subsidio` y `porcentaje_subsidio` | Subsidio aplicado |

Lo que la medición encontró, sin necesidad de ejecutar el pipeline completo:

- **R05 da 91,63 %.** Hay **7.686 identificadores de factura repetidos** sobre filas que no
  son copias exactas. La clave `id_factura` es provisional y requiere decisión.
- **R07 encuentra negativos reales.** `valor_total` tiene **103.136 registros negativos**, con
  mínimo de −115.676.002. `consumo_basico` tiene un registro en −43.
- **R06 detecta tres variantes de escritura** entre las 91 empresas, todas por espacio final:
  `'P'` frente a `'P '` en `tipo_conexion`, `'1'` frente a `'1 '` en `estrato_sector` y `'N'`
  frente a `'N '` en `tipo_factura`. Son cuatro registros cada una; el porcentaje redondea a
  100 % y por eso el conteo se registra en la nota del control.
- **R11 marca 457 importes** dentro del rango de serial de fecha de Excel.
- **`dias_facturados` llega a 33.** Ningún mes del calendario tiene 33 días.
- **`porcentaje_subsidio` va de −1 a 0.** El signo no está explicado.

## Bloque 4 · Unidades y significado

Aquí esta fuente establece un caso extremo que conviene documentar tal cual.

### El publicador no define absolutamente nada

De las **29 columnas, ninguna trae descripción** en el metadato oficial del portal. Y la
descripción del conjunto es su propio título repetido palabra por palabra:

> Nombre: «Información Comercial para el Sector Residencial y No Residencial»
> Descripción: «Información Comercial para el Sector Residencial y No Residencial»

Por eso DEF01 da **0 %** y queda en estado `medido`: no es que falte evidencia para
evaluarlo, es que la evidencia existe y dice que no hay ninguna definición.

Esto completa un patrón en las tres fuentes del proyecto:

| Fuente | Defecto de definición |
|---|---|
| EPM | Documenta un concepto, Cfm,j, que no publica en ninguna fila |
| CHEC | Define de forma circular: `tipomed` se describe como «tipomed» |
| SSPD | **No define ninguna de sus 29 columnas** |

Tres publicadores distintos, tres formas de la misma falla. Deja de ser una anécdota de una
fuente y pasa a ser un patrón del sector, que es un argumento bastante más fuerte para el
marco.

### Consecuencias concretas de esa ausencia

- **La unidad del consumo no está declarada.** Se presume kWh por el nombre de
  `consumo_reside_mayor800`, pero es una inferencia del equipo, no un dato de la fuente.
- **La convención de signo del subsidio no está declarada.** Los datos muestran que la fuente
  lo registra negativo de forma sistemática: 90.469 de los 91.840 registros del censo de
  detalle. R07 lo excluye a propósito, porque contarlo como defecto sería confundir una
  convención no documentada con un error. La ambigüedad se registra en DEF01, que es su sitio.
- **`codigo_conexion` mezcla tres cosas distintas** en un mismo campo: códigos como `1` o
  `CN`, el texto `No Aplica` y nombres de municipio como `TIERRALTA`.
- **`estrato_sector` mezcla dominios**: estratos 1 a 6 junto con las letras C, O, P e I.
- **`tension` tiene 40 valores distintos**, uno de ellos la cadena literal `None`.

Todo esto quedó registrado en [`sspd.yaml`](../../fuentes_datos/diccionarios/sspd.yaml), con
cada lectura de significado marcada como inferida. No se inventaron catálogos ni unidades.

## Bloque 5 · Consumidor del dato

**Pendiente de decisión del equipo.** Ver la sección siguiente.

---

# Ficha 4 · SSPD-NR — Información comercial no residencial

Esta ficha cubre la cuarta fuente. Entra para resolver la limitación declarada de la
Ficha 3: aquella aporta los 59 meses que exigen las cartas pero es de Zonas No
Interconectadas, mientras esta es del **Sistema Interconectado Nacional** y trae la tarifa
aplicada y el eje de propiedad. Ninguna de las dos sola cubre lo que cubren juntas.

## Bloque 1 · Identificación y estructura

| | |
|---|---|
| Conjunto | `bnkp-xdb7` |
| Publicador | Superintendencia de Servicios Públicos Domiciliarios |
| Portal | https://www.datos.gov.co/d/bnkp-xdb7 |
| Filas | **402.500** |
| Columnas en origen | 48 |
| Naturaleza | Registro de facturación **no residencial** |
| Ámbito | **Sistema Interconectado Nacional.** 28 prestadores en 14 departamentos |
| Periodicidad declarada | Semestral |
| Última carga de datos | 26 de mayo de 2023 |

Los prestadores principales son Electrificadora del Meta (137.846 registros), Energía de
Casanare (126.947), Electrificadora del Huila (61.715) y Energía del Bajo Putumayo
(36.052). El territorio es el de los Llanos y la Amazonía: Meta, Casanare, Huila, Putumayo,
Guaviare y Caquetá.

**La copia conservada está normalizada.** El censo completo pesa 137,6 MB y GitHub bloquea
archivos de más de 100 MB. El peso venía de columnas denormalizadas: el nombre de la empresa
repetido en cada fila ocupaba 15,8 MB por sí solo. Por eso se conservan dos archivos:

| Archivo | Contenido |
|---|---|
| `sspd_bnkp-xdb7.csv` | Las 402.500 filas con las 27 columnas analíticas, 71 MB |
| `sspd_bnkp-xdb7_catalogos.csv` | Los 569 pares código-nombre observados, con su conteo |

No se pierde evidencia: si un código resuelve a varios nombres, el catálogo trae una fila
por cada uno, que es justamente lo que INT02 necesita medir.

**Lo que aporta y las otras no tienen:**

- **`tarifa_aplicada`**, promedio 758,98 $/kWh. Es el costo unitario que EPM y CHEC publican
  como especificación, aquí aplicado a facturas concretas.
- **`car_t440_car_inver`** con valores 100, 50 y 0: el eje de propiedad del activo. Por eso
  **R08 y R09 vuelven a aplicarse**, cuando en la Ficha 3 quedaron `no_aplica`.
- **Energía reactiva**, hasta 650.764.
- **Pares código-nombre**, que devuelven a INT02 un caso donde medirse.

## Bloque 2 · Cobertura temporal y series

| | |
|---|---|
| Ventana | julio 2021 a junio 2022 |
| Períodos presentes | **12** |
| Períodos esperados | 12 |
| Huecos internos | ninguno |

**Doce períodos no alcanzan.** El protocolo exige 49, así que **CART01 no es ejecutable
sobre esta fuente** y así queda registrado. Para las cartas sirve la Ficha 3.

Y hay un defecto de completitud que la descripción del portal no menciona: **el volumen se
desploma dentro de la propia ventana.**

```
2021-07   101.608          2022-01    18.934
2021-08   101.986          2022-02    18.901
2021-09    72.384          2022-03    19.087
2021-10    24.936          2022-04     4.644
2021-11    18.346          2022-05       977
2021-12    19.709          2022-06       988
```

De 101.608 a 977. Los últimos tres períodos están prácticamente vacíos, de modo que los
períodos **útiles son unos nueve**, no doce. Cualquier agregado por período debe declararlo
o comparará cosas incomparables.

## Bloque 3 · Datos críticos

Resultados medidos sobre el censo completo:

| Control | Resultado | Qué dice |
|---|---|---|
| R05 | 99,99 % | 53 identificadores de factura repetidos sobre 402.500 |
| **R08** | **92,24 %** | 202 de 219 grupos respetan el orden de tarifa por propiedad |
| **R09** | **98,60 %** | 336.682 de 341.474 facturas reconcilian |
| **INT02** | **98,75 %** | 555 de 562 claves resuelven a un único nombre |
| R11 | 1,17 % | 51.878 importes caen en el rango de serial de fecha |
| R12 | 8,33 % | 28.458 consumos superan diez veces la mediana |

R11 y R12 son indicadores de **prevalencia**: un valor alto señala más sospecha, no mejor
calidad. En esta fuente ambos son bastante más altos que en las otras tres, lo que es
esperable en consumo no residencial, mucho más disperso que el residencial.

### El hallazgo más útil: la relación de la contribución

Al formular R09 supuse que `facturacion_por_consumo = consumos × tarifa_aplicada`. Daba
**12,99 %**, lo que habría sido un defecto enorme. No lo era: el criterio estaba mal.

La razón entre lo facturado y el producto es exactamente **0,833**, que es 1/1,2. La
relación real es:

> **consumos × tarifa_aplicada = facturacion_por_consumo × (1 + contribución)**

`tarifa_aplicada` ya incluye la **contribución de solidaridad**, y la facturación por
consumo no. Lo confirma el propio dato: de las facturas con razón 0,833, el **99,4 % tiene
`valor_de_la_contribucion` igual al 20 % de lo facturado**. Y la tasa varía por sector:

| Sector | Razón dominante | Contribución implícita |
|---|---|---|
| C · comercial | 0,833 (85 %) | 20 % |
| I · industrial | 0,833 (54 %) | 20 % |
| O · oficial | 1,0 (87 %) | exento |
| AP · alumbrado público | 1,0 (89 %) | exento |
| AC · áreas comunes | 1,0 (94 %) | exento |
| IA | 0,909 (80 %) | 10 % |

Con el criterio corregido R09 da **98,60 %**. Queda en `provisional` por una razón
explícita: **la tasa por sector se infirió de los datos, no la documenta la fuente.**

Vale la pena señalar lo que ocurrió aquí, porque es metodológico: un control mal formulado
produjo un 13 % que parecía un defecto grave de la fuente. El defecto estaba en el control.
Antes de reportar un incumplimiento masivo conviene verificar que la regla es correcta.

## Bloque 4 · Unidades y significado

### El mismo vacío de la Ficha 3

**Ninguna de las 48 columnas trae descripción** en el metadato del portal. DEF01 da **0 %**
sobre las 28 variables críticas documentadas, en estado `medido`.

Con esto el patrón queda en cuatro fuentes y tres publicadores:

| Fuente | Defecto de definición |
|---|---|
| EPM | Documenta el concepto Cfm,j, que no publica en ninguna fila |
| CHEC | Define de forma circular: `tipomed` se describe como «tipomed» |
| SSPD | No define ninguna de sus 29 columnas |
| SSPD-NR | No define ninguna de sus 48 columnas |

### Corrupción de codificación en los nombres

Las 7 claves que rompen INT02 no son errores de referencia: son **el mismo nombre publicado
dos veces, una correcta y otra con la codificación dañada**.

```
identificador_empresa 564  → 'EMPRESAS PÚBLICAS DE MEDELLIN E.S.P.'
                           → 'EMPRESAS P�BLICAS DE MEDELLIN E.S.P.'
car_t440_dane 18150000     → 'CAQUETÁ'  /  'CAQUETA'
car_t440_dane 86568033     → 'LA CABAÑA'  /  'LA CABA�A'
```

Dos variantes de defecto conviviendo en el mismo campo: mojibake y tildes inconsistentes.
Es material directo para consistencia, y es exactamente el tipo de defecto que un framework
automatizado debe detectar sin intervención humana.

### Otros rangos que exigen confirmación

- **`car_t440_dias_fact` llega a 152 días.** Un ciclo de facturación de cinco meses.
- **`car_t440_dias_mora` llega a 9.540 días**, unos 26 años de mora.
- **`tarifa_aplicada` tiene mínimo 0.** Hay registros con consumo pero sin tarifa informada.
- **`valor_total_facturado` tiene 1.443 registros negativos.**

Todo quedó en [`sspd_nr.yaml`](../../fuentes_datos/diccionarios/sspd_nr.yaml), con cada
lectura de significado marcada como inferida.

### Una nota sobre oportunidad, para no ilusionarse

Esta fuente trae `car_t440_fec_exp`, fecha de expedición de la factura, y permite medir el
rezago entre el período facturado y la emisión. **Eso es oportunidad del servicio, no del
dato.** OPO01 está especificado sobre la disponibilidad de la publicación, y la propia
matriz prohíbe usar el período como fecha de publicación. Por eso OPO01 sigue en
`no_medible` también aquí: cerrarlo exige reespecificar el control o registrar este rezago
como un indicador distinto. No se fuerza.

Hay además una incoherencia en esas fechas: los períodos 2022-01, 2022-02 y 2022-03 tienen
facturas expedidas el 08-01-**2021**, el 10-02-**2021** y el 10-03-**2021**. Facturas
emitidas un año antes del período que declaran; parece error de año en el origen.

## Bloque 5 · Consumidor del dato

**Pendiente de decisión del equipo.** Ver la sección siguiente.

---

# Bloque 5 común · Consumidor del dato

Es el único bloque que no se mide. Y es el que habilita los umbrales de la matriz OE1, que
hoy están registrados como `propuesta_metodologica_no_aprobada`.

## Candidatos y lo que implica cada uno

| Consumidor | Uso del dato | Exigencia de calidad |
|---|---|---|
| **Regulador** (CREG, Superservicios) | Vigilar cumplimiento tarifario | Tolerancia nula en importes: un error es un cobro indebido. Todos los umbrales a 100 % |
| **Usuario u organización** | Verificar la propia facturación | Exactitud en su categoría y período; el resto del conjunto no le afecta |
| **Investigador o analista sectorial** | Construir y analizar series temporales | Tolera ruido puntual; no tolera huecos temporales ni cambios de estructura |

## Propuesta

Se propone declarar como consumidor al **investigador o analista sectorial**, por tres
razones:

1. **Corresponde al uso real.** El trabajo construye series mensuales y cartas de control,
   no audita facturas individuales.
2. **Es coherente con el diseño de la investigación**, que es metodológico. Declarar al
   regulador obligaría a justificar por qué no se consultó a la entidad.
3. **Hace justificables los umbrales.** Para quien analiza series, la continuidad temporal y
   la estabilidad de la clave pesan más que un importe aislado. Eso explica por qué R01, R05
   e INT01 exigen 100 % mientras R06 puede admitir 99,5 %.

**Si se eligiera al regulador**, todos los umbrales subirían a 100 % y EPM reprobaría
consistencia con su 87,72 % actual. Es una elección legítima, pero cambia el resultado y
debe tomarse de forma consciente.

## Umbrales que se derivan de la propuesta

| Dimensión | Umbral | Fundamento bajo el consumidor propuesto |
|---|---|---|
| Completitud | 100 % en período; por concepto en importes | Un hueco temporal rompe la serie |
| Validez | 100 % | Un valor fuera de dominio no es evaluable |
| Unicidad | 100 % | Una fila repetida distorsiona cualquier agregado |
| Integridad | 100 % | Una clave que se repite no identifica |
| Consistencia | ≥ 99,5 % | Una etiqueta mal escrita se normaliza; no invalida el registro |
| Razonabilidad | Sin umbral; prevalencia | Es una tasa de sospechas, no de errores confirmados |
| Exactitud | Por definir con el diseño muestral | Requiere evidencia externa |
| Oportunidad | Sin numerador disponible | Las fuentes no publican fecha de disponibilidad |

Estos umbrales quedan **propuestos**, no aprobados. Su validación corresponde a la dirección
del trabajo.

---

# Estado del punto 2

| Bloque | EPM | CHEC | SSPD | SSPD-NR |
|---|---|---|---|---|
| 1 · Identificación y estructura | Completo | Completo | Completo, con alcance de copia declarado | Completo, con copia normalizada declarada |
| 2 · Cobertura y series | Completo | Completo, con advertencia de independencia | Completo, con advertencia de independencia | Completo; 12 períodos no habilitan cartas |
| 3 · Datos críticos | Completo | Completo | Completo | Completo |
| 4 · Unidades y significado | Documentado, con tres carencias de la fuente | Documentado, con tres carencias de la fuente | Documentado; la fuente no define ninguna columna | Documentado; la fuente no define ninguna columna |
| 5 · Consumidor del dato | **Pendiente de decisión** | **Pendiente de decisión** | **Pendiente de decisión** | **Pendiente de decisión** |

**Las dos fuentes de consumo son complementarias.** SSPD aporta los 59 períodos que las
cartas exigen; SSPD-NR aporta el régimen interconectado, la tarifa aplicada y el eje de
propiedad. R08, R09 e INT02 quedan `no_aplica` en la primera y medidos en la segunda.

## Pendientes

1. **Decidir el consumidor del dato.** Es la única decisión que bloquea los umbrales.
2. **Someter los umbrales propuestos a la dirección.**
3. **Actualizar la sección 5.8 del anteproyecto**, que describe conjuntos de la CREG y de
   Superservicios y no corresponde a las fuentes efectivamente seleccionadas.
4. **Obtener la unidad de los importes de EPM** y la definición de `tipomed`, `cureal` y
   `subcon` en CHEC. Ambas son consultas a las entidades y alimentan el control DEF01.

## Hallazgos que esta caracterización aporta a otros puntos

- **A la matriz OE1:** el denominador de completitud debe excluir los casos no aplicables
  por nivel; R10 requiere matriz de aplicabilidad por concepto; MAP01 cuenta con respaldo
  documental parcial a partir de la definición de C.S.; INT02 tiene su primer caso
  documentado; DEF01 queda sustentado por la circularidad del metadato de CHEC y, en el
  extremo, por la ausencia total de definiciones en SSPD.
- **Al punto 3 (replicación):** las tres fuentes no comparten estructura. CHEC carece de
  columnas de propiedad equivalentes y de rangos de consumo comparables, de modo que R08 y
  R09 no se trasladan literalmente. SSPD va más lejos: es un registro de facturación y no
  tiene los ejes tarifarios en absoluto, de modo que R08, R09 e INT02 quedan `no_aplica`.
  El informe de diferencias debe distinguir «no aplica» de «no medible».
- **Al consumo observado:** SSPD es la única fuente con consumo medido. Permite cruzar el
  precio que publican EPM y CHEC con una cantidad, cosa que ninguna de las dos sostiene sola.
- **A los resultados del Hito 4:** el remuestreo en CHEC debe hacerse por mercado y nivel, no
  por serie, y la limitación de independencia debe declararse.
