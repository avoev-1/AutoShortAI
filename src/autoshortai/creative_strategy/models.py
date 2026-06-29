"""ZIP07 Creative Strategy Engine models.

These are architecture-level data contracts. They intentionally avoid external
runtime dependencies and heavy implementation logic.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Mapping, Sequence


class PlatformTarget(str, Enum):
    """Supported strategic platform targets."""

    YOUTUBE_SHORTS = "youtube_shorts"
    TIKTOK = "tiktok"
    INSTAGRAM_REELS = "instagram_reels"
    VERTICAL_SHORT = "vertical_short"
    INTERNAL_DRAFT = "internal_draft"


class ContentFormat(str, Enum):
    """High-level content format."""

    SHORT = "short"
    MICRO_DOCUMENTARY = "micro_documentary"
    EXPLAINER = "explainer"
    REACTION = "reaction"
    NEWS = "news"
    STORY = "story"


class EnergyLevel(str, Enum):
    """Creative intensity level."""

    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class RiskLevel(str, Enum):
    """Strategic risk level for content framing."""

    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class StrategyPriority(str, Enum):
    """How the strategy should optimize tradeoffs."""

    SPEED = "speed"
    QUALITY = "quality"
    LOW_COST = "low_cost"
    RETENTION = "retention"
    ORIGINALITY = "originality"


class VariantIntent(str, Enum):
    """Reason for creating a strategy variant."""

    AGGRESSIVE_HOOK = "aggressive_hook"
    MYSTERY_HOOK = "mystery_hook"
    EDUCATIONAL = "educational"
    LOWER_RISK = "lower_risk"
    FASTER_PACING = "faster_pacing"
    DIFFERENT_CTA = "different_cta"


class BlueprintBlockKind(str, Enum):
    """Script blueprint block type."""

    HOOK = "hook"
    CONTEXT = "context"
    VALUE = "value"
    TWIST = "twist"
    CTA = "cta"


class RuleSeverity(str, Enum):
    """Rule violation severity."""

    INFO = "info"
    WARNING = "warning"
    ERROR = "error"


class QualityDimension(str, Enum):
    """Quality score dimensions."""

    HOOK = "hook"
    CLARITY = "clarity"
    RETENTION = "retention"
    ORIGINALITY = "originality"
    PLATFORM_FIT = "platform_fit"
    RISK = "risk"
    COST = "cost"


@dataclass(frozen=True)
class TargetAudience:
    """Audience definition for a creative idea."""

    label: str
    interests: Sequence[str] = field(default_factory=tuple)
    experience_level: str = "general"
    locale: str = "und"


@dataclass(frozen=True)
class ContentHook:
    """Opening hook concept, not final script copy."""

    text: str
    style: str = "direct"
    expected_seconds: float = 3.0


@dataclass(frozen=True)
class ContentAngle:
    """Framing angle for an idea."""

    label: str
    description: str
    risk_level: RiskLevel = RiskLevel.LOW


@dataclass(frozen=True)
class ContentPromise:
    """Promise made to the viewer."""

    value: str
    proof_hint: str | None = None


@dataclass(frozen=True)
class ContentIdea:
    """Normalized idea blueprint."""

    title: str
    angle: ContentAngle
    hook: ContentHook
    promise: ContentPromise
    audience: TargetAudience
    source_notes: Sequence[str] = field(default_factory=tuple)
    metadata: Mapping[str, str] = field(default_factory=dict)

    @property
    def idea_key(self) -> str:
        """Stable human-readable key for logs and manifests."""
        normalized = "-".join(self.title.lower().strip().split())
        return normalized or "untitled-idea"


@dataclass(frozen=True)
class CreationProfile:
    """Reusable creative production profile."""

    profile_id: str
    platform: PlatformTarget
    content_format: ContentFormat
    min_seconds: int
    max_seconds: int
    energy_level: EnergyLevel
    risk_level: RiskLevel
    narrative_blocks: Sequence[BlueprintBlockKind]
    style_tags: Sequence[str] = field(default_factory=tuple)
    visual_tags: Sequence[str] = field(default_factory=tuple)
    audio_tags: Sequence[str] = field(default_factory=tuple)
    asset_requirements: Sequence[str] = field(default_factory=tuple)
    max_estimated_cost: float | None = None


@dataclass(frozen=True)
class StrategyRequest:
    """Input request for creative strategy planning."""

    request_id: str
    profile_id: str
    initial_idea: str
    platform: PlatformTarget | None = None
    priority: StrategyPriority = StrategyPriority.QUALITY
    requested_variants: int = 1
    constraints: Mapping[str, str] = field(default_factory=dict)


@dataclass(frozen=True)
class ScriptBlock:
    """Narrative block in a script blueprint."""

    kind: BlueprintBlockKind
    objective: str
    min_seconds: float
    max_seconds: float
    notes: Sequence[str] = field(default_factory=tuple)


@dataclass(frozen=True)
class ScriptBlueprint:
    """Script architecture without final generated wording."""

    blueprint_id: str
    idea_key: str
    target_duration_seconds: int
    blocks: Sequence[ScriptBlock]
    constraints: Mapping[str, str] = field(default_factory=dict)


@dataclass(frozen=True)
class StrategyVariant:
    """Alternative creative direction for one strategy."""

    variant_id: str
    intent: VariantIntent
    idea: ContentIdea
    script_blueprint: ScriptBlueprint
    notes: Sequence[str] = field(default_factory=tuple)


@dataclass(frozen=True)
class RuleViolation:
    """Rules engine finding."""

    rule_id: str
    severity: RuleSeverity
    message: str
    path: str | None = None


@dataclass(frozen=True)
class QualityScore:
    """Score for one quality dimension."""

    dimension: QualityDimension
    value: float
    reason: str = ""


@dataclass(frozen=True)
class QualityReport:
    """Aggregated quality report for a strategy or variant."""

    scores: Sequence[QualityScore]
    passed: bool
    notes: Sequence[str] = field(default_factory=tuple)

    @property
    def average_score(self) -> float:
        if not self.scores:
            return 0.0
        return sum(score.value for score in self.scores) / len(self.scores)


@dataclass(frozen=True)
class CreativeStrategyPlan:
    """Output of the Creative Strategy Engine."""

    plan_id: str
    request: StrategyRequest
    profile: CreationProfile
    idea: ContentIdea
    script_blueprint: ScriptBlueprint
    variants: Sequence[StrategyVariant] = field(default_factory=tuple)
    rule_violations: Sequence[RuleViolation] = field(default_factory=tuple)
    quality_report: QualityReport | None = None
    asset_requirements: Sequence[str] = field(default_factory=tuple)
    distribution_hints: Mapping[str, str] = field(default_factory=dict)


@dataclass(frozen=True)
class StrategyExecutionContext:
    """Context object passed through hooks and adapters."""

    run_id: str
    release: str = "ZIP07"
    metadata: Mapping[str, str] = field(default_factory=dict)
