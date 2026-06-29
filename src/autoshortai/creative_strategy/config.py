"""Configuration contracts for ZIP07 Creative Strategy Engine."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Mapping, Sequence


@dataclass(frozen=True)
class CreativeStrategyConfig:
    """Declarative configuration for future implementations."""

    default_profile_id: str = "youtube_shorts_default"
    max_variants_per_request: int = 3
    enable_quality_scoring: bool = True
    enable_rule_validation: bool = True
    enabled_hooks: Sequence[str] = field(default_factory=tuple)
    metadata: Mapping[str, str] = field(default_factory=dict)
