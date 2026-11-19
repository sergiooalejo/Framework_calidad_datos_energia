"""Muestra manual de observaciones únicas del protocolo vigente H4-v2."""
import argparse
import csv
import gzip
import hashlib
import json
import math
import random
from datetime import datetime, timezone
from pathlib import Path

ROOT = next(p for p in Path(__file__).resolve().parents if (p / "configs/proyecto.json").is_file())
import sys
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
from Code.trazabilidad_evidencia import matches_evidence, resolve_current_path
INPUT = ROOT / "z_findings/results/experiments/puntajes_reales.csv.gz"
CALIBRATION = ROOT / "z_findings/results/experiments/calibracion.csv"
H4_MANIFEST = ROOT / "z_findings/results/experiments/manifiesto.json"
OUTPUT = ROOT / "z_findings/results/external_validation/muestra_alertas_h4_v2_epm_50.csv"
PROTOCOL = "H4-v2-CV-temporal"
METHODS = ("IMR", "Z_robusto", "IF", "LOF", "KNN", "R12")
REFERENCE = 36
ALPHA = 0.05
QUOTAS = {"EPM": 50}


def digest(path):
    with Path(path).open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def relative(path):
    path = Path(path).resolve()
    return path.relative_to(ROOT.resolve()).as_posix() if path.is_relative_to(ROOT.resolve()) else str(path)


def verify_origin():
    """Rechaza resultados huérfanos o una línea base H4 alterada/desactualizada."""
    manifest = json.loads(H4_MANIFEST.read_text(encoding="utf-8"))
    if manifest.get("protocolo") != PROTOCOL:
        raise ValueError(f"Se requiere el protocolo {PROTOCOL}; ejecutar y verificar hito4")
    paths = {}
    for group in ("entradas", "entradas_auxiliares", "codigo"):
        paths.update(manifest[group])
    quarantine = manifest["cuarentena"]
    paths[quarantine["archivo"]] = quarantine["sha256"]
    for path in (INPUT, CALIBRATION):
        key = next((name for name in manifest["salidas"]
                    if resolve_current_path(ROOT, name).resolve() == path.resolve()), relative(path))
        if key not in manifest["salidas"]:
            raise ValueError(f"Entrada H6 no registrada en el manifiesto H4: {key}")
        paths[key] = manifest["salidas"][key]
    for name, expected in paths.items():
        path = (ROOT / name).resolve()
        if not path.is_relative_to(ROOT.resolve()) or not matches_evidence(ROOT, name, expected):
            raise ValueError(f"Línea base H4 alterada o desactualizada: {name}; ejecutar y verificar hito4")
    return manifest


def read_candidates():
    """Una unidad por fuente/serie/mes, solo escenario principal y alertas guardadas."""
    thresholds = {}
    with CALIBRATION.open(encoding="utf-8-sig", newline="") as stream:
        for row in csv.DictReader(stream):
            if int(row["referencia"]) != REFERENCE or float(row["tasa_objetivo"]) != ALPHA:
                continue
            key = row["banco"], row["metodo"]
            if key in thresholds:
                raise ValueError(f"Umbral duplicado: {key}")
            thresholds[key] = float(row["umbral"]) if row["umbral"] else None
    candidates = {source: [] for source in QUOTAS}
    seen = set()
    with gzip.open(INPUT, "rt", encoding="utf-8-sig", newline="") as stream:
        reader = csv.DictReader(stream)
        required = {"fuente", "referencia", "banco", "sid", "categoria", "medida", "periodo", "nivel"}
        required.update(f"{prefix}_{method}" for prefix in ("puntaje", "alerta") for method in METHODS)
        missing = required.difference(reader.fieldnames or [])
        if missing:
            raise ValueError(f"Faltan columnas H4 en la entrada: {sorted(missing)}")
        for row in reader:
            if row["fuente"] not in candidates or int(row["referencia"]) != REFERENCE:
                continue
            identity = row["fuente"], row["sid"], row["periodo"]
            if not all(identity) or not row["banco"] or not row["medida"]:
                raise ValueError("Observación sin identidad completa")
            if identity in seen:
                raise ValueError(f"Observación repetida en el escenario principal: {identity}")
            seen.add(identity)
            category = json.loads(row["categoria"])
            if not isinstance(category, list) or not category or not all(isinstance(c, str) for c in category):
                raise ValueError(f"Categoría H4 inválida: {identity}")
            if datetime.strptime(row["periodo"], "%Y-%m").strftime("%Y-%m") != row["periodo"]:
                raise ValueError(f"Período H4 inválido: {identity}")
            for method in METHODS:
                score = float(row[f"puntaje_{method}"])
                cut = thresholds.get((row["banco"], method))
                flag = row[f"alerta_{method}"]
                if cut is None or not math.isfinite(cut) or not math.isfinite(score) or flag not in ("0", "1"):
                    raise ValueError(f"Puntaje, umbral o bandera H4 inválidos: {identity}, {method}")
                if int(flag) != int(score > cut):
                    raise ValueError(f"Bandera no coincide con el umbral H4: {identity}, {method}")
                row[f"umbral_{method}"] = cut
            if not any(row[f"alerta_{method}"] == "1" for method in METHODS):
                continue
            row.update(id_alerta=hashlib.sha256(json.dumps(identity, ensure_ascii=False).encode()).hexdigest(),
                       serie="|".join(category), protocolo=PROTOCOL,
                       tasa_objetivo_calibracion=ALPHA, horizonte="t")
            candidates[row["fuente"]].append(row)
    return {source: sorted(rows, key=lambda r: r["id_alerta"]) for source, rows in candidates.items()}


def main(argv=None) -> Path:
    parser = argparse.ArgumentParser(description="Muestra nueva de 50 alertas EPM del H4 vigente; conserva muestras anteriores.")
    parser.add_argument("--salida", type=Path, help="Ruta nueva del CSV y su manifiesto adyacente; nunca se sobrescriben")
    args = parser.parse_args(argv)
    origin = verify_origin()
    candidates = read_candidates()
    rng = random.Random(42)
    selected = []
    for source, quota in QUOTAS.items():
        pool = candidates[source]
        if len(pool) < quota:
            raise RuntimeError(f"{source} tiene {len(pool)} observaciones únicas con alerta; se requieren {quota}. No se duplican ni sustituyen fuentes.")
        selected.extend(rng.sample(pool, quota))
    fields = ["id_muestra", "id_alerta", "fuente", "protocolo", "referencia", "tasa_objetivo_calibracion",
              "horizonte", "banco", "sid", "serie", "medida", "categoria", "nivel", "periodo"]
    fields += [f"{prefix}_{method}" for method in METHODS for prefix in ("puntaje", "umbral", "alerta")]
    fields += ["clasificacion", "evidencia_externa", "revisor", "fecha_revision", "observaciones"]
    target = args.salida or OUTPUT
    if args.salida is None and (target.exists() or target.with_suffix(".manifiesto.json").exists()):
        stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
        target = target.with_name(f"{target.stem}_{stamp}{target.suffix}")
    manifest_path = target.with_suffix(".manifiesto.json")
    if target.exists() or manifest_path.exists():
        raise FileExistsError(f"Se conserva la muestra y su manifiesto existentes: {target}")
    target.parent.mkdir(parents=True, exist_ok=True)
    with manifest_path.open("x", encoding="utf-8") as record:
        with target.open("x", encoding="utf-8-sig", newline="") as stream:
            writer = csv.DictWriter(stream, fieldnames=fields)
            writer.writeheader()
            for row in selected:
                item = {field: row.get(field, "") for field in fields}
                item.update(id_muestra=f"H6-{row['id_alerta'][:16]}", clasificacion="pendiente")
                writer.writerow(item)
        manifest = dict(protocolo_muestra="H6-H4-v2-EPM-50", generado_utc=datetime.now(timezone.utc).isoformat(),
            protocolo_origen=PROTOCOL, ejecucion_h4_utc=origin["ejecucion_utc"], semilla=42,
            referencia=REFERENCE, tasa_objetivo_calibracion=ALPHA, horizonte="t", metodos=METHODS,
            cuotas=QUOTAS, candidatos_por_fuente={s: len(rows) for s, rows in candidates.items()},
            unidad_revision="observacion_unica_fuente_sid_periodo", filas=len(selected),
            entradas={relative(p): digest(p) for p in (INPUT, CALIBRATION, H4_MANIFEST)},
            codigo={relative(Path(__file__)): digest(Path(__file__))},
            muestra=dict(archivo=relative(target), sha256=digest(target)),
            ids_seleccionados=[r["id_alerta"] for r in selected],
            alcance="50 alertas EPM del escenario principal H4; no representa todas las fuentes ni acredita errores confirmados.",
            inferencia="Revisión pendiente. Precisión por método requiere sus alertas revisadas; recall necesita también casos no alertados.",
            politica="Muestras históricas y revisiones conservadas. La tasa objetivo de calibración no es una tasa de error real.")
        json.dump(manifest, record, ensure_ascii=False, indent=2, allow_nan=False)
        record.write("\n")
    print(f"muestra={len(selected)} semilla=42 protocolo={PROTOCOL} fuente=EPM referencia={REFERENCE} archivo={target}; manifiesto={manifest_path}")
    return target


if __name__ == "__main__":
    main()
