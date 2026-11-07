# 4.2 · Análisis de sensibilidad

La lectura principal está en [INFORME_SENSIBILIDAD.md](INFORME_SENSIBILIDAD.md).
El análisis se ejecutó sobre las cuatro fuentes locales y escribe todas sus salidas aquí.

| Archivo | Contenido |
|---|---|
| [cobertura_ventanas.csv](cobertura_ventanas.csv) | Elegibilidad y configuraciones no evaluables. |
| [tasas_alerta_reales.csv](tasas_alerta_reales.csv) | Alertas e IC descriptivos por ventana, cohorte y método. |
| [comparacion_ventanas_pareada.csv](comparacion_ventanas_pareada.csv) | Diferencias 24/48 frente a 36 sobre las mismas series y meses. |
| [parametros_por_serie.csv](parametros_por_serie.csv) | Períodos de referencia/vigilancia, límites, MAD y mediana para R12. |
| [deteccion_inyecciones.csv](deteccion_inyecciones.csv) | Detección t/t+1, ganancia e IC por tipo; señales nuevas respecto a base. |
| [resumen_horizonte_36.csv](resumen_horizonte_36.csv) | Resumen de horizonte por fuente/método con referencia 36. |
| [inyecciones_omitidas.csv](inyecciones_omitidas.csv) | Casos sin perturbación efectiva o sin otra medida comparable. |
| [combinaciones_framework.csv](combinaciones_framework.csv) | Interacción de cartas, percentil IF y factor R12. |
| [alertas_sistemicas_por_mes.csv](alertas_sistemicas_por_mes.csv) | Catálogo mensual de candidatos para cada X, sin confirmar origen regulatorio. |
| [efecto_regla_sistemica_reales.csv](efecto_regla_sistemica_reales.csv) | Tasa original y tasa retenida por X. |
| [efecto_regla_sistemica_inyecciones.csv](efecto_regla_sistemica_inyecciones.csv) | Detecciones retenidas/enmascaradas en errores individuales y colectivos. |
| [inventario_series.csv](inventario_series.csv) | Rachas y elegibilidad de todas las series candidatas. |
| [ejecuciones.csv](ejecuciones.csv) | Escenarios, modelos, tamaños, umbrales y tiempos. |
| [modelos_IF.csv](modelos_IF.csv) | Modelos separados por calendario, fechas de corte y percentiles de referencia. |
| [alertas_reales_detalle.csv.gz](alertas_reales_detalle.csv.gz) | Una fila por escenario/serie/mes, con las once banderas de señal. |
| [inyecciones_detalle.csv.gz](inyecciones_detalle.csv.gz) | Casos auditables y banderas por método en t, t+1 y nuevas respecto a base. |
| [configuracion.json](configuracion.json) | Protocolo, versiones y huellas de entradas. |
| [manifiesto_resultados.json](manifiesto_resultados.json) | Huellas de los archivos entregados. |
| [analisis_sensibilidad.py](analisis_sensibilidad.py), [informe_sensibilidad.py](informe_sensibilidad.py) | Ejecución y generación de informe/figuras. |
| [test_sensibilidad.py](test_sensibilidad.py) | Pruebas de continuidad, ausencia de fuga temporal, límites y bootstrap. |
| [verificar_resultados.py](verificar_resultados.py), [verificacion.json](verificacion.json) | Reconciliación del detalle, denominadores, hashes y pruebas automáticas. |

En [figuras](figuras/) están nueve gráficos en PNG, SVG y PDF.
SSPD con referencia 48 es no evaluable; XM no recibe IC entre categorías.
Los resultados describen sensibilidad, sin aprobar umbrales ni clasificar automáticamente
una señal estadística como error o cambio regulatorio.

```powershell
python desarrollo_puntos/4.2/analisis_sensibilidad.py
```
