from pathlib import Path


def test_zip12_expected_paths_exist():
    root = Path(__file__).resolve().parents[2]
    expected = [
        "docs/AutoShortAI_ZIP12_Video_Rendering_Pipeline/README.md",
        "docs/AutoShortAI_ZIP12_Video_Rendering_Pipeline/ARCHITECTURE.md",
        "docs/AutoShortAI_ZIP12_Video_Rendering_Pipeline/ROADMAP_ZIP12.md",
        "docs/AutoShortAI_ZIP12_Video_Rendering_Pipeline/CHANGELOG.md",
        "docs/AutoShortAI_ZIP12_Video_Rendering_Pipeline/SAFETY.md",
        "docs/AutoShortAI_ZIP12_Video_Rendering_Pipeline/TIMELINE_ENGINE.md",
        "docs/AutoShortAI_ZIP12_Video_Rendering_Pipeline/MULTI_PLATFORM_RENDER_PROFILES.md",
        "docs/AutoShortAI_ZIP12_Video_Rendering_Pipeline/TEMPLATE_RENDERING_SYSTEM.md",
        "docs/AutoShortAI_ZIP12_Video_Rendering_Pipeline/SUBTITLE_CAPTION_CONTRACTS.md",
        "docs/AutoShortAI_ZIP12_Video_Rendering_Pipeline/AUDIO_LAYER_CONTRACTS.md",
        "docs/AutoShortAI_ZIP12_Video_Rendering_Pipeline/RENDER_WORKER_CONTRACTS.md",
        "docs/AutoShortAI_ZIP12_Video_Rendering_Pipeline/DRAFT_FINAL_RENDERING.md",
        "docs/AutoShortAI_ZIP12_Video_Rendering_Pipeline/EXPORT_MANIFESTS.md",
        "docs/AutoShortAI_ZIP12_Video_Rendering_Pipeline/RESOURCE_AND_CHECKPOINT_INTEGRATION.md",
        "docs/AutoShortAI_ZIP12_Video_Rendering_Pipeline/PLATFORM_AGNOSTIC_RENDERING.md",
        "docs/AutoShortAI_ZIP12_Video_Rendering_Pipeline/HOOKS.md",
        "docs/AutoShortAI_ZIP12_Video_Rendering_Pipeline/INTEGRATION_MAP.md",
        "src/autoshortai/rendering/__init__.py",
        "src/autoshortai/rendering/models.py",
        "src/autoshortai/rendering/profiles.py",
        "src/autoshortai/rendering/subtitles.py",
        "src/autoshortai/rendering/audio.py",
        "src/autoshortai/rendering/templates.py",
        "src/autoshortai/rendering/exports.py",
        "src/autoshortai/rendering/workers.py",
        "src/autoshortai/rendering/contracts.py",
        "src/autoshortai/rendering/timeline.py",
        "src/autoshortai/rendering/resources.py",
        "src/autoshortai/rendering/render_core.py",
        "src/autoshortai/rendering/hooks.py",
        "src/autoshortai/rendering/errors.py",
        "src/autoshortai/rendering/version.py",
        "templates/zip12_rendering/render_profile.template.json",
        "templates/zip12_rendering/video_timeline.template.json",
        "templates/zip12_rendering/visual_template.template.json",
        "templates/zip12_rendering/caption_style.template.json",
        "templates/zip12_rendering/audio_mix_policy.template.json",
        "templates/zip12_rendering/export_manifest.template.json",
        "templates/zip12_rendering/render_job.template.json",
        "templates/zip12_rendering/resource_budget.template.json",
        "tests/fixtures/zip12_render_plan.example.json",
        "examples/zip12_rendering_example.py",
        "examples/zip12_render_plan_example.json",
    ]
    for path in expected:
        assert (root / path).exists(), path


def test_zip12_platform_agnostic_terms_are_documented():
    root = Path(__file__).resolve().parents[2]
    architecture = (root / "docs/AutoShortAI_ZIP12_Video_Rendering_Pipeline/ARCHITECTURE.md").read_text(encoding="utf-8")
    assert "platform-agnostic" in architecture
    assert "YouTube Shorts" in architecture
    assert "TikTok" in architecture
    assert "Instagram Reels" in architecture
