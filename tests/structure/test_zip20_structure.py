from pathlib import Path


def test_zip20_expected_files_exist():
    root = Path.cwd()
    expected_file = root / "tests" / "fixtures" / "zip20_expected_files.txt"
    assert expected_file.exists(), "zip20 expected file fixture missing"
    expected = [line.strip() for line in expected_file.read_text(encoding="utf-8").splitlines() if line.strip()]
    missing = [path for path in expected if not (root / path).exists()]
    assert not missing, f"Missing ZIP20 files: {missing}"


def test_zip20_release_governance_imports():
    from autoshortai.release_governance import (
        default_beta_release_checklist,
        default_module_stability_matrix,
        default_platform_agnostic_policy,
        default_restricted_creator_governance_policy,
    )

    assert len(default_beta_release_checklist().items) >= 8
    assert len(default_module_stability_matrix().entries) >= 20
    assert default_platform_agnostic_policy().no_platform_lock_in is True
    assert default_restricted_creator_governance_policy().enabled_by_default is False


def test_zip20_restricted_creator_is_not_default_enabled():
    root = Path.cwd()
    restricted_template = root / "templates" / "zip20_release_governance" / "restricted_creator_governance.template.yaml"
    content = restricted_template.read_text(encoding="utf-8")
    forbidden = [
        "enabled_by_default: true",
        "manual_review_required: false",
        "consent_metadata_required: false",
        "all_participants_18_plus_required: false",
    ]
    for term in forbidden:
        assert term not in content


def test_zip20_platform_governance_not_youtube_only():
    root = Path.cwd()
    doc = root / "docs" / "AutoShortAI_ZIP20_Beta_Stabilization_Release_Governance" / "platform_agnostic_governance.md"
    content = doc.read_text(encoding="utf-8").lower()
    assert "not youtube-only" in content or "not youtube only" in content or "youtube shorts is a first target" in content
    assert "tiktok" in content
    assert "instagram" in content
