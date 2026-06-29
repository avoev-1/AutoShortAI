from dataclasses import dataclass, field
from app.core.pipeline.models import PipelineStep

@dataclass(frozen=True)
class WorkflowTemplate:
    template_id:str
    name:str
    description:str
    steps:list[PipelineStep]
    supported_modes:list[str]=field(default_factory=list)
    supported_platforms:list[str]=field(default_factory=list)
