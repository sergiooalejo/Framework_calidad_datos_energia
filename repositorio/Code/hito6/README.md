# Hito 6 · Herramientas de validación

Implementación disponible:

- `generar_muestra_alertas.py`: selección reproducible de la muestra manual.
- `run.py`: entrada de ejecución como módulo.

Desde `repositorio/`:

```powershell
python -m Code.hito6.run --help
python pipeline.py ejecutar muestra-h6
```

La CLI registra un manifiesto y ejecuta el generador de esta carpeta. También se
puede usar `python -m Code.hito6.run` directamente, sin manifiesto de la CLI.
Si la muestra ya existe, el generador crea otra con fecha; no la sobrescribe.
La ruta anterior `Code/Evaluation/hito6/generar_muestra_alertas.py` conserva un
acceso de compatibilidad.

Las salidas siguen en `Data/gold/outputs/hito6/`. La validación externa, la revisión
manual y el cierre académico continúan pendientes según
`Docs/PLAN_TRABAJO_HITO6.md` y `Docs/ANEXO_VALIDACION_EXTERNA_HITO6.md`.
