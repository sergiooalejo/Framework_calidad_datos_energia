# Verificación funcional — 18 de noviembre de 2026

## Resultado

El framework pasó las comprobaciones locales y en Linux/Docker. Las reorganizaciones y
renombrados no provocaron fallos en las 77 pruebas existentes. Se detectó y reparó una mezcla
de resultados parciales incompatible con los manifiestos guardados. CHEC completó una captura masiva y avanzó a la segunda, que se interrumpió por duración;
no se certifica la comparación de dos capturas nuevas completas de esa fuente.

## Evidencia de las comprobaciones

| Comprobación | Resultado |
|---|---|
| Pruebas en Windows/Python 3.14.0 | 77 aprobadas; ejecutadas con unittest y pytest |
| Pruebas en Linux/Python 3.14.0, Docker | Las mismas 77 aprobadas |
| Estructura y sintaxis | 305 rutas históricas resueltas y 90 scripts válidos |
| Datos de entrada | 16 archivos del inventario histórico con hashes correctos |
| Enlaces locales a archivos | 350 revisados, sin rutas rotas antes de agregar este informe |
| Poetry | `poetry --project src check --lock` correcto |
| Paquete wheel | Construido, instalado sin dependencias en una carpeta temporal y probado fuera del árbol fuente |
| API reutilizable | CSV de ida y vuelta, resumen, perfilamiento, reglas, detectores y YAML correctos |
| Tablero Windows | Tres accesos cargados con Streamlit AppTest y filtro EPM sin excepciones |
| Tablero Linux | AppTest y filtro EPM correctos; servidor real respondió HTTP 200 y `ok` |
| Docker | Imagen construida con las dependencias de `src/poetry.lock`; contenedores de prueba aislados |
| Notebooks | Lanzamiento y replicación ejecutados sin errores en una copia temporal |

## Ejecución completa en copias temporales

Se ejecutó el flujo H3 → H4 → muestra H6, con sus verificaciones. H3 comprobó 742 series,
26 modelos IF y tres pares de capturas. H4 auditó 102 particiones temporales, 1836 umbrales,
22511 observaciones reales, 117857 casos inyectados y 1584 filas de métricas.

Las métricas, calibración, particiones, puntajes reales, puntajes de inyecciones,
182364 puntajes de calibración, resultados por tipo y dimensiones de calidad reprodujeron
la evidencia guardada con tolerancias numéricas de 1e-10/1e-12. También coincidieron los
valores numéricos de los 76 indicadores. Las fechas de medición cambian entre ejecuciones.
La muestra H6 nueva conservó los mismos 50 identificadores; las muestras originales no se sobrescribieron.

En otra copia se ejecutaron las ocho etapas de `baseline`, z-score, Isolation Forest,
calibración, sensibilidad, métricas históricas, regla sistémica y generación de figuras.
Todas terminaron con código 0. Las tres auditorías históricas posteriores también pasaron.
Las figuras regenerables pueden cambiar sus bytes por metadatos y renderizado; no se exige
igualdad binaria entre nuevas figuras y ejecuciones previas.

## Reparación realizada sin cambiar los manifiestos

Nueve archivos procedentes de ejecuciones parciales no coincidían con los hashes esperados:
la matriz de calidad CSV/YAML, cinco perfiles de fuentes y dos tablas de cartas SSPD.
Se recuperaron sus versiones originales de una copia previa, comprobando cada SHA-256
contra los manifiestos existentes. Las auditorías H3/H4 volvieron a pasar en el repositorio
original y en Docker. No se sustituyeron hashes para ocultar discrepancias.

Antes de recuperar esos archivos se conservaron sus versiones actuales y sus metadatos en:

`z_findings/archive/evidence/respaldo_antes_validacion_20261119T015928191335Z.zip`

No se modificaron el código metodológico, la configuración, el lock, los datos de entrada
ni las muestras revisadas. Las ejecuciones que regeneran resultados se realizaron en copias
temporales o contenedores sin montajes de los resultados del host.

## Servicios externos y alcance

Se descargaron las seis referencias normativas oficiales. Se completaron dos capturas reales
de EPM y dos de SSPD_PLAN, usando el descargador del framework. CHEC respondió tanto en
metadatos como en una consulta de datos. Durante la captura masiva completó una descarga
y comenzó una segunda; esta última no terminó dentro de la ventana de comprobación. Una primera prueba
secuencial fue interrumpida al superar 150 segundos; la prueba paralela también se detuvo
tras varios minutos. No se atribuye ese resultado a un error de importación o de rutas.

Las capturas de comprobación quedaron dentro de contenedores descartables. Los datos
versionados de bronze no se reemplazaron. Las API y las páginas oficiales pueden cambiar;
esta verificación describe lo observado en esta fecha.

La validación externa de las alertas y la aprobación académica siguen pendientes; las pruebas
de software no sustituyen esos procesos. Tampoco se declara ejecutado el workflow remoto de GitHub.

## Repetir la verificación

Desde `repositorio/`, con el entorno instalado:

```powershell
poetry --project src check --lock
poetry --project src run pytest -c src/pyproject.toml
poetry --project src run python scripts/verificar.py
```

Para recalcular resultados, trabajar en una copia y respetar el orden:

```powershell
python scripts/flujo_trabajo.py ejecutar hito3
python scripts/flujo_trabajo.py ejecutar hito4
python scripts/flujo_trabajo.py ejecutar muestra-h6
```

Recalcular solo una etapa previa puede invalidar los manifiestos posteriores; deben regenerarse
las etapas dependientes. Las comprobaciones de integridad deben rechazar una mezcla de versiones.
