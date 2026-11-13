# Anexo de validación externa · Hito 6

## Objetivo

Contrastar alertas del framework con una publicación oficial o respuesta del publicador. Este
anexo separa evidencia observada, interpretación técnica y confirmación externa.

## Casos prioritarios heredados

| Caso | Fuente | Evidencia interna | Confirmación externa | Estado |
|---|---|---|---|---|
| Valor 43.577 | EPM | CSV local y visualización compartida en Excel | Fuente independiente o confirmación del publicador pendiente | No concluyente |
| Serial 43.501 | EPM | Pendiente de contraste | Pendiente de EPM/CREG | Hipótesis |
| Valor 205.151 | EPM | Pendiente de contraste | Pendiente de EPM/CREG | Hipótesis |
| Mezcla de enero y abril | EPM | Pendiente de contraste | Pendiente de EPM/CREG | Hipótesis |
| Cambio de febrero de 2020 | EPM | Señal en cartas | Pendiente de EPM/CREG | Hipótesis |

El caso `43577` cuenta con evidencia interna: el CSV conserva el valor en ambos campos y la
captura compartida lo muestra en Excel con formato monetario. Eso no confirma ni descarta una
conversión previa desde una fecha. El detalle se conserva en
`Data/gold/outputs/hito6/evidencia_caso_43577.md`; falta contraste independiente.

## Registro para cada alerta

| Campo | Descripción |
|---|---|
| id_alerta | Identificador de la salida del framework |
| fuente | EPM, CHEC, SSPD o XM |
| serie y período | Clave exacta de la observación |
| método y regla | Técnica que generó la señal |
| evidencia publicada | URL, archivo o captura con fecha de consulta |
| clasificación | Confirmada, descartada, no concluyente o pendiente |
| observaciones | Explicación de la comparación |
| revisor y fecha | Persona y fecha de la revisión |

## Muestra de 50 alertas

La muestra inicial está en `Data/gold/outputs/hito6/muestra_alertas_50.csv`. Fue seleccionada con semilla
`42` y contiene 15 alertas de EPM, 15 de CHEC y 20 de SSPD. XM no tiene alertas reales elegibles
en este corte; por tanto queda documentado como no aplicable para la muestra, sin inventar casos.
La tabla conserva los identificadores y deja `clasificacion=pendiente`. Sus 50 filas corresponden
a 47 combinaciones distintas de fuente, serie y período: tres aparecen en diferentes escenarios.
La columna LOF de esta muestra histórica está vacía porque el archivo de entrada no incluye ese
método; no debe interpretarse como ausencia de alertas LOF. El plan del profesor pide 50 alertas
de EPM: el cambio a tres fuentes y el tratamiento de los escenarios repetidos requieren aprobación.
No se debe reemplazar una alerta difícil por una más conveniente.

El generador ahora crea una copia nueva con fecha si la muestra anterior existe; nunca la
sobrescribe. La copia nueva incluye las columnas de serie y categoría y no incluye LOF, que no
está disponible en esa entrada. Esto no equivale a aprobar una nueva muestra.

## Limitación

Si EPM o CREG no responden, el resultado se presenta como validación interna y limitación del
estudio; no se atribuye una causa regulatoria ni se declara exactitud económica.

