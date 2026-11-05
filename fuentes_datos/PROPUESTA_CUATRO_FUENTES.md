# Cuatro fuentes para validar el proyecto: propuesta y requisitos de aceptación

Revisión del 4 de noviembre de 2026. El requisito es disponer de al menos cuatro datasets útiles para el estudio, con evaluación de las ocho dimensiones en cada uno. Las doce reglas del proyecto deben revisarse por aplicabilidad real; no se cambian silenciosamente sus significados para completar una tabla.

**Prioridad y alcance confirmados:** buscar primero publicaciones directas de CREG y mantener exclusivamente electricidad. La [revisión CREG](REVISION_CREG_ELECTRICIDAD.md) encontró bases eléctricas anuales y cuadros de escenarios, que no superan los criterios temporales del protocolo. Gas queda excluido. La siguiente propuesta se conserva mientras no se verifique una candidata eléctrica de CREG adecuada.

## Selección propuesta para el piloto

| Fuente | Aporte | Evidencia disponible | Estado |
|---|---|---|---|
| EPM `sfcd-b3ey` | Caso tarifario inicial y comparación con resultados del Hito 2 | 3.623 filas; 61 meses globales; 83 series con al menos 49 meses según revisión previa | Conservar; excepción de tamaño aceptada. Falta evidencia de oportunidad y completar exactitud |
| CHEC `c698-wqig` | Segundo publicador tarifario, componentes y categorías | 40.609 filas; 180 grupos con al menos 61 meses positivos y únicos por mes en CU/tarifa | Conservar; falta cerrar catálogos, exactitud y oportunidad |
| Superservicios `ebby-cjha` | Consumo/facturación de operadores ZNI | 11.905.557 filas en origen; copia mensual de 15.075 filas y censo de 91.840 filas de una empresa; 59 meses globales | Candidato temporalmente útil; exige adaptar reglas de dominio y completar evidencia externa |
| XM/SIMEM `c1b851` | Demanda eléctrica del SIN y versiones de liquidación | Piloto descargado: 119.928 registros para un grupo fijo; serie derivada de 61 meses positivos con todas sus horas | Cuarto candidato con longitud comprobada bajo política de versión explícita; faltan adaptación, exactitud y cierre de oportunidad |

Estas cuatro son **datasets diferentes, de cuatro publicadores o sistemas de publicación**, no cuatro instituciones regulatorias independientes. Los dos CSV agregado/detalle de `ebby-cjha` son representaciones de una misma fuente y no cuentan como dos fuentes. Los dos cortes consultados de XM tampoco cuentan como fuentes diferentes.

Enlaces:

- EPM: https://www.datos.gov.co/d/sfcd-b3ey
- CHEC: https://www.datos.gov.co/d/c698-wqig
- Superservicios: https://www.datos.gov.co/d/ebby-cjha
- XM: https://www.simem.co/ ; API/documentación: https://github.com/EquipoAnaliticaXM/API_XM . Detalle de consultas y limitaciones en `desarrollo_puntos/3.2/Evaluacion_fuente_alternativa_XM.md`.

## Verificación adicional de la fuente ZNI

Se recalculó cobertura sobre la copia mensual local, agrupando por empresa y estrato/sector y sumando `consumo_basico_sum` entre las demás categorías:

- 207 grupos distintos.
- **120 grupos con presencia durante al menos 49 meses consecutivos.**
- **117 grupos con suma de consumo básico positiva durante al menos 49 meses consecutivos.**
- Máxima racha positiva: 59 meses.

La nota de incorporación anterior menciona 136 series con al menos 49 meses. Ese conteo no se reproduce con este criterio de consecutividad; no debe usarse como cifra validada del protocolo sin reconciliar definiciones. La presencia temporal no demuestra composición estable, cobertura completa ni meses individuales de cada usuario. El detalle está en `desarrollo_puntos/3.2/perfiles/sspd_verificacion_cobertura_seleccion.json`.

Con 36 cambios de referencia y 12 de vigilancia se requieren 49 observaciones. Una serie completa de 59 observaciones ofrece 58 cambios: 36 de referencia y 22 de vigilancia, no 23. Si se requieren 48 cambios de referencia y 12 de vigilancia, hacen falta 61 observaciones; la fuente ZNI no cumple ese escenario.

## Fuentes que no cuentan como cuarto caso completo para cartas mensuales

`bnkp-xdb7` y el CSV extraído `supers_icnr-l4iw.csv` tienen estructura no residencial y 12 meses de reporte. El archivo extraído además representa identificadores en notación científica. Se conservan como evidencia de facturación en revisión; no solucionan el cuarto caso completo bajo el protocolo temporal actual. No se suman como fuentes independientes solo por tener nombres de archivo distintos.

No se eliminó ni se alteró la cuarta fuente incorporada por el equipo ni sus resultados de medición. Esta propuesta señala por qué esa selección anterior no acredita cartas en las cuatro fuentes.

## Condiciones de aceptación antes de afirmar que sirven para todo el proyecto

1. **Historia:** cada fuente debe aportar un conjunto de series homogéneas con meses consecutivos suficientes y datos positivos cuando se utilicen cambios logarítmicos. No confundir número de filas, antigüedad global y longitud por grupo.
2. **Exactitud:** referencia documental verificable y muestra con categorías, unidades, período y versión equivalentes. No sustituir contraste por un detector de valores atípicos.
3. **Oportunidad:** fecha real de disponibilidad y plazo esperado documentado para un alcance explícito. No usar la última carga global o la fecha de factura como sustitutos automáticos.
4. **Reglas:** en ZNI y XM no existen todos los ejes tarifarios de R08/R09 de EPM. Si se permite transferencia mediante adaptadores, definir controles equivalentes por propósito y justificar cada cambio. Si se exigen literalmente las doce reglas tarifarias sin cambios en cada dataset, **esta pareja adicional no cumple** y se necesitan otras dos bases tarifarias.
5. **Integridad:** catálogos autorizados y vigentes por dominio; la ausencia de una columna nombre no elimina la dimensión. Puede contrastarse un código con una maestra externa adecuada.
6. **Validación del framework:** misma política de partición temporal, comparación con línea base, errores conocidos/inyección, precisión, recall, F1, intervalos, costo y reproducibilidad. Las unidades de evaluación y reglas pueden diferir por dominio sin mezclar resultados no comparables.

Las ocho dimensiones siguen siendo obligatorias. Un resultado de calidad bajo es admisible si se puede medir; una dimensión pendiente de evidencia no equivale a un resultado bajo medido ni cumple el requisito.

## Trabajo para concretar el cuarto caso

- Se descargó un subconjunto filtrado al grupo EPMC/EPMD/STR02, enero de 2020 a enero de 2025, con todas las versiones disponibles. Se conserva en `datos/Datos_en_revision/XM_piloto/`.
- Se comprobaron 61 meses completos y positivos al seleccionar por mes la TX numérica más alta disponible y sumar horas únicas: 44.592 horas en total. Esta política debe justificarse; no equivale a última versión oficial. Exigir la versión final marcada en el calendario deja solo 53 meses coincidentes y una racha máxima de 20, que no sirve para este protocolo.
- Se vincularon fechas de publicación declaradas de 60 de 61 versiones seleccionadas. Falta junio de 2021 y definir los plazos de cada versión; oportunidad no se declara completa. No se suman revisiones como energía adicional.
- Obtener maestras y un contraste oficial de valores; definir las adaptaciones R08/R09 y el uso de demanda frente a tarifa.
- Completar las evidencias faltantes en EPM, CHEC y ZNI en paralelo al piloto de XM.

**Estado final de esta revisión:** hay una propuesta concreta de cuatro casos con datos locales y longitud temporal utilizable, en XM bajo una política alternativa de versión explícita. Todavía no hay cuatro fuentes validadas para todas las condiciones. No se modifica el catálogo definitivo ni se afirma que el profesor haya aprobado las adaptaciones.
