"""ZIP16 publishing runtime protocols."""
from __future__ import annotations

from typing import Protocol, Sequence

from .capabilities import PlatformCapability
from .errors import PublishingError
from .models import PublishingApproval, PublishingContext, PublishingMetadata, PublishingRequest, PublishingResult


class PlatformPublishingAdapter(Protocol):
    @property
    def platform_id(self) -> str: ...

    def get_capability(self) -> PlatformCapability: ...

    def validate_request(self, request: PublishingRequest) -> Sequence[PublishingError]: ...

    def publish(self, request: PublishingRequest, context: PublishingContext) -> PublishingResult: ...

    def schedule(self, request: PublishingRequest, context: PublishingContext) -> PublishingResult: ...


class PublishingRuntime(Protocol):
    def register_adapter(self, adapter: PlatformPublishingAdapter) -> None: ...

    def create_request(self, request: PublishingRequest) -> PublishingRequest: ...

    def validate(self, request: PublishingRequest) -> Sequence[PublishingError]: ...

    def publish(self, request: PublishingRequest, context: PublishingContext) -> PublishingResult: ...


class MetadataBuilder(Protocol):
    def build(self, request: PublishingRequest, context: PublishingContext) -> PublishingMetadata: ...


class ReviewGate(Protocol):
    def review(self, request: PublishingRequest, context: PublishingContext) -> PublishingApproval: ...
