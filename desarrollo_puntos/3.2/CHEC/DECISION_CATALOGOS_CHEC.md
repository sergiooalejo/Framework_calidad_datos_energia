# Análisis técnico de catálogos CHEC

## Perfil observado

Archivo analizado: `fuentes_datos/datos/Datos_seleccionados/CHEC/chec_c698-wqig.csv`.

- 40.609 filas y 24 columnas.
- 19 años y 12 meses; periodo observado 2008–2026.
- No hay nulos en las columnas de periodo ni en los identificadores categóricos principales.
- Hay 11 nulos en cada uno de estos componentes: distribución, comercialización, pérdidas,
  restricciones y subcon.
- `costounitariotarifa_restricciones` contiene valores negativos; no deben eliminarse sin confirmar
  su significado económico.

## Catálogos observados

| Campo | Valores distintos | Interpretación operativa provisional |
|---|---:|---|
| comercializador_codigo | 1 | Código del comercializador; conservar como texto. |
| mercado_codigo | 2 | Código de mercado; debe corresponder con `mercado_nombre`. |
| costounitariotarifa_tipomed | 3 | Código de modalidad de medición; significado formal pendiente. |
| nivel_tension_codigo | 4 | Nivel de tensión; es categoría, no voltaje medido. |
| modalidadcobro_propiedad | 4 | Etiquetas de modalidad/propiedad; requiere catálogo CHEC. |
| claseservicio_codigo | 23 | Código de clase de servicio. |
| claseservicio_descri | 29 | Descripción; hay más descripciones que códigos, por lo que debe revisarse la correspondencia. |
| claseservicio_estrato | 7 | Estrato o categoría no aplicable en algunos servicios. |
| costounitariotarifa_rangoconsumo | 2 | Tramo tarifario; no es consumo observado en kWh. |
| costounitariotarifa_tipomercado | 1 | Código de tipo de mercado; significado pendiente. |

## Clave candidata

La combinación provisional de periodo y categorías principales produce 37.252 claves distintas
para 40.609 filas: quedan 3.357 filas repetidas y la multiplicidad máxima es cuatro. Por tanto,
no se puede declarar unicidad todavía.

La clave debe confirmarse con CHEC o mediante el metadato oficial. Mientras tanto, se conserva la
clave candidata del diccionario y se reporta R05 como provisional. Las filas repetidas pueden ser
versiones de componentes o registros semánticamente distintos; no se deben eliminar por posición.

## Decisiones que requieren aprobación

1. Definir formalmente los códigos de `tipomed`, `tipomercado` y `rangoconsumo`.
2. Confirmar la relación código-descripción de clase de servicio.
3. Confirmar si los valores negativos de restricciones y subcon son válidos por concepto.
4. Confirmar la unidad monetaria y la relación entre CU, CU real, subcon y valor de tarifa.
5. Confirmar la clave completa y el tratamiento de multiplicidades.
6. Definir quién mantiene el catálogo y cómo se versiona.

Este documento es evidencia técnica preparatoria; no convierte las interpretaciones provisionales en
catálogos oficiales.
