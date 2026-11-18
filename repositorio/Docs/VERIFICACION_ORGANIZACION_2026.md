# Verificación de la organización — 17 de noviembre de 2026

## Cambios

Paquete y CLI trasladados a `src/framework_calidad/`, tablero a `apps/`, pruebas de integración
a `tests/` y notebook a `notebooks/`. Registro de tareas y semillas en `configs/pipeline.toml`.
Los accesos anteriores siguen disponibles como delegaciones. Metadatos estándar del paquete,
CLI instalable, guías, registro de traslados y workflow de CI agregados.

## Comprobaciones locales

- Las 74 pruebas científicas y de compatibilidad anteriores pasan con la nueva estructura.
- Tres regresiones adicionales comprueban la CLI nueva, la raíz explícita y la configuración efectiva.
- Resultado final con pytest: **77 pruebas aprobadas**. Se ajustó la salida UTF-8 de la CLI
  para que los mensajes capturados sean compatibles entre Windows y Linux.
- Estructura, sintaxis e integridad de las 16 entradas del mapa histórico verificadas.
- Auditoría H3: 742 series, 26 modelos IF y tres pares de descargas.
- Auditoría H4: 102 folds, 1836 umbrales, 22511 observaciones reales,
  117857 casos inyectados y 1584 filas de métricas.
- `poetry check --lock` correcto, con el lock original sin modificaciones.
- Wheel construido y probado desde una instalación temporal fuera del árbol fuente:
  API, módulo CLI y comando `framework-energia`.
- Streamlit AppTest carga el tablero y el filtro EPM desde `apps/streamlit_app.py`,
  `app_streamlit.py` y `Code/hito5/app_streamlit.py` sin excepciones.
- Datos, resultados existentes, protocolos H3/H4 y lock mantienen sus bytes originales.

Las comprobaciones de ejecución se prepararon en una copia temporal completa para conservar
la evidencia entregada. El motor Docker no estaba disponible: no se construyó ni ejecutó
el contenedor localmente. La construcción y verificación están incluidas en CI.
El workflow remoto todavía debe ejecutarse en GitHub; no se recalcularon los experimentos completos.
La validación externa y la aprobación académica siguen pendientes.

## Limpieza posterior

Se retiraron las tres guías H5 reemplazadas por `Docs/guias/`, la copia del README anterior,
las muestras pequeñas de formato, cuatro README redundantes y tres accesos antiguos de pruebas.
Las pruebas originales siguen en `tests/` y los comandos habituales permanecen disponibles.
También se eliminaron cachés locales fuera de los entornos virtuales.
Por petición del usuario no se ejecutaron nuevamente pruebas ni experimentos.
