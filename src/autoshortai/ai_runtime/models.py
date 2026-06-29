from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Mapping, Sequence


class AIWorkerTaskType(str, Enum):
    SCRIPT_GENERATION = "script_generation"
    VOICE_GENERATION = "voice_generation"
    IMAGE_GENERATION = "image_generation"
    VIDEO_GENERATION = "video_generation"
    SUBTITLE_GENERATION = "subtitle_generation"
    TITLE_GENERATION = "title_generation"
    DESCRIPTION_GENERATION = "description_generation"
    HASHTAG_GENERATION = "hashtag_generation"
    CLASSIFICATION = "classification"
    OPTIMIZATION = "optimization"
    MODERATION = "moderation"
    MANUAL_REVIEW = "manual_review"


class AIWorkerStatus(str, Enum):
    PENDING = "pending"
    ROUTED = "routed"
    RUNNING = "running"
    REVIEW_REQUIRED = "review_required"
    COMPLETED = "completed"
    FAILED = "failed"
    BLOCKED = "blocked"
    CANCELLED = "cancelled"


class ContentMaturityRating(str, Enum):
    GENERAL = "general"
    TEEN = "teen"
    MATURE_18_PLUS = "mature_18_plus"
    RESTRICTED_ADULT = "restricted_adult"


class SafetyReviewLevel(str, Enum):
    NONE = "none"
    BASIC = "basic"
    MANUAL_REVIEW_REQUIRED = "manual_review_required"
    BLOCKED = "blocked"


@dataclass(frozen=True)
class AIWorkerTask:
    id: str
    task_type: AIWorkerTaskType
    prompt_template_id: str
    input_payload: Mapping[str, Any] = field(default_factory=dict)
    required_capabilities: Sequence[str] = field(default_factory=tuple)
    platform_context_id: str = "generic"
    maturity_rating: ContentMaturityRating = ContentMaturityRating.GENERAL
    safety_review_level: SafetyReviewLevel = SafetyReviewLevel.BASIC
    max_cost: float | None = None
    language: str = "fr"
    metadata: Mapping[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class AIWorkerResult:
    task_id: str
    status: AIWorkerStatus
    output_payload: Mapping[str, Any] = field(default_factory=dict)
    provider_id: str | None = None
    worker_id: str | None = None
    estimated_cost: float | None = None
    actual_cost: float | None = None
    safety_review_level: SafetyReviewLevel = SafetyReviewLevel.BASIC
    review_notes: Sequence[str] = field(default_factory=tuple)
    artifacts: Sequence[str] = field(default_factory=tuple)
