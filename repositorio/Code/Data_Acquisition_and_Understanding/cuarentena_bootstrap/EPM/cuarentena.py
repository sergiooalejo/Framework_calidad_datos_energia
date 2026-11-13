"""Materializa la cuarentena de EPM a partir de hallazgos del Hito 2.

Solo se apartan hallazgos que pueden contaminar una carta (R07 con Error, R08,
R11 y R12). Las filas originales permanecen intactas.
"""

from pathlib import Path as _ProjectPath
_PROJECT_ROOT = next(p for p in _ProjectPath(__file__).resolve().parents if (p / "project.json").is_file())
import csv
from pathlib import Path

ROOT = _PROJECT_ROOT
src = (_PROJECT_ROOT / 'Data/silver/verificaciones/trazabilidad_filas/03_hallazgos_trazabilidad.csv')
out = (_PROJECT_ROOT / 'Data/gold/outputs/cuarentena_bootstrap/EPM/cuarentena_registros.csv')
reglas = {"R08", "R11", "R12"}
rows = []
for r in csv.DictReader(src.open(encoding="utf-8")):
    codigo = (r.get("regla") or "")[:3]
    if codigo == "R07" and r.get("severidad") == "Error": reglas.add(codigo)
    if codigo in reglas:
        rows.append({"dataset_id":"sfcd-b3ey","registro_original":r.get("registro_original",""),
                     "clave_contenido":r.get("clave_contenido",""),"regla":r.get("regla",""),
                     "severidad":r.get("severidad",""),"columna":r.get("columna",""),
                     "valor":r.get("valor",""),"estado":"cuarentena"})
with out.open("w",encoding="utf-8",newline="") as fh:
    w=csv.DictWriter(fh,fieldnames=list(rows[0]) if rows else ["dataset_id","clave_contenido"]); w.writeheader(); w.writerows(rows)
print(f"registros_en_cuarentena={len(rows)} archivo={out}")
