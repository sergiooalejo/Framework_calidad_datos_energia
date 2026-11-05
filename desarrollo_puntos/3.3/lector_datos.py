# -*- coding: utf-8 -*-
"""Localiza y abre los CSV de datos, esten donde esten y comprimidos o no.

Dos cosas cambiaron fuera del control de estos scripts y conviene que no vuelvan a
romperlos:

1. La carpeta `fuentes_datos/datos` se reorganizo en subcarpetas el 2 de noviembre
   de 2026 (`Datos_seleccionados`, `Datos_en_revision`).
2. Los CSV grandes se conservan comprimidos, porque GitHub avisa sobre los 50 MB y
   bloquea sobre los 100 MB. El convenio del equipo es `<nombre>-compressed.zip`
   con el CSV adentro.

Por eso se busca por nombre y se acepta cualquiera de las dos formas. Quien lea esto
no necesita saber donde quedo el archivo ni si esta comprimido.
"""

from pathlib import Path
import csv
import io
import zipfile

RAIZ = Path(__file__).resolve().parents[2]
DATOS = RAIZ / "fuentes_datos" / "datos"


def dato(nombre):
    """Devuelve la ruta del CSV `nombre`, o la del zip que lo contiene."""
    directo = DATOS / nombre
    if directo.exists():
        return directo
    encontrados = sorted(DATOS.rglob(nombre))
    if encontrados:
        return encontrados[0]
    comprimido = nombre.replace(".csv", "-compressed.zip")
    zips = sorted(DATOS.rglob(comprimido))
    if zips:
        return zips[0]
    return directo          # que falle con el nombre esperado, no con uno inventado


def filas(nombre, encoding="utf-8"):
    """Itera los registros de `nombre` como diccionarios, venga de CSV o de zip."""
    ruta = dato(nombre)
    if ruta.suffix.lower() == ".zip":
        with zipfile.ZipFile(ruta) as z:
            interno = next((n for n in z.namelist() if n.endswith(".csv")), None)
            if interno is None:
                raise FileNotFoundError("El zip {} no contiene ningun CSV".format(ruta.name))
            with z.open(interno) as fh:
                for f in csv.DictReader(io.TextIOWrapper(fh, encoding=encoding, newline="")):
                    yield f
        return
    with open(ruta, encoding=encoding, newline="") as fh:
        for f in csv.DictReader(fh):
            yield f


def leer(nombre, encoding="utf-8"):
    """Igual que `filas`, pero devuelve la lista completa."""
    return list(filas(nombre, encoding))
