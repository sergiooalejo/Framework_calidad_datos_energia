"""Registra las cuarentenas del Hito 3 que deben gobernar las salidas de 4.1."""
import csv
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
FILES = {
    "EPM": HERE.parent / "3.7/EPM/cuarentena_registros.csv",
    "CHEC": ROOT / "fuentes_datos/verificaciones/trazabilidad_filas/c698-wqig_cuarentena.csv",
    "SSPD": ROOT / "fuentes_datos/verificaciones/trazabilidad_filas/ebby-cjha_cuarentena.csv",
    "XM": ROOT / "fuentes_datos/verificaciones/trazabilidad_filas/c1b851_cuarentena.csv",
}


def main():
    result = {}
    for source, path in FILES.items():
        with path.open(encoding="utf-8-sig", newline="") as handle:
            rows = list(csv.DictReader(handle))
        result[source] = {"ruta": str(path), "filas": len(rows), "reglas": sorted({row.get("regla", "") for row in rows if row.get("regla")})}
    (HERE / "auditoria_cuarentenas_h3.json").write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print("cuarentenas_auditadas=4 filas_totales=" + str(sum(item["filas"] for item in result.values())))


if __name__ == "__main__":
    main()
