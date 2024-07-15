# Data Collection Strategies

## The Three V's of Data
-   **Volume**: How much? (TB/PB)
-   **Velocity**: How fast? (Batch vs Stream)
-   **Variety**: What format? (JSON, Images, Audio, Logs)

## Ingestion Patterns

### 1. Batch API Crawling
-   **Use Case**: Scraping web pages or calling Rate-Limited APIs (e.g., Twitter/X API).
-   **Strategy**: AsyncIO with retries.
-   **Challenge**: Rate limits, IP bans.
-   **Solution**: Rotation of proxies, exponential backoff.

### 2. Change Data Capture (CDC)
-   **Use Case**: Syncing a production Database (Postgres) to a Data Warehouse.
-   **Strategy**: Listen to the DB's Write-Ahead Log (WAL).
-   **Tool**: Debezium + Kafka.
-   **Benefit**: Low impact on the source DB (log-based vs query-based).

### 3. Event Streaming
-   **Use Case**: User clickstreams, IoT sensors.
-   **Strategy**: Push events to a message bus (Kafka/PubSub).
-   **Format**: Protobuf or Avro (enforces schema).

### 4. Bulk File Transfer
-   **Use Case**: Partner drops a CSV on an SFTP server daily.
-   **Strategy**: Watcher script triggers ingest when file stabilizes.
