# Piloto de demanda real XM/SIMEM

Descarga y verificación: 4 de noviembre de 2026. Es un candidato en revisión, no una incorporación automática a la matriz medida.

## Alcance de los archivos

- `xm_demanda_epmc_epmd_str02_202001_202501.csv`: 119.928 registros originales devueltos por la consulta filtrada al agente EPMC, mercado EPMD y sistema STR02, enero de 2020 a enero de 2025. No es el mercado completo ni una muestra aleatoria del mercado. Incluye múltiples versiones por hora.
- `xm_versiones_mensuales_202001_202501.csv`: 161 registros del calendario mensual de versiones de liquidación. Conserva las fechas declaradas de publicación; no son fechas fabricadas por el cliente.
- `xm_demanda_mensual_piloto.csv`: 61 observaciones mensuales derivadas, una por mes. Para cada mes se elige la TX numérica más alta presente en el conjunto de demanda, se excluyen TXF/TXR y se suman sus valores horarios. No se suman versiones entre sí. Esa selección no se presenta como la versión final oficial.

La serie mensual deriva de **44.592 observaciones horarias únicas**. Los 61 meses contienen todas sus horas calendario y tienen suma de demanda positiva. No se interpolaron huecos ni se rellenaron valores faltantes. Esto habilita, en longitud y continuidad, el escenario de 48 cambios de referencia y 12 de vigilancia; todavía falta analizar estabilidad y estacionalidad.

## Diferencia entre dos políticas de versión

Exigir la versión marcada `esMaximaVersion=1` en el calendario deja 53 meses coincidentes y una racha máxima de 20 meses: no cumple el protocolo mensual. Hay ocho meses donde el conjunto de demanda no ofrece la versión final marcada por ese calendario.

La política alternativa de mayor TX numérica disponible permite 61 meses completos, pero se debe justificar y congelar antes de comparar técnicas. Permite una evaluación retrospectiva sobre el conjunto publicado, no certificar la última liquidación final del mercado.

Se vincula fecha de publicación declarada para 60 de las 61 versiones mensuales seleccionadas. Falta junio de 2021. Por ello **oportunidad no está cerrada**: falta ese vínculo y definir plazos y alcance de cada versión. No se convierte la ausencia de evidencia en retraso ni cumplimiento. Tampoco se interpreta la fecha de una revisión como primera publicación.

## Reproducibilidad y pendientes

Los parámetros exactos, filtros y hashes están en `desarrollo_puntos/3.2/perfiles/xm_piloto_cobertura.json`. La consulta usa el conjunto histórico `c1b851`, retirado de actualización, con corte declarado de junio de 2026.

Faltan el contraste de exactitud con referencia equivalente, maestras, adaptación de reglas por dominio, evaluación de oportunidad y el experimento de cartas. No aplicar las reglas de propiedad de EPM literalmente a demanda.
