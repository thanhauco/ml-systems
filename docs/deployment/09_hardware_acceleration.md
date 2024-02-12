# Hardware Acceleration for Serving

## CPU (Central Processing Unit)
-   **Pros**: Cheap, available everywhere, low latency for very small models (Decision Trees) or very small batch size (=1).
-   **Optimization**: AVX-512 instructions (Intel), AMX (Sapphire Rapids).

## GPU (Graphics Processing Unit)
-   **Pros**: Massive parallelism. Essential for Deep Learning / LLMs.
-   **Cons**: Expensive, high power consumption.
-   **Metric**: Throughput (Tokens/sec or Images/sec).
-   **MIG (Multi-Instance GPU)**: Split one A100 into 7 smaller slices to serve 7 small models.

## TPU (Tensor Processing Unit)
-   Google's custom ASIC for Matrix Math.
-   **Pros**: Higher performance/watt than GPU.
-   **Cons**: Not as flexible. Optimized for XLA-compatible graphs.

## FPGA / ASIC (Groq, Cerebras)
-   **Groq**: Deterministic latency (LPU). No HBM bandwidth bottleneck.
-   **Edge**: Neural Processing Units (NPU) on Phones (Apple Neural Engine).

## Choosing Hardware
1.  **LLM (70B)**: Needs multi-GPU (A100/H100) for VRAM.
2.  **ResNet50**: T4 or L4 GPU is sufficient.
3.  **XGBoost**: CPU is usually faster.
