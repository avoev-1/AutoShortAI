# ZIP06 Architecture — Smart Asset Pipeline

## Position in AutoShortAI

The Smart Asset Pipeline is an architecture layer between workflow orchestration and concrete asset production tools. ZIP04 defined mission workflow orchestration. ZIP05 defined intelligent distribution architecture. ZIP06 defines how generated assets are registered, fingerprinted, cached, resumed, verified, stored, and optimized before they flow into later distribution stages.

The pipeline must remain independent from business-specific content decisions. It does not decide what videos to create. It manages assets and their lifecycle.

## Design principles

1. **Core independence** — the asset pipeline exposes contracts and models, not hard-coded providers.
2. **Plugin-first** — storage, cache backends, fingerprint algorithms, profilers, and providers must be replaceable.
3. **Low overhead** — default behavior must be lightweight and avoid permanent background workers.
4. **Incremental by default** — unchanged assets must not be rebuilt unnecessarily.
5. **Resumable by design** — long workflows must be checkpointable.
6. **Cost-aware** — API usage must be estimated before expensive provider calls.
7. **Portable** — all contracts must be compatible with Windows, Linux, and macOS.
8. **Future mobile readiness** — interfaces must avoid desktop-only assumptions.

## Logical modules

```text
Mission Workflow Orchestrator
        |
        v
Smart Asset Pipeline
  ├─ Asset Registry
  ├─ Fingerprint Engine
  ├─ Dependency Graph
  ├─ Incremental Build Planner
  ├─ Cache Manager
  │   ├─ Memory Cache Level
  │   ├─ Local Disk Cache Level
  │   └─ External Cache Level contract
  ├─ Resume Engine
  ├─ Checkpoint System
  ├─ Integrity Checker
  ├─ Storage Manager
  ├─ Provider Abstraction Layer
  ├─ API Cost Optimizer
  └─ Performance Profiler
        |
        v
Distribution / Publishing / Archive Layers
```

## Asset lifecycle

1. A workflow step declares expected assets.
2. The Asset Registry creates stable asset identities.
3. The Fingerprint Engine computes content and metadata fingerprints.
4. The Dependency Graph records which assets depend on others.
5. The Incremental Build planner decides whether to rebuild or reuse.
6. The Cache Manager checks available cache levels.
7. The Storage Manager persists the asset through a provider contract.
8. The Integrity Checker validates that saved outputs match expectations.
9. The Checkpoint System records progress.
10. The Resume Engine restores execution after interruption.
11. The API Cost Optimizer prevents uncontrolled paid API usage.
12. The Performance Profiler records lightweight metrics for future optimization.

## Boundaries

ZIP06 defines the contracts. Real implementations must be added later behind these contracts. No module may directly import provider-specific SDKs unless it lives in a future provider plugin.

## Integration with previous ZIPs

- ZIP01 remains the production foundation.
- ZIP02 remains the modular core engine.
- ZIP03 remains the SDK plugin system.
- ZIP04 remains the mission workflow orchestrator.
- ZIP05 remains the intelligent distribution platform.
- ZIP06 adds an asset lifecycle layer without changing previous contracts.
