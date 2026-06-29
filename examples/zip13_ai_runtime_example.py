from autoshortai.ai_runtime import (
    AIWorkerRuntime,
    AIWorkerTask,
    AIWorkerTaskType,
    PlatformContext,
    PlatformFamily,
    MockScriptGenerationWorker,
)

runtime = AIWorkerRuntime(workers=[MockScriptGenerationWorker()])
context = PlatformContext(id="generic_vertical", family=PlatformFamily.GENERIC, duration_target_seconds=35)
task = AIWorkerTask(
    id="ai.task.demo",
    task_type=AIWorkerTaskType.SCRIPT_GENERATION,
    prompt_template_id="script_generation",
    required_capabilities=("text_generation",),
)
result = runtime.run_task(task, context)
print(result.status.value)
