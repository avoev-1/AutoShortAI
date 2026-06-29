# Roadmap ZIP08 — Production Queue & Scheduler

## Phase 1 — Architecture baseline

- Define production job models
- Define queue status lifecycle
- Define priority contracts
- Define scheduler engine interface
- Define resource budget guard interface
- Define worker contracts
- Define retry and failure policy contracts
- Define batch and cadence contracts

## Phase 2 — Claude implementation target

Claude should implement only after this ZIP is integrated.

Suggested implementation order:

1. Minimal local JSON queue repository
2. In-memory queue manager
3. Basic scheduler decision engine
4. Resource budget guard with simple limits
5. Retry policy evaluator
6. Batch plan to job descriptor conversion
7. CLI-safe queue inspection helpers
8. Integration adapters with ZIP04, ZIP06, and ZIP07

## Phase 3 — Future expansion

Future ZIPs may add:

- advanced analytics feedback
- auto-learning adaptation
- lightweight dashboard
- video rendering pipeline
- AI worker runtime
- device farm deployment
- Guardian Engine

## Non-goals for ZIP08

- No complete production runtime
- No full renderer
- No heavy database
- No SaaS backend
- No analytics intelligence
- No auto-learning
- No Guardian Engine
- No phone farm control
