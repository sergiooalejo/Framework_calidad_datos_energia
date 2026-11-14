# Hito 5 · Integración del framework

Implementación vigente:

- `app_streamlit.py`: tablero y ejecución controlada de etapas.
- `run.py`: CLI, validación, pruebas y manifiestos de ejecución.
- `framework_calidad/`: API reutilizable, instalable como `framework_calidad`.

Desde `repositorio/`:

```powershell
python -m Code.hito5.run listar
python -m Code.hito5.run validar
python -m Code.hito5.run pruebas
python -m streamlit run Code/hito5/app_streamlit.py
```

Los accesos de la raíz `pipeline.py` y `app_streamlit.py` delegan en esta carpeta.
Los imports anteriores con `PYTHONPATH=Code` siguen disponibles mediante
`Code/framework_calidad/__init__.py`. Poetry instala el paquete desde esta carpeta.

Dockerfile, Compose y las dependencias permanecen en la raíz del proyecto;
Docker copia `Code/` completo e incluye la implementación reorganizada.
Datos y salidas permanecen en `Data/`; la documentación está en
`Docs/GUIA_EJECUCION_HITO5.md` y `Docs/CIERRE_HITO5.md`.

## Verificación de la reorganización

El 13 de noviembre de 2026 se verificaron:

- Las 61 pruebas existentes y tres pruebas de compatibilidad de esta carpeta.
- La validación de estructura, sintaxis y hashes de los 16 archivos de datos de entrada.
- La carga del tablero y el filtro EPM mediante Streamlit AppTest, desde ambas rutas.
- La construcción temporal del wheel y la inclusión de los ocho archivos del paquete.
- La configuración de Docker Compose. No se ejecutó el contenedor porque el motor
  de Docker no estaba disponible en la sesión.

Los experimentos completos no se recalcularon para esta reorganización.
