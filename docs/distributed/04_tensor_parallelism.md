# Tensor Parallelism (TP)

## Matrix Multiplication Sharding
$Y = X \cdot A$.
Split $A$ into $[A_1, A_2]$.
Compute $Y_1 = X \cdot A_1$ on GPU 1.
Compute $Y_2 = X \cdot A_2$ on GPU 2.
Concatenate $Y = [Y_1, Y_2]$.

## Megatron-LM Style
-   **Column Parallel Linear**: Split weight matrix by columns.
-   **Row Parallel Linear**: Split weight matrix by rows.
-   **Sequence Parallelism**: Split LayerNorm and Dropout along sequence dimension.

## Communication
Requires an `AllReduce` in the forward pass (to combine results) and backward pass.
Very high bandwidth required. Usually restricted to GPUs inside the same Node (NVLink).
