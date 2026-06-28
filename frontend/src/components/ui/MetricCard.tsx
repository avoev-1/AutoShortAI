import { GlassCard } from "../glass/GlassCard";

type Props = {
  label: string;
  value: string;
};

export function MetricCard({ label, value }: Props) {
  return (
    <GlassCard className="card">
      <div className="card-label">{label}</div>
      <div className="card-value">{value}</div>
    </GlassCard>
  );
}
