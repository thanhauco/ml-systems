# Batch Processing Architectures

## When to use Batch?
Batch processing is the default for:
1.  **Training**: Iterating over static datasets.
2.  **Offline Inference**: Pre-computing recommendations for all users nightly.
3.  **Reporting**: Aggregating metrics.

**Pros**: High throughput, efficient, easier to recover (replay the job).
**Cons**: High latency (results available after job finishes).

## The ETL / ELT Pipeline
-   **Extract**: Pull from Source (SQL, Logs).
-   **Transform**: Clean, Join, Aggregate.
-   **Load**: Save to Destination (Data Warehouse, Feature Store).

## Workflow Orchestration (Airflow, Prefect, Dagster)
Batch jobs are rarely single scripts. They are DAGs (Directed Acyclic Graphs).
-   **Task A**: Ingest Data
-   **Task B**: Validate Data
-   **Task C**: Train Model (Depends on B)
-   **Task D**: Deploy Model (Depends on C)

### Key Concepts in Orchestration
-   **Idempotency**: Retrying a failed job should not duplicate data.
    -   *Technique*: Overwrite partitions, or use `INSERT OVERWRITE` logic.
-   **Backfilling**: Running the pipeline for past time ranges (e.g., "Run for last 30 days").
-   **Sensors**: Waiting for external events (e.g., "Wait for S3 file to appear").

## Optimization Techniques
1.  **Partitioning**: Divide data by Date, Region, etc. Workers process partitions independently.
2.  **Columnar Formats (Parquet/ORC)**: Read only the columns you need. Compress efficiently.
3.  **Vectorization**: Use Pandas/Numpy/Arrow to process batches of rows, not Python for-loops.

## Failure Modes
-   **OOM (Out of Memory)**: A specific partition is too large (Data Skew).
-   **Stragglers**: One task takes 10x longer than others.
-   **Schema Drift**: Upstream changed a column name, breaking the batch job.
