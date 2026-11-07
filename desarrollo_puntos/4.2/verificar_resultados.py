"""Audita las tablas, sus denominadores, las banderas y las huellas de 4.2."""
from collections import defaultdict
import csv
import gzip
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import os

import pandas as pd

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
METHODS=('I_2.66_MRmedia','MR_3.267_MRmedia','IMR_clasica',
         'MAD_2.66sigma','MAD_3sigma','MAD_3.267sigma',
         'IF_p99','IF_p99.5','R12_f5','R12_f10','R12_f20')


def digest(path):
    h=hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda:stream.read(1<<20),b''):h.update(block)
    return h.hexdigest()


def next_month(label):
    year,month=map(int,label.split('-'))
    return f'{year+month//12:04d}-{month%12+1:02d}'


def main():
    sys.stdout.reconfigure(encoding='utf-8')
    config=json.loads((HERE/'configuracion.json').read_text(encoding='utf-8'))
    checks=[]
    for entry in [*config['entradas'].values(),config['cuarentena_EPM']]:
        assert digest(ROOT/entry['ruta'])==entry['sha256']
    for path,expected in config['dependencias'].items():assert digest(ROOT/path)==expected
    checks.append('Cuatro datasets, cuarentena y dependencias conservan sus huellas')
    manifest=json.loads((HERE/'manifiesto_resultados.json').read_text(encoding='utf-8'))
    for entry in manifest['archivos']:
        assert digest(HERE/entry['archivo'])==entry['sha256'],entry['archivo']
    checks.append('Todas las huellas del manifiesto coinciden')

    coverage=pd.read_csv(HERE/'cobertura_ventanas.csv')
    assert len(coverage)==24
    assert (coverage[(coverage.fuente=='SSPD')&(coverage.referencia==48)].series_elegibles==0).all()
    models=pd.read_csv(HERE/'modelos_IF.csv')
    assert (models.ultimo_mes_entrenamiento<models.primer_mes_vigilancia).all()
    assert (models.umbral_p99<=models.umbral_p99_5).all()
    checks.append('SSPD 48 no evaluable y todos los modelos IF respetan el corte temporal')

    real_lookup={}
    totals=defaultdict(lambda:[0,0])
    with gzip.open(HERE/'alertas_reales_detalle.csv.gz','rt',encoding='utf-8',newline='') as f:
        for row in csv.DictReader(f):
            flags=[int(row[m]) for m in METHODS]
            assert flags[3]>=flags[4]>=flags[5]
            assert flags[6]>=flags[7]
            assert flags[8]>=flags[9]>=flags[10]
            key=(row['fuente'],row['cohorte'],int(row['referencia']),row['sid'],row['periodo'])
            assert key not in real_lookup
            real_lookup[key]=flags
            for m,value in zip(METHODS,flags):
                t=totals[key[:3]+(m,)]
                t[0]+=1;t[1]+=value
    assert len(real_lookup)==config['detalle']['alertas_reales']
    real=pd.read_csv(HERE/'tasas_alerta_reales.csv')
    for row in real.itertuples(index=False):
        assert totals[(row.fuente,row.cohorte,row.referencia,row.metodo)]==[row.observaciones,row.alertas]
        assert abs(row.tasa_alerta-row.alertas/row.observaciones)<1e-12
    checks.append('Cada tasa real coincide con el detalle; umbrales monotónicos')

    trial_totals=defaultdict(lambda:[0,0,0,0,0])
    n=0
    with gzip.open(HERE/'inyecciones_detalle.csv.gz','rt',encoding='utf-8',newline='') as f:
        for row in csv.DictReader(f):
            n+=1
            group=(row['fuente'],row['cohorte'],int(row['referencia']))
            key=group+(row['sid'],row['periodo_t'])
            a=real_lookup[key]
            b=real_lookup[group+(row['sid'],next_month(row['periodo_t']))]
            for j,m in enumerate(METHODS):
                t,t1,nt,nt1=[int(row[m+suffix]) for suffix in ('_t','_t1','_nueva_t','_nueva_t1')]
                assert nt==int(t and not a[j])
                assert nt1==int(t1 and not b[j])
                if row['clase_ensayo']=='individual':
                    acc=trial_totals[group+(row['tipo'],m)]
                    for i,val in enumerate((1,t,int(t or t1),nt,int(nt or nt1))):acc[i]+=val
    assert n==config['detalle']['inyecciones']
    detections=pd.read_csv(HERE/'deteccion_inyecciones.csv')
    for row in detections.itertuples(index=False):
        key=(row.fuente,row.cohorte,row.referencia,row.tipo,row.metodo)
        assert trial_totals[key]==[row.casos,row.detecciones_t,row.detecciones_t_o_t1,
                                  row.detecciones_nuevas_t,row.detecciones_nuevas_t_o_t1]
        assert row.detecciones_t_o_t1>=row.detecciones_t
    effects=pd.read_csv(HERE/'efecto_regla_sistemica_inyecciones.csv')
    assert (effects.retenidas_t_o_t1<=effects.detecciones_t_o_t1).all()
    assert (effects[effects.fuente=='XM'].retenidas_t_o_t1==
            effects[effects.fuente=='XM'].detecciones_t_o_t1).all()
    checks.append('Inyecciones reconciliadas por tipo, método y horizonte; señales nuevas verificadas')
    checks.append('La regla sistémica no aumenta detecciones y no se aplica a XM con una serie')

    env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1',PYTHONIOENCODING='utf-8')
    tests=subprocess.run([sys.executable,'-m','unittest','discover','-s',str(HERE),
                          '-p','test_sensibilidad.py','-v'],capture_output=True,text=True,encoding='utf-8',env=env)
    assert tests.returncode==0,tests.stdout+tests.stderr
    checks.append('Nueve pruebas automáticas de propiedades y ausencia de fuga temporal: correctas')
    report={'estado':'correcto','fecha_cliente':'2026-11-06','comprobaciones':checks,
            'escenarios':len(pd.read_csv(HERE/'ejecuciones.csv')),'modelos_IF':len(models),
            'observaciones_detalle':len(real_lookup),'ensayos_detalle':n,
            'pruebas_automaticas':tests.stderr}
    (HERE/'verificacion.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    manifest['archivos']=[{'archivo':p.relative_to(HERE).as_posix(),'bytes':p.stat().st_size,'sha256':digest(p)}
                         for p in sorted(HERE.rglob('*')) if p.is_file()
                         and p.name!='manifiesto_resultados.json' and '__pycache__' not in p.parts]
    (HERE/'manifiesto_resultados.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in report.items() if k!='pruebas_automaticas'},ensure_ascii=False,indent=2))


if __name__=='__main__':main()
