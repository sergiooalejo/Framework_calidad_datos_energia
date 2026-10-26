# Framework automatizado para la evaluación de la calidad de datos en registros administrativos del sector energético en Colombia

Trabajo de grado · Maestría en Ciencia de Datos · Facultad de Estadística · Universidad Santo Tomás

Estudiantes: Grupo 03 · Director del trabajo

## Contenido

| Carpeta | Qué hay |
|---|---|
| `codigo/` | Código entregado hasta el Hito 2 (reglas de calidad, cartas I-MR, Isolation Forest, evaluación con errores inyectados). Requiere el CSV de EPM (`sfcd-b3ey`, datos.gov.co) como `epm_tarifas.csv`. |
| `presentaciones/` | Primera presentación, Hito 1 (7 de octubre de 2026) y Hito 2 (21 de octubre de 2026). |
| `documentos/` | Anteproyecto (junio de 2026) y retroalimentación de dirección. |
| `docs/` | Revisión técnica del Hito 2, plan de hitos 3 a 6 (corto y detallado) y resumen del DAMA-DMBOK aplicado al proyecto. |

## Estado

Hito 2 entregado. El plan de los hitos 3 a 6 está en `docs/plan_hitos_3-6_detallado.md`, trazado a los cuatro objetivos específicos del anteproyecto.

## Datos

Las fuentes son abiertas (datos.gov.co): histórico de tarifas de EPM 2016–2021 (`sfcd-b3ey`) y Superservicios, subsidios, contribuciones y FOES (`vfjy-6fka`). No se versionan los CSV; el código los descarga o los lee de la carpeta de trabajo.
