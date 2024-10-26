# Introduction to Data Engineering for AI

## The Foundation of AI
"Garbage In, Garbage Out". Data Engineering (DE) is the art of preventing garbage from entering the system.
While Data Scientists build models, Data Engineers build the *pipes* that feed those models.

## Core Responsibilities
1.  **Ingestion**: Bringing data from external sources (APIs, DBs, IoT) into the system.
2.  **Storage**: Organizing data efficiently for retrieval (Data Lake, Warehouse, Feature Store).
3.  **Processing**: Transforming raw data into usable formats (Cleaning, Normalization).
4.  **Serving**: Delivering data to models for training or inference.

## The Modern Data Stack for ML
-   **Extraction**: Fivetran, Airbyte.
-   **Loading**: dbt (data build tool) for SQL transformations.
-   **Orchestration**: Airflow, Dagster, Prefect.
-   **Storage**: Snowflake, Databricks (Delta Lake), S3.
-   **Versioning**: DVC, Pachyderm.

## Key Challenges in ML Data Engineering
-   **Reproducibility**: Can you recreate the training dataset from 6 months ago?
-   **Quality**: Is the data drifting? Are there nulls?
-   **Latency**: Can features be served in < 10ms for real-time inference?
-   **Privacy**: Are we leaking PII into the model?
