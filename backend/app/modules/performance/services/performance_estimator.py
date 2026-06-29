from dataclasses import dataclass

@dataclass(frozen=True)
class MachineProfile:
    cpu_tier:str="unknown"; gpu_tier:str="unknown"; ram_gb:int=0; vram_gb:int=0; storage_tier:str="unknown"

@dataclass(frozen=True)
class PerformanceEstimate:
    estimated_duration_seconds:int; estimated_storage_mb:int; recommendation:str; confidence:float

class PerformanceEstimator:
    def estimate(self, step_count:int, quality_mode:str, machine:MachineProfile|None=None)->PerformanceEstimate:
        base=max(step_count,1)*25
        if quality_mode=="fast": return PerformanceEstimate(int(base*.6), step_count*60, "Fast mode selected.", .65)
        if quality_mode=="quality": return PerformanceEstimate(int(base*1.8), step_count*180, "Quality mode selected.", .65)
        return PerformanceEstimate(base, step_count*100, "Balanced mode recommended.", .65)
