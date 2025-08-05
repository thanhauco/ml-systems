# Point-in-Time Correctness (Time Travel)

## The Leakage Problem
When creating training datasets, naively joining features on `user_id` can lead to data leakage if future values are included.

## Solution: ASOF Join
A feature store performs a point-in-time join:
For each observation $(entity, timestamp)$, fetch the feature value $f$ such that $f.timestamp \le timestamp$.

## Implementation
- Offline stores use efficient window functions or `ASOF JOIN` syntax.
- Ensures the model only "sees" what was known at the time of prediction.
