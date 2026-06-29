# Worker Contracts

Workers execute job work through plugin-compatible contracts.

## Base worker

`ProductionWorker` must define:

- worker id
- worker type
- capability list
- readiness check
- execute contract
- cancellation support contract
- optional checkpoint awareness

## Specialized workers

- ScriptWorker
- AssetWorker
- RenderWorker
- DistributionWorker
- AnalysisWorker

Specialized workers remain contracts. Concrete implementation belongs later.

## Coupling rule

Workers must not be hard-coded into the queue. The queue depends on worker contracts only.
