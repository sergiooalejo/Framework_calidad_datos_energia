# 3.6 · Trazabilidad estable entre descargas

Corresponde a la actividad 6 del Hito 3: identificación por contenido, huellas de archivos,
manifiesto y comprobación de reproducibilidad.

- [trazabilidad.py](trazabilidad.py): genera claves estables, manifiesto y copias trazables
  de los hallazgos y alertas históricos de `3.3/insumos_hito2/`.
- [trazabilidad/manifiesto_ejecucion.json](trazabilidad/manifiesto_ejecucion.json):
  manifiesto conservado de la ejecución previa; no se ha sustituido por uno nuevo al moverlo.
- [REPRODUCIBILIDAD_HITO3.md](REPRODUCIBILIDAD_HITO3.md): evidencia existente y requisito
  pendiente de una segunda descarga independiente.

Las salidas de identidad por fila permanecen en
[fuentes_datos/verificaciones/trazabilidad_filas](../../fuentes_datos/verificaciones/trazabilidad_filas/README.md),
conforme a la organización previa de las verificaciones.

Desde la raíz del proyecto:

```powershell
python desarrollo_puntos/3.6/trazabilidad.py
```

La reorganización no genera descargas, fechas ni hashes nuevos de los datasets. Un
manifiesto de una copia congelada no demuestra por sí solo estabilidad entre descargas.
