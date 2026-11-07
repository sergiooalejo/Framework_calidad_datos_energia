# Evidencia de exactitud y oportunidad — preparación

Este documento deja preparado el procedimiento y separa la evidencia disponible de la evidencia
que todavía necesita aprobación o contraste externo. No convierte una referencia en una medición
de exactitud si aún no existe una comparación fila a fila.

## Exactitud (EXA01)

### Diseño aprobado como propuesta

- Muestra: 30 registros por fuente, estratificados por periodo y categoría.
- Campos: periodo, identificadores de categoría y componentes monetarios disponibles.
- Comparación: igualdad después de normalizar unidad y redondeo documentado.
- Resultado: coincidencias / comparaciones válidas × 100.
- Evidencia: URL, archivo de referencia, SHA-256 y fecha de consulta.

La muestra de 30 registros por fuente es exploratoria y no sustituye una auditoría estadística de
la población completa.

### Evidencia actualmente disponible

CHEC tiene una referencia externa preparada en
`desarrollo_puntos/3.1/referencia_exa01_chec.json` (108 registros de Superservicios, consulta
descargada el 2026-10-28). El archivo permite seleccionar pares comparables, pero todavía no
contiene una tabla de coincidencias fila a fila; por eso EXA01 sigue provisional.

Para EPM, SSPD y XM no existe todavía una referencia equivalente aprobada. No se inventan
coincidencias ni porcentajes.

### Plantilla

La captura debe diligenciarse en [plantilla_exactitud.csv](plantilla_exactitud.csv). Cada fila debe
conservar el `snapshot_sha256` del dataset evaluado y el `sha256_referencia` del contraste.

## Oportunidad (OPO01)

### Fórmula propuesta

`retraso_días = fecha_disponible - fecha_límite`.

Si no existe fecha límite publicada, se registra la fecha de publicación observada y se clasifica
como `provisional_proxy`; no se declara cumplimiento.

### Evidencia actualmente disponible

XM tiene fechas declaradas de publicación para 60 de 61 versiones mensuales del piloto. Falta
julio de 2021 y aún debe aprobarse el plazo esperado; por tanto, XM tiene evidencia parcial, no
cierre de oportunidad.

EPM, CHEC y SSPD conservan fecha de descarga y cobertura, pero no un plazo de publicación oficial
por periodo. Sus resultados de oportunidad deben permanecer como proxy o pendiente.

### Plantilla

La captura debe diligenciarse en [plantilla_oportunidad.csv](plantilla_oportunidad.csv), incluyendo
la URL o archivo que demuestra cada fecha. No usar la fecha de descarga como fecha de publicación.

## Decisiones que debe aprobar el director

1. Aceptar la muestra exploratoria de 30 registros por fuente o cambiar su tamaño.
2. Aprobar la referencia de Superservicios para contrastar CHEC.
3. Definir tolerancia de redondeo y equivalencia de unidades.
4. Aprobar el proxy de oportunidad cuando no exista un plazo publicado.
5. Aceptar que los resultados sin contraste siguen como `provisional` o `provisional_proxy`.
