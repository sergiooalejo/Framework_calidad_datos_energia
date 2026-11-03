"""Indicadores de calidad por columna para epm_sfcd-b3ey.csv.

Uso:
    python medir_calidad_epm.py

Exactitud puede contrastarse con una referencia que comparta las claves:
    python medir_calidad_epm.py --reference referencia.csv --keys year,mes,tipodeinformacion,tipodetarifa,tipodedato,rangodeconsumo,nivel

Los CSV de indicadores e incidencias y el resumen JSON se guardan junto a este
script. No requiere paquetes externos.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path
from typing import Any


SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_DIR = SCRIPT_DIR.parent.parent
DEFAULT_INPUT = (
    PROJECT_DIR
    / "fuentes_datos"
    / "datos"
    / "Datos_seleccionados"
    / "epm_sfcd-b3ey.csv"
)
MISSING = {"", "na", "n/a", "null", "none"}
MONTHS = {
    "enero": 1, "febrero": 2, "marzo": 3, "abril": 4,
    "mayo": 5, "junio": 6, "julio": 7, "agosto": 8,
    "septiembre": 9, "setiembre": 9, "octubre": 10,
    "noviembre": 11, "diciembre": 12,
}
NUMERIC_FIELDS = {
    "year", "propiedadepm", "compartido", "propiedaddelcliente",
    "punta", "fueradepunta",
}
TEXT_FIELDS = {
    "tipodeinformacion", "tipodetarifa", "tipodedato", "rangodeconsumo",
    "nivel", "mes",
}
ALLOWED_VALUES = {
    "tipodeinformacion": {"monomia", "horaria"},
    "nivel": {"i", "ii", "iii", "iv"},
}
COMPOSITE_KEY = [
    "year", "mes", "tipodeinformacion", "tipodetarifa", "tipodedato",
    "rangodeconsumo", "nivel",
]


def read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open("r", encoding="utf-8-sig", newline="") as stream:
        reader = csv.DictReader(stream)
        if not reader.fieldnames:
            raise ValueError(f"El archivo no tiene encabezados: {path}")
        original_headers = reader.fieldnames
        headers = [header.strip() for header in original_headers]
        rows = [
            {header: (raw.get(original) or "") for original, header in zip(original_headers, headers)}
            for raw in reader
        ]
    return headers, rows


def is_missing(value: str) -> bool:
    return value.strip().lower() in MISSING


def parse_number(value: str) -> float | None:
    if is_missing(value):
        return None
    try:
        return float(value.replace(",", "").strip())
    except ValueError:
        return None


def month_number(value: str) -> int | None:
    normalized = value.strip().casefold()
    if normalized.isdigit():
        number = int(normalized)
        return number if 1 <= number <= 12 else None
    return MONTHS.get(normalized)


def check_validity(column: str, value: str) -> tuple[bool, str]:
    if is_missing(value):
        return False, "valor faltante"
    if column in NUMERIC_FIELDS:
        number = parse_number(value)
        if number is None:
            return False, "no es numérico"
        if column == "year":
            if not number.is_integer() or not 1900 <= number <= date.today().year + 1:
                return False, "año fuera de rango o no entero"
        return True, ""
    if column == "mes" and month_number(value) is None:
        return False, "mes no reconocido"
    if column in ALLOWED_VALUES and value.strip().casefold() not in ALLOWED_VALUES[column]:
        return False, "categoría no permitida por el catálogo configurado"
    return True, ""


def period_for_row(row: dict[str, str]) -> tuple[int, int] | None:
    year = parse_number(row.get("year", ""))
    month = month_number(row.get("mes", ""))
    if year is None or not year.is_integer() or month is None:
        return None
    return int(year), month


def percentile(values: list[float], proportion: float) -> float:
    ordered = sorted(values)
    position = (len(ordered) - 1) * proportion
    lower = int(position)
    upper = min(lower + 1, len(ordered) - 1)
    fraction = position - lower
    return ordered[lower] * (1 - fraction) + ordered[upper] * fraction


def reference_matches(
    rows: list[dict[str, str]], columns: list[str], reference_path: Path | None,
    keys: list[str],
) -> dict[str, dict[str, int]]:
    result = {column: {"matched": 0, "compared": 0} for column in columns}
    if reference_path is None:
        return result
    reference_columns, reference_rows = read_csv(reference_path)
    absent = [key for key in keys if key not in columns or key not in reference_columns]
    if absent:
        raise ValueError(f"Claves ausentes en uno de los archivos: {absent}")
    comparable = [column for column in columns if column in reference_columns and column not in keys]
    index: dict[tuple[str, ...], list[dict[str, str]]] = defaultdict(list)
    for row in reference_rows:
        key = tuple(row[column] for column in keys)
        if all(not is_missing(value) for value in key):
            index[key].append(row)
    for row in rows:
        key = tuple(row[column] for column in keys)
        candidates = index.get(key, [])
        if len(candidates) != 1:
            continue
        for column in comparable:
            left, right = row[column], candidates[0][column]
            if not is_missing(left) and not is_missing(right):
                result[column]["compared"] += 1
                result[column]["matched"] += left == right
    return result


def percentage(numerator: int, denominator: int) -> float | str:
    return round(100 * numerator / denominator, 2) if denominator else ""


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT, help="CSV de EPM")
    parser.add_argument("--reference", type=Path, help="CSV de referencia para medir exactitud")
    parser.add_argument("--keys", help="Campos clave compartidos, separados por coma; requiere --reference")
    parser.add_argument("--grace-months", type=int, default=1, help="Rezago mensual aceptable (predeterminado: 1)")
    args = parser.parse_args()
    if args.reference and not args.keys:
        parser.error("--reference requiere --keys para emparejar registros")
    if args.keys and not args.reference:
        parser.error("--keys solo se utiliza junto con --reference")
    if args.grace_months < 0:
        parser.error("--grace-months no puede ser negativo")
    if not args.input.exists():
        parser.error(f"No se encontró el CSV: {args.input}")

    columns, rows = read_csv(args.input)
    if not rows:
        parser.error("El CSV no contiene registros")
    keys = [part.strip() for part in args.keys.split(",") if part.strip()] if args.keys else []
    accuracy = reference_matches(rows, columns, args.reference, keys)

    integrity_key = [column for column in COMPOSITE_KEY if column in columns]
    key_counts = Counter(
        tuple(row[column] for column in integrity_key)
        for row in rows
        if integrity_key and all(not is_missing(row[column]) for column in integrity_key)
    )
    repeated_key_rows = sum(count for count in key_counts.values() if count > 1)
    row_counts = Counter(tuple(row[column] for column in columns) for row in rows)
    duplicate_rows = sum(count - 1 for count in row_counts.values() if count > 1)

    periods = [period for row in rows if (period := period_for_row(row)) is not None]
    latest = max(periods) if periods else None
    today = date.today()
    lag = (today.year * 12 + today.month) - (latest[0] * 12 + latest[1]) if latest else None
    is_timely = lag is not None and lag <= args.grace_months

    indicators: list[dict[str, Any]] = []
    validity_failures: list[dict[str, Any]] = []
    missing_cells: list[dict[str, Any]] = []
    for column in columns:
        values = [row[column] for row in rows]
        present = [value for value in values if not is_missing(value)]
        failures = []
        for record_number, value in enumerate(values, start=2):
            if is_missing(value):
                missing_cells.append({"registro_archivo": record_number, "columna": column,
                                      "valor": value, "dimension": "Completitud", "motivo": "valor faltante"})
                continue
            valid, reason = check_validity(column, value)
            if not valid:
                failures.append((record_number, value, reason))
                validity_failures.append({"registro_archivo": record_number, "columna": column,
                                          "valor": value, "dimension": "Validez/Razonabilidad", "motivo": reason})
        valid_count = len(present) - len(failures)

        if column in NUMERIC_FIELDS:
            numeric_values = [number for value in present if (number := parse_number(value)) is not None]
            if len(numeric_values) >= 4:
                q1, q3 = percentile(numeric_values, 0.25), percentile(numeric_values, 0.75)
                iqr = q3 - q1
                low, high = q1 - 1.5 * iqr, q3 + 1.5 * iqr
                reasonable_count = sum(low <= number <= high for number in numeric_values)
                reason_note = (f"Rango estadístico IQR [{low:.6g}, {high:.6g}]; "
                               "los extremos son alertas para revisión, no errores confirmados.")
            else:
                reasonable_count, reason_note = len(numeric_values), "No hay suficientes valores para calcular rango IQR."
            consistency_count = len(numeric_values)
            consistency_note = "Porcentaje de valores que conservan formato numérico interpretable."
        else:
            reasonable_count = valid_count
            reason_note = "Categorías no vacías y reglas de dominio configuradas; no existe catálogo externo."
            consistency_count = sum(value == value.strip() for value in present)
            canonical: dict[str, set[str]] = defaultdict(set)
            for value in present:
                canonical[re.sub(r"\s+", " ", value.strip().casefold())].add(value)
            variant_groups = sum(len(forms) > 1 for forms in canonical.values())
            consistency_note = (f"Sin espacios periféricos; {variant_groups} grupos presentan variantes de "
                                "mayúsculas/espaciado tras normalizar. No se normalizan automáticamente.")

        distinct = len(set(present))
        ref = accuracy[column]
        measures = [
            ("Exactitud", ref["matched"], ref["compared"], percentage(ref["matched"], ref["compared"]),
             "Coincidencia exacta con referencia emparejada por clave; sin --reference y --keys no es evaluable."),
            ("Validez", valid_count, len(present), percentage(valid_count, len(present)),
             f"Cumple formato y reglas de dominio configuradas; {len(failures)} incumplimientos."),
            ("Completitud", len(present), len(rows), percentage(len(present), len(rows)),
             f"Valores presentes; vacío, NA, N/A, null y none se consideran faltantes ({len(rows)-len(present)})."),
            ("Integridad", len(rows) - repeated_key_rows, len(rows), percentage(len(rows)-repeated_key_rows, len(rows)),
             f"Proxy estructural por clave compuesta disponible ({len(integrity_key)} campos); no evalúa relaciones entre tablas."),
            ("Unicidad", distinct, len(present), percentage(distinct, len(present)),
             f"Valores distintos/presentes={distinct}/{len(present)}; métrica descriptiva, una columna no necesariamente es clave."),
            ("Oportunidad", int(is_timely) if latest else 0, 1 if latest else 0,
             percentage(int(is_timely), 1) if latest else "",
             f"Indicador de actualidad del dataset aplicado a cada campo; último periodo {latest[0]:04d}-{latest[1]:02d} "
             f"si disponible, rezago={lag} meses, tolerancia={args.grace_months}."),
            ("Consistencia", consistency_count, len(present), percentage(consistency_count, len(present)), consistency_note),
            ("Razonabilidad", reasonable_count, len(present), percentage(reasonable_count, len(present)), reason_note),
        ]
        for dimension, ok, evaluated, score, note in measures:
            indicators.append({"columna": column, "registros": len(rows), "dimension": dimension,
                               "casos_conformes": ok, "casos_evaluados": evaluated,
                               "indicador_pct": score, "observacion": note})

    indicators_path = SCRIPT_DIR / "indicadores_calidad_epm_por_columna.csv"
    with indicators_path.open("w", encoding="utf-8-sig", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(indicators[0]))
        writer.writeheader()
        writer.writerows(indicators)
    incidents_path = SCRIPT_DIR / "incidencias_calidad_epm.csv"
    incident_rows = validity_failures + missing_cells + [
        {"registro_archivo": "", "columna": "*", "valor": "", "dimension": "Unicidad",
         "motivo": f"Filas duplicadas exactas adicionales: {duplicate_rows}"},
        {"registro_archivo": "", "columna": "*", "valor": "", "dimension": "Integridad",
         "motivo": f"Filas con clave compuesta repetida: {repeated_key_rows}; campos: {','.join(integrity_key)}"},
    ]
    with incidents_path.open("w", encoding="utf-8-sig", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=["registro_archivo", "columna", "valor", "dimension", "motivo"])
        writer.writeheader()
        writer.writerows(incident_rows)

    summary = {
        "archivo_entrada": str(args.input.resolve()), "filas": len(rows), "columnas": len(columns),
        "dimensiones": ["Exactitud", "Validez", "Completitud", "Integridad", "Unicidad", "Oportunidad", "Consistencia", "Razonabilidad"],
        "duplicados_exactos_adicionales": duplicate_rows,
        "filas_con_clave_compuesta_repetida": repeated_key_rows,
        "campos_clave_integridad": integrity_key,
        "ultimo_periodo": f"{latest[0]:04d}-{latest[1]:02d}" if latest else None,
        "rezago_meses": lag, "oportunidad_cumple_tolerancia": is_timely if latest else None,
        "tolerancia_rezago_meses": args.grace_months,
        "exactitud": "medida contra referencia" if args.reference else "no evaluable sin fuente de referencia",
        "nota": "Integridad, consistencia y razonabilidad se estiman con proxies descritos en los indicadores; revisar extremos estadísticos con reglas de negocio.",
    }
    summary_path = SCRIPT_DIR / "resumen_calidad_epm.json"
    summary_path.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Registros analizados: {len(rows)}; columnas: {len(columns)}")
    print(f"Indicadores: {indicators_path}\nIncidencias: {incidents_path}\nResumen: {summary_path}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError, csv.Error) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        raise SystemExit(1)
