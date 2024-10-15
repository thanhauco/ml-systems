# Scaling ML Infrastructure

## The Challenge
ML is no longer just code. It's:
1.  **Compute**: Thousands of GPUs.
2.  **Data**: Petabytes of storage.
3.  **Network**: Terabits per second.

## The Abstraction Ladder
-   **Level 0 (Raw)**: SSH into a box, run `python train.py`.
-   **Level 1 (Batch)**: Slurm/LSF. "Schedule this script on 4 nodes".
-   **Level 2 (Containers)**: Kubernetes/Docker. Reusable environments.
-   **Level 3 (Orchestration)**: Kubeflow/Ray. "Hyperparameter sweep over 100 trials".
-   **Level 4 (Serverless)**: "Here is my model, give me an API".

## Key Metrics
-   **JCT**: Job Completion Time.
-   **Utilization**: Are GPUs running at 100%?
-   **Throughput**: Samples per second.
