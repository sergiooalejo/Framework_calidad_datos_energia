# Reproducir y verificar

## Preparar el entorno

Clone el repositorio completo y entre en `repositorio/`. Instale Python **3.14.0**
y Poetry **2.5.1**. La serie Python compatible está declarada en `pyproject.toml`;
`.python-version`, Docker y CI usan la versión concreta de referencia.

```powershell
python --version
python -m pip install poetry==2.5.1
poetry env use python
poetry check --lock
poetry sync --with dev
poetry run python scripts/verificar.py
```

Poetry instala el paquete desde `src/` y las versiones resueltas de `poetry.lock`.
No ejecute `poetry update` para reproducir esta entrega. `Environment/` conserva requisitos
anteriores y no define el entorno actual. La instalación inicial necesita acceso a los índices
de paquetes; la verificación usa los datos versionados y no descarga fuentes.

## Comprobaciones

`python scripts/verificar.py` comprueba estructura, 16 entradas históricas y las pruebas;
después audita los puntajes, folds, umbrales y métricas guardados de H3/H4. No reentrena
ni cambia resultados. Para omitir pruebas ya ejecutadas: `--sin-pruebas`.
`poetry run pytest` es otra entrada a las mismas suites científicas y de integración.

```powershell
poetry run framework-energia listar
poetry run framework-energia validar
poetry run framework-energia pruebas
poetry run streamlit run apps/streamlit_app.py
```

En un checkout sin instalación también funcionan `python pipeline.py listar`,
`python pipeline.py validar` y `python pipeline.py pruebas` si las dependencias están disponibles.
Con una CLI instalada desde otra carpeta, defina `FRAMEWORK_ENERGIA_ROOT` con la ruta absoluta
a `repositorio/`. La API importable del wheel es independiente de los datos; las etapas
científicas requieren el checkout completo, que contiene `Code/`, `configs/`, `Data/` y `Docs/`.

## Recalcular

Trabaje en una **copia** para conservar la evidencia entregada:

```powershell
poetry run framework-energia ejecutar hito3
poetry run framework-energia ejecutar hito4
poetry run framework-energia ejecutar muestra-h6
```

Estas etapas actualizan resultados y sus manifiestos. `muestra-h6` conserva archivos existentes.
`hito3-descargar` y `hito4-normativa` usan la red y las fuentes pueden cambiar;
para reproducir la entrega se usan las capturas locales de bronze.
`baseline` reproduce tareas anteriores a H4 y no sustituye el protocolo vigente.
Las semillas se registran por etapa; no se admite una semilla global arbitraria.
Los registros nuevos incluyen fecha y entorno: no se espera igualdad de bytes en timestamps,
figuras o archivos comprimidos, ni igualdad numérica bit a bit entre plataformas.

## Docker

Con Docker Desktop o un motor Docker disponible:

```powershell
docker compose config --quiet
docker compose up --build
```

El tablero queda en <http://localhost:8501>. Compose monta las salidas gold y las verificaciones
silver del host: ejecutar etapas desde el tablero las actualiza. Para comprobar una imagen
sin esos montajes puede usarse `docker compose build` y después:

```powershell
docker run --rm repositorio-tablero python scripts/verificar.py
```

El nombre de imagen depende del directorio/proyecto Compose; consulte `docker compose images`.
La imagen usa Python 3.14.0 y Poetry 2.5.1, con las dependencias de `poetry.lock`.
La etiqueta base fija la versión de Python, pero no un digest del sistema operativo.

## Automatización

`../.github/workflows/energia.yml` ejecuta en Linux y Windows: instalación desde el lock,
pruebas, auditorías, construcción de wheel y comprobación del wheel fuera del código fuente.
El job de Linux también construye y verifica el contenedor. Se activa al subir cambios o abrir
una PR; agregar el archivo no significa que el servicio remoto ya lo haya ejecutado.

## Notebooks

`notebooks/HITO3_REPLICACION.ipynb` usa los mismos comandos de H3 y regenera salidas.
Jupyter es una herramienta opcional del editor y no forma parte del entorno canónico del pipeline.
El notebook conserva un acceso desde su nombre anterior en la raíz.
