from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class CampaignTarget:
    platform: str
    accounts: List[str]
    publish_mode: str = "strategy_driven"


@dataclass
class Campaign:
    campaign_id: str
    name: str
    source_asset: str
    status: str = "draft"
    goal: str = "views"
    targets: List[CampaignTarget] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)
    rules: List[Dict[str, Any]] = field(default_factory=list)
    schedule: Optional[Dict[str, Any]] = None
