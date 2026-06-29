"""ZIP17 workspace hooks.

Hooks keep the workspace plugin-first and avoid hard-coding behavior into the
core.
"""

ZIP17_WORKSPACE_HOOKS: tuple[str, ...] = (
    "before_workspace_created",
    "after_workspace_created",
    "before_project_created",
    "after_project_created",
    "before_media_imported",
    "after_media_imported",
    "before_media_indexed",
    "after_media_indexed",
    "before_export_created",
    "after_export_created",
    "before_archive_created",
    "after_archive_created",
    "before_restricted_workspace_access",
    "after_restricted_workspace_access",
)
