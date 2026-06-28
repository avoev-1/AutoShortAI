const nav = [
  "Dashboard",
  "Mission Control",
  "AI Studio",
  "Video Studio",
  "Publishers",
  "Analytics",
  "Storage",
  "Human Control",
  "Settings",
];

export function Sidebar() {
  return (
    <aside className="sidebar glass">
      <div className="logo">AutoShortAI</div>
      <nav className="nav">
        {nav.map((item, index) => (
          <button className={`nav-item ${index === 0 ? "active" : ""}`} key={item}>
            {item}
          </button>
        ))}
      </nav>
    </aside>
  );
}
