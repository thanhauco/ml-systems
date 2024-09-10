# Visualizing Distributed Training

## Key Metrics to Watch
1.  **Loss Spike**: Sudden jump in loss. Can indicate numerical instability (NaNs) or bad data.
2.  **Gradient Norm**: Should decrease or stabilize. If increasing, lower LR.
3.  **Communication Overhead**: `Waiting for AllReduce`.
4.  **Stragglers**: One GPU is slower (thermal throttle?), slowing down the whole Sync SGD group.

## Tools
-   **TensorBoard / WandB**: Loss curves.
-   **PyTorch Profiler**: CUDA kernel timelines. "Where is the bubble?"
