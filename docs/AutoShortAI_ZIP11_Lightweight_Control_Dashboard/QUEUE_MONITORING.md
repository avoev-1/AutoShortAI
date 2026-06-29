# Queue Monitoring

Queue monitoring exposes ZIP08 state to the dashboard.

Displayed information may include:

- pending jobs
- scheduled jobs
- running jobs
- failed jobs
- completed jobs
- retrying jobs
- worker count
- next scheduled job
- resource budget status

The dashboard must use queue contracts instead of directly mutating scheduler state.
