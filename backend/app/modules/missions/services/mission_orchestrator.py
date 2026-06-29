from app.modules.execution.domain.execution_plan import ExecutionPlan
from app.modules.execution.services.execution_planner import ExecutionPlanner
from app.modules.guardian_hooks.services.guardian_hook import GuardianHook
from app.modules.missions.domain.mission import Mission
from app.modules.performance.services.performance_estimator import PerformanceEstimator
from app.modules.workflows.services.template_registry import workflow_template_registry

class MissionOrchestrator:
    def __init__(self)->None:
        self.planner=ExecutionPlanner(); self.performance=PerformanceEstimator(); self.guardian=GuardianHook()
    def plan_mission(self, mission:Mission, template_id:str="standard_short_form")->ExecutionPlan:
        template=workflow_template_registry.get(template_id)
        plan=self.planner.plan(mission, template)
        guardian=self.guardian.pre_execution_check(mission.mission_id, [step.step_id for step in plan.steps])
        perf=self.performance.estimate(len(plan.steps), mission.options.quality_mode)
        plan.metadata["guardian"]={"allowed":guardian.allowed,"score":guardian.score,"messages":guardian.messages}
        plan.metadata["performance"]={"estimated_duration_seconds":perf.estimated_duration_seconds,"estimated_storage_mb":perf.estimated_storage_mb,"recommendation":perf.recommendation,"confidence":perf.confidence}
        return plan
