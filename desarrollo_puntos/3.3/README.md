# 3.3 · Réplica del pipeline y diferencias entre fuentes

Corresponde a la actividad 3 del Hito 3. Agrupa la adaptación de reglas a los esquemas
de las fuentes y el informe de diferencias de su aplicación.

| Archivo o carpeta | Función |
|---|---|
| [INFORME_DIFERENCIAS_FUENTES.md](INFORME_DIFERENCIAS_FUENTES.md) | Comparación de estructura, aplicabilidad, medición y limitaciones. |
| [medir_sspd.py](medir_sspd.py) | Adaptador de la matriz para SSPD ZNI, ebby-cjha. |
| [medir_xm.py](medir_xm.py) | Adaptador específico del piloto de demanda XM. |
| [lector_datos.py](lector_datos.py) | Carga compartida de CSV, incluidos los conservados en ZIP. |
| [EPM](EPM/REVISION_REGLAS_EPM.md), [CHEC](CHEC/REVISION_REGLAS_CHEC.md), [SSPD](SSPD/REVISION_REGLAS_SSPD.md), [XM](XM/REVISION_REGLAS_XM.md) | Documentación de aplicación, adaptación y estado de controles por fuente; también remite a las cartas. |
| [insumos_hito2](insumos_hito2/README.md) | Código y resultados EPM históricos usados como referencia para la réplica. Incluye insumos posteriores del Hito 4. |
| [medir_sspd_nr.py](medir_sspd_nr.py) | Adaptador histórico de bnkp-xdb7; se conserva como antecedente y no participa en la matriz principal actual. |

El script de medición principal está en [3.1](../3.1/medir_matriz_oe1.py), porque su
producto es la matriz OE1. Desde allí importa los adaptadores de esta carpeta.

El plan original menciona Superservicios vfjy-6fka y ocho períodos. Los archivos
actuales documentan SSPD ebby-cjha, con 59 períodos globales, y otras fuentes. La
organización respeta los archivos existentes y no cambia su alcance para hacerlos
coincidir con el ejemplo histórico del plan. Su aprobación metodológica es un asunto
distinto de su ubicación.
