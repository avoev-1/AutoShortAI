# ZIP08 Architecture — Production Queue & Scheduler

## Architectural intent

The Production Queue & Scheduler is the execution planning layer of AutoShortAI.

It must remain:

- lightweight
- local-first
- plugin-first
- deterministic where possible
- resumable
- compatible with previous ZIP releases
- independent from any mandatory database
- independent from any specific AI provider
- independent from any UI or SaaS assumption

It converts creative and operational intent into scheduled production jobs.

## Boundary

ZIP08 owns:

- job representation
- queue state contracts
- scheduling contracts
- priority scoring contracts
- budget and concurrency guard contracts
- retry and failure policy contracts
- worker interface contracts
- queue persistence interfaces
- batch planning contracts
- cadence definitions
- queue hooks

ZIP08 does not own:

- creative strategy generation
- mission workflow execution
- asset fingerprinting
- cache implementation
- video rendering implementation
- distribution publishing implementation
- analytics learning loops
- Guardian quality supervision

## Core flow

```text
CreativeStrategy / MissionPlan / BatchPlan
        ↓
ProductionJobFactory contract
        ↓
ProductionQueue contract
        ↓
SchedulerEngine contract
        ↓
ResourceBudgetGuard contract
        ↓
ProductionWorker contract
        ↓
MissionWorkflowOrchestrator
        ↓
Checkpoint / Cache / Asset / Distribution layers
```

## Production job lifecycle

```text
created
  ↓
pending
  ↓
scheduled
  ↓
running
  ↓
completed
```

Alternative paths:

```text
running → failed → retrying → scheduled
running → paused → scheduled
running → cancelled
failed  → cancelled
scheduled → cancelled
```

The lifecycle is contract-defined only. Runtime persistence and locking are implementation details for Claude.

## Production Queue

The queue is a logical container of `ProductionJob` items.

Required responsibilities:

- accept jobs
- reject invalid jobs
- expose jobs by status
- expose jobs by priority
- support safe state transitions
- support cancellation
- support pause/resume
- support retry eligibility checks
- expose immutable snapshots
- avoid owning heavy execution logic

The queue should not directly call AI providers, renderers, or platform APIs.

## Scheduler Engine

The scheduler decides when jobs are eligible to start.

Inputs:

- job priority
- scheduled time
- required worker type
- resource budget
- API budget
- dependency readiness
- asset availability
- retry policy
- cadence policy
- platform constraints
- checkpoint state

Outputs:

- selected jobs
- blocked jobs with reasons
- scheduling decision records

The scheduler must be deterministic enough for testing and debugging.

## Priority Engine

Priority is represented as a contract, not a hard-coded business rule.

Default priority levels:

- urgent
- high
- normal
- low
- background

A future implementation can combine:

- explicit user priority
- trend urgency
- platform schedule deadline
- campaign deadline
- retry state
- resource cost
- freshness
- expected value

ZIP08 defines the slots without implementing a complete scoring AI.

## Resource Budget Guard

The guard prevents AutoShortAI from becoming heavy.

Budget categories:

- CPU percentage target
- RAM megabytes
- maximum concurrent workers
- maximum render workers
- maximum API calls per window
- maximum API cost per day
- maximum job runtime
- maximum queue size
- maximum retries

The guard should be called before a worker starts.

## Worker Contracts

ZIP08 defines worker interfaces for future runtime modules:

- `ProductionWorker`
- `ScriptWorker`
- `AssetWorker`
- `RenderWorker`
- `DistributionWorker`
- `AnalysisWorker`

Workers are pluggable. The core queue should only depend on the worker contract, not on concrete implementations.

## Failure and retry policy

Failure must be explicit and non-destructive.

Supported contract decisions:

- retry now
- retry later
- pause
- cancel
- skip
- mark failed
- resume from checkpoint
- rollback partial outputs

ZIP06 checkpoints are the preferred way to resume long-running production work.

## Queue persistence

Persistence must be optional and replaceable.

Default architecture:

```text
JSON local persistence
```

Future compatible options:

```text
SQLite local provider
ZIP06 storage provider
remote storage provider
```

No heavy database is mandatory in ZIP08.

## Batch Planner

A batch plan represents a group of jobs derived from a campaign, a creative profile, or a content objective.

Examples:

- produce 10 YouTube Shorts
- generate 5 finance scripts
- create 3 variants of the same hook
- schedule 7 posts over one week

The batch planner creates job descriptors; it does not execute work directly.

## Cadence model

Cadence contracts support:

- daily production
- weekly production
- custom schedules
- campaign windows
- platform-specific posting rhythm
- blackout dates
- timezone-aware planned execution

The cadence layer should remain lightweight and serializable.

## Hooks

ZIP08 exposes queue hooks so plugins can extend behavior without modifying the core:

- `before_job_created`
- `after_job_created`
- `before_job_scheduled`
- `after_job_scheduled`
- `before_job_started`
- `after_job_completed`
- `after_job_failed`
- `before_retry`
- `after_retry`
- `before_queue_flush`
- `after_queue_flush`
- `before_budget_check`
- `after_budget_check`

Hooks are contracts only.

## Compatibility with previous ZIP releases

### ZIP04 — Mission Workflow Orchestrator

ZIP08 schedules jobs. ZIP04 executes mission workflows.

### ZIP05 — Intelligent Distribution Platform

ZIP08 can schedule distribution jobs, but ZIP05 owns platform distribution rules.

### ZIP06 — Smart Asset Pipeline

ZIP08 uses ZIP06 for checkpoint, cache, asset readiness, storage provider, and API cost constraints.

### ZIP07 — Creative Strategy Engine

ZIP07 creates strategy and blueprints. ZIP08 turns them into scheduled jobs.

## Design constraints

- No SaaS assumption
- No mandatory server
- No mandatory database
- No heavy UI dependency
- No hard AI provider dependency
- No direct video renderer dependency
- No phone farm dependency in this ZIP
- No regression against existing ZIP modules
