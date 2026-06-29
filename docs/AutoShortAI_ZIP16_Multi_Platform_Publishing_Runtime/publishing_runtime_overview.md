# Publishing Runtime Overview

ZIP16 defines the runtime layer responsible for transforming a rendered media package into a validated publishing request.

The runtime is intentionally adapter-based:

```text
PublishingRuntime
    ↓
PlatformPublishingAdapter
    ↓
Platform-specific implementation later
```

The runtime owns normalization, validation, review state, scheduling metadata, and result reporting. Platform adapters own platform-specific execution.
