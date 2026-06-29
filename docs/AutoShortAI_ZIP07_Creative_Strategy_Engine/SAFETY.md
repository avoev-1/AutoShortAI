# ZIP07 Safety Notes

## Scope safety

ZIP07 only defines architecture contracts. It must not add production logic that can unexpectedly publish, upload, spend API credits, or mutate previous ZIP behavior.

## Creative safety

Creative strategy modules must support future checks for:

- originality;
- duplicate avoidance;
- platform fit;
- risk level;
- misleading claims;
- copyrighted source misuse;
- unsafe or policy-breaking content;
- cost and provider limits.

## Cost safety

ZIP07 must not call paid APIs directly. Any future implementation must route cost-sensitive work through ZIP06 provider and cost optimization contracts.

## Storage safety

ZIP07 must not own asset storage. It may describe asset needs, but ZIP06 remains responsible for registry, cache, fingerprinting, checkpoints, integrity, providers, and storage.

## Backward compatibility

ZIP07 installs into namespaced locations and must not overwrite previous ZIP documentation or source packages except for the safe namespace initializer when missing.
