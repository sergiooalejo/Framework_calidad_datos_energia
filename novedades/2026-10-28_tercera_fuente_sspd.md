# 28 de octubre de 2026 · Incorporación de una tercera fuente con consumo observado

**Autora del cambio:** Laura Medina.
**Sobre el trabajo previo de:** Najhery Soler (matriz OE1) y la medición del 28 de octubre.

Esta nota explica por qué entra una tercera fuente, qué criterio hubo que relajar y qué
limitaciones quedan declaradas, para que el equipo y la dirección puedan revisarlo sin leer
el diff.

## Qué se buscaba

Una fuente adicional del sector energético que cumpliera cuatro condiciones: energía
eléctrica, con datos de **consumo**, más de 4.000 registros y actualización mensual. Además
tenía que parecerse a EPM y CHEC para no romper la identidad del proyecto.

La razón de fondo está escrita en el propio repositorio. El README de `fuentes_datos` decía:

> «Ambos contienen tarifas/costos, no consumo observado.»

## Qué se encontró al buscar

Se censó el catálogo nacional completo: **2.138 fichas revisadas**, 128 con nombre de
energía, y de esas **24 con alguna columna de consumo**, a las que se les leyeron las
columnas reales en lugar de confiar en el metadato del buscador.

**Ninguna cumple las cuatro condiciones a la vez.** El resultado es nítido:

| Conjunto | Filas | Períodos mensuales | Última carga de datos |
|---|---|---|---|
| `ebby-cjha` | 11.905.557 | **59** | 2023-10-28 |
| `gw2d-7n7y` | 93.989.182 | 12 (solo 2021) | 2022-10-03 |
| `iirc-i7tb` | 3.183.499 | 11 | 2023-05-23 |
| `bnkp-xdb7` | 402.500 | 12 | 2023-05-26 |
| `p62q-r7ag` | 1.939.317 | 11 | 2023-06-01 |

Los conjuntos de consumo eléctrico que siguen cargando datos son diminutos: `tq63-itzr`
tiene 2.786 filas y `bff2-84yc` tiene 92. Los grandes están congelados desde 2022 o 2023.

**La combinación pedida no existe hoy en los datos abiertos de Colombia.** No es que no se
encontrara: no está publicada.

## Qué criterio se relajó y por qué ese

Se relajó la **actualización mensual**. El razonamiento: las cartas de control necesitan una
serie mensual **histórica** de al menos 49 meses, no un flujo vivo. Que no lleguen períodos
nuevos no afecta un análisis sobre 59 meses ya publicados. Soltar cualquiera de los otros
tres criterios sí rompía algo: sin consumo no se cierra la brecha, sin volumen no hay
estadística, sin semejanza se cae la identidad del proyecto.

Y hay una lectura que juega a favor: una fuente que declara una periodicidad y no la cumple
es **materia de la dimensión de oportunidad**, no una razón para descartarla.

## La fuente incorporada

**`ebby-cjha` — Información Comercial para el Sector Residencial y No Residencial**, de la
Superintendencia de Servicios Públicos Domiciliarios.
https://www.datos.gov.co/d/ebby-cjha

- 11.905.557 filas y 29 columnas en origen.
- **59 períodos mensuales consecutivos**, de julio 2017 a mayo 2022, sin huecos internos.
- Consumo en `consumo_basico`, `consumo_complementario` y `consumo_reside_mayor800`.
- 207 series empresa-estrato; **136 alcanzan los 49 meses** que exige el protocolo.

### No se conserva íntegra, y eso está declarado

Pesa unos **9,7 GB** en origen. Se conservan **dos censos declarados, no muestras**:

| Archivo | Filas | Universo |
|---|---|---|
| `sspd_ebby-cjha_mensual.csv` | 15.075 | Las 91 empresas y los 59 períodos, agregados |
| `sspd_ebby-cjha_detalle.csv` | 91.840 | Todos los registros de la empresa 28111 |

El alcance de cada uno está escrito en `diccionarios/sspd.yaml` y se repite en cada
resultado que lo use. Un censo de una subpoblación declarada es defendible; una muestra sin
criterio no lo sería.

## Dos limitaciones que el equipo debe conocer

**1. Es de Zonas No Interconectadas.** Se verificaron las 91 empresas una por una contra el
directorio de Superservicios: **ninguna pertenece al Sistema Interconectado Nacional**. Son
San Andrés, Amazonas, Guainía, Vichada, Chocó, la costa de Nariño. No aplica la fórmula de
la Resolución CREG 119 de 2007 ni comparte los ejes tarifarios de EPM y CHEC.

Por eso **R08, R09 e INT02 quedan `no_aplica`**, un estado nuevo que se añadió a la matriz y
que significa que el concepto no existe en el esquema. Es distinto de `no_medible`, que es
falta de evidencia. La diferencia importa para el informe del punto 3.

**2. Hay que decidir si eso es aceptable.** Si la dirección exige que las tres fuentes
compartan régimen tarifario, esta fuente no sirve y no hay ninguna otra con consumo en
Colombia. Conviene plantearlo en la próxima reunión antes de que lo pregunten.

A cambio aporta **91 publicadores en un mismo esquema**. Validar el framework en dos
empresas grandes y después en 91 operadores pequeños con poca capacidad de reporte es un
argumento de transferibilidad más fuerte que tres empresas grandes.

## Lo que la medición encontró de inmediato

- **R05 da 91,63 %:** 7.686 identificadores de factura repetidos.
- **R07 encuentra negativos reales:** 103.136 registros con `valor_total` negativo, y uno
  con `consumo_basico` en −43.
- **R06 detecta tres variantes de escritura** entre las 91 empresas, todas por espacio final:
  `'P '`, `'1 '` y `'N '`.
- **R11 marca 457 importes** en el rango de serial de fecha de Excel.
- **`dias_facturados` llega a 33.** Ningún mes tiene 33 días.

## El hallazgo que más sirve a la tesis

**El publicador no define ninguna de sus 29 columnas**, y la descripción del conjunto repite
su propio título palabra por palabra. Por eso DEF01 da **0 %** en estado `medido`: no falta
evidencia, la evidencia dice que no hay definiciones.

Con esto se completa un patrón en los tres publicadores:

| Fuente | Defecto de definición |
|---|---|
| EPM | Documenta el concepto Cfm,j, que no publica en ninguna fila |
| CHEC | Define de forma circular: `tipomed` se describe como «tipomed» |
| SSPD | No define ninguna de sus 29 columnas |

Deja de ser una anécdota de una fuente y pasa a ser un patrón del sector.

## Qué cambió en los entregables

- **Punto 1 (matriz OE1):** de 38 a **57 filas**, 19 controles por tres fuentes. El YAML gana
  el bloque `fuentes.sspd` y, por control, su `aplicabilidad` y su `resultado`. El Markdown
  regenera la tabla con tres columnas.
- **Punto 2 (fichas):** se añade la **Ficha 3** con sus bloques 1 a 4. El bloque 5 sigue
  pendiente para las tres.
- **Cobertura:** de 15 a **17 de los 19 controles** con valor en al menos una fuente. MAP01 y
  DEF01 dejan de estar vacíos. Siguen sin valor OPO01 y CART01.
- **Código:** `medir_matriz_oe1.py` pasa de dos fuentes a N, y la medición de la tercera vive
  en `medir_sspd.py` porque su esquema es de facturación y no tarifario.

## Una corrección que conviene registrar

En la primera versión de la medición, R11 y R12 se calcularon como **conformidad** para la
nueva fuente, cuando en EPM y CHEC están definidos como **prevalencia**: el numerador son los
casos sospechosos, no los correctos. Daba 99,96 % donde debía dar 0,04 %. Se corrigió antes
de publicar, pero vale como recordatorio de que al añadir una fuente hay que releer la
definición de cada control, no solo copiar el cálculo.
