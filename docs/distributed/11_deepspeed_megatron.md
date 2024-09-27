# DeepSpeed & Megatron-LM

## DeepSpeed (Microsoft)
-   Focus: Usage/Accessibility.
-   ZeRO Optimizer.
-   Offload (CPU/NVMe).
-   Sparse Attention.
-   Config-based JSON setup.

## Megatron-LM (NVIDIA)
-   Focus: Performance/Scale.
-   The reference implementation for Tensor Parallelism and Pipeline Parallelism.
-   Used to train GPT-3, Megatron-Turing NLG.
-   Complex codebase, heavily optimized CUDA kernels.

## Convergence
Most modern training stacks (e.g., NeMo) mix both.
