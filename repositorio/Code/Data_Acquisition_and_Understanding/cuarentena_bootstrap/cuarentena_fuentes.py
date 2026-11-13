"""Genera cuarentenas conservadoras para CHEC, SSPD y XM.

Solo registra defectos que pueden contaminar directamente una serie: valores no
numéricos/no finitos o negativos en una medida declarada no negativa. No aparta
ajustes, restricciones negativas ni `NA` categóricos sin una regla aprobada.
"""

from pathlib import Path as _ProjectPath
_PROJECT_ROOT = next(p for p in _ProjectPath(__file__).resolve().parents if (p / "project.json").is_file())
import csv, math, zipfile, io, json, hashlib
from pathlib import Path
ROOT=_PROJECT_ROOT
OUT=(_PROJECT_ROOT / 'Data/silver/verificaciones/trazabilidad_filas'); OUT.mkdir(parents=True,exist_ok=True)

def key(row):
    s=json.dumps(row,ensure_ascii=False,sort_keys=True,separators=(',',':'))
    return hashlib.sha256(s.encode()).hexdigest()

def write(name, rows):
    p=OUT/f'{name}_cuarentena.csv'; fields=['dataset_id','clave_contenido','regla','columna','valor','motivo']
    with p.open('w',encoding='utf-8',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)
    print(name,len(rows),p)

# CHEC: los negativos observados están en componentes que pueden representar
# restricciones/subsidios/ajustes; no se apartan sin catálogo semántico.
write('c698-wqig',[])

# SSPD: el consumo básico del censo de detalle no contiene negativos ni no numéricos.
rows=[]; z=(_PROJECT_ROOT / 'Data/bronze/datos/Datos_seleccionados/SSPD/sspd_ebby-cjha_detalle-compressed.zip')
with zipfile.ZipFile(z) as f:
    n=next(x for x in f.namelist() if x.endswith('.csv'))
    for r in csv.DictReader(io.TextIOWrapper(f.open(n),encoding='utf-8')):
        for c in ('consumo_basico','consumo_complementario','consumo_reside_mayor800'):
            try:v=float(r[c])
            except (ValueError,TypeError):
                rows.append({'dataset_id':'ebby-cjha','clave_contenido':key(r),'regla':'R03','columna':c,'valor':r.get(c,''),'motivo':'consumo no numérico'}); continue
            if not math.isfinite(v) or v<0:
                rows.append({'dataset_id':'ebby-cjha','clave_contenido':key(r),'regla':'R07','columna':c,'valor':r.get(c,''),'motivo':'consumo negativo o no finito'})
write('ebby-cjha',rows)

# XM: mensual seleccionado; valores negativos/no finitos contaminan cartas.
rows=[]; p=(_PROJECT_ROOT / 'Data/silver/datos/Datos_seleccionados/XM_piloto/xm_demanda_mensual_piloto.csv')
for r in csv.DictReader(p.open(encoding='utf-8-sig')):
    try:v=float(r['demanda_kwh'])
    except (ValueError,TypeError):
        rows.append({'dataset_id':'c1b851','clave_contenido':key(r),'regla':'R03','columna':'demanda_kwh','valor':r.get('demanda_kwh',''),'motivo':'demanda no numérica'}); continue
    if not math.isfinite(v) or v<0:
        rows.append({'dataset_id':'c1b851','clave_contenido':key(r),'regla':'R07','columna':'demanda_kwh','valor':r.get('demanda_kwh',''),'motivo':'demanda negativa o no finita'})
write('c1b851',rows)
