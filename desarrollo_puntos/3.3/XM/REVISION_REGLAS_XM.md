# Revisión metodológica de reglas para XM/SIMEM

## Propósito

El script y la salida de cartas citados en este documento están en
[3.5/XM](../../3.5/README.md). La matriz se conserva en [3.1](../../3.1/matriz_oe1.md).

Este documento realiza el punto 1 del siguiente paso del Hito 3: revisar la matriz OE1 para XM y recordar el significado de cada regla. XM contiene demanda horaria y versiones de publicación, no tarifas. Por eso una regla tarifaria no se copia literalmente: se adapta por propósito y se deja evidencia de la decisión.

Estados utilizados:

- **Directa:** puede medirse con el contrato actual de XM.
- **Adaptada:** conserva el propósito de la regla, pero cambia la unidad o relación evaluada.
- **No medible:** necesita una fuente externa o una decisión todavía inexistente.
- **No aplica:** el concepto original no existe en XM.

## Reglas base R01–R12

| Regla | Qué controla | Aplicación en XM | Estado actual |
|---|---|---|---|
| **R01** | Período informado | Verifica que `periodo` exista en la serie mensual derivada y que `FechaHora` exista en el crudo. | Directa; 61/61 meses. |
| **R02** | Período válido | Comprueba formato `AAAA-MM`, fechas válidas y horas que puedan convertirse a fecha-hora. | Directa; debe conservar la zona horaria definida. |
| **R03** | Formato numérico | Comprueba que `Valor` y `demanda_kwh` sean números finitos. | Directa; medida preliminar 100 %. |
| **R04** | Duplicados exactos | Busca filas idénticas en el archivo horario o mensual, sin usar la posición de la fila como identificador. | Directa. |
| **R05** | Multiplicidad de clave | Usa la clave `agente + mercado + sistema + versión + FechaHora` para el crudo y `agente + mercado + sistema + periodo` para el agregado. | Directa, con versiones separadas. |
| **R06** | Representación canónica | Revisa escritura consistente de agente, mercado, sistema, versión, unidad y duración. | Adaptada; falta catálogo oficial externo. |
| **R07** | Signo y dominio | Verifica que la demanda sea finita y no negativa, y que la duración y unidad pertenezcan al dominio autorizado. | Adaptada; confirmar formalmente el dominio de demanda. |
| **R08** | Coherencia de tarifas por propiedad | En EPM/CHEC compara tarifas según propiedad. En XM no existe propiedad tarifaria. Se reemplaza por coherencia entre agente, mercado y sistema dentro de una misma serie. | Adaptada; no es una prueba de orden tarifario. |
| **R09** | Aplicabilidad según nivel y modalidad | En EPM/CHEC revisa qué componentes tarifarios aplican. En XM comprueba la compatibilidad `CodigoVariable–UnidadMedida–CodigoDuracion–Version`. | Adaptada. |
| **R10** | Medidas requeridas presentes | Comprueba que cada mes tenga demanda, versión, horas únicas y horas esperadas. | Directa; medida preliminar 100 %. |
| **R11** | Posible serial de fecha en importes | Busca números que parecen fechas de Excel dentro de importes. XM no tiene importes tarifarios. | No aplica a XM. |
| **R12** | Magnitud atípica | Compara cambios de demanda frente a la mediana de una ventana de referencia. | Adaptada; factor 10 provisional y requiere sensibilidad. |

## Controles complementarios

| Control | Qué controla | Aplicación en XM | Estado actual |
|---|---|---|---|
| **INT01** | Integridad estructural | Verifica las nueve columnas del contrato crudo y las columnas esperadas del agregado mensual. | Directa; contrato crudo 9/9. |
| **INT02** | Integridad referencial | Contrasta códigos de agente, mercado y sistema contra catálogos autorizados y versionados. | No medible; faltan catálogos externos. |
| **EXA01** | Exactitud documental | Contrasta una muestra de `Valor` o `demanda_kwh` con una referencia horaria/mensual equivalente. | No medible; falta referencia independiente. |
| **OPO01** | Oportunidad | Compara disponibilidad real de cada publicación con un plazo esperado documentado. | No medible; hay fechas declaradas, pero falta plazo y vínculo completo. |
| **MAP01** | Equivalencia de etiquetas | Documenta transformaciones como códigos, unidades o versiones y demuestra que conservan el significado. | No medible; no se han aplicado mapeos documentados. |
| **DEF01** | Definición semántica | Verifica que las variables críticas tengan significado, unidad y regla de uso aprobados. | No medible; falta aprobación documental completa. |
| **CART01** | Cartas I-MR | Aplica cartas sobre cambios logarítmicos de `demanda_kwh` después de separar referencia y vigilancia. | Provisional; se calcularon 12 meses de vigilancia, pero faltan congelar límites, cuarentena y sensibilidad. |

## Decisiones metodológicas recomendadas

1. Mantener R08 y R09 en la matriz porque el profesor exige evaluar las ocho dimensiones, pero identificarlas como adaptaciones de dominio y no como equivalentes literales de las reglas tarifarias.
2. No convertir R11 en una aprobación automática: en XM queda `no_aplica` porque no hay importes, y esa diferencia se reporta como una característica del esquema.
3. Mantener R12 y CART01 como advertencias estadísticas. Una alerta no demuestra que el valor sea incorrecto.
4. Usar 36 cambios de referencia y 12 de vigilancia para la comparación común. XM tiene 60 cambios disponibles; se conservan los restantes para sensibilidad.
5. No declarar cerradas exactitud ni oportunidad hasta obtener, respectivamente, una referencia equivalente y un plazo de publicación documentado.

## Actualización del adaptador

El catálogo `fuentes_datos/catalogos/XM/xm_definiciones_def01.yaml` documenta las
variables crudas y derivadas del piloto. Se incorporó un proxy de oportunidad con las
fechas declaradas de publicación (60/61 meses), mapeos internos para los códigos fijos
del piloto y una evaluación de integridad referencial interna. Estas decisiones no
equivalen a un catálogo completo ni a una fecha límite oficial de XM.
La carta I-MR queda materializada en `cartas_log_xm.csv` y se reproduce con
`cartas_log_xm.py`: 61 meses, 36 cambios de referencia, 12 de vigilancia y 0 señales
con los límites preliminares actuales.

## Resultado del punto 1

La matriz de XM es metodológicamente utilizable como adaptador de demanda: 7 controles
tienen medición directa, 6 son provisionales, 3 son provisionales internos, 1 es un proxy,
1 no aplica por ausencia de importes tarifarios y EXA01 requiere evidencia externa. Esto
permite continuar con la formalización de cartas del Hito 3 sin afirmar que la exactitud
documental esté cerrada.
