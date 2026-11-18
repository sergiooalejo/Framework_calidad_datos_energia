# Calidad de datos de energía

Framework de investigación para evaluar la calidad de datos de **EPM, CHEC, SSPD y XM**
y comparar alertas estadísticas sin confundirlas con errores confirmados.

## Empezar

Desde `repositorio/`, con **Python 3.14.0** y **Poetry 2.5.1** instalados:

```powershell
poetry env use python
poetry sync --with dev
poetry run framework-energia validar
poetry run python scripts/verificar.py
poetry run streamlit run apps/streamlit_app.py
```

Abrir el tablero en <http://localhost:8501>. `poetry sync` instala las versiones de
`poetry.lock`; no es necesario activar el entorno. La comprobación no recalcula experimentos.
La [guía de reproducibilidad](Docs/guias/reproducibilidad.md) explica instalación, Docker y regeneración.

## Dónde está cada cosa

```text
repositorio/
├── src/framework_calidad/   API Python y CLI instalables
├── apps/                    Tablero Streamlit
├── configs/                 Registro de tareas y semillas
├── tests/                   Integración, compatibilidad y muestras
├── scripts/                 Verificación del proyecto completo
├── notebooks/               Replicación interactiva
├── Data/                    Bronze: capturas; silver: datos preparados; gold: resultados
├── Code/                    Protocolos científicos versionados y accesos compatibles
├── Docs/                    Guías, decisiones y evidencia de la tesis
├── Environment/             Requisitos históricos; el entorno vigente usa poetry.lock
├── pyproject.toml           Paquete, dependencias, CLI y configuración de pruebas
├── poetry.lock              Versiones y hashes de dependencias
├── Dockerfile               Entorno del tablero y los experimentos
└── docker-compose.yml       Ejecución local del contenedor
```

Los protocolos de `Code/` y los datos mantienen sus rutas porque los manifiestos
científicos verifican sus hashes. El código reutilizable y el tablero tienen una única
implementación en `src/` y `apps/`; los accesos anteriores delegan en ella.
Vea el [mapa de arquitectura](Docs/guias/arquitectura.md) antes de agregar código.

## Qué ejecutar

| Necesidad | Comando desde `repositorio/` |
|---|---|
| Ver etapas disponibles | `poetry run framework-energia listar` |
| Validar estructura y datos | `poetry run framework-energia validar` |
| Pruebas y auditorías H3/H4 | `poetry run python scripts/verificar.py` |
| Solo pruebas | `poetry run framework-energia pruebas` |
| Pruebas con pytest | `poetry run pytest` |
| Recalcular protocolo vigente H4 | `poetry run framework-energia ejecutar hito4` |
| Crear otra muestra de revisión H6 | `poetry run framework-energia ejecutar muestra-h6` |
| Iniciar con Docker | `docker compose up --build` |

**Recalcular actualiza salidas y manifiestos.** Use una copia del checkout para conservar
la evidencia entregada. H6 crea archivos nuevos y conserva las muestras revisadas.
`python pipeline.py ...` y `python -m Code.hito5.run ...` siguen funcionando.

## Estado científico

El protocolo de comparación vigente es **H4-v2-CV-temporal**. La muestra H6 vigente contiene
50 observaciones EPM con alertas del escenario de 36 cambios de referencia. La revisión
externa y la aprobación académica siguen pendientes. Las métricas con prevalencia supuesta
no representan precisión empírica ni una validación externa terminada.

La [documentación](Docs/README.md) enlaza los resultados y las limitaciones.
La organización toma como referencias [Cookiecutter Data Science](https://cookiecutter-data-science.drivendata.org/)
y el [diseño src de PyPA](https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/).
