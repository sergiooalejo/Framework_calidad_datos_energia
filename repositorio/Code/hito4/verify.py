"""Auditoría de solo lectura desde puntajes guardados; no reentrena modelos."""
from collections import defaultdict
import json
import math
import numpy as np
import pandas as pd

from Code.hito3.core import ROOT,digest,read_csv
from .protocol import METHODS,TYPES,ALPHAS,threshold,ratio_metrics

OUT=ROOT/'Data/gold/outputs/hito4'


def close(a,b):
    if not math.isclose(float(a),float(b),rel_tol=1e-10,abs_tol=1e-12):
        raise AssertionError((a,b))


def main():
    manifest=json.loads((OUT/'manifiesto.json').read_text(encoding='utf-8'))
    for group in ('entradas','entradas_auxiliares','codigo','salidas'):
        for relative,expected in manifest[group].items():
            assert digest(ROOT/relative)==expected,relative
    q=manifest['cuarentena'];assert digest(ROOT/q['archivo'])==q['sha256']
    folds=pd.read_csv(OUT/'folds.csv')
    assert (folds.entrenamiento_hasta<folds.validacion_desde).all()
    assert (folds.validacion_hasta<=folds.referencia_hasta).all()
    assert (folds.referencia_hasta<folds.primera_vigilancia).all()
    calibration=pd.read_csv(OUT/'calibracion.csv')
    oof=pd.read_csv(OUT/'puntajes_calibracion.csv.gz')
    grouped={(bank,method):rows.puntaje.dropna().to_numpy() for (bank,method),rows in oof.groupby(['banco','metodo'])}
    for r in calibration.itertuples(index=False):
        if pd.isna(r.umbral):continue
        scores=grouped[(r.banco,r.metodo)]
        close(threshold(scores,r.tasa_objetivo),r.umbral)
        close(np.mean(scores>r.umbral),r.tasa_observada_calibracion)
        assert r.tasa_observada_calibracion<=r.tasa_objetivo+1e-12
        assert r.referencia_hasta<r.primera_vigilancia
    all_thresholds={}
    for bank,rows in calibration.groupby('banco'):
        lookup={(r.metodo,r.tasa_objetivo):r.umbral for r in rows.itertuples(index=False)}
        all_thresholds[bank]=np.array([[lookup[(m,a)] for a in ALPHAS] for m in METHODS])
    real=pd.read_csv(OUT/'puntajes_reales.csv.gz');cases=pd.read_csv(OUT/'puntajes_inyecciones.csv.gz')
    assert not real.duplicated(['fuente','referencia','sid','month']).any()
    assert not cases.duplicated(['fuente','referencia','caso_id']).any()
    scores=real[[f'puntaje_{m}' for m in METHODS]].to_numpy()
    real_cut=np.array([all_thresholds[b] for b in real.banco])
    flags=scores[:,:,None]>real_cut
    saved=real[[f'alerta_{m}' for m in METHODS]].to_numpy()
    assert np.array_equal(saved,flags[:,:,ALPHAS.index(.05)])
    case_cut=np.array([all_thresholds[b] for b in cases.banco])
    first=cases[[f'puntaje_{m}_t' for m in METHODS]].to_numpy()[:,:,None]>case_cut
    second=cases[[f'puntaje_{m}_t1' for m in METHODS]].to_numpy()[:,:,None]>case_cut
    both=first|second
    real_lookup={(r.fuente,r.referencia,r.sid,r.month):index for index,r in enumerate(real.itertuples(index=False))}
    following=np.array([real_lookup.get((r.fuente,r.referencia,r.sid,r.month+1),-1) for r in real.itertuples(index=False)])
    usable=following>=0;pair_flags=flags[usable]|flags[following[usable]]
    pair_sources=real.fuente.to_numpy()[usable];pair_windows=real.referencia.to_numpy()[usable]
    metric=pd.read_csv(OUT/'metricas.csv');by_type=pd.read_csv(OUT/'tipos.csv')
    macro={};rates={};types={}
    for (source,window),indices in cases.groupby(['fuente','referencia']).indices.items():
        for h,hit in enumerate((first,both)):
            recalls=[]
            for kind in TYPES:
                subset=indices[cases.tipo.to_numpy()[indices]==kind]
                if not len(subset):continue
                values=hit[subset].mean(axis=0);recalls.append(values)
                types[(source,window,kind,h)]=(len(subset),hit[subset].sum(axis=0))
            macro[(source,window,h)]=np.mean(recalls,axis=0)
    for (source,window),indices in real.groupby(['fuente','referencia']).indices.items():
        rates[(source,window,0)]=(len(indices),flags[indices].mean(axis=0))
        subset=(pair_sources==source)&(pair_windows==window)
        rates[(source,window,1)]=(int(subset.sum()),pair_flags[subset].mean(axis=0))
    for r in metric.itertuples(index=False):
        h=0 if r.horizonte=='t' else 1;m=METHODS.index(r.metodo);a=ALPHAS.index(r.tasa_objetivo)
        recall=macro[(r.fuente,r.referencia,h)][m,a];n,fp=rates[(r.fuente,r.referencia,h)]
        close(recall,r.recall_macro);close(fp[m,a],r.tasa_alerta_proxy);assert n==r.observaciones
        precision,f1=ratio_metrics(recall,fp[m,a],r.prevalencia_supuesta)
        close(precision,r.precision_conservadora);close(f1,r.f1)
        for name in ('recall_macro','precision_conservadora','f1'):
            assert 0<=getattr(r,name)<=1
        if r.categorias==1:
            assert pd.isna(r.recall_ic95_inferior) and pd.isna(r.f1_ic95_inferior)
    for r in by_type.itertuples(index=False):
        h=0 if r.horizonte=='t' else 1;m=METHODS.index(r.metodo);a=ALPHAS.index(r.tasa_objetivo)
        value=types.get((r.fuente,r.referencia,r.tipo,h))
        if value is None:
            assert r.casos==0 and pd.isna(r.recall);continue
        n,counts=value;assert r.casos==n and r.detecciones==counts[m,a]
        close(counts[m,a]/n,r.recall)
    geometry=pd.read_csv(OUT/'lof.csv')
    assert (geometry.vectores_unicos<=geometry.filas_referencia).all()
    # Toda fila que entró al panel tiene calibración y ajuste LOF interpretables.
    common=set(calibration.loc[calibration.panel_comun==1,'banco'])
    assert all(g.lof_estado=='deduplicado_referencia' for g in geometry.itertuples(index=False) if g.banco in common)
    mask=pd.read_csv(OUT/'enmascaramiento.csv')
    assert (mask.detecciones_retenidas+mask.detecciones_enmascaradas==mask.detecciones_sin_reclasificar).all()
    effect=pd.read_csv(OUT/'efecto_regla_alertas_reales.csv')
    assert (effect.retenidas+effect.reclasificadas==effect.alertas_originales).all()
    assert (effect.tasa_retenida<=effect.tasa_original).all()
    draws=pd.read_csv(OUT/'sorteo.csv');assert (draws.repeticiones_de_mes_dentro_replica==0).all()
    paired=pd.read_csv(OUT/'cohorte_pareada.csv')
    for _,rows in paired.groupby('fuente'):
        assert rows.observaciones.nunique()==1 and rows.casos.nunique()==1 and rows.series.nunique()==1
    indicators=pd.read_csv(OUT/'scorecard_indicadores.csv')
    assert len(indicators)==76 and len(pd.read_csv(OUT/'scorecard_dimensiones.csv'))==32
    assert (indicators.aceptacion_director=='no_registrada').all()
    for row in read_csv(OUT/'contraste_regulatorio.csv'):
        assert digest(ROOT/row['archivo'])==row['sha256'] and digest(ROOT/row['texto'])==row['sha256_texto']
        assert row['causa_de_alerta_confirmada']=='no'
    for row in json.loads((OUT/'evidencia_epm_procedencia.json').read_text(encoding='utf-8')):
        assert digest(ROOT/row['archivo'])==row['sha256']
    assert (pd.read_csv(OUT/'cotejo_epm_celdas.csv').coincide==1).all()
    assert (pd.read_csv(OUT/'cotejo_epm_suma.csv').dentro_tolerancia==1).all()
    figures=list((OUT/'figuras').glob('*'))
    assert len(figures)>=16 and all(p.stat().st_size>1000 for p in figures)
    print(json.dumps(dict(estado='correcto',folds_temporales=len(folds),umbrales_auditados=len(calibration),
        observaciones_reales=len(real),casos_inyectados=len(cases),filas_metricas=len(metric),
        scorecard_indicadores=len(indicators),figuras_incluidas=len(figures),
        conclusion='Protocolo técnico verificado; validación externa y aprobación académica pendientes'),ensure_ascii=True,indent=2))


if __name__=='__main__':main()
