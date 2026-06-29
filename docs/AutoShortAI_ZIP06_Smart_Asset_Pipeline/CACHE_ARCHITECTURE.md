# Multi-Level Cache Architecture

ZIP06 defines a cache architecture, not a complete production cache.

## Cache levels

1. Memory cache: fastest, temporary, optional.
2. Local disk cache: durable on a single machine.
3. External cache: future provider-based cache for remote or shared storage.

## Cache Manager responsibilities

- Store and retrieve cache entries by stable keys.
- Validate entries with fingerprints.
- Apply cache policies.
- Invalidate entries safely.
- Expose cache metadata to incremental build planning.

## Design constraints

- The cache manager must not assume one operating system path format.
- Cache keys must be deterministic.
- Eviction policies must be configurable.
- Missing cache must never be fatal if the asset can be rebuilt.
