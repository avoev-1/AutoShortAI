from enum import StrEnum


class SDKEventType(StrEnum):
    plugin_registered = "plugin_registered"
    plugin_health_checked = "plugin_health_checked"
    workflow_created = "workflow_created"
    script_generated = "script_generated"
    video_rendered = "video_rendered"
    publish_requested = "publish_requested"
    private_upload_completed = "private_upload_completed"
    analytics_updated = "analytics_updated"
    human_approval_required = "human_approval_required"
    budget_limit_reached = "budget_limit_reached"
