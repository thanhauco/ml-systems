# Data Lineage and Provenance

## "Where did this number come from?"
In regulated industries (Finance, Healthcare), you must be able to trace a prediction back to the raw data.

## Levels of Lineage
1.  **Table Level**: "Table A -> ETL Job -> Table B".
2.  **Row Level**: "Row 123 in B comes from Row 456 in A". (Very hard).
3.  **Column Level**: "Column `risk_score` is calculated from `age` and `debt`".

## Tools
-   **OpenLineage**: A standard spec for lineage events.
-   **Amundsen / DataHub**: Metadata catalogs that visualize lineage graphs.
-   **Airflow Lineage**: Automatically captures inputs/outputs of tasks.

## Benefits
1.  **Debugging**: "The dashboard is broken. Which upstream job failed?"
2.  **Impact Analysis**: "If I change this column schema, who will break?"
3.  **Compliance**: GDPR "Right to be Forgotten". If user deletes account, find all derived data.
