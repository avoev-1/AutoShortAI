# ZIP06 Safety and Stability Rules

## Architectural safety

- Keep the Smart Asset Pipeline independent from platform-specific publishing code.
- Do not introduce global mutable state in core contracts.
- Do not add provider SDK dependencies to the core package.
- Do not make the cache manager depend on a single storage backend.
- Do not allow workflow orchestration to bypass asset integrity checks once implemented.

## Cost safety

- Paid provider calls must pass through the API Cost Optimizer contract.
- Estimated cost and budget decisions must be recordable before execution.
- The default implementation must be conservative until the user explicitly configures limits.

## Performance safety

- Avoid always-on watchers.
- Avoid unnecessary hashing of unchanged large files.
- Prefer lazy loading and incremental checks.
- Keep profiler output lightweight and optional.

## Recovery safety

- Checkpoints must be append-safe or atomically replaceable in future implementations.
- Resume logic must validate fingerprints before trusting cached outputs.
- Failed checkpoints must be explicit and diagnosable.

## Backward compatibility

ZIP06 must not remove, rename, or override ZIP01-ZIP05 contracts. Any future implementation must preserve installed paths and public names unless a later ZIP defines a formal migration.
