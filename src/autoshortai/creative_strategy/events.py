"""Event names emitted by future ZIP07 implementations."""
from __future__ import annotations

from enum import Enum


class StrategyEventName(str, Enum):
    STRATEGY_REQUESTED = "strategy_requested"
    PROFILE_RESOLVED = "profile_resolved"
    IDEA_BLUEPRINT_CREATED = "idea_blueprint_created"
    SCRIPT_BLUEPRINT_CREATED = "script_blueprint_created"
    VARIANTS_PLANNED = "variants_planned"
    RULES_VALIDATED = "rules_validated"
    QUALITY_SCORED = "quality_scored"
    STRATEGY_PLAN_CREATED = "strategy_plan_created"
