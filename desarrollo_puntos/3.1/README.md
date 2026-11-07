# 3.1 · Matriz dimensión → métrica → indicador → regla (OE1)

Corresponde a la actividad 1 del Hito 3. Aquí se reúnen las definiciones de los
indicadores, sus resultados y las evidencias que sustentan cada medición.

| Archivo o grupo | Función |
|---|---|
| [matriz_oe1.md](matriz_oe1.md) | Definiciones, ocho dimensiones, diez tipos de regla y fichas de indicadores. |
| [matriz_oe1.csv](matriz_oe1.csv) | Matriz principal: 76 registros, 19 controles por cada una de cuatro fuentes. |
| [matriz_oe1.yaml](matriz_oe1.yaml) | Especificación documental y resultados por control y fuente. |
| [medir_matriz_oe1.py](medir_matriz_oe1.py) | Calcula la matriz; utiliza los adaptadores de [3.3](../3.3/README.md) y las cartas de [3.5](../3.5/README.md). |
| [EVIDENCIA_EXACTITUD_OPORTUNIDAD.md](EVIDENCIA_EXACTITUD_OPORTUNIDAD.md) | Procedimiento y limitaciones de EXA01 y OPO01. |
| [referencia_exa01_chec.json](referencia_exa01_chec.json) | Referencia externa conservada para el contraste de exactitud CHEC. |
| [plantilla_exactitud.csv](plantilla_exactitud.csv), [plantilla_oportunidad.csv](plantilla_oportunidad.csv), [plantilla_catalogos.csv](plantilla_catalogos.csv) | Plantillas sin diligenciar para evidencia y validación de indicadores. |
| `matriz_dimensiones_dataset_*.py`, `indicadores_calidad_*_por_columna.csv`, `incidencias_calidad_*.csv`, `resumen_calidad_*.json` | Evaluación auxiliar por columna de EPM y CHEC; se conserva junto a los scripts que la generan. |

La evaluación auxiliar por columna y la matriz principal tienen definiciones y unidades
distintas. No deben mezclarse sus resultados ni asumirse como dos versiones equivalentes.
Por ejemplo, los indicadores auxiliares emplean proxies y tratan marcadores de ausencia
según su propia lógica; la matriz declara la aplicabilidad y el estado por control.

Desde la raíz del proyecto:

```powershell
python desarrollo_puntos/3.1/medir_matriz_oe1.py
```

La reorganización conserva los resultados existentes. No aprueba umbrales, cambia
fórmulas ni resuelve las diferencias metodológicas del plan; los pendientes siguen en
[el documento general](../3_documentacion_general/PENDIENTES_APROBACION_HITO3.md).
