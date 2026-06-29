# Dependency Graph

The Dependency Graph records relationships between assets. It lets AutoShortAI understand which downstream assets are affected when an input changes.

## Examples

- Script text depends on research notes.
- Voiceover depends on final script.
- Captions depend on voiceover timing.
- Short video render depends on script, voiceover, captions, and visual assets.
- Distribution package depends on final render and metadata.

## Required properties

- Directed edges.
- Query impacted assets from an upstream change.
- Snapshot export for diagnostics.
- No direct dependency on workflow execution engine.

## Future implementation guidance

Start with a simple in-memory directed graph and JSON persistence. Avoid heavy graph databases unless a later ZIP explicitly requires them.
