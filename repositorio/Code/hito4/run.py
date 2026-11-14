"""Hito 4 v2: CV temporal, evaluación congelada y sensibilidad reproducible."""
from __future__ import annotations

from collections import defaultdict,Counter
from datetime import datetime,timezone
import gzip
import json
import math
import platform
from pathlib import Path
import time
import warnings
import zlib
import importlib.metadata

import numpy as np
import sklearn
from Code.hito3.core import (ROOT,SOURCES,build_series,content_key,digest,label,longest_run,read_csv,write_csv)
from .protocol import (METHODS,TYPES,ALPHAS,CURVE_ALPHAS,SEED,calibrate,fit_bank,
                       score_bank,score_values,threshold,ratio_metrics,transformed)

OUT=ROOT/'Data/gold/outputs/hito4'
BOOTSTRAPS=1000
PREVALENCES=(.01,.05,.10)


def save(name,rows):
    fields=list(dict.fromkeys(k for r in rows for k in r)) or ['estado']
    write_csv(OUT/name,rows,fields)


def save_gzip(name,rows):
    import csv,io
    fields=list(dict.fromkeys(k for r in rows for k in r)) or ['estado']
    with (OUT/name).open('wb') as raw:
        with gzip.GzipFile(filename='',mode='wb',fileobj=raw,mtime=0) as archive:
            with io.TextIOWrapper(archive,encoding='utf-8',newline='') as stream:
                writer=csv.DictWriter(stream,fieldnames=fields);writer.writeheader();writer.writerows(rows)


def load():
    datasets={};lookup={};inventory=[]
    quarantine=read_csv(ROOT/'Data/gold/outputs/hito3/cuarentena_celdas_epm.csv')
    for source,cfg in SOURCES.items():
        rows=read_csv(ROOT/cfg['path'])
        series=build_series(source,rows,quarantine if source=='EPM' else [])
        items=[]
        for (category,measure),points in sorted(series.items()):
            run=longest_run(points)
            sid=content_key({'serie':json.dumps([source,category,measure],ensure_ascii=False)})
            values=np.array([points[m]['value'] if not points[m]['reason'] else np.nan for m in run],float)
            item=dict(fuente=source,sid=sid,category=json.dumps(category,ensure_ascii=False),category_tuple=category,
                      medida=measure,months=np.array(run),levels=values,points=points)
            if len(run)>=37:items.append(item)
            for month,p in points.items():
                if not p['reason']:lookup[(source,category,month,measure)]=p['value']
            inventory.append(dict(fuente=source,sid=sid,categoria=item['category'],medida=measure,
                meses_racha=len(run),celdas_excluidas=sum(bool(points[m]['reason']) for m in run),
                elegible_24=int(len(run)>=37),elegible_36=int(len(run)>=49),elegible_48=int(len(run)>=61)))
        datasets[source]=items
    return datasets,lookup,inventory


def panel(items,window):
    selected=[]
    for item in items:
        # Ventana retrospectiva: los mismos doce meses finales con 24/36/48.
        if len(item['months'])<window+13:continue
        selected.append(dict(item,levels=item['levels'][-(window+13):].copy(),months=item['months'][-(window+13):]))
    return selected


def build_cases(items,window,lookup):
    cases=[];omitted=[]
    for item in items:
        levels=item['levels']
        for t in range(11):
            index=window+t+1;month=int(item['months'][index])
            # Dos horizontes y cuatro rasgos requieren t-2, t-1, t, t+1.
            if not np.isfinite(levels[index-2:index+2]).all():
                omitted.append(dict(fuente=item['fuente'],sid=item['sid'],periodo=label(month),tipo='todos',motivo='contexto_con_hueco_cuarentena_o_conflicto'))
                continue
            value=levels[index]
            options=dict(decimal_x1000=value*1000,decimal_div1000=value/1000,serial_excel_43577=43577.,
                         aumento_10pct=value*1.1,valor_no_actualizado=levels[index-1])
            alternative=next((lookup.get((item['fuente'],item['category_tuple'],month,m)) for m in sorted(SOURCES[item['fuente']]['measures'])
                              if m!=item['medida'] and lookup.get((item['fuente'],item['category_tuple'],month,m)) not in (None,value)),None)
            if alternative is not None:options['otra_medida']=alternative
            else:omitted.append(dict(fuente=item['fuente'],sid=item['sid'],periodo=label(month),tipo='otra_medida',motivo='sin_otra_medida_positiva_distinta'))
            for kind,new in options.items():
                if new==value:
                    omitted.append(dict(fuente=item['fuente'],sid=item['sid'],periodo=label(month),tipo=kind,motivo='no_altera_valor'));continue
                cases.append(dict(item=item,index=index,t=t,tipo=kind,original=float(value),nuevo=float(new),month=month,
                    caso_id=f'{item["sid"]}:{label(month)}:{kind}'))
    return cases,omitted


def injection_requests(cases):
    requests=[]
    for case in cases:
        item=case['item'];i=case['index'];v=item['levels'];new=case['nuevo'];sid=item['sid']
        change=math.log(new)-math.log(v[i-1])
        previous=math.log(v[i-1])-math.log(v[i-2])
        following=math.log(v[i+1])-math.log(new)
        requests.extend(((sid,change,previous,new),(sid,following,change,v[i+1])))
    return requests


def intervals_by_category(base,cases,source,window):
    """Bootstrap pareado: categoría completa, mismas ponderaciones para TPR y proxy FPR."""
    categories=sorted({r['categoria'] for r in base})
    if not categories:return [],[],[],[]
    cat_index={c:i for i,c in enumerate(categories)}
    G=len(categories);M=len(METHODS);A=len(CURVE_ALPHAS);K=len(TYPES)
    positive=np.zeros((G,K,M,A,2));den=np.zeros((G,K))
    negative=np.zeros((G,M,A,2));neg_den=np.zeros((G,2))
    by_sid_month={(r['sid'],r['month']):r for r in base}
    for row in base:
        g=cat_index[row['categoria']]
        negative[g,:,:,0]+=row['flags'];neg_den[g,0]+=1
        following=by_sid_month.get((row['sid'],row['month']+1))
        if following is not None:
            negative[g,:,:,1]+=row['flags']|following['flags'];neg_den[g,1]+=1
    for case in cases:
        g=cat_index[case['item']['category']];k=TYPES.index(case['tipo'])
        den[g,k]+=1;positive[g,k]+=case['hits']
    weights=np.ones((1,G))
    if G>=2:
        rng=np.random.default_rng(SEED+zlib.crc32(f'{source}:{window}'.encode()))
        weights=np.vstack((weights,rng.multinomial(G,np.full(G,1/G),size=BOOTSTRAPS)))
    sampled_num=np.tensordot(weights,positive,axes=(1,0))
    sampled_den=weights@den
    sampled_fp=np.tensordot(weights,negative,axes=(1,0))
    sampled_n=weights@neg_den
    with np.errstate(divide='ignore',invalid='ignore'):
        recalls=sampled_num/sampled_den[:,:,None,None,None]
        alert_rates=sampled_fp/sampled_n[:,None,None,:]
    with warnings.catch_warnings():
        warnings.simplefilter('ignore',RuntimeWarning)
        macro=np.nanmean(recalls,axis=1)
    def ci(array):
        if G<2:return (None,None)
        values=array[1:];values=values[np.isfinite(values)]
        return tuple(float(v) for v in np.quantile(values,[.025,.975])) if len(values) else (None,None)
    metrics=[];types=[];curves=[];levels=[]
    for m,method in enumerate(METHODS):
        for a,alpha in enumerate(CURVE_ALPHAS):
            for h,horizon in enumerate(('t','t_o_t1')):
                r=float(macro[0,m,a,h]);f=float(alert_rates[0,m,a,h])
                curves.append(dict(fuente=source,referencia=window,metodo=method,tasa_objetivo=alpha,horizonte=horizon,
                    tasa_alerta_vigilancia=f,recall_macro=r,categorias=G,origen_umbral='CV_temporal_solo_referencia'))
                if alpha not in ALPHAS:continue
                lo,hi=ci(macro[:,m,a,h])
                for prevalence in PREVALENCES:
                    p,f1=ratio_metrics(macro[:,m,a,h],alert_rates[:,m,a,h],prevalence)
                    plo,phi=ci(p);flo,fhi=ci(f1)
                    metrics.append(dict(fuente=source,referencia=window,metodo=method,tasa_objetivo=alpha,horizonte=horizon,
                        prevalencia_supuesta=prevalence,recall_macro=r,recall_ic95_inferior=lo,recall_ic95_superior=hi,
                        tasa_alerta_proxy=f,precision_conservadora=float(p[0]),precision_ic95_inferior=plo,precision_ic95_superior=phi,
                        f1=float(f1[0]),f1_ic95_inferior=flo,f1_ic95_superior=fhi,categorias=G,
                        observaciones=int(sampled_n[0,h]),casos=int(den.sum()),
                        estado_metodo='evaluable_experimental' if G>=2 else 'descriptivo_sin_IC_una_categoria',
                        etiqueta_precision='escenario_no_precision_empirica',origen_umbral='CV_temporal_solo_referencia'))
                for k,kind in enumerate(TYPES):
                    value=float(recalls[0,k,m,a,h]);lo,hi=ci(recalls[:,k,m,a,h])
                    types.append(dict(fuente=source,referencia=window,metodo=method,tasa_objetivo=alpha,horizonte=horizon,
                        tipo=kind,casos=int(den[:,k].sum()),detecciones=int(positive[:,k,m,a,h].sum()),
                        recall=value if math.isfinite(value) else None,ic95_inferior=lo,ic95_superior=hi,
                        estado='evaluable' if den[:,k].sum() else 'sin_casos_aplicables'))
    for level in sorted({r['nivel'] for r in base}):
        records=[r for r in base if r['nivel']==level]
        for m,method in enumerate(METHODS):
            alpha_index=CURVE_ALPHAS.index(.05)
            levels.append(dict(fuente=source,referencia=window,nivel=level,metodo=method,series=len({r['sid'] for r in records}),
                observaciones=len(records),alertas=sum(int(r['flags'][m,alpha_index]) for r in records),
                tasa_alerta=sum(int(r['flags'][m,alpha_index]) for r in records)/len(records),tasa_objetivo=.05))
    return metrics,types,curves,levels


def level(item):
    values=item['category_tuple']
    return 'Nivel_'+(values[-1] if item['fuente']=='EPM' else values[3]) if item['fuente'] in ('EPM','CHEC') else 'No_aplica'


def experiment(source,items,window,lookup):
    start=time.perf_counter();selected=panel(items,window)
    groups=defaultdict(list)
    for item in selected:groups[int(item['months'][window])].append(item)
    calibration=[];schedules=[];geometries=[];base=[];all_cases=[];omitted=[];native=[];coverage=[];times=[];cal_scores=[]
    for cutoff,group in sorted(groups.items()):
        clock=time.perf_counter()
        bank_id=f'{source}:W{window}:{label(cutoff)}'
        cutoffs,oof,schedule,geometry=calibrate(group,window)
        final=fit_bank(group,window)
        if final is None:
            coverage.append(dict(fuente=source,referencia=window,banco=bank_id,series=len(group),estado='sin_referencia_valida'));continue
        common=final.lof is not None and all(cutoffs[m][.05] is not None for m in METHODS)
        for record in schedule:schedules.append(dict(fuente=source,referencia=window,banco=bank_id,**record,primera_vigilancia=cutoff+1))
        for record in geometry:geometries.append(dict(fuente=source,referencia=window,banco=bank_id,**record))
        geometries.append(dict(fuente=source,referencia=window,banco=bank_id,fold='final',**final.audit))
        for m,method in enumerate(METHODS):
            for alpha in CURVE_ALPHAS:
                th=cutoffs[method][alpha]
                valid=oof[:,m][np.isfinite(oof[:,m])]
                calibration.append(dict(fuente=source,referencia=window,banco=bank_id,metodo=method,tasa_objetivo=alpha,
                    umbral=th,observaciones_calibracion=len(valid),tasa_observada_calibracion=float(np.mean(valid>th)) if th is not None else None,
                    estado='no_calibrable' if th is None else 'congelado_baja_resolucion' if len(valid)*alpha<5 else 'congelado',
                    referencia_hasta=label(cutoff),primera_vigilancia=label(cutoff+1),
                    origen='tres_folds_temporales_dentro_referencia',panel_comun=int(common)))
            for j,score in enumerate(oof[:,m]):
                cal_scores.append(dict(banco=bank_id,metodo=method,indice_oof=j,puntaje=float(score) if np.isfinite(score) else None))
        coverage.append(dict(fuente=source,referencia=window,banco=bank_id,series=len(group),
                             estado='panel_comun_seis_metodos' if common else 'excluido_panel_comun_LOF_o_calibracion_insuficiente'))
        times.append(dict(fuente=source,referencia=window,banco=bank_id,etapa='CV_y_ajuste_final',segundos=time.perf_counter()-clock))
        if not common:continue
        thresholds=np.array([[cutoffs[m][a] for a in CURVE_ALPHAS] for m in METHODS])
        scoring_clock=time.perf_counter()
        positions=[(i['sid'],j) for i in group for j in range(window,window+12)]
        scores=score_bank(final,group,positions)
        by_sid={i['sid']:i for i in group}
        for (sid,j),scores_row in zip(positions,scores):
            if not np.isfinite(scores_row).all():continue
            item=by_sid[sid];month=int(item['months'][j+1]);flags=scores_row[:,None]>thresholds
            base.append(dict(fuente=source,referencia=window,banco=bank_id,sid=sid,categoria=item['category'],
                medida=item['medida'],nivel=level(item),month=month,periodo=label(month),scores=scores_row,flags=flags))
        cases,skipped=build_cases(group,window,lookup);omitted.extend(skipped)
        case_scores=score_values(final,injection_requests(cases)).reshape(-1,2,len(METHODS)) if cases else np.empty((0,2,len(METHODS)))
        for case,scores_case in zip(cases,case_scores):
            if not np.isfinite(scores_case).all():continue
            hits0=scores_case[0,:,None]>thresholds;hits1=scores_case[1,:,None]>thresholds
            case.update(scores=scores_case,hits=np.stack((hits0,hits0|hits1),axis=-1),banco=bank_id)
            all_cases.append(case)
        times.append(dict(fuente=source,referencia=window,banco=bank_id,etapa='puntuar_vigilancia_e_inyecciones',segundos=time.perf_counter()-scoring_clock))
        # Sensibilidad de constantes/percentil/factor con la misma población y corte.
        native_clock=time.perf_counter()
        reference_features=[]
        for item in group:
            if item['sid'] not in final.params:continue
            x=transformed(item['levels'][:window+1],final.params[item['sid']])
            reference_features.extend(x[np.isfinite(x).all(axis=1)])
        # LOF novelty no puntúa aquí sus propias muestras de ajuste.
        if_reference=-final.forest.score_samples(np.asarray(reference_features))
        variants=[('IMR_2.66_3.267',0,.5),*[(f'MAD_{v}sigma',1,v/(1+v)) for v in (2.66,3.,3.267)],
                  *[(f'IF_p{q*100:g}',2,float(np.quantile(if_reference,q))) for q in (.99,.995)],
                  *[(f'R12_f{f}',5,f/(1+f)) for f in (5,10,20)]]
        valid_case_scores=[c for c in cases if 'scores' in c]
        actual=scores[np.isfinite(scores).all(axis=1)]
        for name,m,cut in variants:
            for h,horizon in enumerate(('t','t_o_t1')):
                detections=sum(bool(np.any(c['scores'][:h+1,m]>cut)) for c in valid_case_scores)
                native.append(dict(fuente=source,referencia=window,banco=bank_id,variante=name,horizonte=horizon,
                    umbral=cut,casos=len(valid_case_scores),detecciones=detections,observaciones=len(actual),
                    alertas_reales=int((actual[:,m]>cut).sum()),estado='sensibilidad_umbral_nativo_no_tasa_igualada'))
        times.append(dict(fuente=source,referencia=window,banco=bank_id,etapa='sensibilidad_umbrales_nativos',segundos=time.perf_counter()-native_clock))
    aggregate_clock=time.perf_counter()
    metricas,types,curves,levels=intervals_by_category(base,all_cases,source,window)
    times.append(dict(fuente=source,referencia=window,banco='todos',etapa='bootstrap_y_metricas',segundos=time.perf_counter()-aggregate_clock))
    times.append(dict(fuente=source,referencia=window,banco='todos',etapa='total',segundos=time.perf_counter()-start))
    # Sorteo reproducible sin reemplazo: tres orígenes distintos por serie/réplica.
    by_sid=defaultdict(lambda:defaultdict(list))
    for case in all_cases:by_sid[case['item']['sid']][case['month']].append(case)
    rng=np.random.default_rng(SEED+zlib.crc32(f'sorteo:{source}:{window}'.encode()))
    draws=[]
    for sid,origins in sorted(by_sid.items()):
        months=sorted(origins)
        if len(months)<3:continue
        counts=Counter()
        for repetition in range(500):
            chosen=rng.choice(months,size=3,replace=False)
            assert len(set(chosen))==3
            for month in chosen:
                candidates=origins[int(month)];case=candidates[int(rng.integers(len(candidates)))];counts[case['tipo']]+=1
        draws.append(dict(fuente=source,referencia=window,sid=sid,replicas=500,meses_disponibles=len(months),
            meses_por_replica=3,repeticiones_de_mes_dentro_replica=0,pruebas_por_tipo=json.dumps(dict(counts),sort_keys=True),semilla=SEED+zlib.crc32(f'sorteo:{source}:{window}'.encode())))
    return dict(metricas=metricas,tipos=types,curvas=curves,niveles=levels,calibracion=calibration,
        folds=schedules,lof=geometries,nativos=native,cobertura=coverage,costos=times,sorteo=draws,
        omitidas=omitted,base=base,casos=all_cases,puntajes_calibracion=cal_scores)


def serialize_details(base,cases):
    real=[];injected=[]
    for r in base:
        row={k:v for k,v in r.items() if k not in ('scores','flags')}
        row.update({f'puntaje_{m}':float(r['scores'][j]) for j,m in enumerate(METHODS)})
        row.update({f'alerta_{m}':int(r['flags'][j,CURVE_ALPHAS.index(.05)]) for j,m in enumerate(METHODS)})
        real.append(row)
    for c in cases:
        row=dict(fuente=c['item']['fuente'],referencia=c['item']['window'],banco=c['banco'],sid=c['item']['sid'],
            categoria=c['item']['category'],caso_id=c['caso_id'],tipo=c['tipo'],periodo=label(c['month']),original=c['original'],nuevo=c['nuevo'])
        for j,m in enumerate(METHODS):
            row[f'puntaje_{m}_t']=float(c['scores'][0,j]);row[f'puntaje_{m}_t1']=float(c['scores'][1,j])
        injected.append(row)
    return real,injected


def main():
    OUT.mkdir(parents=True,exist_ok=True)
    datasets,lookup,inventory=load();save('inventario_series.csv',inventory)
    tables=defaultdict(list);base=[];cases=[]
    for source,items in datasets.items():
        if source=='SSPD_PLAN':continue
        for window in (24,36,48):
            print(f'H4 CV: {source}, referencia {window}',flush=True)
            selected=[dict(i,window=window) for i in items]
            result=experiment(source,selected,window,lookup)
            base.extend(result.pop('base'));cases.extend(result.pop('casos'))
            for key,values in result.items():tables[key].extend(values)
    for name,rows in tables.items():
        if name=='puntajes_calibracion':save_gzip(name+'.csv.gz',rows)
        else:save(name+'.csv',rows)
    paired=[];paired_inventory=[]
    for source in datasets:
        available=sorted({r['referencia'] for r in base if r['fuente']==source})
        if len(available)<2:continue
        real_keys=[{(r['sid'],r['month']) for r in base if r['fuente']==source and r['referencia']==w} for w in available]
        case_keys=[{c['caso_id'] for c in cases if c['item']['fuente']==source and c['item']['window']==w} for w in available]
        common_real=set.intersection(*real_keys);common_cases=set.intersection(*case_keys)
        for window in available:
            b=[r for r in base if r['fuente']==source and r['referencia']==window and (r['sid'],r['month']) in common_real]
            c=[c for c in cases if c['item']['fuente']==source and c['item']['window']==window and c['caso_id'] in common_cases]
            metrics,*_=intervals_by_category(b,c,source,window)
            paired.extend(dict(r,cohorte='observaciones_y_casos_comunes') for r in metrics)
            paired_inventory.append(dict(fuente=source,referencia=window,observaciones=len(b),casos=len(c),
                series=len({r['sid'] for r in b}),meses=sorted({r['periodo'] for r in b})))
    save('sensibilidad_pareada.csv',paired);save('cohorte_pareada.csv',paired_inventory)
    save('aplicabilidad_fuentes.csv',[dict(fuente=source,dataset_id=SOURCES[source]['dataset'],
        series_en_panel_principal_36=len({r['sid'] for r in base if r['fuente']==source and r['referencia']==36}),
        estado='no_aplica_ocho_periodos' if source=='SSPD_PLAN' else 'evaluada_con_alcance_experimental') for source in SOURCES])
    real,injected=serialize_details(base,cases)
    save_gzip('puntajes_reales.csv.gz',real);save_gzip('puntajes_inyecciones.csv.gz',injected)
    # Casos detallados completos se conservan, pero no se convierten en réplicas independientes.
    from .report import publish
    publish(base,cases,tables,inventory)
    manifest=dict(protocolo='H4-v2-CV-temporal',ejecucion_utc=datetime.now(timezone.utc).isoformat(),
        semilla=SEED,python=platform.python_version(),numpy=np.__version__,sklearn=sklearn.__version__,
        versiones_dependencias={p:importlib.metadata.version(p) for p in ('numpy','pandas','scipy','scikit-learn','matplotlib','PyYAML')},
        configuracion=dict(ventanas=[24,36,48],vigilancia=12,folds='mitad inicial de referencia y tres validaciones sucesivas',
            metodos=METHODS,tasas_objetivo=CURVE_ALPHAS,prevalencias_supuestas=PREVALENCES,bootstrap_replicas=BOOTSTRAPS,
            unidad_bootstrap='categoria_completa',LOF='deduplicacion_exacta_de_geometria_solo_referencia_igual_para_IF_LOF_KNN',
            calibracion='solo_puntajes_fuera_de_muestra_en_folds_de_referencia',
            precision='escenarios_por_prevalencia_supuesta_y_tasa_alerta_proxy_no_precision_empirica',
            politica_vigilancia='doce_meses_finales_de_racha_contigua_fijada_antes_de_exclusiones'),
        entradas={c['path']:digest(ROOT/c['path']) for c in SOURCES.values()},
        entradas_auxiliares={p.relative_to(ROOT).as_posix():digest(p) for p in (
            ROOT/'Data/gold/outputs/calidad/matriz_oe1.csv',ROOT/'Data/gold/outputs/calidad/matriz_oe1.yaml',
            ROOT/'Data/silver/catalogos/EPM/epm_etiquetas.yaml',
            ROOT/'Data/gold/outputs/regla_sistemica/evidencia_externa/tarifas_epm_publicadas.csv')},
        cuarentena=dict(archivo='Data/gold/outputs/hito3/cuarentena_celdas_epm.csv',sha256=digest(ROOT/'Data/gold/outputs/hito3/cuarentena_celdas_epm.csv')),
        codigo={p.relative_to(ROOT).as_posix():digest(p) for folder in ('Code/hito3','Code/hito4') for p in sorted((ROOT/folder).glob('*.py'))},
        salidas={p.relative_to(ROOT).as_posix():digest(p) for p in sorted(OUT.rglob('*')) if p.is_file() and p.name!='manifiesto.json'},
        estado='tecnico_corregido_pendiente_validacion_externa_y_aprobacion')
    (OUT/'manifiesto.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print('H4 v2 generado:',OUT,flush=True)


if __name__=='__main__':main()
