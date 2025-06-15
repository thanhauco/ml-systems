# Zero Redundancy Optimizer (ZeRO)

## The Memory Bottleneck
Standard Data Parallelism (DDP) replicates model states across all GPUs.
- **Problem**: Redundant copies of weights, gradients, and optimizer states consume massive VRAM.

## ZeRO Stages
1.  **Stage 1 (Optimizer States)**: Partition the optimizer state across data parallel processes.
2.  **Stage 2 (Gradients)**: Partition gradients.
3.  **Stage 3 (Parameters)**: Partition the model parameters themselves.

## Impact
ZeRO-3 allows training models with billions of parameters on limited hardware by treating aggregate cluster memory as a single pool.
