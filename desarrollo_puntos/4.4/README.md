# 4.4 · Regla de alerta sistémica

La lectura principal está en [INFORME_REGLA_SISTEMICA.md](INFORME_REGLA_SISTEMICA.md). Corresponde a la actividad 4 del
Hito 4: clasificar como candidato sistémico (posible cambio regulatorio) el mes en que más de X % de las series alertan,
calibrar X con feb-2020, jul-2020 y jul-2021, y contrastar con las publicaciones de EPM y las resoluciones de la CREG.
Desarrolla lo que [4.2](../4.2/README.md) solo exploró como sensibilidad. No modifica 4.1, 4.2 ni 4.3.

| Archivo | Contenido |
|---|---|
| [regla_sistemica.py](regla_sistemica.py) | La regla (desigualdad estricta, mínimo de 10 series), el protocolo de ventana móvil sin fuga de futuro, la calibración y la carga de EPM con etiquetas canónicas. |
| [calibrar_regla_sistemica.py](calibrar_regla_sistemica.py), [informe_regla_sistemica.py](informe_regla_sistemica.py) | Ejecución completa; figuras e informe generados desde las tablas. |
| [fracciones_mensuales.csv](fracciones_mensuales.csv) | Series evaluadas y con alerta por mes, fuente, ventana y método, con categorías y componentes que alertan. |
| [reproduccion_hito2.csv](reproduccion_hito2.csv) | Reproducción de 51/83, 24/83 y 18/83 desde los archivos del Hito 2. |
| [calibracion_X.csv](calibracion_X.csv), [calibracion_resumen.csv](calibracion_resumen.csv) | Para X de 5 a 80 %: meses del plan capturados, otros meses marcados, banda factible y alertas reclasificadas. |
| [catalogo_alertas_sistemicas.csv](catalogo_alertas_sistemicas.csv) | Catálogo de meses candidatos con su fracción, amplitud, banderas por X y estado del contraste externo. |
| [efecto_regla_sobre_alertas_reales.csv](efecto_regla_sobre_alertas_reales.csv), [costo_enmascaramiento_4_2.csv](costo_enmascaramiento_4_2.csv) | Alertas reales reclasificadas por X; detecciones de errores inyectados que la regla enmascararía (tomado de 4.2). |
| [composicion_alertas_meses_plan.csv](composicion_alertas_meses_plan.csv), [tamano_componentes_epm.csv](tamano_componentes_epm.csv), [inventario_series_por_variante.csv](inventario_series_por_variante.csv) | Componentes que alertan en los meses del plan, cuánto aportaría cada componente a la fracción y cuántas series hay por variante. |
| [contraste_componentes.csv](contraste_componentes.csv) | Cambio publicado por EPM de cada componente (ene→feb y jun→jul de 2020; jun→jul de 2021) frente a las alertas de cada variante. |
| [verificacion_transcripcion_pdf.csv](verificacion_transcripcion_pdf.csv), [verificacion_suma_componentes.csv](verificacion_suma_componentes.csv) | La transcripción de los PDF coincide con el CSV (108 celdas) y la suma de componentes reproduce el CU total. |
| [evidencia_externa/](evidencia_externa/) | Los seis PDF oficiales de EPM leídos (ene, feb, jun y jul de 2020; jun y jul de 2021), su transcripción y el estado de cada referencia documental (CREG 012, 058 y 104 de 2020 leídas; 015 de 2018 leída parcialmente). |
| [test_regla_sistemica.py](test_regla_sistemica.py), [verificar_resultados.py](verificar_resultados.py), [verificacion.json](verificacion.json) | Diez pruebas de propiedades y auditoría con recálculo independiente. |
| [configuracion.json](configuracion.json), [manifiesto_resultados.json](manifiesto_resultados.json) | Parámetros, versiones y huellas de entradas, PDF y salidas. |

El script `informe_regla_sistemica.py` genera cuatro gráficos en `figuras/`, en PNG, SVG y PDF.
La carpeta no se versiona porque son artefactos regenerables; se debe ejecutar el script con las
dependencias registradas en `configuracion.json` para visualizarlos.
X = 25 % es un **valor de trabajo propuesto, no aprobado**: con tres meses no hay un X único. «Candidato sistémico» no equivale a
«cambio regulatorio confirmado»: el contraste con las publicaciones de EPM muestra que son cambios publicados, pero falta confirmar con EPM o la CREG la causa de cada uno.

```powershell
python desarrollo_puntos/4.4/calibrar_regla_sistemica.py
python desarrollo_puntos/4.4/informe_regla_sistemica.py
python -m unittest discover -s desarrollo_puntos/4.4 -p test_regla_sistemica.py -v
python desarrollo_puntos/4.4/verificar_resultados.py
```
