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
