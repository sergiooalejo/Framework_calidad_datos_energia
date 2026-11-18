# Hito 6 · Validación del protocolo vigente

El generador utiliza `Data/gold/outputs/hito4/puntajes_reales.csv.gz`,
`calibracion.csv` y `manifiesto.json` del protocolo **H4-v2-CV-temporal**.
Selecciona **50 observaciones únicas de EPM con alerta**, de acuerdo con el plan
original, con semilla 42. No reutiliza los escenarios históricos de sensibilidad.

## Ejecución

Desde `repositorio/`:

```powershell
python pipeline.py ejecutar muestra-h6
python -m Code.hito6.run --help
python -m Code.hito6.run --salida Data/gold/outputs/hito6/otra_muestra.csv
python -B -m unittest discover -s Code/hito6 -p "test_*.py" -v
```

La CLI y el acceso anterior `Code/Evaluation/hito6/generar_muestra_alertas.py`
delegan en el mismo generador. La CLI añade su manifiesto general y el generador
siempre escribe un manifiesto específico, también cuando se ejecuta directamente.
`python pipeline.py pruebas` incluye las regresiones de Hito 6.

## Población y criterios

- Fuente EPM, referencia de 36 cambios, horizonte `t` y tasa objetivo de calibración
  5 %, con las banderas almacenadas por H4. El 5 % no es una tasa de error real.
- Una unidad por fuente, `sid` y período: sin repetir observaciones entre ventanas,
  bancos o métodos. El orden del archivo no cambia el sorteo.
- Se conservan los seis métodos: IMR, Z robusto, IF, LOF, KNN y R12; con puntajes,
  umbrales y banderas, incluso cuando un método no activa una señal.
- R12 es el puntaje de magnitud calibrado por CV en este escenario; su bandera no
  equivale necesariamente a superar el factor nativo 10 del experimento histórico.
- Si hay menos de 50 observaciones elegibles, el proceso informa el problema:
  no inventa, duplica ni completa la muestra con otras fuentes.
- Se verifican hashes de las entradas y código H4, cuarentena, puntajes y calibración;
  además se coteja cada bandera con su puntaje y umbral. Una línea base cambiada
  debe regenerarse y verificarse antes de seleccionar una muestra nueva.

## Salidas y revisión

La muestra vigente es `Data/gold/outputs/hito6/muestra_alertas_h4_v2_epm_50.csv`
y su procedencia está en el archivo adyacente `.manifiesto.json`. El manifiesto
registra hashes, población candidata, cuotas, semilla e identificadores elegidos.

La muestra histórica `muestra_alertas_50.csv` se conserva como antecedente, junto
con sus clasificaciones. Una nueva ejecución añade fecha al nombre si ya existe
la muestra o su manifiesto. `--salida` también rechaza rutas ya ocupadas.
No se transfieren revisiones automáticamente entre protocolos.

Completar `clasificacion`, `evidencia_externa`, `revisor`, `fecha_revision` y
`observaciones`. La muestra comienza pendiente: una alerta no confirma un error.
La selección es aleatoria dentro de las alertas EPM del escenario indicado;
no garantiza representación de todos los métodos ni de otras fuentes. La precisión
por método requiere revisar sus alertas y declarar su denominador; esta muestra
por sí sola no permite estimar recall ni la calidad global de los datos.

La revisión externa y la aprobación metodológica siguen pendientes; consultar
`Docs/PLAN_TRABAJO_HITO6.md` y `Docs/ANEXO_VALIDACION_EXTERNA_HITO6.md`.

Verificación de esta actualización: `Docs/VERIFICACION_HITO6.md`.
