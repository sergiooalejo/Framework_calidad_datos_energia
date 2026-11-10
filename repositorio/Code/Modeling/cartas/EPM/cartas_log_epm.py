"""Genera la línea base I-MR sobre cambios logarítmicos de EPM.

La referencia son los primeros 36 cambios de cada serie y la vigilancia los
12 siguientes; no se imputan meses ni se cruzan huecos. El CSV resultante es
una evidencia reproducible para CART01, no una corrección del dato original.
"""

from pathlib import Path as _ProjectPath
_PROJECT_ROOT = next(p for p in _ProjectPath(__file__).resolve().parents if (p / "project.json").is_file())
import csv, hashlib, json, math, statistics
from pathlib import Path

ROOT = _PROJECT_ROOT
src = (_PROJECT_ROOT / 'Data/datos/Datos_seleccionados/EPM/epm_sfcd-b3ey.csv')
out = (_PROJECT_ROOT / 'Outputs/cartas/EPM/cartas_log_epm.csv')
quar_path = (_PROJECT_ROOT / 'Outputs/cuarentena_bootstrap/EPM/cuarentena_registros.csv')
quarantined = {r["clave_contenido"] for r in csv.DictReader(quar_path.open(encoding="utf-8"))} if quar_path.exists() else set()
months = {m:i for i,m in enumerate(("Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"),1)}
cats = ("tipodeinformacion","tipodetarifa","tipodedato","rangodeconsumo","nivel")
measures = ("propiedadepm","compartido","propiedaddelcliente","punta","fueradepunta")
rows = list(csv.DictReader(open(src, encoding="utf-8-sig")))
def row_key(row):
    payload=json.dumps(row,ensure_ascii=False,sort_keys=True,separators=(",", ":"))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()
series = {}
for r in rows:
    if row_key(r) in quarantined:
        continue
    if not r.get("year") or r.get("mes") not in months:
        continue
    key = tuple(r.get(c,"") for c in cats)
    period = (int(r["year"]), months[r["mes"]])
    for m in measures:
        try: v=float(r[m])
        except (TypeError,ValueError): continue
        if v > 0: series.setdefault((key,m),{}).setdefault(period,[]).append(v)
results=[]
for (key,m), vals in series.items():
    periods=sorted(vals)
    if len(periods)<49: continue
    values=[sum(vals[p])/len(vals[p]) for p in periods]
    changes=[]
    for i in range(1,len(values)):
        if values[i-1] <= 0 or values[i] <= 0: continue
        changes.append((periods[i], math.log(values[i])-math.log(values[i-1])))
    if len(changes)<48: continue
    ref=[x for _,x in changes[:36]]
    vig=[x for _,x in changes[36:48]]
    mean=statistics.mean(ref); sd=statistics.stdev(ref) if len(ref)>1 else 0
    lo,hi=mean-3*sd,mean+3*sd
    signals=sum(x<lo or x>hi for x in vig)
    results.append({"serie":"|".join(key),"medida":m,"periodos":len(periods),"cambios_referencia":len(ref),"cambios_vigilancia":len(vig),"limite_inferior":f"{lo:.8f}","limite_superior":f"{hi:.8f}","señales":signals})
with open(out,"w",newline="",encoding="utf-8") as f:
    w=csv.DictWriter(f,fieldnames=list(results[0]) if results else ["serie"]); w.writeheader(); w.writerows(results)
print(f"series={len(results)} señales={sum(int(r['señales']) for r in results)} archivo={out}")
