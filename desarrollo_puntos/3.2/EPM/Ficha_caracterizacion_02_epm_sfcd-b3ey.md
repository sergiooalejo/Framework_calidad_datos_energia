# Ficha de caracterización: epm_sfcd-b3ey

## Identificación

| Atributo | Descripción |
|---|---|
| Archivo | `epm_sfcd-b3ey.csv` |
| Ubicación del archivo fuente | `fuentes_datos/datos/Datos_seleccionados/` |
| Tema | Información de costos unitarios y tarifas de energía eléctrica de EPM |
| Formato | CSV, delimitado por comas, encabezados en la primera fila y valores entre comillas |
| Tamaño | 426.826 bytes (aprox. 417 KiB) |
| Registros | 3.623 filas de datos |
| Variables | 12 |
| Cobertura temporal observada | Diciembre de 2016 a diciembre de 2021; 61 combinaciones año-mes presentes |
| Granularidad temporal | Mensual, con desgloses según tipo de información, tarifa, dato, consumo, nivel y propiedad |
| Unidad de observación | Una combinación de las categorías tarifarias y periodo, con valores reportados para EPM, compartido, cliente, punta y fuera de punta |
| Unidad de medida | No indicada en el archivo. Confirmar en el diccionario o la fuente antes de interpretar o comparar valores. |

## Contenido y variables

| Variable(s) | Interpretación según el nombre y valores observados |
|---|---|
| `tipodeinformacion` | Modalidad de información: `Monomia` o `Horaria`. |
| `tipodetarifa` | Categoría de tarifa. Se observan `Costo Unitario`, `Tarifa`, `Residencial`, `No Residencial`, `Áreas Comunes` y una variante de capitalización (`No residencial`). |
| `tipodedato` | Componente, categoría de usuario o dato tarifario. Hay 28 valores distintos, entre ellos cargos de transporte, restricciones, costos de compra y estratos. |
| `rangodeconsumo` | Segmento de consumo: aparecen `N/A`, `Fuera de Punta`, `Punta`, `Rango 0 - CS`, `Rango > CS`, `Todo el consumo`, `0-CS` y `Mayor CS`. Confirmar equivalencias con el catálogo de origen. |
| `nivel` | Nivel de tensión, representado por números romanos I, II, III y IV. |
| `propiedadepm` | Valor asociado a propiedad de EPM. Su semántica y unidad exactas no se definen en el archivo. |
| `compartido` | Valor asociado al componente compartido. Su semántica y unidad exactas no se definen en el archivo. |
| `propiedaddelcliente` | Valor asociado a propiedad del cliente. Su semántica y unidad exactas no se definen en el archivo. |
| `punta`, `fueradepunta` | Valores para los periodos punta y fuera de punta; contienen muchos ceros según las categorías. |
| `year`, `mes` | Año y nombre del mes en español. Hay 2016–2021; 2016 solo tiene diciembre y 2017–2021 incluyen los doce meses. |

## Perfil de calidad y consistencia

- Se leyeron 3.623 filas y 12 columnas; el archivo se decodifica correctamente como UTF-8 con BOM.
- Hay una fila parcialmente incompleta (fila 657 del archivo): conserva las seis categorías iniciales, pero deja vacíos los cinco valores (`propiedadepm`, `compartido`, `propiedaddelcliente`, `punta`, `fueradepunta`) y el periodo (`year`, `mes`). En total son 7 celdas vacías.
- Se identificaron 10 filas duplicadas exactas al comparar las 12 columnas. Conviene confirmar si son duplicados de extracción o si la fuente admite repeticiones antes de eliminarlas.
- Hay diferencias de escritura que pueden fragmentar categorías: `No Residencial` / `No residencial`; `Rango 0 - CS` / `0-CS`; `Rango > CS` / `Mayor CS`; `Costo compra: Gm, i` / `Costo compra: Gm,i`.
- Los campos de valor contienen valores extremos que requieren validar contra la publicación de origen. Por ejemplo, fila 2048: `compartido=205151.00` frente a `propiedadepm=213.50` y `propiedaddelcliente=197.37`; filas 3132 y 3134 contienen `punta=43577.00` y `punta=43501.00`, respectivamente. No se corrigieron ni eliminaron.
- También se observan valores negativos (mínimo −1,61 en campos de valor). Revisar si son ajustes válidos o errores de captura.
- El archivo no incorpora URL o fecha de descarga, licencia, versión, unidad de medida ni catálogo formal de códigos.

## Recomendaciones de uso

1. Conservar los valores originales y crear una copia de trabajo para normalizar mayúsculas, espacios y variantes de etiquetas después de contrastarlas con la fuente.
2. Tratar la fila sin periodo como registro incompleto; no imputar sus valores sin una regla documentada.
3. Revisar los duplicados y valores extremos con el recurso oficial antes de decidir su exclusión, corrección o conservación.
4. Convertir `year` y los valores monetarios a tipos numéricos, y mapear los nombres de meses a una fecha mensual estandarizada.
5. Obtener metadatos para interpretar `propiedadepm`, `compartido`, `propiedaddelcliente`, la unidad de medida y los códigos de rangos/niveles.
6. En comparaciones, segmentar por tipo de información, tarifa, dato, rango de consumo, nivel y periodo; no combinar categorías heterogéneas sin definir una regla.

## Alcance de esta ficha

Caracterización calculada directamente sobre el archivo local. Las interpretaciones de las columnas se basan en sus nombres y valores observados; las definiciones y unidades que no constan en el CSV quedan pendientes de verificación con los metadatos oficiales.

## Evidencia incorporada en el Hito 3

- La comparación reproducible de `fuentes_datos/verificaciones/EPM/epm_exactitud_referencias.json`
  coincide en 18 de 18 celdas con seis filas de publicaciones oficiales de EPM (2020 y
  2021). Es una muestra de exactitud, no una certificación de todo el histórico.
- `desarrollo_puntos/3.3/cartas_log_epm.csv` contiene 60 series con referencia de 36
  cambios y vigilancia de 12 cambios en escala logarítmica. El resultado actual es
  preliminar y debe someterse a sensibilidad antes de usarlo como alerta operativa.
- La matriz OE1 deja `INT02` como no aplicable (no hay pares código-nombre). `OPO01` se
  evalúa con un proxy de cobertura temporal (períodos presentes frente a esperados), no
  como puntualidad histórica, porque el archivo no conserva fechas de publicación.
  `MAP01` queda como `provisional_interno`: sus equivalencias fueron aprobadas por el
  equipo del proyecto para normalización analítica, sin presentarlas como confirmación
  oficial de EPM. `DEF01` cuenta ahora con el catálogo operativo de las 12 columnas en
  `fuentes_datos/catalogos/EPM/epm_definiciones_def01.yaml`; sus unidades monetarias son
  condicionales al `tipodedato`. `CART01` permanece provisional hasta completar su
  calibración metodológica.
