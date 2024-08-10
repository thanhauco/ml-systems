# Serving Patterns

## 1. REST API (Request-Response)
-   **Protocol**: HTTP/1.1 (JSON).
-   **Pros**: Ubiquitous, easy to debug (curl), firewall friendly.
-   **Cons**: Serialization overhead (text-based), Head-of-Line blocking (HTTP/1).
-   **Tool**: FastAPI, Flask.

## 2. gRPC (Remote Procedure Call)
-   **Protocol**: HTTP/2 + Protobuf.
-   **Pros**: Binary serialization (small payload), Multiplexing, Strongly typed contracts.
-   **Cons**: Harder to debug (binary), requires client stub generation.
-   **Use Case**: Internal microservices, low latency requirements.

## 3. Asynchronous Inference (Message Bus)
-   **Flow**: User -> API -> Kafka -> Worker -> Database.
-   **Use Case**: Image generation, Long document summarization.
-   **Pros**: Decouples Request from Process. Handles bursts gracefully.

## 4. Batch Serving
-   **Flow**: Accumulate 100 requests -> Run minimal padding batch -> Return 100 responses.
-   **Benefit**: Massive throughput increase on GPUs (Matrix multiplication loves large batches).
-   **Cost**: Slightly higher latency for the first request in the batch.
