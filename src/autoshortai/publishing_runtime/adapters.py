"""ZIP16 adapter skeletons.

Adapters are placeholders for future implementation. They must remain separate
from the core publishing runtime.
"""
from __future__ import annotations

from typing import Sequence

from .capabilities import PlatformCapability, default_capabilities
from .errors import PublishingError, PublishingFailureReason, PublishingRecoveryAction
from .models import PlatformCategory, PublishingContext, PublishingRequest, PublishingResult, PublishingStatus
from .restricted import validate_restricted_request


class BasePlatformPublishingAdapter:
    def __init__(self, capability: PlatformCapability) -> None:
        self._capability = capability

    @property
    def platform_id(self) -> str:
        return self._capability.platform_id

    def get_capability(self) -> PlatformCapability:
        return self._capability

    def validate_request(self, request: PublishingRequest) -> Sequence[PublishingError]:
        errors: list[PublishingError] = []
        if request.target.platform_id != self.platform_id:
            errors.append(PublishingError(
                reason=PublishingFailureReason.CAPABILITY_MISMATCH,
                message="request target platform does not match adapter platform",
                recoverable=True,
                recommended_actions=(PublishingRecoveryAction.FIX_METADATA,),
                platform_id=self.platform_id,
                request_id=request.request_id,
            ))
        if not request.media.path:
            errors.append(PublishingError(
                reason=PublishingFailureReason.INVALID_MEDIA,
                message="media path is required",
                recoverable=True,
                recommended_actions=(PublishingRecoveryAction.RE_RENDER,),
                platform_id=self.platform_id,
                request_id=request.request_id,
            ))
        return tuple(errors)

    def publish(self, request: PublishingRequest, context: PublishingContext) -> PublishingResult:
        return PublishingResult(
            request_id=request.request_id,
            status=PublishingStatus.READY_FOR_REVIEW,
            platform_id=self.platform_id,
            warnings=("ZIP16 adapter is dry-run only; no real API call executed.",),
        )

    def schedule(self, request: PublishingRequest, context: PublishingContext) -> PublishingResult:
        return PublishingResult(
            request_id=request.request_id,
            status=PublishingStatus.SCHEDULED,
            platform_id=self.platform_id,
            scheduled_at_iso=request.schedule.scheduled_at_iso,
            warnings=("ZIP16 adapter is dry-run only; no real API call executed.",),
        )


class GenericPlatformPublishingAdapter(BasePlatformPublishingAdapter):
    def __init__(self) -> None:
        super().__init__(default_capabilities()["generic_vertical_video"])


class AdultPlatformPublishingAdapter(BasePlatformPublishingAdapter):
    """Restricted opt-in adapter skeleton for adult creator platforms."""

    def __init__(self) -> None:
        super().__init__(default_capabilities()["generic_adult_creator_platform"])

    def validate_request(self, request: PublishingRequest) -> Sequence[PublishingError]:
        errors = list(super().validate_request(request))
        if request.target.category != PlatformCategory.ADULT_RESTRICTED:
            errors.append(PublishingError(
                reason=PublishingFailureReason.RESTRICTED_COMPLIANCE_MISSING,
                message="adult platform adapter requires adult_restricted target category",
                recoverable=True,
                recommended_actions=(PublishingRecoveryAction.MANUAL_REVIEW,),
                platform_id=self.platform_id,
                request_id=request.request_id,
            ))
        restricted = validate_restricted_request(request)
        for reason in restricted.block_reasons:
            errors.append(PublishingError(
                reason=PublishingFailureReason.RESTRICTED_COMPLIANCE_MISSING,
                message=reason,
                recoverable=True,
                recommended_actions=(PublishingRecoveryAction.MANUAL_REVIEW,),
                platform_id=self.platform_id,
                request_id=request.request_id,
            ))
        return tuple(errors)
