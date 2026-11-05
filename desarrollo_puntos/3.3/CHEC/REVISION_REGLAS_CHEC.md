# CHEC: cierre de controles del Hito 3

Fuente: `fuentes_datos/datos/Datos_seleccionados/CHEC/chec_c698-wqig.csv` (`c698-wqig`,
40.609 filas y 24 columnas).

## Evidencia y resultados

- `EXA01` contrasta 756 celdas contra Superservicios (`td8k-vhq9`) y obtiene 100 % de
  coincidencia en el alcance temporal y categórico disponible.
- `fuentes_datos/catalogos/CHEC/chec_definiciones_def01.yaml` documenta las 24 columnas,
  diferenciando códigos, categorías, componentes y agregados monetarios. El cierre es
  metodológico interno porque faltan algunos catálogos formales de CHEC.
- `MAP01` evalúa 3/3 mapeos código-nombre con aprobación metodológica interna.
- `cartas_log_chec.py` genera `cartas_log_chec.csv` con 276 series y 3.312 cambios
  vigilados; se detectan 37 señales preliminares.
- `OPO01` usa un proxy de cobertura temporal de 225/225 meses. No representa el plazo
  histórico de publicación porque el CSV no contiene fecha de disponibilidad.

## Limitaciones

Las 37 señales deben revisarse contra cambios tarifarios oficiales antes de clasificarlas
como errores. Las unidades y siglas de `tipomed`, `CU real`, `subcon` y `valor_tarifa`
deben interpretarse con el catálogo formal del publicador; mientras no exista, se reportan
como definiciones operativas del proyecto.
