"""Restricted adult creator publishing helpers for ZIP16.

This module contains compliance validation contracts only. It does not generate,
store, or publish adult content.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Sequence

from .models import MaturityRating, PlatformCategory, PublishingRequest, ReviewStatus


@dataclass(frozen=True)
class RestrictedPublishingProfile:
    profile_id: str
    enabled: bool = False
    requires_manual_review: bool = True
    requires_age_gate: bool = True
    requires_consent_metadata: bool = True
    requires_all_participants_18_plus: bool = True
    isolated_credentials_required: bool = True
    isolated_storage_required: bool = True
    sanitized_logs_required: bool = True


@dataclass(frozen=True)
class RestrictedPublishingReviewChecklist:
    maturity_rating_present: bool = False
    all_participants_18_plus_confirmed: bool = False
    consent_metadata_present: bool = False
    age_gate_enabled: bool = False
    manual_review_approved: bool = False
    restricted_storage_enabled: bool = False
    credentials_isolated: bool = False
    block_reasons: Sequence[str] = field(default_factory=tuple)


def validate_restricted_request(request: PublishingRequest) -> RestrictedPublishingReviewChecklist:
    reasons: list[str] = []
    is_restricted = request.target.category == PlatformCategory.ADULT_RESTRICTED or request.adult_compliance.enabled

    maturity_ok = request.metadata.maturity_rating == MaturityRating.ADULT_18_PLUS if is_restricted else True
    if is_restricted and not maturity_ok:
        reasons.append("restricted request must use adult_18_plus maturity rating")

    if is_restricted and not request.adult_compliance.all_participants_18_plus_confirmed:
        reasons.append("all participants 18+ confirmation missing")

    if is_restricted and not request.adult_compliance.consent_metadata_ref:
        reasons.append("consent metadata reference missing")

    if is_restricted and not request.adult_compliance.age_gate_required:
        reasons.append("age gate requirement missing")

    review_ok = request.approval.status == ReviewStatus.APPROVED
    if is_restricted and not review_ok:
        reasons.append("manual review approval required for restricted publishing")

    return RestrictedPublishingReviewChecklist(
        maturity_rating_present=maturity_ok,
        all_participants_18_plus_confirmed=request.adult_compliance.all_participants_18_plus_confirmed,
        consent_metadata_present=bool(request.adult_compliance.consent_metadata_ref),
        age_gate_enabled=request.adult_compliance.age_gate_required,
        manual_review_approved=review_ok,
        restricted_storage_enabled=request.adult_compliance.restricted_storage_required,
        credentials_isolated=False,
        block_reasons=tuple(reasons),
    )
