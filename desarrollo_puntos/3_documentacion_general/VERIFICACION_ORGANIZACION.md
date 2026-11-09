# Verificación de la organización

Verificación realizada el 6 de noviembre de 2026. Se ejecutaron los scripts en una
copia temporal aislada con los datos locales; las tablas y los manifiestos del proyecto
se conservaron. No se realizaron descargas ni se aprobaron decisiones metodológicas.

## Comprobaciones

- Los 76 archivos originales están localizados en el inventario, sin eliminaciones.
- Los CSV originales de resultados, los JSON de evidencia y `matriz_oe1.yaml`
  conservan su SHA-256 anterior.
- Los enlaces relativos de los documentos del Hito 3 y los índices principales se
  comprobaron contra los destinos existentes.
- Se verificaron la sintaxis Python y los imports de la matriz y sus adaptadores.
- Las cuatro cartas, la tabla de revisión EPM y el bootstrap se regeneraron en la copia
  temporal y coinciden, registro por registro, con las tablas conservadas.
- La matriz pudo regenerar 76 registros para cuatro fuentes desde 3.1, usando los
  adaptadores de 3.3 y las cartas de 3.5.
- El scorecard consumidor del Hito 4 pudo leer la nueva ruta de la matriz y producir
  32 registros en la copia temporal.
- La trazabilidad pudo leer los insumos históricos de 3.3 y escribir el manifiesto
  para cuatro archivos en 3.6, además de las copias enriquecidas de hallazgos y alertas.
- Se ejecutaron los generadores de cuarentena EPM y de las otras fuentes en la copia.

## Scripts ejecutados en la copia

- `desarrollo_puntos/3.5/EPM/cartas_log_epm.py`
- `desarrollo_puntos/3.5/CHEC/cartas_log_chec.py`
- `desarrollo_puntos/3.5/SSPD/cartas_log_sspd.py`
- `desarrollo_puntos/3.5/XM/cartas_log_xm.py`
- `desarrollo_puntos/3.5/EPM/revision_cartas_epm.py`
- `desarrollo_puntos/3.7/bootstrap_categorias.py`
- `desarrollo_puntos/3.1/medir_matriz_oe1.py`
- `desarrollo_puntos/4.5/generar_scorecard_oe1.py`
- `desarrollo_puntos/3.6/trazabilidad.py`
- `desarrollo_puntos/3.7/EPM/cuarentena.py`
- `desarrollo_puntos/3.7/cuarentena_fuentes.py`

Estas comprobaciones validan las rutas y la ejecución después de organizar. No
certifican la validez estadística de los métodos ni el cierre de los siete puntos.
Los resultados regenerados en la copia no reemplazan los resultados conservados.
