# Integration Guide for Claude

Claude must treat ZIP06 as architecture authority.

## Allowed next implementation tasks

- Implement minimal adapters behind contracts.
- Add unit tests for adapters.
- Integrate checkpoints with ZIP04 workflow steps through interfaces.
- Add local filesystem provider as a plugin-style adapter.
- Add conservative API cost policy.

## Forbidden tasks

- Do not redesign the architecture.
- Do not hard-code one provider into the core.
- Do not introduce heavy services, queues, databases, or daemons without a future ZIP requiring them.
- Do not convert the project into SaaS.
- Do not remove previous ZIP contracts.

## Implementation style

- Small modules.
- Clear interfaces.
- Minimal dependencies.
- Pure Python standard library first.
- Plugin boundaries respected.
- Cross-platform path handling.
