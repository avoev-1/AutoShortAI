from __future__ import annotations

from .models import ReleaseChecklist, ReleaseChecklistItem, ReleaseGateStatus


def default_beta_release_checklist() -> ReleaseChecklist:
    items = (
        ReleaseChecklistItem("guardian", "Guardian check passed", True),
        ReleaseChecklistItem("verify", "All VERIFY scripts passed", True),
        ReleaseChecklistItem("imports", "Python imports valid", True),
        ReleaseChecklistItem("secrets", "No secrets committed or logged", True),
        ReleaseChecklistItem("platform_agnostic", "No single-platform lock-in", True),
        ReleaseChecklistItem("dependencies", "No heavy dependency made mandatory", True),
        ReleaseChecklistItem("restricted_default", "Restricted creator mode disabled by default", True),
        ReleaseChecklistItem("docs", "Docs and roadmaps updated", True),
        ReleaseChecklistItem("compatibility", "ZIP01-ZIP20 compatibility preserved", True),
    )
    return ReleaseChecklist(id="zip20_beta_release_checklist", items=items)


def mark_item_passed(item: ReleaseChecklistItem, note: str = "") -> ReleaseChecklistItem:
    return ReleaseChecklistItem(
        id=item.id,
        title=item.title,
        required=item.required,
        status=ReleaseGateStatus.PASSED,
        notes=note,
    )
