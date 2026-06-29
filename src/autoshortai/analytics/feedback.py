"""Feedback loop contracts for ZIP09."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Mapping


class FeedbackSeverity(str, Enum):
    INFO = "info"
    WARNING = "warning"
    OPPORTUNITY = "opportunity"
    RISK = "risk"


@dataclass(frozen=True)
class FeedbackItem:
    message: str
    severity: FeedbackSeverity = FeedbackSeverity.INFO
    platform: str | None = None
    metric: str | None = None
    confidence: float = 1.0
    metadata: Mapping[str, str] = field(default_factory=dict)


@dataclass(frozen=True)
class FeedbackReport:
    report_id: str
    content_id: str
    items: tuple[FeedbackItem, ...] = field(default_factory=tuple)
    summary: str | None = None
    machine_readable_tags: tuple[str, ...] = field(default_factory=tuple)
