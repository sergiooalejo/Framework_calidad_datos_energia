# 3.5 · Cartas en cambios logarítmicos

Corresponde a la actividad 5 del Hito 3. Conserva los scripts de cartas y sus salidas,
organizados por fuente.

| Fuente | Script | Resultado |
|---|---|---|
| EPM | [cartas_log_epm.py](EPM/cartas_log_epm.py) | [cartas_log_epm.csv](EPM/cartas_log_epm.csv) |
| CHEC | [cartas_log_chec.py](CHEC/cartas_log_chec.py) | [cartas_log_chec.csv](CHEC/cartas_log_chec.csv) |
| SSPD | [cartas_log_sspd.py](SSPD/cartas_log_sspd.py) | [cartas_log_sspd.csv](SSPD/cartas_log_sspd.csv) |
| XM | [cartas_log_xm.py](XM/cartas_log_xm.py) | [cartas_log_xm.csv](XM/cartas_log_xm.csv) |

EPM también conserva [revision_cartas_epm.py](EPM/revision_cartas_epm.py) y su
[tabla de señales](EPM/revision_senales_cartas_epm.csv). La revisión de señales tiene su
propia implementación; moverla no certifica equivalencia con el cálculo principal.

Desde la raíz del proyecto, por ejemplo:

```powershell
python desarrollo_puntos/3.5/EPM/cartas_log_epm.py
```

El script EPM lee la cuarentena de [3.7/EPM](../3.7/EPM/README_CUARENTENA.md).
Las cartas son insumo de la matriz 3.1 y del bootstrap 3.7. Las revisiones que explican
reglas y adaptaciones por fuente permanecen en [3.3](../3.3/README.md).

Esta ubicación identifica la actividad a la que pertenece el material disponible.
No acredita que estén completadas la modificación de rasgos del Isolation Forest ni
las actualizaciones del marco teórico y de la metodología exigidas por el plan.
