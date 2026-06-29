"""ZIP07 Creative Strategy Engine contracts.

Implementations must satisfy these protocols while keeping the core modular,
plugin-first, and lightweight.
"""
from __future__ import annotations

from typing import Protocol, Sequence

from .models import (
    ContentIdea,
    CreativeStrategyPlan,
    CreationProfile,
    QualityReport,
    RuleViolation,
    ScriptBlueprint,
    StrategyExecutionContext,
    StrategyRequest,
    StrategyVariant,
)


class ContentStrategyEngineContract(Protocol):
    """Coordinates creative strategy creation."""

    def create_strategy(
        self,
        request: StrategyRequest,
        context: StrategyExecutionContext,
    ) -> CreativeStrategyPlan:
        """Return a strategy plan for the supplied request."""
        ...


class CreationProfileRegistryContract(Protocol):
    """Stores and resolves creation profiles."""

    def get_profile(self, profile_id: str) -> CreationProfile:
        """Return a profile by stable id."""
        ...

    def list_profiles(self) -> Sequence[CreationProfile]:
        """Return all available profiles."""
        ...


class IdeaBlueprintContract(Protocol):
    """Builds normalized idea blueprints from user or plugin intent."""

    def build_idea(
        self,
        request: StrategyRequest,
        profile: CreationProfile,
        context: StrategyExecutionContext,
    ) -> ContentIdea:
        """Return a normalized content idea."""
        ...


class ScriptBlueprintContract(Protocol):
    """Builds script structure without final copy generation."""

    def build_script_blueprint(
        self,
        idea: ContentIdea,
        profile: CreationProfile,
        context: StrategyExecutionContext,
    ) -> ScriptBlueprint:
        """Return a script blueprint."""
        ...


class VariantPlannerContract(Protocol):
    """Plans creative variants from a base idea and script blueprint."""

    def plan_variants(
        self,
        idea: ContentIdea,
        blueprint: ScriptBlueprint,
        profile: CreationProfile,
        count: int,
        context: StrategyExecutionContext,
    ) -> Sequence[StrategyVariant]:
        """Return planned variants."""
        ...


class RulesEngineContract(Protocol):
    """Validates strategy plans using lightweight inspectable rules."""

    def validate_plan(
        self,
        plan: CreativeStrategyPlan,
        context: StrategyExecutionContext,
    ) -> Sequence[RuleViolation]:
        """Return validation findings."""
        ...


class QualityScoringContract(Protocol):
    """Scores strategy quality dimensions."""

    def score_plan(
        self,
        plan: CreativeStrategyPlan,
        context: StrategyExecutionContext,
    ) -> QualityReport:
        """Return quality score report."""
        ...


class StrategyHookRegistryContract(Protocol):
    """Lifecycle hook dispatcher for plugin-first extensions."""

    def emit(
        self,
        stage: str,
        context: StrategyExecutionContext,
        payload: object,
    ) -> object:
        """Emit a hook stage and return the possibly adapted payload."""
        ...
