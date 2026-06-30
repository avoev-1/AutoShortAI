from __future__ import annotations

from .models import ReleaseGate, ReleaseGateStatus


def default_release_gates() -> tuple[ReleaseGate, ...]:
    return (
        ReleaseGate("guardian", "Guardian architecture check", ReleaseGateStatus.PENDING, True),
        ReleaseGate("verify", "Repository VERIFY scripts", ReleaseGateStatus.PENDING, True),
        ReleaseGate("vault", "Secrets and credential hygiene", ReleaseGateStatus.PENDING, True),
        ReleaseGate("packaging", "Packaging verification", ReleaseGateStatus.PENDING, True),
        ReleaseGate("compatibility", "ZIP01-ZIP20 compatibility", ReleaseGateStatus.PENDING, True),
        ReleaseGate("restricted", "Restricted workflow isolation", ReleaseGateStatus.PENDING, True),
        ReleaseGate("platform", "Platform-agnostic enforcement", ReleaseGateStatus.PENDING, True),
    )
