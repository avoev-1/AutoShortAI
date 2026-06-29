from __future__ import annotations

from typing import Iterable, Sequence

from .models import AdaptationAction, AdaptationSuggestion, LearningInsight
from .policies import AdaptationPolicy, AdaptationPolicyMode


def suggest_from_insight(insight: LearningInsight, target_ref: str, action: AdaptationAction = AdaptationAction.TEST_MORE) -> AdaptationSuggestion:
    return AdaptationSuggestion(
        suggestion_id=f"suggestion:{insight.insight_id}:{target_ref}",
        target_ref=target_ref,
        action=action,
        rationale=insight.summary,
        platforms=tuple(insight.platforms),
        confidence=insight.confidence,
        proposed_delta={"source_insight": insight.insight_id},
        reversible=True,
    )


def plan_suggestions(insights: Iterable[LearningInsight], target_ref: str, policy: AdaptationPolicy) -> Sequence[AdaptationSuggestion]:
    if policy.mode == AdaptationPolicyMode.LOCKED or target_ref in policy.locked_targets:
        return ()
    return tuple(suggest_from_insight(insight, target_ref) for insight in insights)
