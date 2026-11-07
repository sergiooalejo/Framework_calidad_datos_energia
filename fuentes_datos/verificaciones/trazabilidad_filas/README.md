# Trazabilidad estable del Hito 3

La ejecución de `python3 desarrollo_puntos/3.6/trazabilidad.py` produce:

- Un archivo de correspondencia por dataset con posición física, `clave_contenido` e
  `id_fila_estable`.
- SHA-256, tamaño, filas, columnas y fecha de ejecución en
  `desarrollo_puntos/3.6/trazabilidad/manifiesto_ejecucion.json`.
- Copias enriquecidas de los hallazgos y alertas históricas del Hito 2 con
  `clave_contenido`, sin modificar los archivos originales.

La `clave_contenido` se calcula sobre todas las columnas de la fila, serializadas como
JSON UTF-8 canónico y ordenadas por nombre. Por tanto, no cambia si el portal devuelve
las mismas filas en otro orden. En copias exactas, `id_fila_estable` añade la ocurrencia
ordenada para distinguir instancias sin confundirlas con filas diferentes.

La posición de fila se conserva solo como referencia de lectura; no es la identidad del
registro.

## Cuarentena por fuente

`desarrollo_puntos/3.7/cuarentena_fuentes.py` genera los archivos `*_cuarentena.csv`
para CHEC, SSPD y XM. Actualmente tienen cero filas: no se encontraron valores no
numéricos o negativos en medidas que el catálogo permita declarar estrictamente no
negativas. Los negativos de CHEC se conservan porque pueden corresponder a restricciones,
subsidios o ajustes; no se clasifican como error sin semántica aprobada. La cuarentena de
EPM sí contiene registros y se integra a sus cartas mediante
`desarrollo_puntos/3.7/EPM/cuarentena.py`.
