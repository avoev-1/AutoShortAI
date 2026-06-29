# Failure Policies

## Failure classes

- transient
- provider_error
- resource_limit
- validation_error
- dependency_missing
- cancelled_by_user
- unknown

## Retry decisions

A failure policy can decide:

- retry immediately
- retry after delay
- pause
- cancel
- mark failed
- resume from checkpoint
- require manual review

## Safety

No job should retry forever by default.

Retry counts and delay windows must be explicit.
