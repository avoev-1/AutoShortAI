# Performance Profiler

The Performance Profiler records lightweight timing and resource metrics to help keep AutoShortAI fast and maintainable.

## Metrics

- duration in milliseconds
- optional CPU percentage
- optional memory usage
- scope name
- timestamp
- metadata

## Rules

- Profiling must be optional.
- Profiling must be lightweight.
- It must not require a heavy monitoring stack.
- Future implementations should support no-op profiling by default.

## Use cases

- Detect slow asset fingerprinting.
- Compare cache hit versus rebuild time.
- Identify expensive provider calls.
- Feed future Guardian Engine quality checks without implementing Guardian in ZIP06.
