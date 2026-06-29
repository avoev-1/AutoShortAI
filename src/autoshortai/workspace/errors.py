"""ZIP17 workspace errors."""


class WorkspaceError(Exception):
    """Base workspace error."""


class WorkspaceManifestError(WorkspaceError):
    """Invalid workspace manifest."""


class MediaLibraryError(WorkspaceError):
    """Invalid media library operation."""


class RestrictedWorkspaceError(WorkspaceError):
    """Restricted workspace safeguard violation."""


class WorkspaceExportError(WorkspaceError):
    """Export package failure."""


class WorkspaceImportError(WorkspaceError):
    """Import failure."""
