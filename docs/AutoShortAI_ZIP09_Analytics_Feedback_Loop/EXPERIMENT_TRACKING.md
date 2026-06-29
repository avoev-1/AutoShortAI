# Experiment Tracking

ZIP09 prepares analytics for comparing variants created by ZIP07 and jobs scheduled by ZIP08.

## Objects

- `Experiment`
- `ExperimentVariant`
- `ExperimentResult`
- `VariantPerformance`

## Example

A single idea may have three hooks:

- Variant A: aggressive hook
- Variant B: mystery hook
- Variant C: educational hook

ZIP09 tracks which variant performed better per platform and time window. It does not automatically change future strategy.
