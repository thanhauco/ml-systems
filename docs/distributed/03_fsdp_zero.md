# ZeRO: Zero Redundancy Optimizer

## The Memory Problem
Training a 1.5B parameter model (FP16) requires ~24GB memory.
-   Weights: 3GB
-   Gradients: 3GB
-   Optimizer States (Adam): 18GB !

## Stages
1.  **ZeRO-1**: Shard Optimizer States. (4x memory savings).
2.  **ZeRO-2**: Shard Gradients. (8x savings).
3.  **ZeRO-3**: Shard Model Parameters. (Linear savings with N GPUs).

## FSDP (Fully Sharded Data Parallel)
PyTorch's native implementation of ZeRO-3.
On forward pass, it gathers weights (AllGather). Computes. Discards weights to free memory.
On backward pass, it gathers weights again.
