from __future__ import annotations

from dataclasses import dataclass, field
from typing import Mapping, Sequence


@dataclass(frozen=True)
class ConsentRequirement:
    creator_consent_required: bool = True
    all_participants_18_plus_required: bool = True
    rights_confirmed_required: bool = True


@dataclass(frozen=True)
class AgeGateRequirement:
    age_gate_required: bool = True
    target_platform_requires_18_plus: bool = True


@dataclass(frozen=True)
class RestrictedCreatorDevicePolicy:
    id: str = "adult_x_creator_default"
    enabled: bool = False
    manual_review_required: bool = True
    isolated_device_required: bool = True
    isolated_account_binding_required: bool = True
    restricted_logs_required: bool = True
    consent: ConsentRequirement = field(default_factory=ConsentRequirement)
    age_gate: AgeGateRequirement = field(default_factory=AgeGateRequirement)
    blocked_flags: Sequence[str] = (
        "minor_involved",
        "non_consensual",
        "illegal_content",
        "platform_policy_violation",
    )
    metadata: Mapping[str, str] = field(default_factory=dict)

    def can_dispatch(self, metadata: Mapping[str, bool]) -> bool:
        if not self.enabled:
            return False
        required = [
            "creator_consent",
            "all_participants_18_plus",
            "rights_confirmed",
            "age_gate",
            "manual_review_approved",
        ]
        return all(metadata.get(key) is True for key in required)
