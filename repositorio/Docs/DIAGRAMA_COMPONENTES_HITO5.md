# Diagrama de componentes del artefacto · Hito 5

El siguiente flujo muestra qué recibe cada componente y qué resultado entrega. Las flechas
representan dependencias de proceso; los datos originales no se modifican.

```mermaid
flowchart LR
    A[Fuentes energéticas\nEPM · CHEC · SSPD · XM] --> B[Bronze\nData/bronze/datos · entradas versionadas]
    B --> C[Trazabilidad\nSHA-256 y procedencia]
    B --> D[Cuarentena\nrevisión de entradas]
    D --> E[Preparación y adaptadores\nlectura por fuente]
    E --> F[Cartas de control\nseries temporales]
    F --> G[Revisión de cartas\ncontroles comunes y específicos]
    E --> H[Matriz OE1\n8 dimensiones DAMA-DMBOK]
    E --> I[Bootstrap\ncategorías y referencias]
    F --> J[Detectores\nZ-score · Isolation Forest]
    I --> J
    J --> K[Calibración y sensibilidad]
    K --> L[Métricas]
    J --> M[Regla sistémica]
    H --> N[Scorecard]
    L --> N
    M --> N
    N --> O[Niveles y costos]
    N --> P[Outputs versionados]
    M --> P
    O --> P
    P --> Q[Bitácora de incidentes\nrevisión humana]
    P --> R[Streamlit\nvisualización y ejecución controlada]
    R --> S[Docker\nentorno reproducible]
    T[Configuración YAML\nreglas y umbrales] --> H
    T --> J
    U[Manifiesto de ejecución\nsemilla · fecha · versión · hashes] --> P
```

## Lectura del diagrama

1. Los archivos de las fuentes pertenecen a la capa Bronze y se conservan físicamente en `Data/bronze/datos/`; se identifican mediante hashes.
2. La cuarentena separa entradas que requieren revisión antes de analizarlas.
3. Las cartas, la matriz y los detectores producen resultados independientes que después se
   consolidan en el scorecard.
4. La bitácora no se llena automáticamente: una alerta debe revisarse antes de registrarse como
   incidente.
5. Streamlit muestra las salidas y permite ejecutar etapas autorizadas; Docker empaqueta el
   código y el entorno para que otra persona pueda reproducir el tablero.

