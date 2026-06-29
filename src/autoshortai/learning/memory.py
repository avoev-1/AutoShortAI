from __future__ import annotations

import json
from dataclasses import asdict, is_dataclass
from pathlib import Path
from typing import Sequence

from .models import LearningInsight


def _json_default(value):
    if is_dataclass(value):
        return asdict(value)
    if hasattr(value, "value"):
        return value.value
    if isinstance(value, tuple):
        return list(value)
    raise TypeError(f"Object is not JSON serializable: {value!r}")


class JsonLearningMemoryStore:
    """Simple local JSON learning memory.

    This is a reference storage adapter, not a mandatory persistence backend.
    """

    def __init__(self, path: str | Path):
        self.path = Path(path)

    def save_insight(self, insight: LearningInsight) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        records = []
        if self.path.exists():
            records = json.loads(self.path.read_text(encoding="utf-8"))
        records.append(json.loads(json.dumps(insight, default=_json_default)))
        self.path.write_text(json.dumps(records, indent=2, sort_keys=True), encoding="utf-8")

    def list_raw_records(self) -> Sequence[dict]:
        if not self.path.exists():
            return ()
        return tuple(json.loads(self.path.read_text(encoding="utf-8")))
