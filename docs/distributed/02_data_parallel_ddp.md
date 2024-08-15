# Distributed Data Parallel (DDP)

## How it works
1.  **Forward Pass**: Same model, different data batch on each GPU.
2.  **Backward Pass**: Compute gradients locally.
3.  **Gradient Synchronization**: `AllReduce` sum of gradients across all GPUs.
4.  **Optimizer Step**: Apply averaged gradients.

## Bucketing
Sending one gradient at a time is slow (latency).
DDP groups small gradients into "buckets" (e.g., 25MB) and AllReduces the bucket.

## Async vs Sync
-   **Sync SGD**: Everyone waits for everyone. Mathematically equivalent to large batch SGD.
-   **Async SGD**: Parameter Server updates as soon as one worker finishes. Stale gradients problem.
