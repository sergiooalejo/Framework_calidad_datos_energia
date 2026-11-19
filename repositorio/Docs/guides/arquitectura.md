# Arquitectura

## Código y accesos

| Carpeta | Responsabilidad |
|---|---|
| `src/framework_calidad/` | API instalable: carga, perfilamiento, reglas y reportes. `consola.py` coordina tareas. |
| `apps/` | Interfaz Streamlit; lee resultados y permite ejecutar etapas explícitamente. |
| `configs/etapas.toml` | Registro único de comandos, baseline y semillas declaradas. |
| `tests/` | Pruebas actuales de integración, organización y muestra H6. |
| `Code/data_quality/` | Protocolo científico de calidad: reglas R01–R12, cuarentena, cartas y captura. |
| `Code/experiments/` | Comparación vigente con validación cruzada temporal, referencia y vigilancia separadas. |
| `Code/external_validation/` | Generador de muestras para revisión externa; conserva las muestras anteriores. |
| `Code/interfaces/` y `Code/framework_calidad/` | Accesos compatibles a la API, CLI y tablero actuales. |
| `Code/data_preparation/` | Preparación y línea base OE1. Algunos módulos siguen siendo entradas de H3/H4. |
| `Code/model_development/` y `Code/model_evaluation/` | Experimentos y evaluación anteriores; las etapas históricas están nombradas en la CLI. |

El código se organiza por función, no por entregas. Los resultados históricos conservan sus
identificadores H3/H4/H6 para evitar confundir versiones de protocolos.
`configs/mapa_codigo.json` registra rutas y huellas originales y actuales; un único ZIP
conserva el código anterior. `Code/trazabilidad_evidencia.py` permite comprobar los manifiestos originales
sin editarlos y rechaza cambios posteriores no registrados en el código correspondiente.
La migración es estructural: no se recalcularon resultados ni se ejecutaron pruebas.

## Datos

Flujo: `Data/bronze/` → `Data/silver/` → `z_findings/results/`.
Bronze conserva capturas; silver contiene datos preparados, catálogos y metadatos;
gold reúne cuarentena, puntajes, métricas, figuras y muestras. Los manifiestos registran
entradas, semillas, código y salidas. `Data/manifiesto_medallon.json` describe las capas.

Los formatos y columnas se consultan en los diccionarios y catálogos de `Data/silver/`.
No se creó una carpeta vacía de modelos: el proyecto entrega puntajes y métricas,
no un servicio de predicción con un modelo entrenado publicado.

## Agregar funcionalidad

Agregue componentes reutilizables a `src/framework_calidad/`, interfaces a `apps/`,
pruebas de integración a `tests/` y análisis interactivos a `notebooks/`.
Registre nuevas etapas en `configs/etapas.toml`. Las semillas deben coincidir con las
constantes efectivamente usadas por cada protocolo; cambiar el registro no cambia un experimento.
Los cambios metodológicos requieren una nueva versión de protocolo y su propia evidencia.

## Compatibilidad

`scripts/flujo_trabajo.py`, `apps/iniciar_tablero.py`, los módulos de `Code/interfaces/` y los imports con `PYTHONPATH=Code`
o `PYTHONPATH=Code/interfaces` delegan en las implementaciones actuales. El notebook de la raíz
es un acceso compatible al de `notebooks/`. Las rutas científicas actuales están en `configs/mapa_codigo.json`; las anteriores se conservan como procedencia.
El registro `z_findings/provenance/reorganizacion_codigo.json` documenta los traslados y sus huellas iniciales.

Referencias: [PyPA: src layout](https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/)
y [Cookiecutter Data Science](https://cookiecutter-data-science.drivendata.org/).
Se adoptó la separación de responsabilidades manteniendo la arquitectura medallón del proyecto.
