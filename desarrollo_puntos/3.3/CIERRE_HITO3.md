# Cierre del Hito 3

## Resultado

El Hito 3 queda documentado y reproducible para las cuatro fuentes seleccionadas. Se entregan
las fichas de caracterización, la matriz OE1, las reglas por fuente, las cartas logarítmicas, la
trazabilidad por fila, la cuarentena y el bootstrap por categoría.

## Entregables verificables

- [Matriz OE1](matriz_oe1.md), [CSV](matriz_oe1.csv) y [YAML](matriz_oe1.yaml): 19 controles × 4 fuentes.
- [Informe de diferencias entre fuentes](INFORME_DIFERENCIAS_FUENTES.md).
- [Fichas de caracterización](../3.2/README.md) para EPM, CHEC, SSPD y XM.
- [Cartas de EPM](EPM/REVISION_REGLAS_EPM.md), [CHEC](CHEC/REVISION_REGLAS_CHEC.md),
  [SSPD](SSPD/REVISION_REGLAS_SSPD.md) y [XM](XM/REVISION_REGLAS_XM.md).
- [Trazabilidad estable](../../fuentes_datos/verificaciones/trazabilidad_filas/README.md), con
  SHA-256, manifiesto de ejecución y claves de contenido.
- [Cuarentena](EPM/README_CUARENTENA.md) y verificaciones conservadoras de las demás fuentes.
- [Bootstrap por categoría](bootstrap/README.md), con 2.000 repeticiones y semilla fija.
- [Evidencia de exactitud y oportunidad](EVIDENCIA_EXACTITUD_OPORTUNIDAD.md), con procedimiento,
  fuentes disponibles y plantillas pendientes de diligenciar.
- [Reproducibilidad](REPRODUCIBILIDAD_HITO3.md), con la primera ejecución verificada y el requisito
  de una segunda versión independiente.

## Criterio de cierre y límites

El pipeline se puede ejecutar sin editar manualmente los datos fuente y los resultados quedan
asociados a una versión mediante SHA-256. Cada control tiene dimensión, fórmula, denominador,
umbral, estado y nota por fuente.

El cierre no significa que todas las dimensiones hayan alcanzado 100 % ni que toda evidencia sea
definitiva. Persisten estados provisionales, proxies, controles no aplicables y dos controles no
medibles por falta de evidencia. Exactitud necesita contraste documental y oportunidad necesita
evidencia de publicación y plazo; las alertas estadísticas no sustituyen ninguno de los dos.

## Entrada al Hito 4

El Hito 4 puede comenzar con esta línea base. Sus primeros productos deben ser el scorecard por
fuente y dimensión, la comparación de técnicas bajo el mismo protocolo y el análisis de
sensibilidad. Los resultados provisionales deben conservarse separados de los medidos y no se
deben comparar porcentajes sin revisar población, unidad y aplicabilidad.

Antes de declararlo formalmente aprobado, debe diligenciarse
[PENDIENTES_APROBACION_HITO3.md](PENDIENTES_APROBACION_HITO3.md). Ese documento concentra las
decisiones que dependen del director, de una fuente de contraste o de una segunda descarga; no se
han presentado como cumplidas.
