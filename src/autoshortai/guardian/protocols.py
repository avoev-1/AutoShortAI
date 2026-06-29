"""Guardian Engine protocols for ZIP15.

Claude should implement these contracts later without coupling Guardian to product runtime modules.
"""

from __future__ import annotations

from typing import Protocol, Sequence

from .models import GuardianContext, GuardianReport, GuardianResult, GuardianRule


class GuardianCheck(Protocol):
    """A single check that evaluates one Guardian rule."""

    rule: GuardianRule

    def run(self, context: GuardianContext) -> GuardianResult:
        """Run the check against a project context."""
        raise NotImplementedError


class GuardianRulePack(Protocol):
    """A collection of related Guardian checks."""

    name: str

    def checks(self) -> Sequence[GuardianCheck]:
        """Return checks included in this rule pack."""
        raise NotImplementedError


class GuardianEngine(Protocol):
    """Independent Guardian runner.

    This must remain a development/quality layer and must not become product runtime logic.
    """

    def run(self, context: GuardianContext) -> GuardianReport:
        """Run Guardian checks and return a report."""
        raise NotImplementedError
