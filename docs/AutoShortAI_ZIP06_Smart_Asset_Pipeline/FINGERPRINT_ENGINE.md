# Asset Fingerprint Engine

The Fingerprint Engine creates stable signatures for assets. These signatures are used by incremental build planning, cache validation, integrity checks, and resume safety.

## Fingerprint types

- Content fingerprint: hash of bytes or structured payload.
- Metadata fingerprint: hash of relevant metadata.
- Dependency fingerprint: derived from upstream asset fingerprints.
- Provider fingerprint: optional remote checksum or ETag when available.

## Design rules

- SHA-256 is the default baseline algorithm.
- Algorithm choice must be explicit in models.
- Large assets should be fingerprinted lazily or incrementally in future implementations.
- Fingerprints must not include unstable fields unless explicitly requested.

## Integration points

- Asset Registry stores latest known fingerprint references.
- Dependency Graph uses fingerprints to detect impact.
- Cache Manager uses fingerprints to validate entries.
- Integrity Checker verifies persisted assets against expected fingerprints.
