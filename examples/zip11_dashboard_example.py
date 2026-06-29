from autoshortai.dashboard import DashboardCore, overview_panel, system_health_panel


def main() -> None:
    core = DashboardCore()
    snapshot = core.build_snapshot(
        extra_panels=(
            overview_panel(generated_videos=3, active_jobs=2, alerts=0),
            system_health_panel(cpu_percent=23, ram_percent=45),
        )
    )
    print(snapshot.release)
    print(snapshot.title)
    print([panel.id for panel in snapshot.panels])


if __name__ == "__main__":
    main()
