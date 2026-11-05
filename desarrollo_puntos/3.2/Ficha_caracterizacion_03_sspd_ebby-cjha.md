# Ficha de caracterización: sspd_ebby-cjha

## Identificación

| Atributo | Descripción |
|---|---|
| Dataset | `ebby-cjha` |
| Portal | https://www.datos.gov.co/d/ebby-cjha |
| Archivo de detalle | `fuentes_datos/datos/Datos_en_revision/sspd_ebby-cjha_detalle-compressed.zip` |
| Archivo agregado | `fuentes_datos/datos/Datos_en_revision/sspd_ebby-cjha_mensual.csv` |
| Publicador | Superintendencia de Servicios Públicos Domiciliarios |
| Tema | Información comercial residencial y no residencial de energía eléctrica |
| Filas de origen | 11.905.557 |
| Columnas de origen | 29 |
| Cobertura | Julio de 2017 a mayo de 2022, 59 períodos mensuales |
| Ámbito | Zonas No Interconectadas (ZNI) |
| Unidad de observación | Factura/usuario y período mensual |

## Columnas del detalle

| Grupo | Columnas e interpretación |
|---|---|
| Identificación | `identificador_empresa` (prestador), `niu` (usuario), `id_factura` (factura), `codigo_localidad` (localidad), `codigo_conexion` (conexión). |
| Tiempo | `anio` (año), `periodo` (mes), `fecha_expedicion` (expedición de factura), `fecha_inicio_periodo` (inicio del período), `dias_facturados` (duración facturada). |
| Clasificación | `ubicacion` (urbana/rural u otro código), `tipo_conexion`, `estrato_sector`, `tipo_factura`, `tipo_lectura`, `tipo_categoria`. |
| Consumo | `consumo_basico`, `consumo_complementario`, `consumo_reside_mayor800`. Son consumos facturados por tramo; la unidad debe confirmarse documentalmente, aunque se espera kWh. |
| Facturación | `facturacion_consumo_basico`, `facturacion_complementario`, `facturacion_reside_mayor800`. |
| Otros valores | `valor_refacturacion`, `valor_mora`, `interes_mora`, `valor_subsidio`, `porcentaje_subsidio`, `valor_total`. |

## Archivo agregado mensual

El archivo agregado no es una segunda fuente. Es una transformación reproducible del mismo dataset. Sus columnas son `identificador_empresa`, `anio`, `periodo`, `estrato_sector`, `ubicacion`, `tipo_conexion`, `tipo_lectura`, `tipo_factura`, `n_registros`, `consumo_basico_sum`, `consumo_basico_min`, `consumo_basico_max`, `consumo_compl_sum`, `consumo_mayor800_sum`, `fact_basico_sum`, `valor_total_sum`, `valor_subsidio_sum` y `dias_facturados_sum`.

## Utilidad para el plan de hitos

- Aporta consumo observado, que no existe en EPM ni CHEC.
- Permite probar perfilamiento, reglas de calidad, agrupación mensual y razonabilidad.
- Tiene 59 meses globales; 117 grupos agregados presentan consumo básico positivo durante al menos 49 meses consecutivos.
- Permite probar transferencia del framework a 91 prestadores ZNI.
- Sirve para Hito 3 y para preparar Hito 4, pero las cartas deben ejecutarse sobre series homogéneas, no sobre el total de filas.

## Limitaciones y adaptación de reglas

- Es ZNI; no debe compararse directamente con las reglas tarifarias de EPM/CHEC.
- R08 y R09 no aplican literalmente porque no existe el mismo eje de propiedad/modalidad tarifaria.
- La continuidad agregada no demuestra continuidad individual de cada usuario.
- `fecha_expedicion` mide facturación, no disponibilidad del dataset; no cierra OPO01.
- Exactitud requiere contraste con una fuente documental o maestra externa.
- Cero no debe convertirse automáticamente en dato faltante.

## Dimensiones DAMA-DMBOK2

La fuente permite evaluar completitud, validez, unicidad, consistencia, integridad y razonabilidad con los datos disponibles. Exactitud y oportunidad requieren evidencia adicional. La aplicabilidad de cada regla debe registrarse explícitamente en la matriz, sin usar `no_aplica` para ocultar una falta de evidencia.

Archivo de definición: [`sspd.yaml`](../../fuentes_datos/diccionarios/sspd.yaml).
