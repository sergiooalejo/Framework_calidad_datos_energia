"""Tablero Streamlit de calidad de datos del sector energético.

Lee resultados versionados de Data/gold/outputs/ y no modifica datasets ni recalcula experimentos.
"""
from pathlib import Path
import subprocess
import sys

import pandas as pd
import streamlit as st
import yaml
ROOT = next(p for p in Path(__file__).resolve().parents if (p / "project.json").is_file())
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
from Code.hito5.run import seeds_for_stage

OUTPUTS = ROOT / "Data/gold/outputs"
RULE_CONFIG = OUTPUTS / "calidad" / "matriz_oe1.yaml"


def read_csv(relative: str) -> pd.DataFrame:
    path = OUTPUTS / relative
    if not path.exists():
        return pd.DataFrame()
    return pd.read_csv(path, encoding="utf-8-sig", low_memory=False)


@st.cache_data
def load_data(fingerprint: tuple = ()) -> dict[str, pd.DataFrame]:
    def current(new,old):
        return read_csv(new if (OUTPUTS/new).exists() else old)
    return {
        "scorecard": current("hito4/scorecard_dimensiones.csv","scorecard/scorecard_oe1_provisional.csv"),
        "matrix": current("hito4/scorecard_indicadores.csv","calidad/matriz_oe1.csv"),
        "alerts": current("hito4/catalogo_sistemico.csv","regla_sistemica/catalogo_alertas_sistemicas.csv"),
        "metrics": current("hito4/metricas.csv","metricas/metricas_globales.csv"),
        "incidents": read_csv("incidentes/bitacora_incidentes.csv"),
    }


@st.cache_data
def load_rules() -> pd.DataFrame:
    """Carga las descripciones declarativas de las reglas desde el YAML OE1."""
    if not RULE_CONFIG.exists():
        return pd.DataFrame()
    with RULE_CONFIG.open("r", encoding="utf-8") as stream:
        config = yaml.safe_load(stream) or {}
    rows = []
    for rule in config.get("indicadores", []):
        metric = rule.get("metrica", {}) or {}
        threshold = rule.get("umbral", {}) or {}
        rows.append(
            {
                "regla": rule.get("id", ""),
                "nombre": rule.get("nombre", ""),
                "dimension": rule.get("dimension", ""),
                "que_verifica": metric.get("poblacion", "") + ". " + metric.get("numerador", ""),
                "formula": metric.get("formula", ""),
                "umbral": f"{threshold.get('operador', '')} {threshold.get('valor', '')}",
                "severidad": rule.get("severidad", ""),
                "estado_umbral": threshold.get("estado", ""),
            }
        )
    return pd.DataFrame(rows)


def missing(name: str, frame: pd.DataFrame) -> bool:
    if frame.empty:
        st.warning(f"No se encontró el resultado requerido: {name}.")
        return True
    return False


st.set_page_config(page_title="Calidad de datos · Energía", page_icon="⚡", layout="wide")
st.title("Framework de calidad de datos del sector energético")
st.caption("Hito 5 · tablero Streamlit sobre resultados reproducibles de los Hitos 3 y 4")

tracked = [*sorted((OUTPUTS/"hito4").glob("*.csv")), OUTPUTS/"calidad/matriz_oe1.csv",
           OUTPUTS/"scorecard/scorecard_oe1_provisional.csv", OUTPUTS/"incidentes/bitacora_incidentes.csv"]
data = load_data(tuple((str(p),p.stat().st_mtime_ns) for p in tracked if p.exists()))
scorecard = data["scorecard"]
matrix = data["matrix"]
alerts = data["alerts"]
metrics = data["metrics"]
incidents = data["incidents"]
rules = load_rules()

with st.sidebar:
    st.header("Filtros")
    sources = sorted(scorecard["fuente"].unique()) if not scorecard.empty else []
    source = st.selectbox("Fuente", ["Todas"] + sources)
    st.divider()
    st.info("Una alerta estadística no equivale automáticamente a un error de datos.")

st.sidebar.divider()
st.sidebar.subheader("Ejecución controlada")
st.sidebar.caption("Selecciona una etapa autorizada. La ejecución puede actualizar archivos en Data/gold/outputs/.")
stages = {
    "Hito 4: comparación CV y scorecard vigentes": "hito4",
    "Verificar resultados del Hito 4": "hito4-verificar",
    "1. Trazabilidad": "trazabilidad",
    "2. Cuarentena": "cuarentena",
    "3. Cartas de control": "cartas",
    "4. Revisión de cartas por fuente": "revision-cartas",
    "5. Matriz OE1": "matriz",
    "6. Bootstrap": "bootstrap",
    "7. Z-score robusto": "zscore",
    "8. Isolation Forest": "isolation-forest",
    "9. Calibración histórica": "calibracion",
    "10. Sensibilidad histórica": "sensibilidad",
    "11. Métricas CV vigentes": "metricas",
    "12. Regla sistémica histórica": "sistemica",
    "13. Scorecard": "scorecard",
    "14. Niveles y costos": "niveles-costos",
}
stage_label = st.sidebar.selectbox("Etapa", list(stages))
stage_seeds = seeds_for_stage(stages[stage_label])
if stage_seeds:
    st.sidebar.caption("Semillas base fijas usadas por este método: " + ", ".join(f"{name} = {value}" for name, value in stage_seeds.items()) + ". Algunas se derivan por fuente, serie o partición.")
else:
    st.sidebar.caption("Esta etapa no declara una semilla base configurable.")
confirm_stage = st.sidebar.checkbox("Confirmo ejecutar la etapa seleccionada")
run_stage = st.sidebar.button("Ejecutar etapa", type="primary", disabled=not confirm_stage)

if run_stage:
    stage = stages[stage_label]
    command = [sys.executable, str(ROOT / "pipeline.py"), "ejecutar", stage]
    with st.status(f"Ejecutando {stage_label}...", expanded=True) as status:
        try:
            result = subprocess.run(
                command,
                cwd=ROOT,
                capture_output=True,
                text=True,
                encoding="utf-8",
                check=False,
            )
            if result.stdout:
                st.code(result.stdout)
            if result.returncode == 0:
                status.update(label=f"{stage_label} ejecutado correctamente", state="complete")
                st.success("Pulsa Rerun para cargar los resultados actualizados.")
                st.cache_data.clear()
            else:
                status.update(label=f"{stage_label} terminó con error", state="error")
                st.error(result.stderr or "El proceso no devolvió detalles del error.")
                if "No module named" in result.stderr:
                    st.info("Falta una biblioteca en el entorno con el que abriste el tablero. Actualiza Environment/requirements-streamlit.txt en ese entorno y reinicia Streamlit.")
        except OSError as exc:
            status.update(label="No se pudo iniciar la matriz", state="error")
            st.error(str(exc))

scorecard_view = scorecard if source == "Todas" else scorecard[scorecard["fuente"] == source]
matrix_view = matrix if source == "Todas" else matrix[matrix["fuente"] == source]

tab_summary, tab_dimensions, tab_alerts, tab_metrics, tab_incidents, tab_trace = st.tabs(
    ["Resumen", "Dimensiones", "Alertas sistémicas", "Métricas", "Incidentes", "Trazabilidad"]
)

with tab_summary:
    st.subheader("Estado general")
    if not missing("scorecard", scorecard_view):
        alerts_summary = alerts if source == "Todas" or alerts.empty else alerts[alerts["fuente"] == source]
        x25 = int((alerts_summary["sistemico_X25"] == 1).sum()) if not alerts_summary.empty else 0
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Fuentes", scorecard_view["fuente"].nunique())
        c2.metric("Combinaciones", len(scorecard_view))
        c3.metric("Dimensiones registradas", scorecard_view["dimension"].nunique())
        c4.metric("Filas de escenarios con X=25%", x25)
        st.caption("Un mismo período puede aparecer en distintos escenarios; este conteo no representa eventos únicos.")
        st.dataframe(scorecard_view, use_container_width=True, hide_index=True)

with tab_dimensions:
    st.subheader("Dimensiones DAMA-DMBOK")
    if not missing("matriz OE1", matrix_view):
        st.caption("Los indicadores se muestran por separado: no se promedian porque pueden tener sentidos y poblaciones diferentes. Una agregación requiere una metodología aprobada.")
        st.dataframe(
            matrix_view[[c for c in ("fuente", "control", "nombre", "dimension", "estado_medicion", "resultado_valor", "umbral_operador", "umbral_valor", "estado_frente_umbral", "decision_final", "resultado_nota") if c in matrix_view.columns]],
            use_container_width=True,
            hide_index=True,
        )
        st.subheader("Descripción de las reglas")
        if rules.empty:
            st.info("No se encontró el catálogo YAML de reglas.")
        else:
            selected_rule = st.selectbox("Selecciona una regla para ver su descripción", rules["regla"].tolist())
            rule = rules[rules["regla"] == selected_rule].iloc[0]
            st.markdown(f"**{rule['regla']} — {rule['nombre']}** ({rule['dimension']})")
            st.write(rule["que_verifica"])
            c1, c2, c3 = st.columns(3)
            c1.write(f"**Fórmula:** {rule['formula']}")
            c2.write(f"**Umbral:** {rule['umbral']}")
            c3.write(f"**Severidad:** {rule['severidad']}")
            st.caption(f"Estado del umbral: {rule['estado_umbral']}")

with tab_alerts:
    st.subheader("Candidatos de alerta sistémica")
    if not missing("catálogo de alertas sistémicas", alerts):
        alert_source = st.selectbox("Fuente de alertas", ["Todas"] + sorted(alerts["fuente"].unique()))
        only_x25 = st.checkbox("Mostrar solo candidatos X=25%", value=True)
        view = alerts if alert_source == "Todas" else alerts[alerts["fuente"] == alert_source]
        if only_x25:
            view = view[view["sistemico_X25"] == 1]
        st.metric("Filas mostradas", len(view))
        st.dataframe(view, use_container_width=True, hide_index=True)

with tab_metrics:
    st.subheader("Comparación de métodos")
    if not missing("métricas globales", metrics):
        metrics_source = metrics if source == "Todas" else metrics[metrics["fuente"] == source]
        method = st.selectbox("Método", ["Todos"] + sorted(metrics["metodo"].unique()))
        view = metrics_source if method == "Todos" else metrics_source[metrics_source["metodo"] == method]
        if "referencia" in view.columns and not view.empty:
            windows = sorted(view["referencia"].unique().tolist())
            reference = st.selectbox("Cambios de referencia", windows, index=windows.index(36) if 36 in windows else 0)
            view = view[view["referencia"] == reference]
            st.caption("Umbrales calibrados solo en referencia y congelados antes de vigilancia. Precisión y F1 son escenarios de prevalencia supuesta, no validación empírica. La tasa observada en vigilancia puede diferir de la tasa objetivo de calibración.")
        st.dataframe(
            view[[c for c in ("fuente", "metodo", "tasa_objetivo", "horizonte", "prevalencia_supuesta", "tasa_alerta_proxy", "recall_macro", "recall_ic95_inferior", "recall_ic95_superior", "precision_conservadora", "f1", "estado_metodo") if c in view.columns]],
            use_container_width=True,
            hide_index=True,
        )

with tab_incidents:
    st.subheader("Bitácora de incidentes")
    st.caption("Una alerta estadística no se registra como incidente confirmado hasta contar con revisión y evidencia.")
    if incidents.empty:
        st.info("La bitácora está vacía. Las alertas pendientes deben revisarse antes de registrarse.")
    else:
        incident_status = st.selectbox("Estado", ["Todos"] + sorted(incidents["estado"].dropna().unique()))
        view = incidents if incident_status == "Todos" else incidents[incidents["estado"] == incident_status]
        st.metric("Incidentes registrados", len(view))
        st.dataframe(view, use_container_width=True, hide_index=True)
        st.download_button(
            "Descargar bitácora CSV",
            data=view.to_csv(index=False).encode("utf-8-sig"),
            file_name="bitacora_incidentes.csv",
            mime="text/csv",
        )

with tab_trace:
    st.subheader("Trazabilidad y límites")
    st.success("Los resultados se leen desde Data/gold/outputs/ y conservan manifiestos SHA-256.")
    st.write("La aplicación no descarga datos, no modifica archivos fuente y no convierte una señal estadística en un error confirmado.")
    st.json({
        "raiz": str(ROOT),
        "fuentes": sources,
        "scorecard_filas": len(scorecard),
        "matriz_filas": len(matrix),
        "alertas_filas": len(alerts),
        "metricas_filas": len(metrics),
    })
