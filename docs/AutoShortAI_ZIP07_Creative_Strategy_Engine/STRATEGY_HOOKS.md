# Strategy Hooks

Hooks allow plugins to inspect or adapt the creative strategy lifecycle.

Required stages:

- before_strategy_created;
- after_strategy_created;
- before_blueprint_generated;
- after_blueprint_generated;
- before_variant_planning;
- after_variant_planning;
- before_quality_scoring;
- after_quality_scoring;
- strategy_validation_failed.

Hooks must never force coupling between the core and a specific plugin.
