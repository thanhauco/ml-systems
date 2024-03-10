# Kubernetes (K8s) for ML

## Why K8s?
Standardization. Same stack for Web, DB, and ML.

## ML Operators
K8s doesn't understand "AllReduce". It just knows Pods.
1.  **Kubeflow Training Operator**:
    -   CRDs: `PyTorchJob`, `TFJob`.
    -   Manages `Master`, `Worker` pods.
    -   Sets up `MASTER_ADDR` and `MASTER_PORT` env vars automatically.
2.  **Volcano / Kueue**:
    -   Batch scheduling. "Gang Scheduling" (start all pods or none).
    -   Bin packing for GPU fragmentation.

## Challenges
-   Complexity.
-   Handling node failures (Pods define the job).
-   Storage mounting (PVCs vs HostPath).
