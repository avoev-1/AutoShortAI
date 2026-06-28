from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class PublishPayload:
    title: str
    description: str
    video_path: str
    tags: list[str]
    visibility: str = "private"


@dataclass(frozen=True)
class PublishResult:
    platform: str
    status: str
    external_id: str | None = None
    url: str | None = None
    raw: dict[str, Any] | None = None


class PublisherPlugin(ABC):
    platform_name: str
    display_name: str

    @abstractmethod
    async def authenticate(self) -> bool:
        raise NotImplementedError

    @abstractmethod
    async def upload_private(self, payload: PublishPayload) -> PublishResult:
        raise NotImplementedError

    @abstractmethod
    async def fetch_analytics(self, external_id: str) -> dict[str, Any]:
        raise NotImplementedError
