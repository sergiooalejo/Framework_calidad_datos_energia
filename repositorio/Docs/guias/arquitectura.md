# Arquitectura

## Código y accesos

| Carpeta | Responsabilidad |
|---|---|
| `src/framework_calidad/` | API instalable: carga, perfilamiento, reglas y reportes. `cli.py` coordina tareas. |
| `apps/` | Interfaz Streamlit; lee resultados y permite ejecutar etapas explícitamente. |
| `configs/pipeline.toml` | Registro único de comandos, baseline y semillas declaradas. |
| `tests/` | Pruebas actuales de integración, organización y muestra H6. |
| `Code/hito3/` | Protocolo científico de calidad: reglas R01–R12, cuarentena, cartas y captura. |
| `Code/hito4/` | Comparación vigente con validación cruzada temporal, referencia y vigilancia separadas. |
| `Code/hito6/` | Generador de muestras para revisión externa; conserva las muestras anteriores. |
| `Code/hito5/` y `Code/framework_calidad/` | Accesos compatibles a la API, CLI y tablero actuales. |
| `Code/Data_Acquisition_and_Understanding/` | Preparación y línea base OE1. Algunos módulos siguen siendo entradas de H3/H4. |
| `Code/Modeling/` y `Code/Evaluation/` | Experimentos y evaluación anteriores; las etapas históricas están nombradas en la CLI. |

Los protocolos y algunas pruebas permanecen junto a su evidencia: H3/H4 incluyen sus hashes
en manifiestos. Moverlos o editar importaciones invalidaría esa correspondencia. No se sustituyen
los hashes para presentar evidencia antigua como producto de código nuevo.

## Datos

Flujo: `Data/bronze/` → `Data/silver/` → `Data/gold/outputs/`.
Bronze conserva capturas; silver contiene datos preparados, catálogos y metadatos;
gold reúne cuarentena, puntajes, métricas, figuras y muestras. Los manifiestos registran
entradas, semillas, código y salidas. `Data/medallion_manifest.json` describe las capas.

Los formatos y columnas se consultan en los diccionarios y catálogos de `Data/silver/`.
No se creó una carpeta vacía de modelos: el proyecto entrega puntajes y métricas,
no un servicio de predicción con un modelo entrenado publicado.

## Agregar funcionalidad

Agregue componentes reutilizables a `src/framework_calidad/`, interfaces a `apps/`,
pruebas de integración a `tests/` y análisis interactivos a `notebooks/`.
Registre nuevas etapas en `configs/pipeline.toml`. Las semillas deben coincidir con las
constantes efectivamente usadas por cada protocolo; cambiar el registro no cambia un experimento.
Los cambios metodológicos requieren una nueva versión de protocolo y su propia evidencia.

## Compatibilidad

`pipeline.py`, `app_streamlit.py`, los módulos H5 y los imports con `PYTHONPATH=Code`
o `PYTHONPATH=Code/hito5` delegan en las implementaciones actuales. El notebook de la raíz
es un acceso compatible al de `notebooks/`. Los scripts científicos conservan sus rutas.
El registro `Docs/organizacion_2026.json` documenta los traslados y sus huellas iniciales.

Referencias: [PyPA: src layout](https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/)
y [Cookiecutter Data Science](https://cookiecutter-data-science.drivendata.org/).
Se adoptó la separación de responsabilidades manteniendo la arquitectura medallón del proyecto.
