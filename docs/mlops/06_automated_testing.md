# Automated Testing in MLOps

## Beyond Unit Tests
Standard software testing (`assert add(1, 1) == 2`) is insufficient for ML because the *data* is also part of the source code.

## The Testing Pyramid for ML

### 1. Data Tests (The Foundation)
-   **Schema Validation**: "Age column must be int".
-   **Distribution Tests**: "Mean(Age) should be between 18 and 100".
-   **Null Checks**: "Email cannot be null".
-   *Tools*: Great Expectations, Pandera.

### 2. Model Tests (Unit)
-   **Invariance Tests**: `Predict("I love this movie")` should equal `Predict("I LOVE this movie")`.
-   **Directional Expectation**: Adding "not" should flip sentiment.
-   **Shape Checks**: Output tensor should be (Batch, Classes).

### 3. Integration Tests (Pipeline)
-   Run the full ETL -> Train -> Save loop on a tiny "Toy Dataset" (e.g., 10 rows).
-   Purpose: Ensure the pipeline doesn't crash.

### 4. System Tests (Load/Latency)
-   Can the model handle 1000 QPS? (Locust).
