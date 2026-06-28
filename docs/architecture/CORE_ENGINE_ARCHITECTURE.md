# Core Engine Architecture

```mermaid
flowchart TD
    A[Workflow Definition] --> B[Pipeline Graph]
    B --> C[Orchestrator]
    C --> D[Budget Guard]
    C --> E[Human Control Guard]
    C --> F[Queue]
    F --> G[Workers]
    G --> H[Providers and Plugins]
```
