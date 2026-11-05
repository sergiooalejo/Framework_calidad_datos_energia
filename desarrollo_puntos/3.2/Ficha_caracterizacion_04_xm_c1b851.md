# Ficha de caracterización: XM/SIMEM `c1b851`

## Identificación

| Atributo | Descripción |
|---|---|
| Dataset histórico | `c1b851` |
| Portal | https://www.simem.co/ |
| Documentación API | https://github.com/EquipoAnaliticaXM/API_XM |
| Archivo crudo local | `fuentes_datos/datos/Datos_en_revision/XM_piloto/xm_demanda_epmc_epmd_str02_202001_202501.csv` |
| Archivo mensual derivado | `fuentes_datos/datos/Datos_en_revision/XM_piloto/xm_demanda_mensual_piloto.csv` |
| Publicador | XM/SIMEM |
| Tema | Demanda real de energía eléctrica |
| Alcance del piloto | Agente `EPMC`, mercado `EPMD`, sistema `STR02` |
| Período consultado | Enero de 2020 a enero de 2025 |
| Registros crudos | 119.928, incluyendo versiones por hora |
| Serie derivada | 61 observaciones mensuales y 44.592 observaciones horarias únicas |

## Columnas del archivo crudo

| Columna | Interpretación |
|---|---|
| `CodigoVariable` | Código de la variable reportada, como demanda real. |
| `Valor` | Valor de demanda. |
| `MercadoComercializacion` | Mercado de comercialización. |
| `UnidadMedida` | Unidad del valor; en el piloto, kWh. |
| `CodigoSICAgente` | Código del agente del mercado. |
| `SistemaTransmision` | Sistema de transmisión. |
| `Version` | Versión de la información publicada. |
| `FechaHora` | Fecha y hora de la observación horaria. |
| `CodigoDuracion` | Duración del intervalo, por ejemplo `PT1H`. |

## Columnas de la serie mensual derivada

| Columna | Interpretación |
|---|---|
| `periodo` | Mes de agregación. |
| `CodigoSICAgente` | Agente seleccionado. |
| `MercadoComercializacion` | Mercado seleccionado. |
| `SistemaTransmision` | Sistema seleccionado. |
| `Version_seleccionada` | Versión elegida para el mes. |
| `horas` | Registros horarios usados. |
| `horas_unicas` | Horas únicas encontradas. |
| `horas_esperadas` | Horas esperadas para el calendario del mes. |
| `demanda_kwh` | Suma mensual de demanda. |
| `publicacion_declarada` | Fecha de publicación declarada en el calendario de versiones. |

## Regla de construcción de la serie

Para cada mes se seleccionó la versión numérica `TX` más alta disponible, se excluyeron `TXF` y `TXR`, se conservaron horas únicas y se sumaron sus valores. No se sumaron versiones entre sí, no se interpolaron horas faltantes y no se rellenaron valores.

Esta política produjo 61 meses completos y positivos. Exigir únicamente la versión marcada `esMaximaVersion=1` produce 53 meses y no alcanza la continuidad requerida; por eso la política debe quedar aprobada y congelada antes de comparar técnicas.

## Utilidad para el plan de hitos

- Proporciona una variable operacional diferente de tarifas y facturación: demanda eléctrica.
- Permite probar agregación horaria-mensual, trazabilidad de versiones y continuidad temporal.
- Tiene longitud suficiente para el escenario de 48 cambios de referencia y 12 meses de vigilancia.
- Permite aplicar cartas, Isolation Forest, Z-score robusto y comparar métodos en Hito 4.
- Es útil para validar la reproducibilidad del framework sobre un dominio energético distinto.

## Limitaciones y adaptación de reglas

- Es un piloto filtrado, no el mercado completo.
- La serie mensual depende de una política de selección de versiones; no debe presentarse como “última versión oficial” sin una justificación adicional.
- R08 y R09, diseñadas para propiedad y modalidad tarifaria, deben reemplazarse por controles equivalentes de demanda.
- Exactitud requiere una referencia horaria o mensual equivalente.
- Oportunidad requiere vincular todas las observaciones con una fecha de disponibilidad y un plazo esperado; junio de 2021 aún carece de ese vínculo.

## Dimensiones DAMA-DMBOK2

La fuente permite trabajar completitud, validez, unicidad, consistencia, integridad y razonabilidad. Exactitud y oportunidad siguen pendientes de evidencia externa. La matriz debe conservar el método de versión, el filtro y el hash como parte de la trazabilidad.

La fuente es publicada por XM y no por CREG. CREG se utiliza como referencia regulatoria, no como atribución del dataset.
