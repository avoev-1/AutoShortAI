from pathlib import Path


def test_zip05_scaffold_exists():
    root = Path(__file__).resolve().parents[1]
    assert (root / "src" / "autoshortai" / "distribution").exists()
