# Storage Formats in Data Engineering

## Row-Oriented vs Column-Oriented

| Feature | Row-Oriented (CSV, JSON, Postgres) | Column-Oriented (Parquet, ORC) |
| :--- | :--- | :--- |
| **Storage** | Records stored sequentially | Columns stored sequentially |
| **Read Efficiency** | Good for "Get User ID 123" | Good for "Average Age of All Users" |
| **Compression** | Poor (mixed types) | Excellent (same type repeats) |
| **Use Case** | Transactional (OLTP) | Analytical (OLAP) / ML Training |

## The Big Three for ML
1.  **Parquet**: The gold standard. Supported by Spark, Pandas, Dask. efficient compression (Snappy/Gzip).
2.  **Avro**: Row-based but with schema evolution. Good for **Streaming** (Kafka) where you process one event at a time.
3.  **TFRecord**: TensorFlow's native format. Protocol buffers. Essential for high-performance TPU training pipelines.

## Modern Table Formats (The Lakehouse)
Typical Data Lakes (S3) are immutable files. You can't `UPDATE` a row in a CSV.
**Delta Lake / Iceberg / Hudi** bring ACID transactions to S3.
-   **Time Travel**: `SELECT * FROM table VERSION AS OF 'yesterday'`. (Crucial for reproducibility).
-   **Schema Enforcement**: Reject data that breaks the contract.
-   **Compaction**: Merge small files into big Parquet files automatically.
