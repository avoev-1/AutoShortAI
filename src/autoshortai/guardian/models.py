"""Guardian Engine models for AutoShortAI ZIP15.

These are architecture contracts, not a full Guardian implementation.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Mapping, Sequence


class GuardianSeverity(str, Enum):
    INFO = "info"
    WARNING = "warning"
    ERROR = "error"
    CRITICAL = "critical"


class GuardianStatus(str, Enum):
    PASSED = "passed"
    WARNING = "warning"
    FAILED = "failed"
    SKIPPED = "skipped"
    NOT_APPLICABLE = "not_applicable"


class GuardianScope(str, Enum):
    ARCHITECTURE = "architecture"
    ZIP_COMPATIBILITY = "zip_compatibility"
    MODULE_BOUNDARY = "module_boundary"
    PLATFORM_AGNOSTIC = "platform_agnostic"
    PROVIDER_AGNOSTIC = "provider_agnostic"
    LIGHTWEIGHT = "lightweight"
    SECURITY = "security"
    RESTRICTED_CREATOR = "restricted_creator"
    DOCUMENTATION = "documentation"
    SCRIPTS = "scripts"


@dataclass(frozen=True)
class GuardianContext:
    project_root: str
    release_id: str
    target_paths: Sequence[str] = field(default_factory=tuple)
    previous_releases: Sequence[str] = field(default_factory=tuple)
    metadata: Mapping[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class GuardianRule:
    id: str
    name: str
    scope: GuardianScope
    severity: GuardianSeverity
    description: str
    recommendation: str = ""
    tags: Sequence[str] = field(default_factory=tuple)


@dataclass(frozen=True)
class GuardianViolation:
    rule_id: str
    severity: GuardianSeverity
    message: str
    path: str | None = None
    recommendation: str = ""
    metadata: Mapping[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class GuardianResult:
    rule: GuardianRule
    status: GuardianStatus
    message: str
    violations: Sequence[GuardianViolation] = field(default_factory=tuple)
    warnings: Sequence[str] = field(default_factory=tuple)
    metadata: Mapping[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class GuardianScoreCard:
    architecture_score: float | None = None
    compatibility_score: float | None = None
    platform_neutrality_score: float | None = None
    provider_neutrality_score: float | None = None
    lightweight_score: float | None = None
    restricted_workflow_score: float | None = None
    security_score: float | None = None


@dataclass(frozen=True)
class GuardianReport:
    release_id: str
    status: GuardianStatus
    results: Sequence[GuardianResult] = field(default_factory=tuple)
    scorecard: GuardianScoreCard = field(default_factory=GuardianScoreCard)
    summary: str = ""
    recommendations: Sequence[str] = field(default_factory=tuple)

    @property
    def violations(self) -> tuple[GuardianViolation, ...]:
        collected: list[GuardianViolation] = []
        for result in self.results:
            collected.extend(result.violations)
        return tuple(collected)
