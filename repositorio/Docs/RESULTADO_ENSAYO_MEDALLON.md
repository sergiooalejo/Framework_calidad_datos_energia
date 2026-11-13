# Resultado del ensayo de arquitectura medallón

**Fecha:** 13 de noviembre de 2026. Este documento conserva el resultado histórico del ensayo en
una copia temporal. Para conocer la organización actual consulte [la guía medallón](../Data/MEDALLION.md).

## Qué se probó

En una copia local se ubicaron los datos históricos en `Data/bronze/datos`, los catálogos y
verificaciones en `Data/silver`, los agregados mensuales seleccionados de SSPD y XM en Silver y
las salidas en `Data/gold/outputs`. Se adaptaron rutas de código y se hicieron pruebas de
compatibilidad con las huellas históricas, conservando una copia de los scripts y de la cuarentena
que participaron en los experimentos anteriores.

Esta clasificación es preliminar: se debe revisar la procedencia de los ZIP y fuentes en revisión,
además de separar los adaptadores que quedaron dentro de `outputs` aunque sean insumos Silver.

## Resultados

| Comprobación | Resultado en el ensayo |
|---|---|
| Validación estructural y SHA-256 | Correcta: 305 archivos mapeados, 16 entradas verificadas. |
| Pruebas automáticas | Correctas: 9 de sensibilidad, 12 de métricas y 10 de regla sistémica. |
| Auditorías históricas | Correctas con resolución de rutas antiguas y copias históricas de código y cuarentena. |
| Línea base | Ejecutada: trazabilidad, cuarentena, cartas, matriz, bootstrap, scorecard y niveles/costos. |
| Cartas de cuatro fuentes | Contenido CSV igual al original; los bytes difieren por formato de fin de línea. |
| Matriz OE1 | 76 filas; únicamente cambió la columna de fecha de medición. |
| Streamlit | Prueba automatizada de renderizado sin excepciones ni advertencias del tablero. |
| Docker | Imagen de ensayo construida; validación y renderizado automatizado del tablero correctos dentro del contenedor. |

## Hallazgos y pendientes antes de aplicar la migración

- La primera validación no comprobó los dos agregados movidos a Silver. Se corrigió en la copia
  y volvió a verificar las 16 entradas.
- El lector de datos buscaba solamente en Bronze y no encontraba el agregado SSPD. Se corrigió
  en la copia para buscar en ambas capas.
- Ejecutar la línea base regeneró la cuarentena con distinta huella. Para auditar resultados
  históricos se utilizó la copia histórica, sin cambiar el hash registrado de la ejecución anterior.
- Docker necesitó incorporar `Environment`, `Docs` y `project.json` además de `Data`.
- No se verificaron todas las etapas individuales, las acciones de los botones ni un segundo
  computador. La prueba de Streamlit no sustituye una revisión visual completa en el navegador.
- La copia y sus rutas son temporales. Debe prepararse una implementación versionada, con
  documentación y pruebas de rutas históricas, antes de mover los archivos del proyecto principal.

La imagen Docker local de ensayo se llama `ensayo-medallon-energia:local`.
