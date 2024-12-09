# Orchestration with Kubernetes (K8s)

## Why K8s for ML?
Services need to scale up (Monday morning) and scale down (Sunday night). K8s handles this declarative management.

## Key Concepts
1.  **Pod**: The smallest unit. Runs your Docker container.
2.  **Deployment**: Manages Replicas of Pods. "Make sure 3 copies of Model V1 are running".
3.  **Service**: Stable network endpoint (Load Balancer) to access the dynamic pods.
4.  **Ingress**: Exposes the service to the outside world (HTTP routing).

## Resource Management
ML workloads are resource hungry.
-   **Requests**: Guaranteed resources. "I need 2 CPUs and 4GB RAM".
-   **Limits**: Hard cap. "Kill me if I use > 8GB RAM".
-   **GPU Scheduling**: `nvidia.com/gpu: 1` ensures the pod lands on a node with a GPU.

## KServe / Seldon Core
ML-specific CRDs (Custom Resource Definitions) on top of K8s.
-   Abstracts away Deployment/Service.
-   Provides out-of-the-box Canary, Shadowing, and Explainer patterns.

