"""Funciones del protocolo H4 v2. Ninguna función ajusta con vigilancia."""
from __future__ import annotations

from dataclasses import dataclass
import hashlib
import json
import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.neighbors import LocalOutlierFactor, NearestNeighbors

METHODS = ('IMR', 'Z_robusto', 'IF', 'LOF', 'KNN', 'R12')
TYPES = ('decimal_x1000', 'decimal_div1000', 'serial_excel_43577', 'aumento_10pct', 'valor_no_actualizado', 'otra_medida')
ALPHAS = (.01, .02, .05, .10)
CURVE_ALPHAS = (.005, .01, .02, .03, .05, .075, .10, .15, .20)
SEED = 20261113


def bound_ratio(delta, scale):
    """r/(1+r), con límite 1 cuando escala=0 y delta>0. Nunca inventa epsilon."""
    delta, scale = np.broadcast_arrays(np.abs(np.asarray(delta, float)), np.asarray(scale, float))
    return np.divide(delta, delta+scale, out=np.zeros_like(delta), where=(delta+scale)>0)


def threshold(scores, alpha):
    scores = np.asarray(scores, float)
    if not len(scores) or not np.isfinite(scores).all() or not 0 < alpha < 1:
        raise ValueError('Calibración requiere puntajes finitos y tasa entre cero y uno')
    ordered = np.sort(scores)[::-1]
    k = min(int(np.floor(alpha*len(scores)+1e-9)),len(scores)-1)
    return float(ordered[k])


def folds(window):
    """Tres bloques de validación de referencia con entrenamiento expansivo."""
    if window not in (24,36,48):
        raise ValueError('Ventanas previstas: 24, 36, 48')
    initial = window//2
    edges = np.linspace(initial,window,4,dtype=int)
    return [(int(a),int(b)) for a,b in zip(edges,edges[1:])]


def statistics(levels, train_end):
    """levels[0:train_end+1] exclusivamente; train_end es número de cambios."""
    levels = np.asarray(levels[:train_end+1],float)
    changes = np.diff(np.log(levels))
    valid = changes[np.isfinite(changes)]
    if len(valid)<2:
        return None
    pairs = np.abs(np.diff(changes))
    pairs = pairs[np.isfinite(pairs)]
    if not len(pairs):
        return None
    med = float(np.median(valid))
    level_ref = float(np.nanmedian(levels))
    raw = raw_features(levels, level_ref)
    eligible = np.isfinite(raw).all(axis=1)
    reference = raw[eligible]
    if len(reference)<2:
        return None
    center=np.median(reference,axis=0)
    scale=np.median(np.abs(reference-center),axis=0)/.6744897501960817
    fallback=np.mean(np.abs(reference-center),axis=0)
    scale=np.where(scale>0,scale,np.where(fallback>0,fallback,1.0))
    return dict(mean=float(np.mean(valid)),mr=float(np.mean(pairs)),median=med,
                sigma=float(np.median(np.abs(valid-med))/.6744897501960817),
                level_ref=level_ref,center=center,scale=scale,train_end=train_end)


def raw_features(levels, level_ref):
    levels=np.asarray(levels,float)
    changes=np.diff(np.log(levels))
    previous=np.r_[0.,changes[:-1]]
    return np.column_stack((changes,previous,np.abs(changes-previous),np.log(levels[1:]/level_ref)))


def transformed(levels, stats):
    raw=raw_features(levels,stats['level_ref'])
    return (raw-stats['center'])/stats['scale']


@dataclass
class Bank:
    params: dict
    forest: object
    lof: object
    knn: object
    audit: dict


def fit_bank(items, train_end, seed=SEED):
    params={}
    training=[]
    for item in items:
        p=statistics(item['levels'],train_end)
        if p is None:continue
        params[item['sid']]=p
        x=transformed(item['levels'][:train_end+1],p)
        training.extend(x[np.isfinite(x).all(axis=1)])
    if not training:
        return None
    training=np.asarray(training)
    # Misma geometría de referencia para IF/LOF/KNN. La pérdida de frecuencia
    # por deduplicación es explícita y se estudia aparte; nunca modifica Bronze.
    unique=np.unique(training,axis=0)
    forest=IsolationForest(n_estimators=300,contamination='auto',max_samples=min(256,len(unique)),random_state=seed,n_jobs=1).fit(unique)
    lof=knn=None
    lof_state='sin_geometria_menos_de_tres_vectores'
    if len(unique)>=3:
        lof=LocalOutlierFactor(n_neighbors=min(20,len(unique)-1),novelty=True,n_jobs=1).fit(unique)
        factors=-lof.negative_outlier_factor_
        if not np.isfinite(factors).all() or np.max(factors)>1e6:
            lof=None;lof_state='no_interpretable_geometria_referencia'
        else:lof_state='deduplicado_referencia'
    if len(unique):
        knn=NearestNeighbors(n_neighbors=min(5,len(unique)),n_jobs=1).fit(unique)
    fingerprint=hashlib.sha256(unique.astype('<f8').tobytes()).hexdigest()
    return Bank(params,forest,lof,knn,dict(filas_referencia=len(training),vectores_unicos=len(unique),
                duplicados_referencia=len(training)-len(unique),lof_estado=lof_state,
                vecinos_lof=min(20,len(unique)-1) if lof is not None else None,huella_geometria=fingerprint))


def score_bank(bank, items, positions, replacements=None):
    """Puntúa observaciones indicadas. positions contiene (sid, índice de cambio).

    replacements permite evaluar una inyección sin ajustar de nuevo el banco.
    Todas las técnicas usan las mismas observaciones con cuatro rasgos válidos.
    """
    lookup={i['sid']:i for i in items}
    requests=[]
    for row,(sid,pos) in enumerate(positions):
        original=lookup[sid]['levels']
        levels=original.copy() if replacements else original
        if replacements:
            for index,value in replacements.get(sid,{}).items():levels[index]=value
        change=np.log(levels[pos+1])-np.log(levels[pos])
        previous=0.0 if pos==0 else np.log(levels[pos])-np.log(levels[pos-1])
        current=levels[pos+1]
        requests.append((sid,change,previous,current))
    return score_values(bank,requests)


def score_values(bank,requests):
    output=np.full((len(requests),len(METHODS)),np.nan)
    xs=[];indices=[]
    for row,(sid,change,previous,current) in enumerate(requests):
        p=bank.params.get(sid)
        if p is None:continue
        raw=np.array([change,previous,abs(change-previous),np.log(current/p['level_ref'])])
        if not np.isfinite(raw).all():continue
        output[row,0]=max(bound_ratio(abs(change-p['mean']),2.66*p['mr']),bound_ratio(abs(change-previous),3.267*p['mr']))
        output[row,1]=bound_ratio(abs(change-p['median']),p['sigma'])
        output[row,5]=bound_ratio(abs(current),p['level_ref'])
        xs.append((raw-p['center'])/p['scale']);indices.append(row)
    if xs:
        x=np.asarray(xs)
        output[indices,2]=-bank.forest.score_samples(x)
        if bank.lof is not None:
            ratio=-bank.lof.score_samples(x)
            output[indices,3]=bound_ratio(ratio,1.)
        if bank.knn is not None:
            distances=bank.knn.kneighbors(x)[0].mean(axis=1)
            output[indices,4]=bound_ratio(distances,1.)
    return output


def calibrate(items,window,seed=SEED):
    """Entrena y valida SOLO con el prefijo de referencia; no acepta vigilancia."""
    # Recorte físico antes de calcular estadísticas, rasgos, geometría o cortes.
    prefix=[dict(i,levels=np.asarray(i['levels'][:window+1]).copy(),months=i['months'][:window+1]) for i in items]
    oof=[];schedule=[];geometry=[]
    for fold,(train_end,val_end) in enumerate(folds(window)):
        bank=fit_bank(prefix,train_end,seed+fold)
        if bank is None:continue
        positions=[(i['sid'],j) for i in prefix for j in range(train_end,val_end)]
        scores=score_bank(bank,prefix,positions)
        valid=np.isfinite(scores[:,[0,1,2,4,5]]).all(axis=1)
        oof.extend(scores[valid])
        # Todos los miembros del banco comparten el calendario.
        months=prefix[0]['months']
        schedule.append(dict(fold=fold,entrenamiento_hasta=int(months[train_end]),
                validacion_desde=int(months[train_end+1]),validacion_hasta=int(months[val_end]),
                referencia_hasta=int(months[window]),observaciones=len(positions),observaciones_evaluables=int(valid.sum())))
        geometry.append(dict(fold=fold,**bank.audit))
    values=np.asarray(oof) if oof else np.empty((0,len(METHODS)))
    thresholds={}
    for method_index,method in enumerate(METHODS):
        # Si LOF no fue evaluable en algún fold se excluye la técnica del banco
        # completo antes de vigilancia. No se eligen solo folds favorables.
        valid=np.isfinite(values[:,method_index]) if len(values) else np.array([],bool)
        thresholds[method]={a:threshold(values[:,method_index],a) if len(values) and valid.all() else None for a in CURVE_ALPHAS}
    return thresholds,values,schedule,geometry


def ratio_metrics(tp,fp,prevalence):
    denom=tp*prevalence+fp*(1-prevalence)
    precision=np.divide(tp*prevalence,denom,out=np.zeros_like(np.asarray(tp,float)),where=denom>0)
    f1=np.divide(2*precision*tp,precision+tp,out=np.zeros_like(np.asarray(tp,float)),where=(precision+tp)>0)
    return precision,f1
