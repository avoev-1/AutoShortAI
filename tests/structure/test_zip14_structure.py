from pathlib import Path


def test_zip14_required_paths_exist():
    root = Path(__file__).resolve().parents[2]
    required = [
        "docs/AutoShortAI_ZIP14_Device_Farm_Deployment/README.md",
        "docs/AutoShortAI_ZIP14_Device_Farm_Deployment/ARCHITECTURE.md",
        "docs/AutoShortAI_ZIP14_Device_Farm_Deployment/DEVICE_FARM_CORE.md",
        "docs/AutoShortAI_ZIP14_Device_Farm_Deployment/PHONE_FARM_READINESS.md",
        "docs/AutoShortAI_ZIP14_Device_Farm_Deployment/ADULT_X_CREATOR_DEVICE_WORKFLOWS.md",
        "src/autoshortai/device_farm/__init__.py",
        "src/autoshortai/device_farm/models.py",
        "src/autoshortai/device_farm/routing.py",
        "src/autoshortai/device_farm/restricted_creator.py",
        "templates/zip14_device_farm/device_farm_profile.template.json",
        "tests/fixtures/restricted_creator_device_policy.example.json",
        "examples/zip14_device_farm_example.py",
    ]
    for relative in required:
        assert (root / relative).exists(), relative
