# Device Fleet Manager

The Device Fleet Manager administers authorized devices used in production and distribution workflows.

## Device classes

- Android phone/tablet
- iOS device within platform limits
- Windows PC
- Linux PC
- macOS machine
- Raspberry Pi / edge node
- Mini-PC
- Server
- Virtual machine
- Phone rack

## Device state

```yaml
device_id: string
name: string
class: android|ios|windows|linux|macos|raspberry_pi|server|vm|rack_node
status: online|offline|busy|error|maintenance
battery: optional
storage_free: optional
temperature: optional
network: optional
current_task: optional
last_heartbeat: timestamp
```

## Boundaries

This module is for deployment, monitoring and administration. It must not automate fake engagement.
