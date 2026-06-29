from app.modules.missions.domain.mission import CreationMode
from app.modules.missions.services.mission_factory import MissionFactory
from app.modules.missions.services.mission_orchestrator import MissionOrchestrator
from app.modules.workflows.services.template_registry import workflow_template_registry

def test_workflow_template_registry_contains_standard_template() -> None:
    template=workflow_template_registry.get("standard_short_form")
    assert template.template_id=="standard_short_form"
    assert len(template.steps)>=10

def test_mission_factory_creates_assisted_mission() -> None:
    mission=MissionFactory().create("Test Mission", ["youtube","tiktok"], CreationMode.assisted)
    assert mission.title=="Test Mission"
    assert mission.options.platforms==["youtube","tiktok"]

def test_mission_orchestrator_plans_mission() -> None:
    mission=MissionFactory().create("Test", ["youtube"])
    plan=MissionOrchestrator().plan_mission(mission)
    assert plan.template_id=="standard_short_form"
    assert plan.steps[0].step_id=="topic"
    assert plan.metadata["guardian"]["allowed"] is True
    assert "performance" in plan.metadata
