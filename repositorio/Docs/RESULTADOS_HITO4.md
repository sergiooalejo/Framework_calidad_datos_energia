# Resultados preliminares del Hito 4 · protocolo v2

Referencia 36, vigilancia 12, tasa objetivo de calibración 5 %, prevalencia **supuesta** 5 % y detección en t. Todos los umbrales se congelan antes de vigilancia. Los IC son de categorías completas; XM es descriptivo sin IC.

| Fuente | Método | Recall [IC 95 %] | Alerta observada | Precisión de escenario | F1 [IC 95 %] |
|---|---|---|---|---|---|
| EPM | IMR | 0.633 [0.594, 0.670] | 0.00 % | 1.000 | 0.775 [0.745, 0.803] |
| EPM | Z_robusto | 0.646 [0.601, 0.691] | 0.82 % | 0.806 | 0.717 [0.629, 0.803] |
| EPM | IF | 0.542 [0.511, 0.581] | 0.00 % | 1.000 | 0.703 [0.676, 0.735] |
| EPM | LOF | 0.543 [0.500, 0.606] | 0.00 % | 1.000 | 0.704 [0.667, 0.755] |
| EPM | KNN | 0.549 [0.504, 0.613] | 0.00 % | 1.000 | 0.709 [0.670, 0.760] |
| EPM | R12 | 0.505 [0.481, 0.528] | 16.12 % | 0.141 | 0.221 [0.162, 0.334] |
| CHEC | IMR | 0.618 [0.602, 0.633] | 0.00 % | 1.000 | 0.764 [0.751, 0.775] |
| CHEC | Z_robusto | 0.642 [0.629, 0.656] | 0.00 % | 1.000 | 0.782 [0.772, 0.792] |
| CHEC | IF | 0.603 [0.590, 0.615] | 0.25 % | 0.928 | 0.731 [0.710, 0.749] |
| CHEC | LOF | 0.509 [0.504, 0.514] | 0.00 % | 1.000 | 0.674 [0.670, 0.679] |
| CHEC | KNN | 0.528 [0.515, 0.544] | 0.00 % | 1.000 | 0.691 [0.680, 0.704] |
| CHEC | R12 | 0.373 [0.359, 0.388] | 0.00 % | 1.000 | 0.543 [0.528, 0.559] |
| SSPD | IMR | 0.622 [0.606, 0.637] | 3.02 % | 0.520 | 0.566 [0.525, 0.615] |
| SSPD | Z_robusto | 0.596 [0.575, 0.617] | 3.45 % | 0.477 | 0.530 [0.480, 0.583] |
| SSPD | IF | 0.616 [0.599, 0.632] | 4.32 % | 0.429 | 0.506 [0.457, 0.560] |
| SSPD | LOF | 0.391 [0.358, 0.422] | 3.25 % | 0.388 | 0.390 [0.344, 0.441] |
| SSPD | KNN | 0.559 [0.537, 0.579] | 3.00 % | 0.495 | 0.525 [0.473, 0.580] |
| SSPD | R12 | 0.306 [0.293, 0.320] | 7.16 % | 0.183 | 0.229 [0.198, 0.268] |
| XM | IMR | 0.655 [sin IC] | 0.00 % | 1.000 | 0.791 [sin IC] |
| XM | Z_robusto | 0.673 [sin IC] | 0.00 % | 1.000 | 0.804 [sin IC] |
| XM | IF | 0.709 [sin IC] | 0.00 % | 1.000 | 0.830 [sin IC] |
| XM | LOF | 0.800 [sin IC] | 16.67 % | 0.202 | 0.322 [sin IC] |
| XM | KNN | 0.745 [sin IC] | 0.00 % | 1.000 | 0.854 [sin IC] |
| XM | R12 | 0.418 [sin IC] | 8.33 % | 0.209 | 0.279 [sin IC] |

Una tasa de alerta observada igual a cero produce precisión de escenario igual a uno bajo esa fórmula; **no acredita precisión empírica de 100 %**. Un IC degenerado en ese snapshot tampoco garantiza ausencia de falsas alertas futuras. La precisión real requiere las etiquetas externas del Hito 6.

La comparación general no fuerza un ganador ni convierte diferencias puntuales en evidencia de superioridad. Las conclusiones deben considerar IC, población, tipos de error, baja resolución de calibración y tasa observada. Los resultados por tipo, ventanas pareadas, prevalencias y ambos horizontes están en los CSV y figuras.

LOF se calcula con geometría de referencia deduplicada para los tres métodos ML. La auditoría lof.csv conserva la reducción de frecuencia y verifica si algún banco debe excluirse; resolver duplicados numéricos no convierte el método en aprobado.

Los tres meses de referencia regulatoria se contrastan en contraste_componentes_vigente.csv y meses_plan_epm.csv. Los documentos oficiales y el cotejo numérico respaldan el contexto, sin probar por sí solos una causa.
