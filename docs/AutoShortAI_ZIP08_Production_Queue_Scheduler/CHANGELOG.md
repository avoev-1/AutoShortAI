# Changelog — ZIP08 Production Queue & Scheduler

## Added

- Production queue architecture
- Production job lifecycle contracts
- Scheduler engine contracts
- Priority engine contracts
- Resource budget guard contracts
- Worker interface contracts
- Retry and failure policy contracts
- Queue persistence contracts
- Batch planning contracts
- Cadence and calendar contracts
- Queue hook constants
- ZIP08 documentation
- ZIP08 templates
- ZIP08 examples
- ZIP08 structure tests
- INSTALL and VERIFY scripts

## Compatibility

- Preserves ZIP01 through ZIP07 architecture
- Adds new module namespace only: `autoshortai.production_queue`
- Does not modify existing ZIP contracts
- Does not introduce mandatory external dependencies
- Does not require a database
- Does not require a server
- Does not implement SaaS behavior

## Commit convention

```bash
feat(zip08): production queue scheduler
```
