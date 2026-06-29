# Queue Contracts

## ProductionQueue contract

A ProductionQueue implementation must expose:

- add job
- get job
- list jobs by status
- list jobs by priority
- update status
- pause job
- resume job
- cancel job
- mark failed
- mark completed
- create snapshot

The queue must not directly execute rendering, AI generation, distribution, analytics, or asset processing.

## State transitions

Allowed core transitions:

```text
created -> pending
pending -> scheduled
scheduled -> running
running -> completed
running -> failed
running -> paused
paused -> scheduled
failed -> retrying
retrying -> scheduled
pending -> cancelled
scheduled -> cancelled
running -> cancelled
failed -> cancelled
```

Any other transition should be rejected or explicitly approved by a policy.

## Snapshot rule

A snapshot should be immutable from the caller perspective. It is intended for debugging, verification, dashboard display, and recovery.
