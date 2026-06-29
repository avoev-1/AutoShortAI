from autoshortai.creative_strategy import (
    BlueprintBlockKind,
    ContentAngle,
    ContentHook,
    ContentIdea,
    ContentPromise,
    ContentStrategyEngineContract,
    ContentFormat,
    CreationProfile,
    EnergyLevel,
    PlatformTarget,
    RiskLevel,
    ScriptBlock,
    ScriptBlueprint,
    StrategyPriority,
    StrategyRequest,
    TargetAudience,
)


def test_zip07_models_can_be_instantiated():
    audience = TargetAudience(label="AI creators")
    angle = ContentAngle(label="hidden detail", description="Focus on the overlooked part")
    hook = ContentHook(text="Most people missed this.")
    promise = ContentPromise(value="Understand it fast")
    idea = ContentIdea(
        title="Why this update matters",
        angle=angle,
        hook=hook,
        promise=promise,
        audience=audience,
    )
    assert idea.idea_key == "why-this-update-matters"

    profile = CreationProfile(
        profile_id="youtube_shorts_default",
        platform=PlatformTarget.YOUTUBE_SHORTS,
        content_format=ContentFormat.SHORT,
        min_seconds=25,
        max_seconds=45,
        energy_level=EnergyLevel.HIGH,
        risk_level=RiskLevel.LOW,
        narrative_blocks=(
            BlueprintBlockKind.HOOK,
            BlueprintBlockKind.CONTEXT,
            BlueprintBlockKind.VALUE,
            BlueprintBlockKind.TWIST,
            BlueprintBlockKind.CTA,
        ),
    )
    assert profile.profile_id == "youtube_shorts_default"

    request = StrategyRequest(
        request_id="req-1",
        profile_id=profile.profile_id,
        initial_idea="Simple AI short",
        priority=StrategyPriority.QUALITY,
    )
    assert request.requested_variants == 1

    blueprint = ScriptBlueprint(
        blueprint_id="bp-1",
        idea_key=idea.idea_key,
        target_duration_seconds=35,
        blocks=(ScriptBlock(BlueprintBlockKind.HOOK, "open", 0, 3),),
    )
    assert blueprint.blocks[0].kind is BlueprintBlockKind.HOOK


def test_zip07_contract_exports_exist():
    assert ContentStrategyEngineContract is not None
