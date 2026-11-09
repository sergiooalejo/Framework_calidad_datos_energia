# Hito 4.5 · Scorecard por dimensión

Este punto resume la matriz OE1 por fuente y dimensión, como solicita DAMA-DMBOK para reportar
calidad de datos.

## Ejecución

Desde la raíz del repositorio:

```bash
python3 desarrollo_puntos/4.5/generar_scorecard_oe1.py
```

El script lee `desarrollo_puntos/3.1/matriz_oe1.csv` y genera
`scorecard_oe1_provisional.csv` en esta carpeta.

## Contenido

El scorecard contiene 32 filas: cuatro fuentes por ocho dimensiones. Para cada combinación reporta
controles totales, medidos, provisionales, no medibles, no aplicables y promedio de indicadores.

El estado permanece `provisional` hasta que se aprueben los umbrales, catálogos, evidencia de
exactitud y oportunidad. No debe interpretarse como una calificación final.
