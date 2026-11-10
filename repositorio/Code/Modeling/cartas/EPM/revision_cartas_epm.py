"""Expande las señales de cartas_log_epm.csv para revisión documental."""

from pathlib import Path as _ProjectPath
_PROJECT_ROOT = next(p for p in _ProjectPath(__file__).resolve().parents if (p / "project.json").is_file())
import csv, math, statistics
from pathlib import Path
ROOT=_PROJECT_ROOT
src=(_PROJECT_ROOT / 'Data/datos/Datos_seleccionados/EPM/epm_sfcd-b3ey.csv')
out=(_PROJECT_ROOT / 'Outputs/cartas/EPM/revision_senales_cartas_epm.csv')
months={m:i for i,m in enumerate(('Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre'),1)}
cats=('tipodeinformacion','tipodetarifa','tipodedato','rangodeconsumo','nivel'); measures=('propiedadepm','compartido','propiedaddelcliente','punta','fueradepunta')
rows=list(csv.DictReader(open(src,encoding='utf-8-sig'))); series={}
for r in rows:
    if not r.get('year') or r.get('mes') not in months: continue
    key=tuple(r.get(c,'') for c in cats); p=(int(r['year']),months[r['mes']])
    for m in measures:
        try:v=float(r[m])
        except (TypeError,ValueError):continue
        if v>0: series.setdefault((key,m),{}).setdefault(p,[]).append(v)
outrows=[]
for (key,m),vals in series.items():
    ps=sorted(vals)
    if len(ps)<49:continue
    vs=[sum(vals[p])/len(vals[p]) for p in ps]; ch=[(ps[i],math.log(vs[i])-math.log(vs[i-1]),vs[i-1],vs[i]) for i in range(1,len(vs))]
    ref=[x[1] for x in ch[:36]]; vig=ch[36:48]
    lo=statistics.mean(ref)-3*statistics.stdev(ref); hi=statistics.mean(ref)+3*statistics.stdev(ref)
    for p,x,prev,cur in vig:
        if x<lo or x>hi: outrows.append({'serie':'|'.join(key),'medida':m,'periodo':f'{p[0]}-{p[1]:02d}','valor_anterior':f'{prev:.4f}','valor_actual':f'{cur:.4f}','cambio_log':f'{x:.8f}','limite_inferior':f'{lo:.8f}','limite_superior':f'{hi:.8f}','clasificacion':'pendiente_revision'})
with open(out,'w',newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f,fieldnames=list(outrows[0]) if outrows else ['serie']);w.writeheader();w.writerows(outrows)
print(f'senales={len(outrows)} archivo={out}')
