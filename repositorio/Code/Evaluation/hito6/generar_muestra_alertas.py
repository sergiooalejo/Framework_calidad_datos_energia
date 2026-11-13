"""Genera una muestra reproducible de alertas para validación manual del Hito 6."""

import csv
import gzip
import random
import argparse
from datetime import datetime, timezone
from pathlib import Path

ROOT = next(p for p in Path(__file__).resolve().parents if (p / "project.json").is_file())
INPUT = ROOT / "Data/gold/outputs/sensibilidad/alertas_reales_detalle.csv.gz"
OUTPUT = ROOT / "Data/gold/outputs/hito6/muestra_alertas_50.csv"
METHODS = ("I_2.66_MRmedia", "MAD_3sigma", "IF_p99", "R12_f10")
# XM no tiene alertas reales elegibles en este corte; se distribuyen sus diez cupos
# entre SSPD y las fuentes con señales observadas, sin inventar alertas.
QUOTAS = {"EPM": 15, "CHEC": 15, "SSPD": 20}


def main(argv=None) -> Path:
    parser = argparse.ArgumentParser(description="Genera una copia nueva sin sobrescribir muestras revisadas.")
    parser.add_argument("--salida", type=Path, help="Ruta nueva del CSV; nunca se sobrescribe")
    args = parser.parse_args(argv)
    candidates = {source: [] for source in QUOTAS}
    with gzip.open(INPUT, "rt", encoding="utf-8", newline="") as stream:
        reader = csv.DictReader(stream)
        required = {"fuente", "cohorte", "referencia", "sid", "periodo", *METHODS}
        missing = required.difference(reader.fieldnames or [])
        if missing:
            raise ValueError(f"Faltan columnas en la entrada: {sorted(missing)}")
        for row in reader:
            if row.get("fuente") not in candidates:
                continue
            if not any(row.get(method, "0") == "1" for method in METHODS):
                continue
            candidates[row["fuente"]].append(row)

    rng = random.Random(42)
    selected = []
    for source, quota in QUOTAS.items():
        pool = candidates[source]
        if len(pool) < quota:
            raise RuntimeError(f"{source} tiene {len(pool)} candidatos; se requieren {quota}")
        selected.extend(rng.sample(pool, quota))

    fields = ["id_muestra", "fuente", "cohorte", "referencia", "sid", "serie", "medida", "categoria", "periodo"] + list(METHODS)
    fields += ["clasificacion", "evidencia_externa", "revisor", "fecha_revision", "observaciones"]
    target = args.salida or OUTPUT
    if args.salida is None and target.exists():
        stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
        target = target.with_name(f"{target.stem}_{stamp}{target.suffix}")
    target.parent.mkdir(parents=True, exist_ok=True)
    with target.open("x", encoding="utf-8-sig", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields)
        writer.writeheader()
        for index, row in enumerate(selected, 1):
            item = {field: row.get(field, "") for field in fields}
            item.update({"id_muestra": f"H6-{index:03d}", "clasificacion": "pendiente"})
            writer.writerow(item)
    print(f"muestra={len(selected)} semilla=42 archivo={target}; LOF no está en la entrada")
    return target


if __name__ == "__main__":
    main()
