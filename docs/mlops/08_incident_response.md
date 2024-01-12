# Incident Response for ML

## When Models Go Bad
Code breaks with a `500 Error`. Models break by *silently returning garbage*.

## Common Incidents
1.  **Broken Upstream**: The "Gender" column format changed from "M/F" to "0/1". Model treats "0" as a new category.
2.  **Stale Model**: No retraining for 6 months. Competitor launched a feature that changed user behavior.
3.  **Feedback Loop**: Model predicts "Spam" -> User never sees email -> No click -> Model confirms "Spam".

## Runbook Steps
1.  **Detect**: Alert fires (Prediction Drift > Threshold).
2.  **Mitigate**:
    -   *Rollback*: Revert to `Version N-1`.
    -   *Fallback / Kill Switch*: Turn off ML, use a heuristic (Rule-based system).
3.  **Investigate**: Check data lineage. "Did the ETL job fail?".
4.  **Fix**: Retrain or Fix data pipeline.
