# Model Optimization

## Why Optimize?
-   Running BERT-Large (340M params) takes 1.5GB VRAM and 50ms latency.
-   Optimized, it can run on CPU in 20ms or Mobile device.

## 1. Quantization
Reduce precision of weights/activations.
-   **FP32 (32-bit float)**: Standard training.
-   **FP16 (16-bit float)**: Standard GPU inference. 2x speedup.
-   **INT8 (8-bit integer)**: 4x compression. Harder to maintain accuracy.
    -   *Post-Training Quantization (PTQ)*: Calibrate on a small dataset after training.
    -   *Quantization-Aware Training (QAT)*: Simulate quantization noise during training.

## 2. Pruning
Remove "unimportant" connections (weights near zero).
-   **Unstructured Pruning**: Sets individual weights to 0. Sparse matrices. Hard to accelerate on GPUs.
-   **Structured Pruning**: Removes entire neurons or channels. Smaller matrix. Easy speedup.

## 3. Knowledge Distillation
Train a small "Student" to assume the logs of a large "Teacher".
(Covered in System Design, but applied here for latency).

## 4. Graph Optimization
-   **Operator Fusion**: Combine `Conv2D + BatchNorm + ReLU` into a single GPU kernel to save memory bandwidth.
-   **Constant Folding**: Pre-compute expressions known at compile time.
