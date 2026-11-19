# Resultados y hallazgos del framework

Punto único de consulta de resultados actuales e históricos. Los archivos se trasladaron;
no se recalcularon experimentos ni se modificaron los manifiestos científicos originales.

| Carpeta | Contenido |
|---|---|
| [results/data_quality](results/data_quality/) | Reglas, cuarentena, cartas y hallazgos del protocolo de calidad. |
| [results/experiments](results/experiments/) | Comparación vigente: puntajes, calibración, métricas, scorecard y figuras. |
| [results/external_validation](results/external_validation/) | Muestras de alertas y manifiestos para revisión externa. |
| [results](results/) | También contiene línea base, detectores, costos, incidentes y ejecuciones. |
| [preparation](preparation/) | Salidas de adaptadores y preparación; algunas son entradas de experimentos posteriores. |
| [audits](audits/) | Verificaciones y trazabilidad de filas. |
| [reports](reports/) | Informes legibles de resultados, verificaciones y hallazgos. |
| [provenance](provenance/) | Inventarios, validaciones y registros de migración. |
| [archive/evidence](archive/evidence/) | Evidencia anterior conservada con sus bytes originales. |

## Por dónde empezar

1. [Resultados vigentes](reports/experiments/resultados.md).
2. [Verificación de calidad](reports/data_quality/verificacion.md).
3. [Muestras para revisión externa](results/external_validation/).
4. [Correcciones y hallazgos de revisión](reports/correcciones_revision.md).

El protocolo vigente es **H4-v2-CV-temporal**. Los resultados anteriores se conservan como
antecedentes. Una alerta no confirma un error; la revisión externa y aprobación académica
siguen pendientes.

Los manifiestos pueden mencionar rutas anteriores. `configs/mapa_estructura.json` y
`Code/trazabilidad_evidencia.py` resuelven esas ubicaciones sin reescribir la evidencia científica.
Las futuras salidas del código y del tablero apuntan a esta carpeta.

No se ejecutó el framework ni se hicieron pruebas, auditorías, entrenamientos o experimentos.

## Archivo original bloqueado

Windows mantiene bloqueado `Data/gold/outputs/hito3/EPM/hallazgos.csv`. Sus mismos bytes
ya están en `results/data_quality/EPM/hallazgos.csv`, que es la ruta vigente. Se conservó
el original sin cerrar aplicaciones; podrá retirarse cuando el proceso libere el archivo.
El registro del traslado está en `configs/traslado_resultados.json`.

## Verificación funcional

[Informe del 18 de noviembre de 2026](reports/verificacion_funcional_2026_11_18.md):
pruebas, Docker, reproducción de resultados y reparación de nueve archivos de ejecuciones parciales.
