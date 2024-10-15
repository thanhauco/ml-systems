# The 3D Parallelism Cube

## Why simple DDP isn't enough
Distributed Data Parallel (DDP) replicates the model on every GPU.
If Model Size > GPU Memory, DDP fails (OOM).

## The Dimensions
1.  **Data Parallelism (DP)**: Split the Batch. Replicate the Model.
    -   *Constraint*: Model must fit in memory.
2.  **Tensor Parallelism (TP)**: Split the Layers. Slice matrices horizontally/vertically.
    -   *Constraint*: High communication overhead (needs NVLink).
3.  **Pipeline Parallelism (PP)**: Split the Model depth-wise. GPU 1 does layers 1-4, GPU 2 does 5-8.
    -   *Constraint*: Bubble time (idle GPUs waiting for data).

## 3D Parallelism
Combining all three (DP + TP + PP) to train trillion-parameter models on thousands of GPUs.
