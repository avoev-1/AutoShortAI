# AutoShortAI ZIP07 — Creative Strategy Engine

ZIP07 introduces the architecture layer responsible for deciding what AutoShortAI should produce before a mission is executed.

This release does not implement a full AI content generator, analytics loop, video renderer, dashboard, SaaS layer, or Guardian Engine.
It defines the contracts, models, hooks, templates, and structural tests required for a future implementation to build creative strategies in a modular and reversible way.

## Position in the architecture

- ZIP04 defines mission orchestration.
- ZIP05 defines intelligent distribution planning.
- ZIP06 defines asset management, caching, checkpoints, cost optimization, and provider abstraction.
- ZIP07 defines creative strategy, content profiles, idea blueprints, script blueprints, variants, rules, and quality scoring contracts.

ZIP07 answers:

```text
What should be produced?
For which platform?
With which profile?
With which idea, angle, hook, structure, variants, and constraints?
```

## Required philosophy

ZIP07 keeps AutoShortAI:

- personal-use first, not SaaS;
- plugin-first;
- lightweight;
- core-independent;
- cross-platform;
- compatible with previous ZIPs;
- easy to extend without creating a monolith.

## Installed package

```text
src/autoshortai/creative_strategy/
```

The package contains Python contracts and data models only. Real production logic must be implemented later by Claude or another implementation agent while respecting these interfaces.

## Main architecture blocks

- Content Strategy Engine
- Creation Profile Registry
- Idea Blueprint System
- Script Blueprint Contracts
- Variant Planner
- Lightweight Rules Engine
- Quality Score Contracts
- Strategy Hook Registry
- Integration contracts with ZIP04, ZIP05, and ZIP06

## Integration workflow

From the repository root:

```bash
bash ~/Bureau/Projects/Archives/AutoShortAI_ZIP07_Creative_Strategy_Engine/INSTALL.sh
bash ~/Bureau/Projects/Archives/AutoShortAI_ZIP07_Creative_Strategy_Engine/VERIFY.sh
git status
git add .
git commit -m "feat(zip07): creative strategy engine"
git push origin main
```
