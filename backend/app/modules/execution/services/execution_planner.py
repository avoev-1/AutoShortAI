from app.core.pipeline.graph import PipelineGraph
from app.modules.execution.domain.execution_plan import ExecutionPlan, ExecutionPlanStep
from app.modules.missions.domain.mission import Mission
from app.modules.workflows.domain.workflow_template import WorkflowTemplate

class ExecutionPlanner:
    def plan(self, mission:Mission, template:WorkflowTemplate)->ExecutionPlan:
        ordered=PipelineGraph(template.steps).execution_order()
        cost=sum(step.estimated_cost_usd for step in ordered)
        base=len(ordered)*20
        estimated=int(base*0.65) if mission.options.quality_mode=="fast" else int(base*1.6) if mission.options.quality_mode=="quality" else base
        warnings=[]
        if cost > mission.options.max_estimated_cost_usd: warnings.append("estimated_cost_exceeds_mission_limit")
        return ExecutionPlan(
            mission_id=mission.mission_id, template_id=template.template_id,
            steps=[ExecutionPlanStep(step.step_id, step.name, step.depends_on, mission.options.allow_parallel_steps and bool(step.depends_on), step.requires_human_approval, step.estimated_cost_usd) for step in ordered],
            estimated_total_cost_usd=cost, estimated_duration_seconds=estimated, warnings=warnings,
            metadata={"creation_mode":mission.options.creation_mode, "quality_mode":mission.options.quality_mode, "platforms":mission.options.platforms},
        )
