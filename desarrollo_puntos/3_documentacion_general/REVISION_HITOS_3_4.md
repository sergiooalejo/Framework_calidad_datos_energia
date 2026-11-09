# Revisión de integridad — Hitos 3 y 4

**Fecha de revisión:** 9 de noviembre de 2026  
**Alcance:** estructura del repositorio, entregables previstos en el plan detallado, enlaces locales,
reproducibilidad básica, pendientes de decisión y guía para el equipo.

## Resultado ejecutivo

Los Hitos 3 y 4 están **ordenados y documentados como línea base técnica**. Las actividades
3.1 a 3.7 y 4.1 a 4.6 tienen carpeta e índice de lectura; los resultados provisionales están
distinguidos de los resultados medidos y las decisiones metodológicas pendientes están consolidadas
en un único documento para el director.

Esto no equivale a una aprobación formal de ambos hitos. Siguen pendientes evidencia externa,
una segunda descarga independiente, definiciones metodológicas y la incorporación de los resultados
en el documento oficial de tesis.

## 1. Organización comprobada

| Bloque | Estado | Punto de entrada |
|---|---|---|
| Hito 3: 3.1 a 3.7 | Completo en estructura | [Índice del Hito 3](README.md) |
| Hito 4: 4.1 a 4.6 | Completo en estructura | [Guía, sección 15 en adelante](../../GUIA_EXPLICATIVA_PROYECTO.md) |
| Matriz OE1 | Disponible en CSV, Markdown y YAML | [3.1](../3.1/README.md) |
| Cuatro fuentes y fichas | EPM, CHEC, SSPD y XM | [3.2](../3.2/README.md) |
| Trazabilidad, cuarentena y bootstrap | Disponibles y separados de los datos fuente | [3.6](../3.6/README.md) y [3.7](../3.7/README.md) |
| Técnicas, sensibilidad, métricas, regla sistémica, scorecard y niveles | Documentados por actividad | [4.1](../4.1/README.md), [4.2](../4.2/README.md), [4.3](../4.3/README.md), [4.4](../4.4/README.md), [4.5](../4.5/README.md), [4.6](../4.6/README.md) |

No se movieron ni eliminaron datos durante esta revisión. El CSV en `fuentes_datos/datos/Datos_en_revision/`
permanece fuera del alcance de los cuatro datos seleccionados.

## 2. Verificaciones realizadas

| Verificación | Resultado | Interpretación |
|---|---|---|
| Carpetas e índices | Correcto | Existen los índices 3.1–3.7, 4.1–4.6 y el índice general de Hito 3. |
| Sintaxis de scripts Python | Correcta | Los 39 scripts revisados compilan; esto detecta errores de sintaxis, no valida por sí solo los resultados científicos. |
| Matriz OE1 | Ejecutada | Se regeneraron sus representaciones CSV, Markdown y YAML desde el script de medición. |
| Trazabilidad (3.6) | Ejecutada | Se regeneró el manifiesto de ejecución y las huellas de contenido. |
| Bootstrap (3.7) | Ejecutado | Se generaron resultados para 105 grupos fuente/categoría con semilla fija. |
| Scorecard (4.5) | Ejecutado | Se regeneró el resumen de 4 fuentes × 8 dimensiones (32 combinaciones). Sigue siendo provisional. |
| Niveles y costo (4.6) | Ejecutado | Se regeneraron 36 combinaciones fuente/nivel/método y 47 mediciones de costo. |
| Sensibilidad (4.2) | Validado | 9 pruebas correctas; verificador correcto para 22 escenarios, 39.288 observaciones y 212.497 ensayos. |
| Métricas (4.3) | Validado | 12 pruebas correctas; 720 filas de métricas, 8.328 observaciones y 43.846 casos reconciliados. |
| Regla sistémica (4.4) | Validado | 10 pruebas correctas; 1.272 fracciones mensuales, 9 variantes y 227 filas de catálogo reconciliadas. |
| Enlaces locales de la documentación | Corregidos | Las referencias a figuras no versionadas ahora indican cómo regenerarlas y apuntan a los CSV auditables. |
| Pendientes históricos de 4.1 | Corregidos | Los documentos de cierre ahora indican que las métricas e inyecciones se resolvieron en 4.2/4.3 y remiten al registro único vigente. |

## 3. Límites técnicos que no deben ocultarse

Los análisis 4.2, 4.3 y 4.4 dependen de bibliotecas científicas (`numpy`, `pandas`,
`scikit-learn` y `matplotlib`). Sus configuraciones registran las versiones usadas, pero el
repositorio no tiene todavía un `pyproject.toml` o contenedor, pero ya incluye los archivos
bloqueados [requirements-hito4-2.txt](../../requirements/requirements-hito4-2.txt) y
[requirements-hito4-3-4.txt](../../requirements/requirements-hito4-3-4.txt). Esta revisión los
reejecutó en entornos aislados con las versiones registradas
por cada actividad: 4.2 con numpy 2.3.5, pandas 2.3.3 y scikit-learn 1.8.0; 4.3–4.4 con numpy
2.5.4, pandas 2.3.3 y scikit-learn 1.9.1 (Matplotlib 3.11.2 para las figuras). En un entorno
nuevo se puede preparar esa instalación con los comandos de [requirements/README.md](../../requirements/README.md).

Las figuras de esos puntos tampoco se guardan en Git: son salidas binarias regenerables ignoradas
por diseño. Las tablas CSV, los manifiestos SHA-256 y los scripts sí permanecen disponibles. Esta
decisión evita duplicar archivos derivados, pero exige crear el entorno y ejecutar los scripts para
ver los gráficos. El empaquetado reproducible del entorno es una tarea natural del Hito 5.

## 4. Pendientes que requieren decisión o aprobación

Todo pendiente que cambia alcance, interpretación o metodología está centralizado en
[PENDIENTES_APROBACION_HITO3.md](PENDIENTES_APROBACION_HITO3.md). Incluye:

- roles, umbrales y severidad de reglas;
- catálogos y semántica de CHEC;
- muestra y fuente para exactitud; plazo o proxy para oportunidad;
- segunda versión independiente y política de codificación;
- unidad del bootstrap, R10, R12, CART01 y casos de una sola serie;
- valor X, prevalencia, método principal, etiquetas canónicas, MAD cero, LOF y Extended Isolation Forest;
- condición provisional de los resultados 4.5 y alcance de niveles en 4.6;
- evidencia regulatoria, consulta formal y la incorporación de estos resultados en el documento oficial de tesis.

Nada de esa lista debe presentarse como aprobado mientras no se complete el registro de aprobación
del mismo documento.

## 5. Conclusión operativa

El repositorio está listo para que el equipo y el director revisen decisiones y evidencia sin
perder la trazabilidad. Antes del cierre formal se debe: (1) obtener y comparar una segunda descarga,
(2) completar evidencia de exactitud y oportunidad, (3) obtener las aprobaciones registradas,
(4) integrar el contenido aprobado en la tesis y (5) preparar un entorno reproducible para los
análisis que usan bibliotecas científicas.
