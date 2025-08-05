# Feature Store Architecture

## The Dual-Database Problem
Training requires large batches of historical data (high throughput, offline).
Inference requires single-record lookups at low latency (online).
A Feature Store unifies these two access patterns.

## Components
1.  **Feature Registry**: Central catalog of feature definitions and metadata.
2.  **Offline Store**: Data warehouse (e.g., Snowflake, BigQuery, Parquet) for training data.
3.  **Online Store**: Low-latency KV store (e.g., Redis, DynamoDB) for serving.
4.  **Sync**: Jobs that materialize offline data to the online store.

## Benefits
- **Consistency**: The same transformation logic is used for training and serving.
- **Reusability**: Features are defined once and reused across models.
