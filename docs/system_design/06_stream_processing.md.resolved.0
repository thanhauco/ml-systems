# Stream Processing Architectures

## The Need for Speed
Batch is too slow for:
-   Fraud Detection (need to block *now*).
-   Dynamic Pricing.
-   Session-based Recommendations.

Streaming processes data **as it arrives**.

## Core Concepts
-   **Event**: Immutable fact happened at `t` (e.g., Pixel Click, Transaction).
-   **Topic**: A channel of events (e.g., Kafka Topic).
-   **Consumer Group**: Workers reading from a topic.

## Processing Semantics
1.  **At-Most-Once**: Fire and forget. Can lose data. (Metrics).
2.  **At-Least-Once**: Retries guarantee processing, but might duplicate. (Most common).
    -   *Requires Idempotent Consumers*.
3.  **Exactly-Once**: The holy grail. Hard to achieve. (Transactional Kafka, Flink).

## Windowing
How do you aggregate a stream? You must define boundaries.
-   **Tumbling Window**: Fixed non-overlapping (e.g., every 5 mins: 12:00-12:05, 12:05-12:10).
-   **Sliding Window**: Overlapping (e.g., last 5 mins, updated every 1 min).
-   **Session Window**: Based on activity (e.g., user is active, then timeout after 30 mins).

## The "Kappa Architecture"
Everything is a stream.
-   **Batch** is just a stream with a bounded start and end.
-   Use the same engine (e.g., Flink) for both historical backfill and real-time processing.
-   **Advantage**: One codebase to maintain. No logic drift between Batch ETL and Stream ETL.

## ML on Streams
1.  **Online Learning**: Update model weights on every event (Risky, unstable).
2.  **Online Inference**:
    -   System inputs features -> calls Model API -> returns prediction.
    -   *Or*
    -   Stream Processor enriches event with features -> calls Model -> writes prediction to output stream.
