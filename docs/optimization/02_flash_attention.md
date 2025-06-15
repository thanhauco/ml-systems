# FlashAttention: Fast and Memory-Efficient Exact Attention

## The IO Bottleneck
Standard Attention scales quadratically $O(N^2)$ in memory and runtime.
- A significant bottleneck is reading/writing the large $N \times N$ attention matrix to/from High Bandwidth Memory (HBM).

## Tiling and Recomputation
FlashAttention optimizes GPU IO by:
1.  **Tiling**: Splitting Q, K, V into blocks that fit in fast SRAM.
2.  **Recomputation**: Recomputing attention scores during backward pass instead of storing the huge matrix.

## Result
- Faster training (2x-4x speedup).
- Longer context lengths (due to sub-quadratic memory footprint).
