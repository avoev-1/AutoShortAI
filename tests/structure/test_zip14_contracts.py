from autoshortai.device_farm import (
    ZIP14_RELEASE,
    DeviceFarmRouter,
    DeviceNode,
    DeviceStatus,
    DeviceTask,
    DeviceTaskType,
    DeviceType,
    ContentRestrictionLevel,
    RestrictedCreatorDevicePolicy,
)


def test_zip14_contracts_route_general_task():
    assert ZIP14_RELEASE == "ZIP14"
    node = DeviceNode(
        id="node1",
        display_name="Node 1",
        device_type=DeviceType.LOCAL_MACHINE,
        status=DeviceStatus.ONLINE,
        capabilities=("render",),
        platform_families=("generic",),
    )
    task = DeviceTask(id="task1", task_type=DeviceTaskType.RENDER, required_capabilities=("render",))
    result = DeviceFarmRouter().route(task, [node])
    assert result.accepted is True


def test_restricted_creator_policy_requires_manual_gates():
    policy = RestrictedCreatorDevicePolicy(enabled=True)
    assert policy.can_dispatch({
        "creator_consent": True,
        "all_participants_18_plus": True,
        "rights_confirmed": True,
        "age_gate": True,
        "manual_review_approved": True,
    }) is True
    assert policy.can_dispatch({"creator_consent": True}) is False


def test_restricted_task_routes_only_to_restricted_device():
    task = DeviceTask(
        id="restricted1",
        task_type=DeviceTaskType.MANUAL_REVIEW,
        required_capabilities=("manual_review",),
        platform_family="adult_x_creator_platform",
        restriction_level=ContentRestrictionLevel.RESTRICTED_ADULT_X,
        requires_manual_review=True,
        requires_isolated_device=True,
    )
    device = DeviceNode(
        id="restricted-node",
        display_name="Restricted Review Node",
        device_type=DeviceType.MANUAL_REVIEW_NODE,
        status=DeviceStatus.ONLINE,
        capabilities=("manual_review",),
        platform_families=("adult_x_creator_platform",),
        supports_restricted_creator_mode=True,
    )
    decision = DeviceFarmRouter().route(task, [device])
    assert decision.accepted is True
    assert decision.manual_review_required is True
    assert decision.restricted_workflow is True
