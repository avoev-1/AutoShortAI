# AutoShortAI ZIP17 — Local Workspace & Media Library

ZIP17 defines the architecture for a local-first workspace and media library layer.

This release does not implement a full media manager. It provides architecture, contracts, models, hooks, templates, examples, install/verify scripts, and structural tests so Claude can later implement the real system without changing the project philosophy.

## Purpose

AutoShortAI must be able to organize every file it creates or consumes:

- video projects
- scripts
- voiceovers
- images
- music
- subtitles
- thumbnails
- exports
- platform metadata
- drafts and final versions
- generated assets and imported assets
- general content
- restricted / adult creator content in an isolated opt-in workspace

## Design rules

- Local-first by default.
- No mandatory cloud dependency.
- No mandatory database.
- No SaaS assumption.
- No platform lock-in.
- YouTube Shorts is a first target, never the only target.
- Workspace logic must remain separate from asset caching, publishing, rendering, analytics, and AI workers.
- Restricted / adult creator workspaces must be opt-in, isolated, consent-aware, 18+ only, and manually reviewed by default.

## Installed areas

The installer merges this ZIP into an existing AutoShortAI repository:

```text
.autoshort/releases/zip17/
docs/AutoShortAI_ZIP17_Local_Workspace_Media_Library/
src/autoshortai/workspace/
templates/zip17_workspace/
tests/structure/test_zip17_structure.py
tests/fixtures/zip17_expected_files.txt
examples/zip17_workspace_manifest_example.json
examples/zip17_project_layout_example.md
```

## Workflow

Run from the repository root:

```bash
bash ~/Bureau/Projects/Archives/AutoShortAI_ZIP17_Local_Workspace_Media_Library/INSTALL.sh
bash ~/Bureau/Projects/Archives/AutoShortAI_ZIP17_Local_Workspace_Media_Library/VERIFY.sh
```

Then commit:

```bash
git add .
git commit -m "feat(zip17): local workspace media library"
git push origin main
```
