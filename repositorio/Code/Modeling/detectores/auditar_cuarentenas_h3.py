"""Registra las cuarentenas del Hito 3 que deben gobernar las salidas de 4.1."""

from pathlib import Path as _ProjectPath
_PROJECT_ROOT = next(p for p in _ProjectPath(__file__).resolve().parents if (p / "project.json").is_file())
import csv
import json
from pathlib import Path

HERE = (_PROJECT_ROOT / 'Data/gold/outputs/detectores')
ROOT = _PROJECT_ROOT
FILES = {
    "EPM": (_PROJECT_ROOT / 'Data/gold/outputs/cuarentena_bootstrap/EPM/cuarentena_registros.csv'),
    "CHEC": (_PROJECT_ROOT / 'Data/silver/verificaciones/trazabilidad_filas/c698-wqig_cuarentena.csv'),
    "SSPD": (_PROJECT_ROOT / 'Data/silver/verificaciones/trazabilidad_filas/ebby-cjha_cuarentena.csv'),
    "XM": (_PROJECT_ROOT / 'Data/silver/verificaciones/trazabilidad_filas/c1b851_cuarentena.csv'),
}


def main():
    result = {}
    for source, path in FILES.items():
        with path.open(encoding="utf-8-sig", newline="") as handle:
            rows = list(csv.DictReader(handle))
        result[source] = {"ruta": str(path), "filas": len(rows), "reglas": sorted({row.get("regla", "") for row in rows if row.get("regla")})}
    ((_PROJECT_ROOT / 'Data/gold/outputs/detectores/auditoria_cuarentenas_h3.json')).write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print("cuarentenas_auditadas=4 filas_totales=" + str(sum(item["filas"] for item in result.values())))


if __name__ == "__main__":
    main()
