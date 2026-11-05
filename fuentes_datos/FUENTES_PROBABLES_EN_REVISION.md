# Fuentes probables o en revisión

La selección principal queda fijada en cuatro fuentes eléctricas: EPM, CHEC, Superservicios ZNI (`ebby-cjha`) y XM/SIMEM (`c1b851`). Las siguientes fuentes se conservan porque pueden aportar contexto, variables o una futura ampliación, pero no se cuentan como casos principales del protocolo.

| Fuente | Estado | Motivo de no incorporación principal |
|---|---|---|
| Superservicios no residencial `bnkp-xdb7` | En revisión | Tiene 402.500 filas y consumo/tarifa aplicada, pero solo 12 meses y una caída fuerte de registros; no permite cartas mensuales con el protocolo de 49 observaciones. |
| CSV extraído `supers_icnr-l4iw` | En revisión, sin ficha vigente | Es una extracción relacionada con información comercial; tiene 12 meses y sus identificadores aparecen en notación científica. Se conserva como evidencia, pero no se cuenta como fuente independiente de `bnkp-xdb7`. |
| CREG, Circular 125 de 2025 | Referencia regulatoria | Es eléctrica y contiene EPM, CHEC, ESSA y EDEQ, pero solo tiene 88 registros anuales y 11 columnas. No alcanza el volumen ni la continuidad mensual. |
| CREG, Circulares 053/064 de 2015 | Referencia regulatoria | Son tablas de indicadores y escenarios de calidad, no microdatos mensuales crudos. No deben tratarse como observaciones para cartas. |
| CREG `ek3f-5wn4` | Descartada por alcance | Es una fuente amplia de gas natural. El proyecto quedó limitado a electricidad, por lo que no se incorpora. |
| Antigua fuente SSPD `vfjy-6fka` | Sustituida | Era la fuente indicada en una versión anterior del plan, pero fue reemplazada por `ebby-cjha`, que tiene mayor cobertura y consumo. |

Los archivos de estas fuentes se conservan en `fuentes_datos/datos/Datos_en_revision/` y los motivos detallados están en [`REVISION_CREG_ELECTRICIDAD.md`](REVISION_CREG_ELECTRICIDAD.md) y [`PROPUESTA_CUATRO_FUENTES.md`](PROPUESTA_CUATRO_FUENTES.md).

No se consideran fuentes diferentes las copias agregadas, los archivos comprimidos o las vistas derivadas del mismo identificador de portal. Tampoco se cuentan los anexos CREG como cuatro datasets independientes.
