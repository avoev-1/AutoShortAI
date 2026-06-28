from typing import Any

from app.core.plugins.contracts.publisher import PublisherPlugin, PublishPayload, PublishResult


class InstagramPublisherPlugin(PublisherPlugin):
    platform_name = "instagram"
    display_name = "Instagram"

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
