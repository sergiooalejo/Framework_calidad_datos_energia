# Reproducir y verificar

## Preparar el entorno

Clone el repositorio completo y entre en `repositorio/`. Instale Python **3.14.0**
y Poetry **2.5.1**. La serie Python compatible está declarada en `src/pyproject.toml`;
`src/.python-version`, Docker y CI usan la versión concreta de referencia.

```powershell
python --version
python -m pip install poetry==2.5.1
poetry --project src env use python
poetry --project src check --lock
poetry --project src sync --with dev
poetry --project src run python scripts/verificar.py
```

Poetry instala el paquete desde `src/` y las versiones resueltas de `src/poetry.lock`.
No ejecute `poetry --project src update` para reproducir esta entrega. `environments/` conserva requisitos
anteriores y no define el entorno actual. La instalación inicial necesita acceso a los índices
de paquetes; la verificación usa los datos versionados y no descarga fuentes.

## Comprobaciones

`python scripts/verificar.py` comprueba estructura, 16 entradas históricas y las pruebas;
después audita los puntajes, folds, umbrales y métricas guardados de H3/H4. No reentrena
ni cambia resultados. Para omitir pruebas ya ejecutadas: `--sin-pruebas`.
`poetry --project src run pytest` es otra entrada a las mismas suites científicas y de integración.

```powershell
poetry --project src run framework-energia listar
poetry --project src run framework-energia validar
poetry --project src run framework-energia pruebas
poetry --project src run streamlit run apps/tablero_streamlit.py
```

En un checkout sin instalación también funcionan `python scripts/flujo_trabajo.py listar`,
`python scripts/flujo_trabajo.py validar` y `python scripts/flujo_trabajo.py pruebas` si las dependencias están disponibles.
Con una CLI instalada desde otra carpeta, defina `FRAMEWORK_ENERGIA_ROOT` con la ruta absoluta
a `repositorio/`. La API importable del wheel es independiente de los datos; las etapas
científicas requieren el checkout completo, que contiene `Code/`, `configs/`, `Data/` y `Docs/`.

## Recalcular

Trabaje en una **copia** para conservar la evidencia entregada:

```powershell
poetry --project src run framework-energia ejecutar hito3
poetry --project src run framework-energia ejecutar hito4
poetry --project src run framework-energia ejecutar muestra-h6
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
docker compose -f deployment/compose.yaml config --quiet
docker compose -f deployment/compose.yaml up --build
```

El tablero queda en <http://localhost:8501>. Compose monta las salidas gold y las verificaciones
silver del host: ejecutar etapas desde el tablero las actualiza. Para comprobar una imagen
sin esos montajes puede usarse `docker compose -f deployment/compose.yaml build` y después:

```powershell
docker run --rm repositorio-tablero python scripts/verificar.py
```

El nombre de imagen depende del directorio/proyecto Compose; consulte `docker compose -f deployment/compose.yaml images`.
La imagen usa Python 3.14.0 y Poetry 2.5.1, con las dependencias de `src/poetry.lock`.
La etiqueta base fija la versión de Python, pero no un digest del sistema operativo.

## Automatización

`../.github/workflows/energia.yml` ejecuta en Linux y Windows: instalación desde el lock,
pruebas, auditorías, construcción de wheel y comprobación del wheel fuera del código fuente.
El job de Linux también construye y verifica el contenedor. Se activa al subir cambios o abrir
una PR; agregar el archivo no significa que el servicio remoto ya lo haya ejecutado.

## Notebooks

`notebooks/replicacion_calidad_datos.ipynb` usa los mismos comandos de H3 y regenera salidas.
Jupyter es una herramienta opcional del editor y no forma parte del entorno canónico del pipeline.
El acceso de lanzamiento está en `notebooks/iniciar_replicacion.ipynb`.

## Organización funcional del código

Las rutas vigentes están en [Code/README.md](../../Code/README.md). La estructura por hitos
fue sustituida por responsabilidades. Las etapas de CLI conservan sus nombres anteriores
como alias internos; sus comandos apuntan a los módulos nuevos. Esta reorganización
no incluyó ejecución del proyecto ni pruebas, por petición del usuario.

## Verificación funcional realizada

La verificación posterior a las reorganizaciones se documenta en
[el informe funcional](../../z_findings/reports/verificacion_funcional_2026_11_18.md).
Para regenerar, ejecutar calidad H3, después experimentos H4 y después la muestra H6.
Recalcular únicamente una etapa previa puede dejar desactualizados los manifiestos posteriores.
