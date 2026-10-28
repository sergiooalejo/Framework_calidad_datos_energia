# 28 de octubre de 2026 · Medición de la matriz OE1 (Hito 3, punto 1)

**Autora del cambio:** Laura Medina. **Commits:** `c646822` y `62f8aab`.
**Sobre el trabajo previo de:** Najhery Soler (`c019852`, matriz OE1).

Esta nota resume qué cambió y qué decisiones quedan abiertas, para que el equipo y la
dirección puedan revisarlo sin leer el diff.

## Qué se añadió

La especificación de la matriz no se modificó. Lo que se hizo fue **llenar el casillero
`resultado` que cada control tenía en `null`**, respetando las definiciones de población,
numerador y denominador que ya estaban escritas.

- `docs/hito3/medir_matriz_oe1.py` calcula cada control y escribe el valor dentro de
  `matriz_oe1.csv`, `matriz_oe1.yaml` y `matriz_oe1.md`. Es idempotente y registra el
  SHA-256 de cada archivo medido.
- Los números no se transcriben a mano: se recalculan con
  `python docs/hito3/medir_matriz_oe1.py`.

## Estado resultante

| | |
|---|---|
| Controles con valor | **15 de 19** |
| Dimensiones medidas | **7 de 8** |
| Sin ninguna medición | **oportunidad** |
| Controles sin valor | OPO01, MAP01, DEF01, CART01 |

**El punto 1 no está cerrado.** Cuatro controles siguen sin numerador por falta de
evidencia externa, seis están en `provisional` a la espera de decisiones del equipo, y
ningún umbral está aprobado por dirección.

## Exactitud deja de estar en cero

Superservicios publica los mismos componentes del costo unitario en el conjunto
`td8k-vhq9`, y CHEC aparece ahí con 108 registros. Al ser **otro publicador**, sirve como
fuente de referencia sin depender de que una entidad responda una consulta.

- 756 celdas contrastadas, **756 coinciden**.
- Como un 100 % sin más es sospechoso, se inyectaron 756 valores deliberadamente falsos
  para comprobar que la prueba discrimina: **rechazó el 99,6 %**.
- La referencia quedó versionada en `docs/hito3/referencia_exa01_chec.json` con su
  consulta y fecha de descarga, de modo que el contraste es reproducible sin red.

**Alcance declarado:** solo cubre 2023, no cubre `cureal`, `subcon` ni `valor_tarifa`, y
**no sirve para EPM**, cuyo conjunto termina en diciembre de 2021 mientras la referencia
empieza en 2022. Por eso el control queda en `provisional`, no en `medido`.

## Cuatro hallazgos que exigen decisión

### 1. R10 no detecta columnas enteras en cero

Con unidad de observación **fila**, el control da 100 % en CHEC. Pero la columna `cureal`
tiene **33.871 ceros, el 83,4 % de las filas**. Como toda fila tiene algún importe
informado, el indicador declara conformidad total mientras una columna está vacía.

**Propuesta:** cambiar la unidad de observación de R10 de fila a **celda por columna**. Es
un cambio en la especificación, no en el código.

### 2. Aplicar las definiciones de la matriz corrige tres resultados en EPM

| Control | Lectura ingenua | Con la definición de la matriz |
|---|---|---|
| R05 | 99,72 % | **100 %** |
| R07 | 99,92 % | **100 %** |
| R03 | 99,97 % | **100 %** |

- **R05:** la población exige conservar una fila por clase de copia exacta antes de evaluar
  la clave. Hecho ese paso, no queda ninguna clave repetida: las repeticiones eran las
  mismas filas que ya cuenta R04. Se estaba contando un defecto dos veces.
- **R07:** los 15 importes negativos están **todos** en `Restricciones: Rm`, que es la
  excepción documentada. La excepción describe el dato, no lo relaja.
- **R03:** el denominador son las celdas *informadas*. Las cinco celdas que parecían mal
  formateadas están vacías, y eso pertenece a completitud.

### 3. Los hashes del manifiesto no validan en Windows

`fuentes_datos/verificaciones/manifiesto_archivos.json` registra el SHA-256 de los CSV,
pero al extraer los archivos en Windows `core.autocrlf` convierte LF en CRLF y añade un
byte por línea, de modo que el hash cambia. Convirtiendo el archivo de EPM a LF se obtiene
exactamente el hash del manifiesto.

**No es corrupción.** Es que un hash de archivo de texto solo es verificable si la política
de fin de línea está declarada. **Propuesta:** añadir un `.gitattributes` que trate los CSV
como binarios. Afecta archivos de todo el equipo, así que no se hizo de forma unilateral.

Vale la pena señalar que esto es **evidencia directa para el Hito 6**, que debe medir la
reproducibilidad como resultado y no como herramienta.

### 4. Dos defectos en los metadatos que nadie había leído

- **EPM documenta un concepto que no publica.** La descripción oficial de `tipodedato`
  declara el concepto **Cfm,j ($/factura)** con cinco valores mensuales: dic-2016 = 5.660,
  ene-2017 = 5.642, feb-2017 = 5.699, mar-2017 = 5.757, abr-2017 = 5.784. Ese concepto
  **no existe en ninguna fila del CSV**.
- **CHEC no define sus variables ambiguas.** La descripción oficial de
  `costounitariotarifa_tipomed` es «tipomed» y la de `costounitariotarifa_subcon` es
  «Subcon». Son circulares. La ambigüedad que señala DEF01 **está en la fuente**, no en la
  lectura del equipo, y así puede escribirse en el documento.

A cambio, el metadato de EPM **sí** define `C.S.: Consumo Subsidiado`, lo que da respaldo
documental a las equivalencias de MAP01 (`0-CS` ≡ `Rango 0 - CS`, `Mayor CS` ≡ `Rango > CS`).

## Seis decisiones pendientes del equipo

Seis controles están en `provisional` porque dependen de decisiones no tomadas:

1. ¿Cuál es el catálogo canónico de etiquetas? (R06)
2. ¿Qué dominio de signo aplica a cada concepto? (R07)
3. ¿Qué importes son obligatorios por concepto? (R10)
4. ¿Un cero significa «no aplica»? (R09 y R10)
5. ¿Qué factor usa R12? Hoy está en 10 y con ese valor no detecta nada en CHEC.
6. ¿Cuál es la clave definitiva de CHEC? La provisional deja 1.398 claves repetidas.

## Nota sobre el plan de hitos

El commit `c019852` modificó `docs/plan_hitos_3-6_detallado.md` para que la oportunidad
deje de estar excluida. **El cambio de fondo es correcto**, porque el profesor exige medir
las ocho dimensiones y la exclusión era insostenible.

Lo que conviene corregir es la forma: ese documento lo subió la dirección y el cambio no
lleva nota que lo advierta, a diferencia del resumen DAMA, donde sí se dejó una
actualización fechada. **Se propone añadir la misma nota al plan y comentarlo en la
próxima reunión**, para que la dirección lo sepa por el equipo.
