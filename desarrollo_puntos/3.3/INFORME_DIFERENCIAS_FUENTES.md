# Informe de diferencias entre fuentes — Hito 3

## Alcance

Este informe compara la aplicación de la matriz OE1 y de las cartas de control a las cuatro
fuentes seleccionadas: EPM (`sfcd-b3ey`), CHEC (`c698-wqig`), Superservicios (`ebby-cjha`) y
XM/SIMEM (`c1b851`). La comparación se basa en `matriz_oe1.csv`, las fichas de caracterización,
las cartas logarítmicas y el bootstrap por categoría. No mezcla registros ni resultados entre
fuentes.

## Diferencias estructurales

| Fuente | Naturaleza del dato | Unidad de carta | Tratamiento específico |
|---|---|---|---|
| EPM | Tarifas históricas de energía eléctrica | Serie mensual por combinación tarifaria | Se excluyen de los límites los cambios que tocan registros en cuarentena; no se imputan valores. |
| CHEC | Costos unitarios y tarifas por categoría | Serie mensual por combinación de categoría y nivel | La clave y los catálogos requieren confirmación documental; los negativos no se eliminan automáticamente porque pueden representar restricciones o ajustes. |
| SSPD | Información comercial residencial/no residencial | Serie mensual por combinación de identificadores y concepto | Se aplican reglas transversales; los controles que requieren propiedad o catálogo externo pueden quedar como no aplicables. |
| XM/SIMEM | Demanda eléctrica horaria agregada | Serie horaria de demanda (`demanda_kwh`) | Adaptación explícita de reglas originalmente tarifarias; el resultado es piloto y no se interpreta como tarifa. |

## Comparación de la matriz OE1

La matriz contiene 19 controles para cada fuente (76 filas). Las ocho dimensiones DAMA-DMBOK
están representadas en cada ficha y no se elimina una dimensión porque la fuente tenga un
esquema diferente. Cuando el concepto no existe se registra `no_aplica`; cuando faltan datos
para calcularlo se registra `no_medible`.

| Fuente | Medido | Provisional | Provisional interno | Proxy | No medible | No aplica |
|---|---:|---:|---:|---:|---:|---:|
| EPM | 6 | 9 | 2 | 1 | 0 | 1 |
| CHEC | 5 | 11 | 2 | 1 | 0 | 0 |
| SSPD | 6 | 6 | 2 | 1 | 1 | 3 |
| XM | 7 | 6 | 3 | 1 | 1 | 1 |

Los estados no son calificaciones finales de calidad. `Provisional` indica que falta cerrar una
decisión metodológica o documental; `provisional_proxy` indica que se usó una medida indirecta;
`no_medible` indica ausencia de evidencia; y `no_aplica` indica que el concepto no existe en el
esquema de esa fuente.

## Cartas y bootstrap

Las cartas usan cambios logarítmicos y se ejecutan solo donde existe una serie temporal suficiente.
SSPD tiene series mensuales aptas para el análisis disponible; XM usa una adaptación de demanda.
El archivo `bootstrap/bootstrap_categorias.csv` calcula intervalos del 95 % para la tasa de señales
de CART01 remuestreando series dentro de cada categoría. La ejecución tiene 105 categorías:
EPM (8), CHEC (4), SSPD (92) y XM (1). XM y una categoría de SSPD tienen una sola serie, por lo
que sus intervalos son degenerados.

## Diferencias que deben conservarse en la interpretación

1. Una misma regla puede tener distinto denominador por la estructura y cobertura de cada fuente.
2. Un porcentaje mayor no implica automáticamente mejor calidad si se obtuvo con menor población,
   un proxy o un catálogo no aprobado.
3. Las alertas de cartas identifican señales de comportamiento atípico; no sustituyen un contraste
   documental de exactitud.
4. La oportunidad no queda demostrada por la fecha de descarga. Requiere fecha de publicación,
   frecuencia comprometida y evidencia de disponibilidad.
5. La ausencia de una dimensión en el esquema se informa como `no_aplica`, no como cero ni como
   cumplimiento total.

## Conclusión

Las cuatro fuentes son comparables a nivel metodológico porque pasan por la misma matriz, pero no
son intercambiables a nivel semántico. EPM y CHEC permiten concentrar el análisis tarifario;
SSPD aporta información comercial y consumo; XM aporta una fuente operativa de demanda. Esta
distinción debe mantenerse en el Hito 4 al construir scorecards y comparar técnicas.
