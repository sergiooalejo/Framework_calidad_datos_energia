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

## Muestra vigente de 50 alertas EPM

La muestra para revisar el protocolo vigente está en
`Data/gold/outputs/hito6/muestra_alertas_h4_v2_epm_50.csv`, con su manifiesto
adyacente `.manifiesto.json`. Se obtiene de los puntajes reales de **H4-v2-CV-temporal**:
EPM, referencia 36, horizonte `t`, tasa objetivo de calibración 5 % y semilla 42.
Son 50 observaciones únicas por fuente/serie/período, seleccionadas entre las que
activan al menos una bandera de IMR, Z robusto, IF, LOF, KNN o R12. Se conserva
el resultado de los seis métodos; no se fuerza que todos produzcan alertas.
R12 utiliza el umbral CV vigente, no necesariamente el factor nativo 10.

Cada fila incluye identidad estable, categoría, medida, período, banco, puntajes,
umbrales y banderas. Los campos de revisión se inicializan pendientes. El manifiesto
vincula la selección con las entradas y la ejecución H4 verificadas por hash.
La misma semilla y los mismos datos producen las mismas observaciones, aunque
se reordene la entrada. Si faltan casos no se repiten ni se sustituyen fuentes.

Este diseño sigue la solicitud original de 50 alertas EPM. La evidencia externa,
la interpretación y la aprobación del método de evaluación permanecen pendientes.
No se debe reemplazar una alerta difícil por una más conveniente. La muestra
no representa todas las fuentes ni acredita por sí sola precisión empírica o recall.
La precisión por método requiere su subconjunto revisado y un denominador explícito;
el recall necesita también observaciones no alertadas con referencia externa.

## Muestra histórica conservada

`Data/gold/outputs/hito6/muestra_alertas_50.csv` corresponde al protocolo histórico
de sensibilidad: 15 EPM, 15 CHEC y 20 SSPD, con 47 combinaciones únicas y tres
observaciones repetidas entre escenarios. Su columna LOF vacía no era una medición.
Se conserva para trazabilidad y no valida el H4 vigente. No se sobrescriben ni se
transfieren sus revisiones a la muestra nueva. Los casos prioritarios heredados
siguen como evidencia complementaria, separada del sorteo vigente.

El generador crea otra pareja CSV/manifiesto con fecha si la salida vigente existe.

## Limitación

Si EPM o CREG no responden, el resultado se presenta como validación interna y limitación del
estudio; no se atribuye una causa regulatoria ni se declara exactitud económica.

