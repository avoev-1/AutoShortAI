# Dependency Manager

Dependencies are module-scoped.

## Rule

A dependency required by one optional module must not become mandatory for the full application.

## Examples

- FFmpeg belongs to rendering profiles, not core.
- Device tools belong to device farm profiles, not core.
- Node belongs to future UI profiles, not core.
- OS keyring providers belong to ZIP18 provider profiles, not core.
