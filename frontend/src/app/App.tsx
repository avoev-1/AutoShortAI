import { GlassCard } from "../components/glass/GlassCard";
import { Sidebar } from "../components/navigation/Sidebar";
import { MetricCard } from "../components/ui/MetricCard";
import { MissionControl } from "../features/mission-control/MissionControl";

const metrics = [
  ["Platform Health", "OK"],
  ["Publisher Plugins", "3"],
  ["Real Publishing", "Off"],
  ["API Spend Today", "$0.00"],
];

export function App() {
  return (
    <div className="app-shell">
      <Sidebar />
      <main className="main">
        <GlassCard className="hero">
          <div className="eyebrow">ZIP01 Foundation</div>
          <h1>Content Automation Platform</h1>
          <p>
            Apple Glass interface for multi-platform AI content production.
            Platforms, AI models, voice engines and video engines are plugins.
          </p>
        </GlassCard>

        <section className="metric-grid">
          {metrics.map(([label, value]) => (
            <MetricCard key={label} label={label} value={value} />
          ))}
        </section>

        <MissionControl />
      </main>
    </div>
  );
}
