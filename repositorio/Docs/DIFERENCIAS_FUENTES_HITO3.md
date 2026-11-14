# Diferencias entre fuentes · Hito 3 vigente

Las cifras se regeneran en FICHAS_FUENTES_HITO3.md. Este documento reemplaza la
interpretación de las cartas preliminares para el Hito 3 corregido; los informes
históricos permanecen identificados como antecedentes.

| Fuente | Unidad y población | Reglas específicas / umbrales | Dimensiones y evidencia pendiente |
|---|---|---|---|
| EPM sfcd-b3ey | Tarifas y componentes; categoría tarifaria + mes + medida | R08 orden entre propiedades; R09 aplicabilidad por nivel. Normalización con catálogo interno. I-MR 36+12, 2,66/3,267, R12 factor 10 Advertencia | Exactitud solo muestra contrastada; oportunidad sin plazo/disponibilidad; catálogos y unidades requieren confirmación |
| CHEC c698-wqig | CU/tarifa por mercado, modalidad, nivel, clase y rango | No imponer relación EPM de propiedad. Componentes con signo/ajustes requieren dominio. Conflictos no se promedian. Mismas constantes I-MR; límites estimados por serie | Exactitud parcial por componentes; catálogos referenciales y oportunidad pendientes |
| SSPD ZNI ebby-cjha | Agregado mensual de facturación/consumo por seis identificadores | R08/R09 de EPM no aplican literalmente. No confundir importes con consumo. Cartas solo sobre medidas positivas en rachas aptas | Sin referencia independiente de exactitud; oportunidad histórica pendiente; semántica delimitada |
| XM c1b851 | Demanda mensual del piloto EPMC/EPMD/STR02, kWh | Política de versión y horas según diccionario; demanda no es tarifa. Una categoría: bootstrap descriptivo sin IC inferencial | Exactitud pendiente; fecha declarada de versión no basta sin plazo para oportunidad |
| SSPD original vfjy-6fka | Subsidios, contribuciones y FOES, pesos contables; empresa/mercado/estrato-sector/mes | R01–R11 adaptadas en matriz complementaria; R08/R09 no aplican. Catálogo de sector pendiente. Ocho períodos: cartas/IF no aplican al protocolo 36+12 | Oportunidad y exactitud no medibles con la evidencia actual; integridad externa pendiente |

Los límites numéricos no se copian entre fuentes: se estiman con su referencia.
Un estado no aplica describe ausencia del concepto o del alcance temporal previsto;
no medible señala que falta evidencia para un concepto pertinente. Los promedios
de indicadores de poblaciones o sentidos distintos no se interpretan como calidad global.

Se mantiene la cobertura temporal como diagnóstico del perfil, separada de OPO01.
No se convierte una publicación descargada hoy en evidencia de que se publicó a
tiempo en el pasado. El consumidor y la fecha límite deben constar en cada evidencia.

El conjunto vfjy-6fka se comprobó directamente por API: tiene 5.396 registros,
16 columnas y ocho períodos. Su esquema no contiene Rango de Consumo. Por ello,
las 2.143 ausencias citadas en el plan no se replican artificialmente en esta fuente.
Los metadatos conservados explican sus campos como registros contables en pesos.
