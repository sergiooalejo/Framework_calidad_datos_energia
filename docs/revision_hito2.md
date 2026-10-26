# Revisión técnica del Hito 2

**Borrador preparado para revisión del director. No es el concepto oficial hasta que el director lo apruebe.**

Trabajo de grado: *Framework automatizado para la evaluación de la calidad de datos en registros administrativos del sector energético en Colombia*. Estudiantes: Grupo 03. Fecha de revisión: 23 de octubre de 2026.

Material revisado: anteproyecto (junio de 2026), retroalimentación de junio, presentaciones del Hito 1 y del Hito 2, y el código entregado hasta el Hito 2. El código se ejecutó de principio a fin en un entorno limpio con una descarga nueva del conjunto de EPM (sfcd-b3ey, datos.gov.co).

## 1. Veredicto

El Hito 2 es un avance sólido y honesto. El código se ejecuta sin modificaciones y reproduce todas las cifras de las diapositivas: 445 filas con etiquetas no canónicas, 10 duplicados, 83 series, 77 limpias, 8.282 pruebas, 80 / 80 / 88 % de detección, 11,4 % de alertas en meses limpios y 51 de 83 series alertando en febrero de 2020. La evaluación con errores inyectados, el umbral de Isolation Forest por validación cruzada y el bootstrap por series responden a las observaciones mayores 3 y 4 de la retroalimentación de junio. El hallazgo de los seriales de fecha de Excel es real y está bien argumentado.

Los problemas están en tres frentes: una inconsistencia entre lo que la diapositiva 9 defiende y lo que el pipeline hace, un supuesto estadístico frágil en las cartas, y una sobreestimación del tamaño muestral efectivo.

## 2. Observaciones mayores

1. **La cuarentena no se aplica a las cartas.** La diapositiva 9 sostiene que las reglas van antes que las cartas porque un error en la referencia deja la carta ciega. En el código, las seis series con valores en cuarentena solo se marcan como sucias: sus límites y sus alertas reales se calculan con el error dentro de la referencia. La figura B se construyó a mano, interpolando el valor, fuera del pipeline. La cuarentena por valor debe entrar en la función de límites, y la imputación, si se usa, debe declararse.

2. **Las cartas trabajan sobre cambios absolutos de tarifas indexadas.** Las tarifas crecen con la inflación; la varianza de los cambios crece con el nivel y los límites fijos de 2017 a 2019 quedan estrechos en 2021. Se ve en la figura B: los cambios de 2021 derivan hacia arriba y disparan alertas sin error. Usar diferencias logarítmicas o porcentuales corrige buena parte de las alertas tardías y hace comparables las series, también para los rasgos del Isolation Forest.

3. **No son 83 series independientes.** De las 83, 69 son 23 categorías del Nivel I por sus tres columnas de propiedad, y esas columnas son casi transformaciones lineales una de otra (razones medianas 0,964 y 0,928). El número efectivo está cerca de 30. Esto infla el bootstrap por serie y el conjunto de entrenamiento del Isolation Forest, y explica por qué las reglas detectan el 54 % de las desviaciones del 10 %: la regla de orden entre columnas las atrapa porque el margen entre ellas es menor que el 10 %. El bootstrap debe remuestrear por categoría y los resultados deben reportarse por nivel.

4. **El número de registro no es trazable entre descargas.** Una descarga nueva del portal trae las mismas 3.623 filas en otro orden. Los casos 2047, 3131, 3133 y 2348 de la diapositiva 7 aparecen en otra descarga como 1043, 1808, 1810 y 3092. La clave de trazabilidad debe ser de contenido (categoría, fecha, columna) o el identificador de fila de la API, y el hash SHA-256 debe acompañarse de la fecha de descarga.

5. **Faltan precisión y F1.** El anteproyecto los promete y la retroalimentación los pidió. Se reporta recall por tipo de error y tasa de alerta en meses limpios, que es lo correcto a tasa igualada, pero F1 debe aparecer al menos en la comparación global. Las "falsas alarmas" de los datos reales son alertas sin error conocido, no falsas alarmas confirmadas, y así deben llamarse.

6. **La pseudo-replicación debe declararse.** Veinte sorteos por serie y tipo caen en 13 meses distintos en promedio, y la columna equivocada tiene 760 pruebas frente a 1.540 de los otros tipos. Las 8.282 pruebas no son independientes. El bootstrap por series lo mitiga, pero el documento debe decirlo y reportar las pruebas por tipo.

7. **Febrero de 2020 no es una falsa alarma.** Las alertas se concentran en febrero y julio de 2020 y julio de 2021, meses de ajuste tarifario de inicio de semestre, probablemente la entrada de los cargos de distribución de la Resolución CREG 015 de 2018. Una carta de individuales está diseñada para detectar justamente eso. La regla de alerta sistémica que proponen (alertas compartidas por muchas series en el mismo mes) debe formalizarse dentro del framework.

## 3. Pendientes del anteproyecto y forma

- **Hipótesis frente a diseño sigue sin resolverse.** El anteproyecto conserva H1 y H0 inferenciales junto con Design Science, y el Hito 2 no compara contra ningún método manual. Salida: definir las reglas estáticas como el procedimiento tradicional (lo que hacen MinTIC y Deequ) y el framework como reglas más cartas. Con el bootstrap existente (88 % frente a 73 %, intervalos que no se solapan) la hipótesis se vuelve contrastable.
- **El conjunto de datos del anteproyecto no es el que se usa.** El documento nombra Superservicios y la CREG; el trabajo se hace sobre tarifas de EPM. Población, muestra y sección 5.8 deben actualizarse y EPM debe justificarse.
- **Las cartas de control no están en el anteproyecto.** Ni en objetivos, ni en marco teórico, ni en la lista de técnicas (Z-score, KNN, Isolation Forest extendido, PCA, K-Means, DBSCAN). Deben incorporarse como método estadístico clásico, con respaldo en Jones-Farmer et al. (2014) y en la técnica de control estadístico de procesos del DAMA-DMBOK2, capítulo 13.
- **Todavía no es un framework.** Es un guion lineal que depende de la carga manual en Colab, redefine variables de la Parte 1 en la Parte 2 y no tiene archivo de dependencias. Docker, Poetry y el tablero de Power BI del anteproyecto no aparecen.
- **R12 es demasiado severa.** Marcar como error todo valor mayor a diez veces la mediana de su serie y ponerlo en cuarentena puede eliminar valores legítimos en series que cruzan cero, como Restricciones. Debe ser advertencia hasta confirmación.
- **Detalles.** El código de la diapositiva 11 no es el del archivo entregado. Los dos sinónimos de rango de consumo siguen sin confirmar con EPM. La detección en t o t+1 y el rasgo de "cambio siguiente" del Isolation Forest hacen el método retrospectivo, válido para auditar datos publicados pero debe decirse.

## 4. Sobre el alcance

Un solo conjunto de 3.623 filas no descalifica una tesis de maestría si la pregunta es metodológica, y el protocolo de comparación con errores inyectados es un aporte defendible. Lo que hace corto el trabajo frente al anteproyecto aprobado es: una sola fuente, un tamaño efectivo pequeño, un solo modelo de aprendizaje automático, ausencia de análisis de sensibilidad, ausencia del artefacto prometido y ningún error confirmado con la entidad. El plan de hitos 3 a 6 (`plan_hitos_3-6_detallado.md`) organiza el cierre de esas brechas trazado a los cuatro objetivos específicos.

## 5. Verificación de reproducción

| Cifra de la presentación | Valor reproducido |
|---|---|
| Filas y columnas | 3.623 × 12 |
| Variantes de etiqueta / filas afectadas | 11 / 445 |
| Duplicados exactos adicionales | 10 |
| Series posibles / con 49 meses o más / limpias | 202 / 83 / 77 |
| Pruebas inyectadas | 8.282 |
| Detección total: reglas / cartas / IF / reglas + cartas | 73 / 80 / 80 / 88 % |
| Alertas en meses limpios: cartas / IF (umbral CV) | 11,4 / 12,0 % |
| Series con alerta en febrero de 2020 | 51 de 83 |
| IC 95 % de la diferencia IF − cartas | −1,4 a +2,3 puntos |
