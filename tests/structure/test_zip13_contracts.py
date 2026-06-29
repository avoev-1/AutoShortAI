def test_zip13_contract_imports():
    from autoshortai.ai_runtime import (
        ZIP13_RELEASE,
        AIWorkerRuntime,
        AIWorkerTask,
        AIWorkerTaskType,
        ContentMaturityRating,
        PlatformContext,
        PlatformFamily,
        RestrictedPlatformCategory,
        MockScriptGenerationWorker,
        ZIP13_AI_RUNTIME_HOOKS,
    )

    assert ZIP13_RELEASE == "ZIP13"
    assert "before_provider_called" in ZIP13_AI_RUNTIME_HOOKS
    context = PlatformContext(id="generic", family=PlatformFamily.GENERIC)
    task = AIWorkerTask(
        id="contract.task",
        task_type=AIWorkerTaskType.SCRIPT_GENERATION,
        prompt_template_id="script_generation",
        maturity_rating=ContentMaturityRating.GENERAL,
    )
    result = AIWorkerRuntime(workers=[MockScriptGenerationWorker()]).run_task(task, context)
    assert result.status.value == "completed"


def test_restricted_adult_context_requires_review_or_block():
    from autoshortai.ai_runtime import (
        AIWorkerRuntime,
        AIWorkerTask,
        AIWorkerTaskType,
        ContentMaturityRating,
        PlatformContext,
        PlatformFamily,
        RestrictedPlatformCategory,
    )

    context = PlatformContext(
        id="restricted.example",
        family=PlatformFamily.ADULT_CREATOR_PLATFORM,
        restricted_category=RestrictedPlatformCategory.ADULT_CREATOR_PLATFORM,
        requires_manual_review=True,
        requires_age_gate=True,
        requires_consent_metadata=True,
    )
    task = AIWorkerTask(
        id="restricted.task",
        task_type=AIWorkerTaskType.SCRIPT_GENERATION,
        prompt_template_id="script_generation",
        maturity_rating=ContentMaturityRating.RESTRICTED_ADULT,
        metadata={
            "creator_consent": True,
            "rights_confirmed": True,
            "age_gate": True,
            "all_participants_18_plus": True,
        },
    )
    result = AIWorkerRuntime().run_task(task, context)
    assert result.status.value == "review_required"
