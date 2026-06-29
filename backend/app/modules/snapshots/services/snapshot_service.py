from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any
from uuid import uuid4

@dataclass(frozen=True)
class MissionSnapshot:
    snapshot_id:str; mission_id:str; stage:str; payload:dict[str,Any]; created_at:str=field(default_factory=lambda: datetime.now(timezone.utc).isoformat())

class SnapshotService:
    def __init__(self)->None: self._snapshots:dict[str,list[MissionSnapshot]]={}
    def create_snapshot(self, mission_id:str, stage:str, payload:dict[str,Any])->MissionSnapshot:
        snapshot=MissionSnapshot(str(uuid4()), mission_id, stage, payload)
        self._snapshots.setdefault(mission_id,[]).append(snapshot)
        return snapshot
    def list_snapshots(self, mission_id:str)->list[MissionSnapshot]:
        return self._snapshots.get(mission_id,[])
