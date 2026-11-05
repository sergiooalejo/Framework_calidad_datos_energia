# Ficha de caracterización: chec_c698-wqig

## Identificación

| Atributo | Descripción |
|---|---|
| Archivo | `chec_c698-wqig.csv` |
| Ubicación | `fuentes_datos/datos/Datos_seleccionados/` |
| Tema | Costos unitarios y tarifas de energía eléctrica reportados para mercados atendidos por CHEC |
| Formato | CSV delimitado por comas, encabezados en la primera fila y campos entre comillas |
| Tamaño | 9.626.732 bytes (aprox. 9,18 MiB) |
| Registros | 40.609 |
| Variables | 24 |
| Cobertura temporal | Enero de 2008 a septiembre de 2026; 225 meses calendario presentes |
| Ámbito geográfico/comercial | Mercados CHEC (código 1234, 37.683 registros) y Pereira (código 1218, 2.926 registros) |
| Unidad de observación | Una combinación reportada de periodo, mercado, tipología de medición, nivel de tensión, modalidad de cobro, clase de servicio y rango de consumo |
| Granularidad temporal | Mensual |

## Contenido y variables

Los nombres se conservan tal como aparecen en el CSV. Las magnitudes monetarias parecen corresponder a valores unitarios de tarifa; el archivo no incluye una unidad explícita, por lo que debe confirmarse en el metadato de origen antes de compararlas o convertirlas.

| Variable(s) | Interpretación según el nombre |
|---|---|
| `costounitariotarifa_ano`, `costounitariotarifa_mes` | Año y mes del reporte. |
| `comercializador_codigo`, `comercializador_nombre` | Identificador y nombre del comercializador (CHCC / CENTRAL HIDROELECTRICA DE CALDAS S.A. E.S.P.). |
| `mercado_codigo`, `mercado_nombre` | Código y nombre del mercado (CHEC o PEREIRA). |
| `costounitariotarifa_tipomed` | Tipo de medición: aparecen `S`, `HP` y `HM`; no se proporciona catálogo explicativo. |
| `nivel_tension_codigo` | Nivel de tensión codificado (1 a 4). |
| `modalidadcobro_propiedad` | Modalidad de cobro/propiedad del OR (por ejemplo, `0% OR`, `50% OR`, `100% OR`, `0% OR SIN AOM`). |
| `claseservicio_codigo`, `claseservicio_descri` | Código y descripción de la clase de servicio (29 descripciones observadas). Incluye clases residenciales, comerciales, industriales, oficiales y especiales. |
| `claseservicio_estrato` | Estrato residencial cuando aplica; `NA` en registros donde no se especifica o no corresponde. |
| `costounitariotarifa_rangoconsumo` | Rango de consumo codificado (se observan 1 y 2); requiere catálogo para interpretar sus umbrales. |
| `costounitariotarifa_tipomercado` | Tipo de mercado codificado; solo se observa `R`. |
| `costounitariotarifa_generacion`, `costounitariotarifa_transmision`, `costounitariotarifa_distribucion`, `costounitariotarifa_comercializacion`, `costounitariotarifa_perdidas`, `costounitariotarifa_restricciones` | Componentes de costo/tarifa asociados a generación, transmisión, distribución, comercialización, pérdidas y restricciones. |
| `costounitariotarifa_cu`, `costounitariotarifa_cureal` | Campos `CU` y `CU real`; la definición operativa debe confirmarse en el diccionario de origen. |
| `costounitariotarifa_subcon` | Componente o indicador de subsidio/contribución (interpretación tentativa por el nombre; confirmar en metadatos). |
| `costounitariotarifa_valor_tarifa` | Valor de tarifa reportado. |

## Perfil de calidad y consistencia

- No se encontraron filas duplicadas al comparar las 24 columnas completas.
- No hay celdas vacías en 19 de las 24 columnas. Las cinco columnas con vacíos tienen 11 cada una: `distribucion`, `comercializacion`, `perdidas`, `restricciones` y `subcon` (55 vacíos en total, 0,0056 % de las 975.816 celdas).
- `claseservicio_estrato` contiene 25.266 valores literales `NA` (62,2 %). Deben tratarse como no aplicables/no informados según la clase; no convertirlos automáticamente en cero.
- Los años y meses cubren todos los meses de enero de 2008 a septiembre de 2026 (225/225), pero esto no garantiza que cada combinación de mercado y categoría exista todos los meses.
- Rango de valores observado para los campos numéricos de componentes y tarifas: generación 0–416,1932; transmisión 18,4788–66,8118; distribución 15,6263–335,3986; comercialización 23,1498–197,6767; pérdidas 2,1007–77,6352; restricciones −20,3656–163,8239; `CU` 199,3432–1.114,0034; `CU real` 0–934,8447; `subcon` −0,6000001–0,2; `valor_tarifa` 102,1672–1.336,8041. Los extremos negativos o cero ameritan validar reglas del dato, no son por sí solos prueba de error.
- Los códigos `tipomed`, `nivel_tension`, `claseservicio`, `rangoconsumo` y `tipomercado` requieren sus catálogos para análisis semántico confiable.
- El nombre del archivo sugiere una descarga de datos abiertos, pero el CSV no contiene URL, fecha de extracción, licencia, versión ni diccionario de datos. Registrar esos metadatos al incorporar el dataset al flujo de análisis.

## Recomendaciones de uso

1. Parsear año, mes, códigos y magnitudes como tipos numéricos; conservar códigos con su catálogo y evitar perder ceros iniciales si existieran en futuras versiones.
2. Normalizar `NA` como valor faltante/no aplicable y diferenciarlo de las celdas vacías.
3. Consultar el diccionario de la fuente para confirmar unidades, significado de códigos y fórmulas de `CU`, `CU real`, `subcon` y `valor_tarifa`.
4. Al comparar series, controlar por mercado, clase de servicio, nivel de tensión, modalidad y rango de consumo; no promediar sin definir ponderaciones.
5. Para un corte reproducible, consignar que este archivo llega hasta septiembre de 2026.

## Alcance de esta ficha

Caracterización calculada directamente sobre el archivo local. Las definiciones que no están explícitas en los nombres se señalan como tentativas o pendientes de contraste con los metadatos oficiales de publicación.

## Evidencia incorporada en el Hito 3

- `EXA01` contrasta 756 celdas con Superservicios y obtiene 100 % de coincidencia en la
  muestra disponible.
- `DEF01` dispone del catálogo operativo de las 24 columnas en
  `fuentes_datos/catalogos/CHEC/chec_definiciones_def01.yaml`.
- `MAP01` registra 3/3 equivalencias código-nombre aprobadas metodológicamente por el
  proyecto, sin presentarlas como catálogo oficial CHEC.
- `cartas_log_chec.csv` contiene 276 series y 37 señales preliminares que deben revisarse
  frente a las publicaciones tarifarias.
- `OPO01` usa cobertura temporal 225/225 como proxy, no como puntualidad histórica.
