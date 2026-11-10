# Proyecto y resultados

**Corte: 9 de noviembre de 2026.** Este documento reúne el alcance y el informe de estado
que TDSP distribuye entre Project Charter y Exit Report. Es una línea base técnica; no
declara cierre académico, aceptación del director ni despliegue en producción.

## Problema y alcance

Evaluar la calidad de registros administrativos abiertos del sector energético colombiano
mediante perfilamiento, reglas de negocio, control estadístico y detección de anomalías.
El resultado se consume como tablas de indicadores, alertas trazables y evidencia comparativa
para el equipo de investigación y el director de la maestría. El tablero es trabajo futuro.

Las fuentes principales son EPM, CHEC, SSPD ZNI y XM/SIMEM. Las fuentes en revisión,
incluidas SSPD-NR y candidatas CREG, se conservan separadas y no se incorporan a la matriz
principal. XM no es un dataset publicado por CREG. DAMA-DMBOK2 e ISO/IEC 25012 sirven
de marco conceptual; no convierten las metas propuestas del proyecto en obligaciones normativas.

| Objetivo | Evidencia disponible | Falta para cierre |
|---|---|---|
| OE1: dimensiones, métricas e indicadores | Matriz de 19 controles y scorecard | Aprobar umbrales y completar evidencia externa |
| OE2: caracterización y reglas | Fichas, perfiles, adaptadores y selección de fuentes | Validar semántica, catálogos y alcance regulatorio |
| OE3: framework | Código de preparación, cartas, detectores y evaluación | Empaquetado definitivo, contenedor y tablero |
| OE4: comparación con procedimientos tradicionales | Experimentos, sensibilidad y métricas | Validación externa, contraste de hipótesis y reproducción entre ambientes/versiones |

Roles propuestos: responsable de datos, reglas de negocio, métricas/anomalías, validación
y aprobador final. Los nombres y compromisos no están confirmados. Las propuestas, preguntas
para el profesor y registro de aprobación se conservan en [DECISIONES.md](DECISIONES.md).

## Arquitectura y correspondencia completa

`Data → Code de preparación → Code de modelado → Code de evaluación → Outputs`.
Los scripts leen copias locales y guardan sus resultados dentro de esta carpeta. Cada script
localiza la raíz mediante `project.json`, por lo que no depende del directorio de ejecución.
Las rutas absolutas del equipo original no forman parte del contrato de ejecución.

| Actividad de origen | Código en Code/ | Evidencia en Outputs/ |
|---|---|---|
| 3.1: matriz OE1 | Data_Acquisition_and_Understanding/calidad | calidad |
| 3.2: fichas y perfiles | Actividad documental; no tenía scripts propios | caracterizacion |
| 3.3: réplica y adaptadores | Data_Acquisition_and_Understanding/adaptadores | adaptadores, incluidos insumos_hito2 |
| 3.4: evaluación CREG/XM | Actividad documental; no tenía scripts propios | seleccion_fuentes |
| 3.5: cartas | Modeling/cartas, por fuente | cartas, por fuente |
| 3.6: trazabilidad | Data_Acquisition_and_Understanding/trazabilidad | trazabilidad; tablas por fila en Data/verificaciones |
| 3.7: cuarentena y bootstrap | Data_Acquisition_and_Understanding/cuarentena_bootstrap | cuarentena_bootstrap |
| Documentación general | Consolidada en Docs | organizacion: inventario histórico |
| 4.1: técnicas y calibración | Modeling/detectores | detectores |
| 4.2: sensibilidad | Modeling/sensibilidad | sensibilidad |
| 4.3: métricas | Modeling/metricas | metricas |
| 4.4: regla sistémica | Modeling/regla_sistemica | regla_sistemica, incluida evidencia externa |
| 4.5: scorecard | Evaluation/scorecard | scorecard |
| 4.6: niveles y costo | Evaluation/niveles_costos | niveles_costos |

El export histórico del notebook de Hitos 1–2 permanece en
`Code/Data_Acquisition_and_Understanding/adaptadores/insumos_hito2/`; se adapta a la entrada
local EPM fuera de Colab. No se incluye en el comando baseline porque es un antecedente con
protocolo distinto. Sus tablas originales se conservan como insumos de comparación.

## Datos, métodos e interpretación

Los datos completos están en `Data/datos/`, incluidos ZIP y fuentes en revisión. Diccionarios,
catálogos, metadatos y verificaciones acompañan a cada fuente. `Sample_Data/` contiene solo
pequeñas muestras identificadas por su procedencia; no sirve para reproducir las series largas.

La matriz aplica R01–R12 e INT01, INT02, EXA01, OPO01, MAP01, DEF01 y CART01. El YAML
conserva la especificación documental y todavía no constituye un motor genérico de reglas.
Cada control mantiene fórmula, población, numerador, denominador, unidad y aplicabilidad.
El scorecard distingue medido, provisional, proxy, no medible y no aplica: ninguno acredita
por sí mismo que el director haya aceptado el umbral.

Las técnicas implementadas incluyen cartas en cambios logarítmicos, Z robusto, Isolation
Forest, LOF, KNN y R12. Cada experimento conserva su protocolo y configuración: los
primeros scripts de cartas son antecedentes preliminares y no deben interpretarse como
implementaciones idénticas de los experimentos posteriores. La consolidación conserva
las fórmulas existentes; modifica ubicación, rutas e imports.

La referencia/vigilancia, los errores inyectados y la tasa de alerta igualada permiten
comparar métodos dentro del protocolo. El bootstrap 3.7 remuestrea series dentro de
fuente/categoría; los experimentos posteriores documentan sus propias unidades y repeticiones.
No se sustituyen unos intervalos por otros. Una señal o un candidato sistémico no prueba error
ni causa regulatoria. R12/CART01 siguen sujetos a calibración e interpretación.

EXA01 necesita contraste documental: CHEC tiene una referencia externa preparada de 108
registros, pero no equivale a una muestra aprobada fila a fila. OPO01 requiere disponibilidad
frente a plazo; la fecha de descarga no es fecha de publicación. XM dispone de fechas declaradas
para 60 de 61 versiones mensuales, con plazo aún pendiente. Las propuestas de muestra de 30
registros por fuente (EXA01) y 50 alertas (validación final) responden a objetivos diferentes.

## Resultados conservados

| Producto | Cobertura registrada |
|---|---|
| Matriz OE1 | 76 registros: 19 controles × 4 fuentes |
| Bootstrap 3.7 | 105 grupos fuente/categoría; 2.000 repeticiones y semilla fija |
| Sensibilidad 4.2 | 22 escenarios, 39.288 observaciones y 212.497 ensayos |
| Métricas 4.3 | 720 filas, 8.328 observaciones y 43.846 casos |
| Regla sistémica 4.4 | 1.272 fracciones mensuales, 9 variantes y 227 filas de catálogo |
| Scorecard 4.5 | 32 combinaciones fuente/dimensión, provisionales |
| Niveles/costos 4.6 | 36 combinaciones y 47 mediciones de costo |

Resultados numéricos, PDF, CSV comprimidos y evidencia original se trasladan sin recalcular
los experimentos de entrenamiento. Las configuraciones con rutas y hashes de código se adaptan
a esta estructura: [MIGRACION.csv](MIGRACION.csv) registra las huellas antes/después y distingue
copia íntegra, adaptación y consolidación. Esto es trazabilidad de migración, no una nueva
descarga ni evidencia de estabilidad temporal del portal.

La verificación de esta entrega ejecutó los doce scripts de la línea base y conservó
los indicadores. La matriz cambia únicamente su fecha de medición. El resumen de costos
4.6 original no coincidía con los tiempos de las tablas de ejecución 4.2/4.3: el nuevo
resumen se deriva de esas tablas, sin interpretar sus segundos como un benchmark nuevo.
Las configuraciones originales se preservan en [PROCEDENCIA.json](PROCEDENCIA.json), y
las pruebas y auditorías de la copia autónoma se registran en [VALIDACION.json](VALIDACION.json).

Los intervalos de categorías con una sola serie son descriptivos/degenerados. LOF en CHEC
presenta degeneración por duplicados. Precisión/F1 dependen de prevalencias supuestas
(1 %, 5 % y 10 %). X = 25 % es una propuesta exploratoria; la regla puede enmascarar errores
masivos. Las etiquetas canónicas EPM y la comparabilidad de niveles requieren conservar sus
límites: SSPD y XM no tienen niveles equivalentes a los de EPM/CHEC.

## Plan y aceptación

1. **Hitos 3–4:** completar evidencia externa, segunda descarga, decisiones de catálogos,
   responsables, umbrales, unidades estadísticas y técnica principal. Incorporar resultados
   y cambios metodológicos en el documento oficial de tesis. Las implementaciones ya existen.
2. **Hito 5:** formalizar paquete y configuración ejecutable de reglas, fijar entorno de
   entrenamiento definitivo, contenedor, tablero y bitácora de incidentes. La CLI local de
   esta entrega facilita la ejecución; no certifica que todo el Hito 5 esté terminado.
3. **Hito 6:** contrastar alertas y causas con evidencia externa, evaluar H1 o reformularla
   con fundamento, medir reproducción en ambientes y descargas independientes, entregar
   documento final y sustentación con evidencia por objetivo.

No hay fechas nuevas comprometidas ni aprobaciones inferidas. La aceptación final exige
responsables confirmados, criterios aprobados y evidencia que cierre cada objetivo.

## Documentación técnica

[REFERENCIA_TECNICA.md](REFERENCIA_TECNICA.md) reúne fichas, informes, definiciones, procedimientos
y antecedentes con índice y procedencia. Las secciones históricas se mantienen como evidencia;
este documento y el registro de decisiones definen la lectura vigente. Los informes que los
scripts regeneran permanecen en Outputs como artefactos, separados de la documentación de gestión.

Estructura adaptada de [Azure TDSP ProjectTemplate](https://github.com/Azure/Azure-TDSP-ProjectTemplate):
Code y Docs se conservan; Evaluation, Data, Outputs y Environment explicitan las necesidades
de este proyecto. Sample_Data se reserva para muestras pequeñas como indica la plantilla.
No se incorporan servicios Azure ni se declara un despliegue que todavía no existe.
