# ZIP17 Architecture — Local Workspace & Media Library

## 1. Position in AutoShortAI

ZIP17 adds the local organization layer.

It is not the asset registry from ZIP06.
It is not the renderer from ZIP12.
It is not the publisher from ZIP16.
It is not the dashboard from ZIP11.

ZIP17 answers:

```text
Where is everything stored locally?
How are projects organized?
How are media files indexed?
How are drafts, versions, exports and manifests tracked?
How is restricted creator content isolated?
```

## 2. Core boundary

The workspace layer owns:

- project manifests
- local project folder conventions
- media library item metadata
- project-level import and export contracts
- local versioning metadata
- search and tag indexing contracts
- restricted workspace isolation contracts

The workspace layer does not own:

- provider cache internals
- rendering implementation
- publishing implementation
- AI provider implementation
- analytics collection
- secrets vault
- cloud sync
- heavy UI

## 3. High-level flow

```text
AI Worker / Import
        ↓
ZIP06 Asset Pipeline
        ↓
ZIP17 Local Workspace & Media Library
        ↓
ZIP12 Video Rendering Pipeline
        ↓
ZIP16 Multi-Platform Publishing Runtime
        ↓
ZIP09 Analytics
        ↓
ZIP10 Learning
```

## 4. Workspace structure

Recommended local layout:

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

This is a contract, not a forced implementation.

## 5. Project organization axes

Projects can be organized by:

- platform target
- campaign
- niche
- creative profile
- production status
- maturity rating
- language
- creation date
- publishing date
- performance score
- restricted/general mode

The core must not hard-code YouTube-specific assumptions. Platform-specific data belongs to platform adapters or metadata profiles.

## 6. Media Library

The media library tracks assets at a human/project level:

- scripts
- images
- video clips
- audio
- subtitles
- thumbnails
- metadata files
- render exports
- publishing packages

It references ZIP06 asset identities where available, but it does not replace ZIP06 fingerprints, cache or integrity checks.

## 7. Versioning

ZIP17 uses lightweight versioning contracts:

```text
draft_v1
draft_v2
final_v1
final_youtube_shorts
final_tiktok
final_instagram_reels
```

A version can point to:

- files
- manifests
- render outputs
- platform-specific export packages
- notes
- review status

No heavy VCS or database is required.

## 8. Import / Export

ZIP17 prepares contracts for:

- importing one file
- importing a folder
- importing generated assets
- exporting a project package
- exporting a platform publishing package
- archiving a project
- restoring a project

Export packages must include enough metadata for ZIP16 to publish safely.

## 9. Restricted / Adult Creator Workspace

Restricted creator workspaces are a dedicated opt-in category.

Rules:

- disabled by default
- isolated from general workspace
- separate project roots
- separate media indexes
- separate logs
- explicit maturity rating required
- consent metadata required
- all participants must be 18+
- manual review required by default
- no illegal, non-consensual or underage content
- no automatic unsafe publishing

This supports future adult creator platforms without making the core adult-only.

## 10. Integrations

### ZIP06 — Smart Asset Pipeline

ZIP17 can reference:

- asset ids
- fingerprints
- storage locations
- cache status
- integrity status

### ZIP11 — Dashboard

ZIP17 exposes view models for:

- project browser
- media library status
- recent exports
- storage usage
- restricted workspace status

### ZIP12 — Rendering

ZIP17 stores:

- timeline manifests
- draft renders
- final renders
- subtitle files
- thumbnails
- export manifests

### ZIP16 — Publishing

ZIP17 prepares:

- platform packages
- metadata bundles
- review status
- publishing target references

### ZIP15 — Guardian

Guardian must check:

- workspace stays local-first
- no platform lock-in
- no restricted/general content mixing
- no secrets in manifests
- no forced database/cloud dependency
