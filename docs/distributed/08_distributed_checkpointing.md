# Distributed Checkpointing

## The Problem
A 1TB model cannot be saved by Rank 0 alone (OOM + Slow/Network bottleneck).

## Solutions
1.  **Local Save**: Each Rank saves its own shard (`part_0.pt`, `part_1.pt`...).
    -   *Pros*: Fast parallel write.
    -   *Cons*: Hard to load on different number of GPUs (Resharding needed).
2.  **TensorStore**: Google's library for saving massive arrays in parallel.
3.  **PyTorch Dist Checkpoint**: Standardized API for parallel save/load with auto-resharding support.

## Frequency
Checkpoints cost time. "Async Checkpointing" saves to CPU memory first, then writes to disk in background.
