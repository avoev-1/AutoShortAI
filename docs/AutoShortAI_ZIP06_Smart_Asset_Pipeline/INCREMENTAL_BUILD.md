# Incremental Build

Incremental Build decides whether an asset must be rebuilt or can be reused. The decision must be based on fingerprints, dependencies, cache availability, and integrity state.

## Build decision inputs

- Asset identity
- Current fingerprint
- Previous fingerprint
- Dependency graph snapshot
- Cache entry state
- Integrity report
- Provider availability
- Explicit force-rebuild flag

## Decision output

The planner returns a `BuildDecision` model with:

- target asset ID
- `should_rebuild`
- reason
- required dependency list
- optional metadata

## Hard rule

The planner must not execute the build itself. It only plans. Execution remains owned by workflow orchestration and future implementation layers.
