# Quantization for LLMs

## Loading Big Models on Small GPUs

## Formats
1.  **GPTQ (Post-Training Quantization)**:
    -   Quantizes weights row-by-row based on inverse Hessian.
    -   Fast inference, typically 4-bit.
2.  **AWQ (Activation-aware Weight Quantization)**:
    -   Protects "salient" weights (important ones) from rigorous quantization.
    -   Better accuracy than GPTQ.
3.  **GGUF (llama.cpp)**:
    -   CPU + Apple Silicon optimization.
    -   `k-quants` (e.g., Q4_k_m).

## FP8 Training
-   H100 GPUs support FP8 tensor cores. 2x throughput of BF16.

