# ZIP09 Architecture — Analytics & Feedback Loop

## Purpose

ZIP09 adds the architecture layer that collects, normalizes, scores, stores, and reports performance signals from published content.

Its job is to answer:

- What content performed well?
- On which platform?
- Under which time window?
- Which creative profile or variant performed best?
- Which metrics should later influence Auto-Learning?
- Which feedback can be produced without automatically changing the system yet?

ZIP09 is a feedback layer, not an adaptation engine. ZIP10 will consume ZIP09 output to adapt strategies.

## Global platform-agnostic rule

No analytics core component may directly depend on a single platform.

Allowed:

- `PlatformMetricsAdapter`
- `PlatformCapabilityProfile`
- `NormalizedMetric`
- `MetricSource`
- `PlatformPerformance`

Forbidden:

- hardcoded YouTube-only assumptions in core models
- YouTube-specific field names as canonical internal fields
- platform API clients inside the core engine
- direct scraping logic in core contracts

Platform-specific logic must live behind adapters.

## Main layers

```text
Published Content
      ↓
Platform Metrics Adapters
      ↓
Normalized Metrics Model
      ↓
Analytics Core
      ↓
Performance Scoring
      ↓
Feedback Loop Engine
      ↓
Reports / Experiments / Future ZIP10 Auto-Learning
```

## Integration with previous ZIPs

```text
ZIP07 — Creative Strategy Engine
  creates ideas, profiles, hooks, variants

ZIP08 — Production Queue & Scheduler
  schedules and tracks production jobs

ZIP05 — Intelligent Distribution Platform
  distributes or schedules content on platforms

ZIP09 — Analytics & Feedback Loop
  collects and normalizes results after publication

ZIP10 — Auto-Learning Adaptation Engine
  will use ZIP09 feedback to adapt future decisions
```

## ZIP09 modules

```text
src/autoshortai/analytics/
  models.py        normalized data models
  contracts.py     Protocol interfaces
  adapters.py      adapter base contracts and placeholders
  capabilities.py  platform capability definitions
  normalizer.py    metric normalization contracts
  scoring.py       scoring contracts
  feedback.py      feedback loop contracts
  experiments.py   experiment tracking contracts
  storage.py       storage contracts
  reports.py       reporting contracts
  hooks.py         plugin-first hook names
  errors.py        domain exceptions
  version.py       release metadata
```

## Runtime expectations

ZIP09 must remain lightweight:

- no mandatory database
- no mandatory cloud service
- no heavy analytics runtime
- no forced API dependency
- JSON-local storage as the default future implementation path
- SQLite or remote storage only as optional providers later

## Compatibility

ZIP09 is backward-compatible with ZIP01 through ZIP08. It only adds new architecture surfaces and does not modify existing release contracts.
