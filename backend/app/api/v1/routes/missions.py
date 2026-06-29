from fastapi import APIRouter
from pydantic import BaseModel, Field
from app.modules.missions.domain.mission import CreationMode
from app.modules.missions.services.mission_factory import MissionFactory
from app.modules.missions.services.mission_orchestrator import MissionOrchestrator
from app.modules.workflows.services.template_registry import workflow_template_registry

router=APIRouter()

class MissionPlanRequest(BaseModel):
    title:str=Field(default="Demo Mission")
    platforms:list[str]=Field(default_factory=lambda:["youtube"])
    creation_mode:CreationMode=CreationMode.assisted
    template_id:str="standard_short_form"
    target_duration_seconds:int=45
    creation_profile:str="default"

@router.get("/templates")
async def list_templates()->dict[str,object]:
    return {"templates":[{"template_id":t.template_id,"name":t.name,"description":t.description,"supported_modes":t.supported_modes,"supported_platforms":t.supported_platforms,"step_count":len(t.steps)} for t in workflow_template_registry.list_templates()]}

@router.post("/plan")
async def plan_mission(request:MissionPlanRequest)->dict[str,object]:
    mission=MissionFactory().create(request.title, request.platforms, request.creation_mode, request.target_duration_seconds, request.creation_profile)
    plan=MissionOrchestrator().plan_mission(mission, request.template_id)
    return {"mission_id":plan.mission_id,"template_id":plan.template_id,"estimated_total_cost_usd":plan.estimated_total_cost_usd,"estimated_duration_seconds":plan.estimated_duration_seconds,"warnings":plan.warnings,"metadata":plan.metadata,"steps":[{"step_id":s.step_id,"name":s.name,"depends_on":s.depends_on,"can_run_parallel":s.can_run_parallel,"requires_human_approval":s.requires_human_approval,"estimated_cost_usd":s.estimated_cost_usd} for s in plan.steps]}
