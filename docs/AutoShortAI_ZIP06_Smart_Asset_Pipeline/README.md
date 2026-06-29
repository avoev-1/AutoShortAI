# AutoShortAI ZIP06 — Smart Asset Pipeline

ZIP06 is an official AutoShortAI architecture release. It defines the **Smart Asset Pipeline**, a lightweight and modular architecture layer responsible for asset registration, asset fingerprinting, dependency tracking, incremental rebuild decisions, multi-level caching, resumable execution, storage abstraction, API cost control, and performance profiling.

This ZIP does **not** implement the complete production logic. It provides contracts, models, hooks, templates, documentation, and structure tests so Claude can later implement the real code while respecting the architecture.

## Release scope

ZIP06 introduces the following architecture areas:

- Asset Registry
- Asset Fingerprint Engine
- Dependency Graph
- Incremental Build planner
- Multi-Level Cache
- Cache Manager
- Resume Engine
- Checkpoint System
- Integrity Checker
- Storage Manager
- Provider Abstraction Layer
- API Cost Optimizer
- Performance Profiler

## Non-goals

ZIP06 does not build the full asset processing engine, does not connect real external storage providers, does not call paid APIs, does not implement full cache eviction logic, and does not change ZIP01-ZIP05 behavior.

## Install workflow

From the repository root:

```bash
bash ~/Projects/Archives/AutoShortAI_ZIP06_Smart_Asset_Pipeline/INSTALL.sh
bash ~/Projects/Archives/AutoShortAI_ZIP06_Smart_Asset_Pipeline/VERIFY.sh
```

Expected repository root:

```text
~/Projects/AutoShortAI
```

## Compatibility rule

ZIP06 is additive. It must not remove, rename, or rewrite previous ZIP architecture files. All installed files are namespaced under ZIP06-specific locations where possible.
