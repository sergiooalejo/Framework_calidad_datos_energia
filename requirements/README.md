# Entornos reproducibles del Hito 4

Los análisis 4.2 y 4.3–4.4 usan versiones diferentes de `numpy` y `scikit-learn`.
Por eso se entregan dos archivos bloqueados y no un único `requirements.txt`: mezclarlos
alteraría el entorno que produjo los resultados validados.

Las versiones se validaron con **Python 3.14.6** en macOS arm64. En otro sistema puede
funcionar con una versión compatible de Python, pero esa ejecución debe registrarse como
una nueva validación, no como una reproducción idéntica del entorno.

## Hito 4.2

Desde la raíz del repositorio:

```bash
python3 -m venv .venv-hito42
.venv-hito42/bin/python -m pip install -r requirements/requirements-hito4-2.txt
.venv-hito42/bin/python desarrollo_puntos/4.2/analisis_sensibilidad.py
.venv-hito42/bin/python desarrollo_puntos/4.2/informe_sensibilidad.py
.venv-hito42/bin/python -m unittest discover -s desarrollo_puntos/4.2 -p test_sensibilidad.py -v
.venv-hito42/bin/python desarrollo_puntos/4.2/verificar_resultados.py
```

## Hitos 4.3 y 4.4

```bash
python3 -m venv .venv-hito43_44
.venv-hito43_44/bin/python -m pip install -r requirements/requirements-hito4-3-4.txt

.venv-hito43_44/bin/python desarrollo_puntos/4.3/experimento_tasa_igualada.py
.venv-hito43_44/bin/python desarrollo_puntos/4.3/informe_metricas.py
.venv-hito43_44/bin/python -m unittest discover -s desarrollo_puntos/4.3 -p test_metricas.py -v
.venv-hito43_44/bin/python desarrollo_puntos/4.3/verificar_resultados.py

.venv-hito43_44/bin/python desarrollo_puntos/4.4/calibrar_regla_sistemica.py
.venv-hito43_44/bin/python desarrollo_puntos/4.4/informe_regla_sistemica.py
.venv-hito43_44/bin/python -m unittest discover -s desarrollo_puntos/4.4 -p test_regla_sistemica.py -v
.venv-hito43_44/bin/python desarrollo_puntos/4.4/verificar_resultados.py
```

Las carpetas `.venv-hito42/` y `.venv-hito43_44/` están ignoradas por Git. Las figuras se
generan localmente desde los CSV y tampoco se versionan; los resultados tabulares, scripts,
configuraciones y manifiestos SHA-256 sí permanecen en el repositorio.
