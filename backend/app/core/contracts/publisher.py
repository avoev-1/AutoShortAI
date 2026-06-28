from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class PublicationAsset:
    video_path: str
    title: str
    description: str
    tags: list[str]
    thumbnail_path: str | None = None
    language: str = "fr"


@dataclass(frozen=True)
class PublicationRequest:
    asset: PublicationAsset
    platform: str
    visibility: str = "private"
    schedule_at: str | None = None
    metadata: dict[str, Any] | None = None


@dataclass(frozen=True)
class PublicationResult:
    platform: str
    status: str
    external_id: str | None = None
    url: str | None = None
    raw: dict[str, Any] | None = None


class Publisher(ABC):
    publisher_id: str
    display_name: str

    @abstractmethod
    async def publish_private(self, request: PublicationRequest) -> PublicationResult:
        raise NotImplementedError

    @abstractmethod
    async def fetch_analytics(self, external_id: str) -> dict[str, Any]:
        raise NotImplementedError
