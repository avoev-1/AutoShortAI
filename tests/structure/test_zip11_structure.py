from pathlib import Path


def test_zip11_expected_paths_exist():
    root = Path(__file__).resolve().parents[2]
    expected = [
        "docs/AutoShortAI_ZIP11_Lightweight_Control_Dashboard/README.md",
        "docs/AutoShortAI_ZIP11_Lightweight_Control_Dashboard/ARCHITECTURE.md",
        "docs/AutoShortAI_ZIP11_Lightweight_Control_Dashboard/ROADMAP_ZIP11.md",
        "docs/AutoShortAI_ZIP11_Lightweight_Control_Dashboard/CHANGELOG.md",
        "docs/AutoShortAI_ZIP11_Lightweight_Control_Dashboard/SAFETY.md",
        "docs/AutoShortAI_ZIP11_Lightweight_Control_Dashboard/DASHBOARD_CORE.md",
        "docs/AutoShortAI_ZIP11_Lightweight_Control_Dashboard/CONTROL_API_CONTRACTS.md",
        "docs/AutoShortAI_ZIP11_Lightweight_Control_Dashboard/DASHBOARD_VIEW_MODELS.md",
        "docs/AutoShortAI_ZIP11_Lightweight_Control_Dashboard/QUEUE_MONITORING.md",
        "docs/AutoShortAI_ZIP11_Lightweight_Control_Dashboard/ANALYTICS_MONITORING.md",
        "docs/AutoShortAI_ZIP11_Lightweight_Control_Dashboard/LEARNING_MONITORING.md",
        "docs/AutoShortAI_ZIP11_Lightweight_Control_Dashboard/ASSET_MONITORING.md",
        "docs/AutoShortAI_ZIP11_Lightweight_Control_Dashboard/PLATFORM_AGNOSTIC_DASHBOARD.md",
        "docs/AutoShortAI_ZIP11_Lightweight_Control_Dashboard/UI_ADAPTER_LAYER.md",
        "docs/AutoShortAI_ZIP11_Lightweight_Control_Dashboard/INTEGRATION_MAP.md",
        "docs/AutoShortAI_ZIP11_Lightweight_Control_Dashboard/HOOKS.md",
        "src/autoshortai/dashboard/__init__.py",
        "src/autoshortai/dashboard/models.py",
        "src/autoshortai/dashboard/contracts.py",
        "src/autoshortai/dashboard/core.py",
        "src/autoshortai/dashboard/actions.py",
        "src/autoshortai/dashboard/adapters.py",
        "src/autoshortai/dashboard/monitoring.py",
        "src/autoshortai/dashboard/platforms.py",
        "src/autoshortai/dashboard/panels.py",
        "src/autoshortai/dashboard/hooks.py",
        "src/autoshortai/dashboard/errors.py",
        "src/autoshortai/dashboard/version.py",
        "templates/zip11_dashboard/dashboard_layout.template.json",
        "tests/fixtures/zip11_dashboard_snapshot.example.json",
        "examples/zip11_dashboard_example.py",
    ]
    for path in expected:
        assert (root / path).exists(), path


def test_zip11_platform_agnostic_terms_are_documented():
    root = Path(__file__).resolve().parents[2]
    architecture = (root / "docs/AutoShortAI_ZIP11_Lightweight_Control_Dashboard/ARCHITECTURE.md").read_text(encoding="utf-8")
    assert "platform-agnostic" in architecture
    assert "TikTok" in architecture
    assert "YouTube Shorts" in architecture
