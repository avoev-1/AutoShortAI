class DeviceFarmError(Exception):
    """Base error for ZIP14 device farm contracts."""


class DeviceRoutingError(DeviceFarmError):
    """Raised when a task cannot be routed to a compatible device."""


class RestrictedCreatorPolicyError(DeviceFarmError):
    """Raised when a restricted creator workflow violates policy gates."""
