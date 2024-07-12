# Continuous Training (CT)

## Why Retrain?
The world changes. Models rot.
-   **Data Drift**: User behavior changes (e.g., COVID shopping patterns).
-   **Cold Start**: New users/products need embeddings.

## Triggers
1.  **Scheduled**: "Retrain every Sunday at 2 AM". (Simple, but wasteful or too slow).
2.  **Metric-Driven**: "Retrain if Accuracy drops below 90%".
3.  **Data-Driven**: "Retrain if KL-Divergence of input > Threshold".
4.  **Ad-Hoc**: "We fixed a bug in the code".

## The CT Pipeline
1.  **Ingest**: Fetch latest window of data (e.g., last 30 days).
2.  **Validate**: Ensure schema hasn't broken.
3.  **Process**: Re-compute features.
4.  **Train**: Run `model.fit()`.
5.  **Evaluate**: Compare `New Model` vs `Current Production Model` on a holdout set.
    -   *Gate*: Only promote if `New` is significantly better.
6.  **Deploy**: Update registry.
