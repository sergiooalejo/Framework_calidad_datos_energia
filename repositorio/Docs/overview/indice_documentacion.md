# Documentación

Para empezar: [README del proyecto](../README.md).

## Guías vigentes

- [Arquitectura y ubicación del código](../guides/arquitectura.md).
- [Instalación y reproducibilidad](../guides/reproducibilidad.md).
- [Verificación de la reorganización](../../z_findings/provenance/informe_reorganizacion.md).
- [Registro de los archivos trasladados](../../z_findings/provenance/reorganizacion_codigo.json).

## Evidencia por etapa

| Etapa | Función | Documentos |
|---|---|---|
| H3 | Reglas, cuarentena, cartas y adquisición | [Verificación](../../z_findings/reports/data_quality/verificacion.md), [fuentes](../../z_findings/reports/data_quality/fichas_fuentes.md), [diferencias](../../z_findings/reports/data_quality/diferencias_fuentes.md) |
| H4 | Comparación temporal de métodos y scorecard vigente | [Verificación](../../z_findings/reports/experiments/verificacion.md), [resultados](../../z_findings/reports/experiments/resultados.md) |
| H5 | Integración inicial de CLI y tablero | [Cierre histórico](../../z_findings/reports/interfaces/cierre_tecnico.md); la instalación actual está en las guías anteriores |
| H6 | Muestra para revisión externa pendiente | [Plan](../external_validation/plan_trabajo.md), [anexo](../external_validation/protocolo_revision.md), [verificación](../../z_findings/reports/external_validation/verificacion.md) |

## Historia y decisiones

[Decisiones](../governance/decisiones.md), [correcciones](../../z_findings/reports/correcciones_revision.md),
[referencia técnica](../../z_findings/reports/referencia_tecnica.md), [procedencia](../../z_findings/provenance/procedencia_fuentes.json)
y [migración medallón](../../z_findings/provenance/migracion.csv). Los archivos de `Antecedentes/`,
`codigo_historico/` y `evidencia_historica/` se conservan como antecedentes.

Los documentos fechados describen su entrega original. Para instalar o localizar el código
actual, use las guías vigentes; no combine requisitos históricos con el lock actual.
