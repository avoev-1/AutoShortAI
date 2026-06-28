from abc import ABC, abstractmethod


class AIProviderPlugin(ABC):
    provider_name: str

    @abstractmethod
    async def generate_text(self, prompt: str) -> str:
        raise NotImplementedError


class VoiceProviderPlugin(ABC):
    provider_name: str

    @abstractmethod
    async def generate_voice(self, text: str) -> bytes:
        raise NotImplementedError


class VideoEnginePlugin(ABC):
    engine_name: str

    @abstractmethod
    async def render_vertical_video(self, project_id: str) -> str:
        raise NotImplementedError
