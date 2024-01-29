# Quantization Deep Dive

## Concept
Map continuous float32 values `[-10.5, 2.3, ...]` to discrete int8 integers `[-128, 127]`.
Equation: `r = S(q - Z)`
-   `r`: Real value (float)
-   `S`: Scale (float)
-   `q`: Quantized value (int8)
-   `Z`: Zero-point (int8)

## Types
1.  **Post-Training Quantization (PTQ)**:
    -   Train in FP32.
    -   Calibrate on representative dataset to find min/max.
    -   Convert weights to INT8.
    -   *Pros*: Easy. *Cons*: Accuracy drop for small models.

2.  **Quantization-Aware Training (QAT)**:
    -   Insert "Fake Quantize" nodes during training.
    -   The model "learns" to round values to nearest INT8 bucket.
    -   *Pros*: Best accuracy. *Cons*: Complex training setup.

## Symmetric vs Asymmetric
-   **Symmetric**: Range `[-max, +max]`. Zero point is 0. Faster (simpler math).
-   **Asymmetric**: Range `[min, max]`. Zero point is arbitrary. Better for ReLU (0 to inf).

