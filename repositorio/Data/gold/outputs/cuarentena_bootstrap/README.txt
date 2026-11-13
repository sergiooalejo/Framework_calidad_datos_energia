# 3.7 · Cuarentena por valor y remuestreo

Corresponde a la actividad 7 del Hito 3.

| Archivo o grupo | Función |
|---|---|
| [EPM/cuarentena.py](EPM/cuarentena.py), [cuarentena_registros.csv](EPM/cuarentena_registros.csv), [README_CUARENTENA.md](EPM/README_CUARENTENA.md) | Materialización y explicación de los registros apartados para las cartas EPM. |
| [cuarentena_fuentes.py](cuarentena_fuentes.py) | Generación conservadora de cuarentenas CHEC, SSPD y XM; escribe en las verificaciones de fuentes. |
| [bootstrap_categorias.py](bootstrap_categorias.py) | Remuestreo y cálculo de intervalos a partir de las cartas de 3.5. |
| [bootstrap/README.md](bootstrap/README.md), [resultados](bootstrap/bootstrap_categorias.csv), [configuración](bootstrap/configuracion.json) | Evidencia y parámetros del bootstrap conservado: 105 grupos, 2.000 repeticiones y semilla fija. |

Desde la raíz del proyecto:

```powershell
python desarrollo_puntos/3.7/EPM/cuarentena.py
python desarrollo_puntos/3.7/bootstrap_categorias.py
```

El material existente remuestrea **series dentro de cada categoría**; el texto del plan
original pide bootstrap **por categoría, no por serie**. La ubicación es correcta por
actividad, pero esa diferencia metodológica requiere revisión y no se resuelve cambiando
carpetas. Tampoco se modifica aquí la severidad de R12 ni la lógica de exclusión de cambios.

Los pendientes estadísticos se mantienen en
[PENDIENTES_APROBACION_HITO3.md](../3_documentacion_general/PENDIENTES_APROBACION_HITO3.md).
