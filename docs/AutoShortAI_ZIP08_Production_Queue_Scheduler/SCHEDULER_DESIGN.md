# Scheduler Design

The Scheduler Engine selects eligible jobs without owning the full production execution.

## Inputs

- queue snapshot
- current time
- resource budget status
- dependency graph status
- asset readiness
- API cost budget
- retry policy status
- cadence rules
- platform deadlines
- manual overrides

## Outputs

- scheduling decisions
- blocked jobs
- blocked reasons
- selected jobs
- decision timestamp

## Determinism

The scheduler should be deterministic for the same snapshot and the same clock input.

## Scheduling decision examples

```text
run immediately
schedule for later
block because dependency is missing
block because API budget is exhausted
block because worker is unavailable
block because job exceeded retry policy
```
