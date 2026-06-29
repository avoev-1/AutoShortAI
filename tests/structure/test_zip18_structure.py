"""Structure tests for ZIP18.

These tests verify that the ZIP18 architecture files exist after installation.
They do not test production cryptography or real credential storage.
"""

from pathlib import Path


def test_zip18_required_paths_exist():
    root = Path.cwd()
    required = [
        ".autoshort/releases/zip18/README.md",
        "docs/AutoShortAI_ZIP18_Security_Secrets_Credentials_Vault/vault_design.md",
        "docs/AutoShortAI_ZIP18_Security_Secrets_Credentials_Vault/access_control.md",
        "docs/AutoShortAI_ZIP18_Security_Secrets_Credentials_Vault/redaction_policy.md",
        "docs/AutoShortAI_ZIP18_Security_Secrets_Credentials_Vault/restricted_security.md",
        "src/autoshortai/security_vault/__init__.py",
        "src/autoshortai/security_vault/models.py",
        "src/autoshortai/security_vault/contracts.py",
        "src/autoshortai/security_vault/providers.py",
        "src/autoshortai/security_vault/redaction.py",
        "src/autoshortai/security_vault/policies.py",
        "templates/zip18_security_vault/credential_reference.template.json",
        "examples/zip18_secret_reference_example.json",
    ]

    missing = [path for path in required if not (root / path).exists()]
    assert not missing, f"Missing ZIP18 paths: {missing}"


def test_zip18_no_known_token_patterns():
    root = Path.cwd()
    src = root / "src" / "autoshortai" / "security_vault"
    if not src.exists():
        return

    forbidden = [
        "sk-live-",
        "ghp_",
        "AKIA",
        "mandatory cloud",
        "mandatory database",
        "YouTube-only core",
        "OnlyFans-only core",
    ]

    for file_path in src.rglob("*.py"):
        content = file_path.read_text(encoding="utf-8")
        for term in forbidden:
            assert term not in content
