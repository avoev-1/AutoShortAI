from dataclasses import dataclass, field
from typing import Any

@dataclass(frozen=True)
class ExecutionPlanStep:
    step_id:str; name:str; depends_on:list[str]; can_run_parallel:bool; requires_human_approval:bool; estimated_cost_usd:float

@dataclass(frozen=True)
class ExecutionPlan:
    mission_id:str; template_id:str; steps:list[ExecutionPlanStep]; estimated_total_cost_usd:float; estimated_duration_seconds:int
    warnings:list[str]=field(default_factory=list)
    metadata:dict[str,Any]=field(default_factory=dict)
