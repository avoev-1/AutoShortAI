"""Contract import tests for ZIP06."""

from autoshortai.asset_pipeline import (
    ApiCostOptimizerContract,
    AssetIdentity,
    AssetKind,
    AssetRegistryContract,
    CacheManagerContract,
    CheckpointSystemContract,
    DependencyGraphContract,
    FingerprintEngineContract,
    IncrementalBuildContract,
    IntegrityCheckerContract,
    PerformanceProfilerContract,
    ProviderContract,
    ResumeEngineContract,
    StorageManagerContract,
)


def test_asset_identity_is_stable() -> None:
    identity = AssetIdentity(namespace="demo", name="script", version="1")
    assert identity.asset_id == "demo:script:1"


def test_contracts_are_importable() -> None:
    assert AssetKind.SCRIPT.value == "script"
    assert AssetRegistryContract is not None
    assert FingerprintEngineContract is not None
    assert DependencyGraphContract is not None
    assert IncrementalBuildContract is not None
    assert CacheManagerContract is not None
    assert ResumeEngineContract is not None
    assert CheckpointSystemContract is not None
    assert IntegrityCheckerContract is not None
    assert StorageManagerContract is not None
    assert ProviderContract is not None
    assert ApiCostOptimizerContract is not None
    assert PerformanceProfilerContract is not None
