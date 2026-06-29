# AutoShortAI ZIP08 — Production Queue & Scheduler

`ZIP08 — Production Queue & Scheduler` adds the architecture layer responsible for turning creative strategies and mission plans into ordered, schedulable, resumable production jobs.

This release is an architecture ZIP. It does not implement the full production engine. It defines contracts, models, hooks, templates, examples, documentation, and structure checks so Claude can later implement the real runtime without changing the architecture.

## Purpose

ZIP08 answers these questions:

- What production job should run next?
- When should a job run?
- Which jobs are pending, scheduled, running, paused, completed, failed, cancelled, or retrying?
- How should the system respect CPU, RAM, API cost, worker, cache, and time budgets?
- How should jobs resume after interruption?
- How should batch production be represented without creating a heavy monolith?
- How should future workers plug into the system without coupling the core?

## Position in the AutoShortAI architecture

```text
ZIP07 Creative Strategy Engine
        ↓
ZIP08 Production Queue & Scheduler
        ↓
ZIP04 Mission Workflow Orchestrator
        ↓
ZIP06 Smart Asset Pipeline
        ↓
ZIP05 Intelligent Distribution Platform
```

ZIP08 does not replace the mission orchestrator. It decides job ordering, cadence, retry policy, and resource safety. ZIP04 remains responsible for executing mission workflows.

## Components introduced

- Production Queue
- Production Job Contracts
- Scheduler Engine Contracts
- Priority Engine
- Resource Budget Guard
- Worker Contracts
- Retry and Failure Policy
- Queue Persistence Contracts
- Batch Planner
- Calendar and Cadence Contracts
- Queue Hooks
- Integration map with ZIP04, ZIP05, ZIP06, and ZIP07

## What this ZIP does not include

ZIP08 deliberately excludes:

- advanced analytics
- auto-learning
- Guardian Engine
- heavy dashboard
- complete video rendering runtime
- real AI worker implementation
- phone farm deployment
- SaaS architecture
- mandatory database dependency

These belong to later ZIP milestones.

## Installation

Run from the repository root:

```bash
bash ~/Bureau/Projects/Archives/AutoShortAI_ZIP08_Production_Queue_Scheduler/INSTALL.sh
```

## Verification

Run from the repository root:

```bash
bash ~/Bureau/Projects/Archives/AutoShortAI_ZIP08_Production_Queue_Scheduler/VERIFY.sh
```

## Commit convention

```bash
git add .
git commit -m "feat(zip08): production queue scheduler"
git push origin main
```
