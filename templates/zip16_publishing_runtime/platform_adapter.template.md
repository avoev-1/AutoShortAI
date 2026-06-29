# Platform Adapter Template

Adapter name:
Platform ID:
Platform category:
Supported media ratios:
Supported codecs:
Max duration:
Max file size:
Supports scheduling:
Supports thumbnails:
Supports age restriction:
Supports paid/subscriber visibility:

## Required Methods

- get_capability()
- validate_request(request)
- publish(request, context)
- schedule(request, context)

## Guardrails

- Adapter-specific logic stays in the adapter.
- Core runtime must not call platform APIs directly.
- No credential values in adapter docs or examples.
- No bypass of platform policies.
