# 4.3 · Métricas completas y honestas

La lectura principal está en [INFORME_METRICAS.md](INFORME_METRICAS.md). Corresponde a la actividad 3 del Hito 4:
precisión, recall y F1 a tasa de alerta igualada, curvas de detección contra tasa de alerta por método, pruebas por tipo
y meses distintos sorteados sin reemplazo. Reutiliza las inyecciones y los modelos de [4.2](../4.2/README.md) y completa
lo que [4.1](../4.1/README.md) dejó pendiente (métricas del Z-score robusto y del Isolation Forest, LOF y KNN).
No modifica 4.1 ni 4.2; solo escribe en esta carpeta.

| Archivo | Contenido |
|---|---|
| [metricas_globales.csv](metricas_globales.csv) | Recall macro, tasa de alerta real, precisión y F1 con IC 95 % por fuente, método, tasa igualada (1, 2, 5 y 10 %), horizonte (t y t o t+1) y prevalencia supuesta (1, 5 y 10 %). |
| [deteccion_por_tipo_tasa_igualada.csv](deteccion_por_tipo_tasa_igualada.csv) | Recall por tipo de error con casos, series, categorías e IC: la tabla comparativa por técnica y tipo de error. |
| [diferencias_vs_IMR.csv](diferencias_vs_IMR.csv) | Diferencias pareadas de recall y F1 frente a la carta I-MR, con IC por categorías. |
| [curva_deteccion.csv](curva_deteccion.csv) | Recall macro frente a tasa de alerta en 40 tasas (0,25–30 %). |
| [umbrales_tasa_igualada.csv](umbrales_tasa_igualada.csv) | Umbral de cada método y tasa objetivo, alertas reales y tasa observada. |
| [puntos_operativos_nativos.csv](puntos_operativos_nativos.csv) | Cada método con su umbral propio (I-MR > 1, \|z\| > 3, IF p99,5, R12 > 10), para contrastar con la tasa igualada. |
| [pruebas_por_tipo.csv](pruebas_por_tipo.csv), [sorteo_sin_reemplazo.csv](sorteo_sin_reemplazo.csv) | Denominadores reales por tipo y sorteo con meses distintos, frente al cálculo exhaustivo. |
| [cobertura_experimento.csv](cobertura_experimento.csv), [inyecciones_omitidas.csv](inyecciones_omitidas.csv) | Series, categorías, observaciones, duplicados de entrenamiento, estado de LOF y casos omitidos. |
| [puntajes_reales.csv.gz](puntajes_reales.csv.gz), [puntajes_inyecciones.csv.gz](puntajes_inyecciones.csv.gz) | Puntajes continuos de los seis métodos (observaciones reales y casos inyectados): permiten rehacer umbrales y métricas sin reentrenar. |
| [ejecuciones.csv](ejecuciones.csv) | Tiempos por etapa y fuente. |
| [metricas_base.py](metricas_base.py) | Funciones puras: puntajes, umbral por tasa, precisión, F1 y sorteo sin reemplazo. |
| [experimento_tasa_igualada.py](experimento_tasa_igualada.py), [informe_metricas.py](informe_metricas.py) | Ejecución del experimento; generación de figuras e informe desde las tablas. |
| [test_metricas.py](test_metricas.py) | Doce pruebas de propiedades. |
| [verificar_resultados.py](verificar_resultados.py), [verificacion.json](verificacion.json), [verificacion_contra_4_2.json](verificacion_contra_4_2.json) | Recalcula umbrales, detecciones, FPR, precisión y F1 desde los puntajes; compara las banderas nativas con las de 4.2. |
| [configuracion.json](configuracion.json), [manifiesto_resultados.json](manifiesto_resultados.json) | Protocolo, semilla, versiones y huellas de entradas y salidas. |

En [figuras](figuras/) hay tres gráficos en PNG, SVG y PDF.
XM tiene una sola serie y 12 observaciones: se reporta como descriptivo y no es interpretable a tasa igualada.
LOF queda marcado como degenerado en CHEC (entrenamiento con muchos duplicados exactos).
La fuente `EPM_canonicas` es una variante de sensibilidad con las equivalencias de etiquetas del Hito 2 (11 equivalencias aprobadas internamente): no sustituye a EPM y no existe en 4.2.
Los resultados no aprueban umbrales ni clasifican una señal real como error.

```powershell
python desarrollo_puntos/4.3/experimento_tasa_igualada.py
python desarrollo_puntos/4.3/informe_metricas.py
python -m unittest discover -s desarrollo_puntos/4.3 -p test_metricas.py -v
python desarrollo_puntos/4.3/verificar_resultados.py
```
