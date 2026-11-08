# Hito 4.4 · Regla de alerta sistémica

Fecha: 7 de noviembre de 2026. Corresponde a la actividad 4 del Hito 4: *«Si más de X % de las series alertan en el
mismo mes, se clasifica como cambio regulatorio y no como error de dato; calibrar X con feb-2020 (51 de 83), jul-2020 (24)
y jul-2021 (18). Contrastar con resoluciones CREG y publicaciones tarifarias de EPM de esos meses»*. Entrega el catálogo
de alertas sistémicas del Hito 4. No modifica 4.1, 4.2 ni 4.3.

## Resultado en seis frases

1. **Se reproducen las cifras del plan** desde los archivos del Hito 2: 51 de 83 series en feb-2020 (61,4 %),
   24 en jul-2020 (28,9 %) y 18 en jul-2021 (21,7 %). Pero provienen de un protocolo distinto
   al del Hito 3 (origen fijo y diferencia absoluta). Con cambios logarítmicos y ventana móvil, **solo febrero de 2020 es sistémico
   en todas las variantes** (49 %–67 % de las series); jul-2020 (6 %–44 %) y
   jul-2021 (0 %–16 %) dependen de la ventana, del método y de las etiquetas.
2. **X no se puede calibrar de forma única con esos tres meses**: en ninguna variante hay un X que capture los tres sin marcar otros.
   Incluso con las cifras del Hito 2, abril de 2020 (24,1 %) supera a jul-2021 (21,7 %): un X por debajo de 21,7 %
   los captura a los tres pero también marca abril. Los tres meses tampoco son del mismo tipo: involucran
   11, 5 y
   3 componentes tarifarios, respectivamente.
3. **Se propone X = 25 % como valor de trabajo, no aprobado.** En las cuatro variantes con etiquetas canónicas solo marca meses del plan (ningún otro mes),
   enmascara como máximo 8,2 % de los errores individuales inyectados (con X = 10 % llega a 26,2 %) y
   reclasifica entre 28 % y 53 % de las alertas reales de EPM (según el método).
4. **Contraste externo.** Las publicaciones oficiales de EPM leídas (ene, feb, jun y jul de 2020; jun y jul de 2021) muestran que los
   componentes que alertan son los que cambiaron: en feb-2020 el costo G,T y pérdidas (+25,8 %) y la distribución (+7,8 %); en
   jul-2020 el transporte STN (−20,3 %), el margen de comercialización (+7,2 %) y la distribución (+5,2 %); en jul-2021 el transporte STN
   (−13,3 %), que es **un solo componente** (con I-MR, las 15 series de ese componente), y Restricciones (+147 %, según el Hito 2). Los valores del CSV
   coinciden con las publicaciones, de modo que no son errores de captura. Además CHEC alerta con **270 de 270 series
   en feb-2020** (I-MR, ref. 36): el fenómeno no es exclusivo de EPM.
5. **La regla no debe descartar alertas, solo reclasificarlas para revisión.** A X = 25 % la simulación de 4.2 oculta
   80 %–100 % de los errores *colectivos* (un error masivo en el mismo mes, p. ej. ×1000 en todas las series, es
   indistinguible de un cambio regulatorio solo por fracción): el rótulo es «candidato sistémico» y confirmarlo exige el contraste con la publicación.
6. **Hallazgo colateral que afecta a 4.1 y 4.2:** EPM cambia la escritura de varias etiquetas entre meses (p. ej. «Costo compra: Gm, i» y
   «Costo Compra: Gm, i») y, sin normalizarlas, una misma serie se parte: 266 series con etiquetas originales frente a
   200 con las equivalencias aprobadas internamente en el Hito 2 ([inventario_series_por_variante.csv](inventario_series_por_variante.csv)). Aquí se usan las canónicas como variante principal y las originales como sensibilidad.

## 1. La regla

Para una fuente y un mes: `fracción = series con alerta / series evaluadas ese mes`. El mes es **candidato sistémico** si
`fracción > X` (desigualdad estricta) **y** se evaluaron al menos 10 series. Las alertas de ese mes no se eliminan: pasan a la cola de
«candidatos sistémicos» y se revisan contra la publicación. El mínimo de 10 series evita que dos series que alertan juntas
(100 %) se lean como un cambio de mercado; 4.2 usaba 2 como mínimo técnico para la sensibilidad, aquí se exige un denominador interpretable.
`regla_sistemica.py` implementa la regla y sus pruebas están en `test_regla_sistemica.py`.

**Amplitud (diagnóstico, no parte de la regla).** Las series de EPM están replicadas por columna, nivel de tensión y tipo de tarifa: un solo
componente puede agrupar hasta 15 series, de modo que una fracción alta puede ser «un componente» y no «el mercado». Se reporta, además,
cuántos componentes distintos alertan:

| Mes | Hito 2: series · componentes con alerta | I-MR ref. 36: series · componentes | MAD 3σ ref. 36: series · componentes |
|---|---|---|---|
| feb-2020 | 51 de 83 · 11 componentes | 38 de 69 · 11 de 14 | 45 de 69 · 11 de 14 |
| jul-2020 | 24 de 83 · 5 componentes | 4 de 69 · 2 de 14 | 18 de 69 · 4 de 14 |
| jul-2021 | 18 de 83 · 3 componentes | 15 de 142 · 1 de 17 | 0 de 142 · 0 de 17 |

## 2. Protocolo

- **Ventana móvil sin fuga de futuro.** El mes *m* se evalúa con los W cambios logarítmicos anteriores (W = 24 y 36), solo entre meses consecutivos y sin
  imputar. Así cualquier mes se puede evaluar sin que el futuro entre en la referencia (prueba automática). Es la extensión natural del protocolo 4.1/4.2,
  cuya vigilancia fija de 12 meses finales no alcanza a cubrir feb-2020 ni jul-2020 en EPM.
- **Dos métodos:** I-MR clásica (2,66 y 3,267) y Z-score robusto con MAD 3σ; con MAD cero, señal si el cambio difiere de la mediana (4.1/4.2).
- **Variantes de EPM:** etiquetas canónicas (principal) y originales; W = 24 y 36; dos métodos; más la **reproducción del Hito 2** (83 series, origen fijo, diferencia absoluta).
- **Cuarentena EPM** de 3.7 aplicada igual que en 4.1. No se modifica ningún CSV fuente.
- **Una limitación del origen móvil:** la referencia de los meses posteriores a feb-2020 contiene su salto, lo que ensancha los límites I-MR;
  puede explicar por qué I-MR ref. 36 no señala jul-2020 (5,8 %) y MAD, más robusto, sí. Es una hipótesis no contrastada
  (no se probó excluir los meses sistémicos de la referencia).

![Fracción mensual de EPM](figuras/01_fraccion_mensual_epm.png)

## 3. Calibración de X

Para cada variante se calcula la banda de X que capturaría los tres meses del plan sin marcar ningún otro. Si el mayor valor de los otros
meses es mayor o igual que el menor de los tres, la banda no existe:

| Variante (EPM) | feb-2020 | jul-2020 | jul-2021 | X mínimo para no marcar otro mes | X máximo para capturar los tres | ¿Banda factible? | En X = 25 %: eventos · meses marcados |
|---|---|---|---|---|---|---|---|
| I-MR, ref. 36 | 55,1 % | 5,8 % | 10,6 % | 24,6 % | 5,8 % | no | 1 de 3 · 1 |
| MAD 3σ, ref. 36 | 65,2 % | 26,1 % | 0,0 % | 14,5 % | 0,0 % | no | 2 de 3 · 2 |
| I-MR, ref. 24 | 57,0 % | 14,1 % | 0,0 % | 22,5 % | 0,0 % | no | 1 de 3 · 1 |
| MAD 3σ, ref. 24 | 67,1 % | 25,4 % | 0,0 % | 18,8 % | 0,0 % | no | 2 de 3 · 2 |
| Hito 2 (origen fijo, 83 series) | 61,4 % | 28,9 % | 21,7 % | 24,1 % | 21,7 % | no | 2 de 3 · 2 |

(Valores de «X máximo» iguales a 0 % indican que algún mes del plan no tiene ninguna alerta en esa variante.) En ninguna variante la banda es factible.
Variantes con etiquetas originales: ver [calibracion_resumen.csv](calibracion_resumen.csv); el X que maximiza la exactitud balanceada
va de 5 % a 44 % según la variante: **no es un óptimo estable**.

![Calibración](figuras/03_calibracion_X.png)

**Criterio para el valor de trabajo.** Sin etiquetas confirmadas no hay un óptimo; se propone X = 25 % porque (a) captura febrero de 2020 en las 9 variantes (su fracción mínima es 49 %)
y 5 de 9 capturan además jul-2020; jul-2021 no se captura en ninguna;
(b) en las variantes canónicas no marca ningún mes ajeno al plan; (c) su costo para errores individuales es bajo (siguiente sección); y (d) supera lo que aportaría un
solo componente aunque todas sus series alertaran: como máximo 13,0 % (15 de 115 series en 2020-03;
[tamano_componentes_epm.csv](tamano_componentes_epm.csv)). Con X = 10 % un solo componente ya sería «sistémico». Es un valor de arranque para revisar con el director, no una calibración cerrada.

## 4. Efecto de X: alertas reales y costo de enmascaramiento

Meses clasificados como sistémicos y fracción de alertas reales que se reclasifican (ventana móvil, referencia 36):

| Fuente | Método | X = 10 %: meses sistémicos · alertas reclasificadas | X = 25 % | X = 50 % |
|---|---|---|---|---|
| EPM | I-MR | 7 meses · 86 % | 1 mes · 28 % | 1 mes · 28 % |
| EPM | MAD 3σ | 5 meses · 82 % | 2 meses · 53 % | 1 mes · 38 % |
| CHEC | I-MR | 28 meses · 96 % | 24 meses · 90 % | 9 meses · 46 % |
| CHEC | MAD 3σ | 40 meses · 94 % | 28 meses · 77 % | 7 meses · 28 % |
| SSPD | I-MR | 3 meses · 14 % | 0 meses · 0 % | 0 meses · 0 % |
| SSPD | MAD 3σ | 9 meses · 51 % | 0 meses · 0 % | 0 meses · 0 % |

En EPM, X = 10 % reclasificaría más del 80 % de las alertas (la regla dejaría de discriminar); X = 25 % reclasifica entre 28 % y 53 % y X = 50 % solo febrero de 2020. En CHEC,
24 de 187 meses evaluables superan el 25 % (I-MR): la mayor parte de sus alertas ocurre en meses en que casi toda la fuente cambia a la vez. En SSPD la fracción mensual
máxima es 14,4 % (referencia 36, ambos métodos): **con X = 25 % la regla no se activa y todas sus alertas siguen en revisión individual**.

![CHEC y SSPD](figuras/02_fraccion_mensual_chec_sspd.png)

**Costo para detecciones de errores conocidos** (tomado de 4.2, inyecciones, referencia 36, cohorte común, horizonte t o t+1; fracción de detecciones que la regla enmascararía):

| Fuente | Método | Individual X=10 % | X=25 % | X=50 % | Colectivo X=10 % | X=25 % | X=50 % |
|---|---|---|---|---|---|---|---|
| EPM | I-MR | 11,6 % | 8,2 % | 0,0 % | 100,0 % | 100,0 % | 100,0 % |
| EPM | MAD 3σ | 2,8 % | 0,8 % | 0,0 % | 100,0 % | 100,0 % | 100,0 % |
| CHEC | I-MR | 0,0 % | 0,0 % | 0,0 % | 100,0 % | 100,0 % | 85,5 % |
| CHEC | MAD 3σ | 0,0 % | 0,0 % | 0,0 % | 100,0 % | 100,0 % | 100,0 % |
| SSPD | I-MR | 2,7 % | 0,1 % | 0,0 % | 100,0 % | 79,9 % | 79,9 % |
| SSPD | MAD 3σ | 26,2 % | 0,1 % | 0,0 % | 100,0 % | 100,0 % | 74,0 % |

El enmascaramiento de errores individuales es bajo a X ≥ 25 % y crece cuando X baja; el de errores colectivos es de 74 %–100 % incluso con X = 50 %.
Por eso la regla **etiqueta**, no suprime.

## 5. Contraste con las publicaciones oficiales de EPM

Se leyeron las publicaciones tarifarias de EPM de enero, febrero, junio y julio de 2020 y de junio y julio de 2021 (tabla monomia, nivel I). Su transcripción se verificó de dos maneras:
(1) coincide con el CSV en las 108 celdas (componente × columna × mes) y (2) la suma de componentes reproduce el CU total publicado (tolerancia 0,02) —
[verificacion_transcripcion_pdf.csv](verificacion_transcripcion_pdf.csv) y [verificacion_suma_componentes.csv](verificacion_suma_componentes.csv). De paso, esto suma evidencia de exactitud de EPM para cinco
meses nuevos (feb, jun y jul de 2020; jun y jul de 2021) y otras filas de enero (EXA01 usaba seis filas de ene/dic-2020 y abr/dic-2021); la matriz OE1 de 3.1 no se modifica.

**Febrero de 2020 (enero → febrero).** Las alertas «por componente» cuentan todas las series del componente (todos los niveles y tipos de tarifa); el cambio publicado es el de nivel I, columna Propiedad EPM:

| Componente | 2020-01 | 2020-02 | Cambio publicado | Alertas I-MR (ref. 36) | Alertas MAD (ref. 36) | Alertas Hito 2 | Nota |
|---|---|---|---|---|---|---|---|
| Costo compra: Gm, i | 210,50 | 228,24 | 8,4 % | 0/6 | 0/6 | 0 |  |
| Cargo transporte STN: Tm | 33,62 | 35,41 | 5,3 % | 0/6 | 0/6 | 0 |  |
| Cargo transporte SDL: Dn,m | 191,79 | 206,68 | 7,8 % | 2/3 | 1/3 | 6 |  |
| Margen comercialización: CVm,i,j | 45,60 | 46,02 | 0,9 % | 0/9 | 0/9 | 0 |  |
| Costo G,T, pérdidas: PRn,m | 38,93 | 48,98 | 25,8 % | 9/9 | 9/9 | 9 |  |
| Restricciones: Rm | -0,25 | 2,03 | cruza cero | 3/3 | 3/3 | 0 |  |
| CU total (publicado) | 520,20 | 567,36 | 9,1 % | — | — | — |  |

**Julio de 2020 (junio → julio).**

| Componente | 2020-06 | 2020-07 | Cambio publicado | Alertas I-MR (ref. 36) | Alertas MAD (ref. 36) | Alertas Hito 2 | Nota |
|---|---|---|---|---|---|---|---|
| Costo compra: Gm, i | 221,40 | 222,30 | 0,4 % | 0/6 | 0/6 | 0 |  |
| Cargo transporte STN: Tm | 43,10 | 34,33 | -20,3 % | 0/6 | 6/6 | 6 |  |
| Cargo transporte SDL: Dn,m | 206,40 | 217,22 | 5,2 % | 3/3 | 0/3 | 6 |  |
| Margen comercialización: CVm,i,j | 48,55 | 52,03 | 7,2 % | 0/9 | 9/9 | 9 |  |
| Costo G,T, pérdidas: PRn,m | 48,92 | 48,93 | 0,0 % | 0/9 | 0/9 | 0 |  |
| Restricciones: Rm | 4,55 | 6,41 | 40,9 % | 0/3 | 0/3 | 0 |  |
| CU total (publicado) | 572,92 | 581,22 | 1,4 % | — | — | — | fila «CU CREG 012 de 2020»: 567,36 |

**Julio de 2021 (junio → julio).** La publicación de julio no se encontró con las primeras variantes de URL; el enlace real, tomado de la página «Tarifas años anteriores energía» de EPM, incluye el día («16_julio_2021»).

| Componente | 2021-06 | 2021-07 | Cambio publicado | Alertas I-MR (ref. 36) | Alertas MAD (ref. 36) | Alertas Hito 2 | Nota |
|---|---|---|---|---|---|---|---|
| Costo compra: Gm, i | 228,62 | 221,74 | -3,0 % | 0/15 | 0/15 | 0 |  |
| Cargo transporte STN: Tm | 47,93 | 41,57 | -13,3 % | 15/15 | 0/15 | 6 |  |
| Cargo transporte SDL: Dn,m | 236,60 | 231,74 | -2,1 % | 0/15 | 0/15 | 6 |  |
| Margen comercialización: CVm,i,j | 51,20 | 52,72 | 3,0 % | 0/15 | 0/15 | 0 |  |
| Costo G,T, pérdidas: PRn,m | 49,91 | 47,80 | -4,2 % | 0/15 | 0/15 | 0 |  |
| Restricciones: Rm | 11,50 | 28,40 | 147,0 % | 0/6 | 0/6 | 6 |  |
| CU total (publicado) | 625,76 | 623,97 | -0,3 % | — | — | — | fila «CU CREG 012 de 2020»: 593,99 |

![Cambios publicados](figuras/04_contraste_publicaciones_epm.png)

Lectura, acotada a lo observado:

- Las alertas caen en componentes que la publicación muestra con cambios apreciables: costo G,T y pérdidas (+25,8 %) y distribución (+7,8 %) en febrero; transporte STN (−20,3 %), margen de comercialización (+7,2 %) y distribución (+5,2 %) en julio de 2020.
  En julio de 2020 **qué componente alerta depende del método** (con I-MR ref. 36 solo la distribución; con MAD, STN y margen; en el Hito 2, los tres). Como los valores del CSV coinciden con la publicación, esas alertas **corresponden a cambios publicados y no a errores de captura**.
- No todo cambio alerta: en febrero el costo de compra (+8,4 %) y el STN (+5,3 %), y en julio de 2020 Restricciones (+40,9 %), no alertan en ninguna variante. Es compatible con una variabilidad histórica alta de esas series; no se verificó.
- **La hipótesis del Hito 2 solo se respalda en parte.** La revisión del Hito 2 atribuye febrero-2020 «probablemente» a la entrada de los cargos de distribución de la CREG 015 de 2018. Aquí la distribución sube +7,8 %, pero el costo G,T y pérdidas sube +25,8 % y el costo de compra +8,4 %:
  el cambio no se limita a los cargos de distribución.
- **Resolución CREG 012 de 2020** (opción tarifaria; expedida el 6 de febrero y publicada en el Diario Oficial el 17 de febrero de 2020): sus considerandos citan la 015 de 2018 como motivo, pero no fijan un mes de aplicación para EPM.
  Los encabezados de enero y febrero no citan ninguna resolución de 2020; los de junio y julio añaden CREG 012, 058 y 104 de 2020 y una fila nueva «CU CREG 012 de 2020» (567,36), igual al CU total de febrero, mientras el «CU total» calculado de julio es 581,22.
  Es coherente con que la opción tarifaria mantuviera la tarifa aplicada mientras los componentes seguían moviéndose, pero **no se probó** el mecanismo.
- Restricciones cruza cero entre enero y febrero (−0,25 → 2,03): el protocolo logarítmico excluye esa serie (solo admite valores positivos); otras series del componente sí alertan.
- **Julio de 2021 es un cambio de un solo componente, no de todo el mercado.** El transporte STN baja 13,3 % y es justo el componente cuyas 15 series alertan con I-MR (ref. 36);
  con MAD no alerta ninguna serie, y en el Hito 2 (cambios absolutos, límites fijos) alertan tres componentes: STN, distribución (−2,1 %) y Restricciones (+147,0 %, que sube de 11,50 a 28,40).
  Con X = 25 % ese mes no es «sistémico»: es coherente con que un solo componente no debe reclasificarse como cambio de mercado, aunque sí es un cambio publicado y no un error.
- **Resoluciones CREG leídas.** La **058 de 2020** (expedida el 14 de abril; Diario Oficial del 15 de abril de 2020) fija pagos diferidos de las facturas de abril a junio durante la emergencia sanitaria,
  permite cobrar menos que el máximo aprobado en los cargos de transmisión, distribución y comercialización y remite a la opción tarifaria de la 012. La **104 de 2020** (5 de junio; Diario Oficial del 7 de junio)
  impide que el consumo de subsistencia de los estratos 1 y 2 varíe con el IPC durante la emergencia. Ninguna de las dos fija los valores de los componentes de EPM, así que **explican el contexto regulatorio, no los cambios
  observados**. De la **015 de 2018** solo se verificó de forma literal que se publicó el 3 de febrero de 2018 y su objeto; las reglas de aplicación de los cargos proceden de un resumen de la herramienta de lectura y no se citan como texto.
  Los encabezados de junio y julio de 2021 citan las CREG 012, 104 y 152 de 2020 y la 003 de 2021 (ya no la 058); estas dos últimas no se leyeron.

Fuentes documentales y su estado:

| Id | Mes | Documento | Estado | Límite |
|---|---|---|---|---|
| R1 | 2020-01 | Tarifas y costo de energía eléctrica, enero de 2020 | leido | Los metadatos del PDF (creación 2020-01-16) no son la fecha oficial de publicación. |
| R2 | 2020-02 | Tarifas y costo de energía eléctrica, febrero de 2020 | leido | Los metadatos del PDF (creación 2020-02-14) no son la fecha oficial de publicación. |
| R3 | 2020-06 | Tarifas y costo de energía eléctrica, junio de 2020 | leido | Mes base para comparar con julio de 2020. |
| R4 | 2020-07 | Tarifas y costo de energía eléctrica, julio de 2020 | leido |  |
| R5 | 2020-02 | Resolución CREG 012 de 2020 (opción tarifaria) | leido | El texto no fija un mes de aplicación para cada comercializador; no prueba que EPM la aplicara en febrero de 2020. Las fórmulas están en imágenes y no se leyeron. |
| R6 | 2018-02 | Resolución CREG 015 de 2018 (remuneración de la distribución) | leido_parcialmente | No se verificó literalmente ningún artículo que fije cuándo entran los nuevos cargos de distribución de EPM en las tarifas al usuario; esa fecha depende de la resolución particular de cada operador de red, que no se consultó. |
| R7 | 2021-06 | Tarifas y costo de energía eléctrica, junio de 2021 | leido | El enlace se tomó de la página «Tarifas años anteriores energía» de EPM. |
| R8 | 2021-07 | Tarifas y costo de energía eléctrica, julio de 2021 | leido | Las variantes de URL probadas en la primera búsqueda no funcionaban porque el nombre real incluye el día («16_julio_2021»). |
| R9 | 2020-04 | Resolución CREG 058 de 2020 (medidas transitorias para el pago de facturas) | leido | No establece por sí sola los valores de los componentes de EPM. |
| R10 | 2020-06 | Resolución CREG 104 de 2020 (consumo de subsistencia) | leido | No trata de los componentes del costo unitario ni de los cargos de distribución. |
| R11 | 2021-07 | Resoluciones CREG 152 de 2020 y 003 de 2021 | no_consultado | No se afirma su contenido. |

## 6. Qué no se puede concluir

- **«Candidato sistémico» no es «cambio regulatorio confirmado».** El contraste con las publicaciones oficiales de EPM respalda que feb-2020, jul-2020 y jul-2021 son cambios publicados; solo feb-2020 es amplio (11 componentes). Falta confirmar con EPM o la CREG la causa regulatoria de cada uno.
- **Tres meses no bastan para calibrar.** Los resultados dependen del protocolo; el valor de X es una decisión a aprobar, con esta sensibilidad como insumo.
- **Las series no son independientes** (columnas y niveles replicados): una fracción alta puede ser un solo componente. Por eso se reporta la amplitud, y no se interpreta la fracción como una proporción de eventos independientes.
- **Los costos de enmascaramiento vienen de inyecciones artificiales** (4.2) en la cohorte común de 2021; no se recalcularon con la ventana móvil.
- **Las equivalencias de etiquetas son aprobadas internamente** por el equipo; EPM no las ha confirmado.
- **CHEC y SSPD no tienen contraste externo en este punto.** La coincidencia de feb-2020 en CHEC es evidencia interna entre fuentes, no una verificación documental.

## 7. Qué cierra del plan y qué queda pendiente

Cierra: formalización e implementación de la regla; calibración de X con sensibilidad; catálogo de alertas sistémicas ([catalogo_alertas_sistemicas.csv](catalogo_alertas_sistemicas.csv),
227 filas); contraste con las publicaciones de EPM de feb-2020, jul-2020 y jul-2021; lectura de las CREG 012, 058 y 104 de 2020 y lectura parcial de la 015 de 2018; verificación de las cifras 51/24/18.
**Pendiente:** lectura completa de la CREG 015 de 2018 y de las resoluciones particulares de EPM; lectura de las CREG 152 de 2020 y 003 de 2021; consulta formal a EPM o CREG sobre la causa de cada cambio (plan, Hito 6);
decisión del director sobre X; revisar 4.1/4.2 con etiquetas canónicas; probar la exclusión de meses sistémicos de la referencia.

## Reproducir y auditar

```powershell
python desarrollo_puntos/4.4/calibrar_regla_sistemica.py
python desarrollo_puntos/4.4/informe_regla_sistemica.py
python -m unittest discover -s desarrollo_puntos/4.4 -p test_regla_sistemica.py -v
python desarrollo_puntos/4.4/verificar_resultados.py
```

[configuracion.json](configuracion.json) fija parámetros, versiones y huellas de entradas y de los PDF; [manifiesto_resultados.json](manifiesto_resultados.json) las de todos los archivos entregados.
