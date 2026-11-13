# Reproducibilidad del Hito 5

## Propósito

La reproducibilidad significa que otra persona puede ejecutar el mismo procedimiento con los
mismos datos, código, dependencias y parámetros, y obtener resultados comparables.

## Entorno correcto

El entorno de Streamlit sirve para visualizar y ejecutar el tablero, pero no contiene todas las
bibliotecas de los experimentos estadísticos. Para ejecutar las pruebas de los Hitos 4 y 5 se
debe crear un entorno separado:

```bash
python3 -m venv .venv-validacion
.venv-validacion/bin/python -m pip install -r Environment/requirements-validacion-local.txt
.venv-validacion/bin/python pipeline.py validar
.venv-validacion/bin/python pipeline.py pruebas
.venv-validacion/bin/python pipeline.py auditar
```

En Windows se sustituye `bin/python` por `Scripts/python`.

## Evidencia de cada ejecución

Las etapas ejecutadas por `pipeline.py` generan un manifiesto en
`Data/gold/outputs/ejecuciones/`. Los manifiestos nuevos registran etapa, fecha UTC, versión del
paquete, semillas base fijas de la etapa, versión de Python y SHA-256 de los archivos de entrada.
Algunos métodos derivan semillas adicionales por fuente, serie o partición. Los manifiestos antiguos
que indicaban `semilla: 42` registraban una declaración de la interfaz, no necesariamente la
semilla efectiva; se conservan como evidencia histórica y deben leerse junto a la configuración de
cada método.

## Estado de esta entrega

- La sintaxis de los módulos y de la CLI fue validada.
- La CLI está configurada para ejecutar las pruebas de sensibilidad, métricas y regla sistémica.
- El archivo `requirements-streamlit.txt` incluye ahora las bibliotecas científicas necesarias
  para las etapas del tablero. Un entorno creado antes de este cambio debe actualizarse con
  `python -m pip install -r Environment/requirements-streamlit.txt` usando su propio Python.
- El cierre definitivo exige ejecutar las pruebas con ese entorno y conservar el resultado en la
  documentación de la tesis.

