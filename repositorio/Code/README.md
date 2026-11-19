# Código por responsabilidad

| Carpeta | Contenido |
|---|---|
| `data_preparation/` | Adquisición, adaptación y preparación de datos. |
| `data_quality/` | Reglas de calidad, cuarentena, cartas y controles temporales. |
| `model_development/` | Detectores, sensibilidad y experimentos de la línea base. |
| `experiments/` | Protocolo comparativo vigente con validación cruzada temporal. |
| `model_evaluation/` | Scorecard, costos y evaluación. |
| `external_validation/` | Muestra para revisión externa. |
| `interfaces/` | Entradas de consola y tablero que delegan en `src/` y `apps/`. |
| `framework_calidad/` | Compatibilidad de imports con el paquete instalable de `src/`. |

La API reutilizable está en `src/framework_calidad/`, la aplicación en `apps/`,
la configuración en `configs/` y las pruebas de integración en `tests/`.
Los números de hitos se conservan únicamente como referencias históricas de entregas y resultados.

`trazabilidad_evidencia.py` resuelve rutas históricas mediante `configs/mapa_codigo.json`.
El código anterior se conserva en un único ZIP de evidencia: no se cambiaron los manifiestos
para atribuir resultados anteriores al código reorganizado. Los auditores pueden comprobar
la evidencia original y la correspondencia con los archivos actuales.

No se ejecutaron pruebas, auditorías ni experimentos durante esta reorganización.
