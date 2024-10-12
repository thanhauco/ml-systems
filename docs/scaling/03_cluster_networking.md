# Cluster Networking

## The Bottleneck is often Network
Distributed training requires exchanging gradients every step.

## Technologies
1.  **RDMA (Remote Direct Memory Access)**:
    -   GPU memory to GPU memory on another node *without* CPU involvement.
    -   Bypasses kernel OS stack. Zero-copy.
2.  **InfiniBand (IB)**:
    -   Low latency, high throughput tailored for HPC.
    -   Topology matters (Fat Tree, DragonFly).
3.  **RoCE (RDMA over Converged Ethernet)**:
    -   RDMA semantics over standard Ethernet hardware (cheaper than IB).

## Collective Operations
-   **AllReduce**: Everyone gets the sum.
-   **AllGather**: Everyone gets all data.
-   **ReduceScatter**: Sum and split.
