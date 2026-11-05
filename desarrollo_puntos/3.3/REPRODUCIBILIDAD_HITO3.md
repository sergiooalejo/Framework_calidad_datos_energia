# Reproducibilidad del Hito 3

## Estado de la primera versión

La primera versión de cada fuente está congelada mediante SHA-256 en
`trazabilidad/manifiesto_ejecucion.json`. El manifiesto registra archivo, tamaño, filas, columnas,
fecha de ejecución y clave de contenido. La matriz, las cartas y el bootstrap se regeneran con
los scripts existentes sin modificar los CSV fuente.

## Prueba ejecutada

Se ejecutaron consecutivamente:

```bash
python3 desarrollo_puntos/3.3/medir_matriz_oe1.py
python3 desarrollo_puntos/3.3/bootstrap_categorias.py
python3 desarrollo_puntos/3.3/trazabilidad.py
```

La ejecución produce 76 filas de matriz, 105 categorías bootstrap y un manifiesto para cuatro
archivos fuente.

## Segunda versión requerida

Todavía no se dispone de una segunda descarga real de cada portal. Por tanto, no se declara
reproducibilidad temporal ni estabilidad de las fuentes. Para cerrar este requisito debe guardarse
una segunda versión sin sobrescribir la primera, por ejemplo en `versiones/2026-11-05/`, con su
propio SHA-256 y fecha de descarga.

Si no es posible obtener una segunda descarga, el informe debe declarar que la prueba realizada es
reproducibilidad técnica sobre una versión congelada, no comparación entre descargas.

## Política de archivos

La política propuesta es UTF-8, encabezado conservado, fin de línea LF y sin modificar el contenido
original. Cualquier conversión debe generar un archivo nuevo y registrar el hash antes y después.
Esta propuesta requiere aprobación para convertirse en política oficial del proyecto.
