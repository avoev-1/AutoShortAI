from __future__ import annotations

from dataclasses import dataclass, field
from typing import Mapping, Optional, Sequence


@dataclass(frozen=True)
class FeedbackStrategyLink:
    content_id: str
    strategy_id: str
    creative_profile_id: Optional[str] = None
    variant_id: Optional[str] = None
    platform: str = "generic"
    metadata: Mapping[str, object] = field(default_factory=dict)


@dataclass(frozen=True)
class FeedbackToStrategyMapping:
    links: Sequence[FeedbackStrategyLink] = field(default_factory=tuple)

    def find_by_content(self, content_id: str) -> Sequence[FeedbackStrategyLink]:
        return tuple(link for link in self.links if link.content_id == content_id)
