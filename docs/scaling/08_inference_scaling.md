# Inference Scaling

## Latency vs Throughput
-   **Latency**: Time for one request. (Critical for Search/Ads).
-   **Throughput**: Requests per second. (Critical for Batch/Offline).

## Techniques
1.  **Dynamic Batching**: Wait 5ms to group 10 requests into 1 batch. GPU works better on batches.
2.  **Continuous Batching (Orca)**: Don't wait for the whole batch to finish generation. Eject finished sequences, insert new ones.
3.  **Model Parallelism**: Tensor Parallelism reduces latency (split matrix mul across 8 GPUs). Pipeline Parallelism increases throughput.

## Tools
-   **NVIDIA Triton Inference Server**: C++ backend, standard K8s deployment.
-   **TGI / vLLM**: Specialized for LLMs.
