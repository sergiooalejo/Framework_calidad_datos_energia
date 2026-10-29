# 29 de octubre de 2026 · Cuarta fuente: información comercial no residencial

**Autora del cambio:** Laura Medina.
**Hallazgo de la fuente:** propuesto por el equipo.
**Sobre el trabajo previo:** la tercera fuente incorporada el 28 de octubre.

## Por qué entra

La tercera fuente (`ebby-cjha`) resolvió el consumo observado y la profundidad mensual,
pero tenía una limitación declarada: sus 91 empresas son de **Zonas No Interconectadas**, de
modo que no comparten el régimen tarifario de EPM y CHEC. Esta cuarta fuente resuelve
exactamente eso.

`bnkp-xdb7` es del **Sistema Interconectado Nacional**: 28 prestadores en 14 departamentos
de los Llanos y la Amazonía, encabezados por Electrificadora del Meta, Energía de Casanare y
Electrificadora del Huila. Le aplica el mismo marco regulatorio que a las dos fuentes
tarifarias originales.

Y trae tres cosas que ninguna otra fuente del proyecto tiene:

1. **`tarifa_aplicada`**, promedio 758,98 $/kWh: el costo unitario que EPM y CHEC publican
   como especificación, aquí aplicado a facturas concretas.
2. **`car_t440_car_inver`** con valores 100, 50 y 0: el eje de propiedad del activo.
3. **Energía reactiva** y **pares código-nombre**.

Por eso **R08, R09 e INT02 vuelven a tener dónde medirse**. En la fuente ZNI habían quedado
`no_aplica`.

## Verificación de la propuesta

La descripción con la que llegó la fuente traía tres datos que no se sostienen, y conviene
dejarlos corregidos:

| Se dijo | Lo medido |
|---|---|
| «Tiene consumos en Bogotá» | Meta, Casanare, Huila, Putumayo, Guaviare y Caquetá. **Bogotá no aparece.** |
| «Tiene registros por día, la data está más granulada» | Las fechas son de **factura**, no de consumo. `dias_fact` muestra ciclos de 28 a 32 días: cada fila cubre un mes. |
| «De julio de 2021 a mayo de 2022» | Llega hasta junio de 2022. Son 12 períodos. |

Lo que sí es exacto: 402.500 registros.

Y algo que la descripción no mencionaba: **el volumen se desploma**. De 101.608 registros en
2021-07 a 977 en 2022-05. Los últimos tres períodos están casi vacíos, de modo que los
períodos útiles son unos nueve.

## La copia conservada está normalizada

El censo completo pesa **137,6 MB** y GitHub bloquea archivos de más de 100 MB. El peso
venía de columnas denormalizadas: el nombre de la empresa repetido en cada fila ocupaba
15,8 MB por sí solo.

Se conservan dos archivos en lugar de uno:

| Archivo | Contenido | Peso |
|---|---|---|
| `sspd_bnkp-xdb7.csv` | 402.500 filas × 27 columnas analíticas | 71 MB |
| `sspd_bnkp-xdb7_catalogos.csv` | 569 pares código-nombre con su conteo | 31 KB |

**No se pierde evidencia.** Si un código resuelve a varios nombres, el catálogo trae una
fila por cada uno, que es justamente lo que INT02 mide. Las 21 columnas omitidas están
listadas en el diccionario y en el metadato conservado.

## Dos hallazgos que valen la pena

### 1. La relación de la contribución de solidaridad

Al formular R09 supuse que `facturacion_por_consumo = consumos × tarifa_aplicada`. Dio
**12,99 %**, que habría sido un defecto gravísimo de la fuente. **No lo era: el criterio
estaba mal.**

La razón entre lo facturado y el producto es exactamente **0,833**, o sea 1/1,2. La relación
real es:

> consumos × tarifa_aplicada = facturacion_por_consumo × (1 + contribución)

`tarifa_aplicada` incluye la contribución de solidaridad; la facturación por consumo no. Lo
confirma el propio dato: de las facturas con razón 0,833, el **99,4 % tiene
`valor_de_la_contribucion` igual al 20 % de lo facturado**. Y la tasa cambia por sector:
20 % en comercial e industrial, 10 % en IA, exento en oficial, alumbrado público y áreas
comunes.

Con el criterio corregido **R09 da 98,60 %**.

**La lección es metodológica y conviene registrarla:** un control mal formulado produjo un
13 % que parecía un defecto masivo de la fuente. El defecto estaba en el control. Antes de
reportar un incumplimiento grande hay que verificar que la regla es correcta.

### 2. Corrupción de codificación en los nombres

Las 7 claves que rompen INT02 no son errores de referencia: son **el mismo nombre publicado
dos veces, una correcta y otra con la codificación dañada**.

```
564       → 'EMPRESAS PÚBLICAS DE MEDELLIN E.S.P.' / 'EMPRESAS P?BLICAS DE MEDELLIN E.S.P.'
18150000  → 'CAQUETÁ' / 'CAQUETA'
86568033  → 'LA CABAÑA' / 'LA CABA?A'
```

Mojibake y tildes inconsistentes conviviendo en el mismo campo. Es el tipo de defecto que un
framework automatizado debe detectar sin intervención humana.

*(Nota al margen: EPM aparece en esta fuente con el código 564, pero solo **51 registros**.
Es presencia marginal y no sirve como puente con la fuente tarifaria de EPM.)*

## Qué cambió en los entregables

- **Punto 1 (matriz OE1):** de 57 a **76 filas**, 19 controles por cuatro fuentes.
- **Punto 2 (fichas):** se añade la **Ficha 4** con sus bloques 1 a 4.
- **Cobertura:** sigue en **17 de 19** controles con valor en al menos una fuente. OPO01 y
  CART01 siguen vacíos. Lo que mejoró es la *profundidad*: R08, R09 e INT02 pasan de tener
  una sola fuente medida a tener dos.
- **Código:** `medir_matriz_oe1.py` ya era de N fuentes; se añade `medir_sspd_nr.py`.

## Lo que sigue pendiente

1. **Decidir el consumidor del dato.** Sigue bloqueando todos los umbrales, ahora para
   cuatro fuentes.
2. **OPO01 sigue sin ninguna medición.** La fecha de expedición de factura mide oportunidad
   del *servicio*, no del *dato*. Cerrarlo exige reespecificar el control.
3. **CART01 solo es ejecutable sobre la fuente ZNI**, que es la única con 49 meses o más.
4. **Confirmar con la fuente** la tasa de contribución por sector, los ciclos de 152 días y
   las moras de 9.540 días.
5. **Avisar al director** que el proyecto pasó de dos a cuatro fuentes y por qué. Cada una
   arrastra la obligación de las ocho dimensiones, y esa obligación no está cerrada en
   ninguna.
