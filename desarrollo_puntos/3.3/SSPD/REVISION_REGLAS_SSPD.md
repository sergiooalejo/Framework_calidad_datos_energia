# SSPD: cierre de controles del Hito 3

Fuente: `ebby-cjha`, información comercial de energía en ZNI. La copia conserva el
censo mensual de 91 empresas y el detalle completo de una empresa.

## Resultados incorporados

- `DEF01`: 19/19 variables críticas documentadas en
  `fuentes_datos/catalogos/SSPD/sspd_definiciones_def01.yaml`. Es una definición
  metodológica porque el portal no publica descripciones completas.
- `MAP01`: 3/3 grupos de variantes normalizados internamente, sin afirmar que exista
  aprobación oficial de la SSPD.
- `OPO01`: proxy de cobertura 59/65 períodos del alcance enero de 2017 a mayo de 2022
  (90,77 %). Los seis primeros meses de 2017 no están en la fuente.
- `CART01`: 361 series con al menos 49 períodos, 4.332 cambios vigilados y 143 señales
  preliminares. Las señales no se clasifican automáticamente como errores.

## Limitaciones

`EXA01` permanece sin medir directamente porque no se encontró una segunda fuente que
reporte los mismos consumos de las 91 empresas ZNI con la misma granularidad. La exactitud
debe presentarse como limitación de evidencia, no como 100 % inferido del propio archivo.
R08 y R09 no aplican al esquema tarifario de esta fuente. Las unidades de consumo y
facturación son hipótesis operativas hasta contar con un diccionario formal del publicador.
