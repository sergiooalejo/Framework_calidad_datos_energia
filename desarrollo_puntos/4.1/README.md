# Hito 4.1 · Viñeta 1 · Z-score robusto

Este componente implementa una línea base robusta para detectar cambios atípicos
en las series del proyecto. Se aplica sobre cambios logarítmicos y conserva el
mismo protocolo de las cartas del Hito 3:

1. primeros 36 cambios mensuales consecutivos para referencia;
2. siguientes 12 cambios para vigilancia;
3. mediana y MAD calculados solo con referencia;
4. señal cuando `|z_robusto| > umbral`.

La fórmula es `0.6744897501960817 × (cambio_log − mediana) / MAD`.
El umbral predeterminado es `3.267`; también están disponibles `2.66` y `3.0`
para sensibilidad.

## Ejecución

Desde la raíz del repositorio:

```bash
python desarrollo_puntos/4.1/zscore_robusto.py
python desarrollo_puntos/4.1/zscore_robusto.py --umbral 2.66
python desarrollo_puntos/4.1/zscore_robusto.py --umbral 3.0
```

Procesa EPM, CHEC, SSPD y XM. Solo calcula cambios entre meses consecutivos;
los huecos temporales no se cruzan. En EPM aplica `3.7/EPM/cuarentena_registros.csv`
sin modificar la fuente ni imputar valores.

## Salidas

- `zscore_robusto_detalle.csv`: cada cambio vigilado y su Z-score robusto.
- `zscore_robusto_resumen.csv`: resultados por serie y medida.
- `configuracion.json`: protocolo, umbral y SHA-256 de las entradas.

Si el MAD es cero, se registra `mad_cero`, no se inventa una escala y se marca
señal solo cuando el cambio difiere de la mediana. Una señal estadística no
prueba por sí sola un error de datos.
