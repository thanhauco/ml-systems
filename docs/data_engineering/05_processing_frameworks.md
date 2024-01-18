# Processing Frameworks at Scale

When `import pandas as pd` crashes with `MemoryError`, you need distributed processing.

## Apache Spark (The Heavyweight)
-   **Paradigm**: MapReduce (in-memory).
-   **Language**: Scala (native), Python (PySpark).
-   **Pros**: Industry standard, massive ecosystem, SQL support.
-   **Cons**: JVM overhead, debugging is hell, startup latency.

## Dask (The Pythonic Choice)
-   **Paradigm**: Distributed Task Graph.
-   **API**: Mimics Pandas and Numpy. `dask_dataframe.read_csv(...)`.
-   **Pros**: Pure Python, lighter weight, great for single-machine parallelism.
-   **Cons**: Less mature than Spark for petabyte scale.

## Ray (The ML Choice)
-   **Paradigm**: Actor model + Task parallelism.
-   **Use Case**: Distributed Training (Ray Train), Hyperparameter Tuning (Ray Tune), Serving (Ray Serve).
-   **Pros**: Low latency, handles stateful actors (Simulators), native support for PyTorch/TF.

## DuckDB (The Laptop Warrior)
-   **Paradigm**: In-process OLAP database (like SQLite for Analytics).
-   **Pros**: Insanely fast on single machine. Can process larger-than-RAM datasets via spilling to disk.
-   **Strategy**: Use DuckDB for < 100GB. Move to Spark for > 1TB.
