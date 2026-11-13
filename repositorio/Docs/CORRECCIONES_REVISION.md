# Correcciones posteriores a la revisión

## Semillas y reproducibilidad

La interfaz ya no ofrece una semilla configurable. El manifiesto registra las semillas base que
realmente fijan los scripts: Bootstrap `20261105`, Isolation Forest y sensibilidad `20261106`,
métricas `20261107` y selección de muestra Hito 6 `42`. Calibración usa la semilla base de
Isolation Forest y deriva valores por partición; sensibilidad y métricas también derivan semillas
por fuente o serie. Las etapas sin aleatoriedad declarada registran un objeto vacío.

La CLI rechaza expresamente `--semilla` para evitar registrar un valor que no controla el cálculo.
Los manifiestos históricos con `semilla: 42` se preservan, pero ese campo representa lo declarado
por la interfaz antigua, no prueba de la semilla ejecutada. Debe contrastarse con la configuración
de cada método.

## Scorecard

El resumen conserva las 32 combinaciones de fuente y dimensión y los conteos por estado, pero su
columna `promedio_indicadores` queda vacía. No se promedia una tasa de incumplimiento con otra de
cumplimiento sin acordar dirección, población y ponderaciones. El tablero presenta los controles
individuales y no un promedio global. Aprobar una posible agregación sigue pendiente con el profesor.
El conteo del tablero para X=25 % ahora respeta el filtro de fuente y se identifica como filas de
escenarios, no como número de eventos únicos; un mismo período puede aparecer varias veces.

La versión anterior se conserva en `Docs/evidencia_historica/scorecard_antes_correccion_20261113.csv`
con SHA-256 `725f030909fa67bb117d114f38d38f403d14ecc4c6ff2ee0fae3f2d74cd5a56c`. Es histórica:
sus promedios no deben interpretarse como porcentaje global de calidad.

## Muestra y caso 43.577

La muestra previa permanece intacta. Si se genera otra con `pipeline.py ejecutar muestra-h6`, el
archivo nuevo recibe un nombre con fecha y no sobrescribe la revisión anterior. La entrada no
incluye LOF, por lo que las nuevas muestras no muestran esa columna. La muestra existente tiene 50
filas y 47 combinaciones distintas de fuente, serie y período; tres observaciones aparecen en
escenarios diferentes. El plan solicita 50 alertas EPM, por lo que el diseño definitivo sigue
pendiente de aprobación y no se presenta precisión empírica como resultado cerrado.

Se corrigió la nota del valor `43577`: verlo con formato monetario en Excel no confirma ni descarta
una conversión previa de fecha. El caso permanece no concluyente y requiere contraste adicional.

## Entorno del tablero

`Environment/requirements-streamlit.txt` incluye las bibliotecas científicas principales usadas por
los botones. Los entornos anteriores deben actualizarse. Poetry y su lock son la opción para fijar
también las dependencias indirectas. La imagen Docker debe reconstruirse después de estos cambios.
