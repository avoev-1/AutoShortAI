# ZIP10 Architecture — Auto-Learning Adaptation Engine

## Position in AutoShortAI

ZIP10 closes the first controlled intelligence loop of AutoShortAI:

```text
ZIP07 Creative Strategy Engine
        ↓
ZIP08 Production Queue & Scheduler
        ↓
ZIP05 Distribution Platform
        ↓
ZIP09 Analytics & Feedback Loop
        ↓
ZIP10 Auto-Learning Adaptation Engine
        ↓
ZIP07 Creative Strategy Engine
```

ZIP10 does not replace strategy, scheduling, distribution or analytics. It only transforms observed outcomes into safe, reviewable adaptation suggestions.

## Architectural boundaries

ZIP10 may consume data from:

- ZIP07 creative strategies, profiles, blueprints and variants,
- ZIP08 production jobs and run outcomes,
- ZIP09 normalized analytics and experiment results,
- ZIP06 costs, cache and storage providers,
- ZIP05 publishing/distribution results.

ZIP10 must not:

- directly publish content,
- render videos,
- own platform APIs,
- mutate creative profiles without an explicit policy,
- force a database dependency,
- implement Guardian Engine responsibilities,
- turn AutoShortAI into a SaaS.

## Core components

### Learning Core

Receives normalized evidence and produces learning outputs:

- `LearningSignal`
- `LearningInsight`
- `AdaptationSuggestion`
- `StrategyRecommendation`

The core is deterministic by default and can later delegate scoring to AI providers through explicit worker contracts.

### Adaptation Engine

Transforms insights into concrete suggested adjustments:

- shorter hooks,
- stronger openings,
- duration range changes,
- format prioritization,
- platform-specific timing preferences,
- reduced use of weak variants,
- improved cost/performance balance.

### Learning Memory

Stores historical learning state locally through lightweight persistence. JSON local storage is the default. SQLite or other providers may be added later through ZIP06 storage abstractions.

### Experiment Learning

Uses ZIP07 variants and ZIP09 experiment metrics to identify strong and weak patterns with confidence levels.

### Confidence & Safety Layer

Every suggestion must include:

- confidence level,
- sample size,
- risk level,
- whether rollback is available,
- whether manual review is required.

### Adaptation Policies

Supported policy modes:

- `manual_only`
- `suggestion_only`
- `semi_automatic`
- `automatic_safe`
- `locked`

The default must be `suggestion_only`.

## Platform-agnostic requirement

All learning outputs must support:

- generic cross-platform insights,
- platform-specific adjustments,
- platform capability limits,
- future network providers.

The core must never be named or designed around only YouTube.

## Data flow

```text
Normalized analytics snapshot
        ↓
Learning signal extraction
        ↓
Insight generation
        ↓
Confidence and policy evaluation
        ↓
Adaptation suggestion
        ↓
Optional profile adjustment proposal
        ↓
Learning memory save
```

## Extension model

ZIP10 is plugin-first. New learning providers, scoring strategies and policy evaluators must be injectable without modifying the core.
