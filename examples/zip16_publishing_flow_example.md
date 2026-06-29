# ZIP16 Publishing Flow Example

```text
1. ZIP12 renders a vertical video.
2. ZIP16 creates a PublishingRequest.
3. MetadataBuilder normalizes title, description, hashtags, language, and maturity rating.
4. PublishingRuntime selects a PlatformPublishingAdapter.
5. Capability validation checks duration, ratio, file size, metadata limits, and visibility.
6. ManualReviewGate blocks or approves the request.
7. Adapter performs dry-run now; real implementation comes later.
8. PublishingResult is sent to analytics and dashboard layers.
```

The example is platform-agnostic. YouTube Shorts can be the first adapter, but TikTok, Instagram, and future platforms must follow the same adapter contract.
