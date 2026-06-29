from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping


@dataclass(frozen=True)
class PromptTemplateRef:
    id: str
    path: str
    version: str = "1.0"
    metadata: Mapping[str, str] | None = None


DEFAULT_PROMPT_TEMPLATES = {
    "script_generation": "templates/zip13_ai_runtime/script_generation.template.md",
    "voice_prompt": "templates/zip13_ai_runtime/voice_prompt.template.md",
    "image_prompt": "templates/zip13_ai_runtime/image_prompt.template.md",
    "video_prompt": "templates/zip13_ai_runtime/video_prompt.template.md",
    "title_generation": "templates/zip13_ai_runtime/title_generation.template.md",
    "description_generation": "templates/zip13_ai_runtime/description_generation.template.md",
    "hashtag_generation": "templates/zip13_ai_runtime/hashtag_generation.template.md",
    "moderation_review": "templates/zip13_ai_runtime/moderation_review.template.md",
    "restricted_platform_review": "templates/zip13_ai_runtime/restricted_platform_review.template.md",
}
