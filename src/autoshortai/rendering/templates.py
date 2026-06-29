from __future__ import annotations

from dataclasses import dataclass, field
from typing import Mapping, Sequence, Any


@dataclass(frozen=True)
class VisualTemplate:
    id: str
    label: str
    supported_profile_ids: Sequence[str] = field(default_factory=tuple)
    caption_style_id: str | None = None
    safe_zone_policy: str = "profile_default"
    metadata: Mapping[str, Any] = field(default_factory=dict)


def default_visual_templates() -> tuple[VisualTemplate, ...]:
    return (
        VisualTemplate(id="short_clean_caption", label="Short Clean Caption"),
        VisualTemplate(id="dark_motivation", label="Dark Motivation"),
        VisualTemplate(id="news_fast_cut", label="News Fast Cut"),
        VisualTemplate(id="gaming_clip_overlay", label="Gaming Clip Overlay"),
        VisualTemplate(id="documentary_micro_story", label="Documentary Micro Story"),
        VisualTemplate(id="finance_explainer", label="Finance Explainer"),
        VisualTemplate(id="ai_news_vertical", label="AI News Vertical"),
    )
