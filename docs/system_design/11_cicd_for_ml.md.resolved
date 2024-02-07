# CI/CD for Machine Learning (MLOps)

## Continuous Integration (CI)
CI is about merging code often and validating it. In ML, "Code" includes Data and Configs.
-   **Trigger**: Git Commit.
-   **Steps**:
    1.  Linting (Ruff/Black).
    2.  Type Checking (MyPy).
    3.  Unit Tests (PyTest).
    4.  Build Docker Image.

## Continuous Delivery (CD)
CD is about automating the release.
-   **Trigger**: Merge to `main` or Tag.
-   **Steps**:
    1.  Push Docker Image to Registry.
    2.  Update K8s manifest / Helm chart.
    3.  Deploy to Staging.

## Continuous Training (CT) - The ML Speciality
Code hasn't changed, but Data has.
-   **Trigger**:
    -   *Schedule*: Every Sunday.
    -   *Metric*: "Accuracy dropped below 80%".
    -   *Data*: "New partition of data arrived".
-   **Pipeline**:
    1.  Pull latest code + latest data.
    2.  Run Training Job.
    3.  Evaluate against Test Set.
    4.  Evaluate against "Golden Set".
    5.  Register Model to Registry (e.g., MLflow) as "Candidate".

## Continuous Monitoring (CM)
-   The feedback loop closing.
-   Monitor:
    -   **System**: Latency, CPU, RAM.
    -   **Data**: Drift (Input distribution).
    -   **Model**: Performance (Accuracy, F1).

## The Maturity Levels (Google MLOps Guide)
1.  **Level 0 (Manual)**: Script driven, manual handoffs.
2.  **Level 1 (Pipeline Auto)**: Automated Training pipeline. Continuous Training.
3.  **Level 2 (CI/CD)**: Automated pipeline deployment. Full MLOps.
