# EPM: cierre de controles del Hito 3

Fuente: `fuentes_datos/datos/Datos_seleccionados/EPM/epm_sfcd-b3ey.csv` (`sfcd-b3ey`, 3.623 filas).
La medición se ejecuta con `python3 desarrollo_puntos/3.1/medir_matriz_oe1.py`.

Los archivos de cartas y revisión de señales citados abajo están en
[3.5/EPM](../../3.5/README.md); los de cuarentena, en
[3.7/EPM](../../3.7/EPM/README_CUARENTENA.md).

## Evidencia incorporada

- `fuentes_datos/verificaciones/EPM/epm_exactitud_referencias.json` conserva seis
  comparaciones reproducibles (enero/diciembre de 2020, abril/diciembre de 2021) contra
  los PDF oficiales de EPM. Se contrastan `propiedadepm`, `compartido` y
  `propiedaddelcliente` en nivel I.
- `cartas_log_epm.py` genera `cartas_log_epm.csv`: 60 series con al menos 49 períodos,
  36 cambios de referencia y 12 de vigilancia. No se imputan meses ni se mezclan valores
  no positivos. El resultado es una línea base preliminar para CART01.
- `revision_cartas_epm.py` genera `revision_senales_cartas_epm.csv` con las 50 señales
  individuales, sus períodos, valores anterior/actual y límites. La columna
  `clasificacion` queda como `pendiente_revision` hasta contrastar cada señal con su
  publicación mensual; no se convierten automáticamente en errores.
- `cuarentena.py` genera `cuarentena_registros.csv` con 9 filas derivadas de R08, R11,
  R12 y R07-error. `cartas_log_epm.py` las excluye por `clave_contenido`, sin modificar
  el CSV fuente ni interpolar valores.
- Los metadatos oficiales locales se usan para DEF01. La cobertura es parcial: describen
  7 de 12 columnas, pero no fijan la unidad y semántica completa de todos los importes.
- `fuentes_datos/catalogos/EPM/epm_etiquetas.yaml` documenta las equivalencias aprobadas
  metodológicamente por el equipo del proyecto. Esta aprobación es interna y no sustituye
  una confirmación de EPM; el CSV original no se modifica.
- `fuentes_datos/catalogos/EPM/epm_definiciones_def01.yaml` documenta las 12 columnas con
  significado, unidad, aplicación y evidencia. Las unidades de las medidas son
  condicionales al `tipodedato` y no se tratan como una unidad única.

## Estado interpretado

| Control | Estado | Interpretación |
|---|---|---|
| EXA01 | provisional | La muestra coincide con la publicación oficial; falta ampliar a todos los meses y categorías. |
| MAP01 | provisional_interno | Las variantes se normalizan con una decisión metodológica del proyecto; no se presenta como aprobación oficial de EPM. |
| DEF01 | provisional_interno | Las 12 columnas tienen definición operativa documentada; las unidades condicionadas y la aprobación son metodológicas del proyecto. |
| CART01 | provisional | Ya existe carta I-MR preliminar en cambios logarítmicos; falta sensibilidad y revisión de dominio. |
| INT02 | no aplica | No existen pares código-nombre en el esquema EPM. |
| OPO01 | provisional_proxy | Se comparan los períodos presentes frente a los esperados (61/61); esto evalúa cobertura temporal, no el plazo histórico real de publicación. |

Por tanto, EPM ya no queda con controles técnicos sin ejecutar: las brechas restantes
son de evidencia o aprobación externa y están separadas de los resultados medidos. El
proxy de OPO01 se presenta explícitamente como una aproximación, no como puntualidad.
