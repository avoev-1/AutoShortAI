# Integration with ZIP04, ZIP05, and ZIP06

## ZIP04 Mission Workflow Orchestrator

ZIP07 produces a `CreativeStrategyPlan`. ZIP04 consumes that plan to build and run missions.

## ZIP05 Intelligent Distribution Platform

ZIP07 includes platform intent and distribution hints. ZIP05 remains responsible for publishing decisions, platform packaging, and distribution-specific logic.

## ZIP06 Smart Asset Pipeline

ZIP07 declares asset requirements. ZIP06 remains responsible for assets, fingerprints, dependency graphs, cache, checkpoints, providers, cost optimization, and storage.

## Rule

ZIP07 must not duplicate ZIP04, ZIP05, or ZIP06 responsibilities.
