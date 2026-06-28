from app.core.pipeline.models import PipelineStep


class PipelineGraph:
    def __init__(self, steps: list[PipelineStep]) -> None:
        self.steps = {step.step_id: step for step in steps}
        self._validate()

    def _validate(self) -> None:
        for step in self.steps.values():
            for dependency in step.depends_on:
                if dependency not in self.steps:
                    raise ValueError(f"Unknown dependency '{dependency}' for step '{step.step_id}'")

    def execution_order(self) -> list[PipelineStep]:
        visited: set[str] = set()
        order: list[PipelineStep] = []

        def visit(step_id: str) -> None:
            if step_id in visited:
                return
            step = self.steps[step_id]
            for dependency in step.depends_on:
                visit(dependency)
            visited.add(step_id)
            order.append(step)

        for step_id in self.steps:
            visit(step_id)

        return order
