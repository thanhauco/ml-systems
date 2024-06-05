# Reliability & Scalability in ML Systems

## Defining Reliability in ML
Reliability in traditional software means the application works as expected. in ML, it's more nuanced:
1.  **Software Reliability**: The API doesn't crash, latency is low.
2.  **Data Reliability**: Inputs are within expected distributions.
3.  **Model Reliability**: Predictions are accurate and robust to noise.

### Strategies for Reliability
-   **Circuit Breakers**: Stop traffic to a model if error rates spike.
-   **Fallbacks**: If a complex model times out, return a heuristic or a cached prediction.
-   **Retries**: Exponential backoff for transient failures (e.g., database connection).
-   **Bulkheads**: Isolate failures in one component (e.g., log processing) from crashing the main inference path.

## Scalability Patterns

### 1. Horizontal Scaling vs Vertical Scaling
-   **Vertical (Scale Up)**: Bigger machine. Good for training single massive models (e.g., LLMs needing 80GB VRAM).
-   **Horizontal (Scale Out)**: More machines. Essential for inference services and distributed data processing.

### 2. Auto-scaling Policies
ML workloads are often "bursty".
-   **Metric-based**: Scale on CPU utilization (traditional).
-   **Event-based**: Scale on Queue Depth (better for batch jobs).
-   **Schedule-based**: Scale up at 9 AM for business hours.

### 3. Asynchrony
Decouple components to improve scalability.
-   **Training**: Always async. Triggered by data arrival or cron.
-   **Inference**:
    -   *Real-time*: Synchronous (blocking). Hardest to scale.
    -   *Near real-time*: Async queue.
    -   *Batch*: Nightly cron jobs.

## The CAP Theorem for ML
In distributed ML systems (like parameter servers), you often trade off **Consistency** (all nodes see same weights) for **Availability** (system keeps running) and **Partition Tolerance**.
-   **Hogwild!**: A training scheme that allows inconsistent weight updates to speed up training, sacrificing strict consistency for speed.

