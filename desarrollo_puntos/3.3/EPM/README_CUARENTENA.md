# Cuarentena EPM

`cuarentena_registros.csv` contiene las filas apartadas antes de calcular las cartas.
Se construye con `cuarentena.py` a partir de los hallazgos trazables del Hito 2:

- R08: incoherencia entre propiedades.
- R11: posible serial de fecha en un importe.
- R12: magnitud extrema frente a la mediana de la serie.
- R07 con severidad Error: signo fuera del dominio documentado.

La cuarentena no elimina ni corrige valores. `cartas_log_epm.py` excluye cualquier cambio
mensual que toque una fila cuyo `clave_contenido` esté en este archivo. No se interpolan
meses ni se ajustan los límites usando valores de vigilancia.
