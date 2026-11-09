# Hito 3 · Índice de organización

Organización por contenido realizada el 6 de noviembre de 2026. La numeración sigue las
siete actividades del Hito 3 del [plan transcrito del SVG](../../0_Recomendaciones_profesor/plan_hitos_3-6_detallado.txt),
hasta antes del Hito 4. Los documentos existentes reflejan un alcance de fuentes y algunas
decisiones posteriores a ese plan; la clasificación no modifica ni aprueba esas decisiones.

| Punto | Contenido |
|---|---|
| [3.1](../3.1/README.md) | Matriz OE1, indicadores, plantillas y evidencia de medición. |
| [3.2](../3.2/README.md) | Fichas, semántica y perfiles de caracterización de fuentes. |
| [3.3](../3.3/README.md) | Réplica, adaptadores, diferencias e insumos históricos del pipeline. |
| [3.4](../3.4/README.md) | Evidencia de selección CREG y evaluación de alternativas. |
| [3.5](../3.5/README.md) | Cartas logarítmicas y revisión de sus señales. |
| [3.6](../3.6/README.md) | Trazabilidad estable y reproducibilidad entre versiones. |
| [3.7](../3.7/README.md) | Cuarentena y remuestreo/bootstrap. |

Los documentos generales quedan aquí porque abarcan varios puntos:

- [Plan de hitos en Markdown](plan_hitos_3-6_detallado.md), que incluye también los hitos 4 a 6.
- [Documento de cierre](CIERRE_HITO3.md), con sus límites y pendientes existentes.
- [Pendientes de aprobación de Hitos 3 y 4](PENDIENTES_APROBACION_HITO3.md).
- [Referencia anterior de roles y umbrales](VALIDACION_ROLES_UMBRALES.md).
- [Contexto previo](CONTEXTO_PREVIO_HITO3.md), conservado con su contenido histórico.

La revisión cubrió los **76 archivos originales** de las carpetas que empiezan por 3:
8 en 3.1, 22 en 3.2 y 46 en 3.3; 3.4, 3.5 y 3.6 estaban vacías. Se movieron **51**
archivos y se mantuvieron 25 en su ubicación. Se añadieron índices para orientar la lectura.

El [inventario completo](INVENTARIO_ORGANIZACION.csv) registra, archivo por archivo, origen,
destino, punto asignado, motivo y SHA-256 anterior. Los CSV de datos/resultados, JSON de
evidencia y la especificación YAML se conservan íntegros. Se ajustaron rutas e imports
para mantener las dependencias, incluidos los consumidores existentes del Hito 4.

La [verificación de la organización](VERIFICACION_ORGANIZACION.md) detalla las once
ejecuciones realizadas en una copia temporal y las comprobaciones de integridad y enlaces.

La clasificación no certifica cumplimiento del Hito 3. En particular, la fuente SSPD actual
no es la del ejemplo original, la matriz incorpora oportunidad y el bootstrap existente
remuestrea series dentro de categorías. Las diferencias del plan y las aprobaciones
pendientes siguen siendo asuntos metodológicos documentados por separado.
