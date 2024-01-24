# Deployment Strategies

## 1. Rolling Deployment (Default)
-   Replace 1 pod at a time.
-   **Pros**: Zero downtime.
-   **Cons**: Mix of V1 and V2 running simultaneously (API client must handle both).

## 2. Blue/Green Deployment
-   Spin up V2 (Green) alongside V1 (Blue).
-   Wait for Green to be healthy.
-   Switch Load Balancer 100% to Green.
-   **Pros**: Instant rollback (switch back to Blue). No mixed versions.
-   **Cons**: Double the cost (need 2x capacity) during the switch.

## 3. Canary Deployment
-   Route 1% of traffic to V2.
-   Check metrics (Error rate, Latency, Conversion).
-   If good, increase to 10%, 50%, 100%.
-   **Pros**: Lowest risk.

## 4. Shadow Deployment (Dark Launch)
-   Route 100% of traffic to V1 (Return to user).
-   **Duplicate** 100% of traffic to V2 (Fire and forget).
-   Compare V1 and V2 outputs offline.
-   **Pros**: Zero risk to user. Tests V2 under full load.
-   **Cons**: Double compute cost.
