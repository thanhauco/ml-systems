# Pipeline Parallelism (PP)

## Inter-Layer Parallelism
Model has 32 layers. 4 GPUs.
GPU 1: Layers 1-8.
GPU 2: Layers 9-16...

## The Bubble Problem
GPU 4 is idle while GPU 1 is processing Batch 1.
GPU 1 is idle while GPU 4 is processing Batch 1 gradients.
"Idle time" = Bubble.

## Solutions
1.  **GPipe**: Micro-batches. Split batch into M chunks. Inject all chunks. Reduce bubble size.
2.  **1F1B (One Forward One Backward)**: Schedule forward and backward passes interleaved to keep GPUs busy.
