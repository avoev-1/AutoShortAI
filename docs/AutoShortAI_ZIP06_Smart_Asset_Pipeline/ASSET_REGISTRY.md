# Asset Registry

The Asset Registry is the authoritative catalog of known assets. It does not generate content and does not store large binary data directly. It records asset identity, status, kind, provider location, metadata, and lifecycle information.

## Responsibilities

- Create and resolve stable asset identifiers.
- Store asset metadata needed by workflows.
- Track asset status without owning execution.
- Expose query operations for other modules.
- Remain provider-agnostic.

## Non-responsibilities

- It does not compute fingerprints.
- It does not decide whether assets must be rebuilt.
- It does not upload assets to publishing platforms.
- It does not perform business-level content strategy.

## Required behavior for future implementation

- Asset IDs must be deterministic where possible.
- Duplicate registration must be handled safely.
- Metadata updates must not destroy previous required fields.
- Registry storage must be replaceable through plugins.

## Contract

See `src/autoshortai/asset_pipeline/contracts.py` and `asset_registry.py`.
