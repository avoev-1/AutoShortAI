from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class TextGenerationRequest:
    prompt: str
    system_prompt: str | None = None
    temperature: float = 0.7
    max_tokens: int | None = None
    metadata: dict[str, Any] | None = None


@dataclass(frozen=True)
class TextGenerationResult:
    text: str
    provider: str
    model: str | None = None
    estimated_cost_usd: float = 0.0
    raw: dict[str, Any] | None = None


class AIProvider(ABC):
    provider_id: str
    display_name: str

    @abstractmethod
    async def generate_text(self, request: TextGenerationRequest) -> TextGenerationResult:
        raise NotImplementedError
