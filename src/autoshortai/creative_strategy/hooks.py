"""Strategy lifecycle hook names for ZIP07."""
from __future__ import annotations

from enum import Enum


class StrategyHookStage(str, Enum):
    """Stable lifecycle hooks exposed by the Creative Strategy Engine."""

    BEFORE_STRATEGY_CREATED = "before_strategy_created"
    AFTER_STRATEGY_CREATED = "after_strategy_created"
    BEFORE_BLUEPRINT_GENERATED = "before_blueprint_generated"
    AFTER_BLUEPRINT_GENERATED = "after_blueprint_generated"
    BEFORE_VARIANT_PLANNING = "before_variant_planning"
    AFTER_VARIANT_PLANNING = "after_variant_planning"
    BEFORE_QUALITY_SCORING = "before_quality_scoring"
    AFTER_QUALITY_SCORING = "after_quality_scoring"
    STRATEGY_VALIDATION_FAILED = "strategy_validation_failed"


REQUIRED_STRATEGY_HOOKS: tuple[str, ...] = tuple(stage.value for stage in StrategyHookStage)
