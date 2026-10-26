"""Grupo03 · Hito 1 + Hito 2: framework de calidad de datos (tarifas EPM).
Uso: python codigo_hasta_hito2.py   (con el CSV del portal guardado como epm_tarifas.csv en la misma carpeta)
"""
try:
    from IPython.display import display
except ImportError:
    display = print

# # Framework de calidad de datos · Tarifas de energía EPM
# **Diseño e implementación de un framework automatizado para la evaluación de la calidad de datos en registros administrativos del sector energético en Colombia**
# 
# Maestría en Ciencia de Datos · Grupo 03 · Director del trabajo
# 
# Este notebook reúne los dos avances:
# 
# * **Parte 1 · Hito 1 (7 de octubre de 2026):** reglas básicas, preparación con trazabilidad y cartas I y MR sobre una serie.
# * **Parte 2 · Hito 2 (21 de octubre de 2026):** unificación de etiquetas, reglas de negocio, cartas I-MR en todas las series,
#   Isolation Forest y evaluación con errores inyectados.
# 
# Se ejecuta de principio a fin con *Entorno de ejecución → Ejecutar todas*. Al inicio pide subir el CSV de EPM
# (datos.gov.co, conjunto `sfcd-b3ey`). La Parte 2 reutiliza lo que deja la Parte 1 (`df`, `registro`, `importes_numericos`).

# # Parte 1 · Hito 1: primer flujo exploratorio

# ### 1.1 Cargar el archivo

import pandas as pd
from io import BytesIO
from pathlib import Path

try:
    from google.colab import files

    # Abre el selector para subir el CSV desde tu computador.
    subidos = files.upload()

    if len(subidos) != 1:
        raise ValueError("Selecciona únicamente el archivo CSV de EPM.")

    nombre = next(iter(subidos))
    contenido = subidos[nombre]
except ImportError:
    # Fuera de Colab: se lee el archivo de la carpeta del notebook.
    nombre = "epm_tarifas.csv"
    contenido = Path(nombre).read_bytes()

df = pd.read_csv(
    BytesIO(contenido),
    dtype="string"
)

df.columns = df.columns.str.strip()

print("Archivo cargado:", nombre)
print("Filas y columnas:", df.shape)

# ### 1.2 Reglas de calidad del Hito 1

# Copia normalizada para validaciones; df conserva el archivo original.
datos = df.apply(lambda columna: columna.str.strip())
datos = datos.replace("", pd.NA)

# Número de registro dentro del archivo, sin contar el encabezado.
registro = pd.Series(range(1, len(datos) + 1), index=datos.index)

incidencias = []
resumen = []

# 2. Función común para registrar el resultado de cada regla.
def evaluar_regla(codigo, nombre, dimension, incumple, aplica=None):
    if aplica is None:
        aplica = pd.Series(True, index=datos.index)

    aplica = aplica.fillna(False)
    incumple = incumple.fillna(False) & aplica

    evaluados = int(aplica.sum())
    fallos = int(incumple.sum())

    resumen.append({
        "regla": codigo,
        "nombre": nombre,
        "dimension": dimension,
        "evaluados": evaluados,
        "incumplen": fallos,
        "cumplimiento_pct": (
            round(100 * (evaluados - fallos) / evaluados, 2)
            if evaluados else None
        )
    })

    if fallos:
        detalle = df.loc[incumple].copy()
        detalle.insert(0, "registro", registro.loc[incumple])
        detalle.insert(1, "regla", codigo)
        detalle.insert(2, "motivo", nombre)
        incidencias.append(detalle)

# 3. R01: año y mes obligatorios.
periodo_incompleto = datos[["Año", "Mes"]].isna().any(axis=1)

evaluar_regla(
    "R01",
    "Año o mes ausente",
    "Completitud",
    periodo_incompleto
)

# 4. R02: año numérico entero.
anio = pd.to_numeric(datos["Año"], errors="coerce")

anio_invalido = anio.isna() | anio.mod(1).ne(0)

evaluar_regla(
    "R02",
    "Año no interpretable como entero",
    "Validez",
    anio_invalido,
    aplica=datos["Año"].notna()
)

# 5. R03: mes reconocido.
meses = {
    "enero": 1, "febrero": 2, "marzo": 3,
    "abril": 4, "mayo": 5, "junio": 6,
    "julio": 7, "agosto": 8, "septiembre": 9,
    "octubre": 10, "noviembre": 11, "diciembre": 12
}

mes_numero = datos["Mes"].str.casefold().map(meses)

evaluar_regla(
    "R03",
    "Nombre de mes no reconocido",
    "Validez",
    mes_numero.isna(),
    aplica=datos["Mes"].notna()
)

# 6. R04: formato monetario colombiano.
columnas_importe = [
    "Propiedad Epm",
    "Compartido",
    "Propiedad del Cliente",
    "Punta",
    "Fuera de Punta"
]

# Acepta ejemplos como:
# $684,23 | $1.234,56 | 0 | -$100,00 | $-100,00
patron = r"(?:-?\$?|\$-)(?:\d{1,3}(?:\.\d{3})+|\d+)(?:,\d{1,2})?"

# Hito 2: la descarga por API trae los importes como 684.23 (punto decimal, sin $).
# Se acepta ese formato y se convierte sin cambiar el punto por coma.
patron_simple = r"-?\d+(?:\.\d+)?"

importes_numericos = pd.DataFrame(index=datos.index)

for columna in columnas_importe:
    texto = datos[columna]
    es_simple = texto.str.fullmatch(patron_simple, na=False)
    formato_valido = texto.str.fullmatch(patron, na=False) | es_simple

    evaluar_regla(
        f"R04_{columna}",
        f"Formato monetario inválido: {columna}",
        "Validez",
        ~formato_valido,
        aplica=texto.notna()
    )

    normalizado = (
        texto.where(formato_valido)
        .str.replace("$", "", regex=False)
        .str.replace(".", "", regex=False)
        .str.replace(",", ".", regex=False)
    )

    normalizado = normalizado.where(~es_simple, texto)

    importes_numericos[columna] = pd.to_numeric(
        normalizado, errors="coerce"
    )

# 7. R05: duplicados exactos del archivo original.
# Marcamos TODOS los registros involucrados para poder revisarlos.
duplicados = df.duplicated(keep=False)

evaluar_regla(
    "R05",
    "Registro involucrado en duplicación exacta",
    "Unicidad",
    duplicados
)

print(
    "Repeticiones adicionales:",
    int(df.duplicated(keep="first").sum())
)

# 8. Reportes.
reporte_resumen = pd.DataFrame(resumen)

reporte_incidencias = (
    pd.concat(incidencias, ignore_index=True)
    if incidencias
    else pd.DataFrame(columns=["registro", "regla", "motivo"])
)

reporte_resumen.to_csv(
    "resumen_calidad.csv", index=False, encoding="utf-8-sig"
)
reporte_incidencias.to_csv(
    "incidencias_calidad.csv", index=False, encoding="utf-8-sig"
)

print(reporte_resumen.to_string(index=False))

# ### 1.3 Incidencias encontradas

display(
    reporte_incidencias[
        ["registro", "regla", "motivo", "Año", "Mes",
         "Tipo de Tarifa", "Tipo de Dato"]
    ]
)

# ### 1.4 Detalle: registro incompleto y duplicados

# Mostrar todas las columnas.
pd.set_option("display.max_columns", None)

# Registro incompleto.
display(df.loc[periodo_incompleto])

# Duplicados ordenados para facilitar la comparación.
duplicados_detalle = df.loc[
    df.duplicated(keep=False)
].copy()

duplicados_detalle.insert(
    0, "registro", registro.loc[duplicados_detalle.index]
)

display(
    duplicados_detalle.sort_values(
        by=list(df.columns),
        na_position="last"
    )
)

# ### 1.5 Copia para el análisis con trazabilidad

# Separar registros que no tienen un periodo válido.
periodo_valido = (
    anio.notna()
    & anio.mod(1).eq(0)
    & mes_numero.notna()
).fillna(False)

registros_sin_periodo = df.loc[~periodo_valido].copy()

# Identificar repeticiones adicionales; conservar la primera aparición.
repeticion_adicional = df.duplicated(keep="first")

# Guardar trazabilidad del tratamiento.
bitacora = pd.DataFrame({
    "registro": registro,
    "sin_periodo_valido": ~periodo_valido,
    "repeticion_adicional": repeticion_adicional
})

display(
    bitacora[
        bitacora["sin_periodo_valido"]
        | bitacora["repeticion_adicional"]
    ]
)

# Crear la copia destinada al análisis.
seleccion = periodo_valido & ~repeticion_adicional
base_analisis = datos.loc[seleccion].copy()

# Conservar el número de registro original.
base_analisis.insert(
    0, "registro_original", registro.loc[seleccion]
)

# Incorporar los importes ya convertidos a números.
for columna in columnas_importe:
    base_analisis[columna] = importes_numericos.loc[
        seleccion, columna
    ]

# Construir una fecha mensual.
base_analisis["fecha"] = pd.to_datetime(
    pd.DataFrame({
        "year": anio.loc[seleccion].astype(int),
        "month": mes_numero.loc[seleccion].astype(int),
        "day": 1
    })
)

print("Registros originales:", len(df))
print("Registros para análisis:", len(base_analisis))

# ### 1.6 Clave candidata (categoría + periodo)

# Clave candidata: categoría tarifaria + periodo.
categorias = [
    "Tipo de Información",
    "Tipo de Tarifa",
    "Tipo de Dato",
    "Rango de Consumo",
    "Nivel"
]

clave = categorias + ["fecha"]

# Marcar todas las filas con la misma clave candidata.
clave_repetida = base_analisis.duplicated(
    subset=clave,
    keep=False
)

print(
    "Filas con categoría y periodo repetidos:",
    int(clave_repetida.sum())
)

if clave_repetida.any():
    display(
        base_analisis.loc[clave_repetida]
        .sort_values(clave)
    )
else:
    print("Cada categoría tiene como máximo una fila por mes.")

# ### 1.7 Series candidatas

# Evaluar cada categoría y cada variable monetaria.
resultados_series = []

for categoria, grupo in base_analisis.groupby(
    categorias, dropna=False, sort=False
):
    grupo = grupo.sort_values("fecha")

    calendario = pd.date_range(
        grupo["fecha"].min(),
        grupo["fecha"].max(),
        freq="MS"
    )

    meses_ausentes = calendario.difference(grupo["fecha"])

    for variable in columnas_importe:
        valores = grupo[variable]

        resultados_series.append({
            **dict(zip(categorias, categoria)),
            "variable": variable,
            "inicio": grupo["fecha"].min(),
            "fin": grupo["fecha"].max(),
            "meses_observados": grupo["fecha"].nunique(),
            "meses_ausentes_internos": len(meses_ausentes),
            "valores_validos": valores.notna().sum(),
            "valores_distintos": valores.nunique(),
            "porcentaje_ceros": round(
                100 * valores.dropna().eq(0).mean(), 2
            ) if valores.notna().any() else None
        })

perfil_series = pd.DataFrame(resultados_series)

# Filtro exploratorio, no garantía de aptitud estadística.
candidatas = perfil_series[
    (perfil_series["meses_observados"] >= 48)
    & (perfil_series["meses_ausentes_internos"] == 0)
    & (
        perfil_series["valores_validos"]
        == perfil_series["meses_observados"]
    )
    & (perfil_series["valores_distintos"] > 1)
].sort_values(
    ["meses_observados", "valores_distintos"],
    ascending=False
)

print("Series candidatas:", len(candidatas))
display(candidatas.head(20))

# ### 1.8 Serie seleccionada: Restricciones Rm

import matplotlib.pyplot as plt

# Seleccionar la primera candidata.
elegida = candidatas.iloc[0]
variable = elegida["variable"]

# Buscar su categoría, incluyendo campos que no aplican.
mascara = pd.Series(True, index=base_analisis.index)

for columna in categorias:
    valor = elegida[columna]

    if pd.isna(valor):
        mascara &= base_analisis[columna].isna()
    else:
        mascara &= base_analisis[columna].eq(valor).fillna(False)

serie = (
    base_analisis.loc[
        mascara, ["registro_original", "fecha", variable]
    ]
    .sort_values("fecha")
    .reset_index(drop=True)
)

# Visualizar los valores y sus cambios mensuales.
serie["cambio_mensual"] = serie[variable].diff()

fig, ejes = plt.subplots(2, 1, figsize=(12, 7), sharex=True)

ejes[0].plot(
    serie["fecha"], serie[variable],
    marker="o", markersize=3
)
ejes[0].set_title(
    f"{elegida['Tipo de Dato']} — {variable}"
)
ejes[0].set_ylabel("Valor reportado")
ejes[0].grid(alpha=0.3)

ejes[1].plot(
    serie["fecha"], serie["cambio_mensual"],
    marker="o", markersize=3, color="darkorange"
)
ejes[1].axhline(0, color="gray", linestyle="--")
ejes[1].set_ylabel("Cambio respecto al mes anterior")
ejes[1].set_xlabel("Fecha")
ejes[1].grid(alpha=0.3)

plt.tight_layout()
plt.show()

# ### 1.9 Autocorrelación de los cambios

import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.stats.diagnostic import acorr_ljungbox

# Diferencias entre meses consecutivos.
cambios = (
    serie["cambio_mensual"]
    .dropna()
    .astype(float)
)

print("Cambios mensuales analizados:", len(cambios))
print("Cambio promedio:", round(cambios.mean(), 2))
print(
    "Correlación entre cambios consecutivos:",
    round(cambios.autocorr(lag=1), 3)
)

# Explorar la relación entre cambios separados de 1 a 12 meses.
fig, ax = plt.subplots(figsize=(10, 4))

plot_acf(
    cambios,
    lags=12,
    zero=False,
    alpha=0.05,
    ax=ax
)

ax.set_title("Relación temporal entre los cambios mensuales")
ax.set_xlabel("Separación en meses")
ax.set_ylabel("Autocorrelación")

plt.tight_layout()
plt.show()

# Prueba conjunta de autocorrelación.
prueba = acorr_ljungbox(
    cambios,
    lags=[6, 12],
    return_df=True
)

display(prueba)

# ### 1.10 Distribución y variabilidad

fig, ejes = plt.subplots(1, 2, figsize=(12, 4))

# Distribución de los cambios.
ejes[0].hist(cambios, bins=12, edgecolor="white")
ejes[0].set_title("Distribución de los cambios mensuales")
ejes[0].set_xlabel("Cambio mensual")
ejes[0].set_ylabel("Frecuencia")

# Variabilidad en ventanas de 12 cambios.
variabilidad = (
    serie["cambio_mensual"]
    .astype(float)
    .rolling(window=12, min_periods=12)
    .std()
)

ejes[1].plot(serie["fecha"], variabilidad)
ejes[1].set_title("Variabilidad móvil de 12 cambios")
ejes[1].set_xlabel("Fecha")
ejes[1].set_ylabel("Desviación estándar")

plt.tight_layout()
plt.show()

# ### 1.11 Carta I

import matplotlib.pyplot as plt

# Preparar los 60 cambios en orden temporal.
carta = (
    serie[
        ["registro_original", "fecha", variable, "cambio_mensual"]
    ]
    .dropna(subset=["cambio_mensual"])
    .sort_values("fecha")
    .reset_index(drop=True)
    .copy()
)

carta["cambio_mensual"] = carta["cambio_mensual"].astype(float)

# División provisional para el prototipo.
n_referencia = 36

if len(carta) <= n_referencia:
    raise ValueError("No hay suficientes cambios para separar monitoreo.")

referencia = carta.iloc[:n_referencia].copy()

# Rango móvil de los CAMBIOS, no de los importes originales.
rangos_moviles = referencia["cambio_mensual"].diff().abs()
mr_promedio = rangos_moviles.dropna().mean()

centro = referencia["cambio_mensual"].mean()
sigma_estimada = mr_promedio / 1.128

if pd.isna(sigma_estimada) or sigma_estimada <= 0:
    raise ValueError("No se pueden estimar límites con esta referencia.")

limite_inferior = centro - 3 * sigma_estimada
limite_superior = centro + 3 * sigma_estimada

carta["fase"] = "Monitoreo"
carta.loc[:n_referencia - 1, "fase"] = "Referencia"

carta["fuera_limites"] = (
    (carta["cambio_mensual"] < limite_inferior)
    | (carta["cambio_mensual"] > limite_superior)
)

# Gráfica.
fig, ax = plt.subplots(figsize=(12, 5))

ax.plot(
    carta["fecha"], carta["cambio_mensual"],
    marker="o", markersize=4, label="Cambio mensual"
)

ax.axhline(centro, color="green", label="Línea central")
ax.axhline(
    limite_superior, color="red", linestyle="--",
    label="Límites de control provisionales"
)
ax.axhline(limite_inferior, color="red", linestyle="--")

inicio_monitoreo = carta.iloc[n_referencia]["fecha"]
ax.axvline(
    inicio_monitoreo, color="gray", linestyle=":",
    label="Inicio del monitoreo"
)

alertas = carta[carta["fuera_limites"]]

ax.scatter(
    alertas["fecha"], alertas["cambio_mensual"],
    color="red", s=65, zorder=5, label="Señal para revisión"
)

ax.set_title("Carta de individuales — cambios mensuales de Restricciones: Rm")
ax.set_xlabel("Fecha")
ax.set_ylabel("Cambio mensual")
ax.legend()
ax.grid(alpha=0.2)

plt.tight_layout()
plt.show()

print(f"Línea central: {centro:.2f}")
print(f"Límite inferior: {limite_inferior:.2f}")
print(f"Límite superior: {limite_superior:.2f}")

print("\nSeñales por fase:")
print(carta.groupby("fase")["fuera_limites"].agg(["sum", "count"]))

display(alertas)

# ### 1.12 Carta MR

# Rango móvil entre cambios mensuales consecutivos.
carta["rango_movil"] = carta["cambio_mensual"].diff().abs()

# Límites para rangos móviles de dos observaciones.
# mr_promedio ya se calculó únicamente con la referencia.
centro_mr = mr_promedio
limite_inferior_mr = 0.0
limite_superior_mr = 3.267 * centro_mr

# La primera observación no tiene rango móvil.
carta["alerta_mr"] = (
    carta["rango_movil"].notna()
    & (carta["rango_movil"] > limite_superior_mr)
)

fig, ax = plt.subplots(figsize=(12, 5))

ax.plot(
    carta["fecha"],
    carta["rango_movil"],
    marker="o",
    markersize=4,
    label="Rango móvil"
)

ax.axhline(
    centro_mr, color="green",
    label=f"Promedio MR: {centro_mr:.2f}"
)

ax.axhline(
    limite_superior_mr, color="red", linestyle="--",
    label=f"Límite superior: {limite_superior_mr:.2f}"
)

ax.axhline(
    limite_inferior_mr, color="red", linestyle="--",
    label="Límite inferior: 0"
)

ax.axvline(
    inicio_monitoreo, color="gray", linestyle=":",
    label="Inicio del monitoreo"
)

alertas_mr = carta.loc[carta["alerta_mr"]]

ax.scatter(
    alertas_mr["fecha"],
    alertas_mr["rango_movil"],
    color="red", s=65, zorder=5,
    label="Señal para revisión"
)

ax.set_title("Carta MR — rangos móviles de los cambios mensuales")
ax.set_xlabel("Fecha")
ax.set_ylabel("Diferencia absoluta entre cambios consecutivos")
ax.legend()
ax.grid(alpha=0.2)

plt.tight_layout()
plt.show()

print(f"Promedio MR: {centro_mr:.2f}")
print(f"Límite superior MR: {limite_superior_mr:.2f}")

resumen_mr = carta.groupby("fase").agg(
    rangos_evaluados=("rango_movil", "count"),
    señales=("alerta_mr", "sum")
)

display(resumen_mr)

display(
    alertas_mr[
        ["registro_original", "fecha", "cambio_mensual",
         "rango_movil", "fase"]
    ]
)

# ### 1.13 Caso de julio de 2021

display(
    serie.loc[
        serie["fecha"].between("2021-05-01", "2021-07-01"),
        ["registro_original", "fecha", variable, "cambio_mensual"]
    ]
)

# # Parte 2 · Hito 2: pipeline y modelo

# ## 2.0 Configuración del Hito 2

import hashlib, json, re
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mt
from sklearn.ensemble import IsolationForest
try:
    from IPython.display import display
except ImportError:          # si se ejecuta como .py
    display = print

pd.set_option("display.max_colwidth", 80)
OUT = Path("salida"); OUT.mkdir(exist_ok=True)
FIG = Path("figuras"); FIG.mkdir(exist_ok=True)

SEED = 2026          # semilla fija: mismos resultados en cada ejecución
N_REF = 36           # cambios mensuales de referencia (ene-2017 a dic-2019)
MIN_MESES = 49       # 36 cambios de referencia + al menos 12 meses de vigilancia
R_REPS = 20          # repeticiones por serie y tipo de error en la evaluación

MESES = dict(Enero=1, Febrero=2, Marzo=3, Abril=4, Mayo=5, Junio=6, Julio=7, Agosto=8,
             Septiembre=9, Octubre=10, Noviembre=11, Diciembre=12)
COLS_N1 = ["Propiedad Epm", "Compartido", "Propiedad del Cliente"]   # columnas del Nivel I
COLS_N24 = ["Punta", "Fuera de Punta"]                                 # columnas de Niveles II a IV
NUM = COLS_N1 + COLS_N24
CAT = ["Tipo de Información", "Tipo de Tarifa", "Tipo de Dato", "Rango de Consumo", "Nivel"]
EXCEL_MIN, EXCEL_MAX = 36526, 47483   # números con que Excel guarda fechas entre 2000 y 2029

# Colores de las gráficas
AZUL, VERDE, VIOLETA, AMARILLO, NARANJA, ROJO, GRIS = "#2a78d6", "#1baf7a", "#6250d6", "#eda100", "#eb6834", "#e34948", "#6b7280"
plt.rcParams.update({"font.size": 11, "axes.spines.top": False, "axes.spines.right": False,
                     "axes.spines.left": False, "axes.edgecolor": "#cbd2da", "axes.grid": True,
                     "grid.color": "#eef1f4", "axes.axisbelow": True, "xtick.color": GRIS, "ytick.color": GRIS})
import hashlib
resumen = {"sha256": hashlib.sha256(contenido).hexdigest()}

# ## 2.1 Datos de partida
# Se parte del mismo archivo cargado en la Parte 1. Los importes se toman ya convertidos a número
# (`importes_numericos`) y cada fila conserva el mismo `registro` del Hito 1 (posición en el archivo, sin contar el encabezado).

tabla = df.astype("object").where(df.notna(), "")
tabla = tabla.apply(lambda col: col.astype(str).str.strip())
for c in NUM:
    tabla[c] = importes_numericos[c].map(lambda v: "" if pd.isna(v) else repr(float(v)))
tabla.insert(0, "registro_original", registro.values)
df_hito1 = df          # se conserva el original de la Parte 1
df = tabla             # la Parte 2 trabaja sobre esta copia

resumen["filas"], resumen["columnas"] = len(df), len(df.columns) - 1
print(f"Filas: {len(df):,} · registro del {df.registro_original.min()} al {df.registro_original.max()}")

# ## 2.3 Unificación de etiquetas
# Varias categorías aparecen escritas de formas distintas (mayúsculas, espacios). Se toma como canónica la forma
# más frecuente. Además se proponen dos **sinónimos** (`0-CS` = `Rango 0 - CS` y `Mayor CS` = `Rango > CS`),
# pendientes de confirmar con EPM.

def clave_txt(s):
    return re.sub(r"\s+", "", s.strip().casefold())

SINONIMOS = {"Rango de Consumo": {"0-CS": "Rango 0 - CS", "Mayor CS": "Rango > CS"}}
catalogo = []
for col in ["Tipo de Tarifa", "Tipo de Dato", "Rango de Consumo"]:
    vc = df[col].value_counts()
    canon = {}
    for val in vc.index:
        canon.setdefault(clave_txt(val), val)
    mapa = {v: canon[clave_txt(v)] for v in vc.index}
    mapa.update(SINONIMOS.get(col, {}))
    for v, n in vc.items():
        if mapa[v] != v:
            catalogo.append(dict(columna=col, variante=v, canonico=mapa[v], filas=int(n),
                                 tipo="sinónimo propuesto" if v in SINONIMOS.get(col, {}) else "mayúsculas/espacios"))
    df[col + "_norm"] = df[col].map(mapa)
catalogo = pd.DataFrame(catalogo)
catalogo.to_csv(OUT / "02_catalogo_variantes.csv", index=False)
print(f"{len(catalogo)} variantes en {catalogo.filas.sum()} filas")
display(catalogo)

# ## 2.4 Reglas de calidad
# | Regla | Qué revisa | Dimensión |
# |---|---|---|
# | R01 | Año y mes presentes | Completitud |
# | R02 | Año entero y mes válido | Validez |
# | R03 | Importes con formato numérico | Validez |
# | R04 | Filas duplicadas exactas | Unicidad |
# | R05 | Misma categoría y fecha repetida tras unificar etiquetas | Unicidad |
# | R06 | Etiqueta escrita distinto a la forma canónica | Consistencia |
# | R07 | Importes negativos (en Restricciones solo es aviso) | Validez |
# | R08 | Tarifa EPM ≥ Compartida ≥ Cliente (Nivel I) | Consistencia |
# | R09 | Columnas usadas según el nivel de tensión | Consistencia |
# | R10 | Todos los importes en cero | Completitud |
# | R11 | Número que en realidad es una fecha de Excel | Exactitud |
# | R12 | Valor más de 10 veces la mediana de su serie (se aplica en el paso 5) | Exactitud |

hall = []
def H(reg, regla, dim, sev, col="", valor="", detalle=""):
    hall.append(dict(registro_original=int(reg), regla=regla, dimension=dim, severidad=sev,
                     columna=col, valor=valor, detalle=detalle))

for _, r in df.iterrows():                                    # R01, R02
    if r["Año"] == "" or r["Mes"] == "":
        H(r.registro_original, "R01 Período presente", "Completitud", "Error", "Año/Mes"); continue
    if not r["Año"].isdigit() or r["Mes"] not in MESES:
        H(r.registro_original, "R02 Año entero y mes válido", "Validez", "Error", "Año/Mes", f'{r["Año"]}/{r["Mes"]}')

num = df[NUM].apply(pd.to_numeric, errors="coerce")           # R03
for c in NUM:
    for i in df.index[num[c].isna() & (df[c] != "")]:
        H(df.at[i, "registro_original"], "R03 Formato numérico", "Validez", "Error", c, df.at[i, c])

columnas_originales = list(df.columns[1:13])                   # R04
dup = df.duplicated(subset=columnas_originales, keep="first")
for i in df.index[dup]:
    H(df.at[i, "registro_original"], "R04 Duplicado exacto (adicional)", "Unicidad", "Error")
resumen["filas_en_duplicados"] = int(df.duplicated(subset=columnas_originales, keep=False).sum())
resumen["duplicados_adicionales"] = int(dup.sum())

for col in ["Tipo de Tarifa", "Tipo de Dato", "Rango de Consumo"]:   # R06
    for i in df.index[df[col] != df[col + "_norm"]]:
        H(df.at[i, "registro_original"], "R06 Etiqueta no canónica", "Consistencia", "Advertencia",
          col, df.at[i, col], f'→ {df.at[i, col + "_norm"]}')

con_periodo = df["Año"] != ""
for i in df.index[con_periodo]:                                # R07 a R11
    reg, nivel = df.at[i, "registro_original"], df.at[i, "Nivel"]
    es_rm = df.at[i, "Tipo de Dato_norm"].startswith("Restricciones")
    vals = num.loc[i]
    for c in NUM:
        v = vals[c]
        if pd.isna(v): continue
        if v < 0:
            H(reg, "R07 No negatividad", "Validez", "Informativa" if es_rm else "Error", c, v,
              "Rm puede ser negativo (pendiente confirmar)" if es_rm else "")
        if float(v).is_integer() and EXCEL_MIN <= v <= EXCEL_MAX:
            fecha = (pd.Timestamp("1899-12-30") + pd.Timedelta(days=int(v))).date()
            H(reg, "R11 Posible serial de fecha Excel", "Exactitud", "Error", c, v, f"equivale a {fecha}")
    if nivel == "I" and vals["Propiedad Epm"] > 0:
        a, b, cl = vals["Propiedad Epm"], vals["Compartido"], vals["Propiedad del Cliente"]
        if not (a >= b >= cl):
            H(reg, "R08 Orden EPM ≥ Compartido ≥ Cliente", "Consistencia", "Advertencia", "Propiedad", f"{a} / {b} / {cl}")
    if nivel == "I" and (vals[COLS_N24] != 0).any():
        H(reg, "R09 Columnas según nivel", "Consistencia", "Advertencia", "Punta/Fuera")
    if nivel != "I" and (vals[COLS_N1] != 0).any():
        H(reg, "R09 Columnas según nivel", "Consistencia", "Advertencia", "Propiedad")
    if (vals.fillna(0) == 0).all():
        H(reg, "R10 Todos los importes en cero", "Completitud", "Advertencia")
print(f"Hallazgos hasta ahora: {len(hall)}")

# ## 2.5 Series mensuales
# Una **serie** es la evolución mes a mes de una misma tarifa (misma combinación de categorías y columna).
# Se retiran los duplicados exactos y la fila sin período. Si dos filas son la misma categoría y fecha con
# **los mismos importes** (duplicado oculto por etiquetas sinónimas), se conserva una.

prep = df[(~dup) & con_periodo].copy()
prep["fecha"] = pd.to_datetime(dict(year=prep["Año"].astype(int), month=prep["Mes"].map(MESES), day=1))
for c in NUM:
    prep[c] = pd.to_numeric(prep[c])
KEY = [c + "_norm" if c in ["Tipo de Tarifa", "Tipo de Dato", "Rango de Consumo"] else c for c in CAT]

clave_rep = prep.duplicated(subset=KEY + ["fecha"], keep=False)          # R05
for i in prep.index[clave_rep]:
    H(prep.at[i, "registro_original"], "R05 Clave categoría+fecha repetida", "Unicidad", "Advertencia",
      detalle="mismos importes con etiquetas sinónimas")
resumen["clave_repetida_filas"] = int(clave_rep.sum())
sem = prep.duplicated(subset=KEY + ["fecha"] + NUM, keep="first")
prep = prep[~sem].copy()
resumen["duplicados_semanticos_retirados"] = int(sem.sum())
clave_dup = prep.duplicated(subset=KEY + ["fecha"], keep=False)

series = []
for k, g in prep[~clave_dup].groupby(KEY):
    nivel = k[4]; g = g.sort_values("fecha")
    for c in (COLS_N1 if nivel == "I" else COLS_N24):
        s = g.set_index("fecha")[c]
        completa = len(pd.date_range(s.index.min(), s.index.max(), freq="MS")) == len(s)
        series.append(dict(clave=" | ".join(k), columna=c, nivel=nivel, tipo_dato=k[2], n=len(s),
                           completa=completa, distintos=s.nunique(), s=s,
                           regs=g.set_index("fecha")["registro_original"]))

for se in series:                                                         # R12
    s = se["s"]; med = s.abs().median()
    if med > 0:
        for f in s.index[s.abs() > 10 * med]:
            H(se["regs"][f], "R12 Magnitud > 10× mediana de su serie", "Exactitud", "Error",
              se["columna"], s[f], f"mediana {med:.2f}")

hall = pd.DataFrame(hall)
hall.to_csv(OUT / "03_hallazgos.csv", index=False)
res_reglas = hall.groupby(["regla", "dimension", "severidad"]).registro_original.nunique().rename("filas").reset_index()
res_reglas.to_csv(OUT / "04_resumen_reglas.csv", index=False)
print("Resumen de reglas (filas marcadas):")
display(res_reglas)

# ### Hallazgos de exactitud y consistencia sobre los importes

clave_hall = hall[hall.regla.str[:3].isin(["R08", "R11", "R12"])]
display(clave_hall)

# Filas que se apartan (cuarentena) antes de calcular las cartas
reg_cuarentena = set(clave_hall.registro_original)
reg_cuarentena |= set(hall[(hall.regla.str[:3] == "R07") & (hall.severidad == "Error")].registro_original)
resumen["filas_cuarentena"] = len(reg_cuarentena)

elig = [se for se in series if se["completa"] and se["n"] >= MIN_MESES and se["distintos"] >= 2]
for se in elig:
    se["sucia"] = bool(set(se["regs"].values) & reg_cuarentena)
resumen["series_total"], resumen["series_completas_49"] = len(series), len(elig)
print(f"Series: {len(series)} posibles · {len(elig)} con ≥ {MIN_MESES} meses seguidos · filas en cuarentena: {len(reg_cuarentena)}")

# ## 2.6 Modelo A: cartas de control I-MR
# Se trabaja con el **cambio mensual** (valor del mes − valor del mes anterior).
# Los límites se calculan con los 36 cambios de referencia (2017–2019) y se mantienen fijos en la vigilancia (2020–2021):
# 
# * Carta I: media ± 2,66 · MR̄
# * Carta MR: rango móvil ≤ 3,267 · MR̄

def limites(d_ref):
    mr = np.abs(np.diff(d_ref)); mrbar = mr.mean(); xbar = d_ref.mean()
    return xbar, mrbar, xbar - 2.66 * mrbar, xbar + 2.66 * mrbar, 3.267 * mrbar

def imr_alertas(v):
    """Devuelve los meses (posición en v) con alerta I o MR durante la vigilancia."""
    d = np.diff(v)
    xbar, mrbar, lcl, ucl, mrucl = limites(d[:N_REF])
    mr = np.abs(np.diff(d)); al = set()
    for j in range(N_REF, len(d)):
        if d[j] < lcl or d[j] > ucl: al.add(j + 1)      # carta I
        if mr[j - 1] > mrucl:        al.add(j + 1)      # carta MR
    return al, mrbar

for se in elig:
    _, se["mrbar"] = imr_alertas(se["s"].values)
utiles = [se for se in elig if se["mrbar"] > 0]
limpias = [se for se in utiles if not se["sucia"]]
resumen.update(series_utiles=len(utiles), series_limpias=len(limpias),
               series_con_valores_en_cuarentena=len(utiles) - len(limpias))

alert_real = []
for se in utiles:
    al, _ = imr_alertas(se["s"].values)
    for t in sorted(al):
        f = se["s"].index[t]
        alert_real.append(dict(clave=se["clave"], columna=se["columna"], fecha=f.date(), valor=se["s"].iloc[t],
                               registro_original=int(se["regs"][f]), serie_con_cuarentena=se["sucia"]))
alert_real = pd.DataFrame(alert_real)
alert_real.to_csv(OUT / "05_alertas_imr_reales.csv", index=False)
resumen["meses_monitoreados_reales"] = sum(len(se["s"]) - (N_REF + 1) for se in utiles)
resumen["alertas_imr_reales"] = len(alert_real)
print(f"{len(utiles)} series · {len(alert_real)} alertas en {resumen['meses_monitoreados_reales']} meses-serie vigilados")

# ## 2.7 Modelo B: Isolation Forest
# Un solo modelo para todas las series sin hallazgos (cada serie es corta). Para cada mes usa 4 variables,
# escaladas con la variabilidad de referencia de su serie: cambio anterior, cambio siguiente, rango móvil y
# nivel relativo. Se entrena **solo con meses de referencia**.

def features(v, mrbar):
    sig = mrbar / 1.128
    d = np.diff(v); ref_med = np.median(np.abs(v[:N_REF + 1])) + 1e-9
    X, meses = [], []
    for t in range(1, len(v) - 1):
        X.append([d[t - 1] / sig, d[t] / sig, abs(d[t] - d[t - 1]) / sig, np.log((abs(v[t]) + 1e-6) / ref_med)])
        meses.append(t)
    return np.array(X), np.array(meses)

Xtr = []
for se in limpias:
    X, m = features(se["s"].values, se["mrbar"])
    Xtr.append(X[m <= N_REF - 1])
Xtr = np.vstack(Xtr)
iforest = IsolationForest(n_estimators=300, random_state=SEED).fit(Xtr)
umbral_if = np.quantile(-iforest.score_samples(Xtr), 0.995)     # umbral propio (percentil 99,5)

def if_puntajes(v, mrbar):
    X, m = features(v, mrbar); sc = -iforest.score_samples(X)
    return dict(zip(m[m >= N_REF + 1], sc[m >= N_REF + 1]))
print(f"Entrenado con {len(Xtr):,} meses de referencia de {len(limpias)} series")

# ## 2.8 Evaluación con errores inyectados
# Como no hay errores confirmados, se meten errores a propósito en copias de las series sin hallazgos y se mide
# cuántos detecta cada método. Tres tipos copian errores reales encontrados en esta fuente.
# Un error cuenta como **detectado** si hay alerta en el mes alterado o en el siguiente.
# ⏱ Esta celda tarda unos 4 minutos.

def reglas_valor(v_nuevo, col, fila, tipo_dato, med_serie):
    if v_nuevo < 0 and not tipo_dato.startswith("Restricciones"): return True
    if float(v_nuevo).is_integer() and EXCEL_MIN <= v_nuevo <= EXCEL_MAX: return True
    if med_serie > 0 and abs(v_nuevo) > 10 * med_serie: return True
    if col in COLS_N1:
        f = fila.copy(); f[col] = v_nuevo
        if f["Propiedad Epm"] > 0 and not (f["Propiedad Epm"] >= f["Compartido"] >= f["Propiedad del Cliente"]):
            return True
    return False

TIPOS = ["Separador decimal (×1000)", "Fecha de Excel", "Signo invertido",
         "Columna equivocada", "Desviación +10 %", "Valor no actualizado"]
rng = np.random.default_rng(SEED)
prep_idx = prep.set_index("registro_original")

def inyectar(tipo, v, t, se, fila):
    x = v[t]
    if tipo == TIPOS[0]: return x * 1000
    if tipo == TIPOS[1]:
        dia = int(min(max(abs(x), 1), 28)); mes = int(rng.integers(1, 13))
        return float((pd.Timestamp(2019, mes, dia) - pd.Timestamp("1899-12-30")).days)
    if tipo == TIPOS[2]: return -x
    if tipo == TIPOS[3]:
        otras = [c for c in (COLS_N1 if se["nivel"] == "I" else COLS_N24) if c != se["columna"]]
        cands = [fila[c] for c in otras if fila[c] != x]
        return cands[int(rng.integers(len(cands)))] if cands else None
    if tipo == TIPOS[4]: return x * 1.10
    if tipo == TIPOS[5]: return v[t - 1] if v[t - 1] != x else None

reg = []
for se in limpias:
    v0 = se["s"].values.astype(float); med = np.median(np.abs(v0))
    for tipo in TIPOS:
        for _ in range(R_REPS):
            t = int(rng.integers(N_REF + 1, len(v0) - 1))
            if v0[t] == 0 and tipo in TIPOS[:3] + [TIPOS[4]]: continue
            fila = prep_idx.loc[int(se["regs"].iloc[t]), NUM]
            nuevo = inyectar(tipo, v0, t, se, fila)
            if nuevo is None: continue
            v = v0.copy(); v[t] = nuevo
            a_imr, _ = imr_alertas(v)
            p_if = if_puntajes(v, se["mrbar"])
            det_r = reglas_valor(nuevo, se["columna"], fila, se["tipo_dato"], med)
            det_imr = bool(a_imr & {t, t + 1})
            det_if = any(p_if.get(k, 0) > umbral_if for k in (t, t + 1))
            reg.append(dict(tipo=tipo, clave=se["clave"], columna=se["columna"], mes=t,
                            reglas=det_r, imr=det_imr, iforest=det_if,
                            puntaje_if=max(p_if.get(t, 0), p_if.get(t + 1, 0)),
                            reglas_imr=det_r or det_imr, reglas_if=det_r or det_if))
reg = pd.DataFrame(reg)
reg.to_csv(OUT / "06_experimento_inyeccion.csv", index=False)
resumen["casos_inyectados"] = len(reg)
print(f"{len(reg):,} pruebas")

# ### Alertas en series sin errores conocidos (meses de vigilancia sin inyección)

fa_imr = n_mon = 0; punt = []
for se in limpias:
    v0 = se["s"].values.astype(float); al = imr_alertas(v0)[0]
    n_mon += len(v0) - (N_REF + 1); fa_imr += len(al)
    for t_, sc_ in if_puntajes(v0, se["mrbar"]).items():
        punt.append(dict(clave=se["clave"], columna=se["columna"], mes=int(t_), puntaje=float(sc_), alerta_imr=int(t_) in al))
punt = pd.DataFrame(punt)
punt.to_csv(OUT / "11_puntajes_limpios_por_serie.csv", index=False)
resumen.update(meses_monitoreo_limpios=n_mon, tasa_fa_imr=fa_imr / n_mon,
               tasa_fa_if_umbral_propio=float((punt.puntaje > umbral_if).mean()))
print(f"Cartas I-MR: {100 * fa_imr / n_mon:.1f} % de meses con alerta · "
      f"Isolation Forest (umbral propio): {100 * resumen['tasa_fa_if_umbral_propio']:.1f} %")

# ## 2.9 Comparación justa: validación cruzada e intervalos de confianza
# El umbral de Isolation Forest se fija para dar **la misma tasa de alertas que las cartas**, pero calculado con
# **otras series** (5 grupos), para no ajustarlo con los mismos datos con que se evalúa. Los intervalos de 95 % se
# obtienen remuestreando series completas (bootstrap), porque las pruebas de una misma serie no son independientes.

K = 5
punt["sid"] = punt.clave + " || " + punt.columna; reg["sid"] = reg.clave + " || " + reg.columna
sids = np.array(sorted(punt.sid.unique())); rng_cv = np.random.default_rng(SEED); rng_cv.shuffle(sids)
grupo = {s: i % K for i, s in enumerate(sids)}
punt["g"] = punt.sid.map(grupo); reg["g"] = reg.sid.map(grupo)
tasa_imr = punt.alerta_imr.mean()
reg["if_cv"] = False; fa_cv = []
for k in range(K):
    thr = np.quantile(punt.loc[punt.g != k, "puntaje"], 1 - tasa_imr)
    fa_cv.append((punt.loc[punt.g == k, "puntaje"] > thr).values)
    reg.loc[reg.g == k, "if_cv"] = reg.loc[reg.g == k, "puntaje_if"] > thr
resumen["tasa_fa_if_cv"] = float(np.concatenate(fa_cv).mean())

cols = ["reglas", "imr", "if_cv", "reglas_imr"]
recall = reg.groupby("tipo")[cols].mean().loc[TIPOS]
recall.loc["Total"] = reg[cols].mean()
recall.columns = ["Reglas", "Cartas I-MR", "Isolation Forest", "Reglas + cartas"]
recall.to_csv(OUT / "07_deteccion_por_tipo.csv")

# Bootstrap por series
g = reg.groupby("sid"); sums = g[["imr", "if_cv", "reglas_imr"]].sum(); ns = g.size(); ids = sums.index.values
boot = {c: [] for c in ["imr", "if_cv", "reglas_imr", "dif"]}
for _ in range(1000):
    smp = rng_cv.choice(ids, len(ids), replace=True); tot = ns.loc[smp].sum()
    for c in ["imr", "if_cv", "reglas_imr"]:
        boot[c].append(sums.loc[smp, c].sum() / tot)
    boot["dif"].append(boot["if_cv"][-1] - boot["imr"][-1])
ic = {c: np.percentile(v, [2.5, 97.5]) for c, v in boot.items()}
resumen["ic95"] = {c: [float(a), float(b)] for c, (a, b) in ic.items()}

print(f"Alertas sin error conocido → cartas: {100 * tasa_imr:.1f} % · Isolation Forest: {100 * resumen['tasa_fa_if_cv']:.1f} %")
print(f"Diferencia IF − cartas en el total: entre {100 * ic['dif'][0]:+.1f} y {100 * ic['dif'][1]:+.1f} puntos (IC 95 %)")
print(f"Reglas + cartas: {100 * recall.loc['Total', 'Reglas + cartas']:.0f} % "
      f"(IC 95 %: {100 * ic['reglas_imr'][0]:.0f}–{100 * ic['reglas_imr'][1]:.0f} %)")
display((100 * recall).round(0))

# ## 2.10 Gráficas

# ### Resultados: % de errores detectados por tipo

etq = ["Coma\ndecimal", "Fecha de\nExcel", "Signo\ninvertido", "Columna\ncambiada", "Desviación\n10 %", "Valor sin\nactualizar", "Total"]
fig, ax = plt.subplots(figsize=(12, 4.5))
w = 0.2; x = np.arange(len(recall))
for i, (col, color) in enumerate(zip(recall.columns, [AMARILLO, AZUL, VERDE, VIOLETA])):
    vals = 100 * recall[col].values
    b = ax.bar(x + (i - 1.5) * w, vals, w, color=color, label=col, edgecolor="white", linewidth=1)
    ax.bar_label(b, fmt="%.0f", fontsize=8, color="#1f2937", padding=2)
ax.set_xticks(x); ax.set_xticklabels(etq); ax.set_ylim(0, 110); ax.set_ylabel("% detectado")
ax.legend(ncol=4, loc="upper center", bbox_to_anchor=(0.5, 1.12), frameon=False)
fig.tight_layout(); fig.savefig(FIG / "resultados.png", dpi=200); plt.show()

# ### Una fecha de Excel dentro de la serie (datos originales)

d0 = df[con_periodo].copy()
d0["fecha"] = pd.to_datetime(dict(year=d0["Año"].astype(int), month=d0["Mes"].map(MESES), day=1))
q = d0[(d0["Tipo de Información"] == "Horaria") & (d0["Tipo de Tarifa"] == "Tarifa") &
       (d0["Tipo de Dato"] == "Cargo transporte SDL: Dn,m") & (d0["Nivel"] == "IV")].drop_duplicates(subset=columnas_originales)
q = q.sort_values("fecha"); y = pd.to_numeric(q["Punta"])
fig, ax = plt.subplots(figsize=(12, 3.9))
ax.plot(q["fecha"], y, color=AZUL, marker="o", ms=4, lw=2); ax.set_yscale("log")
ax.set_ylabel("Cargo Dn,m Punta (escala log)")
i = y.idxmax(); f = q.loc[i, "fecha"]
ax.scatter([f], [y[i]], s=90, facecolor="none", edgecolor=ROJO, lw=2, zorder=5)
ax.annotate(f"Fila {q.loc[i, 'registro_original']}: 43.577\n= 22-abr-2019 en Excel", (f, y[i]), xytext=(40, -35),
            textcoords="offset points", color=ROJO, fontweight="bold", arrowprops=dict(arrowstyle="->", color=ROJO))
fig.tight_layout(); fig.savefig(FIG / "fecha_excel.png", dpi=200); plt.show()

# ### Por qué las reglas van antes que las cartas

se = [s for s in series if "Estrato 1 | Rango 0 - CS" in s["clave"] and s["columna"] == "Compartido"][0]
s = se["s"].astype(float)
s_cuar = s.copy(); s_cuar[pd.Timestamp("2018-07-01")] = np.nan; s_cuar = s_cuar.interpolate()
fechas = s.index[1:]
fig, axs = plt.subplots(1, 2, figsize=(12, 3.9))
for ax, v, tit in [(axs[0], s.values, "A. Con el error en la referencia"), (axs[1], s_cuar.values, "B. Con el error en cuarentena")]:
    d = np.diff(v); xb, mrb, lcl, ucl, _ = limites(d[:N_REF])
    out = (d < lcl) | (d > ucl); out[:N_REF] = False
    ax.axvspan(fechas[N_REF], fechas[-1], color="#F2F5F9")
    ax.plot(fechas, d, color=AZUL, lw=1.8, marker="o", ms=3.5)
    ax.axhline(xb, color=VERDE, lw=1); ax.axhline(lcl, color=NARANJA, ls="--"); ax.axhline(ucl, color=NARANJA, ls="--")
    ax.scatter(fechas[out], d[out], color=ROJO, s=30, zorder=5)
    ax.set_title(f"{tit}\nlímites {lcl:,.2f} y {ucl:,.2f} · {out.sum()} alertas", loc="left", fontsize=11)
axs[0].yaxis.set_major_formatter(mt.FuncFormatter(lambda x, _: f"{x:,.0f}"))
fig.tight_layout(); fig.savefig(FIG / "reglas_antes_que_cartas.png", dpi=200); plt.show()

# ### Alertas de las cartas por mes (datos reales)

meses = pd.period_range("2020-01", "2021-12", freq="M")
cnt = pd.to_datetime(alert_real.fecha).dt.to_period("M").value_counts().reindex(meses, fill_value=0)
fig, ax = plt.subplots(figsize=(12, 3.8))
colores = [AZUL if str(m) == "2020-02" else "#b7d0f0" for m in meses]
MM = ["ene", "feb", "mar", "abr", "may", "jun", "jul", "ago", "sep", "oct", "nov", "dic"]
b = ax.bar([f"{MM[m.month - 1]}\n{str(m.year)[2:]}" for m in meses], cnt.values, color=colores)
ax.bar_label(b, fontsize=8, color=GRIS)
ax.set_ylabel("Alertas")
fig.tight_layout(); fig.savefig(FIG / "alertas_por_mes.png", dpi=200); plt.show()
feb = alert_real[pd.to_datetime(alert_real.fecha) == "2020-02-01"]
print(f"Febrero de 2020: {feb.groupby(['clave', 'columna']).ngroups} de {len(utiles)} series con alerta")

# ## 2.11 Exportar resultados

prep.to_csv(OUT / "08_copia_preparada.csv", index=False)
json.dump(resumen, open(OUT / "00_resumen.json", "w"), indent=2, ensure_ascii=False, default=float)
print(json.dumps({k: v for k, v in resumen.items() if k != "ic95"}, indent=2, ensure_ascii=False, default=float))
print("\nArchivos en salida/:", sorted(p.name for p in OUT.iterdir()))

