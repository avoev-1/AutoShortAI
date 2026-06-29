from autoshortai.rendering import (
    RenderJob,
    RenderMode,
    RenderingCore,
    VideoProject,
    basic_short_timeline,
)


def main() -> None:
    timeline = basic_short_timeline(duration_seconds=35)
    project = VideoProject(
        id="project.demo.short",
        title="Demo Short",
        timeline=timeline,
        render_profile_id="generic_vertical_video",
        template_id="short_clean_caption",
    )
    job = RenderJob(id="render.job.demo", project=project, mode=RenderMode.DRAFT)
    result = RenderingCore().plan_only_render(job)
    print(result)


if __name__ == "__main__":
    main()
