# Guía de ejecución del Hito 5

## 1. Elegir la forma de ejecución

Hay dos alternativas:

- **Streamlit local:** útil para desarrollar y revisar cambios rápidamente.
- **Docker:** recomendado para demostrar un entorno reproducible a otra persona.

## 2. Streamlit local

Desde la carpeta `repositorio/`:

```bash
poetry install
poetry run streamlit run app_streamlit.py
```

Poetry lee `poetry.lock`, por lo que instala las versiones fijadas. Si no se tiene Poetry,
puede utilizarse Docker o el entorno virtual descrito en `Environment/`. Si ese entorno fue
creado antes de la actualización de dependencias, reinstala su archivo de requisitos antes de
ejecutar los detectores; el tablero usa el mismo Python con el que se inició.

Abrir `http://localhost:8501`. Si se cambia el código, pulsar **Rerun**; si se cambian
dependencias, detener con `Ctrl+C` y volver a iniciar.

## 3. Docker

Con Docker Desktop iniciado:

```bash
docker compose up --build
```

Abrir `http://localhost:8501`. Para detener el contenedor, pulsar `Ctrl+C`. Compose conecta los
resultados Gold y las verificaciones Silver con las carpetas locales, para conservar los cambios
que se generen desde el tablero. Si se usa `docker run --rm` sin conectar carpetas, los resultados
creados dentro de ese contenedor se pierden cuando se detiene.

## 4. Orden de ejecución

En la barra lateral de Streamlit, las etapas aparecen en este orden:

1. Trazabilidad.
2. Cuarentena.
3. Cartas de control.
4. Revisión de cartas por fuente.
5. Matriz OE1.
6. Bootstrap.
7. Z-score robusto.
8. Isolation Forest.
9. Calibración.
10. Sensibilidad.
11. Métricas.
12. Regla sistémica.
13. Scorecard.
14. Niveles y costos.

Cada etapa requiere confirmación. No se deben presentar las alertas como incidentes confirmados
sin revisión y evidencia.

## 5. Semilla y manifiesto

Cada método usa su propia semilla fija cuando corresponde. Por ejemplo, Bootstrap usa la semilla
base `20261105`; la selección de la muestra Hito 6 usa `42`. La aplicación las muestra y no
permite cambiarlas. El manifiesto nuevo registra `semillas_base` en
`Data/gold/outputs/ejecuciones/`, junto con fecha, etapa, versión y SHA-256 de entradas.

En los manifiestos anteriores, el campo `semilla` era una declaración de la interfaz y no prueba
cuál usó cada script. Para interpretarlos hay que consultar la configuración del método.

## 6. Validación técnica

Para validar estructura y datos:

```bash
.venv-validacion/bin/python pipeline.py validar
.venv-validacion/bin/python pipeline.py pruebas
.venv-validacion/bin/python pipeline.py auditar
```

Las pruebas estadísticas requieren `.venv-validacion`, no el entorno mínimo de Streamlit.
Con Poetry se puede ejecutar cada comando por separado, por ejemplo
`poetry run python pipeline.py validar`, y luego repetirlo con `pruebas` y `auditar`.

## 7. Archivos principales

- `app_streamlit.py`: tablero.
- `pipeline.py`: línea de comandos.
- `Code/framework_calidad/`: paquete reutilizable.
- `Data/gold/outputs/calidad/matriz_oe1.yaml`: reglas y umbrales.
- `Data/gold/outputs/incidentes/bitacora_incidentes.csv`: bitácora.
- `Docs/DIAGRAMA_COMPONENTES_HITO5.md`: arquitectura.

