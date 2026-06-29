from dataclasses import dataclass, field
from enum import StrEnum
from typing import Any
from uuid import uuid4

class CreationMode(StrEnum):
    manual="manual"; assisted="assisted"; semi_auto="semi_auto"; full_auto="full_auto"; expert="expert"

class MissionStatus(StrEnum):
    draft="draft"; planned="planned"; running="running"; paused="paused"; waiting_for_human="waiting_for_human"; completed="completed"; failed="failed"; cancelled="cancelled"

@dataclass
class MissionOptions:
    platforms:list[str]
    language:str="fr"
    target_duration_seconds:int=45
    creation_profile:str="default"
    creation_mode:CreationMode=CreationMode.assisted
    quality_mode:str="balanced"
    max_estimated_cost_usd:float=0.0
    allow_parallel_steps:bool=True
    require_human_approval_before_publish:bool=True
    expert_options:dict[str,Any]=field(default_factory=dict)

@dataclass
class Mission:
    title:str
    options:MissionOptions
    mission_id:str=field(default_factory=lambda: str(uuid4()))
    status:MissionStatus=MissionStatus.draft
    metadata:dict[str,Any]=field(default_factory=dict)
