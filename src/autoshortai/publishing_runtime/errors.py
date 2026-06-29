"""ZIP16 normalized publishing errors."""
from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Sequence


class PublishingFailureReason(str, Enum):
    INVALID_MEDIA = "invalid_media"
    INVALID_METADATA = "invalid_metadata"
    CAPABILITY_MISMATCH = "capability_mismatch"
    CREDENTIAL_EXPIRED = "credential_expired"
    ACCOUNT_RESTRICTED = "account_restricted"
    RATE_LIMITED = "rate_limited"
    PLATFORM_REJECTED = "platform_rejected"
    NETWORK_TIMEOUT = "network_timeout"
    MANUAL_REVIEW_BLOCKED = "manual_review_blocked"
    POLICY_VIOLATION = "policy_violation"
    RESTRICTED_COMPLIANCE_MISSING = "restricted_compliance_missing"
    UNKNOWN = "unknown"


class PublishingRecoveryAction(str, Enum):
    RETRY = "retry"
    RESCHEDULE = "reschedule"
    FIX_METADATA = "fix_metadata"
    RE_RENDER = "re_render"
    REFRESH_CREDENTIALS = "refresh_credentials"
    MANUAL_REVIEW = "manual_review"
    BLOCK = "block"


@dataclass(frozen=True)
class PublishingError:
    reason: PublishingFailureReason
    message: str
    recoverable: bool = False
    recommended_actions: Sequence[PublishingRecoveryAction] = field(default_factory=tuple)
    platform_id: str | None = None
    request_id: str | None = None


@dataclass(frozen=True)
class PublishingRetryPolicy:
    max_attempts: int = 0
    backoff_seconds: int = 300
    retry_on: Sequence[PublishingFailureReason] = field(default_factory=tuple)
    require_manual_review_after_failure: bool = True
