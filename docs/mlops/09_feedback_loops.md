# Feedback Loops

## Closing the Loop
A model predicts. Ideally, we eventually know if it was *right*.
`Prediction (t=0) -> Outcome (t=N) -> Join -> Metric`.

## Types of Feedback
1.  **Immediate**: Recommendation System. "Did user click?" (ms to seconds).
2.  **Delayed**: Credit Scoring. "Did user default?" (Months to Years).
3.  **Indirect**: Chatbot. "Did user thumb-up?" or "Did user rephrase query?".

## Logging Feedback
You need a system to join Prediction ID with Outcome ID.
-   **Log Payload**: `{"pred_id": "uuid", "input": "...", "score": 0.9}`.
-   **Feedback Payload**: `{"pred_id": "uuid", "actual": 1}`.
-   **Join**: Stream processing (Kappa architecture) or Batch nightly job.

