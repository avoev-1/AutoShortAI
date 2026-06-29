from dataclasses import dataclass

@dataclass(frozen=True)
class GuardianCheckResult:
    allowed:bool; score:float; messages:list[str]

class GuardianHook:
    def pre_execution_check(self, mission_id:str, step_ids:list[str])->GuardianCheckResult:
        return GuardianCheckResult(True, 1.0, [f"Guardian placeholder allowed mission {mission_id} with {len(step_ids)} steps."])
