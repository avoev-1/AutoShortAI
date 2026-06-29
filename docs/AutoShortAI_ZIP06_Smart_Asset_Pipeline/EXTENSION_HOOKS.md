# ZIP06 Extension Hooks

Hooks allow future plugins to observe or extend asset pipeline behavior without coupling to core modules.

## Hook categories

- `asset.registering`
- `asset.registered`
- `asset.fingerprinting`
- `asset.fingerprinted`
- `dependency.changed`
- `build.planned`
- `cache.hit`
- `cache.miss`
- `checkpoint.created`
- `resume.requested`
- `integrity.failed`
- `provider.operation_planned`
- `cost.estimated`
- `performance.sampled`

## Hook rules

- Hooks must receive serializable payloads where possible.
- Hooks must not be required for core correctness.
- A failed optional hook must not corrupt asset state.
- Hook registration belongs behind the Hook Registry contract.
