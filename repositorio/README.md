# Calidad de datos del sector energético colombiano

## Hito 4 corregido · CV temporal y scorecard

La comparación vigente se implementa en `Code/hito4/` y conserva el entrenamiento,
la validación cruzada y los umbrales dentro de referencia. La vigilancia y las
inyecciones se evalúan después, sin reajustar los umbrales. LOF, IF y KNN reciben
la misma geometría deduplicada de entrenamiento; se auditan los casos no interpretables.

```powershell
python pipeline.py ejecutar hito4
python pipeline.py ejecutar hito4-verificar
python pipeline.py pruebas
```

[Verificación y pendientes](Docs/VERIFICACION_HITO4.md),
[resultados preliminares](Docs/RESULTADOS_HITO4.md),
[scorecard por indicador](Data/gold/outputs/hito4/scorecard_indicadores.csv) y
[figuras PNG/SVG incluidas](Data/gold/outputs/hito4/figuras/).
El tablero prioriza estas salidas y distingue medición, umbral propuesto y aprobación.
`metricas` ejecuta ahora el protocolo vigente; `metricas-historicas` conserva el antecedente.

El contraste regulatorio incorpora seis documentos oficiales con fecha y hash,
la calibración exploratoria de X y el cotejo de componentes EPM. No se atribuye
causalidad a la mera coincidencia mensual. Las aprobaciones, evidencia externa
pendiente y precisión empírica del Hito 6 permanecen explícitas.

## Hito 3 corregido · 13 de noviembre de 2026

La implementación vigente del Hito 3 está en `Code/hito3/`. Corrige I-MR,
cuarentena por celda, bootstrap por categorías completas y R12 como Advertencia;
incluye dos capturas reales por API de EPM, CHEC y `vfjy-6fka`, y la réplica
transversal de esta última. Desde esta carpeta:

```powershell
python pipeline.py ejecutar hito3
python -B -m unittest discover -s Code/hito3 -p "test_*.py" -v
```

[Verificación y pendientes del Hito 3](Docs/VERIFICACION_HITO3.md),
[texto para actualizar el anteproyecto](Docs/ACTUALIZACION_ANTEPROYECTO_HITO3.md),
[fichas vigentes](Docs/FICHAS_FUENTES_HITO3.md),
[diferencias entre fuentes](Docs/DIFERENCIAS_FUENTES_HITO3.md) y
[notebook de réplica](HITO3_REPLICACION.ipynb).
Para obtener dos capturas adicionales sin sustituir las existentes:
`python pipeline.py ejecutar hito3-descargar`.

**El cierre integral sigue pendiente de evidencia externa:** disponibilidad/plazo
para oportunidad, catálogos/semántica autorizados, aprobación de umbrales y
responsables, e integración del texto en el anteproyecto oficial. Los experimentos
4.2–4.4 conservan su protocolo histórico y no se declaran recalculados con este Hito 3.
Las secciones siguientes describen también antecedentes de la consolidación.

Proyecto de ciencia de datos consolidado al **9 de noviembre de 2026**, con código,
datos locales, experimentos, resultados y pruebas de todas las actividades 3.1–3.7 y
4.1–4.6. Esta carpeta se puede copiar y ejecutar por separado: no necesita las carpetas
originales `desarrollo_puntos` ni `fuentes_datos`.

Los Hitos 3 y 4 cuentan con una línea base técnica. La aprobación metodológica y académica
continúa pendiente. El tablero y el contenedor están implementados; la validación externa
del Hito 6 y las aprobaciones académicas siguen pendientes.

## Organizaci?n vigente de los Hitos 5 y 6

- `Code/hito5/`: tablero (`app_streamlit.py`), CLI (`run.py`) y paquete
  reutilizable (`framework_calidad/`).
- `Code/hito6/`: generador de la muestra de validaci?n (`generar_muestra_alertas.py`)
  y entrada de ejecuci?n (`run.py`). El Hito 6 sigue parcialmente implementado.
- `app_streamlit.py` y `pipeline.py` en la ra?z conservan los comandos anteriores;
  delegan en Hito 5. `Code/framework_calidad/` mantiene los imports anteriores.
- Dockerfile y Compose permanecen en la ra?z como configuraci?n de despliegue.
  Los datos y documentos siguen en `Data/` y `Docs/`, como en los Hitos 3 y 4.

Desde `repositorio/`:

```powershell
python -m Code.hito5.run listar
python -m streamlit run Code/hito5/app_streamlit.py
python -m Code.hito6.run --help
python pipeline.py ejecutar muestra-h6
```

La ?ltima orden genera una muestra nueva y su manifiesto; conserva la muestra anterior.
Ver [organizaci?n del Hito 5](Code/hito5/README.md) y
[organizaci?n del Hito 6](Code/hito6/README.md).

## Estructura

```text
repositorio/
├── Code/
│   ├── Data_Acquisition_and_Understanding/  # Calidad, adaptadores, trazabilidad y cuarentena
│   ├── Modeling/                          # Cartas, detectores y experimentos
│   └── Evaluation/                        # Scorecard, niveles y costos
├── Code/hito5/framework_calidad/                 # API reutilizable del framework
├── Data/                                  # Capas Bronze, Silver y Gold; datos y evidencia
│   ├── bronze/datos/                      # Copias de fuentes y candidatas en revisión
│   ├── silver/                            # Agregados, catálogos y verificaciones
│   ├── gold/outputs/                      # Resultados analíticos y reportes
│   └── MEDALLION.md                       # Arquitectura y correspondencias
├── Sample_Data/                           # Diez filas por fuente, solo para inspección
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

La estructura adapta [Azure TDSP ProjectTemplate](https://github.com/Azure/Azure-TDSP-ProjectTemplate)
y organiza físicamente los archivos en las capas medallón. Los manifiestos históricos
conservan sus rutas originales y las auditorías las resuelven a sus nuevas ubicaciones.
Se mantienen Code, Docs, Data, Sample_Data y Environment. Las muestras no contienen los datasets
completos. No hay servicios de Azure ni despliegue en producción implementados.

Hay **cinco documentos de lectura principal**, contando este README y `Data/MEDALLION.md`. Los informes de texto
en Gold son salidas regenerables, no documentos de gestión adicionales. Las fichas,
decisiones y evidencia de todos los puntos originales están cubiertas en Docs y su inventario.

## Empezar

Desde esta carpeta, con Python 3.14:

```powershell
python pipeline.py validar
python pipeline.py listar
python pipeline.py ejecutar baseline
```

`validar` comprueba la estructura medallón, la sintaxis y los hashes de datos sin instalar bibliotecas externas.
`baseline` regenera trazabilidad, cuarentena, las cuatro cartas, revisión EPM, matriz,
bootstrap, scorecard y niveles/costos a partir de los datos y experimentos conservados.
Estas etapas usan la biblioteca estándar. Leen Bronze y Silver y escriben resultados Gold;
no modifican los datos de entrada. Para comparar salidas conviene guardar una copia previa.

Cada ejecución de `ejecutar` crea un manifiesto JSON en `Data/gold/outputs/ejecuciones/` con fecha UTC,
etapa, versión del paquete, semillas base realmente fijadas por el método, versión de Python y
SHA-256 de los archivos de entrada. Por ejemplo: `python pipeline.py ejecutar scorecard`. Las
semillas no se modifican desde la CLI: cada experimento conserva sus valores fijos y algunas
derivan semillas por fuente, serie o partición.

Los manifiestos anteriores que contienen `semilla: 42` registraban una declaración de la interfaz,
no necesariamente la semilla usada. Para esas ejecuciones se deben consultar los archivos de
configuración de cada método; no se modifica la evidencia histórica.

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
40 pruebas automáticas: 31 científicas, tres de compatibilidad de trazabilidad medallón y
seis de semillas, scorecard y protección de muestras.
`auditar` reconcilia los resultados de sensibilidad, métricas y
regla sistémica y actualiza sus informes de verificación/manifiestos. No reentrena modelos.
Las fechas históricas dentro de las salidas heredadas identifican su experimento original;
la validación de esta reorganización se registra en `Docs/VALIDACION.json`.

Los archivos `Environment/requirements-hito4-2.txt` y
`Environment/requirements-hito4-3-4.txt` conservan las versiones de los experimentos
originales. Deben utilizarse en entornos separados si se pretende reproducir ese
entrenamiento; pasar las auditorías locales no acredita identidad con aquellos ambientes.

## Paquete reutilizable

El paquete `Code/hito5/framework_calidad` separa responsabilidades comunes para cargar datos,
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
`Data/gold/outputs/calidad/matriz_oe1.yaml`. Allí están las ocho dimensiones, los tipos de regla, los
indicadores, las fórmulas, los umbrales propuestos, la severidad y el estado de aprobación.
El paquete expone `cargar_configuracion()` y `listar_indicadores()` para leerla sin codificar
esas decisiones directamente en Python.

## Tablero Streamlit del Hito 5

Por sugerencia del profesor, el artefacto de visualización se implementa inicialmente en
Streamlit. `app_streamlit.py` lee únicamente las salidas versionadas de `Data/gold/outputs/`: scorecard,
matriz de dimensiones, alertas sistémicas y métricas. No descarga datos, no cambia los CSV y
no recalcula los experimentos. Para ejecutarlo en un entorno separado:

```powershell
python -m venv .venv-streamlit
.venv-streamlit/Scripts/python -m pip install -r Environment/requirements-streamlit.txt
.venv-streamlit/Scripts/streamlit run app_streamlit.py
```

En Linux/macOS se sustituye `Scripts` por `bin`. El tablero es la primera vista funcional del
Hito 5. La aceptación metodológica y académica permanece pendiente.
El archivo `requirements-streamlit.txt` instala las dependencias principales para usar los
botones; para fijar también las versiones indirectas se recomienda Poetry con `poetry.lock`.

La barra lateral incluye un selector de etapas autorizadas y el botón **Ejecutar etapa**.
Permite ejecutar matriz OE1, cartas, bootstrap, detectores, métricas, scorecard y niveles/costos.
Requiere marcar la confirmación y muestra las semillas base fijadas para la etapa. La acción llama únicamente a
la etapa seleccionada de `pipeline.py`, crea el manifiesto de ejecución y actualiza sus salidas.
Después se debe pulsar `Rerun` para visualizar los nuevos resultados.

La revisión de cartas ahora tiene dos niveles: una revisión estructural comparable para EPM,
CHEC, SSPD y XM (`Data/gold/outputs/cartas/revision_cartas_fuentes.csv`) y la revisión estadística
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
las dependencias y los archivos locales de `Data/`; no descarga datos durante el arranque.
Compose conecta Gold y las verificaciones Silver con las carpetas locales para conservar los
resultados. Con `docker run --rm` sin volúmenes, las salidas nuevas se pierden al detener el contenedor.

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
- [Migración física medallón](Docs/RESULTADO_MIGRACION_MEDALLON.md): rutas, trazabilidad y pruebas.
- [Correcciones de la revisión](Docs/CORRECCIONES_REVISION.md): semillas, scorecard, muestra y limitaciones.
- [Cierre del Hito 5](Docs/CIERRE_HITO5.md): entregables terminados y pendientes académicos.
- [Plan de trabajo del Hito 6](Docs/PLAN_TRABAJO_HITO6.md): validación, hipótesis, reproducibilidad
  y sustentación.
- [Anexo de validación externa](Docs/ANEXO_VALIDACION_EXTERNA_HITO6.md): casos prioritarios y
  formato para la muestra manual de alertas.

- [Diagrama de componentes del Hito 5](Docs/DIAGRAMA_COMPONENTES_HITO5.md): flujo del artefacto,
  entradas, procesos, salidas, Streamlit y Docker.
- [Guía de ejecución del Hito 5](Docs/GUIA_EJECUCION_HITO5.md): instalación, orden de etapas,
  validación y solución de uso básico.

La bitácora inicial está en `Data/gold/outputs/incidentes/bitacora_incidentes.csv` y se visualiza en la
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
