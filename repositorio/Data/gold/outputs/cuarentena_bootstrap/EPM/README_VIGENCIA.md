# Cuarentena vigente del Hito 3

La cuarentena por **celda** utilizada por las cartas corregidas está en
`Data/gold/outputs/hito3/cuarentena_celdas_epm.csv`. Sus R12 son Advertencia y
no equivalen a errores confirmados. El comando `pipeline.py ejecutar cuarentena`
la regenera sin modificar los valores originales.

`cuarentena_registros.csv` de esta carpeta se conserva con su hash anterior
porque es entrada versionada de los experimentos históricos 4.2–4.4. No es la
cuarentena vigente del Hito 3. Esos experimentos no se declaran reevaluados con
las nuevas exclusiones. Los hallazgos históricos con R12 reclasificada están en
`Data/gold/outputs/hito3/hallazgos_epm_h2_reclasificados.csv`.
