# Alerting & Incident Response

## SLIs and SLOs
- **SLI**: Service Level Indicator (e.g., Latency, Error Rate, Drift Score).
- **SLO**: Service Level Objective (e.g., Drift Score < 0.1 for 99% of days).

## Severity Levels
1.  **P1 (Critical)**: Model output is garbage. Page on-call immediately.
2.  **P2 (High)**: Significant drift detected. Investigate within 24h.
3.  **P3 (Low)**: Minor drift. Log for next retraining cycle.

## Channels
- **Webhook/Slack**: For P2/P3.
- **PagerDuty**: For P1.
