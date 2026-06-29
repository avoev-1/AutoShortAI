# Workspace Layout

ZIP17 defines a local-first workspace layout.

Recommended structure:

```text
workspace/
  projects/
    <project_id>/
      project.manifest.json
      scripts/
      audio/
      images/
      video/
      subtitles/
      thumbnails/
      metadata/
      exports/
      reports/
      versions/
  library/
    media.index.json
    collections/
    tags/
  restricted/
    projects/
    library/
    manifests/
```

The structure is a contract for future implementation. It is not a required final filesystem implementation.

## Rules

- Project folders must be portable.
- Platform-specific exports must be stored as packages, not hard-coded into the core.
- General and restricted workspaces must remain separate.
- Workspace manifests must never contain raw secrets.
