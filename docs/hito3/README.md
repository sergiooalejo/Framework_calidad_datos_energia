# Hito 3 · Punto 1 · Matriz OE1

El punto 1 queda desarrollado como especificación documental para EPM y CHEC. No se modificó el código del Hito 2.

Los tres archivos de la matriz incluyen además la **línea base medida** sobre los CSV conservados en `fuentes_datos/datos/`: resultado, estado y nota por control y fuente. La especificación no se modificó; solo se llenó el casillero de resultado que quedaba en `null`.

## Archivos

- [Matriz y fichas explicadas](matriz_oe1.md): lectura principal, ocho dimensiones, diez tipos de regla y diecinueve indicadores, con el resultado de cada ficha y la sección de línea base.
- [Matriz CSV](matriz_oe1.csv): 38 filas (19 controles × 2 fuentes), legible en Excel con UTF-8 y separador coma; incluye las columnas de resultado.
- [Especificación YAML](matriz_oe1.yaml): definiciones, fórmulas, parámetros, decisiones de medición y bloque `resultado` por fuente. Es documental; no es un motor de reglas ejecutado.
- [Plantilla de exactitud](plantilla_exactitud.csv): contraste de una muestra con publicaciones verificadas.
- [Plantilla de oportunidad](plantilla_oportunidad.csv): plazos, evidencia temporal e intervalos de disponibilidad.
- [Plantilla de catálogos](plantilla_catalogos.csv): dominios, equivalencias y relaciones con fundamento documental.
- [Script de medición](medir_matriz_oe1.py): calcula el resultado de cada control y lo escribe dentro de los tres archivos anteriores. Reejecutable e idempotente con `python docs/hito3/medir_matriz_oe1.py`; registra el SHA-256 de cada archivo medido.
- [Referencia externa de EXA01](referencia_exa01_chec.json): registros de CHEC en `td8k-vhq9` de Superservicios, con su consulta y fecha de descarga. Permite contrastar exactitud sin depender de una respuesta de la entidad, y hace el contraste reproducible sin red.

Las tres plantillas contienen solo cabeceras: están pendientes de diligenciar con evidencia real. No existen referencias o fechas de publicación inventadas.

## Estado de la medición

La especificación la elaboró el entregable anterior; esta entrega añade el resultado calculado de cada control. El `estado_medicion` de cada fila distingue tres situaciones:

| Estado | Qué significa |
|---|---|
| `medido` | La definición de la matriz se aplica sin supuestos añadidos. El valor no cambia salvo que cambien los datos. |
| `provisional` | Hay valor, pero depende de una decisión documental todavía abierta (catálogo canónico, dominio por concepto, conjunto de medidas requeridas, factor de R12, clave definitiva de CHEC). El valor puede cambiar cuando esa decisión se cierre. |
| `no_medible` | No hay numerador posible con la evidencia disponible. No es falta de definición, es falta de evidencia. |

Cobertura actual: **15 de los 19 controles** tienen valor en al menos una fuente, y **siete de las ocho dimensiones** están medidas. La única sin ninguna medición es **oportunidad**, porque ninguna de las dos fuentes publica la fecha real de disponibilidad por período.

Cada valor va acompañado de su numerador, su denominador y una nota que declara los supuestos aplicados. Las cifras se recalculan ejecutando el script; no se transcriben a mano.

## Qué cambia frente al plan anterior

La oportunidad pasa de excluida a obligatoria por instrucción del profesor. Se mantienen R01–R12 y se añaden INT01/INT02, EXA01, OPO01, MAP01, DEF01 y CART01 para completar la especificación conceptual. No se fuerza una asignación uno a uno entre doce reglas y diez tipos.

Las metas de conformidad del 100 % son propuestas del proyecto; los umbrales de tasas de alertas requieren calibración y no se fijan en cero. Deben validarse antes de declarar cumplimiento. El documento distingue cambios propuestos al código (especialmente R10/R11/R12) de su comportamiento actual.

## Pendientes para ejecutar y cerrar

1. Asignar nombres a los roles y validar los criterios/umbrales con el equipo y dirección.
2. Confirmar catálogos, unidades, semántica, clave candidata y adaptaciones R08/R09 para CHEC.
3. Completar la evidencia de exactitud y oportunidad. EXA01 ya tiene un contraste parcial en CHEC contra otro publicador; falta cubrir EPM, que no tiene traslape temporal con esa referencia, y falta por completo la evidencia de oportunidad en ambas fuentes. «No evaluable» no acredita el requisito de ocho dimensiones.
4. Generar scorecards; corresponde a las actividades posteriores. La línea base ya cubre 15 de los 19 controles, a la espera de las decisiones de los puntos 1 a 3.
5. Revisar dos propuestas que surgen de medir: cambiar la unidad de observación de R10 de fila a celda por columna, y declarar la política de fin de línea de los CSV para que sus hashes sean verificables.

La actividad cuenta con su entregable documental; la validación metodológica, implementación, medición y cierre del Hito 3 siguen pendientes. El plan detallado en Markdown y esta matriz contienen el alcance actualizado; las imágenes del plan son una representación anterior y no deben usarse para excluir oportunidad.
