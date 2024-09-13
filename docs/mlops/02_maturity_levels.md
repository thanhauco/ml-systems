# MLOps Maturity Levels (Based on Google)

## Level 0: Manual Process
-   **Characteristics**:
    -   Data Scientists hand off Juyter Notebooks to Engineering.
    -   "Throw it over the wall".
    -   No active monitoring.
    -   Retraining is ad-hoc (once a year).
-   **Risks**: Training-Serving skew, silent failures, bus factor.

## Level 1: ML Pipeline Automation
-   **Characteristics**:
    -   Automated training pipeline (Airflow/Kubeflow).
    -   Continuous Training (CT): Triggered by new data.
    -   Data validation before training.
    -   Metadata tracking (MLflow).
-   **Goal**: Rapid experimentation.

## Level 2: CI/CD Pipeline Automation
-   **Characteristics**:
    -   CI/CD for the *pipeline code* itself.
    -   Automated testing of new model code.
    -   A/B Testing infrastructure.
    -   Feature Store implementation.
-   **Goal**: Reliable, rapid deployment of new architectures.
