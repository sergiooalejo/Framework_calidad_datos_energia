# Matriz OE1: dimensiones, métricas, indicadores y reglas

Hito 3, actividad 1 · 27 de octubre de 2026 · EPM y CHEC.

**Estado:** especificación documental elaborada. No se presentan resultados de medición ni se declara cumplida la evaluación de las ocho dimensiones.

## Alcance y uso

Se definen 19 indicadores: las doce reglas base y siete controles complementarios. El CSV contiene 38 filas, una por control y fuente. El YAML es la especificación completa; no es un motor ejecutado.

Consumidores previstos: equipo de tesis para auditar datos tarifarios y usuarios analíticos que necesitan comparar tarifas publicadas por categoría y mes. La finalidad es detectar problemas de representación y valores sospechosos con evidencia trazable; no certificar legalidad de tarifas ni consumo real.

Se toma DAMA-DMBOK2 (2017), capítulo 13, como edición base. Las definiciones operativas, métricas y umbrales son del proyecto. El resumen oficial de cambios de DAMA confirma que una edición revisada incorpora una dimensión adicional; no se mezclan ediciones.

## Ocho dimensiones y relación con ISO

La relación con ISO/IEC 25012 es conceptual y parcial; no se afirma que sus características sean las mismas ocho dimensiones ni que la matriz certifique cumplimiento de la norma. Oportunidad de publicación no equivale por sí sola a actualidad del dato. Credibilidad no se añade como novena dimensión obligatoria.

| Dimensión | Definición aplicada a tarifas | Indicadores | Relación ISO |
|---|---|---|---|
| Completitud | Presencia de campos y observaciones requeridos para interpretar cada tarifa. | R01, R10 | completeness; directa conceptual |
| Validez | Conformidad de períodos, categorías e importes con dominios documentados. | R02, R03, R07, R11 | Sin equivalencia nominal única; sin equivalencia nominal unica |
| Unicidad | Una sola representación por entidad tarifaria y período dentro del alcance definido. | R04, R05 | Sin equivalencia nominal única; sin equivalencia nominal unica |
| Consistencia | Coherencia de etiquetas y relaciones de tarifas al comparar categorías equivalentes. | R06, R08, R09, MAP01, DEF01 | consistency; directa conceptual |
| Integridad | Estructura completa y referencias de categorías resolubles en catálogos versionados. | INT01, INT02 | Sin equivalencia nominal única; relacion parcial con completeness y consistency |
| Razonabilidad | Comportamiento tarifario compatible con una referencia temporal y contexto documentados. | R12, CART01 | Sin equivalencia nominal única; sin equivalencia nominal unica |
| Exactitud | Concordancia de valores con una publicación oficial equivalente y verificada. | EXA01 | accuracy; directa conceptual con alcance muestral |
| Oportunidad | Disponibilidad de la publicación requerida dentro del plazo que necesita el consumidor. | OPO01 | currentness; parcial no equivalente a actualidad |

## Diez tipos de regla

Los tipos son una clasificación, no diez reglas adicionales ni una exigencia de asignación uno a uno. Una regla puede tener más de un tipo; se declara un principal para evitar doble conteo. Los nombres en español son traducciones de trabajo.

| Tipo | Nombre | Controles clasificados |
|---|---|---|
| T01 | Conformidad definicional | DEF01 |
| T02 | Presencia y completitud | R01, R10 |
| T03 | Cumplimiento de formato | R03 |
| T04 | Pertenencia a dominio | R02, R06 |
| T05 | Conformidad de rango | R02, R07, R11, R12, CART01 |
| T06 | Conformidad de mapeo | MAP01 |
| T07 | Consistencia entre atributos | R08, R09, INT01, INT02 |
| T08 | Verificación de exactitud | EXA01 |
| T09 | Verificación de unicidad | R04, R05 |
| T10 | Validación de oportunidad | OPO01 |

## Reglas comunes de medición

- Todo indicador se calcula como porcentaje de unidades definidas; nunca mezclar celdas, filas, referencias y publicaciones en un denominador. Las tasas R11, R12 y CART01 son prevalencias de sospechas/alertas, no porcentajes de errores confirmados.
- Reportar elegibles, evaluadas, exclusiones por causa, fallos y cobertura por fuente, control y período. Si falta evidencia, el resultado es parcial o pendiente, sin aprobar la dimensión.
- Denominador cero produce valor nulo y motivo; no se convierte en 100 %. Toda exclusión debe ser visible y justificada antes de observar resultados.
- Las metas de 100 % son propuestas de conformidad total para unidades aplicables, no umbrales del profesor, de DAMA, de ISO ni del publicador. Las tasas estadísticas no tienen un umbral de aceptación inventado; requieren calibración.
- Tendencia por mes de vigencia y versión de descarga. Para oportunidad se usa período de publicación esperado. No confundir un análisis retrospectivo por vigencia con seguimiento histórico de publicación.
- Los responsables son roles; falta asignar nombres. No se inventan integrantes ni aprobaciones del director.
- Se conserva el original; las tasas se distinguen antes/después de preparar datos. No eliminar los fallos antes de calcular la calidad de la fuente.
- La meta final exige medición de las ocho dimensiones en cada fuente con alcance explícito. Los estados pendientes no acreditan el cierre.

## Fichas completas por indicador

### R01 · Período informado

- **Dimensión / tipo:** completitud / T02 (Presencia y completitud).
- **Métrica y población:** Todas las filas del snapshot original. Unidad observada: fila.
- **Numerador:** Filas con ambos campos de período informados.
- **Denominador:** Número total de filas.
- **Indicador:** 100 × numerador / denominador; unidad: porcentaje.
- **Umbral:** ≥ 100 % propuesto. Meta de conformidad total para las unidades aplicables; es una propuesta del proyecto, no un umbral de DAMA, ISO o del publicador. Reportar tasa continua aunque no alcance la meta.
- **Severidad:** error; se refiere al hallazgo, sin confirmación automática de error real.
- **Frecuencia:** En cada ejecución y nueva versión de descarga; por mes de vigencia cuando corresponda.
- **Responsable:** responsable_reglas_negocio; nombre pendiente.
- **Tendencia:** Mayor es mejor Por fuente y período de vigencia; conservar también el snapshot y versión de control.
- **EPM:** year y mes no vacíos.
- **CHEC:** costounitariotarifa_ano y costounitariotarifa_mes no vacíos.
- **Precondiciones:** N/A no es un período válido; distinguir presencia de validez.
- **Estado:** EPM 99.97 % (3622/3623, medido); CHEC 100 % (40609/40609, medido).

### R02 · Período válido

- **Dimensión / tipo:** validez / T04 (Pertenencia a dominio).
- **Métrica y población:** Filas con período presente por R01. Unidad observada: fila.
- **Numerador:** Filas cuyo año es entero y cuyo mes pertenece al dominio; fecha construible.
- **Denominador:** Filas con período presente.
- **Indicador:** 100 × numerador / denominador; unidad: porcentaje.
- **Umbral:** ≥ 100 % propuesto. Meta de conformidad total para las unidades aplicables; es una propuesta del proyecto, no un umbral de DAMA, ISO o del publicador. Reportar tasa continua aunque no alcance la meta.
- **Severidad:** error; se refiere al hallazgo, sin confirmación automática de error real.
- **Frecuencia:** En cada ejecución y nueva versión de descarga; por mes de vigencia cuando corresponda.
- **Responsable:** responsable_reglas_negocio; nombre pendiente.
- **Tendencia:** Mayor es mejor Por fuente y período de vigencia; conservar también el snapshot y versión de control.
- **EPM:** Mapear nombres de mes mediante catálogo explícito; validar year como entero sin truncar.
- **CHEC:** Validar año y mes enteros; mes de 1 a 12.
- **Precondiciones:** No rechazar nuevas fechas solo por exceder la cobertura de la descarga previa. Reportar excluidos por ausencia en R01.
- **Estado:** EPM 100 % (3622/3622, medido); CHEC 100 % (40609/40609, medido).

### R03 · Importes numéricos y finitos

- **Dimensión / tipo:** validez / T03 (Cumplimiento de formato).
- **Métrica y población:** Celdas monetarias informadas en campos aplicables según concepto. Unidad observada: celda.
- **Numerador:** Celdas convertibles sin ambigüedad a número finito.
- **Denominador:** Celdas informadas y aplicables.
- **Indicador:** 100 × numerador / denominador; unidad: porcentaje.
- **Umbral:** ≥ 100 % propuesto. Meta de conformidad total para las unidades aplicables; es una propuesta del proyecto, no un umbral de DAMA, ISO o del publicador. Reportar tasa continua aunque no alcance la meta.
- **Severidad:** error; se refiere al hallazgo, sin confirmación automática de error real.
- **Frecuencia:** En cada ejecución y nueva versión de descarga; por mes de vigencia cuando corresponda.
- **Responsable:** responsable_reglas_negocio; nombre pendiente.
- **Tendencia:** Mayor es mejor Por fuente y período de vigencia; conservar también el snapshot y versión de control.
- **EPM:** Cinco columnas monetarias; preservar texto original y evitar conversión ambigua de separadores.
- **CHEC:** Diez medidas declaradas texto; convertir con convención explícita y conservar original.
- **Precondiciones:** Matriz de aplicabilidad por concepto; nulos se reportan en completitud. No aceptar NaN o infinito como importes válidos.
- **Estado:** EPM 100 % (18110/18110, provisional); CHEC 100 % (406035/406035, provisional).

### R04 · Ausencia de duplicados exactos adicionales

- **Dimensión / tipo:** unicidad / T09 (Verificación de unicidad).
- **Métrica y población:** Todas las filas originales, sin campos técnicos generados. Unidad observada: fila.
- **Numerador:** Total de filas menos duplicados exactos adicionales.
- **Denominador:** Número total de filas.
- **Indicador:** 100 × numerador / denominador; unidad: porcentaje.
- **Umbral:** ≥ 100 % propuesto. Meta de conformidad total para las unidades aplicables; es una propuesta del proyecto, no un umbral de DAMA, ISO o del publicador. Reportar tasa continua aunque no alcance la meta.
- **Severidad:** error; se refiere al hallazgo, sin confirmación automática de error real.
- **Frecuencia:** En cada ejecución y nueva versión de descarga; por mes de vigencia cuando corresponda.
- **Responsable:** responsable_reglas_negocio; nombre pendiente.
- **Tendencia:** Mayor es mejor Por fuente y período de vigencia; conservar también el snapshot y versión de control.
- **EPM:** Comparar las 12 columnas originales.
- **CHEC:** Comparar las 24 columnas originales.
- **Precondiciones:** Una clase de n filas idénticas aporta n-1 duplicados; no usar esa cifra para R05.
- **Estado:** EPM 99.72 % (3613/3623, medido); CHEC 100 % (40609/40609, medido).

### R05 · Clave tarifaria sin multiplicidad

- **Dimensión / tipo:** unicidad / T09 (Verificación de unicidad).
- **Métrica y población:** Filas con clave completa y período válido; tras identificar copias exactas y conservar una por clase. Unidad observada: fila.
- **Numerador:** Filas cuya clave candidata tiene una sola representación.
- **Denominador:** Filas con clave evaluable en esa etapa.
- **Indicador:** 100 × numerador / denominador; unidad: porcentaje.
- **Umbral:** ≥ 100 % propuesto. Meta de conformidad total para las unidades aplicables; es una propuesta del proyecto, no un umbral de DAMA, ISO o del publicador. Reportar tasa continua aunque no alcance la meta.
- **Severidad:** advertencia; se refiere al hallazgo, sin confirmación automática de error real.
- **Frecuencia:** En cada ejecución y nueva versión de descarga; por mes de vigencia cuando corresponda.
- **Responsable:** responsable_reglas_negocio; nombre pendiente.
- **Tendencia:** Mayor es mejor Por fuente y período de vigencia; conservar también el snapshot y versión de control.
- **EPM:** Cinco categorías normalizadas + fecha mensual.
- **CHEC:** Doce categorías originales como clave provisional + fecha; revisar dependencias código-nombre antes de fijar clave final.
- **Precondiciones:** Versionar la clave y las equivalencias. Todas las filas de una clave multiplicada incumplen; separar redundancia semántica y valores en conflicto.
- **Estado:** EPM 100 % (3612/3612, medido); CHEC 88.44 % (35914/40609, provisional).

### R06 · Representación canónica

- **Dimensión / tipo:** consistencia / T04 (Pertenencia a dominio).
- **Métrica y población:** Celdas categóricas informadas con catálogo canónico aprobado. Unidad observada: celda categórica.
- **Numerador:** Celdas cuyo valor original ya coincide con su forma canónica.
- **Denominador:** Celdas categóricas con catálogo aprobado.
- **Indicador:** 100 × numerador / denominador; unidad: porcentaje.
- **Umbral:** ≥ 100 % propuesto. Meta de conformidad total para las unidades aplicables; es una propuesta del proyecto, no un umbral de DAMA, ISO o del publicador. Reportar tasa continua aunque no alcance la meta.
- **Severidad:** advertencia; se refiere al hallazgo, sin confirmación automática de error real.
- **Frecuencia:** En cada ejecución y nueva versión de descarga; por mes de vigencia cuando corresponda.
- **Responsable:** responsable_reglas_negocio; nombre pendiente.
- **Tendencia:** Mayor es mejor Por fuente y período de vigencia; conservar también el snapshot y versión de control.
- **EPM:** Tipo de tarifa, tipo de dato y rango de consumo; conservar variantes originales.
- **CHEC:** Código/nombre, modalidad, clase, estrato y rangos según catálogo de cada campo.
- **Precondiciones:** Una variante no canónica es advertencia de estandarización, no necesariamente valor incorrecto. No convertir la moda observada en referencia oficial; medir cobertura de catálogo aparte.
- **Estado:** EPM 98.85 % (8626/8726, provisional); CHEC 100 % (340215/340215, provisional).

### R07 · Signo y rango por concepto

- **Dimensión / tipo:** validez / T05 (Conformidad de rango).
- **Métrica y población:** Importes numéricos aplicables con dominio documentado. Unidad observada: celda.
- **Numerador:** Importes dentro del dominio específico del concepto.
- **Denominador:** Importes con dominio verificable.
- **Indicador:** 100 × numerador / denominador; unidad: porcentaje.
- **Umbral:** ≥ 100 % propuesto. Meta de conformidad total para las unidades aplicables; es una propuesta del proyecto, no un umbral de DAMA, ISO o del publicador. Reportar tasa continua aunque no alcance la meta.
- **Severidad:** error; se refiere al hallazgo, sin confirmación automática de error real.
- **Frecuencia:** En cada ejecución y nueva versión de descarga; por mes de vigencia cuando corresponda.
- **Responsable:** responsable_reglas_negocio; nombre pendiente.
- **Tendencia:** Mayor es mejor Por fuente y período de vigencia; conservar también el snapshot y versión de control.
- **EPM:** Revisar restricciones por separado; no aplicar no negatividad general a todos los conceptos.
- **CHEC:** Definir dominio de cada componente; subcon y cureal requieren definición antes de evaluar.
- **Precondiciones:** Excluir solo con causa explícita cuando falte el dominio; eso no aprueba el control.
- **Estado:** EPM 100 % (18110/18110, provisional); CHEC 98.99 % (401948/406035, provisional).

### R08 · Orden entre tarifas por propiedad

- **Dimensión / tipo:** consistencia / T07 (Consistencia entre atributos).
- **Métrica y población:** Comparaciones completas de igual período, concepto y categoría salvo propiedad; nivel 1. Unidad observada: comparación de propiedad.
- **Numerador:** Comparaciones que respetan el orden documentado con tolerancia de redondeo.
- **Denominador:** Comparaciones completas con orden autorizado.
- **Indicador:** 100 × numerador / denominador; unidad: porcentaje.
- **Umbral:** ≥ 100 % propuesto. Meta de conformidad total para las unidades aplicables; es una propuesta del proyecto, no un umbral de DAMA, ISO o del publicador. Reportar tasa continua aunque no alcance la meta.
- **Severidad:** advertencia; se refiere al hallazgo, sin confirmación automática de error real.
- **Frecuencia:** En cada ejecución y nueva versión de descarga; por mes de vigencia cuando corresponda.
- **Responsable:** responsable_reglas_negocio; nombre pendiente.
- **Tendencia:** Mayor es mejor Por fuente y período de vigencia; conservar también el snapshot y versión de control.
- **EPM:** Propiedad EPM >= compartida >= cliente en la misma fila del nivel I; contrastar fundamento documental.
- **CHEC:** Alinear filas por las demás categorías y propiedad; confirmar las tres etiquetas y variable comparada antes de exigir el orden.
- **Precondiciones:** No comparar filas con estrato, modalidad o rango diferentes. Falta de un miembro de comparación se registra como falta de cobertura, no cumplimiento.
- **Estado:** EPM 99.91 % (2146/2148, provisional); CHEC sin medir (no_medible).

### R09 · Estructura de importes según categoría

- **Dimensión / tipo:** consistencia / T07 (Consistencia entre atributos).
- **Métrica y población:** Filas con nivel/modalidad identificados y matriz de aplicabilidad documentada. Unidad observada: fila.
- **Numerador:** Filas que cumplen todas las condiciones de aplicabilidad por nivel y modalidad.
- **Denominador:** Filas con matriz de aplicabilidad evaluable.
- **Indicador:** 100 × numerador / denominador; unidad: porcentaje.
- **Umbral:** ≥ 100 % propuesto. Meta de conformidad total para las unidades aplicables; es una propuesta del proyecto, no un umbral de DAMA, ISO o del publicador. Reportar tasa continua aunque no alcance la meta.
- **Severidad:** advertencia; se refiere al hallazgo, sin confirmación automática de error real.
- **Frecuencia:** En cada ejecución y nueva versión de descarga; por mes de vigencia cuando corresponda.
- **Responsable:** responsable_reglas_negocio; nombre pendiente.
- **Tendencia:** Mayor es mejor Por fuente y período de vigencia; conservar también el snapshot y versión de control.
- **EPM:** Revisar patrón del código: nivel I usa propiedad; otros niveles usan punta/fuera de punta. Validar si cero significa no aplica.
- **CHEC:** Comprobar combinaciones nivel-propiedad-modalidad-concepto; no exigir columnas punta/fuera de punta inexistentes.
- **Precondiciones:** En CHEC este es un adaptador semántico, no una copia literal del código EPM.
- **Estado:** EPM 100 % (3623/3623, provisional); CHEC sin medir (no_medible).

### R10 · Importes requeridos disponibles

- **Dimensión / tipo:** completitud / T02 (Presencia y completitud).
- **Métrica y población:** Filas para las que se conocen las medidas requeridas. Unidad observada: fila.
- **Numerador:** Filas con todos los importes obligatorios informados y sin marcador de ausencia documentado.
- **Denominador:** Filas con conjunto de medidas requeridas definido.
- **Indicador:** 100 × numerador / denominador; unidad: porcentaje.
- **Umbral:** ≥ 100 % propuesto. Meta de conformidad total para las unidades aplicables; es una propuesta del proyecto, no un umbral de DAMA, ISO o del publicador. Reportar tasa continua aunque no alcance la meta.
- **Severidad:** advertencia; se refiere al hallazgo, sin confirmación automática de error real.
- **Frecuencia:** En cada ejecución y nueva versión de descarga; por mes de vigencia cuando corresponda.
- **Responsable:** responsable_reglas_negocio; nombre pendiente.
- **Tendencia:** Mayor es mejor Por fuente y período de vigencia; conservar también el snapshot y versión de control.
- **EPM:** Evaluar columnas aplicables por nivel y concepto.
- **CHEC:** Evaluar tarifa/CU y componentes requeridos por el concepto; no exigir todo campo en toda fila.
- **Precondiciones:** Cambio propuesto frente al código: todos ceros no prueba incompletitud. Un cero informado cuenta como presente salvo documentación que lo defina como ausencia.
- **Estado:** EPM 99.94 % (3621/3623, provisional); CHEC 100 % (40609/40609, provisional).
- **Cambio frente al código:** El Hito 2 alerta filas con todos los importes en cero. Conservar ese hallazgo como sospecha, pero no medirlo como ausencia confirmada.

### R11 · Sospecha de serial de fecha en importe

- **Dimensión / tipo:** validez / T05 (Conformidad de rango).
- **Métrica y población:** Importes numéricos finitos en campos monetarios aplicables. Unidad observada: celda.
- **Numerador:** Importes enteros dentro del intervalo configurado de seriales Excel.
- **Denominador:** Importes numéricos finitos aplicables.
- **Indicador:** 100 × numerador / denominador; unidad: porcentaje.
- **Umbral:** Pendiente de calibración; informativo. No se prescribe tasa cero ni se equiparan alertas con errores. Calibrar en referencia y validación; congelar antes de vigilancia.
- **Severidad:** advertencia; se refiere al hallazgo, sin confirmación automática de error real.
- **Frecuencia:** En cada ejecución y nueva versión de descarga; por mes de vigencia cuando corresponda.
- **Responsable:** responsable_reglas_negocio; nombre pendiente.
- **Tendencia:** Interpretar según contexto; menor no significa necesariamente mejor calidad. Por fuente y período de vigencia; conservar también el snapshot y versión de control.
- **EPM:** Intervalo heredado [36526, 47483]; no confirma error.
- **CHEC:** Misma heurística solo tras revisar escala y unidad; los valores legítimos pueden caer en el intervalo.
- **Precondiciones:** No es indicador de exactitud confirmada ni criterio automático de cuarentena.
- **Estado:** EPM 0.0166 % (3/18110, medido); CHEC 0 % (0/406035, medido).
- **Cambio frente al código:** Reclasificación propuesta de Exactitud a Validez y severidad de sospecha; no se cambió el motor.
- **Parámetros:** {"serial_min": 36526, "serial_max": 47483}.

### R12 · Prevalencia de magnitud atípica

- **Dimensión / tipo:** razonabilidad / T05 (Conformidad de rango).
- **Métrica y población:** Observaciones numéricas en series homogéneas con referencia válida. Unidad observada: serie-mes.
- **Numerador:** Observaciones con abs(valor) > factor * mediana(abs(referencia)).
- **Denominador:** Observaciones evaluables en vigilancia.
- **Indicador:** 100 × numerador / denominador; unidad: porcentaje.
- **Umbral:** Pendiente de calibración; informativo. No se prescribe tasa cero ni se equiparan alertas con errores. Calibrar en referencia y validación; congelar antes de vigilancia.
- **Severidad:** advertencia; se refiere al hallazgo, sin confirmación automática de error real.
- **Frecuencia:** En cada ejecución y nueva versión de descarga; por mes de vigencia cuando corresponda.
- **Responsable:** responsable_metricas_anomalias; nombre pendiente.
- **Tendencia:** Interpretar según contexto; menor no significa necesariamente mejor calidad. Por fuente y período de vigencia; conservar también el snapshot y versión de control.
- **EPM:** Serie = categorías + columna monetaria.
- **CHEC:** Serie = categorías + variable monetaria; no mezclar CU y tarifa.
- **Precondiciones:** Mediana de referencia estrictamente positiva; no estimarla con vigilancia. Factor 10 heredado, pendiente sensibilidad 5/10/20. No sustituye valoración de inflación, subsidio o cambio regulatorio.
- **Estado:** EPM 0.0426 % (4/9379, provisional); CHEC 0 % (0/355289, provisional).
- **Cambio frente al código:** El código usa mediana de toda la serie y severidad Error; se propone referencia temporal y Advertencia.
- **Parámetros:** {"factor": 10, "sensibilidad": [5, 10, 20]}.

### INT01 · Contrato estructural íntegro

- **Dimensión / tipo:** integridad / T07 (Consistencia entre atributos).
- **Métrica y población:** Columnas y contratos de tipo declarados por versión del esquema. Unidad observada: columna esperada.
- **Numerador:** Columnas presentes exactamente una vez con contrato de lectura compatible.
- **Denominador:** Columnas esperadas en el esquema versionado.
- **Indicador:** 100 × numerador / denominador; unidad: porcentaje.
- **Umbral:** ≥ 100 % propuesto. Meta de conformidad total para las unidades aplicables; es una propuesta del proyecto, no un umbral de DAMA, ISO o del publicador. Reportar tasa continua aunque no alcance la meta.
- **Severidad:** error; se refiere al hallazgo, sin confirmación automática de error real.
- **Frecuencia:** En cada ejecución y nueva versión de descarga; por mes de vigencia cuando corresponda.
- **Responsable:** responsable_datos; nombre pendiente.
- **Tendencia:** Mayor es mejor Por fuente y período de vigencia; conservar también el snapshot y versión de control.
- **EPM:** Doce columnas oficiales, con cinco medidas numéricas.
- **CHEC:** Veinticuatro columnas oficiales; texto monetario es compatible si existe conversión definida.
- **Precondiciones:** Columnas extra se reportan aparte como deriva de esquema, sin suponer pérdida. Este control no demuestra integridad referencial por sí solo.
- **Estado:** EPM 100 % (12/12, medido); CHEC 100 % (24/24, medido).

### INT02 · Referencias categóricas resolubles

- **Dimensión / tipo:** integridad / T07 (Consistencia entre atributos).
- **Métrica y población:** Referencias aplicables de categorías/códigos contra catálogos versionados. Unidad observada: referencia por fila.
- **Numerador:** Referencias que resuelven a una entidad y combinación vigente permitida.
- **Denominador:** Referencias con catálogo verificable.
- **Indicador:** 100 × numerador / denominador; unidad: porcentaje.
- **Umbral:** ≥ 100 % propuesto. Meta de conformidad total para las unidades aplicables; es una propuesta del proyecto, no un umbral de DAMA, ISO o del publicador. Reportar tasa continua aunque no alcance la meta.
- **Severidad:** error; se refiere al hallazgo, sin confirmación automática de error real.
- **Frecuencia:** En cada ejecución y nueva versión de descarga; por mes de vigencia cuando corresponda.
- **Responsable:** responsable_datos; nombre pendiente.
- **Tendencia:** Mayor es mejor Por fuente y período de vigencia; conservar también el snapshot y versión de control.
- **EPM:** Relacionar combinación tarifaria con catálogo de modalidades, conceptos, nivel y rangos autorizado.
- **CHEC:** Comercializador, mercado y clase código-nombre; combinaciones permitidas de nivel/propiedad/estrato.
- **Precondiciones:** El catálogo debe tener referencia documental; no basta extraer todos los valores del mismo CSV. Una referencia sin clave es fallo si la clave es obligatoria; catálogo ausente es falta de evidencia.
- **Estado:** EPM sin medir (no_medible); CHEC 96.15 % (25/26, provisional).

### EXA01 · Concordancia documental de importes

- **Dimensión / tipo:** exactitud / T08 (Verificación de exactitud).
- **Métrica y población:** Muestra predefinida de importes con categoría, unidad y mes comparables. Unidad observada: celda seleccionada para contraste.
- **Numerador:** Celdas contrastadas que coinciden con el valor de referencia bajo precisión documentada.
- **Denominador:** Celdas efectivamente contrastadas con referencia verificada.
- **Indicador:** 100 × numerador / denominador; unidad: porcentaje.
- **Umbral:** ≥ 100 % propuesto. Meta de conformidad total para las unidades aplicables; es una propuesta del proyecto, no un umbral de DAMA, ISO o del publicador. Reportar tasa continua aunque no alcance la meta.
- **Severidad:** error; se refiere al hallazgo, sin confirmación automática de error real.
- **Frecuencia:** En cada ejecución y nueva versión de descarga; por mes de vigencia cuando corresponda.
- **Responsable:** responsable_validacion; nombre pendiente.
- **Tendencia:** Mayor es mejor Por fuente y período de vigencia; conservar también el snapshot y versión de control.
- **EPM:** Publicación tarifaria original EPM con concepto, nivel, propiedad y franja equivalentes.
- **CHEC:** Publicación CHEC con mercado, estrato, nivel, propiedad, concepto y período equivalentes.
- **Precondiciones:** Seleccionar muestra antes de buscar concordancia; registrar semilla, estratos y universo. Separar muestra aleatoria de alertas seleccionadas por conveniencia. Usar Decimal y regla de redondeo documentada a precisión comparable; no elegir tolerancia después de observar diferencias. Publicación original es referencia de concordancia, no prueba independiente de tarifa económicamente correcta.
- **Estado:** EPM sin medir (no_medible); CHEC 100 % (756/756, provisional).
- **Parámetros:** {"tamano_muestra_por_fuente": null, "semilla": 2026, "precision_comparacion": null, "regla_redondeo": null}.

### OPO01 · Publicaciones disponibles dentro del plazo

- **Dimensión / tipo:** oportunidad / T10 (Validación de oportunidad).
- **Métrica y población:** Publicaciones esperadas por fuente y período dentro del alcance temporal fijado. Unidad observada: publicación fuente-período-versión.
- **Numerador:** Publicaciones con evidencia que acredita disponibilidad a más tardar en la fecha límite.
- **Denominador:** Publicaciones con fecha límite y disponibilidad evaluable mediante evidencia.
- **Indicador:** 100 × numerador / denominador; unidad: porcentaje.
- **Umbral:** ≥ 100 % propuesto. Meta de conformidad total para las unidades aplicables; es una propuesta del proyecto, no un umbral de DAMA, ISO o del publicador. Reportar tasa continua aunque no alcance la meta.
- **Severidad:** advertencia; se refiere al hallazgo, sin confirmación automática de error real.
- **Frecuencia:** En cada ejecución y nueva versión de descarga; por mes de vigencia cuando corresponda.
- **Responsable:** responsable_datos; nombre pendiente.
- **Tendencia:** Mayor es mejor Por fuente y período de vigencia; conservar también el snapshot y versión de control.
- **EPM:** Reconstruir evidencia temporal de publicaciones EPM, sin usar year/mes como fecha de publicación.
- **CHEC:** Reconstruir evidencia de publicaciones CHEC; fecha de carga del dataset no prueba cada período.
- **Precondiciones:** Definir primero consumidor, obligación o plazo operativo y zona horaria. Primera observación en un rastreo solo acota disponibilidad: clasificar como indeterminado si el intervalo cruza el plazo. Ausencia de evidencia no demuestra ni puntualidad ni retraso. Un seguimiento prospectivo se declara aparte; no valida el histórico retrospectivamente.
- **Estado:** EPM sin medir (no_medible); CHEC sin medir (no_medible).
- **Parámetros:** {"plazo_documentado": null, "zona_horaria": "America/Bogota", "periodo_inicio": null, "periodo_fin": null}.

### MAP01 · Equivalencias de etiquetas verificadas

- **Dimensión / tipo:** consistencia / T06 (Conformidad de mapeo).
- **Métrica y población:** Equivalencias aplicadas por el adaptador en las filas del snapshot. Unidad observada: mapeo utilizado.
- **Numerador:** Mapeos con significado equivalente y fundamento registrado.
- **Denominador:** Mapeos distintos aplicados.
- **Indicador:** 100 × numerador / denominador; unidad: porcentaje.
- **Umbral:** ≥ 100 % propuesto. Meta de conformidad total para las unidades aplicables; es una propuesta del proyecto, no un umbral de DAMA, ISO o del publicador. Reportar tasa continua aunque no alcance la meta.
- **Severidad:** error; se refiere al hallazgo, sin confirmación automática de error real.
- **Frecuencia:** En cada ejecución y nueva versión de descarga; por mes de vigencia cuando corresponda.
- **Responsable:** responsable_datos; nombre pendiente.
- **Tendencia:** Mayor es mejor Por fuente y período de vigencia; conservar también el snapshot y versión de control.
- **EPM:** Validar por escrito equivalencias como variantes de 0-CS; no asumirlas solo por similitud.
- **CHEC:** Validar etiquetas de propiedad, clase y mercado; no fusionar códigos distintos por nombre parecido.
- **Precondiciones:** Sin equivalencias usadas, denominador cero se reporta sin unidades, no como 100 %. R06 mide representación original; MAP01 verifica que normalizar no cambie significado.
- **Estado:** EPM sin medir (no_medible); CHEC sin medir (no_medible).

### DEF01 · Semántica de variables críticas documentada

- **Dimensión / tipo:** consistencia / T01 (Conformidad definicional).
- **Métrica y población:** Variables críticas incluidas en las reglas o en las series de cada fuente. Unidad observada: variable crítica.
- **Numerador:** Variables con significado, unidad y uso aprobados mediante evidencia de la fuente.
- **Denominador:** Variables críticas planificadas.
- **Indicador:** 100 × numerador / denominador; unidad: porcentaje.
- **Umbral:** ≥ 100 % propuesto. Meta de conformidad total para las unidades aplicables; es una propuesta del proyecto, no un umbral de DAMA, ISO o del publicador. Reportar tasa continua aunque no alcance la meta.
- **Severidad:** advertencia; se refiere al hallazgo, sin confirmación automática de error real.
- **Frecuencia:** En cada ejecución y nueva versión de descarga; por mes de vigencia cuando corresponda.
- **Responsable:** responsable_datos; nombre pendiente.
- **Tendencia:** Mayor es mejor Por fuente y período de vigencia; conservar también el snapshot y versión de control.
- **EPM:** Tipo de dato y cinco importes; distinguir COP/kWh y otros cargos según concepto.
- **CHEC:** CU, tarifa, componentes; confirmar tipomed, cureal y subcon si intervienen en controles.
- **Precondiciones:** Indicador de preparación semántica del contrato; no es exactitud de los valores. No excluir del denominador una variable solo porque su significado aún no se conoce.
- **Estado:** EPM sin medir (no_medible); CHEC sin medir (no_medible).

### CART01 · Tasa de alertas de cartas I-MR

- **Dimensión / tipo:** razonabilidad / T05 (Conformidad de rango).
- **Métrica y población:** Cambios logarítmicos válidos y vigilados tras referencia independiente. Unidad observada: serie-mes vigilado.
- **Numerador:** Meses vigilados que activan I o MR (unión, sin doble conteo).
- **Denominador:** Meses efectivamente vigilados.
- **Indicador:** 100 × numerador / denominador; unidad: porcentaje.
- **Umbral:** Pendiente de calibración; informativo. No se prescribe tasa cero ni se equiparan alertas con errores. Calibrar en referencia y validación; congelar antes de vigilancia.
- **Severidad:** advertencia; se refiere al hallazgo, sin confirmación automática de error real.
- **Frecuencia:** En cada ejecución y nueva versión de descarga; por mes de vigencia cuando corresponda.
- **Responsable:** responsable_metricas_anomalias; nombre pendiente.
- **Tendencia:** Interpretar según contexto; menor no significa necesariamente mejor calidad. Por fuente y período de vigencia; conservar también el snapshot y versión de control.
- **EPM:** Categorías EPM y variable monetaria; agrupar dependencia por categoría en evaluación.
- **CHEC:** Categorías CHEC y CU/tarifa por separado; no sumar como réplicas independientes.
- **Precondiciones:** Solo valores positivos, únicos y meses consecutivos; no interpolar para ocultar huecos. Referencia base propuesta de 36 cambios y al menos 12 de vigilancia (49 observaciones). Excluir cambios que tocan valores en cuarentena; MR exige cambios válidos adyacentes. Contrastar alertas sistémicas con contexto; no clasificarlas automáticamente como error ni como cambio regulatorio confirmado.
- **Estado:** EPM sin medir (no_medible); CHEC sin medir (no_medible).
- **Parámetros:** {"cambios_referencia_base": 36, "min_cambios_vigilancia": 12, "sensibilidad_referencia": [24, 36, 48], "constante_I": 2.66, "constante_MR": 3.267}.

<!-- INICIO LINEA BASE -->
## Línea base medida

Valores calculados por [`medir_matriz_oe1.py`](medir_matriz_oe1.py) sobre los CSV de
`fuentes_datos/datos/`, aplicando las definiciones de población, numerador y denominador
de esta misma matriz. Última ejecución: 2026-10-28T22:04:08Z.

| Archivo medido | Filas | SHA-256 |
|---|---|---|
| `fuentes_datos/datos/epm_sfcd-b3ey.csv` | 3623 | `98acd40e8d2b92433b1dfc60422228f26f53ab331fd600631f03f830e7ba38f4` |
| `fuentes_datos/datos/chec_c698-wqig.csv` | 40609 | `05865b094a4cc4eb9f822ed2af686a11a8905d6606f40bb554f5bb5258e3c53f` |

> Estos hashes no coinciden con `fuentes_datos/verificaciones/manifiesto_archivos.json`.
> La causa está identificada y no es corrupción: el repositorio no declara política de fin
> de línea y `core.autocrlf` convierte LF a CRLF al extraer en Windows, lo que añade un byte
> por línea. Convirtiendo el archivo de EPM a LF se obtiene exactamente el hash del manifiesto.
> Un hash de archivo de texto solo es verificable si la política de fin de línea está declarada.

### Resultado por control

| Control | EPM | CHEC | Estado EPM / CHEC |
|---|---|---|---|
| R01 | 99.97 %<br><sub>3622/3623</sub> | 100 %<br><sub>40609/40609</sub> | medido / medido |
| R02 | 100 %<br><sub>3622/3622</sub> | 100 %<br><sub>40609/40609</sub> | medido / medido |
| R03 | 100 %<br><sub>18110/18110</sub> | 100 %<br><sub>406035/406035</sub> | provisional / provisional |
| R04 | 99.72 %<br><sub>3613/3623</sub> | 100 %<br><sub>40609/40609</sub> | medido / medido |
| R05 | 100 %<br><sub>3612/3612</sub> | 88.44 %<br><sub>35914/40609</sub> | medido / provisional |
| R06 | 98.85 %<br><sub>8626/8726</sub> | 100 %<br><sub>340215/340215</sub> | provisional / provisional |
| R07 | 100 %<br><sub>18110/18110</sub> | 98.99 %<br><sub>401948/406035</sub> | provisional / provisional |
| R08 | 99.91 %<br><sub>2146/2148</sub> | — | provisional / no_medible |
| R09 | 100 %<br><sub>3623/3623</sub> | — | provisional / no_medible |
| R10 | 99.94 %<br><sub>3621/3623</sub> | 100 %<br><sub>40609/40609</sub> | provisional / provisional |
| R11 | 0.0166 %<br><sub>3/18110</sub> | 0 %<br><sub>0/406035</sub> | medido / medido |
| R12 | 0.0426 %<br><sub>4/9379</sub> | 0 %<br><sub>0/355289</sub> | provisional / provisional |
| INT01 | 100 %<br><sub>12/12</sub> | 100 %<br><sub>24/24</sub> | medido / medido |
| INT02 | — | 96.15 %<br><sub>25/26</sub> | no_medible / provisional |
| EXA01 | — | 100 %<br><sub>756/756</sub> | no_medible / provisional |
| OPO01 | — | — | no_medible / no_medible |
| MAP01 | — | — | no_medible / no_medible |
| DEF01 | — | — | no_medible / no_medible |
| CART01 | — | — | no_medible / no_medible |

### Observación de apoyo: continuidad de cobertura

| Fuente | Períodos presentes | Esperados en la ventana | Ventana |
|---|---|---|---|
| EPM | 61 | 61 | 2016-12 a 2021-12 |
| CHEC | 225 | 225 | 2008-01 a 2026-09 |

**No acredita OPO01 y no debe presentarse como tal.** OPO01 exige evidencia de que cada
publicación estuvo disponible dentro de un plazo documentado, y su propia especificación
prohíbe usar `year`/`mes` como fecha de publicación. La continuidad solo muestra que no
faltan períodos dentro de la ventana, que es una propiedad distinta.

### Lo que cambia al aplicar las definiciones de esta matriz

**R05 en EPM da 100 %.** La población exige conservar una fila por clase de copia exacta
antes de evaluar la clave. Con ese paso no queda ninguna clave repetida: las repeticiones
de clave en EPM son las mismas filas que ya detecta R04. Medir R05 sin deduplicar primero
reporta como defecto de unicidad lo que ya se contó una vez.

**R07 en EPM da 100 %.** Los 15 importes negativos
están todos en el concepto con excepción documentada: 15 en Restricciones: Rm. Ningún otro concepto presenta
negativos, de modo que la excepción describe el dato en lugar de relajarlo.

**R03 en EPM da 100 %.** El denominador de esta matriz son las celdas *informadas*. Las
celdas vacías no entran y se reportan en completitud; contarlas como fallo de formato
mezcla dos dimensiones.

### Hallazgos que surgen de medir

**R10 con unidad de observación «fila» no detecta columnas vacías.** El control da
99.94 % en EPM y 100 % en CHEC porque toda fila
tiene al menos un importe informado. El detalle por columna en CHEC muestra otra realidad:

| Columna | Ceros | % de filas | Negativos | Vacías |
|---|---|---|---|---|
| `cureal` | 33871 | 83.4 % | 0 | 0 |
| `subcon` | 16854 | 41.5 % | 3360 | 11 |
| `generacion` | 11 | 0.0 % | 0 | 0 |
| `restricciones` | 0 | 0.0 % | 727 | 11 |
| `distribucion` | 0 | 0.0 % | 0 | 11 |
| `comercializacion` | 0 | 0.0 % | 0 | 11 |
| `perdidas` | 0 | 0.0 % | 0 | 11 |

Se propone cambiar la unidad de observación de R10 de fila a celda por columna. Es un cambio
en la especificación, no en el código, y sin él un scorecard declararía a CHEC completo.

**`cureal` y `subcon` necesitan DEF01 antes de que R07 y R10 signifiquen algo.** Un 83 % de
ceros en una columna y un 41 % en otra no se interpretan sin saber qué representan. La matriz
ya lo advierte; la medición lo cuantifica.

**INT02 encuentra su primer caso en CHEC.**

- `claseservicio_codigo = 'RS'` resuelve a 7 descripciones: Residencial Estrato 4 (4560) · Residencial Estrato 5 (2955) · Residencial Estrato 6 (2907) · Residencial (1800) · Residencial Estrato 2 (1092) · Residencial Estrato 3 (1073) · Residencial Estrato 1 (956)

El estrato ya viaja en `claseservicio_estrato` y la descripción lo duplica en la mayoría de
las filas pero no en todas. Es denormalización inconsistente, que es el defecto que INT02
existe para detectar.

**R06 no detecta sinónimos.** Sin catálogo canónico aprobado, la medición toma como forma
canónica la variante más frecuente tras normalizar mayúsculas y espacios. Con ese criterio
CHEC da 100 %: no hay variantes de capitalización. No significa que esté limpio en
consistencia, sino que este criterio solo ve diferencias de forma. Los sinónimos son
competencia de MAP01, que sigue sin evidencia.

### Qué sigue sin poder medirse

| Control | Qué falta |
|---|---|
| EXA01 | La publicación tarifaria original de cada entidad. Las alertas de R11, R12 y las cartas solo generan sospechas. |
| OPO01 | Evidencia de la fecha real de disponibilidad por período y un plazo esperado documentado. |
| MAP01 | Validación escrita de que dos etiquetas significan lo mismo. |
| DEF01 | Significado, unidad y uso aprobados por la fuente. |
| CART01 | Las cartas en cambios logarítmicos de la actividad 5 del Hito 3. |
| R08 y R09 en CHEC | Matriz de combinaciones nivel-propiedad-modalidad-concepto y confirmación de las etiquetas de propiedad. |

Cinco de los diecinueve controles dependen de evidencia externa a los conjuntos. Esa es la
brecha real del punto 1, y no se cierra midiendo mejor.
<!-- FIN LINEA BASE -->

## Evidencia externa y cierre

Exactitud y oportunidad requieren datos que no están en los CSV de tarifas. Se incluyen plantillas vacías; no se inventan fechas, documentos ni resultados. Para integridad se necesita también un catálogo autorizado y versionado.

- `plantilla_exactitud.csv`: universo/muestra preseleccionada, clave, celda, referencia, precisión y verificación. Una muestra de alertas no estima por sí sola exactitud poblacional.
- `plantilla_oportunidad.csv`: calendario esperado, límites de observación de disponibilidad y evidencia; separar períodos sin evidencia de retrasos confirmados.
- `plantilla_catalogos.csv`: valores, relaciones y equivalencias con fuente y vigencia. Un catálogo extraído del mismo CSV no valida su corrección.

El punto 1 entrega la matriz y las fichas; su validación metodológica sigue pendiente de revisión del equipo/director, cierre de catálogos y calibración. La implementación y los scorecards empíricos corresponden a las siguientes actividades. No se marca completo el Hito 3.

## Referencias

- DAMA International (2017). *DAMA-DMBOK2*, cap. 13, tabla de dimensiones (pp. 461–462) y tipos de regla, sección 1.3.7 (pp. 467–468). [PDF del editor](https://technicspub.com/wp-content/uploads/2023/07/DAMA-DMBOK2.pdf). Se consultó para contrastar las categorías; las fichas son formulaciones propias del proyecto.
- [DAMA: cambios en la edición revisada](https://www.damadmbok.org/dmbok2-revisions). Consulta: 27 de octubre de 2026.
- [ISO/IEC 25012:2008, ficha oficial](https://www.iso.org/standard/35736.html) y [vista previa](https://www.iso.org/obp/ui/?_escaped_fragment_=iso:std:iso-iec:25012:ed-1:v1:en). Relación conceptual; no se reproducen requisitos no consultados de la norma.
- Anteproyecto y retroalimentación del 21 de junio de 2026 (`documentos/`); exigencia adicional de ocho dimensiones comunicada por el usuario.
- `codigo/codigo_hasta_hito2.py`, Parte 2. No se modificó el motor ni se ejecutaron nuevas métricas de calidad.
