"""Experiment tracking contracts for ZIP09."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Mapping


@dataclass(frozen=True)
class ExperimentVariant:
    variant_id: str
    label: str
    creative_profile_id: str | None = None
    hook_id: str | None = None
    metadata: Mapping[str, str] = field(default_factory=dict)


@dataclass(frozen=True)
class Experiment:
    experiment_id: str
    name: str
    variants: tuple[ExperimentVariant, ...]
    target_platforms: tuple[str, ...] = field(default_factory=tuple)
    objective: str | None = None


@dataclass(frozen=True)
class VariantPerformance:
    variant_id: str
    platform: str
    score: float | None = None
    metric_summary: Mapping[str, float] = field(default_factory=dict)


@dataclass(frozen=True)
class ExperimentResult:
    experiment_id: str
    variant_performances: tuple[VariantPerformance, ...] = field(default_factory=tuple)
    winner_variant_id: str | None = None
    confidence: float = 0.0
