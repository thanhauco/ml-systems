# Vision Transformers (ViT)

## "An Image is worth 16x16 Words"
1.  **Patchify**: Split image into 16x16 squares.
2.  **Linear Projection**: Flatten patches and map to embedding dim.
3.  **Positional Embedding**: Add learnable vector to know where the patch is.
4.  **Transformer Encoder**: Standard Self-Attention ($O(N^2)$).
5.  **CLS Token**: Special token for classification head.

## Inductive Bias
CNNs have translation invariance built-in. ViTs learn it from massive data (JFT-300M).
