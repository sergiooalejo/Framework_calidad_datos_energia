# Organización física medallón

Los archivos de trabajo del repositorio están organizados en tres capas:

| Capa | Ubicación | Contenido |
|---|---|---|
| Bronze | [`bronze/datos/`](bronze/datos/) | Copias y extracciones recibidas de las fuentes seleccionadas y archivos en revisión. Una extracción filtrada no representa necesariamente el conjunto completo del portal. |
| Silver | [`silver/`](silver/) | Agregados mensuales de SSPD y XM, copia procesada de SSPD no residencial en revisión, catálogos, diccionarios, metadatos, verificaciones y adaptadores. |
| Gold | [`gold/outputs/`](gold/outputs/) | Matriz de calidad, cartas de control, detectores, métricas, scorecards, informes y evidencias del Hito 6. |

Los directorios `Datos_en_revision` contienen candidatas y documentos de diferente procedencia;
mantienen ese estado y su clasificación como origen debe revisarse antes de incorporarlos a la
investigación. El detalle SSPD es un subconjunto de una empresa, no la descarga completa del portal.
Bronze conserva las copias de entrada sin reemplazar sus valores; Silver y Gold contienen los
productos de análisis existentes, sin afirmar que toda anomalía haya sido corregida.

## Trazabilidad de las ejecuciones anteriores

Los manifiestos históricos conservan las rutas y SHA-256 que usaban al producirse. La
compatibilidad de auditoría traduce las rutas antiguas a las nuevas. Cuando una dependencia de
esos resultados fue regenerada, la auditoría busca la copia histórica en `Docs/evidencia_historica`
o `Docs/codigo_historico` y comprueba que su huella coincide con la registrada; no reemplaza la
huella histórica por la de una ejecución nueva. `Docs/evidencia_historica/MIGRACION_antes_medallon.csv`
conserva el manifiesto previo; `Docs/MIGRACION.csv` contiene los destinos actuales.
El detalle del ensayo y sus límites está en [el registro de migración](../Docs/RESULTADO_MIGRACION_MEDALLON.md).

Los comandos de ejecución registran las huellas de los archivos de `bronze/datos` y `silver/datos`
en `gold/outputs/ejecuciones`. Para verificar la instalación desde `repositorio/`:

```bash
python pipeline.py validar
python pipeline.py pruebas
python pipeline.py auditar
```

Consulte los README de cada capa y el [manifiesto medallón](medallion_manifest.json).
