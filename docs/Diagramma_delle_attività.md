

```mermaid
graph LR
    A[Start] --> B(Lancio Steam)
    B --> C(Login Steam)
    C --> D{Seleziono Bastalon}
    D --> E(Lancio Bastalon)
    D --> F[Stop]
    E --> G[Fork or Join]
    G --> H(Gioco Bastalon)
    G --> I(Raccolta Statistiche)
    H --> L[Fork or Join]
    I --> L
    L --> M(Chiudo Bastalon)
    M --> F
```