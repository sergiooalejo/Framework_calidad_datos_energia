# Decisión de fuentes principales del proyecto

## Decisión

Para el desarrollo de los Hitos 3 a 6 se trabajará con cuatro fuentes eléctricas:

1. EPM — `sfcd-b3ey`.
2. CHEC — `c698-wqig`.
3. Superservicios — Información comercial residencial y no residencial ZNI, `ebby-cjha`.
4. XM/SIMEM — Demanda real histórica, `c1b851`.

La decisión se toma porque las cuatro permiten evaluar el framework en registros energéticos con estructuras distintas: tarifas, costos unitarios, facturación/consumo y demanda horaria agregada.

## Justificación

| Fuente | Función en el proyecto |
|---|---|
| EPM | Mantiene la continuidad con el Hito 2 y permite reproducir el caso tarifario original. |
| CHEC | Comprueba la transferencia del framework a otro publicador tarifario con historia extensa. |
| Superservicios ZNI | Aporta consumo observado y 59 períodos mensuales para series de operadores ZNI. |
| XM/SIMEM | Aporta demanda horaria y 61 meses derivados con trazabilidad de versiones. |

## Alcance metodológico

Las doce reglas originales se mantienen, pero no todas tienen el mismo significado en las cuatro fuentes. En SSPD ZNI y XM deben utilizarse adaptadores documentados por dominio. En particular, R08 y R09 no se pueden copiar literalmente desde EPM porque ZNI y demanda XM no son tablas de tarifas con propiedad y modalidad equivalentes.

La matriz OE1 conserva 19 controles por fuente. Los controles de XM se incorporan como `pendiente_implementacion` hasta que se ejecute su adaptador y se verifique la política de versiones.

## Fuentes que no forman parte del conjunto principal

- `bnkp-xdb7`: fuente no residencial de Superservicios; tiene consumo y tarifa aplicada, pero solo 12 meses y una caída importante de volumen.
- `supers_icnr-l4iw`: extracción relacionada con información comercial; no se cuenta como dataset independiente y sus identificadores presentan notación científica.
- Anexos eléctricos CREG: sirven como referencia regulatoria, pero son paneles anuales o tablas de indicadores y escenarios, no microdatos mensuales suficientes para cartas.
- `ek3f-5wn4`: fuente de gas natural excluida porque el alcance del proyecto es únicamente electricidad.

## Condición de cierre

La selección no significa que las ocho dimensiones ya estén demostradas. Para cerrar el Hito 3 se deben ejecutar los 19 controles en las cuatro fuentes, completar la evidencia de exactitud y oportunidad y conservar hashes, versión, política de transformación y fecha de cada ejecución.
