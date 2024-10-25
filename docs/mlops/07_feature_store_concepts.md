# Feature Stores

## The Problem: Training-Serving Skew
-   **Data Scientist (Python)**: Calculates `avg_spend_last_30d` using Pandas.
-   **Backend Engineer (Java)**: Re-implements `avg_spend_last_30d` using SQL.
-   **Result**: The logic differs slightly. Model performs worse in production.

## The Feature Store Solution
Center repository for feature definitions. "Define Once, Use Everywhere".

## Architecture
1.  **Offline Store**: Cheap, high-capacity storage (Parquet/S3). Used for generating historical training datasets.
2.  **Online Store**: Low-latency Key-Value store (Redis/DynamoDB). Used for real-time inference.
3.  **Registry**: Catalog of feature definitions (`name`, `type`, `owner`).

## Tools
-   **Feast**: Open source, manages the Offline/Online sync.
-   **Tecton/Hopsworks**: Commercial platforms.
