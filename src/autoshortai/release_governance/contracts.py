from __future__ import annotations

from typing import Protocol, Sequence

from .models import (
    GovernanceReport,
    ModuleStabilityMatrix,
    ReleaseCandidate,
    ReleaseGate,
    ReleaseRisk,
)


class ReleaseGateChecker(Protocol):
    """Checks one release gate without mutating the project."""

    def check(self, candidate: ReleaseCandidate) -> ReleaseGate:
        ...


class ReleaseGovernanceRuntime(Protocol):
    """Coordinates release governance checks."""

    def evaluate_candidate(self, candidate: ReleaseCandidate) -> GovernanceReport:
        ...


class ModuleStabilityEvaluator(Protocol):
    """Builds or updates the module stability matrix."""

    def evaluate(self) -> ModuleStabilityMatrix:
        ...


class RiskRegistry(Protocol):
    """Provides known release risks."""

    def list_risks(self, candidate: ReleaseCandidate) -> Sequence[ReleaseRisk]:
        ...


class CompatibilityGuard(Protocol):
    """Verifies ZIP01-ZIP20 backward compatibility."""

    def check_candidate(self, candidate: ReleaseCandidate) -> ReleaseGate:
        ...


class GovernanceReporter(Protocol):
    """Writes human-readable and machine-readable governance reports."""

    def write_report(self, report: GovernanceReport) -> None:
        ...
