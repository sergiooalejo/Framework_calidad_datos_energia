# Verificación técnica del Hito 6 · 17 de noviembre de 2026

Se actualizó la selección manual al protocolo H4-v2-CV-temporal sin recalcular los
experimentos H3/H4 ni alterar las muestras o revisiones históricas.

## Muestra vigente

- Entrada: puntajes reales H4 y calibración, con su manifiesto e integridad comprobados.
- Escenario: EPM, referencia 36, horizonte t y tasa objetivo de calibración 5 %.
- Población: 118 observaciones únicas con al menos una alerta; sorteo de 50, semilla 42.
- Resultado: 50 observaciones distintas; todas con R12 y dos también con Z robusto.
  Se conservan las banderas de los seis métodos; esta selección no permite afirmar
  validación empírica de IMR, IF, LOF o KNN ni generalizar a otras fuentes.
- Salidas: `Data/gold/outputs/hito6/muestra_alertas_h4_v2_epm_50.csv` y su
  `.manifiesto.json`, con hashes, identidad y procedencia.
- Las 50 clasificaciones permanecen pendientes; no se confirman errores automáticamente.

## Comprobaciones

En una copia temporal con los datos y el código del proyecto se ejecutó
`python -B -X utf8 pipeline.py pruebas`: **74 pruebas exitosas** en nueve grupos
(11 H6, 3 H5, 9 H4, 12 H3, 9 sensibilidad, 12 métricas, 10 regla sistémica,
3 compatibilidad y 5 correcciones). Las regresiones H6 cubren integridad,
protocolo, umbrales y banderas, duplicados, cuotas insuficientes, reproducibilidad
ante reordenamiento y conservación de muestras/manifiestos revisados.
La generación sobre los datos H4 reales también finalizó correctamente.

La muestra histórica `muestra_alertas_50.csv` sigue disponible como antecedente.
La revisión externa, el análisis de precisión y la aprobación metodológica siguen
pendientes según el plan y el anexo H6. No se recalcularon ni alteraron salidas H4.
