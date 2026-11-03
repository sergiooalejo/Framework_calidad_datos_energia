"""Calcula indicadores de calidad por columna para chec_c698-wqig.csv.

Uso desde cualquier carpeta:
    python medir_calidad_chec.py

Opcionalmente se puede proporcionar una fuente de referencia para comparar
exactitud, usando una clave compartida:
    python medir_calidad_chec.py --reference ruta.csv --keys campo1,campo2

Los resultados se escriben junto a este script. Solo usa la biblioteca estándar.
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
    / "chec_c698-wqig.csv"
)
MISSING = {"", "na", "n/a", "null", "none"}
MONTHS = {
    "enero": 1,
    "febrero": 2,
    "marzo": 3,
    "abril": 4,
    "mayo": 5,
    "junio": 6,
    "julio": 7,
    "agosto": 8,
    "septiembre": 9,
    "setiembre": 9,
    "octubre": 10,
    "noviembre": 11,
    "diciembre": 12,
}

# Reglas de formato y dominio que se pueden verificar sin una tabla externa.
NUMERIC_FIELDS = {
    "costounitariotarifa_ano",
    "costounitariotarifa_mes",
    "mercado_codigo",
    "nivel_tension_codigo",
    "claseservicio_estrato",
    "costounitariotarifa_rangoconsumo",
    "costounitariotarifa_generacion",
    "costounitariotarifa_transmision",
    "costounitariotarifa_distribucion",
    "costounitariotarifa_comercializacion",
    "costounitariotarifa_perdidas",
    "costounitariotarifa_restricciones",
    "costounitariotarifa_cu",
    "costounitariotarifa_cureal",
    "costounitariotarifa_subcon",
    "costounitariotarifa_valor_tarifa",
}
NONNEGATIVE_FIELDS = NUMERIC_FIELDS - {
    "costounitariotarifa_restricciones",
    "costounitariotarifa_subcon",
}
ALLOWED_VALUES = {
    "costounitariotarifa_tipomed": {"s", "hp", "hm"},
    "nivel_tension_codigo": {"1", "2", "3", "4"},
    "costounitariotarifa_rangoconsumo": {"1", "2"},
    "costounitariotarifa_tipomercado": {"r"},
}
COMPOSITE_KEY = [
    "costounitariotarifa_ano",
    "costounitariotarifa_mes",
    "comercializador_codigo",
    "mercado_codigo",
    "costounitariotarifa_tipomed",
    "nivel_tension_codigo",
    "modalidadcobro_propiedad",
    "claseservicio_codigo",
    "claseservicio_estrato",
    "costounitariotarifa_rangoconsumo",
    "costounitariotarifa_tipomercado",
]


def read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    """Lee CSV como texto y limpia espacios de encabezados, sin alterar valores."""
    with path.open("r", encoding="utf-8-sig", newline="") as stream:
        reader = csv.DictReader(stream)
        if not reader.fieldnames:
            raise ValueError(f"El archivo no tiene encabezados: {path}")
        headers = [name.strip() for name in reader.fieldnames]
        rows = []
        for raw in reader:
            rows.append(
                {
                    # Conserva espacios para que Consistencia pueda detectarlos;
                    # las funciones de parseo y de faltantes los normalizan al evaluar.
                    header: (raw.get(original) or "")
                    for original, header in zip(reader.fieldnames, headers)
                }
            )
    return headers, rows


def is_missing(value: str) -> bool:
    return value.strip().lower() in MISSING


def parse_number(value: str) -> float | None:
    if is_missing(value):
        return None
    try:
        return float(value.replace(",", ""))
    except ValueError:
        return None


def month_number(value: str) -> int | None:
    normalized = value.strip().lower()
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
        if column == "costounitariotarifa_ano":
            year = int(number) if number.is_integer() else None
            if year is None or not 1900 <= year <= date.today().year + 1:
                return False, "año fuera de rango o no entero"
        elif column == "costounitariotarifa_mes":
            if not number.is_integer() or not 1 <= number <= 12:
                return False, "mes fuera de 1–12 o no entero"
        elif column == "nivel_tension_codigo":
            if not number.is_integer() or str(int(number)) not in ALLOWED_VALUES[column]:
                return False, "nivel de tensión no permitido"
        elif column in {"costounitariotarifa_rangoconsumo"}:
            if not number.is_integer() or str(int(number)) not in ALLOWED_VALUES[column]:
                return False, "rango de consumo no permitido"
        elif column in NONNEGATIVE_FIELDS and number < 0:
            return False, "valor negativo"
        return True, ""
    if column in ALLOWED_VALUES and value.lower() not in ALLOWED_VALUES[column]:
        return False, "categoría no permitida por el catálogo configurado"
    if column == "costounitariotarifa_ano":
        return False, "año con formato inválido"
    return True, ""


def period_for_row(row: dict[str, str], columns: list[str]) -> tuple[int, int] | None:
    year_col = next((c for c in columns if c.lower() in {"year", "ano", "año", "costounitariotarifa_ano"}), None)
    month_col = next((c for c in columns if c.lower() in {"mes", "month", "costounitariotarifa_mes"}), None)
    if not year_col or not month_col:
        return None
    try:
        year = int(float(row[year_col]))
    except (ValueError, TypeError):
        return None
    month = month_number(row[month_col])
    if month is None:
        try:
            month = int(float(row[month_col]))
        except (ValueError, TypeError):
            return None
    return (year, month) if 1 <= month <= 12 else None


def exactness_reference(
    rows: list[dict[str, str]],
    columns: list[str],
    reference_path: Path | None,
    key_columns: list[str],
) -> dict[str, dict[str, Any]]:
    """Compara valores con la referencia; sin ella, exactitud no es observable."""
    result = {column: {"matched": 0, "compared": 0} for column in columns}
    if reference_path is None:
        return result
    ref_columns, ref_rows = read_csv(reference_path)
    missing = [key for key in key_columns if key not in columns or key not in ref_columns]
    if missing:
        raise ValueError(f"Claves ausentes en uno de los archivos: {missing}")
    common = [column for column in columns if column in ref_columns and column not in key_columns]
    ref_index: dict[tuple[str, ...], list[dict[str, str]]] = defaultdict(list)
    for row in ref_rows:
        key = tuple(row[key] for key in key_columns)
        if not any(is_missing(value) for value in key):
            ref_index[key].append(row)
    for row in rows:
        key = tuple(row[key] for key in key_columns)
        matches = ref_index.get(key, [])
        if len(matches) != 1:
            continue
        ref = matches[0]
        for column in common:
            if is_missing(row[column]) or is_missing(ref[column]):
                continue
            result[column]["compared"] += 1
            if row[column] == ref[column]:
                result[column]["matched"] += 1
    return result


def pct(numerator: int, denominator: int) -> float | str:
    return round(100 * numerator / denominator, 2) if denominator else ""


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT, help="CSV de CHEC")
    parser.add_argument("--reference", type=Path, help="CSV de referencia para medir exactitud")
    parser.add_argument("--keys", help="Columnas clave compartidas, separadas por coma; requiere --reference")
    parser.add_argument("--grace-months", type=int, default=1, help="Meses de rezago aceptables para oportunidad (predeterminado: 1)")
    args = parser.parse_args()

    if args.reference and not args.keys:
        parser.error("--reference requiere --keys para emparejar los registros")
    if args.keys and not args.reference:
        parser.error("--keys solo se usa junto con --reference")
    if args.grace_months < 0:
        parser.error("--grace-months no puede ser negativo")
    if not args.input.exists():
        parser.error(f"No se encontró el CSV: {args.input}")

    columns, rows = read_csv(args.input)
    if not rows:
        parser.error("El CSV no contiene registros")
    keys = [part.strip() for part in args.keys.split(",") if part.strip()] if args.keys else []
    reference = exactness_reference(rows, columns, args.reference, keys)

    configured_key = [column for column in COMPOSITE_KEY if column in columns]
    key_counts = Counter(
        tuple(row[column] for column in configured_key)
        for row in rows
        if configured_key and not any(is_missing(row[column]) for column in configured_key)
    )
    duplicated_key_rows = sum(count for count in key_counts.values() if count > 1)
    full_row_counts = Counter(tuple(row[column] for column in columns) for row in rows)
    duplicate_rows_beyond_first = sum(count - 1 for count in full_row_counts.values() if count > 1)

    periods = [period for row in rows if (period := period_for_row(row, columns)) is not None]
    latest_period = max(periods) if periods else None
    now = date.today()
    current_month_index = now.year * 12 + now.month
    latest_month_index = latest_period[0] * 12 + latest_period[1] if latest_period else None
    lag_months = current_month_index - latest_month_index if latest_month_index else None
    timely = lag_months is not None and lag_months <= args.grace_months

    output_rows: list[dict[str, Any]] = []
    for column in columns:
        values = [row[column] for row in rows]
        present = [value for value in values if not is_missing(value)]
        missing_count = len(rows) - len(present)
        validity_failures = [
            (index, value, reason)
            for index, value in enumerate(values, start=2)
            if not is_missing(value) and not check_validity(column, value)[0]
            for reason in [check_validity(column, value)[1]]
        ]
        valid_count = len(present) - len(validity_failures)
        value_counts = Counter(present)
        repeated_value_rows = sum(count for count in value_counts.values() if count > 1)
        normalized_labels: dict[str, set[str]] = defaultdict(set)
        for value in present:
            normalized_labels[re.sub(r"\s+", " ", value.strip().casefold())].add(value)
        label_variant_groups = sum(len(variants) > 1 for variants in normalized_labels.values())

        if column in NUMERIC_FIELDS:
            consistency_ok = sum(parse_number(value) is not None for value in present)
            consistency_note = "Conformidad de formato numérico; no contrasta sistemas externos."
        else:
            consistency_ok = sum(value == value.strip() for value in present)
            consistency_note = (
                f"Espacios periféricos conformes; {label_variant_groups} grupos tienen variantes de mayúsculas/espaciado. "
                "La coincidencia normalizada es una alerta, no una corrección automática."
            )

        acc = reference[column]
        base = {"columna": column, "registros": len(rows)}
        metrics = [
            ("Exactitud", acc["matched"], acc["compared"], pct(acc["matched"], acc["compared"]),
             "Coincidencia exacta con referencia por clave; no evaluable sin --reference y --keys."),
            ("Validez", valid_count, len(present), pct(valid_count, len(present)),
             f"Cumple reglas de formato/rango configuradas; {len(validity_failures)} incumplimientos."),
            ("Completitud", len(present), len(rows), pct(len(present), len(rows)),
             f"Valores presentes; faltantes reconoce vacío, NA, N/A, null y none ({missing_count})."),
            ("Integridad", len(rows) - duplicated_key_rows, len(rows), pct(len(rows) - duplicated_key_rows, len(rows)),
             f"Integridad estructural aproximada usando clave compuesta disponible ({len(configured_key)} campos); "
             "no reemplaza integridad referencial entre tablas."),
            ("Unicidad", len(present) - (len(present) - len(value_counts)), len(present),
             pct(len(value_counts), len(present)),
             f"Indicador descriptivo: valores distintos/presentes={len(value_counts)}/{len(present)}; "
             f"{repeated_value_rows} filas contienen valores repetidos. No implica que la columna deba ser clave."),
            ("Oportunidad", int(timely) if latest_period else 0, 1 if latest_period else 0,
             pct(int(timely), 1) if latest_period else "",
             f"Indicador del periodo del dataset repetido por columna: último periodo "
             f"{latest_period[0]:04d}-{latest_period[1]:02d} si disponible; rezago={lag_months} meses; "
             f"tolerancia={args.grace_months}."),
            ("Consistencia", consistency_ok, len(present), pct(consistency_ok, len(present)), consistency_note),
            ("Razonabilidad", valid_count, len(present), pct(valid_count, len(present)),
             "Proxy de razonabilidad: rangos simples (año/mes/niveles/códigos configurados y no negatividad "
             "para componentes no ajustables); revisar alertas de negocio y extremos por contexto."),
        ]
        for dimension, numerator, denominator, score, note in metrics:
            output_rows.append({**base, "dimension": dimension, "casos_conformes": numerator,
                                "casos_evaluados": denominator, "indicador_pct": score, "observacion": note})

    indicators_path = SCRIPT_DIR / "indicadores_calidad_chec_por_columna.csv"
    with indicators_path.open("w", encoding="utf-8-sig", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(output_rows[0]))
        writer.writeheader()
        writer.writerows(output_rows)

    incidents_path = SCRIPT_DIR / "incidencias_calidad_chec.csv"
    with incidents_path.open("w", encoding="utf-8-sig", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=["registro_archivo", "columna", "valor", "dimension", "motivo"])
        writer.writeheader()
        for column in columns:
            for index, value, reason in (
                (i, v, reason)
                for i, row in enumerate(rows, start=2)
                for v in [row[column]]
                for ok, reason in [check_validity(column, v)]
                if not is_missing(v) and not ok
            ):
                writer.writerow({"registro_archivo": index, "columna": column, "valor": value,
                                 "dimension": "Validez/Razonabilidad", "motivo": reason})
        for index, row in enumerate(rows, start=2):
            if any(is_missing(row[column]) for column in columns):
                for column in columns:
                    if is_missing(row[column]):
                        writer.writerow({"registro_archivo": index, "columna": column, "valor": row[column],
                                         "dimension": "Completitud", "motivo": "valor faltante"})
        writer.writerow({"registro_archivo": "", "columna": "*", "valor": "", "dimension": "Unicidad",
                         "motivo": f"Filas duplicadas exactas adicionales: {duplicate_rows_beyond_first}"})
        writer.writerow({"registro_archivo": "", "columna": "*", "valor": "", "dimension": "Integridad",
                         "motivo": f"Filas con clave compuesta repetida: {duplicated_key_rows}; campos usados: {','.join(configured_key)}"})

    summary = {
        "archivo_entrada": str(args.input.resolve()),
        "filas": len(rows),
        "columnas": len(columns),
        "dimensiones": ["Exactitud", "Validez", "Completitud", "Integridad", "Unicidad", "Oportunidad", "Consistencia", "Razonabilidad"],
        "duplicados_exactos_adicionales": duplicate_rows_beyond_first,
        "filas_con_clave_compuesta_repetida": duplicated_key_rows,
        "campos_clave_integridad": configured_key,
        "ultimo_periodo": f"{latest_period[0]:04d}-{latest_period[1]:02d}" if latest_period else None,
        "rezago_meses": lag_months,
        "oportunidad_cumple_tolerancia": timely if latest_period else None,
        "tolerancia_rezago_meses": args.grace_months,
        "exactitud": "medida contra referencia" if args.reference else "no evaluable sin fuente de referencia",
        "nota": "Integridad es aproximada dentro del archivo; consistencia y razonabilidad usan proxies documentados en el CSV de indicadores.",
    }
    summary_path = SCRIPT_DIR / "resumen_calidad_chec.json"
    summary_path.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"Registros analizados: {len(rows)}; columnas: {len(columns)}")
    print(f"Indicadores: {indicators_path}")
    print(f"Incidencias: {incidents_path}")
    print(f"Resumen: {summary_path}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError, csv.Error) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        raise SystemExit(1)
