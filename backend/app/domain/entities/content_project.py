from dataclasses import dataclass


@dataclass(frozen=True)
class ContentProject:
    id: str
    workspace_id: str
    title: str
    target_platforms: list[str]
