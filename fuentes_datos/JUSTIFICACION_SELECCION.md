# Justificación de selección: EPM y CHEC

Fecha de organización: 27 de octubre de 2026.

Se seleccionan dos casos de registros administrativos tarifarios de energía eléctrica en Colombia. El usuario permitió conservar EPM aunque no alcanza las 10.000 filas. La exigencia del profesor de evaluar las ocho dimensiones se mantiene para ambas fuentes. Esta selección no demuestra que esa evaluación ya esté completa.

## EPM — Histórico de tarifas de energía eléctrica

- Portal: https://www.datos.gov.co/d/sfcd-b3ey
- CSV: `datos/epm_sfcd-b3ey.csv`. Diccionario: `diccionarios/epm.yaml`.
- Volumen comprobado: **3.623 filas y 12 columnas**.
- Cobertura descrita por el publicador: **diciembre de 2016 a diciembre de 2021**.

Se selecciona por continuidad metodológica: es el caso con el que se desarrollaron perfilamiento, reglas, cartas y experimentos del Hito 2. Permite conservar una referencia para comprobar las correcciones del framework. Sus categorías tarifarias, nivel de tensión, propiedad y franjas horarias permiten formular controles de negocio concretos.

La revisión local del Hito 2 reporta 83 series con al menos 49 meses y 77 clasificadas como limpias por el código de esa entrega. Varias series por propiedad están fuertemente relacionadas; no son réplicas independientes. Esas cifras son evidencia previa, no una nueva ejecución sobre el CSV ahora conservado.

Se acepta la excepción de tamaño para este caso: longitud temporal y validación rigurosa sustentan su utilidad. No tiene consumo observado; el rango de consumo es una categoría. Los importes pueden representar diferentes conceptos y sus unidades deben confirmarse por concepto.

## CHEC — Información de costo unitario de tarifas de energía

- Portal: https://www.datos.gov.co/d/c698-wqig
- CSV: `datos/chec_c698-wqig.csv`. Diccionario: `diccionarios/chec.yaml`.
- Volumen comprobado: **40.609 filas y 24 columnas**.
- Cobertura global: **enero de 2008 a septiembre de 2026**, 225 meses.

Se selecciona para evaluar transferencia a otro publicador y estructura manteniendo el dominio tarifario. Supera el volumen solicitado y aporta comercializador, mercado, nivel, propiedad, clase de servicio, estrato, rango y componentes del costo unitario.

La validación local encontró, para cada variable costo unitario y valor de tarifa, **180 grupos con al menos 61 meses consecutivos con un registro único por mes y valores positivos y finitos**. Se agruparon las 12 columnas categóricas y se exigió variación en los valores del grupo. La mayor racha bajo estas condiciones fue de 201 meses. Estas dos variables no constituyen réplicas independientes de una misma categoría.

Con 61 observaciones se pueden reservar 48 cambios de referencia y 12 de vigilancia. Esa longitud habilita diseñar el experimento; todavía hay que verificar supuestos y ejecutar el protocolo. Existen 1.398 claves categoría-mes repetidas que requieren revisión, no eliminación automática. El resumen está en `verificaciones/chec_validacion_series.json`.

CHEC tampoco contiene consumo observado. Las medidas están declaradas como texto en el esquema; definiciones como `tipomed`, `cureal` y `subcon` requieren confirmación. El diccionario no inventa catálogos ni unidades faltantes.

## SSPD — Información comercial residencial y no residencial

- Portal: https://www.datos.gov.co/d/ebby-cjha
- CSV: `datos/sspd_ebby-cjha_mensual.csv` y `datos/sspd_ebby-cjha_detalle.csv`.
  Diccionario: `diccionarios/sspd.yaml`.
- Volumen en origen: **11.905.557 filas y 29 columnas**.
- Cobertura: **julio de 2017 a mayo de 2022, 59 períodos mensuales consecutivos.**

Se incorpora por una razón explícita: este mismo documento y el README declaraban que EPM y
CHEC **no contienen consumo observado**. Esta fuente lo aporta, en `consumo_basico`,
`consumo_complementario` y `consumo_reside_mayor800`.

Se evaluaron todas las alternativas del catálogo nacional antes de elegirla. De 2.138 fichas
revisadas, 128 de energía y 24 con alguna columna de consumo, **es la única con profundidad
mensual suficiente para cartas de control**: las demás tienen once o doce períodos. Con 59
meses caben 36 cambios de referencia y 23 de vigilancia, y 136 de sus 207 series
empresa-estrato alcanzan el mínimo de 49.

**Se relaja un criterio y se declara.** La fuente no se actualiza desde el 28 de octubre de
2023 y declara periodicidad anual. Se aceptó porque las cartas requieren una serie mensual
histórica, no un flujo vivo: que no lleguen períodos nuevos no afecta un análisis sobre 59
meses ya publicados. Además, una fuente que declara una frecuencia y no la cumple es materia
de la dimensión de oportunidad, no una razón para descartarla.

**Dos limitaciones que no se ocultan.** La primera: es de **Zonas No Interconectadas**. Se
verificaron las 91 empresas contra el directorio de Superservicios y ninguna es del Sistema
Interconectado Nacional, de modo que no aplica la fórmula de la Resolución CREG 119 de 2007
ni comparte los ejes tarifarios de EPM y CHEC. Por eso R08, R09 e INT02 quedan `no_aplica`.
La segunda: en origen pesa unos 9,7 GB, así que se conservan dos censos declarados en lugar
del conjunto íntegro, con su universo escrito en el diccionario.

A cambio aporta algo que las otras dos no tienen: **91 publicadores en un mismo esquema**.
Validar el framework en dos empresas grandes y después en 91 operadores pequeños con poca
capacidad de reporte es un argumento de transferibilidad bastante más fuerte.

## SSPD-NR — Información comercial no residencial

- Portal: https://www.datos.gov.co/d/bnkp-xdb7
- CSV: `datos/sspd_bnkp-xdb7.csv`. Diccionario: `diccionarios/sspd_nr.yaml`.
- Volumen: **402.500 filas y 48 columnas**, conservadas íntegras.
- Cobertura: **julio de 2021 a junio de 2022, 12 períodos mensuales.**

Entra para resolver la limitación declarada de la fuente anterior. SSPD aporta los 59 meses
que las cartas necesitan pero es de Zonas No Interconectadas; esta es del **Sistema
Interconectado Nacional** —32 prestadores en Meta, Casanare, Huila, Putumayo, Guaviare y
Caquetá, encabezados por Electrificadora del Meta y Electrificadora del Huila—, de modo que
le aplica el mismo régimen regulatorio que a EPM y CHEC.

Aporta además tres cosas que ninguna otra fuente del proyecto tiene:

1. **`tarifa_aplicada`**, con promedio de 758,98 $/kWh. Es el costo unitario que EPM y CHEC
   publican como especificación, aquí aplicado a una factura concreta. Es el puente entre el
   dominio tarifario y el consumo observado.
2. **`car_t440_car_inver` con valores 100, 50 y 0**: el eje de propiedad del activo. Por eso
   **R08 y R09 vuelven a ser aplicables**, cuando en la fuente ZNI quedaron `no_aplica`.
3. **Energía reactiva** y **pares código-nombre** (empresa y mercado), que devuelven a INT02
   un caso donde medirse.

**Su limitación es el espejo de la anterior.** Solo tiene 12 períodos, por debajo de los 49
que exige el protocolo, así que CART01 no es ejecutable sobre ella. Y el volumen se desploma
dentro de la propia ventana: 101.608 registros en 2021-07 frente a 977 en 2022-05, de modo
que los períodos útiles son unos nueve. Eso es un defecto de completitud de la fuente y está
declarado como tal, no disimulado.

**Sobre la oportunidad, una precisión que conviene no perder.** La fuente trae
`car_t440_fec_exp`, fecha de expedición de la factura. Permite medir el rezago entre el
período facturado y la emisión, pero eso es **oportunidad del servicio, no del dato**. OPO01
está especificado sobre la disponibilidad de la publicación, así que esta evidencia no lo
cierra tal como está escrito: habría que reespecificar el control o registrarlo como un
indicador distinto. No se fuerza.

## Por qué cuatro fuentes y no tres

Las dos fuentes de consumo cubren huecos opuestos y ninguna sola basta:

| | SSPD (ZNI) | SSPD-NR (interconectado) |
|---|---|---|
| Períodos mensuales | **59** | 12 |
| Régimen | Zonas No Interconectadas | **Sistema Interconectado** |
| Tarifa aplicada | no | **sí** |
| Eje de propiedad | no | **sí** |
| Pares código-nombre | no | **sí** |
| Energía reactiva | no | **sí** |

Con la primera se pueden construir las series que exigen las cartas; con la segunda se
sostiene que el framework se aplicó al mismo régimen regulatorio de EPM y CHEC. El costo es
real y conviene decirlo: cada fuente añadida arrastra la obligación de evaluarle las ocho
dimensiones, y esa obligación todavía no está cerrada en ninguna.

## Utilidad de la pareja

Mantiene el dominio del trabajo realizado y permite contrastar dos estructuras tarifarias. Se propone un núcleo común y adaptadores por fuente. R08 y R09 deben traducirse al esquema de CHEC: copiar literalmente el código EPM no sería una réplica válida.

Permite desarrollar perfilamiento, reglas, cartas, comparación de detectores, scorecards y un artefacto reproducible. La solidez de la tesis dependerá de verdad de referencia, métricas, sensibilidad, intervalos e independencia de las unidades de evaluación; la selección por sí sola no garantiza esos resultados.

## Condición obligatoria: ocho dimensiones por dataset

| Dimensión | Control/evidencia prevista | Pendiente |
|---|---|---|
| Completitud | Campos obligatorios y cobertura esperada | Aplicabilidad y denominadores; cero no equivale a faltante |
| Validez | Tipos, formatos, períodos, dominios y signos | Confirmar unidades y excepciones por concepto |
| Unicidad | Duplicados exactos y claves repetidas | Cerrar claves y distinguir conflictos |
| Consistencia | Etiquetas y relaciones por propiedad, nivel y concepto | Adaptar R08/R09 a CHEC |
| Integridad | Estructura y correspondencia con catálogos/código-nombre | Especificar e implementar INT01; distinguirlo de unicidad |
| Razonabilidad | R12, cartas y modelos | Protocolo temporal, cuarentena y dependencia entre series |
| Exactitud | Muestra contrastada con documentos tarifarios originales | Obtener referencias, definir muestreo y medir concordancia |
| Oportunidad | Disponibilidad real frente a plazo esperado | Conseguir evidencia histórica o diseñar seguimiento prospectivo con alcance explícito |

**“No evaluable” no cumple el requisito final del profesor.** La selección queda condicionada a obtener evidencia para exactitud y oportunidad en cada fuente. Si falta, será necesario complementar las fuentes o revisar la selección con el director.

Vigencia, fecha de descarga y modificación global del portal no equivalen a disponibilidad real por período. Un seguimiento futuro no demuestra oportunidad histórica.

Las doce reglas base no cubren por sí solas las ocho dimensiones. Se proponen controles complementarios INT01, EXA01 y OPO01 en el YAML, sin presentarlos como implementados. También se propone distinguir R11/validez y R12/razonabilidad de exactitud; el código existente conserva sus etiquetas y no fue modificado.

## Trazabilidad y alcance documental

Metadatos originales en `metadatos/`; CSV sin modificación en `datos/`; hashes y tamaños en `verificaciones/manifiesto_archivos.json`. La fecha del manifiesto no se presenta como fecha de descarga original ni de publicación.

Fundamento: anteproyecto y retroalimentación de junio de 2026 en `documentos/`, revisión técnica del Hito 2 en `docs/` y exigencia adicional del profesor comunicada por el usuario. La revisión técnica es un borrador local, no un concepto oficial del profesor. No se modificó el anteproyecto; queda pendiente actualizar publicadores, población/muestra y alcance de ocho dimensiones.
