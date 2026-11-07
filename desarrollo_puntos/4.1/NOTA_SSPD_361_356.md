# Diferencia entre 361 y 356 series SSPD

El Hito 3 reporta 361 series SSPD y 4.332 cambios de vigilancia en la línea
base de cartas. La implementación actual de las viñetas 1 y 2 reporta 356
series y 4.272 observaciones de vigilancia.

La diferencia no proviene de una modificación del archivo fuente. El Hito 4.1
aplica el criterio temporal explícito del plan: solo se calcula un cambio cuando
los dos meses son consecutivos. Cinco series de SSPD no alcanzan 36 cambios de
referencia más 12 cambios de vigilancia bajo ese criterio y se excluyen.

No se imputan meses ni se cruzan discontinuidades. Los resultados del Hito 3 se
conservan como línea base histórica y los resultados de 4.1 como línea base
estricta por meses consecutivos. Las tasas no deben compararse sin declarar esta
diferencia de población.
