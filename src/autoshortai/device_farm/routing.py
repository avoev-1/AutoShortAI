from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence

from .models import ContentRestrictionLevel, DeviceAssignment, DeviceNode, DeviceTask


@dataclass(frozen=True)
class DeviceRouteDecision:
    selected_device_id: str | None
    accepted: bool
    reason: str
    manual_review_required: bool = False
    restricted_workflow: bool = False


class DeviceFarmRouter:
    def route(self, task: DeviceTask, devices: Sequence[DeviceNode]) -> DeviceRouteDecision:
        for device in devices:
            if not set(task.required_capabilities).issubset(set(device.capabilities)):
                continue
            if task.platform_family != "generic" and task.platform_family not in device.platform_families:
                continue
            if task.restriction_level == ContentRestrictionLevel.RESTRICTED_ADULT_X:
                if not device.supports_restricted_creator_mode:
                    continue
                return DeviceRouteDecision(
                    selected_device_id=device.id,
                    accepted=True,
                    reason="restricted creator compatible device selected; manual review remains required",
                    manual_review_required=True,
                    restricted_workflow=True,
                )
            return DeviceRouteDecision(
                selected_device_id=device.id,
                accepted=True,
                reason="capability match",
                manual_review_required=task.requires_manual_review,
                restricted_workflow=False,
            )
        return DeviceRouteDecision(
            selected_device_id=None,
            accepted=False,
            reason="no compatible device found",
            manual_review_required=task.requires_manual_review,
            restricted_workflow=task.restriction_level == ContentRestrictionLevel.RESTRICTED_ADULT_X,
        )

    def assign(self, task: DeviceTask, devices: Sequence[DeviceNode]) -> DeviceAssignment | None:
        decision = self.route(task, devices)
        if not decision.accepted or decision.selected_device_id is None:
            return None
        return DeviceAssignment(
            task_id=task.id,
            device_id=decision.selected_device_id,
            reason=decision.reason,
            manual_review_required=decision.manual_review_required,
            restricted_workflow=decision.restricted_workflow,
        )
