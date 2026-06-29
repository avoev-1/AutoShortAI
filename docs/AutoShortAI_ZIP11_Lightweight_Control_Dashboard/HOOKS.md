# Dashboard Hooks

ZIP11 reserves dashboard hook names for plugin-first extension.

Hooks:

- before_dashboard_loaded
- after_dashboard_loaded
- before_snapshot_created
- after_snapshot_created
- before_panel_rendered
- after_panel_rendered
- before_action_executed
- after_action_executed
- before_alert_created
- after_alert_created
- before_platform_panel_loaded
- after_platform_panel_loaded

Hooks must not allow plugins to bypass safety rules.
