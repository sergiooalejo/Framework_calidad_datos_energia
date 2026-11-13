# Calidad de datos del sector energético colombiano

Proyecto de ciencia de datos consolidado al **9 de noviembre de 2026**, con código,
datos locales, experimentos, resultados y pruebas de todas las actividades 3.1–3.7 y
4.1–4.6. Esta carpeta se puede copiar y ejecutar por separado: no necesita las carpetas
originales `desarrollo_puntos` ni `fuentes_datos`.

Los Hitos 3 y 4 cuentan con una línea base técnica. La aprobación metodológica y académica
continúa pendiente. El empaquetado definitivo, contenedor, tablero y validación externa
de los Hitos 5–6 siguen en el plan.

## Estructura

```text
repositorio/
├── Code/
│   ├── Data_Acquisition_and_Understanding/  # Calidad, adaptadores, trazabilidad y cuarentena
│   ├── Modeling/                          # Cartas, detectores y experimentos
│   └── Evaluation/                        # Scorecard, niveles y costos
├── Code/framework_calidad/                 # API reutilizable del framework
├── Data/                                  # Datos completos y evidencia de las fuentes
├── Sample_Data/                           # Diez filas por fuente, solo para inspección
├── Outputs/                               # Tablas, configuraciones, informes y figuras
├── Environment/                           # Dependencias históricas y validación local
├── Docs/
│   ├── PROYECTO.md                        # Alcance, métodos, resultados y plan
│   ├── DECISIONES.md                      # Propuestas y aprobación pendiente
│   ├── REFERENCIA_TECNICA.md               # Fichas e informes consolidados con procedencia
│   ├── MIGRACION.csv                      # Origen, destino y hashes de cada archivo
│   └── Antecedentes/                      # Evidencia del plan original
├── project.json                           # Mapa de actividades y marcador de raíz
└── pipeline.py                            # Comandos de ejecución y comprobación
```

La estructura adapta [Azure TDSP ProjectTemplate](https://github.com/Azure/Azure-TDSP-ProjectTemplate).
Se mantienen Code, Docs y Sample_Data; se añaden Data, Outputs, Environment y Evaluation
para separar entradas, resultados y evaluación. Las muestras no contienen los datasets
completos. No hay servicios de Azure ni despliegue en producción implementados.

Hay **cuatro documentos de lectura principal**, contando este README. Los informes de texto
en Outputs son salidas regenerables, no documentos de gestión adicionales. Las fichas,
decisiones y evidencia de todos los puntos originales están cubiertas en Docs y su inventario.

## Empezar

Desde esta carpeta, con Python 3.14:

```powershell
python pipeline.py validar
python pipeline.py listar
python pipeline.py ejecutar baseline
```

`validar` comprueba estructura, sintaxis y hashes de datos sin instalar bibliotecas externas.
`baseline` regenera trazabilidad, cuarentena, las cuatro cartas, revisión EPM, matriz,
bootstrap, scorecard y niveles/costos a partir de los datos y experimentos conservados.
Estas etapas usan la biblioteca estándar. Escriben en Outputs y Data/verificaciones;
no modifican los datos de entrada. Para comparar salidas conviene guardar una copia previa.

Cada ejecución de `ejecutar` crea un manifiesto JSON en `Outputs/ejecuciones/` con fecha UTC,
etapa, versión del paquete, semilla declarada, versión de Python y SHA-256 de los archivos de
entrada. Por ejemplo: `python pipeline.py ejecutar scorecard --semilla 42`.

## Pruebas y auditoría científica

El entorno local comprobado es Windows, Python 3.14.0, NumPy 2.3.5, pandas 2.3.3,
scikit-learn 1.8.0 y Matplotlib 3.10.8. Para recrearlo en un entorno independiente:

```powershell
python -m venv .venv-validacion
.venv-validacion/Scripts/python -m pip install -r Environment/requirements-validacion-local.txt
.venv-validacion/Scripts/python pipeline.py pruebas
.venv-validacion/Scripts/python pipeline.py auditar
```

En Linux/macOS se sustituye `Scripts/python` por `bin/python`. `pruebas` ejecuta las
31 pruebas existentes. `auditar` reconcilia los resultados de sensibilidad, métricas y
regla sistémica y actualiza sus informes de verificación/manifiestos. No reentrena modelos.
Las fechas históricas dentro de las salidas heredadas identifican su experimento original;
la validación de esta reorganización se registra en `Docs/VALIDACION.json`.

Los archivos `Environment/requirements-hito4-2.txt` y
`Environment/requirements-hito4-3-4.txt` conservan las versiones de los experimentos
originales. Deben utilizarse en entornos separados si se pretende reproducir ese
entrenamiento; pasar las auditorías locales no acredita identidad con aquellos ambientes.

## Paquete reutilizable

El paquete `Code/framework_calidad` separa responsabilidades comunes para cargar datos,
perfilar columnas, evaluar reglas, aplicar detectores y escribir resultados. Se puede instalar
en modo editable desde `repositorio/`:

```powershell
python -m pip install -e .
```

Para instalar el entorno completo y reproducible con Poetry:

```powershell
poetry install
```

El archivo `poetry.lock` fija las versiones exactas. Docker utiliza este mismo lock durante la
construcción de la imagen.

Los scripts históricos de `Code/` se conservan como evidencia. La migración de cada experimento
al paquete será gradual y solo se aceptará si reproduce sus salidas.

La configuración declarativa vigente se encuentra en
`Outputs/calidad/matriz_oe1.yaml`. Allí están las ocho dimensiones, los tipos de regla, los
indicadores, las fórmulas, los umbrales propuestos, la severidad y el estado de aprobación.
El paquete expone `cargar_configuracion()` y `listar_indicadores()` para leerla sin codificar
esas decisiones directamente en Python.

## Tablero Streamlit del Hito 5

Por sugerencia del profesor, el artefacto de visualización se implementa inicialmente en
Streamlit. `app_streamlit.py` lee únicamente las salidas versionadas de `Outputs/`: scorecard,
matriz de dimensiones, alertas sistémicas y métricas. No descarga datos, no cambia los CSV y
no recalcula los experimentos. Para ejecutarlo en un entorno separado:

```powershell
python -m venv .venv-streamlit
.venv-streamlit/Scripts/python -m pip install -r Environment/requirements-streamlit.txt
.venv-streamlit/Scripts/streamlit run app_streamlit.py
```

En Linux/macOS se sustituye `Scripts` por `bin`. El tablero es la primera vista funcional del
Hito 5; todavía deben completarse el empaquetado definitivo, el contenedor, la bitácora de
incidentes y la revisión de aceptación metodológica.

La barra lateral incluye un selector de etapas autorizadas y el botón **Ejecutar etapa**.
Permite ejecutar matriz OE1, cartas, bootstrap, detectores, métricas, scorecard y niveles/costos.
Requiere marcar la confirmación y permite declarar una semilla. La acción llama únicamente a
la etapa seleccionada de `pipeline.py`, crea el manifiesto de ejecución y actualiza sus salidas.
Después se debe pulsar `Rerun` para visualizar los nuevos resultados.

La revisión de cartas ahora tiene dos niveles: una revisión estructural comparable para EPM,
CHEC, SSPD y XM (`Outputs/cartas/revision_cartas_fuentes.csv`) y la revisión estadística
detallada heredada de EPM. La primera no sustituye la interpretación específica de cada fuente.

## Ejecutar componentes

## Ejecutar con Docker

Con Docker instalado, desde `repositorio/`:

```bash
docker build -t calidad-energia-streamlit .
docker run --rm -p 8501:8501 calidad-energia-streamlit
```

También se puede usar Compose:

```bash
docker compose up --build
```

El tablero quedará disponible en `http://localhost:8501`. La imagen contiene el código,
las dependencias y las salidas versionadas; no incluye los datasets completos de `Data/datos/`
ni descarga información durante el arranque.

```powershell
python pipeline.py ejecutar zscore
python pipeline.py ejecutar isolation-forest
python pipeline.py ejecutar calibracion
python pipeline.py ejecutar sensibilidad
python pipeline.py ejecutar metricas
python pipeline.py ejecutar sistemica
python pipeline.py ejecutar figuras
```

Los experimentos de entrenamiento pueden ser prolongados; se ejecutan de forma explícita
y requieren el entorno correspondiente. `listar` muestra las rutas concretas para ejecutar
un script directamente y consultar sus parámetros. Los datos completos están incluidos;
no se realizan descargas de los portales como parte de estos comandos.

## Lectura y trazabilidad

- [Informe de validación del Hito 5](Docs/INFORME_VALIDACION_HITO5.md): comandos, resultados,
  evidencia y limitaciones.
- [Cierre del Hito 5](Docs/CIERRE_HITO5.md): entregables terminados y pendientes académicos.

- [Diagrama de componentes del Hito 5](Docs/DIAGRAMA_COMPONENTES_HITO5.md): flujo del artefacto,
  entradas, procesos, salidas, Streamlit y Docker.
- [Guía de ejecución del Hito 5](Docs/GUIA_EJECUCION_HITO5.md): instalación, orden de etapas,
  validación y solución de uso básico.

La bitácora inicial está en `Outputs/incidentes/bitacora_incidentes.csv` y se visualiza en la
pestaña **Incidentes**. Solo deben registrarse alertas confirmadas o formalmente abiertas después
de revisión; el tablero no convierte automáticamente una señal estadística en un incidente.

- [Proyecto y resultados](Docs/PROYECTO.md): alcance, correspondencia de todas las actividades,
  interpretación científica y criterios de aceptación.
- [Decisiones](Docs/DECISIONES.md): propuestas para el profesor, sin aprobaciones inventadas.
- [Referencia técnica](Docs/REFERENCIA_TECNICA.md): detalle consolidado con índice y contexto histórico.
- [Migración](Docs/MIGRACION.csv): cobertura por archivo y hashes originales/adaptados.
- [Procedencia](Docs/PROCEDENCIA.json): configuraciones JSON originales, antes de adaptar rutas y huellas.
- [Validación de esta entrega](Docs/VALIDACION.json): comprobaciones, entorno y límites.

Los originales permanecen intactos fuera de esta carpeta. Las fórmulas y decisiones de los
experimentos se conservan; la adaptación separa rutas, imports y salidas. Las configuraciones
que dependen de rutas/hashes se actualizan con trazabilidad: no se presentan como hashes del
código original ni como una nueva adquisición de datos.
