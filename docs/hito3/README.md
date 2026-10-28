# Hito 3 · Punto 1 · Matriz OE1

El punto 1 queda desarrollado como especificación documental para EPM y CHEC. No se modificó el código del Hito 2 ni se presentan resultados empíricos nuevos.

## Archivos

- [Matriz y fichas explicadas](matriz_oe1.md): lectura principal, ocho dimensiones, diez tipos de regla y diecinueve indicadores.
- [Matriz CSV](matriz_oe1.csv): 38 filas (19 controles × 2 fuentes), legible en Excel con UTF-8 y separador coma.
- [Especificación YAML](matriz_oe1.yaml): definiciones, fórmulas, parámetros y decisiones de medición. Es documental; no es un motor de reglas ejecutado.
- [Plantilla de exactitud](plantilla_exactitud.csv): contraste de una muestra con publicaciones verificadas.
- [Plantilla de oportunidad](plantilla_oportunidad.csv): plazos, evidencia temporal e intervalos de disponibilidad.
- [Plantilla de catálogos](plantilla_catalogos.csv): dominios, equivalencias y relaciones con fundamento documental.

Las tres plantillas contienen solo cabeceras: están pendientes de diligenciar con evidencia real. No existen referencias o fechas de publicación inventadas.

## Qué cambia frente al plan anterior

La oportunidad pasa de excluida a obligatoria por instrucción del profesor. Se mantienen R01–R12 y se añaden INT01/INT02, EXA01, OPO01, MAP01, DEF01 y CART01 para completar la especificación conceptual. No se fuerza una asignación uno a uno entre doce reglas y diez tipos.

Las metas de conformidad del 100 % son propuestas del proyecto; los umbrales de tasas de alertas requieren calibración y no se fijan en cero. Deben validarse antes de declarar cumplimiento. El documento distingue cambios propuestos al código (especialmente R10/R11/R12) de su comportamiento actual.

## Pendientes para ejecutar y cerrar

1. Asignar nombres a los roles y validar los criterios/umbrales con el equipo y dirección.
2. Confirmar catálogos, unidades, semántica, clave candidata y adaptaciones R08/R09 para CHEC.
3. Obtener evidencia de exactitud y oportunidad en ambas fuentes; no evaluable no acredita el requisito de ocho dimensiones.
4. Implementar indicadores, medir cobertura y generar scorecards; corresponde a las actividades posteriores.

La actividad cuenta con su entregable documental; la validación metodológica, implementación, medición y cierre del Hito 3 siguen pendientes. El plan detallado en Markdown y esta matriz contienen el alcance actualizado; las imágenes del plan son una representación anterior y no deben usarse para excluir oportunidad.
