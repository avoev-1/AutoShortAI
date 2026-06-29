# Resource Budget Guard

The Resource Budget Guard prevents AutoShortAI from becoming too heavy.

## Guard categories

- CPU budget
- RAM budget
- concurrent workers
- render workers
- API calls
- API cost
- maximum runtime
- queue size
- retry count

## Contract behavior

The guard returns a decision:

```text
allowed
blocked
deferred
requires_manual_approval
```

## Expected implementation style

Start simple:

- local process limits
- configured max workers
- estimated job cost
- simple daily API budget

Do not require a monitoring daemon in ZIP08.
