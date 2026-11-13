"""Produce tablas de lectura, figuras exportables e informe desde resultados 4.2."""

from pathlib import Path as _ProjectPath
_PROJECT_ROOT = next(p for p in _ProjectPath(__file__).resolve().parents if (p / "project.json").is_file())
from pathlib import Path
import json

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

HERE=(_PROJECT_ROOT / 'Data/gold/outputs/sensibilidad')
SOURCES=('EPM','CHEC','SSPD','XM')
COLORS={'EPM':'#2563eb','CHEC':'#059669','SSPD':'#d97706','XM':'#7c3aed'}


def read(name):return pd.read_csv(HERE/name)


def table(frame, columns):
    rows=['| '+' | '.join(columns)+' |','| '+' | '.join('---' for _ in columns)+' |']
    for row in frame[columns].itertuples(index=False,name=None):
        rows.append('| '+' | '.join('No evaluable' if pd.isna(v) else str(v) for v in row)+' |')
    return '\n'.join(rows)


def save(fig,name):
    target=(_PROJECT_ROOT / 'Data/gold/outputs/sensibilidad/figuras');target.mkdir(exist_ok=True)
    fig.tight_layout()
    for suffix in ('png','svg','pdf'):
        fig.savefig(target/(name+'.'+suffix),dpi=180,bbox_inches='tight')
    plt.close(fig)


def generate():
    coverage=read('cobertura_ventanas.csv')
    real=read('tasas_alerta_reales.csv')
    injections=read('deteccion_inyecciones.csv')
    effects=read('efecto_regla_sistemica_reales.csv')
    stress=read('efecto_regla_sistemica_inyecciones.csv')
    paired=read('comparacion_ventanas_pareada.csv')
    params=read('parametros_por_serie.csv')
    combinations=read('combinaciones_framework.csv')
    runs=read('ejecuciones.csv')
    config=json.loads(((_PROJECT_ROOT / 'Data/gold/outputs/sensibilidad/configuracion.json')).read_text(encoding='utf-8'))
    plt.rcParams.update({'font.size':9,'axes.spines.top':False,'axes.spines.right':False})

    fig,axes=plt.subplots(1,2,figsize=(11,4),sharey=True)
    for ax,panel in zip(axes,('disponible','comun')):
        for source in SOURCES:
            sub=coverage[(coverage.fuente==source)&(coverage.cohorte==panel)]
            ax.plot(sub.referencia,sub.series_elegibles,'o-',label=source,color=COLORS[source])
        ax.set(title='Todas las elegibles' if panel=='disponible' else 'Cohorte común por fuente',
               xlabel='Cambios de referencia',xticks=[24,36,48])
        ax.grid(alpha=.2)
    axes[0].set_ylabel('Series elegibles');axes[1].legend()
    save(fig,'01_cobertura_ventanas')

    methods=('IMR_clasica','MAD_3sigma','IF_p99','IF_p99.5','R12_f10')
    fig,axes=plt.subplots(2,2,figsize=(11,7))
    for ax,source in zip(axes.flat,SOURCES):
        for method in methods:
            sub=real[(real.fuente==source)&(real.cohorte=='comun')&(real.metodo==method)]
            ax.plot(sub.referencia,100*sub.tasa_alerta,'o-',label=method)
        ax.set(title=source,xlabel='Cambios de referencia',ylabel='Alertas / observaciones (%)',xticks=[24,36,48])
        ax.set_ylim(0,max(1,ax.get_ylim()[1]))
        ax.grid(alpha=.2)
    axes[0,0].legend(fontsize=7)
    save(fig,'02_ventanas_cohorte_comun')

    coeffs=('I_2.66_MRmedia','MR_3.267_MRmedia','IMR_clasica','MAD_2.66sigma','MAD_3sigma','MAD_3.267sigma')
    fig,axes=plt.subplots(2,2,figsize=(12,7))
    for ax,source in zip(axes.flat,SOURCES):
        sub=real[(real.fuente==source)&(real.cohorte=='comun')&(real.referencia==36)].set_index('metodo')
        values=[100*sub.loc[m,'tasa_alerta'] for m in coeffs]
        ax.bar(range(len(coeffs)),values,color=COLORS[source])
        ax.set_ylim(0,max(1,ax.get_ylim()[1]))
        if not any(values):ax.text(.5,.5,'0 señales en esta vigilancia',transform=ax.transAxes,ha='center')
        ax.set(title=source,ylabel='Alertas (%)',xticks=range(len(coeffs)))
        ax.set_xticklabels(coeffs,rotation=25,ha='right',fontsize=7)
    save(fig,'03_constantes_y_MAD')

    for number,prefix,methods_list,title in (
        ('04','percentiles_IF',('IF_p99','IF_p99.5'),'Percentiles de referencia IF'),
        ('05','factor_R12',('R12_f5','R12_f10','R12_f20'),'Factor R12 sobre niveles')):
        fig,axes=plt.subplots(1,2,figsize=(11,4))
        for ax,metric,label in zip(axes,('tasa_alerta','tasa_t_o_t1'),('Alertas reales (%)','Detección de inyecciones (%)')):
            for si,source in enumerate(SOURCES):
                if metric=='tasa_alerta':
                    frame=real[(real.fuente==source)&(real.cohorte=='comun')&(real.referencia==36)].set_index('metodo')
                    rates=[100*frame.loc[m,metric] for m in methods_list]
                else:
                    frame=injections[(injections.fuente==source)&(injections.cohorte=='comun')&(injections.referencia==36)]
                    grouped=frame.groupby('metodo')[['detecciones_t_o_t1','casos']].sum()
                    rates=[100*grouped.loc[m,'detecciones_t_o_t1']/grouped.loc[m,'casos'] for m in methods_list]
                ax.plot(range(len(methods_list)),rates,'o-',label=source,color=COLORS[source])
            ax.set(xticks=range(len(methods_list)),xticklabels=methods_list,ylabel=label,title=title)
            ax.set_ylim(0,max(1,ax.get_ylim()[1]))
            ax.grid(alpha=.2)
        axes[1].legend();save(fig,number+'_'+prefix)

    selected=injections[(injections.cohorte=='comun')&(injections.referencia==36)]
    grouped=selected.groupby(['fuente','metodo'],sort=False)[[
        'casos','detecciones_t','detecciones_t_o_t1','detecciones_nuevas_t','detecciones_nuevas_t_o_t1']].sum().reset_index()
    grouped['tasa_t']=grouped.detecciones_t/grouped.casos
    grouped['tasa_t_o_t1']=grouped.detecciones_t_o_t1/grouped.casos
    grouped['ganancia_pp']=100*(grouped.tasa_t_o_t1-grouped.tasa_t)
    grouped['tasa_nueva_t_o_t1']=grouped.detecciones_nuevas_t_o_t1/grouped.casos
    grouped.to_csv((_PROJECT_ROOT / 'Data/gold/outputs/sensibilidad/resumen_horizonte_36.csv'),index=False,encoding='utf-8-sig')
    fig,axes=plt.subplots(2,2,figsize=(12,7))
    plot_methods=('IMR_clasica','MAD_3sigma','IF_p99','IF_p99.5','R12_f10')
    for ax,source in zip(axes.flat,SOURCES):
        g=grouped[grouped.fuente==source].set_index('metodo')
        x=np.arange(len(plot_methods));width=.36
        ax.bar(x-width/2,[100*g.loc[m,'tasa_t'] for m in plot_methods],width,label='Solo t')
        ax.bar(x+width/2,[100*g.loc[m,'tasa_t_o_t1'] for m in plot_methods],width,label='t o t+1')
        ax.set(title=source,ylabel='Detección simulada (%)',xticks=x,ylim=(0,105))
        ax.set_xticklabels(plot_methods,rotation=20,ha='right',fontsize=7)
    axes[0,0].legend();save(fig,'06_horizonte_deteccion')

    fig,axes=plt.subplots(2,2,figsize=(11,7))
    for ax,source in zip(axes.flat,SOURCES):
        for method in plot_methods:
            s=effects[(effects.fuente==source)&(effects.cohorte=='comun')&(effects.referencia==36)&(effects.metodo==method)]
            ax.plot(100*s.umbral_fraccion,100*s.tasa_retenida,'o-',label=method)
        ax.set(title=source if source!='XM' else 'XM · regla no aplicable: una serie',xlabel='Umbral sistémico X (%)',ylabel='Alertas retenidas (%)')
        ax.set_ylim(0,max(1,ax.get_ylim()[1]))
        ax.grid(alpha=.2)
    axes[0,0].legend(fontsize=7);save(fig,'07_efecto_sistemico_reales')

    fig,axes=plt.subplots(2,2,figsize=(11,7))
    for ax,source in zip(axes.flat,SOURCES):
        for method in ('IMR_clasica','MAD_3sigma','IF_p99.5'):
            s=stress[(stress.fuente==source)&(stress.cohorte=='comun')&(stress.referencia==36)&
                     (stress.tipo=='masivo_x1000')&(stress.metodo==method)]
            values=100*s.fraccion_detecciones_enmascaradas
            ax.plot(100*s.umbral_fraccion,values,'o-',label=method)
            if values.isna().all():ax.text(.02,.12,f'{method}: sin detecciones',transform=ax.transAxes,fontsize=7)
        ax.set(title=source if source!='XM' else 'XM · regla no aplicable: una serie',xlabel='Umbral sistémico X (%)',ylabel='Detecciones enmascaradas (%)',ylim=(-3,103))
        ax.grid(alpha=.2)
    axes[0,0].legend(fontsize=7);save(fig,'08_riesgo_errores_masivos')

    fig,axes=plt.subplots(2,2,figsize=(10,7))
    for ax,source in zip(axes.flat,SOURCES):
        s=combinations[(combinations.fuente==source)&(combinations.cohorte=='comun')&
                       (combinations.referencia==36)&(combinations.cartas=='IMR_clasica')]
        pivot=s.pivot(index='factor_R12',columns='percentil_IF',values='tasa_alerta')*100
        im=ax.imshow(pivot.to_numpy(),cmap='YlOrRd',aspect='auto',vmin=0,vmax=max(1,float(pivot.max().max())))
        for i in range(len(pivot.index)):
            for j in range(len(pivot.columns)):
                ax.text(j,i,f'{pivot.iloc[i,j]:.2f}%',ha='center',va='center',fontsize=8)
        ax.set(title=source,xlabel='Percentil IF',ylabel='Factor R12',
               xticks=range(len(pivot.columns)),xticklabels=list(pivot.columns),
               yticks=range(len(pivot.index)),yticklabels=list(pivot.index))
        fig.colorbar(im,ax=ax,label='Tasa de alerta unión (%)')
    save(fig,'09_interaccion_percentil_R12')

    coverage_show=coverage[coverage.cohorte=='disponible'].pivot(index='fuente',columns='referencia',values='series_elegibles').reindex(SOURCES)
    coverage_show.columns=['Ref. '+str(c) for c in coverage_show.columns]
    coverage_show=coverage_show.reset_index().rename(columns={'fuente':'Fuente'})
    focus=real[(real.cohorte=='comun')&(real.referencia==36)&real.metodo.isin(plot_methods)].copy()
    focus['Alertas (%)']=focus.tasa_alerta.map(lambda v:f'{100*v:.3f}')
    focus['IC95 (%)']=focus.apply(lambda r:'Sin IC: una categoría' if pd.isna(r.ic95_inferior)
        else f'{100*r.ic95_inferior:.3f}–{100*r.ic95_superior:.3f}',axis=1)
    focus=focus.rename(columns={'fuente':'Fuente','metodo':'Método','series':'Series'})
    horizon=grouped[grouped.metodo.isin(('IMR_clasica','MAD_3sigma','IF_p99.5','R12_f10'))].copy()
    for old,new in (('tasa_t','Solo t (%)'),('tasa_t_o_t1','t o t+1 (%)'),('tasa_nueva_t_o_t1','Nueva frente a base (%)')):
        horizon[new]=horizon[old].map(lambda v:f'{100*v:.2f}')
    horizon['Ganancia (pp)']=horizon.ganancia_pp.map(lambda v:f'{v:.2f}')
    horizon=horizon.rename(columns={'fuente':'Fuente','metodo':'Método','casos':'Casos'})
    differences=paired[(paired.estado=='mismas_series_y_mismos_meses')&paired.metodo.isin(('IMR_clasica','MAD_3sigma','IF_p99.5'))].copy()
    differences['Cambio (pp)']=(100*differences.diferencia_tasa).map(lambda v:f'{v:+.3f}')
    differences=differences.rename(columns={'fuente':'Fuente','referencia_alternativa':'Ventana vs. 36','metodo':'Método','series':'Series'})
    maxgain=horizon.loc[horizon.ganancia_pp.idxmax()]
    natural=effects[(effects.cohorte=='comun')&(effects.referencia==36)&(effects.metodo=='IMR_clasica')&(effects.umbral_fraccion==.25)].copy()
    natural['Original (%)']=(natural.tasa_original*100).map(lambda x:f'{x:.3f}')
    natural['Retenida (%)']=(natural.tasa_retenida*100).map(lambda x:f'{x:.3f}')
    natural=natural.rename(columns={'fuente':'Fuente','alertas_reclasificadas':'Reclasificadas'})
    madzero=params[(params.cohorte=='comun')&(params.referencia==36)].groupby('fuente').estado_mad.apply(lambda s:int((s=='mad_cero').sum())).to_dict()
    findings=[]
    for source in SOURCES:
        rates=real[(real.fuente==source)&(real.cohorte=='comun')&(real.referencia==36)].set_index('metodo')
        trial=grouped[(grouped.fuente==source)].set_index('metodo')
        findings.append(f"- **{source}:** I/MR clásica genera {100*rates.loc['IMR_clasica','tasa_alerta']:.3f} % "
            f"de alertas reales y MAD 3σ, {100*rates.loc['MAD_3sigma','tasa_alerta']:.3f} %. "
            f"IF p99,5 detecta {100*trial.loc['IF_p99.5','tasa_t_o_t1']:.2f} % de las inyecciones individuales "
            f"en t o t+1, sobre {int(trial.loc['IF_p99.5','casos']):,} casos de la mezcla diseñada.")
    findings='\n'.join(findings)
    body=f'''# Hito 4.2 · Resultados del análisis de sensibilidad

Fecha: 6 de noviembre de 2026. Se ejecutó el punto 2 del Hito 4 del plan local sobre
los snapshots conservados de EPM, CHEC, SSPD y XM. Las salidas de 3.x y 4.1 permanecen intactas.

## Resultado principal

Se evaluaron 24, 36 y 48 cambios de referencia cuando la longitud lo permite, las
constantes I/MR, límites robustos con MAD, percentiles IF 99 y 99,5, R12 con factores
5, 10 y 20, ambos horizontes de detección y cuatro umbrales de reclasificación sistémica.
Se ejecutaron **{len(runs)} escenarios fuente/cohorte/ventana**, con
**{config['detalle']['alertas_reales']:,} observaciones detalladas** y
**{config['detalle']['inyecciones']:,} ensayos de inyección detallados**, sumando paneles
y ventanas. Estos conteos incluyen repeticiones deliberadas del mismo caso bajo otros
parámetros; no son tamaños de muestra independientes. El tipo de ensayo distingue
inyecciones individuales y estrés colectivo.

SSPD no permite 48 cambios más 12 de vigilancia: tiene como máximo 59 meses
consecutivos y esa configuración requiere 61. Se registra como **no evaluable**,
sin recortar vigilancia ni rellenar datos. XM conserva una sola serie/categoría;
sus resultados son descriptivos y no reciben un IC entre categorías.

## 1. Cobertura y comparación de ventanas

{table(coverage_show,list(coverage_show.columns))}

La carga reutiliza `4.1/zscore_robusto.py`. Después se selecciona la racha mensual
consecutiva más larga de cada serie; en empate, la de fin más reciente. Se fija la
vigilancia en sus doce últimos cambios y se toman inmediatamente antes 24, 36 o 48
cambios. No se unen rachas separadas ni se cruza un mes ausente.

El panel `disponible` describe la población elegible de cada ventana. El panel `comun`
mantiene las mismas series, categorías y meses en todas las ventanas factibles de la
fuente. En SSPD compara 24 y 36; en las otras fuentes, 24/36/48. IF también se vuelve
a entrenar dentro de esta cohorte común, evitando que una variación en la población
de entrenamiento se confunda con la longitud de referencia.

Lectura inicial de la cohorte común con referencia 36:

{findings}

Una tasa real de cero significa que estos límites no señalaron esos doce meses;
no demuestra ausencia de errores. La detección artificial también depende del tipo
de perturbación y del umbral: por ejemplo, una configuración IF con pocas alertas
puede tener baja detección de las inyecciones. Se conservan esos resultados sin
ajustar retrospectivamente los percentiles para mejorar la cifra de vigilancia.

Las diferencias siguientes son tasa alternativa menos tasa con referencia 36, en
las mismas series y meses. Sus IC por categorías están en el CSV correspondiente.

{table(differences,['Fuente','Ventana vs. 36','Método','Series','Cambio (pp)'])}

Estos resultados no se comparan directamente con las tasas de 4.1: allí se usaron
los primeros cambios y podían concatenarse parejas consecutivas de distintas rachas.
Aquí la vigilancia es final y toda la partición pertenece a una sola racha continua.

## 2. Constantes y límites robustos

Las constantes del plan cumplen funciones distintas:

- Carta I: media de cambios ± **2,66 × MR medio de referencia**.
- Carta MR: señal si el rango móvil excede **3,267 × MR medio de referencia**.
- `IMR_clasica` es la unión de ambas señales; el primer MR vigilado usa el último
  cambio de referencia, sin incorporar vigilancia al cálculo de límites.
- `MAD_3sigma`: mediana ± **3 × MAD / 0,6744897501960817**.
  También se examinan multiplicadores 2,66 y 3,267 sobre esta escala robusta como
  sensibilidad adicional; no se presentan como las mismas constantes de la carta I/MR.

Las fórmulas se apoyan en [NIST, cartas individuales](https://www.itl.nist.gov/div898/handbook/pmc/section3/pmc322.htm),
[NIST, constantes I/MR](https://nvlpubs.nist.gov/nistpubs/Legacy/IR/nistir4941.pdf) y
[NIST, MAD escalado](https://www.itl.nist.gov/div898/software/dataplot/refman2/auxillar/mad.htm).
Los multiplicadores explorados proceden del plan y del protocolo del proyecto;
no se atribuye a NIST una recomendación de seleccionar uno de ellos para estas fuentes.

Con MAD igual a cero se conserva el criterio explícito de 4.1: cualquier cambio
distinto de la mediana produce una señal y no se añade una escala artificial.
Series con MAD cero en referencia 36/cohorte común: `{madzero}`.
Esto puede hacer que cambiar el multiplicador no tenga efecto; no se interpreta
una tasa idéntica como prueba de robustez del proceso.

Tasas reales bajo referencia 36 y cohorte común:

{table(focus,['Fuente','Método','Series','Alertas (%)','IC95 (%)'])}

Los intervalos son bootstrap descriptivo de **categorías completas**, no de filas
mensuales ni series supuestamente independientes: {config['bootstrap']['repeticiones']}
repeticiones, razón de numeradores y denominadores remuestreados, semilla fija.
Condicionan a las fuentes y modelos ajustados y no incluyen incertidumbre por reentrenamiento
ni garantizan representatividad poblacional. Se conservan por fuente, método y ventana.

## 3. Percentiles 99 y 99,5 de Isolation Forest

Se usan 300 árboles por fuente/ventana/cohorte/calendario de vigilancia, con cuatro rasgos: cambio log actual,
cambio anterior, diferencia absoluta entre cambios y nivel log relativo a la mediana
del nivel de referencia. Centros, escalas y percentiles se calculan solo en referencia;
las inyecciones no vuelven a ajustar el modelo. Las series que terminan en meses
distintos tienen modelos separados, para que ninguna referencia termine después
del inicio de vigilancia de otra serie del mismo modelo. `modelos_IF.csv` conserva
los calendarios y umbrales; el submuestreo es el menor de 256 y el número de referencias.
El umbral 99,5 es mayor o igual al 99
y sus alertas son un subconjunto, verificado durante la ejecución.

Los percentiles son de puntajes **de entrenamiento**. No representan una tasa de
falsas alarmas garantizada fuera de muestra ni equivalen a una validación cruzada
a tasa igualada. Se conserva esta distinción frente al componente de calibración 4.1.

## 4. Sensibilidad de R12 e interacción de parámetros

Se aplica `abs(nivel) > factor × mediana(abs(niveles_referencia))` con factores
5, 10 y 20. El umbral utiliza solo los niveles de referencia; no se estima sobre
la serie completa como ocurría en el Hito 2. R12 se mantiene como advertencia.
En XM se analiza magnitud de demanda, no un importe tarifario ni el valor absoluto
de un cambio logarítmico. Su semántica debe seguir identificada como adaptación.

Además de cada detector aislado, `combinaciones_framework.csv` cruza dos alternativas
de cartas (I/MR clásica o MAD 3σ), dos percentiles IF y tres factores R12, por ventana
y cohorte: doce uniones de señales por escenario. La figura 09 muestra el efecto
conjunto sobre la tasa real de alertas. No se elige una combinación usando la propia
vigilancia como conjunto de validación.

## 5. Detección en t frente a t o t+1

Se perturba un único nivel positivo en copias de la vigilancia, con referencia y modelo
congelados. Se usan todos los once primeros meses, sin reemplazo; el duodécimo es el
seguimiento del último origen. Los seis tipos son multiplicar/dividir por 1.000,
serial Excel fijo 43.577, aumento de 10 %, valor anterior y otra medida positiva
del mismo grupo/mes. La otra medida se elige por orden de nombre para reproducibilidad.
Si el valor no cambia o no existe otra medida, el caso se omite con motivo explícito.

El serial Excel replica un mecanismo de representación tarifaria; en demanda/consumo
es solo una perturbación numérica de escala, no evidencia de un defecto observado.
Signos negativos, ceros, faltantes y texto quedan fuera de este ensayo logarítmico:
no se convierten en logaritmos ficticios ni se mezclan con reglas de validez.

`t1` en el detalle significa la señal **solo en el mes siguiente**. La métrica
`t_o_t1` es la unión, no la suma; una prueba se cuenta una sola vez. Se conservan
también señales nuevas respecto a la copia sin inyección, para mostrar cuánto
puede inflar el resultado la presencia de alertas naturales previas. Estas señales
nuevas no son una estimación de precisión de alertas reales.

Resumen agregado de tipos para referencia 36/cohorte común:

{table(horizon,['Fuente','Método','Casos','Solo t (%)','t o t+1 (%)','Ganancia (pp)','Nueva frente a base (%)'])}

En esta comparación, la mayor ganancia entre los métodos mostrados corresponde a
**{maxgain['Fuente']} / {maxgain['Método']}: {maxgain['ganancia_pp']:.2f} puntos porcentuales**.
Los CSV por tipo conservan denominadores e IC por categoría. Los porcentajes agregados
describen la mezcla de errores diseñada y no una prevalencia real de errores.

## 6. Efecto de la regla sistémica

Para cada fuente, método y mes se divide el número de series-medida con señal entre
las series-medida realmente observadas en vigilancia ese mes. Se evalúan X = 10, 25,
50 y 75 %, con desigualdad estricta `fracción > X`. Se exige al menos dos series;
XM no admite una interpretación transversal con una sola serie y conserva sus alertas.
La unidad series-medida es la misma de los detectores; medidas del mismo grupo pueden
estar correlacionadas, por lo que no se interpreta el denominador como independencia.

Se calcula la tasa original y la retenida para revisión individual. Las señales
reclasificadas quedan guardadas en el catálogo mensual: no se eliminan. La etiqueta
es **candidato sistémico**, sin afirmar que sea un cambio regulatorio confirmado.
La calibración regulatoria y el contraste de fechas concretas son materia de 4.4;
esta ejecución 4.2 estudia sensibilidad sobre una grilla explícita, no elige X óptimo.

Ejemplo I/MR, referencia 36/cohorte común, X = 25 %:

{table(natural,['Fuente','Original (%)','Retenida (%)','Reclasificadas'])}

Se recalcula el contexto mensual al inyectar: para el error individual se cambia
la señal de esa serie; para un evento colectivo se cambian simultáneamente todas
las series afectadas. El estrés colectivo aplica +10 % o ×1.000 en el mes con más
orígenes disponibles (desempate: el más reciente). Permite medir cuántas detecciones
de errores conocidos se ocultarían al aplicar la reclasificación sin validación.
Los eventos colectivos son ensayos descriptivos únicos y no reciben un IC basado
en fingir que cada serie es un evento independiente.

## 7. Lectura y límites

- La comparación de ventanas debe partir del panel común y de sus cambios pareados;
  el panel disponible informa cobertura, pero mezcla poblaciones distintas.
- Un percentil o factor mayor reduce o conserva señales para un modelo/referencia
  dados; una tasa menor no demuestra mejor calidad ni mejor sensibilidad.
- Extender detección a t+1 puede recuperar el retorno del pico o un rasgo rezagado;
  también añade un mes de oportunidad de alerta. Se muestran ambos horizontes y
  las señales nuevas respecto a base, sin presentar esa ganancia como gratuita.
- La regla sistémica reduce la cola de revisión individual, pero puede esconder
  errores masivos. Los resultados de estrés cuantifican ese riesgo por configuración.
- Las series ya tienen restricciones de positividad y cuarentena EPM de la carga 4.1;
  esto condiciona el análisis. No constituye una auditoría de todos los registros fuente.
- La cuarentena histórica permanece fija al variar el factor R12. Se estudia su efecto
  como umbral detector; no se simula una nueva política que readmita o excluya registros
  históricos y vuelva a estimar todas las referencias.
- Las inyecciones siguen la mezcla diseñada; no sustituyen etiquetas externas ni
  completan la validación de alertas reales o todos los experimentos de 4.3.
- No se declaran óptimos umbrales ni aprobaciones de negocio. Los modelos se ajustan
  solo con referencias y no se modifican los datos ni resultados anteriores.

## Reproducir y auditar

Desde la raíz del proyecto:

```powershell
python desarrollo_puntos/4.2/analisis_sensibilidad.py
python -m unittest discover -s desarrollo_puntos/4.2 -p test_sensibilidad.py -v
python desarrollo_puntos/4.2/verificar_resultados.py
```

`configuracion.json` fija versiones, semilla, fuentes, hashes, parámetros y fórmulas.
`manifiesto_resultados.json` permite verificar cada archivo. Las tablas de detalle
comprimidas son CSV UTF-8 legibles con `pandas.read_csv(ruta, compression="gzip")`.
`informe_sensibilidad.py` genera nueve figuras en PNG, SVG y PDF para revisión y exportación.
La carpeta `figuras/` contiene artefactos regenerables y no se versiona; debe reconstruirse en un
entorno que tenga las dependencias fijadas en `configuracion.json`.
'''
    ((_PROJECT_ROOT / 'Data/gold/outputs/sensibilidad/INFORME_SENSIBILIDAD.txt')).write_text(body,encoding='utf-8')
    ((_PROJECT_ROOT / 'Data/gold/outputs/sensibilidad/README.txt')).write_text('''# 4.2 · Análisis de sensibilidad

La lectura principal está en [INFORME_SENSIBILIDAD.md](INFORME_SENSIBILIDAD.md).
El análisis se ejecutó sobre las cuatro fuentes locales y escribe todas sus salidas aquí.

| Archivo | Contenido |
|---|---|
| [cobertura_ventanas.csv](cobertura_ventanas.csv) | Elegibilidad y configuraciones no evaluables. |
| [tasas_alerta_reales.csv](tasas_alerta_reales.csv) | Alertas e IC descriptivos por ventana, cohorte y método. |
| [comparacion_ventanas_pareada.csv](comparacion_ventanas_pareada.csv) | Diferencias 24/48 frente a 36 sobre las mismas series y meses. |
| [parametros_por_serie.csv](parametros_por_serie.csv) | Períodos de referencia/vigilancia, límites, MAD y mediana para R12. |
| [deteccion_inyecciones.csv](deteccion_inyecciones.csv) | Detección t/t+1, ganancia e IC por tipo; señales nuevas respecto a base. |
| [resumen_horizonte_36.csv](resumen_horizonte_36.csv) | Resumen de horizonte por fuente/método con referencia 36. |
| [inyecciones_omitidas.csv](inyecciones_omitidas.csv) | Casos sin perturbación efectiva o sin otra medida comparable. |
| [combinaciones_framework.csv](combinaciones_framework.csv) | Interacción de cartas, percentil IF y factor R12. |
| [alertas_sistemicas_por_mes.csv](alertas_sistemicas_por_mes.csv) | Catálogo mensual de candidatos para cada X, sin confirmar origen regulatorio. |
| [efecto_regla_sistemica_reales.csv](efecto_regla_sistemica_reales.csv) | Tasa original y tasa retenida por X. |
| [efecto_regla_sistemica_inyecciones.csv](efecto_regla_sistemica_inyecciones.csv) | Detecciones retenidas/enmascaradas en errores individuales y colectivos. |
| [inventario_series.csv](inventario_series.csv) | Rachas y elegibilidad de todas las series candidatas. |
| [ejecuciones.csv](ejecuciones.csv) | Escenarios, modelos, tamaños, umbrales y tiempos. |
| [modelos_IF.csv](modelos_IF.csv) | Modelos separados por calendario, fechas de corte y percentiles de referencia. |
| [alertas_reales_detalle.csv.gz](alertas_reales_detalle.csv.gz) | Una fila por escenario/serie/mes, con las once banderas de señal. |
| [inyecciones_detalle.csv.gz](inyecciones_detalle.csv.gz) | Casos auditables y banderas por método en t, t+1 y nuevas respecto a base. |
| [configuracion.json](configuracion.json) | Protocolo, versiones y huellas de entradas. |
| [manifiesto_resultados.json](manifiesto_resultados.json) | Huellas de los archivos entregados. |
| [analisis_sensibilidad.py](analisis_sensibilidad.py), [informe_sensibilidad.py](informe_sensibilidad.py) | Ejecución y generación de informe/figuras. |
| [test_sensibilidad.py](test_sensibilidad.py) | Pruebas de continuidad, ausencia de fuga temporal, límites y bootstrap. |
| [verificar_resultados.py](verificar_resultados.py), [verificacion.json](verificacion.json) | Reconciliación del detalle, denominadores, hashes y pruebas automáticas. |

El script `informe_sensibilidad.py` genera nueve gráficos en `figuras/`, en PNG, SVG y PDF.
La carpeta no se versiona porque son artefactos regenerables; se debe ejecutar el script con las
dependencias registradas en `configuracion.json` para visualizarlos.
SSPD con referencia 48 es no evaluable; XM no recibe IC entre categorías.
Los resultados describen sensibilidad, sin aprobar umbrales ni clasificar automáticamente
una señal estadística como error o cambio regulatorio.

```powershell
python desarrollo_puntos/4.2/analisis_sensibilidad.py
```
''',encoding='utf-8')


if __name__=='__main__':generate()
