def test_zip12_contract_imports():
    from autoshortai.rendering import (
        RenderingCore,
        RenderJob,
        RenderMode,
        VideoProject,
        ZIP12_RENDERING_HOOKS,
        ZIP12_RELEASE,
        basic_short_timeline,
        default_render_profiles,
    )

    assert ZIP12_RELEASE == "ZIP12"
    assert "after_final_render_completed" in ZIP12_RENDERING_HOOKS
    profiles = default_render_profiles()
    assert "youtube_shorts_9x16" in profiles
    assert "tiktok_9x16" in profiles
    assert "generic_vertical_video" in profiles

    timeline = basic_short_timeline(duration_seconds=35)
    project = VideoProject(
        id="project.test",
        title="Test",
        timeline=timeline,
        render_profile_id="generic_vertical_video",
        template_id="short_clean_caption",
    )
    job = RenderJob(id="render.job.test", project=project, mode=RenderMode.DRAFT)
    result = RenderingCore().plan_only_render(job)
    assert result.success is True
    assert result.outputs[0].path.startswith("planned://")
