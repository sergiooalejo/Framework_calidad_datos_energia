"""Scorecard, regla sistémica, figuras y resultados del protocolo H4 v2."""
from collections import defaultdict,Counter
import json
import math
from pathlib import Path

import numpy as np
from Code.hito3.core import ROOT,read_csv,digest,label,write_csv
from .protocol import METHODS,CURVE_ALPHAS

OUT=ROOT/'Data/gold/outputs/hito4'


def save(name,rows):
    fields=list(dict.fromkeys(k for row in rows for k in row)) or ['estado']
    write_csv(OUT/name,rows,fields)


def scorecard():
    matrix=read_csv(ROOT/'Data/gold/outputs/calidad/matriz_oe1.csv')
    indicators=[];summary=[];groups=defaultdict(list)
    for r in matrix:
        row=dict(r)
        measurement=r['estado_medicion'];operator=r['umbral_operador'];cut=r['umbral_valor'];value=r['resultado_valor']
        assessment='sin_umbral_cuantitativo'
        if measurement=='no_aplica':assessment='no_aplica'
        elif not value:assessment='sin_medicion'
        elif cut and operator in ('>=','<=','>','<','=='):
            a,b=float(value),float(cut)
            passed={'>=':a>=b,'<=':a<=b,'>':a>b,'<':a<b,'==':a==b}[operator]
            assessment='satisface_umbral_propuesto' if passed else 'no_satisface_umbral_propuesto'
        row.update(estado_frente_umbral=assessment,
                   decision_final='no_aplica' if measurement=='no_aplica' else
                   'pendiente_evidencia' if measurement in ('no_medible','provisional_proxy') else 'pendiente_aprobacion',
                   aceptacion_director='no_registrada',
                   nota_scorecard='Resultado técnico individual; satisfacer una meta propuesta no acredita aprobación ni exactitud global.')
        indicators.append(row);groups[(r['fuente'],r['dimension'])].append(row)
    for (source,dimension),rows in sorted(groups.items()):
        counts=Counter(r['estado_medicion'] for r in rows)
        summary.append(dict(fuente=source,dimension=dimension,controles=len(rows),controles_medidos=counts['medido'],
            controles_provisionales=sum(counts[s] for s in ('provisional','provisional_proxy','provisional_interno')),
            controles_no_medibles=counts['no_medible'],controles_no_aplica=counts['no_aplica'],
            satisface_umbral_propuesto=sum(r['estado_frente_umbral']=='satisface_umbral_propuesto' for r in rows),
            no_satisface_umbral_propuesto=sum(r['estado_frente_umbral']=='no_satisface_umbral_propuesto' for r in rows),
            sin_umbral_cuantitativo=sum(r['estado_frente_umbral']=='sin_umbral_cuantitativo' for r in rows),
            promedio_indicadores='',estado_scorecard='medicion_y_decision_separadas',
            nota='Sin puntuación global: metas, sentidos, poblaciones y aprobación se conservan por indicador.'))
    save('scorecard_indicadores.csv',indicators);save('scorecard_dimensiones.csv',summary)
    return indicators,summary


def systemic(base,cases):
    alpha_index=CURVE_ALPHAS.index(.05)
    groups=defaultdict(list)
    for row in base:groups[(row['fuente'],row['referencia'],row['month'])].append(row)
    catalog=[];lookup={}
    for (source,window,month),rows in sorted(groups.items()):
        for m,method in enumerate(METHODS):
            total=sum(int(r['flags'][m,alpha_index]) for r in rows);n=len(rows)
            fraction=total/n
            state=dict(fuente=source,referencia=window,periodo=label(month),metodo=method,series_observadas=n,
                       categorias_observadas=len({r['categoria'] for r in rows}),series_con_alerta=total,fraccion=fraction,
                       estado='candidato_para_contraste' if n>=2 else 'no_aplica_una_serie')
            for percent in (10,25,50,75):
                state[f'sistemico_X{percent}']=int(n>=2 and fraction>percent/100)
            state['clasificacion_regulatoria']='no_confirmada'
            catalog.append(state);lookup[(source,window,month,method)]=(rows,total)
    effects=defaultdict(lambda:[0,0,0])
    for case in cases:
        source=case['item']['fuente'];window=case['item']['window'];sid=case['item']['sid'];month=case['month']
        for m,method in enumerate(METHODS):
            context=lookup.get((source,window,month,method))
            if context is None:continue
            rows,total=context;original=next((r for r in rows if r['sid']==sid),None)
            if original is None:continue
            detected=int(case['hits'][m,alpha_index,0]);changed=total-int(original['flags'][m,alpha_index])+detected
            for percent in (10,25,50,75):
                group=effects[(source,window,method,percent,'individual')]
                masked=len(rows)>=2 and changed/len(rows)>percent/100
                group[0]+=1;group[1]+=detected;group[2]+=detected*masked
    # Estrés masivo: rasgos y modelos no usan agregados contemporáneos; por eso
    # combinar alteraciones individuales recalcula exactamente el contexto colectivo.
    case_groups=defaultdict(list)
    for c in cases:
        if c['tipo'] in ('decimal_x1000','aumento_10pct'):
            case_groups[(c['item']['fuente'],c['item']['window'],c['tipo'],c['month'])].append(c)
    chosen={}
    for (source,window,kind,month),records in case_groups.items():
        key=source,window,kind
        if key not in chosen or (len(records),month)>(len(chosen[key][1]),chosen[key][0]):chosen[key]=(month,records)
    for (source,window,kind),(month,records) in chosen.items():
        edited={c['item']['sid']:c for c in records}
        for m,method in enumerate(METHODS):
            rows,total=lookup[(source,window,month,method)]
            changed=sum(int(edited[r['sid']]['hits'][m,alpha_index,0]) if r['sid'] in edited else int(r['flags'][m,alpha_index]) for r in rows)
            detected=sum(int(c['hits'][m,alpha_index,0]) for c in records)
            for percent in (10,25,50,75):
                masked=len(rows)>=2 and changed/len(rows)>percent/100
                group=effects[(source,window,method,percent,'colectivo_'+kind)]
                group[0]+=len(records);group[1]+=detected;group[2]+=detected*masked
    effect_rows=[dict(fuente=s,referencia=w,metodo=m,X=percent/100,tipo_ensayo=kind,casos=v[0],
        detecciones_sin_reclasificar=v[1],detecciones_enmascaradas=v[2],detecciones_retenidas=v[1]-v[2],
        fraccion_enmascarada=v[2]/v[1] if v[1] else None,
        interpretacion='Inyecciones artificiales; no prueba de error o cambio regulatorio real')
        for (s,w,m,percent,kind),v in sorted(effects.items())]
    save('catalogo_sistemico.csv',catalog);save('enmascaramiento.csv',effect_rows)
    aggregate=defaultdict(lambda:[0,0,0])
    for row in catalog:
        for percent in (10,25,50,75):
            counts=aggregate[(row['fuente'],row['referencia'],row['metodo'],percent)]
            counts[0]+=row['series_observadas'];counts[1]+=row['series_con_alerta']
            counts[2]+=row['series_con_alerta']*row[f'sistemico_X{percent}']
    save('efecto_regla_alertas_reales.csv',[dict(fuente=s,referencia=w,metodo=m,X=x/100,observaciones=v[0],
        alertas_originales=v[1],reclasificadas=v[2],retenidas=v[1]-v[2],
        tasa_original=v[1]/v[0],tasa_retenida=(v[1]-v[2])/v[0],
        interpretacion='Reclasificación exploratoria; alertas conservadas y causa sin confirmar') for (s,w,m,x),v in sorted(aggregate.items())])
    return catalog,effect_rows


def regulatory():
    captures=sorted((ROOT/'Data/bronze/normativa_hito4').glob('*/manifiesto.json'))
    if not captures:return []
    documents=json.loads(captures[-1].read_text(encoding='utf-8'))
    facts={
        '0015_2018':('1.3.3 y 1.3.4','Ingresos desde el mes siguiente a la vigencia de la resolución particular; variables anuales desde abril a marzo.',
                     'La regla temporal está verificada literalmente. Falta fecha de notificación/firmeza particular y cálculo LAC para probar aplicación EPM en febrero de 2020.'),
        '0078_2019':('artículos 1 y 19','Aprueba variables de distribución para EPM en aplicación de la metodología 015/2018; exige notificación y admite reposición.',
                     'Publicación en julio de 2019 no basta para atribuir un cambio tarifario concreto a esa fecha.'),
        '0156_2019':('considerandos y artículo 12','Resuelve la reposición de EPM contra 078/2019; exige notificación y publicación, sin recurso adicional.',
                     'Publicada el 2 de enero de 2020; no se ha obtenido constancia de notificación/firmeza ni conciliación de cargos LAC.'),
        '0012_2020':('considerandos y artículo 4','Establece opción tarifaria y rige desde la publicación del 17 de febrero de 2020.',
                     'El PDF EPM de febrero no acredita que esa opción causara su cambio; CU calculado y tarifa aplicada son conceptos distintos.'),
        '0152_2020':('artículos 2, 3, 4 y 5','Modifica reglas de pago diferido y aplicación de opción tarifaria; tiene disposiciones específicas para ZNI.',
                     'Expedida el 30 de julio y publicada el 2 de agosto de 2020: su mención posterior no explica por sí sola un salto inicial de julio. La versión consolidada incluye anotaciones posteriores; no se extrapolan al histórico.'),
        '0003_2021':('artículos 1, 9 y 11','Regula el cálculo de subsidios para consumo residencial de estratos 1 y 2, con tratamiento transitorio durante emergencia sanitaria.',
                     'Vigente desde publicación del 14 de enero de 2021 en su texto original; no demuestra que el costo unitario de todas las categorías debiera cambiar en julio de 2021.'),
    }
    records=[]
    for doc in documents:
        if digest(ROOT/doc['archivo'])!=doc['sha256'] or digest(ROOT/doc['texto'])!=doc['sha256_texto']:
            raise ValueError('Documento regulatorio alterado')
        section,fact,limit=facts[doc['id']]
        records.append(dict(**doc,apartados_contrastados=section,hecho_documentado=fact,limite_inferencia=limit,
                            estado='lectura_de_apartados_verificados',causa_de_alerta_confirmada='no'))
    save('contraste_regulatorio.csv',records)
    # Se conserva el contraste numérico EPM original, junto a su procedencia y hash.
    evidence=ROOT/'Data/gold/outputs/regla_sistemica/evidencia_externa'
    inputs=[evidence/'tarifas_epm_publicadas.csv',ROOT/'Data/gold/outputs/regla_sistemica/contraste_componentes.csv',
            evidence/'referencias_documentales.csv',*sorted(evidence.glob('*.pdf'))]
    (OUT/'evidencia_epm_procedencia.json').write_text(json.dumps([dict(archivo=p.relative_to(ROOT).as_posix(),sha256=digest(p),
        alcance='Evidencia conservada del contraste de publicaciones EPM; no se presenta como nueva validación del publicador') for p in inputs],ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    return records


def figures():
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    import pandas as pd
    folder=OUT/'figuras';folder.mkdir(exist_ok=True)
    plt.rcParams.update({'font.size':9,'axes.spines.top':False,'axes.spines.right':False})
    def export(fig,name):
        fig.tight_layout()
        for suffix in ('png','svg'):fig.savefig(folder/f'{name}.{suffix}',dpi=160,bbox_inches='tight')
        plt.close(fig)
    metrics=pd.read_csv(OUT/'metricas.csv')
    main=metrics[(metrics.referencia==36)&(metrics.tasa_objetivo==.05)&(metrics.prevalencia_supuesta==.05)&(metrics.horizonte=='t')]
    fig,axes=plt.subplots(1,2,figsize=(12,4))
    for ax,column in zip(axes,('recall_macro','f1')):
        for source,rows in main.groupby('fuente'):
            legend=source+' (descriptivo)' if source=='XM' else source
            ax.plot(rows.metodo,rows[column],'o-',label=legend)
            lo='recall_ic95_inferior' if column=='recall_macro' else 'f1_ic95_inferior'
            hi='recall_ic95_superior' if column=='recall_macro' else 'f1_ic95_superior'
            for _,r in rows.iterrows():
                if pd.notna(r[lo]) and pd.notna(r[hi]):ax.vlines(r.metodo,r[lo],r[hi],alpha=.6)
        ax.set_ylim(0,1.02);ax.set_ylabel(column);ax.tick_params(axis='x',rotation=35);ax.legend()
    fig.suptitle('CV solo en referencia · α calibración=5 % · prevalencia supuesta=5 %')
    export(fig,'01_comparacion_metodos')
    curve=pd.read_csv(OUT/'curvas.csv');curve=curve[(curve.referencia==36)&(curve.horizonte=='t')]
    fig,axes=plt.subplots(2,2,figsize=(11,8))
    for ax,(source,rows) in zip(axes.flat,curve.groupby('fuente')):
        for method,data in rows.groupby('metodo'):
            data=data.sort_values('tasa_objetivo');ax.plot(data.tasa_alerta_vigilancia,data.recall_macro,'.-',label=method)
        ax.set(title=source,xlabel='Tasa de alerta observada en vigilancia',ylabel='Recall experimental');ax.legend(fontsize=7)
    export(fig,'02_deteccion_vs_alerta')
    paired=pd.read_csv(OUT/'sensibilidad_pareada.csv')
    if not paired.empty:
        paired=paired[(paired.tasa_objetivo==.05)&(paired.prevalencia_supuesta==.05)&(paired.horizonte=='t')]
        fig,axes=plt.subplots(2,2,figsize=(11,8))
        for ax,(source,rows) in zip(axes.flat,paired.groupby('fuente')):
            for method,data in rows.groupby('metodo'):ax.plot(data.referencia,data.recall_macro,'o-',label=method)
            ax.set(title=source,xlabel='Cambios de referencia (cohorte común)',ylabel='Recall');ax.legend(fontsize=7)
        export(fig,'03_sensibilidad_ventanas_pareada')
    native=pd.read_csv(OUT/'nativos.csv');native=native[(native.referencia==36)&(native.horizonte=='t')]
    native=native.groupby(['fuente','variante'],as_index=False)[['casos','detecciones']].sum()
    fig,ax=plt.subplots(figsize=(12,5))
    for source,rows in native.groupby('fuente'):ax.plot(rows.variante,rows.detecciones/rows.casos,'o-',label=source)
    ax.set_ylabel('Detección con umbral nativo · mezcla diseñada');ax.tick_params(axis='x',rotation=35);ax.legend()
    export(fig,'04_sensibilidad_constantes_percentiles_factores')
    fig,ax=plt.subplots(figsize=(10,4))
    subset=metrics[(metrics.referencia==36)&(metrics.tasa_objetivo==.05)&(metrics.prevalencia_supuesta==.05)]
    for (source,method),rows in subset.groupby(['fuente','metodo']):
        if method=='IMR':ax.plot(rows.horizonte,rows.recall_macro,'o-',label=source)
    ax.set_ylabel('Recall I-MR');ax.legend();export(fig,'05_sensibilidad_horizonte')
    effect=pd.read_csv(OUT/'enmascaramiento.csv');effect=effect[(effect.referencia==36)&(effect.metodo=='IMR')]
    fig,ax=plt.subplots(figsize=(10,4))
    for (source,kind),rows in effect.groupby(['fuente','tipo_ensayo']):
        ax.plot(rows.X,rows.fraccion_enmascarada,'o-',label=f'{source}/{kind}')
    ax.set(xlabel='X exploratorio',ylabel='Fracción de detecciones enmascaradas');ax.legend(fontsize=6,ncol=2)
    export(fig,'06_riesgo_regla_sistemica')
    score=pd.read_csv(OUT/'scorecard_dimensiones.csv')
    fig,ax=plt.subplots(figsize=(11,5));labels=[f'{r.fuente}/{r.dimension}' for r in score.itertuples()]
    ax.bar(range(len(score)),score.controles_no_medibles,label='No medibles')
    ax.bar(range(len(score)),score.controles_provisionales,bottom=score.controles_no_medibles,label='Provisionales')
    ax.set_xticks(range(len(labels)),labels,rotation=90,fontsize=6);ax.set_ylabel('Controles por estado de evidencia');ax.legend()
    export(fig,'07_scorecard_evidencia')
    contrast=pd.read_csv(OUT/'contraste_componentes_vigente.csv')
    fig,axes=plt.subplots(1,3,figsize=(13,5))
    for ax,(period,rows) in zip(axes,contrast.groupby('mes')):
        rows=rows[~rows.componente.str.startswith('CU')]
        ax.barh(rows.componente,rows.cambio_porcentual)
        ax.set(title=period,xlabel='Cambio publicado (%) · sin inferir causa')
        ax.tick_params(axis='y',labelsize=7)
    export(fig,'08_contraste_componentes_epm')
    return [p.relative_to(ROOT).as_posix() for p in sorted(folder.iterdir())]


def publish(base,cases,tables,inventory):
    indicators,dimensions=scorecard();catalog,effects=systemic(base,cases);regulations=regulatory()
    from .systemic_review import load_epm,run as review_epm
    evidence=review_epm(load_epm(),OUT)
    images=figures()
    calibration=tables['calibracion'];low=sum(r['estado']=='congelado_baja_resolucion' for r in calibration)
    excluded=sum(r['estado']!='panel_comun_seis_metodos' for r in tables['cobertura'])
    text=f'''# Verificación del Hito 4 · protocolo v2

La implementación se ejecuta con `python pipeline.py ejecutar hito4`. Conserva las
salidas históricas 4.2–4.4 y genera el protocolo corregido en `Data/gold/outputs/hito4/`.
No declara validación externa ni aprobación académica.

## Protocolo comparativo

Se usan las fuentes y cuarentenas por celda del Hito 3 corregido. La racha mensual
se fija antes de excluir valores; duplicados conflictivos, huecos y valores no
positivos invalidan cambios o rasgos. El análisis es retrospectivo: los doce meses
finales forman vigilancia y los 24/36/48 cambios anteriores forman referencia.
Esto delimita una población distinta del origen inicial del Hito 3.

Cada fuente y fecha de fin de referencia define un banco. Tres folds temporales
expansivos emplean la mitad inicial como primer entrenamiento y validan los tres
bloques siguientes, siempre dentro de referencia. Se recalculan estadísticas,
escalas y modelos en cada fold. Los umbrales por método/tasa se calculan con esos
puntajes fuera de muestra; luego se ajusta el modelo final solo con referencia y
se congelan los umbrales antes de puntuar vigilancia e inyecciones.

Se comparan I-MR, Z robusto, IF, LOF, KNN y R12 sobre los mismos casos en cada banco
común. La tasa se iguala en calibración hasta la resolución de empates; **no se
fuerza igualdad de tasas observadas en vigilancia**. Su diferencia es un resultado,
no un motivo para recalibrar con la prueba. Hay {low} filas de calibración con
menos de cinco alertas esperadas; esa baja resolución se identifica explícitamente.
Los IC son bootstrap pareado de categorías completas, 1.000 repeticiones.

## Tratamiento de LOF

La política técnica fijada antes de evaluar vigilancia elimina duplicados exactos
de los cuatro rasgos estandarizados **solo en referencia**. IF, LOF y KNN reciben
la misma geometría deduplicada. No se eliminan observaciones de prueba ni se cambia
la frecuencia publicada en Bronze. Se registran filas originales, vectores únicos,
vecinos y huella de geometría para cada fold y ajuste final.

Con menos de tres vectores o geometría de referencia numéricamente degenerada, LOF
se declara no interpretable. El banco completo se excluye del panel principal de
seis métodos, sin comparar poblaciones distintas ni inventar puntajes. Se excluyeron
{excluded} bancos por referencia insuficiente o ausencia de calibración/geometría
común. La deduplicación cambia la ponderación de frecuencias de entrenamiento;
esa limitación permanece y no se presenta como aprobación del director.

## Métricas, sensibilidad y población

Los seis tipos de inyección se generan una vez y se comparten entre técnicas.
`tipos.csv` conserva denominadores por tipo; `sorteo.csv` registra 500 réplicas con
tres meses distintos por serie y sin reemplazo dentro de réplica. Esas repeticiones
no aumentan el número de meses independientes. Se reportan t y t o t+1.

Precisión y F1 se calculan para prevalencias **supuestas** de 1 %, 5 % y 10 %.
La tasa de alerta sobre registros reales sin verdad terreno es un proxy; estas
columnas no son precisión empírica. XM no recibe un IC inferencial con una categoría.
No se extrapolan las inyecciones a prevalencia real de errores.

`sensibilidad_pareada.csv` y `cohorte_pareada.csv` usan los mismos casos y
observaciones de vigilancia en las ventanas disponibles por fuente. Las tablas
generales conservan también el panel disponible, que tiene distinta cobertura.
`nativos.csv` contrasta constantes 2,66/3,267 y MAD 2,66/3/3,267, IF 99/99,5 y
R12 5/10/20 sin confundir sensibilidad nativa con la comparación a tasa calibrada.
Los costos por banco/etapa están en `costos.csv` y los niveles en `niveles.csv`.

## Scorecard

Se exportan {len(indicators)} indicadores con fórmula, numerador, denominador,
umbral propuesto, estado de medición, resultado frente al umbral y decisión final;
{len(dimensions)} filas resumen fuente/dimensión. Se distingue satisfacer una meta
propuesta de tenerla aprobada. No se promedian tasas con sentidos/poblaciones
distintas ni se publica un porcentaje global de calidad sin metodología acordada.
Oportunidad y exactitud/catálogos conservan sus limitaciones del Hito 3.

## Regla sistémica y contraste regulatorio

X=10/25/50/75 % son escenarios exploratorios, con desigualdad estricta y mínimo
dos series. Las alertas se conservan y se identifican como candidatas, sin convertir
la coincidencia mensual en cambio regulatorio confirmado. Se recalcula el contexto
tras inyecciones individuales y colectivas y se cuantifica el enmascaramiento.

Se capturaron seis documentos oficiales completos y se verificaron apartados
específicos; el registro está en `contraste_regulatorio.csv`, con hashes, fechas,
localizadores y límites. La 015/2018 enlaza la aplicación de ingresos con la
resolución particular; 078/2019 y 156/2019 son las de EPM. Falta constancia de
notificación/firmeza y conciliación con la liquidación LAC para demostrar el
mecanismo de febrero de 2020. La 152/2020 modifica medidas de pago/opción tarifaria;
la 003/2021 trata subsidios de estratos 1 y 2. Una cita en el encabezado de un PDF
no demuestra que esas normas causaran cada componente observado. Los valores
publicados por EPM se conservan junto a la procedencia del contraste numérico.

La calibración exploratoria de X vuelve a calcular con las entradas y cuarentenas
vigentes una carta móvil nativa I-MR y MAD para 24/36/48 cambios. No reemplaza la
comparación CV de las seis técnicas. `meses_plan_epm.csv`, `calibracion_X.csv` y
`composicion_meses_plan.csv` muestran los tres meses solicitados y la posibilidad
o imposibilidad de separarlos de otros meses. Esos otros meses no se etiquetan como
errores. Se reconciliaron {evidence['celdas_cotejadas']} celdas transcritas con el CSV
EPM y {evidence['sumas_cotejadas']} sumas de componentes con el CU total, tolerancia
de redondeo 0,02; esto verifica concordancia numérica, no causalidad regulatoria.

## Figuras incluidas

Se generaron {len(images)} archivos PNG/SVG, versionables y con huella en el manifiesto:
comparación, curva detección/alerta, ventanas pareadas, constantes/percentiles/factores,
horizontes, riesgo de regla sistémica, evidencia del scorecard y componentes EPM. Sus datos son los
CSV del protocolo v2. Las figuras históricas no se presentan como resultados nuevos.

## Pendientes explícitos para cierre integral

1. Validación externa de alertas reales y precisión empírica, que corresponden al Hito 6.
2. Confirmar la causa concreta de los meses EPM con notificación/firmeza, cálculo LAC
   y/o respuesta del publicador; el contraste normativo por sí solo no la demuestra.
3. Aprobar umbrales de calidad, responsables, prevalencia/método principal y política
   operativa de X y LOF; las decisiones técnicas aquí adoptadas no son esa aprobación.
4. Resolver la evidencia de dimensiones todavía no medibles/provisionales heredada
   del Hito 3 e integrar estos resultados en el documento académico oficial.

No se marca completo el cierre académico mientras esos puntos sigan pendientes.

## Fuentes metodológicas y normativas

- [scikit-learn: validación temporal](https://scikit-learn.org/stable/modules/cross_validation.html#time-series-split).
- [scikit-learn: LOF con novelty=True y observaciones nuevas](https://scikit-learn.org/stable/modules/outlier_detection.html#novelty-detection-with-local-outlier-factor).
'''
    for doc in regulations:text+=f"- [CREG {doc['id']}]({doc['url']}): {doc['apartados_contrastados']}.\n"
    (ROOT/'Docs/VERIFICACION_HITO4.md').write_text(text,encoding='utf-8')
    main=[r for r in tables['metricas'] if r['referencia']==36 and r['tasa_objetivo']==.05
          and r['prevalencia_supuesta']==.05 and r['horizonte']=='t']
    lines=['# Resultados preliminares del Hito 4 · protocolo v2','',
        'Referencia 36, vigilancia 12, tasa objetivo de calibración 5 %, prevalencia **supuesta** 5 % y detección en t. '
        'Todos los umbrales se congelan antes de vigilancia. Los IC son de categorías completas; XM es descriptivo sin IC.','',
        '| Fuente | Método | Recall [IC 95 %] | Alerta observada | Precisión de escenario | F1 [IC 95 %] |',
        '|---|---|---|---|---|---|']
    def interval(value,lo,hi):
        return f'{value:.3f} [{lo:.3f}, {hi:.3f}]' if lo is not None and hi is not None else f'{value:.3f} [sin IC]'
    for r in main:
        lines.append(f"| {r['fuente']} | {r['metodo']} | {interval(r['recall_macro'],r['recall_ic95_inferior'],r['recall_ic95_superior'])} | "
            f"{100*r['tasa_alerta_proxy']:.2f} % | {r['precision_conservadora']:.3f} | {interval(r['f1'],r['f1_ic95_inferior'],r['f1_ic95_superior'])} |")
    lines+=['','Una tasa de alerta observada igual a cero produce precisión de escenario igual a uno '
        'bajo esa fórmula; **no acredita precisión empírica de 100 %**. Un IC degenerado en ese snapshot tampoco '
        'garantiza ausencia de falsas alertas futuras. La precisión real requiere las etiquetas externas del Hito 6.',
        '', 'La comparación general no fuerza un ganador ni convierte diferencias puntuales en evidencia de superioridad. '
        'Las conclusiones deben considerar IC, población, tipos de error, baja resolución de calibración y tasa observada. '
        'Los resultados por tipo, ventanas pareadas, prevalencias y ambos horizontes están en los CSV y figuras.',
        '', 'LOF se calcula con geometría de referencia deduplicada para los tres métodos ML. '
        'La auditoría lof.csv conserva la reducción de frecuencia y verifica si algún banco debe excluirse; '
        'resolver duplicados numéricos no convierte el método en aprobado.',
        '', 'Los tres meses de referencia regulatoria se contrastan en contraste_componentes_vigente.csv y meses_plan_epm.csv. '
        'Los documentos oficiales y el cotejo numérico respaldan el contexto, sin probar por sí solos una causa.']
    (ROOT/'Docs/RESULTADOS_HITO4.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
    criteria=dict(estado='implementacion_tecnica_corregida_con_pendientes_externos',calibracion='CV_solo_referencia_con_umbral_congelado',
        scorecard='indicadores_con_umbral_y_estado_sin_aprobaciones_inferidas',figuras_incluidas=images,
        pendientes_externos=['Precisión empírica y validación externa Hito 6','Notificación/firmeza y conciliación LAC EPM o respuesta del publicador',
                           'Aprobación metodológica de umbrales/políticas/responsables','Evidencia pendiente Hito 3 e integración académica'],
        documento='Docs/VERIFICACION_HITO4.md')
    (OUT/'criterios_cierre.json').write_text(json.dumps(criteria,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
