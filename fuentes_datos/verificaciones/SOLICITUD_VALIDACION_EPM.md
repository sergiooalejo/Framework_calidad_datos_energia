# Solicitud de validación semántica EPM

Este documento registra las confirmaciones que faltan para cerrar completamente
`MAP01`, `DEF01` y `OPO01` sin inferir significados a partir de nombres.

1. ¿`No Residencial` y `No residencial` representan exactamente la misma categoría?
2. ¿`0-CS` equivale a `Rango 0 - CS` y `Mayor CS` equivale a `Rango > CS`?
3. ¿Qué unidad tiene cada importe (`propiedadepm`, `compartido`,
   `propiedaddelcliente`, `punta` y `fueradepunta`) según `tipodedato` y `nivel`?
4. ¿Qué significa `N/A` en `rangodeconsumo` y cuándo es aplicable cada franja?
5. ¿Cuál era la fecha límite y cuál fue la fecha real de publicación de cada tarifa
   mensual de diciembre de 2016 a diciembre de 2021?

Hasta recibir esta confirmación, la matriz debe conservar los estados `provisional`
o `no_medible`; no deben convertirse en 100 % por similitud textual.
