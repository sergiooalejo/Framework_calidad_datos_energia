# Informe de validación técnica · Hito 5

**Fecha de validación:** 2026-11-10  
**Proyecto:** Framework de calidad de datos del sector energético colombiano

## Comandos ejecutados

```bash
.venv-validacion/bin/python pipeline.py validar
.venv-validacion/bin/python pipeline.py pruebas
.venv-validacion/bin/python pipeline.py auditar
```

También se construyó la imagen del tablero:

```bash
docker build -t calidad-energia-streamlit .
```

## Resultados

| Comprobación | Resultado |
|---|---|
| Estructura y sintaxis | Correcta |
| Archivos mapeados | 305 |
| Scripts con sintaxis válida | 48 |
| Datos íntegros | 16 |
| Pruebas de sensibilidad | 12 correctas |
| Pruebas de métricas | 12 correctas |
| Pruebas de regla sistémica | 10 correctas |
| Filas de métricas globales | 720 |
| Observaciones reales puntuadas | 8.328 |
| Casos puntuados | 43.846 |
| Variantes calibradas | 9 |
| Filas del catálogo sistémico | 227 |
| Auditoría final | Correcta |

## Evidencia generada

- Manifiestos de ejecución en `Outputs/ejecuciones/`.
- Huellas SHA-256 en la migración y configuraciones de resultados.
- Pruebas automáticas en sensibilidad, métricas y regla sistémica.
- Imagen Docker `calidad-energia-streamlit`.
- Tablero Streamlit y bitácora de incidentes.

## Limitaciones

- Las figuras de sensibilidad se consideran regenerables.
- Los umbrales y algunas decisiones metodológicas siguen pendientes de aprobación del profesor.
- Una alerta estadística no equivale automáticamente a un incidente confirmado.
- La revisión estadística detallada de cartas se conserva como específica de EPM; para las demás
  fuentes se aplica la revisión estructural común.

