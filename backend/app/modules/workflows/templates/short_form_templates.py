from app.core.pipeline.models import PipelineStep
from app.modules.workflows.domain.workflow_template import WorkflowTemplate

def standard_short_form_template() -> WorkflowTemplate:
    return WorkflowTemplate(
        template_id="standard_short_form", name="Standard Short Form Content",
        description="Default workflow for short-form content generation.",
        supported_modes=["manual","assisted","semi_auto","full_auto","expert"],
        supported_platforms=["youtube","tiktok","instagram"],
        steps=[
            PipelineStep(step_id="topic", name="Topic selection"),
            PipelineStep(step_id="research", name="Research", depends_on=["topic"]),
            PipelineStep(step_id="script", name="Script generation", depends_on=["research"]),
            PipelineStep(step_id="voice", name="Voice generation", depends_on=["script"], estimated_cost_usd=0.01),
            PipelineStep(step_id="visuals", name="Visual generation", depends_on=["script"], estimated_cost_usd=0.02),
            PipelineStep(step_id="edit", name="Video editing", depends_on=["voice","visuals"]),
            PipelineStep(step_id="subtitles", name="Subtitle generation", depends_on=["edit"]),
            PipelineStep(step_id="metadata", name="Metadata generation", depends_on=["script"]),
            PipelineStep(step_id="approval", name="Human approval", depends_on=["subtitles","metadata"], requires_human_approval=True),
            PipelineStep(step_id="private_publish", name="Private publishing", depends_on=["approval"]),
            PipelineStep(step_id="analytics", name="Analytics collection", depends_on=["private_publish"]),
            PipelineStep(step_id="learning", name="Learning update", depends_on=["analytics"]),
        ],
    )

def fast_draft_template() -> WorkflowTemplate:
    return WorkflowTemplate(
        template_id="fast_draft", name="Fast Draft", description="Quick draft workflow.",
        supported_modes=["manual","assisted","expert"], supported_platforms=["youtube","tiktok","instagram"],
        steps=[PipelineStep(step_id="topic", name="Topic selection"), PipelineStep(step_id="script", name="Script generation", depends_on=["topic"]), PipelineStep(step_id="draft_preview", name="Draft preview", depends_on=["script"])],
    )
