# Migration Notes — ZIP05 to ZIP06

ZIP06 is additive. There is no breaking migration.

## What changes

ZIP06 adds a Smart Asset Pipeline package and documentation. Existing distribution architecture remains untouched.

## Expected integration path

1. Install ZIP06.
2. Run VERIFY.
3. Commit and push.
4. Claude may implement adapters behind ZIP06 contracts.
5. Distribution code from ZIP05 may later consume asset outputs through the registry and storage manager contracts.

## What must not happen

- Do not rewrite ZIP05 distribution logic to depend on concrete ZIP06 internals.
- Do not bypass ZIP03 plugin rules.
- Do not move prior ZIP documentation.
