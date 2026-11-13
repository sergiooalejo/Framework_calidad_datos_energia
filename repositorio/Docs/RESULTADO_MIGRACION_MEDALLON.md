# Migración física a medallón · registro técnico

Fecha de trabajo: 13 de noviembre de 2026.

## Qué se cambió

Las copias de entrada se trasladaron a `Data/bronze/datos`; los agregados mensuales de SSPD y XM,
la copia procesada de SSPD no residencial en revisión, catálogos, diccionarios, metadatos,
verificaciones y adaptadores se ubicaron en `Data/silver`; y los resultados en `Data/gold/outputs`.
La copia SSPD de detalle contiene una sola empresa. Las fuentes en revisión conservan su estado y
deben ser evaluadas por procedencia antes de utilizarse como fuentes aprobadas.

Se actualizaron rutas del código, la aplicación, el contenedor y el mapa del proyecto. Se conservó
`Docs/evidencia_historica/MIGRACION_antes_medallon.csv` y copias identificadas de las dependencias
usadas por las auditorías anteriores. La compatibilidad solo acepta una copia histórica cuando su
SHA-256 coincide con el valor registrado; no convierte esa copia en una ejecución nueva.

Se volvió a generar el manifiesto de trazabilidad de las cuatro entradas analíticas con sus rutas y
huellas actuales. El manifiesto y las tablas de trazabilidad anteriores se conservan en
`Docs/evidencia_historica/trazabilidad`.

## Comprobaciones

- `pipeline.py validar`: 305 entradas mapeadas y 16 archivos de datos con huella verificada.
- `pipeline.py pruebas`: 31 pruebas científicas y tres de compatibilidad medallón correctas.
- `pipeline.py auditar`: resultados históricos de sensibilidad, métricas y regla sistémica correctos.
- En una copia independiente se ejecutaron la línea base, Z-score, Isolation Forest, calibración,
  sensibilidad, métricas, regla sistémica y figuras. Las cartas de las cuatro fuentes coincidieron
  en contenido con las anteriores; la matriz conservó sus 76 filas y resultados, con nueva fecha.
- Se comprobó el renderizado de Streamlit y el botón de ejecución del scorecard mediante pruebas
  automatizadas. El resto de botones no se probó individualmente en una interfaz de navegador.
- Se construyó la imagen Docker con la estructura nueva. En el contenedor pasaron la validación,
  las auditorías históricas y una prueba automatizada de renderizado de Streamlit. La imagen no
  incluye 27 figuras regenerables y la auditoría informa esa ausencia.
- Se simuló una clonación local con `core.autocrlf=true`: pasaron validación, auditorías y el
  renderizado automatizado del tablero. Se añadió `.gitattributes` para conservar los bytes de
  las entradas, el código y la evidencia histórica entre sistemas.
- Las figuras regenerables pueden tener bytes y SHA-256 diferentes por fecha, formato o entorno.
  La auditoría distingue sus ausencias o diferencias de las huellas de datos obligatorios y las
  informa expresamente; una diferencia no demuestra que la figura sea visualmente idéntica.

La verificación en un segundo computador de un integrante continúa pendiente; Docker y la simulación
de clonación local no reemplazan una prueba en Windows u otro equipo. Las decisiones académicas y
validaciones externas siguen pendientes de aprobación.
