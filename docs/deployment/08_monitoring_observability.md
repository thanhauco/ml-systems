# Monitoring and Observability

## The Three Pillars

### 1. Logs (Events)
"What happened?"
-   `INFO: Request received.`
-   `ERROR: CUDA OOM.`
-   **Tool**: ELK Stack (Elasticsearch, Logstash, Kibana), Fluentd.

### 2. Metrics (Aggregates)
"What is the trend?"
-   **System**: CPU %, RAM %, GPU Util %.
-   **Application**: Requests per second (RPS), P99 Latency (ms).
-   **Model**: Prediction distribution mean.
-   **Tool**: Prometheus, Grafana.

### 3. Traces (Context)
"Where did the time go?"
-   Follow a request ID through microservices.
-   `Gateway (2ms) -> Auth (5ms) -> Model (100ms) -> DB save (10ms)`.
-   **Tool**: Jaeger, OpenTelemetry.

## Monitoring ML Specifically
1.  **Data Drift**: Input distribution P(X) changes. (e.g., Camera lens gets dirty).
2.  **Concept Drift**: Relationship P(Y|X) changes. (e.g., Inflation makes $100 less valuable).
3.  **Prediction Drift**: Output distribution P(Y) changes. (e.g., Model starts predicting "Spam" 90% of time).

**Alerting**: "If P99 Latency > 200ms for 5 mins, Page On-Call."
