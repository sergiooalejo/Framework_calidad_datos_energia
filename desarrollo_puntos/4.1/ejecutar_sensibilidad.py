"""Ejecuta el Z-score robusto en los tres umbrales del protocolo de Hito 4."""
from pathlib import Path
import csv
import json
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from zscore_robusto import evaluate, sha256  # noqa: E402


def write_csv(path, rows):
    fields = list(rows[0]) if rows else ["fuente"]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def main():
    for threshold in (2.66, 3.0, 3.267):
        target = HERE / f"resultados_umbral_{str(threshold).replace('.', '_')}"
        target.mkdir(exist_ok=True)
        details, summaries, inputs = [], [], {}
        for source in ("EPM", "CHEC", "SSPD", "XM"):
            detail, summary, input_path = evaluate(source, threshold)
            details.extend(detail)
            summaries.extend(summary)
            inputs[source] = {"ruta": str(input_path), "sha256": sha256(input_path)}
        write_csv(target / "zscore_robusto_detalle.csv", details)
        write_csv(target / "zscore_robusto_resumen.csv", summaries)
        config = {
            "metodo": "zscore_robusto_logaritmico",
            "umbral": threshold,
            "cambios_referencia": 36,
            "cambios_vigilancia": 12,
            "solo_periodos_mensuales_consecutivos": True,
            "entradas": inputs,
            "series": len(summaries),
            "observaciones_vigilancia": len(details),
            "señales": sum(int(row["señales"]) for row in summaries),
        }
        (target / "configuracion.json").write_text(json.dumps(config, ensure_ascii=False, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
