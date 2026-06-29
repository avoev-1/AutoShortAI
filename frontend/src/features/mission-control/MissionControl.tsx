import { GlassCard } from "../../components/glass/GlassCard";
import { MissionOptionsPanel } from "./components/MissionOptionsPanel";
import { missionControlSteps } from "./lib/missionControlModel";

export function MissionControl() {
  return (
    <GlassCard className="pipeline">
      <div className="section-header">
        <div>
          <div className="eyebrow">Workflow Orchestrator</div>
          <h2>Mission Control</h2>
        </div>
        <span className="status-pill">Ready</span>
      </div>
      <div className="pipeline-grid">
        <MissionOptionsPanel />
        {missionControlSteps.map((step, index) => (
          <div className="pipeline-step" key={step.id}>
            <div className="step-index">{String(index + 1).padStart(2, "0")}</div>
            <div className="step-title">{step.label}</div>
            <div className="step-status">{step.detail}</div>
          </div>
        ))}
      </div>
    </GlassCard>
  );
}
