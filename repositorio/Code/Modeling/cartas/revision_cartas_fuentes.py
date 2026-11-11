"""Revisión estructural comparable de las cartas generadas por cada fuente."""

import csv
from pathlib import Path

ROOT = next(p for p in Path(__file__).resolve().parents if (p / "project.json").is_file())
SOURCES = ("EPM", "CHEC", "SSPD", "XM")
OUTPUT = ROOT / "Outputs/cartas/revision_cartas_fuentes.csv"


def inspect(source: str) -> dict[str, object]:
    path = ROOT / f"Outputs/cartas/{source}/cartas_log_{source.lower()}.csv"
    if not path.exists():
        return {"fuente": source, "estado": "sin_salida", "filas": 0, "columnas": 0, "series": 0, "periodos": 0}
    with path.open(encoding="utf-8-sig", newline="") as stream:
        rows = list(csv.DictReader(stream))
    columns = set(rows[0]) if rows else set()
    series = {r.get("serie") or r.get("id_serie") or r.get("nombre_serie") for r in rows}
    periods = {r.get("periodo") or r.get("mes") or r.get("fecha") for r in rows}
    empty = sum(1 for r in rows if not any(str(value or "").strip() for value in r.values()))
    return {
        "fuente": source,
        "estado": "revisada",
        "filas": len(rows),
        "columnas": len(columns),
        "series": len(series - {None}),
        "periodos": len(periods - {None}),
        "filas_vacias": empty,
        "archivo": str(path.relative_to(ROOT)),
        "observacion": "Revisión estructural; las señales requieren interpretación específica de la fuente.",
    }


def main() -> None:
    rows = [inspect(source) for source in SOURCES]
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    fields = sorted({key for row in rows for key in row})
    with OUTPUT.open("w", encoding="utf-8-sig", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)
    print(f"fuentes={len(rows)} archivo={OUTPUT}")


if __name__ == "__main__":
    main()
