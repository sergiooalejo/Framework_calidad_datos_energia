# Salidas de la ejecución del Hito 2

Archivos que produce `codigo/codigo_hasta_hito2.py` al correr de principio a fin. Se
versionan porque el plan de hitos los nombra como **insumo** de los hitos 3 y 4, y sin
ellos esas actividades no se pueden iniciar.

## Procedencia de esta ejecución

| | |
|---|---|
| Fecha de ejecución | 27 de octubre de 2026 |
| Entrada | Histórico de tarifas de EPM, conjunto `sfcd-b3ey` |
| Descarga | `https://www.datos.gov.co/api/views/sfcd-b3ey/rows.csv?accessType=DOWNLOAD`, 27-10-2026 23:12:43 UTC |
| SHA-256 de la entrada | `8d792b49c1f15ded30183d1488199c5230b63e856be53723d65b665ca2b797e8` |
| Filas × columnas | 3.623 × 12 |
| Entorno | Python 3.12.10 · pandas 2.3.3 · scikit-learn 1.9.1 · statsmodels 0.15.0 |

El mismo SHA-256 queda registrado dentro de `00_resumen.json`, que lo calcula el propio
código.

## Verificación

La ejecución reproduce **las trece cifras** de la tabla de verificación de
`docs/revision_hito2.md`, sin ninguna diferencia:

| Cifra | Valor |
|---|---|
| Filas y columnas | 3.623 × 12 |
| Variantes de etiqueta / filas afectadas | 11 / 445 |
| Duplicados exactos adicionales | 10 |
| Series posibles / con ≥49 meses / limpias | 202 / 83 / 77 |
| Pruebas inyectadas | 8.282 |
| Detección: reglas / cartas / IF / reglas+cartas | 73 / 80 / 80 / 88 % |
| Alertas en meses limpios: cartas / IF | 11,4 / 12,0 % |
| Series con alerta en feb-2020 | 51 de 83 |
| IC 95 % de la diferencia IF − cartas | −1,4 a +2,3 puntos |

Esto constituye el **primer dato de reproducibilidad entre ambientes** que pide el Hito 6:
el Hito 2 se desarrolló en Colab y estas salidas provienen de una ejecución en Windows.

## Dos condiciones para reejecutarlo

**1. Codificación.** El código imprime el símbolo `≥` en el nombre de la regla R08. Una
consola de Windows con la codificación por defecto falla con `UnicodeEncodeError`. Hay que
forzar UTF-8 por entorno, sin tocar el código:

```
PYTHONUTF8=1 PYTHONIOENCODING=utf-8 MPLBACKEND=Agg python codigo/codigo_hasta_hito2.py
```

Esto es un hallazgo de reproducibilidad en sí mismo: el código es reproducible siempre que
el entorno se declare; sin declararlo, falla.

**2. Nombres de columna.** El código espera los **nombres de visualización** del portal
(`Año`, `Mes`, `Tipo de Tarifa`, `Propiedad Epm`…) y lee el archivo como `epm_tarifas.csv`
desde la carpeta de trabajo.

El CSV conservado en `fuentes_datos/datos/epm_sfcd-b3ey.csv` trae los **nombres técnicos de
la API** (`year`, `mes`, `tipodetarifa`, `propiedadepm`…), porque se descargó por el
endpoint `/resource/`. **Con ese archivo el pipeline falla con `KeyError`.** Para
reejecutar hay que descargar por el endpoint `rows.csv?accessType=DOWNLOAD` o añadir un
mapeo de nombres en la capa de carga.

Resolver esto corresponde a la actividad 3 del Hito 3, que exige que el pipeline corra
«sin cambios manuales en las dos fuentes».

## Archivos

| Archivo | Contenido | Lo usa |
|---|---|---|
| `00_resumen.json` | Cifras agregadas y SHA-256 de la entrada | Verificación |
| `02_catalogo_variantes.csv` | Variantes de etiqueta y su forma canónica | R06, MAP01 |
| `03_hallazgos.csv` | Bitácora de incidencias por regla | **Insumo de los hitos 3 y 6** |
| `04_resumen_reglas.csv` | Filas marcadas por regla | Hito 3 |
| `05_alertas_imr_reales.csv` | Alertas de las cartas sobre datos reales | **Insumo de los hitos 3 y 6** |
| `06_experimento_inyeccion.csv` | Resultado por prueba inyectada | **Insumo del hito 4** |
| `07_deteccion_por_tipo.csv` | Detección por tipo de error y método | **Insumo del hito 4** |
| `08_copia_preparada.csv` | Copia preparada con trazabilidad | **Insumo del hito 3** |
| `11_puntajes_limpios_por_serie.csv` | Puntajes en meses sin error conocido | **Insumo del hito 4** |
| `figuras/` | Las cuatro gráficas del Hito 2 | Presentación |

## Advertencia

Estas salidas corresponden a **una** descarga del portal. El criterio de cierre del Hito 3
exige obtener los mismos hallazgos con **dos descargas distintas**, y la revisión del Hito 2
documenta que el portal devuelve las mismas filas en otro orden entre descargas. Esa
comprobación corresponde a la actividad 6 y no está hecha.
