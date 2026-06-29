# ZIP07 Architecture — Creative Strategy Engine

## Purpose

The Creative Strategy Engine is the strategic layer of AutoShortAI. It receives a creative intent and produces a structured plan that can later be executed by mission orchestration, asset generation, and distribution modules.

It is not responsible for rendering videos, uploading content, scraping analytics, running a dashboard, or managing a SaaS environment.

## High-level flow

```text
StrategyRequest
    ↓
CreationProfile selection
    ↓
IdeaBlueprint creation
    ↓
ScriptBlueprint planning
    ↓
Variant planning
    ↓
Rules validation
    ↓
Quality scoring
    ↓
CreativeStrategyPlan
    ↓
ZIP04 Mission Workflow Orchestrator
    ↓
ZIP06 Smart Asset Pipeline
    ↓
ZIP05 Intelligent Distribution Platform
```

## Core modules

### Content Strategy Engine

Coordinates profile resolution, idea normalization, script blueprint construction, variant planning, rule validation, and quality scoring.

The engine must stay small. It delegates specialized work to contracts instead of embedding everything into one class.

### Creation Profiles

Reusable strategy presets for platforms, niches, tones, durations, narrative shapes, energy levels, and risk levels.

Examples:

- `youtube_shorts_default`
- `tiktok_viral_fast`
- `instagram_reels_clean`
- `gaming_clip_reaction`
- `ai_news_daily`
- `motivation_dark_style`
- `finance_explainer_short`
- `documentary_micro_story`

### Idea Blueprint System

Defines stable structures for ideas before scripts or assets are generated.

Main objects:

- `ContentIdea`
- `ContentAngle`
- `ContentHook`
- `ContentPromise`
- `TargetAudience`

### Script Blueprint Contracts

Defines narrative blocks without generating final scripts.

Main objects:

- `ScriptBlueprint`
- `ScriptBlock`
- `HookBlock`
- `ContextBlock`
- `ValueBlock`
- `TwistBlock`
- `CTABlock`

### Variant Planner

Defines how multiple creative alternatives are planned from the same idea.

Variant examples:

- aggressive hook;
- mysterious hook;
- educational hook;
- faster pacing;
- lower-risk angle;
- different call-to-action.

### Lightweight Rules Engine

Validates strategy plans against simple, inspectable rules.

Examples:

- platform duration constraints;
- title length constraints;
- profile compatibility;
- estimated cost limits;
- duplicate idea prevention;
- asset availability requirements;
- safety and originality boundaries.

### Quality Score Contracts

Defines scoring dimensions without hardcoding an AI evaluator.

Score dimensions:

- hook score;
- clarity score;
- retention score;
- originality score;
- platform fit score;
- risk score;
- cost score.

### Strategy Hooks

Plugins can inspect or adapt the strategy lifecycle without modifying the core.

Required hook stages:

- `before_strategy_created`
- `after_strategy_created`
- `before_blueprint_generated`
- `after_blueprint_generated`
- `before_variant_planning`
- `after_variant_planning`
- `before_quality_scoring`
- `after_quality_scoring`
- `strategy_validation_failed`

## Separation from previous ZIPs

### ZIP04

ZIP04 orchestrates missions. ZIP07 gives ZIP04 a strategy plan.

### ZIP05

ZIP05 handles distribution intelligence. ZIP07 prepares platform-aware creative intent but does not upload or schedule posts.

### ZIP06

ZIP06 manages assets, fingerprints, cache, providers, and checkpoints. ZIP07 can request asset needs but must not own storage or caching logic.

## Non-goals

ZIP07 must not include:

- full video generation;
- final script generation logic;
- automatic analytics learning;
- Guardian Engine;
- dashboard implementation;
- SaaS billing, accounts, tenants, or public API;
- mandatory external AI dependency;
- phone-farm deployment logic.

## Extension principles

New creative strategies must be added as profiles, rules, hooks, or plugins.
The core package must remain small and stable.
