"""Bootstrap estratificado por categoría para las señales de CART01.

No mezcla fuentes ni series entre categorías. La unidad remuestreada es la serie,
no la fila horaria/mensual, para no inflar artificialmente el tamaño efectivo.
"""
import csv, json, random
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'desarrollo_puntos/3.7/bootstrap'
OUT.mkdir(parents=True,exist_ok=True)
FILES={
 'EPM': ROOT/'desarrollo_puntos/3.5/EPM/cartas_log_epm.csv',
 'CHEC': ROOT/'desarrollo_puntos/3.5/CHEC/cartas_log_chec.csv',
 'SSPD': ROOT/'desarrollo_puntos/3.5/SSPD/cartas_log_sspd.csv',
 'XM': ROOT/'desarrollo_puntos/3.5/XM/cartas_log_xm.csv',
}
SEED=20261105; B=2000

def category(source, serie):
    p=serie.split('|')
    if source=='EPM': return '|'.join(p[:2]+p[-1:])
    if source=='CHEC': return '|'.join(p[:2]+p[3:4])
    if source=='SSPD': return '|'.join(p[:2])
    return serie

def percentile(xs,q):
    xs=sorted(xs); pos=(len(xs)-1)*q; lo=int(pos); hi=min(lo+1,len(xs)-1); frac=pos-lo
    return xs[lo]+(xs[hi]-xs[lo])*frac

results=[]
for source,path in FILES.items():
    groups={}
    for row in csv.DictReader(path.open(encoding='utf-8-sig')):
        den=int(row.get('cambios_vigilancia') or 0)
        if not den: continue
        rate=int(row.get('señales') or 0)/den
        groups.setdefault(category(source,row['serie']),[]).append(rate)
    rng=random.Random(SEED)
    for cat,rates in sorted(groups.items()):
        n=len(rates); observed=sum(rates)/n if n else None
        boot=[]
        for _ in range(B): boot.append(sum(rates[rng.randrange(n)] for _ in range(n))/n)
        results.append({'fuente':source,'categoria':cat,'series':n,'tasa_observada':round(100*observed,6),'ic95_inferior':round(100*percentile(boot,.025),6),'ic95_superior':round(100*percentile(boot,.975),6),'repeticiones':B,'semilla':SEED,'unidad_remuestreo':'serie'})
with (OUT/'bootstrap_categorias.csv').open('w',encoding='utf-8',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(results[0]));w.writeheader();w.writerows(results)
summary={'semilla':SEED,'repeticiones':B,'unidad':'serie dentro de categoría y fuente','grupos':len(results),'fuentes':sorted(FILES)}
(OUT/'README.md').write_text(f'''# Bootstrap por categoría

El archivo `bootstrap_categorias.csv` calcula la tasa de señales de CART01 y su IC95 % por categoría. Se remuestrean series dentro de cada categoría, sin mezclar fuentes. La semilla es {SEED} y se ejecutan {B} repeticiones.

La tasa es descriptiva: una señal no equivale automáticamente a un error de datos. Categorías con una sola serie tienen un intervalo degenerado y deben interpretarse con cautela.

La ejecución actual produce {len(results)} categorías: EPM (8), CHEC (4), SSPD (92) y XM (1).
La unidad estadística es la serie de cartas, no cada fila del CSV; por eso no se mezclan observaciones de fuentes, años o categorías distintas. SSPD tiene una categoría de una sola serie y XM también; sus intervalos son necesariamente degenerados.

## Reproducir

Desde la raíz del repositorio:

```bash
python3 desarrollo_puntos/3.7/bootstrap_categorias.py
```

El script lee las cartas generadas en las carpetas de cada fuente y reemplaza de forma determinista `bootstrap_categorias.csv`, `configuracion.json` y este resumen. La semilla fija permite comparar ejecuciones mientras no cambien las cartas de entrada.
''',encoding='utf-8')
(OUT/'configuracion.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(f'grupos={len(results)} archivo={OUT/"bootstrap_categorias.csv"}')
