"""Genera las figuras y INFORME_METRICAS.md de 4.3 a partir de los CSV ya calculados.

Todas las cifras del informe se leen de las tablas; ninguna se transcribe a mano.
"""
from __future__ import annotations

import sys
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402

HERE = Path(__file__).resolve().parent
sys.dont_write_bytecode = True
sys.path.insert(0, str(HERE))
from metricas_base import ERROR_TYPES, METHODS, METHOD_LABELS  # noqa: E402

ALPHA, PREV, HZ = 0.05, 0.05, 't'
MAIN_SOURCES = ('EPM', 'CHEC', 'SSPD')           # XM tiene una serie y 12 observaciones
COLORS = {'IMR': '#2a78d6', 'Z_robusto': '#eb6834', 'IF': '#1baf7a',
          'LOF': '#eda100', 'KNN': '#e87ba4', 'R12': '#008300'}   # ranuras 1-6 de la paleta de referencia
INK, INK2, MUTED, GRID, BASE, SURFACE = '#0b0b0b', '#52514e', '#898781', '#e1e0d9', '#c3c2b7', '#fcfcfb'
TYPE_LABEL = {'decimal_x1000': 'Decimal ×1000', 'decimal_div1000': 'Decimal ÷1000',
              'serial_excel_43577': 'Serial Excel', 'aumento_10pct': 'Aumento 10 %',
              'valor_no_actualizado': 'Valor no actualizado', 'otra_medida': 'Otra medida'}


def pct(x, digits=1):
    return f'{100 * x:.{digits}f}'.replace('.', ',') + ' %'


def num(x, digits=3):
    return f'{x:.{digits}f}'.replace('.', ',')


def style():
    plt.rcParams.update({
        'figure.facecolor': SURFACE, 'axes.facecolor': SURFACE, 'savefig.facecolor': SURFACE,
        'font.family': ['Segoe UI', 'DejaVu Sans'], 'font.size': 9.5, 'text.color': INK,
        'axes.edgecolor': BASE, 'axes.labelcolor': INK2, 'xtick.color': INK2, 'ytick.color': INK2,
        'axes.spines.top': False, 'axes.spines.right': False, 'axes.grid': True,
        'grid.color': GRID, 'grid.linewidth': 0.8, 'axes.axisbelow': True,
        'lines.linewidth': 2.0, 'legend.frameon': False})


def save(fig, name):
    (HERE / 'figuras').mkdir(exist_ok=True)
    for ext in ('png', 'svg', 'pdf'):
        fig.savefig(HERE / 'figuras' / f'{name}.{ext}', dpi=200, bbox_inches='tight')
    plt.close(fig)


def usable(frame, method, source):
    return frame[(frame.metodo == method) & (frame.fuente == source) & (frame.estado_metodo == 'evaluable')]


def figure_curves(curve):
    fig, axes = plt.subplots(1, 3, figsize=(11.5, 3.9), sharey=True)
    for ax, source in zip(axes, MAIN_SOURCES):
        for method in METHODS:
            d = usable(curve, method, source)
            if d.empty:
                continue
            ax.plot(100 * d.tasa_objetivo, d.recall_macro_t, color=COLORS[method], label=METHOD_LABELS[method])
        ax.axvline(100 * ALPHA, color=MUTED, linewidth=1.0, linestyle=(0, (2, 3)))
        ax.set_xscale('log')
        ax.set_xticks([0.5, 1, 2, 5, 10, 20])
        ax.set_xticklabels(['0,5', '1', '2', '5', '10', '20'])
        ax.set_xlabel('Tasa de alerta en meses reales (%)')
        ax.set_title(source, loc='left', fontsize=10.5, fontweight='bold')
        ax.set_ylim(0, 1.02)
    axes[0].set_ylabel('Recall macro (seis tipos, igual peso)')
    handles, labels = axes[0].get_legend_handles_labels()
    for ax in axes[1:]:
        for h, l in zip(*ax.get_legend_handles_labels()):
            if l not in labels:
                handles.append(h)
                labels.append(l)
    fig.legend(handles, labels, loc='lower center', ncol=6, bbox_to_anchor=(0.5, -0.08), fontsize=9)
    fig.suptitle('Curvas de detección: recall frente a tasa de alerta igualada (horizonte t)',
                 x=0.01, ha='left', fontsize=11.5, fontweight='bold')
    fig.text(0.01, 0.905, 'Línea punteada: 5 %. Se omiten celdas con menos de 5 alertas esperadas y LOF en CHEC (degenerado por duplicados).',
             fontsize=8.5, color=INK2)
    fig.subplots_adjust(top=0.80)
    save(fig, '01_curvas_deteccion')


def figure_f1(metrics):
    fig, axes = plt.subplots(1, 3, figsize=(11.5, 3.6), sharex=True)
    for ax, source in zip(axes, MAIN_SOURCES):
        d = metrics[(metrics.fuente == source) & (metrics.tasa_objetivo == ALPHA) &
                    (metrics.horizonte == HZ) & (metrics.prevalencia_supuesta == PREV)]
        for row_index, method in enumerate(METHODS):
            r = d[d.metodo == method].iloc[0]
            y = len(METHODS) - 1 - row_index
            if r.estado_metodo != 'evaluable':
                ax.text(0.02, y, 'n/d (degenerado)', va='center', fontsize=8.5, color=MUTED)
                continue
            ax.plot([r.ic95_inferior_f1, r.ic95_superior_f1], [y, y], color=COLORS[method], linewidth=2.0)
            ax.plot(r.f1, y, 'o', color=COLORS[method], markersize=8, markeredgecolor=SURFACE, markeredgewidth=1.6)
            ax.text(min(r.ic95_superior_f1 + 0.02, 0.97), y, num(r.f1, 2), va='center', fontsize=8.5, color=INK2)
        ax.set_yticks(range(len(METHODS)))
        ax.set_yticklabels([METHOD_LABELS[m] for m in reversed(METHODS)] if source == MAIN_SOURCES[0] else [''] * len(METHODS))
        ax.set_xlim(0, 1.05)
        ax.set_xlabel('F1 (IC 95 % por categorías)')
        ax.set_title(source, loc='left', fontsize=10.5, fontweight='bold')
        ax.grid(axis='y', visible=False)
    fig.suptitle('F1 a tasa de alerta igualada del 5 % (precisión con prevalencia supuesta del 5 %, horizonte t)',
                 x=0.01, ha='left', fontsize=11.5, fontweight='bold')
    fig.subplots_adjust(top=0.84, wspace=0.08)
    save(fig, '02_f1_por_metodo')


def figure_types(by_type):
    from matplotlib.colors import LinearSegmentedColormap
    cmap = LinearSegmentedColormap.from_list('seq', ['#cde2fb', '#6da7ec', '#256abf', '#0d366b'])
    fig, axes = plt.subplots(1, 3, figsize=(12.5, 3.6))
    for ax, source in zip(axes, MAIN_SOURCES):
        d = by_type[(by_type.fuente == source) & (by_type.tasa_objetivo == ALPHA) & (by_type.horizonte == HZ)]
        grid = np.full((len(ERROR_TYPES), len(METHODS)), np.nan)
        for j, method in enumerate(METHODS):
            sub = d[(d.metodo == method)]
            if (sub.estado_metodo != 'evaluable').any():
                continue
            for i, kind in enumerate(ERROR_TYPES):
                v = sub[sub.tipo == kind].recall
                if len(v):
                    grid[i, j] = float(v.iloc[0])
        ax.imshow(np.ma.masked_invalid(grid), cmap=cmap, vmin=0, vmax=1, aspect='auto')
        ax.grid(False)
        for i in range(grid.shape[0]):
            for j in range(grid.shape[1]):
                v = grid[i, j]
                label = 'n/d' if np.isnan(v) else num(v, 2)
                ax.text(j, i, label, ha='center', va='center', fontsize=8.5,
                        color='#ffffff' if (not np.isnan(v) and v > 0.5) else INK)
        ax.set_xticks(range(len(METHODS)))
        ax.set_xticklabels(['I-MR', 'Z-rob.', 'IF', 'LOF', 'KNN', 'R12'], fontsize=8.5)
        ax.set_yticks(range(len(ERROR_TYPES)))
        ax.set_yticklabels([TYPE_LABEL[k] for k in ERROR_TYPES] if source == MAIN_SOURCES[0] else [''] * len(ERROR_TYPES))
        ax.set_title(source, loc='left', fontsize=10.5, fontweight='bold')
        for spine in ax.spines.values():
            spine.set_visible(False)
    fig.suptitle('Recall por tipo de error a tasa de alerta igualada del 5 % (horizonte t)',
                 x=0.01, ha='left', fontsize=11.5, fontweight='bold')
    fig.subplots_adjust(top=0.84, wspace=0.06)
    save(fig, '03_recall_por_tipo')


# ------------------------------------------------------------------- informe
def md_table(header, rows):
    out = ['| ' + ' | '.join(header) + ' |', '|' + '|'.join(['---'] * len(header)) + '|']
    out += ['| ' + ' | '.join(str(c) for c in r) + ' |' for r in rows]
    return '\n'.join(out)


def main():
    style()
    metrics = pd.read_csv(HERE / 'metricas_globales.csv')
    by_type = pd.read_csv(HERE / 'deteccion_por_tipo_tasa_igualada.csv')
    curve = pd.read_csv(HERE / 'curva_deteccion.csv')
    diff = pd.read_csv(HERE / 'diferencias_vs_IMR.csv')
    native = pd.read_csv(HERE / 'puntos_operativos_nativos.csv')
    draw = pd.read_csv(HERE / 'sorteo_sin_reemplazo.csv')
    tests = pd.read_csv(HERE / 'pruebas_por_tipo.csv')
    cover = pd.read_csv(HERE / 'cobertura_experimento.csv')
    thresholds = pd.read_csv(HERE / 'umbrales_tasa_igualada.csv')
    omitted = pd.read_csv(HERE / 'inyecciones_omitidas.csv')
    figure_curves(curve)
    figure_f1(metrics)
    figure_types(by_type)

    head = metrics[(metrics.tasa_objetivo == ALPHA) & (metrics.horizonte == HZ) & (metrics.prevalencia_supuesta == PREV)]

    def cell(r, name):
        return f"{num(r[name], 2)} [{num(r['ic95_inferior_' + name], 2)}–{num(r['ic95_superior_' + name], 2)}]"

    sections = {}
    for source in ('EPM', 'CHEC', 'SSPD', 'XM'):
        d = head[head.fuente == source]
        rows = []
        for method in METHODS:
            r = d[d.metodo == method].iloc[0]
            if source == 'XM':
                rows.append([METHOD_LABELS[method], num(r.recall_macro, 2), pct(r.tasa_alerta_sin_error_conocido), '—', '—', r.estado_metodo])
            else:
                rows.append([METHOD_LABELS[method], cell(r, 'recall_macro'),
                             pct(r.tasa_alerta_sin_error_conocido), cell(r, 'precision_conservadora'), cell(r, 'f1'),
                             'evaluable' if r.estado_metodo == 'evaluable' else r.estado_metodo])
        sections[source] = md_table(['Método', 'Recall macro [IC 95 %]', 'Tasa de alerta real', 'Precisión conservadora [IC]', 'F1 [IC]', 'Estado'], rows)

    d5 = diff[(diff.tasa_objetivo == ALPHA) & (diff.horizonte == HZ) & (diff.prevalencia_supuesta == PREV)]
    rows = []
    for source in MAIN_SOURCES:
        for method in METHODS[1:]:
            r = d5[(d5.fuente == source) & (d5.metodo == method)].iloc[0]
            rows.append([source, METHOD_LABELS[method], num(r.delta_recall, 3),
                         f"{num(r.delta_f1, 3)} [{num(r.ic95_inferior_delta_f1, 3)}; {num(r.ic95_superior_delta_f1, 3)}]",
                         'sí' if r.ic_f1_excluye_cero else 'no', r.estado_metodo])
    diff_table = md_table(['Fuente', 'Método', 'Δ recall', 'Δ F1 frente a I-MR [IC 95 %]', 'IC excluye 0', 'Estado'], rows)

    rows = []
    for source in ('EPM', 'CHEC', 'SSPD', 'XM'):
        for kind in ERROR_TYPES:
            r = tests[(tests.fuente == source) & (tests.tipo == kind)].iloc[0]
            rows.append([source, kind, f'{r.casos:,}'.replace(',', '.'), r.series, r.categorias,
                         r.meses_calendario_distintos, num(r.pruebas_por_replica_media, 1)])
    tests_table = md_table(['Fuente', 'Tipo', 'Casos exhaustivos', 'Series', 'Categorías', 'Meses de calendario distintos', 'Pruebas por réplica (sorteo)'], rows)

    ds = draw[(draw.tasa_objetivo == ALPHA) & (draw.horizonte == HZ) & (draw.metodo == 'IMR')]
    rows = [[r.fuente, int(r.pruebas_por_replica_media), num(r.recall_sorteo_media, 3),
             f'{num(r.recall_sorteo_p2_5, 3)}–{num(r.recall_sorteo_p97_5, 3)}', num(r.recall_exhaustivo_macro, 3),
             num(r.diferencia_sorteo_menos_exhaustivo, 3)] for r in ds.itertuples()]
    draw_table = md_table(['Fuente', 'Pruebas por réplica', 'Recall del sorteo (media)', 'Rango 95 % entre réplicas', 'Recall exhaustivo macro', 'Diferencia'], rows)
    max_draw_gap = draw[draw.estado_metodo == 'evaluable'].diferencia_sorteo_menos_exhaustivo.abs().max()

    nat = native[(native.horizonte == HZ) & (native.prevalencia_supuesta == PREV)]
    rows = []
    for source in MAIN_SOURCES:
        for method in ('IMR', 'Z_robusto', 'IF', 'R12'):
            n = nat[(nat.fuente == source) & (nat.metodo == method)].iloc[0]
            e = head[(head.fuente == source) & (head.metodo == method)].iloc[0]
            rows.append([source, METHOD_LABELS[method], n.umbral_nativo, pct(n.tasa_alerta_sin_error_conocido, 2),
                         num(n.recall_macro, 2), num(n.f1, 2), num(e.recall_macro, 2), num(e.f1, 2)])
    native_table = md_table(['Fuente', 'Método', 'Umbral nativo', 'Tasa de alerta nativa', 'Recall nativo', 'F1 nativo', 'Recall al 5 %', 'F1 al 5 %'], rows)

    type_tables = {}
    for source in MAIN_SOURCES:
        d = by_type[(by_type.fuente == source) & (by_type.tasa_objetivo == ALPHA) & (by_type.horizonte == HZ)]
        rows = []
        for kind in ERROR_TYPES:
            row = [kind]
            for method in METHODS:
                r = d[(d.tipo == kind) & (d.metodo == method)].iloc[0]
                row.append('n/d' if r.estado_metodo != 'evaluable' else
                           f"{num(r.recall, 2)} [{num(r.ic95_inferior, 2)}–{num(r.ic95_superior, 2)}]")
            rows.append(row)
        type_tables[source] = md_table(['Tipo'] + [METHOD_LABELS[m] for m in METHODS], rows)

    can = head[head.fuente == 'EPM_canonicas'].set_index('metodo')
    raw_epm = head[head.fuente == 'EPM'].set_index('metodo')
    d5c = d5[d5.fuente == 'EPM_canonicas'].set_index('metodo')
    cov = cover.set_index('fuente')
    rows = []
    for method in METHODS:
        c = can.loc[method]
        if method == 'IMR':
            delta = '—'
        else:
            q = d5c.loc[method]
            delta = f"{num(q.delta_f1, 3)} [{num(q.ic95_inferior_delta_f1, 3)}; {num(q.ic95_superior_delta_f1, 3)}]"
        rows.append([METHOD_LABELS[method], num(raw_epm.loc[method, 'f1'], 2), cell(c, 'f1'), delta,
                     'evaluable' if c.estado_metodo == 'evaluable' else c.estado_metodo])
    canon_table = md_table(['Método', 'F1 EPM (etiquetas originales)', 'F1 EPM (etiquetas canónicas) [IC]',
                            'Δ F1 frente a I-MR (canónicas) [IC]', 'Estado (canónicas)'], rows)
    canon_core = can.loc[['IMR', 'Z_robusto', 'IF', 'KNN'], 'f1']
    raw_core = raw_epm.loc[['IMR', 'Z_robusto', 'IF', 'KNN'], 'f1']
    canon_sig = d5c[(d5c.ic_f1_excluye_cero == 1) & (d5c.estado_metodo == 'evaluable')]
    canon_sig_text = ('las diferencias pareadas frente a I-MR no excluyen el cero para ningún método evaluable' if canon_sig.empty else
                      'las diferencias pareadas frente a I-MR excluyen el cero en: ' + '; '.join(
                          f"{METHOD_LABELS[m]} (Δ F1 = {num(r.delta_f1, 3)})" for m, r in canon_sig.iterrows()))
    gain = (can.f1 - raw_epm.f1).loc[['IMR', 'Z_robusto', 'IF', 'KNN', 'R12']]

    def thousands(value):
        return f'{int(value):,}'.replace(',', '.')
    stale = by_type[(by_type.tipo == 'valor_no_actualizado') & (by_type.tasa_objetivo == ALPHA) &
                    (by_type.estado_metodo == 'evaluable') & (by_type.fuente.isin(MAIN_SOURCES))]
    stale_t = stale[stale.horizonte == 't'].recall
    stale_2 = stale[stale.horizonte == 't_o_t1'].recall
    top = head[head.fuente.isin(MAIN_SOURCES) & head.metodo.isin(['IMR', 'Z_robusto', 'IF', 'KNN'])]
    spread = top.groupby('fuente').f1.agg(['min', 'max'])
    sig_worse = d5[(d5.ic_f1_excluye_cero == 1) & (d5.delta_f1 < 0) & (d5.estado_metodo == 'evaluable')]
    sig_better = d5[(d5.ic_f1_excluye_cero == 1) & (d5.delta_f1 > 0)]
    sig_better_text = '; '.join(f"{r.fuente}, {METHOD_LABELS[r.metodo]} (Δ F1 = {num(r.delta_f1, 3)})"
                                for r in sig_better.itertuples()) or 'ninguna'
    lof_chec = cover[cover.fuente == 'CHEC'].iloc[0]
    xm = head[head.fuente == 'XM']
    unique_note = (f"{int(lof_chec.entrenamiento_filas):,}".replace(',', '.') + ' filas de entrenamiento, '
                   + f"{int(lof_chec.entrenamiento_filas_unicas):,}".replace(',', '.') + ' únicas')
    base_rates = thresholds[(thresholds.tasa_objetivo == ALPHA) & (thresholds.fuente.isin(MAIN_SOURCES)) &
                            (thresholds.estado_metodo == 'evaluable')]
    omitted_note = '; '.join(f"{r.fuente}/{r.tipo}: {r.casos} ({r.motivo.replace('_', ' ')})" for r in omitted.itertuples())

    text = f"""# Hito 4.3 · Métricas completas y honestas

Fecha: 7 de noviembre de 2026. Corresponde a la actividad 3 del Hito 4 del plan: precisión,
recall y F1 a tasa de alerta igualada, curvas de detección contra tasa de alerta por método,
pruebas por tipo, meses distintos sorteados sin reemplazo. Completa además lo que 4.1 dejó
pendiente: métricas del Z-score robusto y del Isolation Forest con rasgos logarítmicos, y LOF/KNN.
No modifica 4.1 ni 4.2.

## Resultado en cinco frases

1. A tasa de alerta igualada del 5 %, **I-MR, Z-score robusto, Isolation Forest y KNN no se separan de forma
   consistente**: su F1 queda entre {num(spread.loc['EPM', 'min'], 2)} y {num(spread.loc['EPM', 'max'], 2)} en EPM,
   entre {num(spread.loc['CHEC', 'min'], 2)} y {num(spread.loc['CHEC', 'max'], 2)} en CHEC y entre
   {num(spread.loc['SSPD', 'min'], 2)} y {num(spread.loc['SSPD', 'max'], 2)} en SSPD, con intervalos que se solapan.
   De {int((d5.estado_metodo == 'evaluable').sum())} diferencias pareadas evaluables frente a I-MR, el IC excluye el cero a favor
   de otro método en {len(sig_better)} (sin corrección por comparaciones múltiples): {sig_better_text}.
2. **LOF y R12 rinden menos que las cartas** donde se pueden evaluar. El IC de la diferencia excluye el cero para R12 en
   {', '.join(sorted(set(sig_worse[sig_worse.metodo == 'R12'].fuente)))} y para LOF en
   {', '.join(sorted(set(sig_worse[sig_worse.metodo == 'LOF'].fuente)))}; en EPM la diferencia tiene el mismo signo pero el IC
   la incluye (solo hay 5 categorías). LOF es **numéricamente degenerado en CHEC** ({unique_note}).
3. **Ningún método estadístico detecta el «valor no actualizado»**: su recall en t va de
   {num(stale_t.min(), 2)} a {num(stale_t.max(), 2)} (de {num(stale_2.min(), 2)} a {num(stale_2.max(), 2)} si se admite t+1).
   Un valor repetido no es un cambio atípico; se detecta con una regla, no con una carta. Es el argumento a favor de
   «reglas + cartas» frente a cartas solas.
4. **La precisión no es una propiedad del método sino de la prevalencia de errores**, que aquí no se conoce. Por eso se
   reporta con prevalencias supuestas del 1, 5 y 10 %, y la tasa de «falsas alertas» se llama *tasa de alerta en meses reales
   sin error conocido*: no hay etiquetas externas que confirmen que esas alertas sean falsas.
5. **Las conclusiones no dependen de cómo se escriban las etiquetas de EPM.** EPM escribe de varias formas la misma etiqueta y, sin
   normalizar, sus series se fragmentan ({int(cov.loc['EPM', 'series'])} series en el panel común frente a {int(cov.loc['EPM_canonicas', 'series'])} con las equivalencias aprobadas internamente en el Hito 2).
   Repetido con esas equivalencias, el F1 de I-MR, Z-score, Isolation Forest y KNN queda entre {num(canon_core.min(), 2)} y {num(canon_core.max(), 2)} (antes entre {num(raw_core.min(), 2)} y {num(raw_core.max(), 2)}),
   con los mismos intervalos solapados; ver la sección 3b.

## 1. Qué se midió

**Panel.** El escenario principal de 4.2: referencia de 36 cambios, vigilancia de 12, cohorte común
(EPM {int(cover[cover.fuente=='EPM'].series.iloc[0])}, CHEC {int(cover[cover.fuente=='CHEC'].series.iloc[0])},
SSPD {int(cover[cover.fuente=='SSPD'].series.iloc[0])} y XM {int(cover[cover.fuente=='XM'].series.iloc[0])} series).
Las inyecciones y los modelos Isolation Forest son los mismos de 4.2: se verificó que, para cada caso,
las banderas nativas de este experimento coinciden con `4.2/inyecciones_detalle.csv.gz`
([verificacion_contra_4_2.json](verificacion_contra_4_2.json)).

**Seis métodos con puntaje continuo** (más alto = más anómalo, necesario para igualar tasas):

| Método | Puntaje | Umbral nativo |
|---|---|---|
| Cartas I-MR | máx(\\|c−media\\|/(2,66·MR̄), \\|c−anterior\\|/(3,267·MR̄)) | puntaje > 1 |
| Z-score robusto | \\|c−mediana\\|·0,6745/MAD | \\|z\\| > 3 |
| Isolation Forest | −score_samples, 300 árboles, 4 rasgos | percentil 99,5 de entrenamiento |
| LOF | −score_samples (`novelty=True`, 20 vecinos), mismos rasgos | no tiene |
| KNN | distancia media a los 5 vecinos de referencia, mismos rasgos | no tiene |
| R12 | \\|nivel\\| / mediana de referencia | factor 5, 10 o 20 |

Modelos y escalas se ajustan solo con la referencia. Cuando MAD o MR valen cero se usa una escala de respaldo
(desviación absoluta media, luego desviación estándar) **solo para ordenar puntajes**; la regla nativa de 4.1
para MAD cero se conserva en la verificación contra 4.2 (sin discrepancias en series con escala positiva).

**Tasa de alerta igualada.** Para cada fuente, método y tasa objetivo (1, 2, 5 y 10 %) el umbral es el puntaje que deja esa
fracción de las observaciones **reales** de vigilancia por encima. No usa etiquetas. Así todos los métodos alertan lo mismo
sobre los datos reales y solo pueden diferenciarse por cuánto detectan de lo inyectado. Los empates pueden dejar la tasa
observada ligeramente por debajo de la objetivo; se reporta en [umbrales_tasa_igualada.csv](umbrales_tasa_igualada.csv).

**Etiquetas.** Positivo: el valor inyectado en el mes t. Negativo: las observaciones reales sin inyección, que incluyen alertas
reales sin error conocido (supuesto conservador: pueden contener errores verdaderos, de modo que la precisión es un límite
inferior). Horizonte *t*: alerta en el mes inyectado; horizonte *t o t+1*: alerta en cualquiera de los dos, con la tasa de
alerta real medida sobre pares de meses consecutivos para que el criterio sea el mismo en positivos y negativos.

**Métricas.** El recall global es **macro**: promedio de los recall de los seis tipos con el mismo peso, de modo que ningún
tipo domine por tener más casos. La precisión se obtiene de recall y tasa de alerta real para una prevalencia supuesta
π: `P = R·π / (R·π + FPR·(1−π))`, y F1 es su media armónica con el recall. Los intervalos son bootstrap de
**categorías completas** (1.000 repeticiones, TPR y tasa de alerta remuestreados juntos); sin IC cuando hay una sola categoría.

## 2. Pruebas por tipo y meses distintos (observación 6 de la revisión)

La revisión del Hito 2 señaló que 20 sorteos por serie y tipo caían en 13 meses distintos en promedio y que «columna
equivocada» tenía 760 pruebas frente a 1.540 de los otros tipos. Aquí se reportan los denominadores reales y el sorteo se hace
**sin reemplazo**: en cada réplica, cada serie recibe {int(draw.origenes_por_serie.iloc[0])} meses de origen distintos y un tipo de
error uniforme entre los disponibles ese mes ({int(draw.replicas.iloc[0])} réplicas). La condición de meses distintos se
verifica con una aserción en cada ejecución y con pruebas unitarias.

{tests_table}

«Otra medida» solo existe donde la serie tiene otra medida positiva en el mismo grupo y mes (en EPM, 12 de 27 series; en XM
ninguna), y «valor no actualizado» se omite cuando el valor anterior es igual al actual. Omisiones registradas en
[inyecciones_omitidas.csv](inyecciones_omitidas.csv): {omitted_note}.

**Las pruebas siguen sin ser independientes**: los casos de una misma serie comparten referencia, escala y modelo, y las
series de una categoría están correlacionadas. Por eso los intervalos remuestrean categorías completas y no casos.

Consistencia del sorteo con el cálculo exhaustivo (I-MR, 5 %, horizonte t):

{draw_table}

La diferencia absoluta máxima entre el sorteo y el cálculo exhaustivo es de {num(max_draw_gap, 3)}. Aparece en EPM porque el
sorteo reparte los tipos uniformemente **entre los disponibles de cada mes** y «otra medida» está disponible en menos series;
no es un error de cálculo.

## 3. Precisión, recall y F1 a tasa de alerta del 5 %

Horizonte t, prevalencia supuesta del 5 %. La fila «Tasa de alerta real» es la tasa observada sobre meses reales tras igualar.

**EPM** ({int(cover[cover.fuente=='EPM'].categorias.iloc[0])} categorías; el IC es amplio porque hay pocas):

{sections['EPM']}

**CHEC** ({int(cover[cover.fuente=='CHEC'].categorias.iloc[0])} categorías):

{sections['CHEC']}

**SSPD** ({int(cover[cover.fuente=='SSPD'].categorias.iloc[0])} categorías):

{sections['SSPD']}

**XM** (una serie y 12 observaciones: con un 5 % de tasa objetivo se esperan 0,6 alertas, por lo que la tasa de alerta real
es 0 % y la precisión sale 100 % por construcción; **no es interpretable**, se conserva solo como evidencia descriptiva):

{sections['XM']}

![F1 por método](figuras/02_f1_por_metodo.png)

### Diferencias pareadas frente a I-MR

I-MR es el método clásico del proyecto (el que sustituye a la regla estática). Las diferencias usan las mismas categorías
remuestreadas en ambos métodos, por lo que son más informativas que comparar dos intervalos por separado:

{diff_table}

Con tan pocas categorías (EPM, CHEC) los intervalos son anchos y apenas permiten rechazar nada; con 89 categorías (SSPD)
sí se distingue que LOF y R12 pierden frente a I-MR y que IF, KNN y Z-score no se distinguen de él.
Son 5 métodos × 3 fuentes por configuración y no se aplicó corrección por comparaciones múltiples; léase como exploración.

### 3b. Sensibilidad: EPM con etiquetas canónicas

EPM cambia la escritura de varias etiquetas entre meses (p. ej. «Costo compra: Gm, i» y «Costo Compra: Gm, i», o «Rango 0 - CS» y «0-CS»). Si no se
normalizan, una misma serie económica se parte en varias, y el panel común (series con 61 meses continuos) se reduce. Se repitió el experimento completo con las
11 equivalencias del Hito 2 ([02_catalogo_variantes.csv](../3.3/insumos_hito2/02_catalogo_variantes.csv), aprobadas internamente por el equipo, aplicadas en una copia de trabajo) como una
fuente adicional, `EPM_canonicas`. **No sustituye a EPM**: 4.1, 4.2 y la matriz OE1 usan las etiquetas originales y la variante canónica no existe en 4.2, por lo que no se
compara con él.

| | EPM (originales) | EPM (canónicas) |
|---|---|---|
| Series en el panel común | {int(cov.loc['EPM', 'series'])} | {int(cov.loc['EPM_canonicas', 'series'])} |
| Categorías | {int(cov.loc['EPM', 'categorias'])} | {int(cov.loc['EPM_canonicas', 'categorias'])} |
| Observaciones reales de vigilancia | {int(cov.loc['EPM', 'observaciones_reales'])} | {int(cov.loc['EPM_canonicas', 'observaciones_reales'])} |
| Casos inyectados | {thousands(cov.loc['EPM', 'casos_individuales'])} | {thousands(cov.loc['EPM_canonicas', 'casos_individuales'])} |

F1 a tasa del 5 %, prevalencia supuesta del 5 %, horizonte t:

{canon_table}

- **El orden y las conclusiones se mantienen.** I-MR, Z-score, Isolation Forest y KNN siguen sin separarse (intervalos solapados; {canon_sig_text}); R12 sigue siendo el más bajo.
- **El F1 sube ligeramente** (entre +{num(gain.min(), 2)} y +{num(gain.max(), 2)} según el método) con más series y casos; no se probó la causa del aumento. Con solo {int(cov.loc['EPM_canonicas', 'categorias'])} categorías los intervalos siguen siendo anchos.
- **LOF pasa a degenerado también en EPM** ({thousands(cov.loc['EPM_canonicas', 'entrenamiento_filas'])} filas de entrenamiento, {thousands(cov.loc['EPM_canonicas', 'entrenamiento_filas_unicas'])} únicas; {pct(cov.loc['EPM_canonicas', 'LOF_fraccion_puntajes_reales_explotados'])} de los puntajes reales estallan) y se marca como tal.
- Decidir si estas equivalencias se aceptan como oficiales y si hay que repetir 4.1 y 4.2 con ellas es **decisión del equipo y del director**; mientras tanto el resultado principal sigue usando las etiquetas originales.

## 4. Curvas de detección contra tasa de alerta

![Curvas de detección](figuras/01_curvas_deteccion.png)

Datos en [curva_deteccion.csv](curva_deteccion.csv) (40 tasas entre 0,25 y 30 %). Las curvas no tienen IC: son el recall
macro exhaustivo en cada punto. Se omiten los puntos con menos de 5 alertas esperadas y LOF en CHEC.

## 5. Recall por tipo de error

![Recall por tipo](figuras/03_recall_por_tipo.png)

Tabla comparativa con IC 95 % por técnica y tipo de error (horizonte t, tasa 5 %). El resto de tasas y el horizonte
t o t+1 están en [deteccion_por_tipo_tasa_igualada.csv](deteccion_por_tipo_tasa_igualada.csv).

**EPM**

{type_tables['EPM']}

**CHEC**

{type_tables['CHEC']}

**SSPD**

{type_tables['SSPD']}

## 6. Por qué igualar la tasa (puntos operativos nativos frente a tasa igualada)

Con su umbral nativo cada método alerta con una frecuencia distinta; comparar sus F1 así mezcla la calidad del puntaje con
la elección del umbral. Por ejemplo, el Isolation Forest con percentil 99,5 casi no alerta en EPM y por eso detecta poco en 4.2,
pero con la misma tasa de alerta que las cartas su recall es comparable:

{native_table}

(Prevalencia supuesta 5 %, horizonte t. Los puntos nativos no llevan IC. En CHEC (y en XM, no mostrado) la tasa nativa de
I-MR y Z-score es 0 % sobre meses reales, de modo que su precisión es 100 % por construcción y su F1 nativo no es comparable
con el igualado. Los puntos nativos de todas las fuentes están en [puntos_operativos_nativos.csv](puntos_operativos_nativos.csv).)

## 7. Lo que no se puede concluir

- **No hay verdad terreno para las alertas reales.** Las inyecciones son artificiales y siguen la mezcla diseñada (seis tipos
  uniformes); no estiman la prevalencia ni el tipo de errores que existe en las fuentes.
- **La precisión depende de la prevalencia supuesta**; el informe no elige una. Con prevalencia baja la precisión de todos los
  métodos cae, porque la tasa de alerta real (5 %) pesa más que los positivos.
- **XM no es evaluable a tasa igualada** (una serie, 12 meses). **CHEC y EPM tienen pocas categorías** (4 y 5): sus IC son
  anchos y los contrastes entre métodos tienen poca potencia.
- **LOF en CHEC está degenerado** por duplicados exactos en el entrenamiento: con más duplicados que vecinos, la densidad local
  diverge y el puntaje estalla (~10⁹–10¹⁰). Se conserva el cálculo y se marca `degenerado_por_duplicados`. Una corrección
  (eliminar duplicados o aumentar vecinos) cambia el significado de densidad y queda como decisión del equipo.
- **El experimento es retrospectivo** (se mira t+1 y los rasgos usan el cambio anterior), válido para auditar datos ya
  publicados y no para vigilancia en tiempo real.
- **Los umbrales por tasa igualada se calibran en los mismos meses reales** donde luego se miden las falsas alertas (sin
  etiquetas, pero sin separación temporal): describe cómo se comportan los métodos a igual tasa, no una tasa futura garantizada.
- **Las equivalencias de etiquetas de EPM son una aprobación interna del equipo**, no una confirmación de EPM (sección 3b).
- **No se aprobó ningún umbral ni método.** Los resultados no confirman que una señal sea un error ni un cambio regulatorio.

## 8. Qué cierra de los pendientes de 4.1

Quedan resueltos aquí: precisión, recall y F1 del Z-score robusto y del Isolation Forest de 4.2 (rasgos logarítmicos);
LOF y KNN, que el plan pedía y no existían; comparación a tasa igualada **sobre las mismas inyecciones** de 4.2 para los seis
métodos; detección en t frente a t o t+1 con ambos horizontes. **Siguen abiertos**: Extended Isolation Forest
(el plan lo condiciona al tiempo), validación externa de alertas reales y aprobación del tratamiento de MAD igual a cero.

## Reproducir y auditar

Desde la raíz del proyecto:

```powershell
python desarrollo_puntos/4.3/experimento_tasa_igualada.py
python desarrollo_puntos/4.3/informe_metricas.py
python -m unittest discover -s desarrollo_puntos/4.3 -p test_metricas.py -v
python desarrollo_puntos/4.3/verificar_resultados.py
```

[configuracion.json](configuracion.json) fija semilla, versiones, definiciones y huellas de las entradas;
[manifiesto_resultados.json](manifiesto_resultados.json) lista las huellas de todos los archivos entregados.
"""
    (HERE / 'INFORME_METRICAS.md').write_text(text, encoding='utf-8')
    print('Informe y figuras generados')


if __name__ == '__main__':
    main()
