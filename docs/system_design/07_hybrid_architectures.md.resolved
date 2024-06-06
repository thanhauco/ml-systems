# Hybrid Architectures: Lambda, Kappa, and Beyond

## The Lambda Architecture
Proposed by Nathan Marz to handle massive data with low latency.
It acknowledges that the "Speed Layer" (Stream) might be approximate or less accurate than the "Batch Layer" (Source of Truth).

### Three Layers:
1.  **Batch Layer**: Stores master dataset (immutable). Computes batch views (e.g., daily metrics). Highly reliable, high latency.
2.  **Speed Layer**: Processes recent data only (e.g., last hour). Low latency, high complexity.
3.  **Serving Layer**: Merges results from Batch and Speed layers to answer queries.
    -   `Query(t) = BatchView(t) + SpeedView(t)`

**Pros**: Robust. If Speed layer bugs out, reset it or wait for Batch layer to correct it.
**Cons**: Maintenance nightmare. Two codebases (Batch Logic vs Stream Logic) to keep in sync.

## The Unification: Kappa Architecture
(Discussed in Streaming Chapter)
-   Remove the Batch Layer.
-   Treat "History" as a stream played from `t=0`.
-   **Requirement**: A streaming engine that can handle very high throughput for replay (e.g., Flink).

## Modern Hybrid: The Feature Store
Feature Stores often implement a Lambda-like architecture internally but hide it from the DS.
-   **Offline Store**: Parquet/S3. Used for training data generation.
-   **Online Store**: Redis/DynamoDB. Used for low-latency inference.
-   **Sync**: A job continually pushes cached features from Offline -> Online, or Stream -> Online.

## Service-Level Hybrid Patterns
1.  **Request-Response with Async Fallback**
    -   Try to get prediction in 50ms.
    -   Timeout? Return "Pending" ID to user.
    -   Process in background queue.
    -   Client polls or gets webhook.

2.  **Edge-Cloud Hybrid**
    -   **Edge**: Run small, quantized model on device (fast, privacy-preserving).
    -   **Cloud**: Send "hard" examples or aggregates to cloud for heavy model inference or training.
