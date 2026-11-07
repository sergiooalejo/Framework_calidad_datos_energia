# Hito 4.1 · Viñeta 2 · Entrenamiento en referencia y evaluación en vigilancia

## Implementación

`isolation_forest_referencia_vigilancia.py` es una implementación independiente
del Isolation Forest del Hito 2. No modifica sus scripts, CSV ni resultados.

El protocolo utiliza:

- cambios logarítmicos de meses consecutivos;
- 36 cambios de referencia;
- 12 cambios de vigilancia;
- un modelo independiente por fuente;
- escalamiento robusto calculado solo con referencia;
- umbral definido por el percentil 99,5 de los puntajes de entrenamiento.

Las cuatro características son:

1. cambio logarítmico actual;
2. cambio logarítmico anterior;
3. diferencia absoluta entre ambos cambios;
4. nivel logarítmico relativo a la mediana de referencia.

## Ejecución

Desde la raíz del repositorio:

```bash
python desarrollo_puntos/4.1/isolation_forest_referencia_vigilancia.py
```

Para sensibilidad del umbral de referencia:

```bash
python desarrollo_puntos/4.1/isolation_forest_referencia_vigilancia.py --percentil 0.99
python desarrollo_puntos/4.1/isolation_forest_referencia_vigilancia.py --percentil 0.9975
```

## Salidas

- `isolation_forest_referencia_vigilancia_detalle.csv`: puntaje y señal por
  serie y periodo de vigilancia.
- `isolation_forest_referencia_vigilancia_resumen.csv`: resumen por fuente.
- `isolation_forest_referencia_vigilancia_configuracion.json`: configuración,
  hashes de entradas y evidencia de que el entrenamiento usó únicamente la
  referencia.
- `auditoria_cuarentenas_h3.json`: registro de las cuatro cuarentenas heredadas
  del Hito 3. EPM se aplica al construir las series; las otras tres se auditan
  explícitamente y actualmente no contienen filas.

La ejecución no produce todavía precisión, recall o F1: esas métricas requieren
repetir el experimento de errores inyectados con este método.
