"""Genera el scorecard provisional del punto 4.5 desde la matriz OE1."""

from pathlib import Path as _ProjectPath
_PROJECT_ROOT = next(p for p in _ProjectPath(__file__).resolve().parents if (p / "project.json").is_file())
import csv
from collections import defaultdict
from pathlib import Path

HERE = (_PROJECT_ROOT / 'Outputs/scorecard')
MATRIX = (_PROJECT_ROOT / 'Outputs/calidad/matriz_oe1.csv')
OUT = (_PROJECT_ROOT / 'Outputs/scorecard/scorecard_oe1_provisional.csv')


def main():
    groups = defaultdict(list)
    with MATRIX.open(encoding="utf-8-sig", newline="") as handle:
        for row in csv.DictReader(handle):
            groups[(row["fuente"], row["dimension"])].append(row)
    rows = []
    for (source, dimension), controls in sorted(groups.items()):
        states = defaultdict(int)
        for control in controls:
            states[control["estado_medicion"]] += 1
        values = [float(c["resultado_valor"]) for c in controls if c["resultado_valor"] not in ("", None)]
        rows.append({
            "fuente": source,
            "dimension": dimension,
            "controles": len(controls),
            "controles_medidos": states["medido"],
            "controles_provisionales": states["provisional"] + states["provisional_proxy"] + states["provisional_interno"],
            "controles_no_medibles": states["no_medible"],
            "controles_no_aplica": states["no_aplica"],
            "promedio_indicadores": "" if not values else f"{sum(values) / len(values):.6f}",
            "estado_scorecard": "provisional",
            "nota": "No sustituye aprobación de umbrales ni evidencia externa.",
        })
    with OUT.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    print(f"filas={len(rows)} archivo={OUT}")


if __name__ == "__main__":
    main()
