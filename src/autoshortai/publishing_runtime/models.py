"""ZIP16 publishing runtime models.

These are architecture contracts only. They do not perform real API calls.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Mapping, Sequence


class PlatformCategory(str, Enum):
    GENERAL = "general"
    CREATOR = "creator"
    ADULT_RESTRICTED = "adult_restricted"


class PublishingStatus(str, Enum):
    DRAFT = "draft"
    READY_FOR_REVIEW = "ready_for_review"
    REVIEW_BLOCKED = "review_blocked"
    APPROVED = "approved"
    SCHEDULED = "scheduled"
    PUBLISHING = "publishing"
    PUBLISHED = "published"
    FAILED = "failed"
    CANCELLED = "cancelled"


class PublishingVisibility(str, Enum):
    PRIVATE = "private"
    UNLISTED = "unlisted"
    PUBLIC = "public"
    SUBSCRIBERS_ONLY = "subscribers_only"
    PAID_ONLY = "paid_only"


class PublishingMode(str, Enum):
    IMMEDIATE = "immediate"
    SCHEDULED = "scheduled"
    MANUAL_HOLD = "manual_hold"
    DRY_RUN = "dry_run"


class MaturityRating(str, Enum):
    GENERAL = "general"
    TEEN = "teen"
    MATURE_17 = "mature_17"
    ADULT_18_PLUS = "adult_18_plus"


class ReviewRequirement(str, Enum):
    NOT_REQUIRED = "not_required"
    REQUIRED = "required"
    REQUIRED_FOR_RESTRICTED = "required_for_restricted"
    BLOCKED = "blocked"


class ReviewStatus(str, Enum):
    NOT_SUBMITTED = "not_submitted"
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"
    BLOCKED = "blocked"


@dataclass(frozen=True)
class MediaAssetRef:
    asset_id: str
    path: str
    media_type: str = "video"
    fingerprint: str | None = None
    duration_seconds: float | None = None
    width: int | None = None
    height: int | None = None
    file_size_bytes: int | None = None


@dataclass(frozen=True)
class PlatformAccount:
    account_id: str
    platform_id: str
    display_name: str
    category: PlatformCategory = PlatformCategory.GENERAL
    restricted: bool = False
    credential_ref: str | None = None


@dataclass(frozen=True)
class PublishingChannel:
    channel_id: str
    platform_id: str
    account_id: str
    display_name: str
    default_visibility: PublishingVisibility = PublishingVisibility.PRIVATE
    restricted: bool = False


@dataclass(frozen=True)
class PublishingTarget:
    platform_id: str
    account_id: str
    channel_id: str | None = None
    category: PlatformCategory = PlatformCategory.GENERAL
    visibility: PublishingVisibility = PublishingVisibility.PRIVATE
    platform_overrides: Mapping[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class PublishingMetadata:
    title: str
    description: str = ""
    hashtags: Sequence[str] = field(default_factory=tuple)
    tags: Sequence[str] = field(default_factory=tuple)
    language: str = "en"
    category: str | None = None
    maturity_rating: MaturityRating = MaturityRating.GENERAL
    disclaimer: str | None = None
    platform_overrides: Mapping[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class PublishingSchedule:
    mode: PublishingMode = PublishingMode.MANUAL_HOLD
    scheduled_at_iso: str | None = None
    timezone: str | None = None
    cadence_id: str | None = None
    retry_window_minutes: int | None = None


@dataclass(frozen=True)
class PublishingApproval:
    status: ReviewStatus = ReviewStatus.NOT_SUBMITTED
    reviewer: str | None = None
    reviewed_at_iso: str | None = None
    notes: str | None = None
    block_reasons: Sequence[str] = field(default_factory=tuple)


@dataclass(frozen=True)
class AdultCreatorCompliance:
    enabled: bool = False
    all_participants_18_plus_confirmed: bool = False
    consent_metadata_ref: str | None = None
    age_gate_required: bool = False
    restricted_storage_required: bool = True
    manual_review_required: bool = True
    policy_notes: str | None = None


@dataclass(frozen=True)
class PublishingRequest:
    request_id: str
    media: MediaAssetRef
    target: PublishingTarget
    metadata: PublishingMetadata
    schedule: PublishingSchedule = field(default_factory=PublishingSchedule)
    approval: PublishingApproval = field(default_factory=PublishingApproval)
    adult_compliance: AdultCreatorCompliance = field(default_factory=AdultCreatorCompliance)
    source_job_id: str | None = None
    dry_run: bool = True


@dataclass(frozen=True)
class PublishingResult:
    request_id: str
    status: PublishingStatus
    platform_id: str
    external_id: str | None = None
    external_url: str | None = None
    scheduled_at_iso: str | None = None
    warnings: Sequence[str] = field(default_factory=tuple)
    metadata: Mapping[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class PublishingJob:
    job_id: str
    request: PublishingRequest
    status: PublishingStatus = PublishingStatus.DRAFT
    priority: str = "normal"
    created_at_iso: str | None = None
    updated_at_iso: str | None = None


@dataclass(frozen=True)
class PublishingContext:
    runtime_id: str
    platform_registry_ref: str | None = None
    guardian_enabled: bool = True
    default_review_requirement: ReviewRequirement = ReviewRequirement.REQUIRED
    extra: Mapping[str, Any] = field(default_factory=dict)
