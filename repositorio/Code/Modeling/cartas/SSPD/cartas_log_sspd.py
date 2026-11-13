"""Genera cartas I-MR preliminares sobre series mensuales SSPD."""

from pathlib import Path as _ProjectPath
_PROJECT_ROOT = next(p for p in _ProjectPath(__file__).resolve().parents if (p / "project.json").is_file())
import csv, math, statistics
from pathlib import Path
ROOT=_PROJECT_ROOT
src=(_PROJECT_ROOT / 'Data/silver/datos/Datos_seleccionados/SSPD/sspd_ebby-cjha_mensual.csv')
out=(_PROJECT_ROOT / 'Data/gold/outputs/cartas/SSPD/cartas_log_sspd.csv')
rows=list(csv.DictReader(open(src,encoding='utf-8-sig')))
cats=('identificador_empresa','estrato_sector','ubicacion','tipo_conexion','tipo_lectura','tipo_factura')
measures=('consumo_basico_sum','consumo_compl_sum','consumo_mayor800_sum','valor_total_sum')
series={}
for r in rows:
    try:p=(int(r['anio']),int(r['periodo']))
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
    vs=[sum(vals[p])/len(vals[p]) for p in ps]
    ch=[(ps[i],math.log(vs[i])-math.log(vs[i-1])) for i in range(1,len(vs))]
    if len(ch)<48:continue
    ref=[x for _,x in ch[:36]]; vig=ch[36:48]; mu=statistics.mean(ref); sd=statistics.stdev(ref) if len(ref)>1 else 0
    lo,hi=mu-3*sd,mu+3*sd; sig=sum(x<lo or x>hi for _,x in vig)
    res.append({'serie':'|'.join(key),'medida':m,'periodos':len(ps),'cambios_referencia':36,'cambios_vigilancia':12,'limite_inferior':f'{lo:.8f}','limite_superior':f'{hi:.8f}','señales':sig})
with open(out,'w',newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f,fieldnames=list(res[0]) if res else ['serie']);w.writeheader();w.writerows(res)
print(f'series={len(res)} señales={sum(int(x["señales"]) for x in res)} archivo={out}')
