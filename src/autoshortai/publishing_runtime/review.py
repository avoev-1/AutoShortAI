"""ZIP16 manual review gate contracts."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Sequence

from .models import PlatformCategory, PublishingApproval, PublishingContext, PublishingRequest, ReviewStatus
from .restricted import validate_restricted_request


@dataclass(frozen=True)
class ManualReviewPolicy:
    default_required: bool = True
    restricted_required: bool = True
    require_media_check: bool = True
    require_metadata_check: bool = True
    require_target_check: bool = True


@dataclass(frozen=True)
class ReviewDecision:
    approved: bool
    status: ReviewStatus
    reasons: Sequence[str] = field(default_factory=tuple)


class DefaultReviewGate:
    """Safe default review gate: does not auto-approve real publishing."""

    def __init__(self, policy: ManualReviewPolicy | None = None) -> None:
        self.policy = policy or ManualReviewPolicy()

    def review(self, request: PublishingRequest, context: PublishingContext) -> PublishingApproval:
        block_reasons: list[str] = []
        if self.policy.require_media_check and not request.media.path:
            block_reasons.append("media path is required")
        if self.policy.require_metadata_check and not request.metadata.title:
            block_reasons.append("title is required")
        if self.policy.require_target_check and not request.target.platform_id:
            block_reasons.append("target platform is required")
        if request.target.category == PlatformCategory.ADULT_RESTRICTED or request.adult_compliance.enabled:
            restricted = validate_restricted_request(request)
            block_reasons.extend(restricted.block_reasons)
        if block_reasons:
            return PublishingApproval(status=ReviewStatus.BLOCKED, block_reasons=tuple(block_reasons))
        if self.policy.default_required:
            return PublishingApproval(status=ReviewStatus.PENDING, notes="Manual review required before publish.")
        return PublishingApproval(status=ReviewStatus.APPROVED, notes="Approved by policy.")
