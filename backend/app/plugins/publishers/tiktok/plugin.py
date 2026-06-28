from typing import Any

from app.core.plugins.contracts.publisher import PublisherPlugin, PublishPayload, PublishResult


class TikTokPublisherPlugin(PublisherPlugin):
    platform_name = "tiktok"
    display_name = "TikTok"

    async def authenticate(self) -> bool:
        return False

    async def upload_private(self, payload: PublishPayload) -> PublishResult:
        return PublishResult(
            platform=self.platform_name,
            status="not_implemented",
            raw={"message": "ZIP01 placeholder. No real upload performed."},
        )

    async def fetch_analytics(self, external_id: str) -> dict[str, Any]:
        return {"platform": self.platform_name, "status": "not_implemented"}
