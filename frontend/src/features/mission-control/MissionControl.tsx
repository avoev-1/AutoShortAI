import { GlassCard } from "../../components/glass/GlassCard";

const steps = [
  "Research",
  "Script",
  "Voice",
  "Visuals",
  "Video",
  "Subtitles",
  "Metadata",
  "Publish",
  "Analytics",
  "Learning",
];

export function MissionControl() {
  return (
    <GlassCard className="pipeline">
      <div className="section-header">
        <div>
          <div className="eyebrow">Signature View</div>
          <h2>Mission Control</h2>
        </div>
        <span className="status-pill">Ready</span>
      </div>
      <div className="pipeline-grid">
        {steps.map((step, index) => (
          <div className="pipeline-step" key={step}>
            <div className="step-index">{String(index + 1).padStart(2, "0")}</div>
            <div className="step-title">{step}</div>
            <div className="step-status">{index === 0 ? "Ready" : "Waiting"}</div>
          </div>
        ))}
      </div>
    </GlassCard>
  );
}
