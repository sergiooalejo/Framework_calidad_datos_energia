"""Construye trazabilidad estable para las cuatro fuentes seleccionadas.

La posición de una fila solo se conserva como referencia de lectura. La identidad
reproducible es `clave_contenido`, calculada sobre el contenido canónico de la fila,
y `id_fila_estable`, que añade la ocurrencia ordenada cuando existen copias exactas.
"""

from pathlib import Path as _ProjectPath
_PROJECT_ROOT = next(p for p in _ProjectPath(__file__).resolve().parents if (p / "project.json").is_file())
import csv, hashlib, json
from datetime import datetime, timezone
from pathlib import Path

ROOT = _PROJECT_ROOT
DATA = (_PROJECT_ROOT / 'Data/bronze/datos/Datos_seleccionados')
OUT = (_PROJECT_ROOT / 'Data/silver/verificaciones/trazabilidad_filas')
MANIFEST = (_PROJECT_ROOT / 'Data/gold/outputs/trazabilidad/trazabilidad/manifiesto_ejecucion.json')

FILES = {
    "sfcd-b3ey": (_PROJECT_ROOT / 'Data/bronze/datos/Datos_seleccionados/EPM/epm_sfcd-b3ey.csv'),
    "c698-wqig": (_PROJECT_ROOT / 'Data/bronze/datos/Datos_seleccionados/CHEC/chec_c698-wqig.csv'),
    "ebby-cjha-mensual": (_PROJECT_ROOT / 'Data/silver/datos/Datos_seleccionados/SSPD/sspd_ebby-cjha_mensual.csv'),
    "c1b851-mensual": (_PROJECT_ROOT / 'Data/silver/datos/Datos_seleccionados/XM_piloto/xm_demanda_mensual_piloto.csv'),
}


def sha256(path):
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for block in iter(lambda: fh.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def row_key(row):
    payload = json.dumps(row, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def main():
    generated = datetime.now(timezone.utc).isoformat()
    OUT.mkdir(parents=True, exist_ok=True)
    (_PROJECT_ROOT / 'Data/gold/outputs/trazabilidad/trazabilidad').mkdir(parents=True, exist_ok=True)
    manifest = {"version": "1.0", "generado_utc": generated, "algoritmo": "SHA-256",
                "clave_contenido": "JSON UTF-8 canónico de todas las columnas, ordenadas por nombre",
                "archivos": []}
    for dataset_id, path in FILES.items():
        with path.open(encoding="utf-8-sig", newline="") as fh:
            reader = csv.DictReader(fh)
            rows = list(reader)
        counts = {}
        output = OUT / f"{dataset_id}_filas.csv"
        with output.open("w", encoding="utf-8", newline="") as fh:
            writer = csv.DictWriter(fh, fieldnames=["fila_posicion", "clave_contenido", "id_fila_estable"])
            writer.writeheader()
            for pos, row in enumerate(rows, start=2):
                key = row_key(row)
                occurrence = counts.get(key, 0) + 1
                counts[key] = occurrence
                writer.writerow({"fila_posicion": pos, "clave_contenido": key,
                                 "id_fila_estable": f"{dataset_id}:{key}:{occurrence}"})
        manifest["archivos"].append({
            "dataset_id": dataset_id,
            "archivo": str(path.relative_to(ROOT)),
            "sha256": sha256(path),
            "bytes": path.stat().st_size,
            "filas": len(rows),
            "columnas": len(rows[0]) if rows else 0,
            "salida_trazabilidad": str(output.relative_to(ROOT)),
            "duplicados_por_contenido": sum(v - 1 for v in counts.values() if v > 1),
        })
    # Conserva los archivos históricos del Hito 2 y crea copias enriquecidas con la
    # identidad estable. `registro_original` es posición de datos sin encabezado.
    epm_map = {}
    key_file = (_PROJECT_ROOT / 'Data/silver/verificaciones/trazabilidad_filas/sfcd-b3ey_filas.csv')
    for r in csv.DictReader(key_file.open(encoding="utf-8")):
        epm_map[int(r["fila_posicion"]) - 2] = r["clave_contenido"]
    for nombre in ("03_hallazgos", "05_alertas_imr_reales"):
        origen = (_PROJECT_ROOT / 'Data/silver/outputs/adaptadores/insumos_hito2') / f"{nombre}.csv"
        if not origen.exists():
            continue
        destino = OUT / f"{nombre}_trazabilidad.csv"
        with origen.open(encoding="utf-8-sig", newline="") as fi:
            reader = csv.DictReader(fi); campos = list(reader.fieldnames or [])
            with destino.open("w", encoding="utf-8", newline="") as fo:
                writer = csv.DictWriter(fo, fieldnames=campos + ["clave_contenido"])
                writer.writeheader()
                for row in reader:
                    try: registro = int(row.get("registro_original", ""))
                    except ValueError: registro = None
                    row["clave_contenido"] = epm_map.get(registro, "__SIN_FILA_FISICA__")
                    writer.writerow(row)
    MANIFEST.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Trazabilidad generada para {len(manifest['archivos'])} archivos: {MANIFEST}")


if __name__ == "__main__":
    main()
