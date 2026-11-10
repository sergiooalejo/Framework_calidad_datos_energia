"""Regla de alerta sistémica (Hito 4.4): definición, protocolo de ventana móvil y calibración.

La regla del plan: si más de X % de las series alertan en el mismo mes, ese mes se clasifica como
*candidato sistémico* (posible cambio regulatorio o de publicación) y no como error de dato. Aquí:

- `rolling_signals` calcula las señales de cada mes usando solo los W cambios anteriores (origen
  móvil), de modo que cualquier mes pueda evaluarse sin fuga de información del futuro;
- `classify` aplica la regla (desigualdad estricta y mínimo de series observadas);
- `calibrate` mide, para una malla de X, qué meses quedan clasificados y qué costo tiene.

Las funciones puras no leen archivos. La carga de EPM con etiquetas canónicas (`canonical_epm_items`)
es lo único que toca disco y solo lee.
"""
from __future__ import annotations

from pathlib import Path as _ProjectPath
_PROJECT_ROOT = next(p for p in _ProjectPath(__file__).resolve().parents if (p / "project.json").is_file())

import hashlib
import json
import math
import sys
from pathlib import Path

import numpy as np
import pandas as pd
from numpy.lib.stride_tricks import sliding_window_view

HERE = (_PROJECT_ROOT / 'Outputs/regla_sistemica')
ROOT = _PROJECT_ROOT
sys.dont_write_bytecode = True

NORMAL_MEDIAN = 0.6744897501960817
I_COEF, MR_COEF = 2.66, 3.267
N_MIN = 10                       # series observadas mínimas para que la fracción sea interpretable
X_GRID = tuple(round(0.05 + 0.01 * i, 2) for i in range(76))      # 5 % ... 80 %
X_WORK = 0.25                    # valor de trabajo propuesto; no aprobado
EVENT_MONTHS = ('2020-02', '2020-07', '2021-07')                  # meses que fija el plan (Hito 2)
METHOD_COLUMNS = {'IMR_clasica': 'imr', 'MAD_3sigma': 'mad'}


# ------------------------------------------------------------------- señales
def rolling_signals(changes: np.ndarray, window: int):
    """Señales I-MR y MAD 3σ para cada cambio con al menos `window` cambios previos.

    Devuelve (índice del cambio, imr, mad). El cambio j se evalúa con los cambios j-window..j-1;
    ningún valor posterior influye en la señal de j (`test_regla_sistemica.py` lo comprueba).
    Con MAD cero se conserva la regla de 4.1/4.2: señal si el cambio difiere de la mediana.
    """
    changes = np.asarray(changes, dtype=float)
    n = len(changes)
    if n <= window:
        return np.array([], dtype=int), np.array([], dtype=bool), np.array([], dtype=bool)
    reference = sliding_window_view(changes, window)[: n - window]
    current, previous = changes[window:], changes[window - 1:-1]
    mean = reference.mean(axis=1)
    mr_mean = np.abs(np.diff(reference, axis=1)).mean(axis=1)
    median = np.median(reference, axis=1)
    mad = np.median(np.abs(reference - median[:, None]), axis=1)
    imr = (np.abs(current - mean) > I_COEF * mr_mean) | (np.abs(current - previous) > MR_COEF * mr_mean)
    with np.errstate(divide='ignore', invalid='ignore'):
        z_signal = NORMAL_MEDIAN * np.abs(current - median) / mad > 3.0
    mad_signal = np.where(mad > 0, z_signal, current != median)
    return np.arange(window, n), imr, mad_signal


def period_label(month_index: int) -> str:
    year, month0 = divmod(int(month_index), 12)
    return f'{year:04d}-{month0 + 1:02d}'


def evaluate_items(items, window: int) -> pd.DataFrame:
    """Una fila por serie y mes evaluable, con las dos señales y los atributos para agrupar."""
    frames = []
    for item in items:
        levels, months = np.asarray(item['valores'], float), np.asarray(item['meses'], int)
        if not (np.all(levels > 0) and np.all(np.diff(months) == 1)):
            raise ValueError('Las series deben ser positivas y de meses consecutivos')
        index, imr, mad = rolling_signals(np.diff(np.log(levels)), window)
        if not len(index):
            continue
        frames.append(pd.DataFrame({
            'serie': item['serie'] + '|' + item['medida'], 'categoria': item['categoria'],
            'componente': item.get('componente', ''), 'mes': months[index + 1],
            'imr': imr, 'mad': mad}))
    if not frames:
        return pd.DataFrame(columns=['serie', 'categoria', 'componente', 'mes', 'imr', 'mad'])
    return pd.concat(frames, ignore_index=True)


# ------------------------------------------------------------ fracciones y regla
def monthly_fractions(long: pd.DataFrame, method: str) -> pd.DataFrame:
    """Fracción de series con alerta por mes, con diagnóstico de amplitud."""
    column = METHOD_COLUMNS[method]
    rows = []
    for month, g in long.groupby('mes'):
        alerting = g[g[column]]
        has_component = (g.componente != '').any()
        rows.append(dict(
            periodo=period_label(month), series_evaluadas=len(g), series_con_alerta=len(alerting),
            fraccion=len(alerting) / len(g),
            categorias_evaluadas=g.categoria.nunique(), categorias_con_alerta=alerting.categoria.nunique(),
            componentes_evaluados=g.componente.nunique() if has_component else None,
            componentes_con_alerta=alerting.componente.nunique() if has_component else None,
            aplicable=int(len(g) >= N_MIN)))
    return pd.DataFrame(rows)


def classify(fraction, applicable, x: float):
    """Regla del plan: más de X % (desigualdad estricta) y al menos N_MIN series observadas."""
    fraction, applicable = np.asarray(fraction, float), np.asarray(applicable, bool)
    return applicable & (fraction > x)


def calibrate(fractions: pd.DataFrame, events=EVENT_MONTHS, grid=X_GRID):
    """Para cada X: eventos capturados, meses de fondo marcados y alertas reclasificadas."""
    evaluable = fractions[fractions.aplicable == 1]
    is_event = evaluable.periodo.isin(events).to_numpy()
    event_months = [e for e in events if e in set(evaluable.periodo)]
    background = evaluable[~is_event]
    rows = []
    total_alerts = int(evaluable.series_con_alerta.sum())
    for x in grid:
        flagged = classify(evaluable.fraccion, evaluable.aplicable, x)
        captured = int((flagged & is_event).sum())
        flagged_bg = int((flagged & ~is_event).sum())
        reclassified = int(evaluable.series_con_alerta[flagged].sum())
        recall = captured / len(event_months) if event_months else float('nan')
        specificity = 1 - flagged_bg / len(background) if len(background) else float('nan')
        rows.append(dict(
            umbral_X=x, eventos_evaluables=len(event_months), eventos_capturados=captured,
            meses_fondo=len(background), meses_fondo_marcados=flagged_bg, meses_marcados_total=int(flagged.sum()),
            sensibilidad_eventos=recall, especificidad_fondo=specificity,
            exactitud_balanceada=(recall + specificity) / 2 if event_months and len(background) else float('nan'),
            alertas_totales=total_alerts, alertas_reclasificadas=reclassified,
            fraccion_alertas_reclasificadas=reclassified / total_alerts if total_alerts else float('nan')))
    return pd.DataFrame(rows)


def separability(fractions: pd.DataFrame, events=EVENT_MONTHS):
    """Banda de X que capturaría todos los eventos sin marcar ningún otro mes, si existe."""
    evaluable = fractions[fractions.aplicable == 1]
    event_f = evaluable[evaluable.periodo.isin(events)].set_index('periodo').fraccion
    background = evaluable[~evaluable.periodo.isin(events)].fraccion
    x_hi = float(event_f.min()) if len(event_f) else float('nan')   # X debe ser < este valor
    x_lo = float(background.max()) if len(background) else float('nan')  # X debe ser >= este valor
    return dict(eventos_evaluables=int(len(event_f)),
                fraccion_por_evento={k: float(v) for k, v in event_f.items()},
                X_minimo_para_no_marcar_fondo=x_lo, X_maximo_para_capturar_todos=x_hi,
                banda_factible=bool(len(event_f) and x_lo < x_hi))


# ------------------------------------------------------ EPM con etiquetas canónicas
def canonical_epm_items():
    """Series EPM con las equivalencias de etiquetas del Hito 2 (copia de trabajo; el CSV no se toca).

    Aplica `3.3/insumos_hito2/02_catalogo_variantes.csv` a tipo de tarifa, tipo de dato y rango de
    consumo, y la cuarentena de 3.7 igual que `4.1/zscore_robusto.py`. Sin esto, una misma serie
    económica se parte en varias cuando EPM cambia la escritura de una etiqueta entre meses.
    """
    sys.path.insert(0, str((_PROJECT_ROOT / 'Code/Modeling/sensibilidad')))
    import analisis_sensibilidad as A
    import zscore_robusto as Z
    catalog = pd.read_csv((_PROJECT_ROOT / 'Outputs/adaptadores/insumos_hito2/02_catalogo_variantes.csv'))
    column_of = {'Tipo de Tarifa': 'tipodetarifa', 'Tipo de Dato': 'tipodedato', 'Rango de Consumo': 'rangodeconsumo'}
    mapping = {(column_of[r.columna], r.variante): r.canonico for r in catalog.itertuples()}
    path = (_PROJECT_ROOT / 'Data/datos/Datos_seleccionados/EPM/epm_sfcd-b3ey.csv')
    quarantine = {r['clave_contenido'] for r in Z.read_csv((_PROJECT_ROOT / 'Outputs/cuarentena_bootstrap/EPM/cuarentena_registros.csv'))}
    months = {n: i for i, n in enumerate(('Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto',
                                          'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'), 1)}
    columns = ('tipodeinformacion', 'tipodetarifa', 'tipodedato', 'rangodeconsumo', 'nivel')
    measures = ('propiedadepm', 'compartido', 'propiedaddelcliente', 'punta', 'fueradepunta')
    series = {}
    for row in Z.read_csv(path):
        if Z.row_hash(row) in quarantine or not row.get('year') or row.get('mes') not in months:
            continue
        period = (int(row['year']), months[row['mes']])
        key = tuple(mapping.get((c, row.get(c, '')), row.get(c, '')) for c in columns)
        for measure in measures:
            try:
                value = float(row[measure])
            except (KeyError, TypeError, ValueError):
                continue
            if value > 0 and math.isfinite(value):
                series.setdefault((key, measure), {}).setdefault(period, []).append(value)
    items = []
    for (key, measure), values in sorted(series.items()):
        run = A.longest_run(values)
        sid = hashlib.sha256(json.dumps(['EPM_canonicas', key, measure], ensure_ascii=False).encode()).hexdigest()[:24]
        items.append(dict(fuente='EPM_canonicas', sid=sid, serie='|'.join(key), key=key, medida=measure,
                          categoria=A.category('EPM', key), componente=key[2],
                          meses=np.array([p for p, _ in run]), valores=np.array([v for _, v in run]), raw=values))
    return items, mapping, path


def with_components(items, source):
    """Añade `componente` (tipo de dato) a las series EPM de A.load_sources."""
    for item in items:
        item['componente'] = item['key'][2] if source == 'EPM' else ''
    return items
