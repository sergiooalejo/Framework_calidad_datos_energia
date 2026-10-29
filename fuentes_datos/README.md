# Fuentes seleccionadas: EPM, CHEC, SSPD y SSPD-NR

Esta carpeta conserva las dos fuentes tarifarias eléctricas acordadas y dos de facturación,
incorporadas para cubrir el consumo observado que a las dos primeras les falta.

| Fuente | Qué aporta | CSV | Diccionario | Portal |
|---|---|---|---|---|
| **EPM** · 3.623 filas, 12 col. | Tarifa, forma larga | [csv](datos/epm_sfcd-b3ey.csv) | [epm.yaml](diccionarios/epm.yaml) | https://www.datos.gov.co/d/sfcd-b3ey |
| **CHEC** · 40.609 filas, 24 col. | Tarifa, forma ancha | [csv](datos/chec_c698-wqig.csv) | [chec.yaml](diccionarios/chec.yaml) | https://www.datos.gov.co/d/c698-wqig |
| **SSPD** · 11.905.557 filas en origen, 29 col. | Consumo y **59 meses** para las cartas | [mensual](datos/sspd_ebby-cjha_mensual.csv) · [detalle](datos/sspd_ebby-cjha_detalle.csv) | [sspd.yaml](diccionarios/sspd.yaml) | https://www.datos.gov.co/d/ebby-cjha |
| **SSPD-NR** · 402.500 filas, 48 col. | Consumo, **tarifa aplicada**, propiedad y régimen interconectado | [csv](datos/sspd_bnkp-xdb7.csv) | [sspd_nr.yaml](diccionarios/sspd_nr.yaml) | https://www.datos.gov.co/d/bnkp-xdb7 |

**Las dos fuentes de consumo se complementan y no se reemplazan.** SSPD aporta la
profundidad temporal —59 períodos consecutivos, los únicos que alcanzan el mínimo de 49 que
exigen las cartas— pero es de Zonas No Interconectadas. SSPD-NR es del Sistema
Interconectado y trae la tarifa aplicada y el eje de propiedad del activo, pero solo tiene
12 períodos. Ninguna de las dos sola cubre lo que cubren juntas.

**La tercera fuente no se conserva íntegra.** Pesa unos 9,7 GB en origen, que no es
versionable. En su lugar se conservan **dos censos declarados, no muestras**: uno mensual
agregado que cubre las 91 empresas y los 59 períodos (15.075 filas), y uno de detalle con
todos los registros de la empresa 28111 (91.840 filas). El alcance de cada uno está escrito
en `diccionarios/sspd.yaml` y se repite en cada resultado que lo use.

## Cómo consultar la información

- **Datos:** abrir los CSV con Excel usando UTF-8 y delimitador coma, o leerlos con Python. Conservan las columnas originales. Los importes CHEC necesitan conversión y validación explícitas.
- **Justificación:** [JUSTIFICACION_SELECCION.md](JUSTIFICACION_SELECCION.md) explica la selección, las limitaciones y la cobertura prevista por dimensión.
- **Variables:** los YAML explican todas las columnas, tipo oficial, significado, unidad o incertidumbre, rol, reglas relacionadas y uso para series.
- **Dimensiones y reglas:** [dimensiones_reglas.yaml](diccionarios/dimensiones_reglas.yaml) distingue las doce reglas base de los controles complementarios. Es una especificación documental, no un motor ejecutado.
- **Matriz OE1 del Hito 3:** [fichas completas](../docs/hito3/matriz_oe1.md), [CSV para Excel](../docs/hito3/matriz_oe1.csv) y [YAML](../docs/hito3/matriz_oe1.yaml). Incluye 19 indicadores y su aplicación en ambas fuentes.
- **Metadatos:** `metadatos/` contiene los esquemas y descripciones del portal.
- **Verificaciones:** `verificaciones/` conserva cobertura y validación de CHEC, además de hashes de ambos archivos.
- **Catálogo:** `catalogos/busqueda_tarifas_energia.json` contiene solo EPM y CHEC; es un catálogo curado, no la búsqueda íntegra original.

## Estado

EPM se conserva con la excepción de tamaño aceptada por el usuario. EPM y CHEC contienen
tarifas y costos, no consumo observado; esa carencia es la que cubre la tercera fuente.

**SSPD es de Zonas No Interconectadas.** Sus 91 empresas se verificaron una por una contra
el directorio de Superservicios y ninguna pertenece al Sistema Interconectado Nacional, de
modo que no comparte el régimen tarifario de EPM y CHEC. Se incorpora por el consumo
observado y por la profundidad mensual, no como par tarifario; la matriz OE1 marca
`no_aplica` los controles cuyo concepto no existe en su esquema.

**Es obligatorio evaluar las ocho dimensiones por fuente.** Todavía falta evidencia externa para exactitud y oportunidad. No se afirma cobertura completa ni se considera “no evaluable” cumplimiento final. Los YAML identifican esas brechas y las definiciones pendientes.

Se eliminaron los datasets descartados, muestras y documentos de recomendaciones anteriores de esta carpeta. El código y los documentos del proyecto fuera de `fuentes_datos/` no fueron modificados.
