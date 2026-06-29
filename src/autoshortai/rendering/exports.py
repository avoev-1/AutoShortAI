from __future__ import annotations

from dataclasses import dataclass, field
from typing import Mapping, Sequence, Any

from .models import RenderMode, RenderOutput


@dataclass(frozen=True)
class ExportManifest:
    id: str
    project_id: str
    timeline_id: str
    render_profile_id: str
    render_mode: RenderMode
    outputs: Sequence[RenderOutput] = field(default_factory=tuple)
    template_id: str | None = None
    source_asset_refs: Sequence[str] = field(default_factory=tuple)
    created_at: str | None = None
    provider_metadata: Mapping[str, Any] = field(default_factory=dict)
