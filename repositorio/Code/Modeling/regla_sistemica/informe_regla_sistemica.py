"""Genera figuras e INFORME_REGLA_SISTEMICA.md de 4.4 a partir de las tablas ya calculadas."""
from __future__ import annotations

from pathlib import Path as _ProjectPath
_PROJECT_ROOT = next(p for p in _ProjectPath(__file__).resolve().parents if (p / "project.json").is_file())

import sys
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402

HERE = (_PROJECT_ROOT / 'Data/gold/outputs/regla_sistemica')
sys.dont_write_bytecode = True
sys.path.insert(0, str((_PROJECT_ROOT / 'Code/Modeling/regla_sistemica')))
import regla_sistemica as R  # noqa: E402

INK, INK2, MUTED, GRID, BASE, SURFACE = '#0b0b0b', '#52514e', '#898781', '#e1e0d9', '#c3c2b7', '#fcfcfb'
# Color por entidad (ranuras 1-5 de la paleta de referencia): misma variante, mismo color en todas las figuras.
VARIANTS = {
    ('canonicas', 36, 'IMR_clasica'): ('I-MR, ref. 36', '#2a78d6'),
    ('canonicas', 36, 'MAD_3sigma'): ('MAD 3σ, ref. 36', '#eb6834'),
    ('canonicas', 24, 'IMR_clasica'): ('I-MR, ref. 24', '#1baf7a'),
    ('canonicas', 24, 'MAD_3sigma'): ('MAD 3σ, ref. 24', '#eda100'),
    ('canonicas_hito2', 36, 'IMR_clasica_hito2'): ('Hito 2 (origen fijo, 83 series)', '#e87ba4'),
}
EVENT_LABEL = {'2020-02': 'feb-2020', '2020-07': 'jul-2020', '2021-07': 'jul-2021'}


def pct(x, digits=1):
    return f'{100 * x:.{digits}f}'.replace('.', ',') + ' %'


def num(x, digits=2):
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
    ((_PROJECT_ROOT / 'Data/gold/outputs/regla_sistemica/figuras')).mkdir(exist_ok=True)
    for ext in ('png', 'svg', 'pdf'):
        fig.savefig((_PROJECT_ROOT / 'Data/gold/outputs/regla_sistemica/figuras') / f'{name}.{ext}', dpi=200, bbox_inches='tight')
    plt.close(fig)


def md_table(header, rows):
    out = ['| ' + ' | '.join(header) + ' |', '|' + '|'.join(['---'] * len(header)) + '|']
    out += ['| ' + ' | '.join(str(c) for c in r) + ' |' for r in rows]
    return '\n'.join(out)


def pick(frame, etiquetas, referencia, metodo, fuente='EPM'):
    return frame[(frame.fuente == fuente) & (frame.etiquetas == etiquetas) &
                 (frame.referencia == referencia) & (frame.metodo == metodo)].sort_values('periodo')


# ----------------------------------------------------------------------- figuras
def figure_timeline(fr):
    fig, ax = plt.subplots(figsize=(10.5, 4.3))
    months = [R.period_label(2020 * 12 + i) for i in range(24)]
    xs = np.arange(len(months))
    for event in R.EVENT_MONTHS:
        if event in months:
            ax.axvspan(months.index(event) - 0.5, months.index(event) + 0.5, color='#e1e0d9', alpha=0.7, linewidth=0)
            ax.text(months.index(event), 0.98, EVENT_LABEL[event], ha='center', va='top', fontsize=8.5, color=INK2)
    for key in (('canonicas', 36, 'IMR_clasica'), ('canonicas', 36, 'MAD_3sigma'), ('canonicas_hito2', 36, 'IMR_clasica_hito2')):
        label, color = VARIANTS[key]
        d = pick(fr, *key).set_index('periodo').reindex(months)
        ax.plot(xs, d.fraccion, color=color, label=label, marker='o', markersize=4.5, markeredgecolor=SURFACE, markeredgewidth=1.2)
    for x, name in ((0.10, '10 %'), (0.25, '25 % (trabajo)'), (0.50, '50 %')):
        ax.axhline(x, color=MUTED, linewidth=0.9, linestyle=(0, (2, 3)))
        ax.text(len(months) - 0.4 if x >= 0.25 else 3.5, x + 0.008, name, ha='right' if x >= 0.25 else 'left',
                va='bottom', fontsize=8.3, color=INK2)
    ax.set_xticks(xs[::2])
    ax.set_xticklabels(months[::2], rotation=45, ha='right', fontsize=8.5)
    ax.set_ylim(0, 1.0)
    ax.set_yticks(np.arange(0, 1.01, 0.2))
    ax.set_yticklabels([f'{int(100 * v)} %' for v in np.arange(0, 1.01, 0.2)])
    ax.set_ylabel('Series con alerta / series evaluadas')
    ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.2), ncol=3, fontsize=9)
    ax.set_title('EPM: fracción mensual de series con alerta (2020-2021)', loc='left', fontsize=11.5, fontweight='bold')
    save(fig, '01_fraccion_mensual_epm')


def figure_sources(fr):
    fig, axes = plt.subplots(1, 2, figsize=(11.5, 3.9), sharey=True)
    for ax, (source, title) in zip(axes, (('CHEC', 'CHEC (4 categorías, hasta 270 series)'), ('SSPD', 'SSPD ZNI (hasta 337 series)'))):
        d = pick(fr, 'originales', 36, 'IMR_clasica', source)
        d = d[d.aplicable == 1]
        dates = pd.to_datetime(d.periodo + '-01')
        ax.vlines(dates, 0, d.fraccion, color='#2a78d6', linewidth=1.6)
        ax.plot(dates, d.fraccion, 'o', color='#2a78d6', markersize=3.8, markeredgecolor=SURFACE, markeredgewidth=0.8)
        ax.axhline(R.X_WORK, color=MUTED, linewidth=0.9, linestyle=(0, (2, 3)))
        ax.text(dates.iloc[0], R.X_WORK + 0.012, '25 % (trabajo)', fontsize=8.3, color=INK2)
        ax.set_title(title, loc='left', fontsize=10.5, fontweight='bold')
        ax.set_ylim(0, 1.05)
    top = pick(fr, 'originales', 36, 'IMR_clasica', 'CHEC').set_index('periodo').loc['2020-02']
    axes[0].annotate(f"feb-2020: {int(top.series_con_alerta)} de {int(top.series_evaluadas)} series",
                     xy=(pd.Timestamp('2020-02-01'), top.fraccion), xytext=(pd.Timestamp('2013-06-01'), 0.9),
                     fontsize=8.8, color=INK, arrowprops=dict(arrowstyle='-', color=MUTED, lw=0.9))
    axes[0].set_ylabel('Series con alerta / series evaluadas')
    axes[0].set_yticks(np.arange(0, 1.01, 0.2))
    axes[0].set_yticklabels([f'{int(100 * v)} %' for v in np.arange(0, 1.01, 0.2)])
    fig.suptitle('Otras fuentes: la regla se comporta de forma muy distinta (I-MR, referencia 36)', x=0.01, ha='left',
                 fontsize=11.5, fontweight='bold')
    fig.subplots_adjust(top=0.82, wspace=0.06)
    save(fig, '02_fraccion_mensual_chec_sspd')


def figure_calibration(calibration):
    fig, axes = plt.subplots(1, 2, figsize=(11.5, 3.9))
    for key, (label, color) in VARIANTS.items():
        d = calibration[(calibration.etiquetas == key[0]) & (calibration.referencia == key[1]) & (calibration.metodo == key[2])]
        axes[0].step(100 * d.umbral_X, d.eventos_capturados, where='post', color=color, label=label)
        axes[1].step(100 * d.umbral_X, d.meses_fondo_marcados, where='post', color=color, label=label)
    axes[0].set_ylabel('Meses del plan capturados (de 3)')
    axes[0].set_yticks([0, 1, 2, 3])
    axes[1].set_ylabel('Otros meses marcados como sistémicos')
    for ax in axes:
        ax.set_xlabel('Umbral X (% de series con alerta)')
        ax.axvline(100 * R.X_WORK, color=MUTED, linewidth=0.9, linestyle=(0, (2, 3)))
    handles, labels = axes[0].get_legend_handles_labels()
    fig.legend(handles, labels, loc='lower center', ncol=5, bbox_to_anchor=(0.5, -0.1), fontsize=8.8)
    fig.suptitle('Calibración de X: ningún valor captura los tres meses sin marcar otros', x=0.01, ha='left', fontsize=11.5, fontweight='bold')
    fig.subplots_adjust(top=0.84, wspace=0.18)
    save(fig, '03_calibracion_X')


def figure_contrast(contrast):
    fig, axes = plt.subplots(1, 3, figsize=(16, 3.9))
    for ax, (base, month) in zip(axes, (('2020-01', '2020-02'), ('2020-06', '2020-07'), ('2021-06', '2021-07'))):
        d = contrast[(contrast.mes == month) & (~contrast.componente.str.startswith('CU'))].reset_index(drop=True)
        for i, r in d.iterrows():
            y = len(d) - 1 - i
            name = r.componente.replace('�', 'ó')
            if pd.isna(r.cambio_porcentual):
                ax.text(0.4, y, f'cruza cero ({num(r.valor_base)} → {num(r.valor_mes)})', va='center', fontsize=8.5, color=MUTED)
            else:
                shown = min(r.cambio_porcentual, 55.0)
                ax.barh(y, shown, color='#2a78d6', height=0.55)
                if r.cambio_porcentual > 55.0:
                    ax.text(54, y, f'{num(r.cambio_porcentual, 1)} % (fuera de escala)', va='center', ha='right',
                            fontsize=8.3, color='#ffffff')
                else:
                    ax.text(r.cambio_porcentual + (0.6 if r.cambio_porcentual >= 0 else -0.6), y, f'{num(r.cambio_porcentual, 1)} %',
                            va='center', ha='left' if r.cambio_porcentual >= 0 else 'right', fontsize=8.5, color=INK2)
        ax.set_yticks(range(len(d)))
        ax.set_yticklabels([c.replace('�', 'ó').split(':')[0] for c in d.componente][::-1], fontsize=8.8)
        ax.axvline(0, color=BASE, linewidth=1.0)
        ax.set_title(f'{base} → {month}', loc='left', fontsize=10.5, fontweight='bold')
        ax.set_xlabel('Cambio porcentual publicado (nivel I, Propiedad EPM)')
        ax.grid(axis='y', visible=False)
        ax.set_xlim(-37, 56)
        ax.set_ylim(-0.7, len(d) - 0.3)
    fig.suptitle('Publicaciones oficiales de EPM: variación de cada componente del costo unitario', x=0.01, ha='left', fontsize=11.5, fontweight='bold')
    fig.subplots_adjust(top=0.84, wspace=0.7)
    save(fig, '04_contraste_publicaciones_epm')


# ----------------------------------------------------------------------- informe
def main():
    style()
    fr = pd.read_csv((_PROJECT_ROOT / 'Data/gold/outputs/regla_sistemica/fracciones_mensuales.csv'))
    calibration = pd.read_csv((_PROJECT_ROOT / 'Data/gold/outputs/regla_sistemica/calibracion_X.csv'))
    summary = pd.read_csv((_PROJECT_ROOT / 'Data/gold/outputs/regla_sistemica/calibracion_resumen.csv'))
    effect = pd.read_csv((_PROJECT_ROOT / 'Data/gold/outputs/regla_sistemica/efecto_regla_sobre_alertas_reales.csv'))
    cost = pd.read_csv((_PROJECT_ROOT / 'Data/gold/outputs/regla_sistemica/costo_enmascaramiento_4_2.csv'))
    contrast = pd.read_csv((_PROJECT_ROOT / 'Data/gold/outputs/regla_sistemica/contraste_componentes.csv'))
    composition = pd.read_csv((_PROJECT_ROOT / 'Data/gold/outputs/regla_sistemica/composicion_alertas_meses_plan.csv'))
    h2 = pd.read_csv((_PROJECT_ROOT / 'Data/gold/outputs/regla_sistemica/reproduccion_hito2.csv'))
    refs = pd.read_csv((_PROJECT_ROOT / 'Data/gold/outputs/regla_sistemica/evidencia_externa/referencias_documentales.csv'))
    catalog = pd.read_csv((_PROJECT_ROOT / 'Data/gold/outputs/regla_sistemica/catalogo_alertas_sistemicas.csv'))
    figure_timeline(fr)
    figure_sources(fr)
    figure_calibration(calibration)
    figure_contrast(contrast)

    # ---- tabla de calibración por variante
    rows = []
    for key, (label, _) in VARIANTS.items():
        r = summary[(summary.etiquetas == key[0]) & (summary.referencia == key[1]) & (summary.metodo == key[2])].iloc[0]
        rows.append([label, pct(r['fraccion_2020-02']), pct(r['fraccion_2020-07']), pct(r['fraccion_2021-07']),
                     pct(r.X_minimo_para_no_marcar_fondo), pct(r.X_maximo_para_capturar_todos),
                     'sí' if r.banda_factible else 'no', f"{int(r.eventos_capturados_en_X_trabajo)} de 3 · {int(r.meses_marcados_en_X_trabajo)}"])
    orig = summary[summary.etiquetas == 'originales']
    calibration_table = md_table(['Variante (EPM)', 'feb-2020', 'jul-2020', 'jul-2021', 'X mínimo para no marcar otro mes', 'X máximo para capturar los tres', '¿Banda factible?', 'En X = 25 %: eventos · meses marcados'], rows)
    ev = summary[summary.etiquetas.isin(['canonicas', 'originales'])]
    feb_lo, feb_hi = ev['fraccion_2020-02'].min(), ev['fraccion_2020-02'].max()
    jul20_lo, jul20_hi = ev['fraccion_2020-07'].min(), ev['fraccion_2020-07'].max()
    jul21_lo, jul21_hi = ev['fraccion_2021-07'].min(), summary['fraccion_2021-07'].max()
    jul21_log_hi = ev['fraccion_2021-07'].max()
    canon = summary[summary.etiquetas == 'canonicas']
    h2s = summary[summary.etiquetas == 'canonicas_hito2'].iloc[0]
    h2f = h2.set_index('periodo').fraccion
    apr20 = h2f['2020-04']
    best_x = summary[summary.etiquetas.isin(['canonicas', 'originales'])].X_mejor_exactitud_balanceada

    # ---- efecto sobre alertas reales y costo de enmascaramiento
    eff_rows = []
    for source, labels in (('EPM', 'canonicas'), ('CHEC', 'originales'), ('SSPD', 'originales')):
        for method in R.METHOD_COLUMNS:
            line = [source, 'I-MR' if method == 'IMR_clasica' else 'MAD 3σ']
            for x in (0.10, 0.25, 0.50):
                e = effect[(effect.fuente == source) & (effect.etiquetas == labels) & (effect.referencia == 36) &
                           (effect.metodo == method) & (effect.umbral_X == x)].iloc[0]
                n_months = int(e.meses_marcados_total)
                line.append(f"{n_months} {'mes' if n_months == 1 else 'meses'} · {pct(e.fraccion_alertas_reclasificadas, 0)}")
            eff_rows.append(line)
    effect_table = md_table(['Fuente', 'Método', 'X = 10 %: meses sistémicos · alertas reclasificadas', 'X = 25 %', 'X = 50 %'], eff_rows)
    cost_rows = []
    for source in ('EPM', 'CHEC', 'SSPD'):
        for method in R.METHOD_COLUMNS:
            line = [source, 'I-MR' if method == 'IMR_clasica' else 'MAD 3σ']
            for klass in ('individual', 'colectivo'):
                for x in (0.10, 0.25, 0.50):
                    c = cost[(cost.fuente == source) & (cost.metodo == method) & (cost.clase_ensayo == klass) & (cost.umbral_fraccion == x)].iloc[0]
                    line.append(pct(c.fraccion_enmascarada, 1))
            cost_rows.append(line)
    cost_table = md_table(['Fuente', 'Método', 'Individual X=10 %', 'X=25 %', 'X=50 %', 'Colectivo X=10 %', 'X=25 %', 'X=50 %'], cost_rows)

    chec = fr[(fr.fuente == 'CHEC') & (fr.referencia == 36) & (fr.metodo == 'IMR_clasica') & (fr.aplicable == 1)]
    chec_feb = chec[chec.periodo == '2020-02'].iloc[0]
    chec_over = int((chec.fraccion > R.X_WORK).sum())
    sspd = fr[(fr.fuente == 'SSPD') & (fr.referencia == 36) & (fr.aplicable == 1)]
    sspd_max = sspd.fraccion.max()
    block = pd.read_csv((_PROJECT_ROOT / 'Data/gold/outputs/regla_sistemica/tamano_componentes_epm.csv'))
    block_max = block.fraccion_si_alertan_todas.max()
    block_row = block.loc[block.fraccion_si_alertan_todas.idxmax()]
    cfg_n = pd.read_csv((_PROJECT_ROOT / 'Data/gold/outputs/regla_sistemica/fracciones_mensuales.csv'), usecols=['fuente', 'etiquetas', 'referencia', 'metodo', 'periodo', 'series_evaluadas'])
    inventory = pd.read_csv((_PROJECT_ROOT / 'Data/gold/outputs/regla_sistemica/inventario_series_por_variante.csv')).set_index(['fuente', 'etiquetas'])
    epm_c = int(inventory.loc[('EPM', 'canonicas'), 'series_totales'])
    epm_o = int(inventory.loc[('EPM', 'originales'), 'series_totales'])
    e25 = effect[(effect.fuente == 'EPM') & (effect.etiquetas == 'canonicas') & (effect.referencia == 36) & (effect.umbral_X == 0.25)].fraccion_alertas_reclasificadas
    coll_all = cost[(cost.clase_ensayo == 'colectivo') & (cost.umbral_fraccion == 0.25) & cost.fuente.isin(['EPM', 'CHEC', 'SSPD'])].fraccion_enmascarada
    coll_50 = cost[(cost.clase_ensayo == 'colectivo') & (cost.umbral_fraccion == 0.50) & cost.fuente.isin(['EPM', 'CHEC', 'SSPD'])].fraccion_enmascarada

    # ---- composición y contraste
    comp = composition[(composition.etiquetas == 'canonicas') & (composition.referencia == 36) & (composition.metodo == 'MAD_3sigma')]
    comp_h2 = composition[composition.etiquetas == 'canonicas_hito2']
    breadth_rows = []
    for month in R.EVENT_MONTHS:
        a = comp_h2[comp_h2.periodo == month]
        b_imr = fr[(fr.fuente == 'EPM') & (fr.etiquetas == 'canonicas') & (fr.referencia == 36) & (fr.metodo == 'IMR_clasica') & (fr.periodo == month)]
        b_mad = fr[(fr.fuente == 'EPM') & (fr.etiquetas == 'canonicas') & (fr.referencia == 36) & (fr.metodo == 'MAD_3sigma') & (fr.periodo == month)]
        breadth_rows.append([EVENT_LABEL[month], f"{int(a.series_con_alerta.sum())} de 83 · {a.componente.nunique()} componentes",
                             f"{int(b_imr.series_con_alerta.iloc[0])} de {int(b_imr.series_evaluadas.iloc[0])} · {int(b_imr.componentes_con_alerta.iloc[0])} de {int(b_imr.componentes_evaluados.iloc[0])}",
                             f"{int(b_mad.series_con_alerta.iloc[0])} de {int(b_mad.series_evaluadas.iloc[0])} · {int(b_mad.componentes_con_alerta.iloc[0])} de {int(b_mad.componentes_evaluados.iloc[0])}"])
    breadth_table = md_table(['Mes', 'Hito 2: series · componentes con alerta', 'I-MR ref. 36: series · componentes', 'MAD 3σ ref. 36: series · componentes'], breadth_rows)

    contrast_tables = {}
    for base, month in (('2020-01', '2020-02'), ('2020-06', '2020-07'), ('2021-06', '2021-07')):
        d = contrast[contrast.mes == month]
        rows = []
        for r in d.itertuples(index=False):
            name = str(r.componente).replace('�', 'ó')
            if str(r.componente).startswith('CU total'):
                rows.append([name, num(r.valor_base), num(r.valor_mes), f'{num(r.cambio_porcentual, 1)} %', '—', '—', '—', r.observacion if isinstance(r.observacion, str) else ''])
                continue
            change = 'cruza cero' if pd.isna(r.cambio_porcentual) else f'{num(r.cambio_porcentual, 1)} %'

            def share(method):
                return f"{int(getattr(r, f'series_con_alerta_{method}_W36'))}/{int(r.series_evaluadas_W36)}"
            rows.append([name, num(r.valor_base), num(r.valor_mes), change, share('IMR_clasica'), share('MAD_3sigma'),
                         f"{int(r.series_con_alerta_hito2_IMR_absoluta)}", ''])
        contrast_tables[month] = md_table(['Componente', f'{base}', f'{month}', 'Cambio publicado', 'Alertas I-MR (ref. 36)', 'Alertas MAD (ref. 36)', 'Alertas Hito 2', 'Nota'], rows)

    refs_table = md_table(['Id', 'Mes', 'Documento', 'Estado', 'Límite'],
                          [[r.id, r.mes_asociado, r.documento, r.estado, r.limite if isinstance(r.limite, str) else ''] for r in refs.itertuples(index=False)])
    masking_epm_25 = cost[(cost.fuente == 'EPM') & (cost.clase_ensayo == 'individual') & (cost.umbral_fraccion == 0.25)].set_index('metodo').fraccion_enmascarada
    masking_max_10 = cost[(cost.clase_ensayo == 'individual') & (cost.umbral_fraccion == 0.10) & cost.fuente.isin(['EPM', 'CHEC', 'SSPD'])].fraccion_enmascarada.max()
    masking_max_25 = cost[(cost.clase_ensayo == 'individual') & (cost.umbral_fraccion == 0.25) & cost.fuente.isin(['EPM', 'CHEC', 'SSPD'])].fraccion_enmascarada.max()
    coll_25 = cost[(cost.clase_ensayo == 'colectivo') & (cost.umbral_fraccion == 0.25) & cost.fuente.isin(['EPM', 'CHEC'])].fraccion_enmascarada
    canon_event_flag = canon.eventos_capturados_en_X_trabajo.tolist(), canon.meses_marcados_en_X_trabajo.tolist()
    all_background_free = all(a == b for a, b in zip(*canon_event_flag))
    pe = fr[(fr.fuente == 'EPM') & (fr.etiquetas == 'canonicas') & (fr.referencia == 36) & (fr.metodo == 'IMR_clasica')].set_index('periodo')

    text = f"""# Hito 4.4 · Regla de alerta sistémica

Fecha: 7 de noviembre de 2026. Corresponde a la actividad 4 del Hito 4: *«Si más de X % de las series alertan en el
mismo mes, se clasifica como cambio regulatorio y no como error de dato; calibrar X con feb-2020 (51 de 83), jul-2020 (24)
y jul-2021 (18). Contrastar con resoluciones CREG y publicaciones tarifarias de EPM de esos meses»*. Entrega el catálogo
de alertas sistémicas del Hito 4. No modifica 4.1, 4.2 ni 4.3.

## Resultado en seis frases

1. **Se reproducen las cifras del plan** desde los archivos del Hito 2: 51 de 83 series en feb-2020 ({pct(h2f['2020-02'])}),
   24 en jul-2020 ({pct(h2f['2020-07'])}) y 18 en jul-2021 ({pct(h2f['2021-07'])}). Pero provienen de un protocolo distinto
   al del Hito 3 (origen fijo y diferencia absoluta). Con cambios logarítmicos y ventana móvil, **solo febrero de 2020 es sistémico
   en todas las variantes** ({pct(feb_lo, 0)}–{pct(feb_hi, 0)} de las series); jul-2020 ({pct(jul20_lo, 0)}–{pct(jul20_hi, 0)}) y
   jul-2021 ({pct(jul21_lo, 0)}–{pct(jul21_log_hi, 0)}) dependen de la ventana, del método y de las etiquetas.
2. **X no se puede calibrar de forma única con esos tres meses**: en ninguna variante hay un X que capture los tres sin marcar otros.
   Incluso con las cifras del Hito 2, abril de 2020 ({pct(apr20)}) supera a jul-2021 ({pct(h2f['2021-07'])}): un X por debajo de {pct(h2f['2021-07'])}
   los captura a los tres pero también marca abril. Los tres meses tampoco son del mismo tipo: involucran
   {int(comp_h2[comp_h2.periodo == '2020-02'].componente.nunique())}, {int(comp_h2[comp_h2.periodo == '2020-07'].componente.nunique())} y
   {int(comp_h2[comp_h2.periodo == '2021-07'].componente.nunique())} componentes tarifarios, respectivamente.
3. **Se propone X = 25 % como valor de trabajo, no aprobado.** En las cuatro variantes con etiquetas canónicas {'solo marca meses del plan (ningún otro mes)' if all_background_free else 'marca meses del plan y algún otro'},
   enmascara como máximo {pct(masking_max_25)} de los errores individuales inyectados (con X = 10 % llega a {pct(masking_max_10)}) y
   reclasifica entre {pct(e25.min(), 0)} y {pct(e25.max(), 0)} de las alertas reales de EPM (según el método).
4. **Contraste externo.** Las publicaciones oficiales de EPM leídas (ene, feb, jun y jul de 2020; jun y jul de 2021) muestran que los
   componentes que alertan son los que cambiaron: en feb-2020 el costo G,T y pérdidas (+25,8 %) y la distribución (+7,8 %); en
   jul-2020 el transporte STN (−20,3 %), el margen de comercialización (+7,2 %) y la distribución (+5,2 %); en jul-2021 el transporte STN
   (−13,3 %), que es **un solo componente** (con I-MR, las 15 series de ese componente), y Restricciones (+147 %, según el Hito 2). Los valores del CSV
   coinciden con las publicaciones, de modo que no son errores de captura. Además CHEC alerta con **{int(chec_feb.series_con_alerta)} de {int(chec_feb.series_evaluadas)} series
   en feb-2020** (I-MR, ref. 36): el fenómeno no es exclusivo de EPM.
5. **La regla no debe descartar alertas, solo reclasificarlas para revisión.** A X = 25 % la simulación de 4.2 oculta
   {pct(coll_all.min(), 0)}–{pct(coll_all.max(), 0)} de los errores *colectivos* (un error masivo en el mismo mes, p. ej. ×1000 en todas las series, es
   indistinguible de un cambio regulatorio solo por fracción): el rótulo es «candidato sistémico» y confirmarlo exige el contraste con la publicación.
6. **Hallazgo colateral que afecta a 4.1 y 4.2:** EPM cambia la escritura de varias etiquetas entre meses (p. ej. «Costo compra: Gm, i» y
   «Costo Compra: Gm, i») y, sin normalizarlas, una misma serie se parte: {epm_o} series con etiquetas originales frente a
   {epm_c} con las equivalencias aprobadas internamente en el Hito 2 ([inventario_series_por_variante.csv](inventario_series_por_variante.csv)). Aquí se usan las canónicas como variante principal y las originales como sensibilidad.

## 1. La regla

Para una fuente y un mes: `fracción = series con alerta / series evaluadas ese mes`. El mes es **candidato sistémico** si
`fracción > X` (desigualdad estricta) **y** se evaluaron al menos {R.N_MIN} series. Las alertas de ese mes no se eliminan: pasan a la cola de
«candidatos sistémicos» y se revisan contra la publicación. El mínimo de {R.N_MIN} series evita que dos series que alertan juntas
(100 %) se lean como un cambio de mercado; 4.2 usaba 2 como mínimo técnico para la sensibilidad, aquí se exige un denominador interpretable.
`regla_sistemica.py` implementa la regla y sus pruebas están en `test_regla_sistemica.py`.

**Amplitud (diagnóstico, no parte de la regla).** Las series de EPM están replicadas por columna, nivel de tensión y tipo de tarifa: un solo
componente puede agrupar hasta {int(block.series_del_componente.max())} series, de modo que una fracción alta puede ser «un componente» y no «el mercado». Se reporta, además,
cuántos componentes distintos alertan:

{breadth_table}

## 2. Protocolo

- **Ventana móvil sin fuga de futuro.** El mes *m* se evalúa con los W cambios logarítmicos anteriores (W = 24 y 36), solo entre meses consecutivos y sin
  imputar. Así cualquier mes se puede evaluar sin que el futuro entre en la referencia (prueba automática). Es la extensión natural del protocolo 4.1/4.2,
  cuya vigilancia fija de 12 meses finales no alcanza a cubrir feb-2020 ni jul-2020 en EPM.
- **Dos métodos:** I-MR clásica (2,66 y 3,267) y Z-score robusto con MAD 3σ; con MAD cero, señal si el cambio difiere de la mediana (4.1/4.2).
- **Variantes de EPM:** etiquetas canónicas (principal) y originales; W = 24 y 36; dos métodos; más la **reproducción del Hito 2** (83 series, origen fijo, diferencia absoluta).
- **Cuarentena EPM** de 3.7 aplicada igual que en 4.1. No se modifica ningún CSV fuente.
- **Una limitación del origen móvil:** la referencia de los meses posteriores a feb-2020 contiene su salto, lo que ensancha los límites I-MR;
  puede explicar por qué I-MR ref. 36 no señala jul-2020 ({pct(pe.loc['2020-07', 'fraccion'])}) y MAD, más robusto, sí. Es una hipótesis no contrastada
  (no se probó excluir los meses sistémicos de la referencia).

*Figura regenerable:* `python desarrollo_puntos/4.4/informe_regla_sistemica.py` crea
`figuras/01_fraccion_mensual_epm.png`. Los valores auditables están en
[fracciones_mensuales.csv](fracciones_mensuales.csv).

## 3. Calibración de X

Para cada variante se calcula la banda de X que capturaría los tres meses del plan sin marcar ningún otro. Si el mayor valor de los otros
meses es mayor o igual que el menor de los tres, la banda no existe:

{calibration_table}

(Valores de «X máximo» iguales a 0 % indican que algún mes del plan no tiene ninguna alerta en esa variante.) En ninguna variante la banda es factible.
Variantes con etiquetas originales: ver [calibracion_resumen.csv](calibracion_resumen.csv); el X que maximiza la exactitud balanceada
va de {pct(best_x.min(), 0)} a {pct(best_x.max(), 0)} según la variante: **no es un óptimo estable**.

*Figura regenerable:* `informe_regla_sistemica.py` crea `figuras/03_calibracion_X.png`; los datos
auditables están en [calibracion_X.csv](calibracion_X.csv).

**Criterio para el valor de trabajo.** Sin etiquetas confirmadas no hay un óptimo; se propone X = {R.X_WORK * 100:.0f} % porque (a) captura febrero de 2020 en las {len(summary)} variantes (su fracción mínima es {pct(feb_lo, 0)})
y {int((summary.eventos_capturados_en_X_trabajo == 2).sum())} de {len(summary)} capturan además jul-2020; jul-2021 no se captura en ninguna;
(b) en las variantes canónicas no marca ningún mes ajeno al plan; (c) su costo para errores individuales es bajo (siguiente sección); y (d) supera lo que aportaría un
solo componente aunque todas sus series alertaran: como máximo {pct(block_max)} ({int(block_row.series_del_componente)} de {int(block_row.series_evaluadas_mes)} series en {block_row.periodo};
[tamano_componentes_epm.csv](tamano_componentes_epm.csv)). Con X = 10 % un solo componente ya sería «sistémico». Es un valor de arranque para revisar con el director, no una calibración cerrada.

## 4. Efecto de X: alertas reales y costo de enmascaramiento

Meses clasificados como sistémicos y fracción de alertas reales que se reclasifican (ventana móvil, referencia 36):

{effect_table}

En EPM, X = 10 % reclasificaría más del 80 % de las alertas (la regla dejaría de discriminar); X = 25 % reclasifica entre {pct(e25.min(), 0)} y {pct(e25.max(), 0)} y X = 50 % solo febrero de 2020. En CHEC,
{chec_over} de {len(chec)} meses evaluables superan el 25 % (I-MR): la mayor parte de sus alertas ocurre en meses en que casi toda la fuente cambia a la vez. En SSPD la fracción mensual
máxima es {pct(sspd_max)} (referencia 36, ambos métodos): **con X = 25 % la regla no se activa y todas sus alertas siguen en revisión individual**.

*Figura regenerable:* `informe_regla_sistemica.py` crea
`figuras/02_fraccion_mensual_chec_sspd.png`; los valores auditables están en
[fracciones_mensuales.csv](fracciones_mensuales.csv).

**Costo para detecciones de errores conocidos** (tomado de 4.2, inyecciones, referencia 36, cohorte común, horizonte t o t+1; fracción de detecciones que la regla enmascararía):

{cost_table}

El enmascaramiento de errores individuales es bajo a X ≥ 25 % y crece cuando X baja; el de errores colectivos es de {pct(coll_50.min(), 0)}–{pct(coll_50.max(), 0)} incluso con X = 50 %.
Por eso la regla **etiqueta**, no suprime.

## 5. Contraste con las publicaciones oficiales de EPM

Se leyeron las publicaciones tarifarias de EPM de enero, febrero, junio y julio de 2020 y de junio y julio de 2021 (tabla monomia, nivel I). Su transcripción se verificó de dos maneras:
(1) coincide con el CSV en las {int(len(pd.read_csv((_PROJECT_ROOT / 'Data/gold/outputs/regla_sistemica/verificacion_transcripcion_pdf.csv'))))} celdas (componente × columna × mes) y (2) la suma de componentes reproduce el CU total publicado (tolerancia 0,02) —
[verificacion_transcripcion_pdf.csv](verificacion_transcripcion_pdf.csv) y [verificacion_suma_componentes.csv](verificacion_suma_componentes.csv). De paso, esto suma evidencia de exactitud de EPM para cinco
meses nuevos (feb, jun y jul de 2020; jun y jul de 2021) y otras filas de enero (EXA01 usaba seis filas de ene/dic-2020 y abr/dic-2021); la matriz OE1 de 3.1 no se modifica.

**Febrero de 2020 (enero → febrero).** Las alertas «por componente» cuentan todas las series del componente (todos los niveles y tipos de tarifa); el cambio publicado es el de nivel I, columna Propiedad EPM:

{contrast_tables['2020-02']}

**Julio de 2020 (junio → julio).**

{contrast_tables['2020-07']}

**Julio de 2021 (junio → julio).** La publicación de julio no se encontró con las primeras variantes de URL; el enlace real, tomado de la página «Tarifas años anteriores energía» de EPM, incluye el día («16_julio_2021»).

{contrast_tables['2021-07']}

*Figura regenerable:* `informe_regla_sistemica.py` crea
`figuras/04_contraste_publicaciones_epm.png`; los valores auditables están en
[contraste_componentes.csv](contraste_componentes.csv).

Lectura, acotada a lo observado:

- Las alertas caen en componentes que la publicación muestra con cambios apreciables: costo G,T y pérdidas (+25,8 %) y distribución (+7,8 %) en febrero; transporte STN (−20,3 %), margen de comercialización (+7,2 %) y distribución (+5,2 %) en julio de 2020.
  En julio de 2020 **qué componente alerta depende del método** (con I-MR ref. 36 solo la distribución; con MAD, STN y margen; en el Hito 2, los tres). Como los valores del CSV coinciden con la publicación, esas alertas **corresponden a cambios publicados y no a errores de captura**.
- No todo cambio alerta: en febrero el costo de compra (+8,4 %) y el STN (+5,3 %), y en julio de 2020 Restricciones (+40,9 %), no alertan en ninguna variante. Es compatible con una variabilidad histórica alta de esas series; no se verificó.
- **La hipótesis del Hito 2 solo se respalda en parte.** La revisión del Hito 2 atribuye febrero-2020 «probablemente» a la entrada de los cargos de distribución de la CREG 015 de 2018. Aquí la distribución sube +7,8 %, pero el costo G,T y pérdidas sube +25,8 % y el costo de compra +8,4 %:
  el cambio no se limita a los cargos de distribución.
- **Resolución CREG 012 de 2020** (opción tarifaria; expedida el 6 de febrero y publicada en el Diario Oficial el 17 de febrero de 2020): sus considerandos citan la 015 de 2018 como motivo, pero no fijan un mes de aplicación para EPM.
  Los encabezados de enero y febrero no citan ninguna resolución de 2020; los de junio y julio añaden CREG 012, 058 y 104 de 2020 y una fila nueva «CU CREG 012 de 2020» (567,36), igual al CU total de febrero, mientras el «CU total» calculado de julio es 581,22.
  Es coherente con que la opción tarifaria mantuviera la tarifa aplicada mientras los componentes seguían moviéndose, pero **no se probó** el mecanismo.
- Restricciones cruza cero entre enero y febrero (−0,25 → 2,03): el protocolo logarítmico excluye esa serie (solo admite valores positivos); otras series del componente sí alertan.
- **Julio de 2021 es un cambio de un solo componente, no de todo el mercado.** El transporte STN baja 13,3 % y es justo el componente cuyas 15 series alertan con I-MR (ref. 36);
  con MAD no alerta ninguna serie, y en el Hito 2 (cambios absolutos, límites fijos) alertan tres componentes: STN, distribución (−2,1 %) y Restricciones (+147,0 %, que sube de 11,50 a 28,40).
  Con X = 25 % ese mes no es «sistémico»: es coherente con que un solo componente no debe reclasificarse como cambio de mercado, aunque sí es un cambio publicado y no un error.
- **Resoluciones CREG leídas.** La **058 de 2020** (expedida el 14 de abril; Diario Oficial del 15 de abril de 2020) fija pagos diferidos de las facturas de abril a junio durante la emergencia sanitaria,
  permite cobrar menos que el máximo aprobado en los cargos de transmisión, distribución y comercialización y remite a la opción tarifaria de la 012. La **104 de 2020** (5 de junio; Diario Oficial del 7 de junio)
  impide que el consumo de subsistencia de los estratos 1 y 2 varíe con el IPC durante la emergencia. Ninguna de las dos fija los valores de los componentes de EPM, así que **explican el contexto regulatorio, no los cambios
  observados**. De la **015 de 2018** solo se verificó de forma literal que se publicó el 3 de febrero de 2018 y su objeto; las reglas de aplicación de los cargos proceden de un resumen de la herramienta de lectura y no se citan como texto.
  Los encabezados de junio y julio de 2021 citan las CREG 012, 104 y 152 de 2020 y la 003 de 2021 (ya no la 058); estas dos últimas no se leyeron.

Fuentes documentales y su estado:

{refs_table}

## 6. Qué no se puede concluir

- **«Candidato sistémico» no es «cambio regulatorio confirmado».** El contraste con las publicaciones oficiales de EPM respalda que feb-2020, jul-2020 y jul-2021 son cambios publicados; solo feb-2020 es amplio (11 componentes). Falta confirmar con EPM o la CREG la causa regulatoria de cada uno.
- **Tres meses no bastan para calibrar.** Los resultados dependen del protocolo; el valor de X es una decisión a aprobar, con esta sensibilidad como insumo.
- **Las series no son independientes** (columnas y niveles replicados): una fracción alta puede ser un solo componente. Por eso se reporta la amplitud, y no se interpreta la fracción como una proporción de eventos independientes.
- **Los costos de enmascaramiento vienen de inyecciones artificiales** (4.2) en la cohorte común de 2021; no se recalcularon con la ventana móvil.
- **Las equivalencias de etiquetas son aprobadas internamente** por el equipo; EPM no las ha confirmado.
- **CHEC y SSPD no tienen contraste externo en este punto.** La coincidencia de feb-2020 en CHEC es evidencia interna entre fuentes, no una verificación documental.

## 7. Qué cierra del plan y qué queda pendiente

Cierra: formalización e implementación de la regla; calibración de X con sensibilidad; catálogo de alertas sistémicas ([catalogo_alertas_sistemicas.csv](catalogo_alertas_sistemicas.csv),
{len(catalog)} filas); contraste con las publicaciones de EPM de feb-2020, jul-2020 y jul-2021; lectura de las CREG 012, 058 y 104 de 2020 y lectura parcial de la 015 de 2018; verificación de las cifras 51/24/18.
**Pendiente:** lectura completa de la CREG 015 de 2018 y de las resoluciones particulares de EPM; lectura de las CREG 152 de 2020 y 003 de 2021; consulta formal a EPM o CREG sobre la causa de cada cambio (plan, Hito 6);
decisión del director sobre X; revisar 4.1/4.2 con etiquetas canónicas; probar la exclusión de meses sistémicos de la referencia.

## Reproducir y auditar

```powershell
python desarrollo_puntos/4.4/calibrar_regla_sistemica.py
python desarrollo_puntos/4.4/informe_regla_sistemica.py
python -m unittest discover -s desarrollo_puntos/4.4 -p test_regla_sistemica.py -v
python desarrollo_puntos/4.4/verificar_resultados.py
```

[configuracion.json](configuracion.json) fija parámetros, versiones y huellas de entradas y de los PDF; [manifiesto_resultados.json](manifiesto_resultados.json) las de todos los archivos entregados.
"""
    ((_PROJECT_ROOT / 'Data/gold/outputs/regla_sistemica/INFORME_REGLA_SISTEMICA.txt')).write_text(text, encoding='utf-8')
    print('Informe y figuras generados')


if __name__ == '__main__':
    main()
