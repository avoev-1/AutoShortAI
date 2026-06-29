# Safety — ZIP08 Production Queue & Scheduler

## Purpose

ZIP08 protects AutoShortAI from uncontrolled production execution.

The queue and scheduler must prevent:

- runaway background jobs
- excessive CPU usage
- excessive RAM usage
- uncontrolled API spending
- infinite retries
- duplicate execution
- unsafe state transitions
- hidden coupling between modules
- accidental SaaS assumptions

## Resource safety rules

A future implementation must support explicit limits for:

- concurrent jobs
- concurrent workers
- render workers
- API calls per time window
- API cost per day
- job runtime
- queue size
- retry count
- memory budget
- CPU target

## Retry safety rules

Retries must be bounded.

A job must never retry forever unless the user explicitly configures an experimental policy.

## Persistence safety rules

Queue state must be persisted in a way that can survive interruption.

Default expected persistence:

- local JSON
- atomic writes when implemented
- recoverable snapshots when implemented

SQLite or another storage provider may be added later, but ZIP08 must not make it mandatory.

## Provider safety

Workers must never call AI, rendering, distribution, or storage providers through hidden global coupling.

Every provider must be accessed through an explicit contract or adapter.

## User control

Future implementations must allow jobs to be:

- paused
- resumed
- cancelled
- retried
- inspected

## Non-SaaS safety

ZIP08 must not add tenant concepts, subscription logic, hosted billing logic, or centralized service assumptions.
