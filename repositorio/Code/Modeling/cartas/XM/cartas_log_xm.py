"""Genera la carta I-MR preliminar de la serie mensual XM."""

from pathlib import Path as _ProjectPath
_PROJECT_ROOT = next(p for p in _ProjectPath(__file__).resolve().parents if (p / "project.json").is_file())
import csv, math, statistics
from pathlib import Path
ROOT=_PROJECT_ROOT
src=(_PROJECT_ROOT / 'Data/datos/Datos_seleccionados/XM_piloto/xm_demanda_mensual_piloto.csv')
out=(_PROJECT_ROOT / 'Outputs/cartas/XM/cartas_log_xm.csv')
rows=list(csv.DictReader(open(src,encoding='utf-8-sig')))
rows=sorted(rows,key=lambda r:r['periodo'])
vals=[float(r['demanda_kwh']) for r in rows if float(r['demanda_kwh'])>0]
changes=[math.log(b)-math.log(a) for a,b in zip(vals,vals[1:])]
ref=changes[:36]; vig=changes[36:48]
mu=statistics.mean(ref); sd=statistics.stdev(ref); lo,hi=mu-3*sd,mu+3*sd
signals=sum(x<lo or x>hi for x in vig)
result={'serie':'EPMC|EPMD|STR02','medida':'demanda_kwh','periodos':len(vals),'cambios_referencia':len(ref),'cambios_vigilancia':len(vig),'limite_inferior':f'{lo:.8f}','limite_superior':f'{hi:.8f}','señales':signals}
with open(out,'w',newline='',encoding='utf-8') as f:
 w=csv.DictWriter(f,fieldnames=list(result));w.writeheader();w.writerow(result)
print(f'periodos={len(vals)} señales={signals} archivo={out}')
