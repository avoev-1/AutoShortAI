# Lightweight UI Adapter Layer

The dashboard can be rendered through multiple adapters over time.

Planned adapter types:

- CLI dashboard
- local web dashboard
- desktop wrapper
- future mobile companion

ZIP11 defines only the boundaries. It does not require a heavy UI framework.

Each adapter receives dashboard view models and emits control actions.
