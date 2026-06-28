from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass(frozen=True)
class StoredObject:
    key: str
    uri: str
    size_bytes: int | None = None
    content_type: str | None = None
    checksum: str | None = None


class StorageProvider(ABC):
    provider_id: str

    @abstractmethod
    async def save(self, key: str, data: bytes, content_type: str | None = None) -> StoredObject:
        raise NotImplementedError

    @abstractmethod
    async def read(self, key: str) -> bytes:
        raise NotImplementedError

    @abstractmethod
    async def delete_temp(self, key: str) -> bool:
        raise NotImplementedError
