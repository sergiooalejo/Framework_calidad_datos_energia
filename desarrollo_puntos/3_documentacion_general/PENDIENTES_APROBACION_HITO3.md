# Pendientes de aprobación — Hito 3

Este es el documento único para registrar las decisiones metodológicas y de negocio que todavía requieren aprobación del director o del equipo. Los scripts y resultados ya ejecutados no deben modificarse hasta cerrar estas decisiones.

## Estado general

La matriz OE1, las fichas, las cartas, la trazabilidad, la cuarentena y el bootstrap ya están implementados. Permanecen pendientes las decisiones que afectan interpretación, umbrales, catálogos y evidencia externa.

## 1. Roles y gobernanza

| Decisión requerida | Propuesta inicial | Estado |
|---|---|---|
| Responsable de reglas de negocio | Persona que conoce tarifas, consumo y categorías | Pendiente de asignar nombre o cargo |
| Responsable de datos | Persona que descarga, versiona y conserva archivos | Pendiente de asignar nombre o cargo |
| Responsable de métricas y anomalías | Persona que ejecuta cartas, bootstrap y scripts | Pendiente de asignar nombre o cargo |
| Responsable de validación | Director o persona que revisa la muestra externa | Pendiente de confirmar |
| Aprobador final | Director del proyecto | Pendiente de confirmar |

## 2. Umbrales y severidad

| Grupo | Controles | Propuesta | Estado |
|---|---|---|---|
| Integridad mínima | R01–R04, R07, INT01, INT02, MAP01 | Meta de 100 % | Pendiente de aprobación |
| Completitud y consistencia | R05, R06, R08–R10, DEF01 | Meta de 100 %, reportada como tasa continua; advertencia cuando corresponda | Pendiente de aprobación |
| Exactitud | EXA01 | 100 % en la muestra validada | Pendiente de aprobar muestra y fuente |
| Oportunidad | OPO01 | Medir retraso publicación-descarga; usar proxy si no existe plazo publicado | Pendiente de aprobar plazo/proxy |
| Estadística | R11, R12, CART01 | Advertencia; no convertir señal automáticamente en error | Pendiente de calibración |

El 100 % es una meta del proyecto, no un umbral impuesto por DAMA-DMBOK ni ISO. Si el director aprueba tolerancias diferentes, deben registrarse junto con su justificación.

## 3. Catálogos y semántica de CHEC

Se debe aprobar el significado de categorías, niveles, unidades y conceptos tarifarios; el catálogo canónico y las equivalencias; la unidad de cada importe y el tratamiento de valores negativos; la clave candidata para identificar una tarifa por período; la aplicación definitiva de R08 y R09; y el responsable de mantener los catálogos.

**Estado:** análisis técnico en [DECISION_CATALOGOS_CHEC.md](../3.2/CHEC/DECISION_CATALOGOS_CHEC.md); aprobación documental pendiente.

## 4. Evidencia de exactitud

Se propone contrastar 30 registros por fuente, estratificados por período y categoría, contra una fuente oficial independiente o una publicación oficial del mismo período. Debe aprobarse la fuente, el tamaño y método de selección, los campos comparados, la tolerancia numérica y el tratamiento de diferencias por redondeo o unidad.

**Estado:** procedimiento y plantilla en [EVIDENCIA_EXACTITUD_OPORTUNIDAD.md](../3.1/EVIDENCIA_EXACTITUD_OPORTUNIDAD.md); la muestra y la fuente no están aprobadas.

## 5. Evidencia de oportunidad

Se propone registrar fecha de publicación o actualización, fecha de descarga, frecuencia esperada, retraso calculado y evidencia de la URL o metadato. Si el publicador no declara un plazo esperado, debe aprobarse el uso de un proxy y reportarse como `provisional_proxy`.

**Estado:** procedimiento en [EVIDENCIA_EXACTITUD_OPORTUNIDAD.md](../3.1/EVIDENCIA_EXACTITUD_OPORTUNIDAD.md); pendiente de aprobar el plazo o proxy por fuente.

## 6. Reproducibilidad y versiones

El criterio de cierre solicita dos descargas. Debe aprobarse obtener una segunda descarga real del portal o usar una segunda copia congelada con fecha y SHA-256 diferentes, declarando que demuestra reproducibilidad técnica pero no estabilidad temporal del portal. También debe aprobarse la política de codificación y fin de línea de los CSV.

**Estado:** procedimiento en [REPRODUCIBILIDAD_HITO3.md](../3.6/REPRODUCIBILIDAD_HITO3.md); segunda versión y política de fin de línea pendientes.

## 7. Decisiones estadísticas pendientes

- Confirmar que el bootstrap remuestrea series dentro de cada categoría y no filas individuales.
- Aceptar que XM y una categoría de SSPD tienen intervalos degenerados por contar con una sola serie.
- Confirmar que R12 y CART01 se interpretan como advertencias hasta contar con calibración de negocio o evidencia histórica suficiente.
- Confirmar si R10 seguirá medido por fila o se cambiará a celda por columna.

**Estado:** propuesta documentada; aprobación metodológica pendiente.

## Registro de aprobación

| Campo | Valor |
|---|---|
| Fecha | Pendiente |
| Director o aprobador | Pendiente |
| Participantes | Pendiente |
| Decisiones aceptadas | Pendiente |
| Cambios solicitados | Pendiente |
| Versión aprobada de la matriz | Pendiente |
| Observaciones | Pendiente |

## Texto para enviar al director

> Consolidamos en un único documento las decisiones pendientes del Hito 3: responsables, umbrales, catálogos CHEC, evidencia de exactitud y oportunidad, segunda versión para reproducibilidad y decisiones estadísticas. Solicitamos confirmar o ajustar cada propuesta y registrar la versión aprobada de la matriz OE1.
