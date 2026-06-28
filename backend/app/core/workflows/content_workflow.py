from app.core.pipeline.models import PipelineStep


def default_short_form_content_workflow() -> list[PipelineStep]:
    return [
        PipelineStep(step_id="research", name="Trend and topic research"),
        PipelineStep(step_id="script", name="Script generation", depends_on=["research"]),
        PipelineStep(step_id="voice", name="Voice generation", depends_on=["script"], estimated_cost_usd=0.01),
        PipelineStep(step_id="visuals", name="Visual asset generation", depends_on=["script"], estimated_cost_usd=0.02),
        PipelineStep(step_id="video", name="Video rendering", depends_on=["voice", "visuals"]),
        PipelineStep(step_id="subtitles", name="Subtitle generation", depends_on=["video"]),
        PipelineStep(step_id="metadata", name="Title, description and tags", depends_on=["script"]),
        PipelineStep(step_id="private_publish", name="Private publication", depends_on=["video", "metadata"], requires_human_approval=True),
        PipelineStep(step_id="analytics", name="Analytics collection", depends_on=["private_publish"]),
        PipelineStep(step_id="learning", name="Learning loop", depends_on=["analytics"]),
    ]
