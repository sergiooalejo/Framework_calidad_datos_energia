# Prioridad CREG: búsqueda de fuentes eléctricas

Revisión: 4 de noviembre de 2026. El usuario confirmó **mantener solo electricidad**. La CREG tiene prioridad como publicador, siempre que el conjunto permita cumplir la metodología. No se reduce el requisito de ocho dimensiones ni se cuentan anexos y vistas como casos completos solo para alcanzar cuatro fuentes.

## 1. Electricidad: panel de comercializadores, Circular 125 de 2025

Publicación oficial: https://gestornormativo.creg.gov.co/gestor/entorno/docs/circular_creg_0125_2025.htm

Excel oficial: https://gestornormativo.creg.gov.co/gestor/entorno/docs/originales/Circular_CREG_125_2025/Datos%20panel-IPC-empresas.xlsx

Archivo local: `datos/Datos_en_revision/CREG_prioridad/creg_panel_electrico_circular125_2025.xlsx`.

Se descargó el Excel y se inspeccionó su hoja:

- **88 registros de datos, 11 columnas y 23 empresas**.
- **Cinco períodos anuales: 2019, 2020, 2021, 2022 y 2023**; no todas las empresas tienen necesariamente los cinco.
- Columnas originales: `Empresa`, `Periodo`, `CG`, `EmpSer`, `DepAmo`, `GenMan`, `UsuRur`, `UsuUrb`, `Usu`, `RedUrb`, `RedRur`.
- Entre las empresas figuran EPM, CHEC, ESSA y EDEQ. Se conservaron los nombres observados; no se interpretan las siglas de costos sin revisar el informe técnico.
- El archivo contiene celdas vacías, coherentes con la necesidad de estudiar el alcance de información publicada. La circular advierte exclusión de información cuya divulgación no fue autorizada; no se infiere que cada vacío tenga esa causa.

**Decisión:** referencia sectorial prioritaria por ser CREG y electricidad, pero **no apta como caso completo del protocolo actual**: no cumple 10.000 registros ni longitud mensual de 49/61 observaciones. Tener fecha de la circular no equivale a contar con historia de disponibilidad mensual. No se transforman los cinco años en meses ficticios ni se multiplican filas por variables para cumplir volumen.

## 2. Electricidad: calidad de distribución, Circulares 053 y 064 de 2015

Publicaciones oficiales:

- https://gestornormativo.creg.gov.co/gestor/entorno/docs/circular_creg_0053_2015.htm
- https://gestornormativo.creg.gov.co/gestor/entorno/docs/circular_creg_0064_2015.htm

Se descargaron cuatro libros oficiales en `datos/Datos_en_revision/CREG_prioridad/`:

- `creg_calidad_sdl_053_2015_anexo.xlsx`.
- `creg_calidad_sdl_053_2015_anexo2.xlsx`.
- `creg_calidad_sdl_064_2015_anexo2.xlsx`.
- `creg_calidad_sdl_064_2015_anexo3.xlsx`.

Se inspeccionaron sus hojas por empresa, incluidas EPM, CHEC, ESSA y EDEQ. Contienen cuadros de frecuencia/duración, objetivos, ajustes y escenarios por año. Por ejemplo, en el anexo 2 de la Circular 064, la hoja EPM muestra indicadores reales y proyecciones «Año 0» a «Año 4». **Son resultados y escenarios de un estudio, no una serie mensual cruda verificada.**

Las hojas tienen aproximadamente 46–47 filas XML, que también incluyen etiquetas, fórmulas y formato; ese conteo no representa registros de interrupciones. Las celdas con años de escenario no se pueden tratar como observaciones históricas para cartas.

El informe del estudio menciona bases masivas utilizadas en el análisis. **Eso no demuestra que los anexos descargados contengan o hagan descargables esos microdatos.** No se verificó acceso a los archivos por transformador/evento mencionados en el informe ni su longitud temporal.

**Decisión:** conservar como referencias técnicas CREG, no contar estos cuatro archivos como cuatro datasets independientes aptos para todo el proyecto.

## 3. Estadísticas históricas eléctricas

ARIAE referencia estadísticas del sector eléctrico con autor/editor CREG:
https://www.ariae.org/servicio-documental/estadisticas-del-sector-electrico-de-colombia

La referencia es una pista de localización, no evidencia suficiente de un conjunto actualmente descargable. No se ha validado archivo, volumen, periodicidad ni continuidad por grupo para contarlo como caso completo.

## 4. Gas: excluido por decisión de alcance

El catálogo sí ofrece `ek3f-5wn4`, tarifas de gas publicadas por CREG. Se verificaron 165.360 filas y 238 meses, pero **no se incorpora porque el usuario decidió mantener solo electricidad**. Se retiró el CSV descargado del área de candidatos; quedan metadatos y un perfil pequeño como evidencia del descarte.

Las entradas `mbkj-hd98`, `f8zf-xyx8`, `duwb-pa7h`, `79rk-nbgs` y `qzkz-3vyk` son filtros o visualizaciones derivados de `ek3f-5wn4` según el catálogo consultado. No son cinco fuentes independientes. La consulta `q=CREG` devolvió 62 resultados; no se presenta como un censo de todo lo que la entidad podría publicar fuera de ese catálogo.

## Conclusión operativa

La prioridad CREG se mantiene, pero **esta revisión no identificó una fuente eléctrica publicada directamente por CREG que pueda declararse apta para todo el protocolo actual**. No es una afirmación de inexistencia: se documentan las publicaciones examinadas y sus limitaciones concretas.

Hasta disponer de una candidata CREG que supere esas pruebas, la propuesta de cuatro casos de electricidad sigue siendo **EPM, CHEC, Superservicios ZNI y XM**, con los pendientes de ocho dimensiones y reglas ya declarados. Los datos de XM están regulados por CREG, pero su publicador es XM; no se cambia su atribución.

Las bases CREG se pueden utilizar para fundamentar variables y contextualizar resultados, sin presentarlas como cumplimiento del cuarto caso ni usar valores de otra unidad/período como verdad de referencia automáticamente. No se modifica el catálogo definitivo ni se sustituyen los datasets medidos.

## Evidencia local

- `metadatos/candidatos_creg/catalogo_creg_2026-11-04.json`: respuesta de catálogo y relaciones entre vistas.
- `desarrollo_puntos/3.4/perfiles/creg_electricidad_anexos.json`: archivos, hojas, conteos XML y hashes de los libros eléctricos.
- `desarrollo_puntos/3.4/perfiles/creg_prioridad_perfil.json`: perfil del conjunto de gas descartado; no es una fuente seleccionada.

La fecha y los hashes registran la revisión/descarga; no prueban por sí solos oportunidad histórica por período.
