# Fuentes seleccionadas: EPM y CHEC

Esta carpeta conserva exclusivamente las dos fuentes tarifarias eléctricas acordadas.

| Fuente | CSV completo | Diccionario YAML | Portal |
|---|---|---|---|
| EPM: 3.623 filas, 12 columnas | [epm_sfcd-b3ey.csv](datos/epm_sfcd-b3ey.csv) | [epm.yaml](diccionarios/epm.yaml) | https://www.datos.gov.co/d/sfcd-b3ey |
| CHEC: 40.609 filas, 24 columnas | [chec_c698-wqig.csv](datos/chec_c698-wqig.csv) | [chec.yaml](diccionarios/chec.yaml) | https://www.datos.gov.co/d/c698-wqig |

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

EPM se conserva con la excepción de tamaño aceptada por el usuario. Ambos contienen tarifas/costos, no consumo observado.

**Es obligatorio evaluar las ocho dimensiones por fuente.** Todavía falta evidencia externa para exactitud y oportunidad. No se afirma cobertura completa ni se considera “no evaluable” cumplimiento final. Los YAML identifican esas brechas y las definiciones pendientes.

Se eliminaron los datasets descartados, muestras y documentos de recomendaciones anteriores de esta carpeta. El código y los documentos del proyecto fuera de `fuentes_datos/` no fueron modificados.
