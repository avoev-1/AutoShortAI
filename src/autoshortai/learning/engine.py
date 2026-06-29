from __future__ import annotations

from dataclasses import dataclass, field
from typing import Sequence

from .confidence import build_confidence_report
from .models import LearningInsight, LearningSignal, LearningSignalType, RiskLevel


@dataclass
class LearningEngine:
    """Lightweight reference learning engine contract.

    This is intentionally simple. Claude can replace or extend this with providers later.
    """

    default_platforms: Sequence[str] = field(default_factory=lambda: ("generic",))

    def extract_basic_signal(self, source_id: str, signal_type: LearningSignalType, strength: float, sample_size: int, platforms: Sequence[str] | None = None) -> LearningSignal:
        return LearningSignal(
            signal_id=f"signal:{source_id}:{signal_type.value}",
            signal_type=signal_type,
            source_ids=(source_id,),
            platforms=tuple(platforms or self.default_platforms),
            strength=strength,
            sample_size=sample_size,
        )

    def generate_basic_insight(self, signal: LearningSignal, title: str, summary: str) -> LearningInsight:
        score = max(0.0, min(1.0, signal.strength))
        confidence = build_confidence_report(score=score, sample_size=signal.sample_size, risk_level=RiskLevel.MEDIUM)
        return LearningInsight(
            insight_id=f"insight:{signal.signal_id}",
            title=title,
            summary=summary,
            signals=(signal,),
            platforms=tuple(signal.platforms),
            confidence=confidence,
        )
