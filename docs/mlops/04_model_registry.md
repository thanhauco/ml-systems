# Model Registry

## The Single Source of Truth
A Git repository stores code. A Model Registry stores *deployable models*.

## Organization
-   **Registered Model**: "FraudDetector".
-   **Model Version**: "Version 1", "Version 2".
-   **Model Stage**:
    -   `Staging`: Currently being tested (Integration tests, Load tests).
    -   `Production`: Live and taking traffic.
    -   `Archived`: Old versions kept for rollback.

## Lifecycle Transitions
1.  DS trains model -> Logs to Tracking Server.
2.  Best model is registered -> "Version 12" (Stage: None).
3.  CI Pipeline runs -> Promotes to `Staging`.
4.  CD Pipeline deploys Staging -> Run Smoke Tests.
5.  Manual Approval / A/B Test success -> Promote to `Production`.
6.  Old "Version 11" moves to `Archived`.
