# Calidad de datos de energía

Framework de investigación para EPM, CHEC, SSPD y XM. La raíz de `repositorio/`
contiene únicamente carpetas; los archivos de instalación están dentro de `src/`.

## Mapa del proyecto

| Carpeta | Contenido |
|---|---|
| `Code/` | Preparación, calidad, modelos, experimentos y evaluación por responsabilidad. |
| `src/` | Paquete Python instalable, `pyproject.toml`, lock y versión de Python. |
| `apps/` | Tablero Streamlit y su acceso de lanzamiento. |
| `configs/` | Registro del proyecto, tareas, semillas y mapas de rutas. |
| `Data/` | Datos de entrada, catálogos, metadatos y diccionarios. |
| `z_findings/` | Resultados, hallazgos, auditorías, informes y evidencia histórica. |
| `Docs/` | Guías, resultados, decisiones, referencias y archivo histórico. |
| `deployment/` | Dockerfile, Compose y exclusiones del contexto Docker. |
| `environments/` | Requisitos históricos conservados por procedencia. |
| `notebooks/` | Replicación interactiva. |
| `scripts/` | CLI de acceso y utilidades de verificación y empaquetado. |
| `tests/` | Pruebas de integración y regresión. |
| `.streamlit/` | Configuración estándar del tablero. |

Los datos de entrada permanecen en `Data/`; las rutas históricas de resultados se resuelven mediante los mapas de `configs/`.
Los entornos locales `.venv*` siguen ignorados por Git. Las reglas Git se aplican desde
la raíz del repositorio contenedor, sin dejar archivos sueltos en esta carpeta.

## Comandos para usar después

Desde `repositorio/`, con Python 3.14.0 y Poetry 2.5.1:

```powershell
poetry --project src sync --with dev
poetry --project src run framework-energia listar
poetry --project src run streamlit run apps/tablero_streamlit.py
```

La CLI sin instalación se accede mediante `python scripts/flujo_trabajo.py ...`, si las
bibliotecas están disponibles. Docker: `docker compose -f deployment/compose.yaml up --build`.

## Documentación

- [Instalación y reproducibilidad](guides/reproducibilidad.md).
- [Arquitectura](guides/arquitectura.md).
- [Índice de evidencia por etapa](overview/indice_documentacion.md).
- [Calidad de datos](../z_findings/reports/data_quality/verificacion.md).
- [Resultados de experimentos](../z_findings/reports/experiments/resultados.md).
- [Validación externa pendiente](external_validation/plan_trabajo.md).
- [Decisiones](governance/decisiones.md).

El protocolo vigente es H4-v2-CV-temporal. La revisión externa y la aprobación académica
siguen pendientes. Los identificadores históricos describen versiones, no la organización del código.

Esta reorganización actualizó rutas, importaciones, documentación y despliegue.
No se ejecutó el proyecto, ni se corrieron pruebas, auditorías o experimentos.

## Resultados centralizados

Todos los resultados, hallazgos, auditorías e informes se consultan en
[z_findings/README.md](../z_findings/README.md). Los datos de entrada permanecen en `Data/`.

## Nombres de archivos

Los nombres descriptivos están en español. Se conservan convenciones como `README.md`,
`__init__.py`, `pyproject.toml`, `poetry.lock`, `Dockerfile`, `test_` y nombres oficiales de fuentes.
El historial de cambios está en `configs/renombrado_archivos.json`. No se ejecutó el proyecto ni pruebas.

## Verificación funcional posterior

El 18 de noviembre de 2026 se ejecutaron las pruebas, pipelines y comprobaciones de Docker.
Consulte el [informe de verificación funcional](../z_findings/reports/verificacion_funcional_2026_11_18.md),
que describe la reparación de nueve resultados y el límite de la segunda captura de CHEC.
