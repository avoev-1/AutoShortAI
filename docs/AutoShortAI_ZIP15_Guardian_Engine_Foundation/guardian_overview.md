# Guardian Overview

Guardian is the architecture protection layer for AutoShortAI.

It should be used by Claude as a checklist before and after implementation.

## Before implementation

- Read the ZIP architecture.
- Check module ownership.
- Check existing contracts.
- Check platform-agnostic rules.
- Check provider-agnostic rules.
- Check restricted workflow requirements if relevant.

## After implementation

- Run structure checks.
- Validate imports and boundaries.
- Validate docs/scripts/tests presence.
- Validate no secrets were committed.
- Validate no platform lock-in was introduced.
- Validate no previous ZIP was broken.
