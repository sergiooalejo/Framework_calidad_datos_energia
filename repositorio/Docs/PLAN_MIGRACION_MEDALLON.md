# Plan histórico de migración física a arquitectura medallón

**Estado histórico:** este plan se escribió antes de trasladar los archivos. Consulte el estado
actual y las rutas en [la guía medallón](../Data/MEDALLION.md).

## Clasificación inicial

| Archivo o grupo | Capa propuesta | Consideración |
|---|---|---|
| EPM y CHEC seleccionados | Bronze | Conservar la copia descargada y sus huellas. |
| XM demanda horaria piloto | Bronze | Preservar la extracción original del piloto. |
| SSPD mensual y XM demanda mensual | Silver | Son agregados derivados; conservar la transformación y sus entradas. |
| Catálogos, diccionarios y trazabilidad | Apoyo a Silver | Mantener también su procedencia y estado de aprobación. |
| Cartas, indicadores, métricas y scorecards | Gold | Resultados de análisis; conservar parámetros y versión. |

Los ZIP, las fuentes en revisión y el calendario de versiones XM requieren clasificación por
procedencia y contenido antes de moverlos. Una extracción o subconjunto no debe describirse como
una descarga completa sin comprobarlo.

## Dependencias que deben adaptarse

1. Rutas codificadas en `Code/`, `pipeline.py`, `app_streamlit.py` y sus pruebas.
2. Configuraciones y verificadores de sensibilidad, métricas y regla sistémica, que guardan rutas
   históricas y SHA-256 de datos, resultados y scripts. Las huellas históricas no deben actualizarse
   silenciosamente como si se hubieran producido con una nueva versión del código.
3. Manifiesto `Docs/MIGRACION.csv`, documentación, enlaces y configuración de Docker y Git.
4. Ejecución de matriz, cartas y demás etapas; validación, pruebas y auditorías; arranque de
   Streamlit y prueba de Docker en un entorno independiente.

Se preparó una copia temporal para ensayar la migración sin alterar las fuentes. Hasta completar
las comprobaciones, las rutas históricas siguen siendo las utilizadas por el proyecto.
