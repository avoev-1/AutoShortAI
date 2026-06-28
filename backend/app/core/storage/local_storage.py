from pathlib import Path
from app.core.contracts.storage import StoredObject


class LocalTempStorage:
    def __init__(self, root: Path) -> None:
        self.root = root

    async def save(self, key: str, data: bytes, content_type: str | None = None) -> StoredObject:
        path = self.root / key
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)
        return StoredObject(key=key, uri=str(path), size_bytes=len(data), content_type=content_type)

    async def read(self, key: str) -> bytes:
        return (self.root / key).read_bytes()

    async def delete_temp(self, key: str) -> bool:
        path = self.root / key
        if path.exists():
            path.unlink()
            return True
        return False
