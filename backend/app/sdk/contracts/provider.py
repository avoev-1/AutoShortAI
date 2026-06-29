from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class ProviderHealth:
    provider_id: str
    healthy: bool
    message: str = ""


class SDKProvider(ABC):
    provider_id: str
    display_name: str

    @abstractmethod
    async def healthcheck(self) -> ProviderHealth:
        raise NotImplementedError

    @abstractmethod
    def capabilities(self) -> list[str]:
        raise NotImplementedError

    @abstractmethod
    def metadata(self) -> dict[str, Any]:
        raise NotImplementedError
