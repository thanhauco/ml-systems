# Large Batch Optimization

## The Generalization Gap
Large batch size (>8k) often leads to worse test accuracy.
Sharp Minima vs Flat Minima.

## Scaling Learning Rate
-   **Linear Scaling Rule**: If you multiply batch size by $k$, multiply LR by $k$.
-   **Square Root Rule**: Multiply LR by $\sqrt{k}$.

## Special Optimizers
1.  **LARS (Layer-wise Adaptive Rate Scaling)**: Normalizes update based on weight norm vs gradient norm per layer. Used for ResNet-50 on ImageNet in minutes.
2.  **LAMB (Layer-wise Adaptive Moments for BERT)**: LARS + Adam. Essential for large batch BERT training.
