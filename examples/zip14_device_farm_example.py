from autoshortai.device_farm import (
    DeviceFarmRouter,
    DeviceNode,
    DeviceStatus,
    DeviceTask,
    DeviceTaskType,
    DeviceType,
    ContentRestrictionLevel,
)

node = DeviceNode(
    id="local-render-node",
    display_name="Local Render Node",
    device_type=DeviceType.LOCAL_MACHINE,
    status=DeviceStatus.ONLINE,
    capabilities=("render", "ai_worker"),
    platform_families=("generic", "youtube_shorts", "tiktok"),
)

task = DeviceTask(
    id="task.render.001",
    task_type=DeviceTaskType.RENDER,
    required_capabilities=("render",),
    platform_family="generic",
    restriction_level=ContentRestrictionLevel.GENERAL,
)

assignment = DeviceFarmRouter().assign(task, [node])
print(assignment)
