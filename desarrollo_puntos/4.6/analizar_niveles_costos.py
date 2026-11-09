"""Genera los resultados del punto 4.6: niveles y costo computacional."""
import csv, gzip
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "desarrollo_puntos/4.6"
OUT.mkdir(parents=True, exist_ok=True)

METHODS = {
    "IMR_clasica": "IMR",
    "MAD_3.267sigma": "Z_robusto",
    "IF_p99.5": "Isolation_Forest",
    "R12_f10": "R12",
}


def level(source, category):
    parts = category.split("|")
    if source in {"EPM", "EPM_canonicas"} and parts[-1] in {"I", "II", "III", "IV"}:
        return f"Nivel_{parts[-1]}"
    if source == "CHEC" and parts[-1] in {"1", "2", "3", "4"}:
        return f"Nivel_{parts[-1]}"
    return "No_aplica"


def write_level_results():
    groups = defaultdict(lambda: {"observaciones": 0, "detecciones": 0, "series": set()})
    path = ROOT / "desarrollo_puntos/4.2/alertas_reales_detalle.csv.gz"
    with gzip.open(path, "rt", encoding="utf-8-sig", newline="") as handle:
        for row in csv.DictReader(handle):
            if row["referencia"] != "36" or row["cohorte"] != "comun":
                continue
            source = row["fuente"]
            group = level(source, row["categoria"])
            for column, method in METHODS.items():
                key = (source, group, method)
                item = groups[key]
                item["observaciones"] += 1
                item["detecciones"] += int(row[column])
                item["series"].add(row["sid"])
    fields = ["fuente", "nivel", "metodo", "series", "observaciones", "detecciones", "tasa_alerta", "interpretacion"]
    with (OUT / "resultados_por_nivel.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for (source, group, method), item in sorted(groups.items()):
            rate = item["detecciones"] / item["observaciones"] if item["observaciones"] else 0
            interpretation = "nivel explícito" if group != "No_aplica" else "sin nivel comparable en el esquema"
            writer.writerow({
                "fuente": source, "nivel": group, "metodo": method,
                "series": len(item["series"]), "observaciones": item["observaciones"],
                "detecciones": item["detecciones"], "tasa_alerta": f"{rate:.8f}",
                "interpretacion": interpretation,
            })
    return len(groups)


def write_costs():
    rows = []
    inputs = [
        ("4.2_sensibilidad", ROOT / "desarrollo_puntos/4.2/ejecuciones.csv"),
        ("4.3_metricas", ROOT / "desarrollo_puntos/4.3/ejecuciones.csv"),
    ]
    for experiment, path in inputs:
        with path.open(encoding="utf-8-sig", newline="") as handle:
            for row in csv.DictReader(handle):
                if experiment == "4.2_sensibilidad":
                    context = f"cohorte={row['cohorte']};referencia={row['referencia']}"
                    for stage in ("segundos",):
                        rows.append({"experimento": experiment, "fuente": row["fuente"], "contexto": context, "etapa": "total", "segundos": row[stage], "series": row["series"], "observaciones": row["observaciones_referencia"]})
                else:
                    for stage in ("segundos_ajuste_modelos", "segundos_puntajes", "segundos_tasa_igualada_y_bootstrap", "segundos_sorteo", "segundos_total"):
                        rows.append({"experimento": experiment, "fuente": row["fuente"], "contexto": "protocolo_4.3", "etapa": stage.replace("segundos_", ""), "segundos": row[stage], "series": row["series"], "observaciones": row["observaciones_reales"]})
    fields = ["experimento", "fuente", "contexto", "etapa", "segundos", "series", "observaciones"]
    with (OUT / "costos_computacionales.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader(); writer.writerows(rows)
    return len(rows)


def write_report(level_rows, cost_rows):
    text = f'''# Hito 4.6 · Resultados por nivel y costo computacional

Este informe completa la actividad 6 del Hito 4. El análisis separa niveles únicamente cuando
la fuente tiene un nivel explícito: EPM usa I–IV y CHEC usa los códigos 1–4. SSPD y XM se
reportan como `No_aplica` porque su esquema utilizado en este experimento no contiene un nivel
comparable. No se inventa una equivalencia para esas fuentes.

## Archivos

- `resultados_por_nivel.csv`: observaciones, detecciones y tasa de alerta por nivel y método.
- `costos_computacionales.csv`: tiempos registrados por etapa, fuente y experimento.
- `analizar_niveles_costos.py`: generación reproducible de ambos archivos.

## Protocolo de niveles

Se usa la cohorte `comun` y la referencia de 36 cambios del detalle de 4.2. Los métodos resumidos
son IMR, Z-score robusto, Isolation Forest y R12. La tasa es detecciones / observaciones; no es
una medida de exactitud y no debe confundirse con recall de errores inyectados.

Se separan los niveles para evitar que una fuente con muchas series de un solo nivel domine la
interpretación. El plan original menciona 69 series de Nivel I y 14 de niveles II–IV; esa cifra
corresponde a una variante de EPM y no se extrapola automáticamente a SSPD o XM.

## Costo computacional

Los tiempos se toman de las ejecuciones ya registradas en 4.2 y 4.3. En 4.3 se conservan las
etapas de ajuste, puntuación, tasa igualada/bootstrap, sorteo y total. En 4.2 se conserva el total
por escenario de sensibilidad. Los tiempos dependen del equipo y sirven para comparar escenarios
relativos, no como garantía de tiempo en otro computador.

## Limitaciones

- Las series dentro de una fuente pueden estar correlacionadas.
- SSPD y XM no tienen un nivel comparable en este corte.
- La variante `EPM_canonicas` es sensibilidad y no reemplaza a EPM.
- El costo por nivel no puede atribuirse causalmente a una sola variable si cambian también el
  número de series, observaciones o métodos.
- La ejecución de los scripts de 4.2–4.4 requiere numpy/pandas/scikit-learn instalados.

Filas generadas: {level_rows} por nivel/método y {cost_rows} de costo computacional.
'''
    (OUT / "INFORME_NIVELES_COSTO.md").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    n_levels = write_level_results()
    n_costs = write_costs()
    write_report(n_levels, n_costs)
    print(f"niveles={n_levels} costos={n_costs}")
