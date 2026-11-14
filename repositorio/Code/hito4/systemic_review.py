"""Calibración exploratoria de X y cotejo numérico EPM con las entradas vigentes."""
from collections import defaultdict
from decimal import Decimal
import json
import math
import numpy as np

from Code.hito3.core import ROOT,aliases,business_key,label,month_index,read_csv,SOURCES
from .protocol import statistics,bound_ratio

EVENTS=('2020-02','2020-07','2021-07')


def load_epm():
    from Code.hito3.core import build_series,longest_run,content_key
    rows=read_csv(ROOT/SOURCES['EPM']['path'])
    q=read_csv(ROOT/'Data/gold/outputs/hito3/cuarentena_celdas_epm.csv')
    items=[]
    for (category,measure),points in sorted(build_series('EPM',rows,q).items()):
        run=longest_run(points)
        if len(run)<26:continue
        items.append(dict(sid=content_key({'categoria':json.dumps(category),'medida':measure}),
            category=json.dumps(category,ensure_ascii=False),category_tuple=category,months=np.array(run),
            levels=np.array([points[m]['value'] if not points[m]['reason'] else np.nan for m in run],float)))
    return items


def run(items,out):
    from .report import save
    rows=[];composition=defaultdict(lambda:[0,0])
    for window in (24,36,48):
        for item in items:
            months=item['months'];values=item['levels']
            for index in range(window+1,len(values)):
                levels=values[index-window-1:index+1]
                stats=statistics(levels,window)
                if stats is None or not np.isfinite(levels[-3:]).all():continue
                change=math.log(levels[-1])-math.log(levels[-2])
                previous=math.log(levels[-2])-math.log(levels[-3])
                imr=max(float(bound_ratio(abs(change-stats['mean']),2.66*stats['mr'])),
                        float(bound_ratio(abs(change-previous),3.267*stats['mr'])))>.5
                mad=float(bound_ratio(abs(change-stats['median']),stats['sigma']))>.75
                period=label(int(months[index]))
                for method,flag in (('IMR_nativo',imr),('MAD3_nativo',mad)):
                    rows.append(dict(referencia=window,periodo=period,sid=item['sid'],categoria=item['category'],
                        componente=item['category_tuple'][2],metodo=method,senal=int(flag)))
                    group=composition[(window,period,method,item['category_tuple'][2])]
                    group[0]+=1;group[1]+=int(flag)
    aggregated=defaultdict(lambda:[0,0,set()])
    for row in rows:
        value=aggregated[(row['referencia'],row['periodo'],row['metodo'])]
        value[0]+=1;value[1]+=row['senal'];value[2].add(row['categoria'])
    fractions=[dict(referencia=w,periodo=p,metodo=m,series_evaluadas=v[0],series_con_alerta=v[1],categorias=len(v[2]),fraccion=v[1]/v[0])
               for (w,p,m),v in sorted(aggregated.items())]
    save('regla_X_fracciones_epm_rolling.csv',fractions)
    event_rows=[];calibration=[]
    for window in (24,36,48):
        for method in ('IMR_nativo','MAD3_nativo'):
            selected=[r for r in fractions if r['referencia']==window and r['metodo']==method and r['series_evaluadas']>=2]
            events=[r for r in selected if r['periodo'] in EVENTS]
            background=[r['fraccion'] for r in selected if r['periodo'] not in EVENTS]
            for period in EVENTS:
                found=next((r for r in events if r['periodo']==period),None)
                event_rows.append(found or dict(referencia=window,periodo=period,metodo=method,series_evaluadas=0,
                                                series_con_alerta=None,categorias=0,fraccion=None))
            complete=len(events)==3
            low=max(background,default=0);high=min((r['fraccion'] for r in events),default=0)
            for percent in range(1,100):
                x=percent/100
                calibration.append(dict(referencia=window,metodo=method,X=x,meses_plan_evaluables=len(events),
                    meses_plan_capturados=sum(r['fraccion']>x for r in events),otros_meses_marcados=sum(f>x for f in background),
                    limite_inferior_factible=low if complete and low<high else None,
                    limite_superior_exclusivo_factible=high if complete and low<high else None,
                    estado='banda_exploratoria_factible' if complete and low<high else 'sin_banda_factible' if complete else 'meses_plan_no_evaluables',
                    interpretacion='Los tres meses son referencias del plan, no etiquetas causales ni errores confirmados'))
    save('meses_plan_epm.csv',event_rows);save('calibracion_X.csv',calibration)
    comp=[dict(referencia=w,periodo=p,metodo=m,componente=c,series_evaluadas=v[0],series_con_alerta=v[1])
          for (w,p,m,c),v in sorted(composition.items()) if p in EVENTS]
    save('composicion_meses_plan.csv',comp)
    raw=read_csv(ROOT/SOURCES['EPM']['path']);mapping=aliases()
    # Solo para cotejar rótulos del componente: mayúsculas y espacios no
    # cambian tokens/puntuación. No modifica claves ni series del experimento.
    orthographic=lambda value:''.join(value.casefold().split())
    published=read_csv(ROOT/'Data/gold/outputs/regla_sistemica/evidencia_externa/tarifas_epm_publicadas.csv')
    by_period_component={(r['periodo'],mapping.get(('tipodedato',r['componente']),r['componente'])):r for r in published}
    comparisons=[];sums=[];contrast=[]
    measures=('propiedadepm','compartido','propiedaddelcliente')
    for pub in published:
        if pub['componente'].startswith('CU'):continue
        component=mapping.get(('tipodedato',pub['componente']),pub['componente'])
        selected=[r for r in raw if r['nivel']=='I' and r['tipodeinformacion']=='Monomia'
            and orthographic(mapping.get(('tipodedato',r['tipodedato']),r['tipodedato']))==orthographic(component)
            and (p:=month_index(r,SOURCES['EPM'])) is not None and label(p)==pub['periodo']]
        for measure in measures:
            observed=sorted({Decimal(r[measure]) for r in selected if r.get(measure)})
            target=Decimal(pub[measure])
            comparisons.append(dict(periodo=pub['periodo'],componente=component,columna=measure,valor_publicado=str(target),
                valores_csv='|'.join(str(v) for v in observed),coincide=int(any(abs(v-target)<=Decimal('.02') for v in observed)),
                etiquetas_csv='|'.join(sorted({r['tipodedato'] for r in selected})),
                alcance='Concordancia numérica de componente monomio nivel I; no validación económica de cada tarifa'))
    for period in sorted({r['periodo'] for r in published}):
        selected=[r for r in published if r['periodo']==period]
        total=next(r for r in selected if r['componente']=='CU total')
        components=[r for r in selected if not r['componente'].startswith('CU')]
        for measure in measures:
            summed=sum(Decimal(r[measure]) for r in components);difference=summed-Decimal(total[measure])
            sums.append(dict(periodo=period,columna=measure,cu_total=total[measure],suma_componentes=str(summed),
                             diferencia=str(difference),dentro_tolerancia=int(abs(difference)<=Decimal('.02'))))
    for base,period in (('2020-01','2020-02'),('2020-06','2020-07'),('2021-06','2021-07')):
        for (p,component),pub in by_period_component.items():
            if p!=period or (base,component) not in by_period_component:continue
            a=float(by_period_component[(base,component)]['propiedadepm']);b=float(pub['propiedadepm'])
            record=dict(mes_base=base,mes=period,componente=component,valor_base=a,valor_mes=b,cambio_absoluto=b-a,
                cambio_porcentual=100*(b-a)/a if a>0 and b>0 else None,
                observacion='sin_logaritmo_por_signo' if a<=0 or b<=0 else 'cambio_publicado_no_causa_confirmada')
            for method in ('IMR_nativo','MAD3_nativo'):
                states=[r for r in comp if r['referencia']==36 and r['periodo']==period and r['metodo']==method
                        and orthographic(r['componente'])==orthographic(component)]
                record['alertas_'+method]=sum(r['series_con_alerta'] for r in states) if states else None
                record['evaluadas_'+method]=sum(r['series_evaluadas'] for r in states) if states else None
            contrast.append(record)
    save('cotejo_epm_celdas.csv',comparisons);save('cotejo_epm_suma.csv',sums);save('contraste_componentes_vigente.csv',contrast)
    if not all(r['coincide'] for r in comparisons) or not all(r['dentro_tolerancia'] for r in sums):
        raise ValueError('El cotejo numérico EPM debe revisarse; no se declara concordancia')
    return dict(celdas_cotejadas=len(comparisons),sumas_cotejadas=len(sums),meses_plan=event_rows)
