from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Mapping, Sequence


class ReleaseStatus(str, Enum):
    DRAFT = "draft"
    CANDIDATE = "candidate"
    VALIDATED = "validated"
    BLOCKED = "blocked"
    RELEASED = "released"
    DEPRECATED = "deprecated"


class ReleaseGateStatus(str, Enum):
    PENDING = "pending"
    PASSED = "passed"
    WARNING = "warning"
    FAILED = "failed"
    BLOCKED = "blocked"
    SKIPPED = "skipped"


class ApprovalStatus(str, Enum):
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"
    NEEDS_REVIEW = "needs_review"


class ModuleStabilityStatus(str, Enum):
    PLANNED = "planned"
    ARCHITECTURE_READY = "architecture_ready"
    IMPLEMENTATION_READY = "implementation_ready"
    EXPERIMENTAL = "experimental"
    STABLE = "stable"
    RESTRICTED = "restricted"
    BLOCKED = "blocked"


class RiskLevel(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"
    BLOCKER = "blocker"


class RiskCategory(str, Enum):
    ARCHITECTURE = "architecture"
    SECURITY = "security"
    PERFORMANCE = "performance"
    PLATFORM = "platform"
    ADULT_RESTRICTED_MODE = "adult_restricted_mode"
    PUBLISHING = "publishing"
    STORAGE = "storage"
    CREDENTIALS = "credentials"
    RENDERING = "rendering"
    AI_PROVIDER = "ai_provider"
    PACKAGING = "packaging"
    COMPATIBILITY = "compatibility"


@dataclass(frozen=True)
class ReleaseChecklistItem:
    id: str
    title: str
    required: bool = True
    status: ReleaseGateStatus = ReleaseGateStatus.PENDING
    notes: str = ""


@dataclass(frozen=True)
class ReleaseChecklist:
    id: str
    items: Sequence[ReleaseChecklistItem] = field(default_factory=tuple)


@dataclass(frozen=True)
class ReleaseGate:
    id: str
    name: str
    status: ReleaseGateStatus = ReleaseGateStatus.PENDING
    required: bool = True
    message: str = ""


@dataclass(frozen=True)
class ReleaseApproval:
    approver: str
    status: ApprovalStatus
    note: str = ""


@dataclass(frozen=True)
class ReleaseRisk:
    id: str
    title: str
    category: RiskCategory
    level: RiskLevel
    mitigation: str
    blocks_release: bool = False


@dataclass(frozen=True)
class KnownIssue:
    id: str
    title: str
    risk_level: RiskLevel
    workaround: str | None = None
    blocks_release: bool = False


@dataclass(frozen=True)
class ModuleStabilityEntry:
    module_id: str
    name: str
    status: ModuleStabilityStatus
    owner_zip: str
    notes: str = ""


@dataclass(frozen=True)
class ModuleStabilityMatrix:
    baseline: str
    entries: Sequence[ModuleStabilityEntry] = field(default_factory=tuple)


@dataclass(frozen=True)
class BackwardCompatibilityPolicy:
    baseline: str
    rules: Sequence[str] = field(default_factory=tuple)


@dataclass(frozen=True)
class PlatformAgnosticPolicy:
    first_target: str = "youtube_shorts"
    future_platforms: Sequence[str] = field(default_factory=tuple)
    core_must_use_adapters: bool = True
    no_platform_lock_in: bool = True


@dataclass(frozen=True)
class RestrictedCreatorGovernancePolicy:
    enabled_by_default: bool = False
    opt_in_required: bool = True
    isolated_workspace_required: bool = True
    isolated_credentials_required: bool = True
    isolated_logs_required: bool = True
    manual_review_required: bool = True
    consent_metadata_required: bool = True
    all_participants_18_plus_required: bool = True
    maturity_rating_required: bool = True
    blocked_content_flags: Sequence[str] = field(default_factory=tuple)


@dataclass(frozen=True)
class ReleaseCandidate:
    id: str
    version: str
    baseline: str
    status: ReleaseStatus = ReleaseStatus.DRAFT
    gates: Sequence[ReleaseGate] = field(default_factory=tuple)
    checklist: ReleaseChecklist | None = None
    risks: Sequence[ReleaseRisk] = field(default_factory=tuple)
    notes: str = ""


@dataclass(frozen=True)
class BetaRelease:
    version: str
    baseline: str
    candidate: ReleaseCandidate
    approvals: Sequence[ReleaseApproval] = field(default_factory=tuple)
    release_notes: Sequence[str] = field(default_factory=tuple)


@dataclass(frozen=True)
class GovernanceReport:
    release_candidate_id: str
    baseline: str
    gates: Sequence[ReleaseGate]
    risks: Sequence[ReleaseRisk]
    module_matrix: ModuleStabilityMatrix | None = None
    metadata: Mapping[str, str] = field(default_factory=dict)

    @property
    def is_blocked(self) -> bool:
        if any(g.status in {ReleaseGateStatus.FAILED, ReleaseGateStatus.BLOCKED} and g.required for g in self.gates):
            return True
        return any(r.blocks_release or r.level == RiskLevel.BLOCKER for r in self.risks)
