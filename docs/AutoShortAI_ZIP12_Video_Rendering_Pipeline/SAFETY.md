# SAFETY — ZIP12 Video Rendering Pipeline

## Rendering Safety Rules

Rendering can become CPU/RAM intensive. ZIP12 must preserve lightweight and controlled execution.

## Resource Safety

A future implementation must respect:

- CPU budget
- RAM budget
- maximum render duration
- maximum simultaneous renders
- draft/final render separation
- queue scheduling constraints

## Provider Safety

The core must not require one rendering provider.

Allowed future providers may include:

- FFmpeg
- MoviePy
- OpenCV
- native renderer
- external renderer provider

But they must be adapter/provider implementations, not core dependencies.

## Platform Safety

No platform-specific hard-coding in the rendering core.

Render profiles must handle platform differences through metadata and capability contracts.

## Asset Safety

Rendering must validate assets through ZIP06 integrity and storage contracts before final export.

## Resume Safety

Long renders should be resumable through checkpoints and cached intermediate artifacts when implemented.

## Output Safety

Export manifests should include enough metadata to audit:

- source assets
- render profile
- template id
- render mode
- generated outputs
- checksums or fingerprints when available

## Non-SaaS Rule

ZIP12 does not introduce a cloud rendering service or SaaS workflow.
