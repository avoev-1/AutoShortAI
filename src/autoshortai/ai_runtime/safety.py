from __future__ import annotations

from dataclasses import dataclass, field
from typing import Sequence

from .models import AIWorkerTask, ContentMaturityRating, SafetyReviewLevel
from .platform_context import PlatformContext


@dataclass(frozen=True)
class ConsentRequirement:
    required: bool = False
    metadata_keys: Sequence[str] = field(default_factory=lambda: ("creator_consent", "rights_confirmed"))


@dataclass(frozen=True)
class AgeGateRequirement:
    required: bool = False
    metadata_keys: Sequence[str] = field(default_factory=lambda: ("age_gate", "all_participants_18_plus"))


@dataclass(frozen=True)
class SafetyPolicy:
    id: str = "zip13.default.safety"
    restricted_platforms_require_manual_review: bool = True
    consent_requirement: ConsentRequirement = field(default_factory=lambda: ConsentRequirement(required=True))
    age_gate_requirement: AgeGateRequirement = field(default_factory=lambda: AgeGateRequirement(required=True))
    blocked_policy_flags: Sequence[str] = field(default_factory=lambda: (
        "minor_or_ambiguous_age",
        "non_consensual",
        "illegal_content",
        "credential_leak",
    ))


class SafetyValidator:
    def __init__(self, policy: SafetyPolicy | None = None):
        self.policy = policy or SafetyPolicy()

    def review_task(self, task: AIWorkerTask, platform_context: PlatformContext) -> tuple[SafetyReviewLevel, tuple[str, ...]]:
        notes: list[str] = []
        metadata = dict(task.metadata)

        for flag in self.policy.blocked_policy_flags:
            if metadata.get(flag) is True:
                return SafetyReviewLevel.BLOCKED, (f"blocked_policy_flag:{flag}",)

        if platform_context.is_restricted_adult or task.maturity_rating in {
            ContentMaturityRating.MATURE_18_PLUS,
            ContentMaturityRating.RESTRICTED_ADULT,
        }:
            notes.append("restricted_or_18_plus_context")
            if self.policy.restricted_platforms_require_manual_review:
                notes.append("manual_review_required")
            if platform_context.requires_consent_metadata or self.policy.consent_requirement.required:
                missing = [k for k in self.policy.consent_requirement.metadata_keys if not metadata.get(k)]
                if missing:
                    return SafetyReviewLevel.BLOCKED, tuple(notes + [f"missing_consent_metadata:{','.join(missing)}"])
            if platform_context.requires_age_gate or self.policy.age_gate_requirement.required:
                missing = [k for k in self.policy.age_gate_requirement.metadata_keys if not metadata.get(k)]
                if missing:
                    return SafetyReviewLevel.BLOCKED, tuple(notes + [f"missing_age_gate_metadata:{','.join(missing)}"])
            return SafetyReviewLevel.MANUAL_REVIEW_REQUIRED, tuple(notes)

        return task.safety_review_level, tuple(notes)
