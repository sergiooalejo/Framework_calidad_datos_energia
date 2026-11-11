# Guía de ejecución del Hito 5

## 1. Elegir la forma de ejecución

Hay dos alternativas:

- **Streamlit local:** útil para desarrollar y revisar cambios rápidamente.
- **Docker:** recomendado para demostrar un entorno reproducible a otra persona.

## 2. Streamlit local

Desde la carpeta `repositorio/`:

```bash
python3 -m venv .venv-streamlit
.venv-streamlit/bin/python -m pip install -r Environment/requirements-streamlit.txt
.venv-streamlit/bin/python -m pip install -e .
.venv-streamlit/bin/streamlit run app_streamlit.py
```

Abrir `http://localhost:8501`. Si se cambia el código, pulsar **Rerun**; si se cambian
dependencias, detener con `Ctrl+C` y volver a iniciar.

## 3. Docker

Con Docker Desktop iniciado:

```bash
docker build -t calidad-energia-streamlit .
docker run --rm -p 8501:8501 calidad-energia-streamlit
```

Abrir `http://localhost:8501`. Para detener el contenedor, pulsar `Ctrl+C`.

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

Se recomienda usar la semilla `42` para comparaciones. Cada ejecución crea un archivo en
`Outputs/ejecuciones/` con fecha, etapa, versión, semilla y SHA-256 de entradas.

## 6. Validación técnica

Para validar estructura y datos:

```bash
.venv-validacion/bin/python pipeline.py validar
.venv-validacion/bin/python pipeline.py pruebas
.venv-validacion/bin/python pipeline.py auditar
```

Las pruebas estadísticas requieren `.venv-validacion`, no el entorno mínimo de Streamlit.

## 7. Archivos principales

- `app_streamlit.py`: tablero.
- `pipeline.py`: línea de comandos.
- `Code/framework_calidad/`: paquete reutilizable.
- `Outputs/calidad/matriz_oe1.yaml`: reglas y umbrales.
- `Outputs/incidentes/bitacora_incidentes.csv`: bitácora.
- `Docs/DIAGRAMA_COMPONENTES_HITO5.md`: arquitectura.

