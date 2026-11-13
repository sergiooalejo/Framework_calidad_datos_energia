"""Resume series con MAD cero y sus señales bajo el tratamiento conservador."""

from pathlib import Path as _ProjectPath
_PROJECT_ROOT = next(p for p in _ProjectPath(__file__).resolve().parents if (p / "project.json").is_file())
from pathlib import Path
import csv
import json

HERE = (_PROJECT_ROOT / 'Data/gold/outputs/detectores')
SUMMARY = (_PROJECT_ROOT / 'Data/gold/outputs/detectores/zscore_robusto_resumen.csv')


def main():
    with SUMMARY.open(encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    zero = [row for row in rows if row["estado_escala"] == "mad_cero"]
    result = {
        "metodo": "zscore_robusto_logaritmico",
        "tratamiento": "No se inventa una escala; se marca señal si el cambio difiere de la mediana.",
        "series_totales": len(rows),
        "series_mad_cero": len(zero),
        "señales_mad_cero": sum(int(row["señales"]) for row in zero),
        "por_fuente": {},
        "series": zero,
    }
    for source in sorted({row["fuente"] for row in zero}):
        group = [row for row in zero if row["fuente"] == source]
        result["por_fuente"][source] = {
            "series": len(group),
            "señales": sum(int(row["señales"]) for row in group),
        }
    ((_PROJECT_ROOT / 'Data/gold/outputs/detectores/auditoria_mad_cero.json')).write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"series_mad_cero={len(zero)} señales_mad_cero={result['señales_mad_cero']}")


if __name__ == "__main__":
    main()
