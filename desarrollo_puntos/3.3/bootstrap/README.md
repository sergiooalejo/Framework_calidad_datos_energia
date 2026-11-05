# Bootstrap por categoría

El archivo `bootstrap_categorias.csv` calcula la tasa de señales de CART01 y su IC95 % por categoría. Se remuestrean series dentro de cada categoría, sin mezclar fuentes. La semilla es 20261105 y se ejecutan 2000 repeticiones.

La tasa es descriptiva: una señal no equivale automáticamente a un error de datos. Categorías con una sola serie tienen un intervalo degenerado y deben interpretarse con cautela.

La ejecución actual produce 105 categorías: EPM (8), CHEC (4), SSPD (92) y XM (1).
La unidad estadística es la serie de cartas, no cada fila del CSV; por eso no se mezclan observaciones de fuentes, años o categorías distintas. SSPD tiene una categoría de una sola serie y XM también; sus intervalos son necesariamente degenerados.

## Reproducir

Desde la raíz del repositorio:

```bash
python3 desarrollo_puntos/3.3/bootstrap_categorias.py
```

El script lee las cartas generadas en las carpetas de cada fuente y reemplaza de forma determinista `bootstrap_categorias.csv`, `configuracion.json` y este resumen. La semilla fija permite comparar ejecuciones mientras no cambien las cartas de entrada.
