"""Línea base I-MR preliminar de CHEC en cambios logarítmicos."""
import csv, math, statistics
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]; src=ROOT/'fuentes_datos/datos/Datos_seleccionados/CHEC/chec_c698-wqig.csv'; out=Path(__file__).resolve().parent/'cartas_log_chec.csv'
rows=list(csv.DictReader(open(src,encoding='utf-8-sig'))); cats=('comercializador_codigo','mercado_codigo','costounitariotarifa_tipomed','nivel_tension_codigo','modalidadcobro_propiedad','claseservicio_codigo','costounitariotarifa_rangoconsumo','costounitariotarifa_tipomercado'); measures=('costounitariotarifa_cu','costounitariotarifa_valor_tarifa')
series={}
for r in rows:
    try:p=(int(r['costounitariotarifa_ano']),int(r['costounitariotarifa_mes']))
    except (ValueError,TypeError):continue
    key=tuple(r.get(c,'') for c in cats)
    for m in measures:
        try:v=float(r[m])
        except (ValueError,TypeError):continue
        if v>0:series.setdefault((key,m),{}).setdefault(p,[]).append(v)
res=[]
for (key,m),vals in series.items():
    ps=sorted(vals)
    if len(ps)<49:continue
    vs=[sum(vals[p])/len(vals[p]) for p in ps]; ch=[(ps[i],math.log(vs[i])-math.log(vs[i-1])) for i in range(1,len(vs))]
    ref=[x for _,x in ch[:36]]; vig=ch[36:48]
    if len(ref)<2 or len(vig)<12:continue
    mu=statistics.mean(ref); sd=statistics.stdev(ref); lo,hi=mu-3*sd,mu+3*sd; signals=sum(x<lo or x>hi for _,x in vig)
    res.append({'serie':'|'.join(key),'medida':m,'periodos':len(ps),'cambios_referencia':36,'cambios_vigilancia':12,'limite_inferior':f'{lo:.8f}','limite_superior':f'{hi:.8f}','señales':signals})
with open(out,'w',newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f,fieldnames=list(res[0]) if res else ['serie']);w.writeheader();w.writerows(res)
print(f'series={len(res)} señales={sum(int(x["señales"]) for x in res)} archivo={out}')
