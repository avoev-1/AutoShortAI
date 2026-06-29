# Guardian Security Checks

ZIP15 Guardian should use ZIP18 rules to detect unsafe architecture drift.

## Checks

- scan examples for token-like strings
- scan docs for fake credentials that look real
- detect hard-coded provider keys
- detect raw secret logging
- detect restricted credentials used outside restricted workflows
- detect platform-specific credential coupling in the core

These checks should start as warnings, then become stronger once implementation stabilizes.
