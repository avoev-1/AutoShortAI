"""ZIP16 publishing hooks."""
PUBLISHING_HOOKS = (
    "before_publishing_job_created",
    "after_publishing_job_created",
    "before_platform_selected",
    "after_platform_selected",
    "before_metadata_built",
    "after_metadata_built",
    "before_capability_validation",
    "after_capability_validation",
    "before_review_gate",
    "after_review_gate",
    "before_publish",
    "after_publish",
    "after_publish_failed",
    "after_publish_scheduled",
)
