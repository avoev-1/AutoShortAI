# Architecture

```mermaid
flowchart LR
    UI[Dashboard] --> API[FastAPI]
    API --> DB[(PostgreSQL)]
    API --> R[(Redis)]
    R --> W[Workers]
    W --> AI[AI Pipeline]
    W --> V[Video Pipeline]
    W --> YT[YouTube Pipeline]
    W --> S[Storage Manager]
    YT --> AN[Analytics]
    AN --> OPT[Optimization]
    OPT --> AI
```
