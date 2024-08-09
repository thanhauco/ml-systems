# Video Generation

## The 4th Dimension: Time
Images are $(C, H, W)$. Video is $(T, C, H, W)$.

## Challenges
-   **Temporal Consistency**: Objects shouldn't flicker or morph randomly.
-   **Compute**: $T$ times more data.

## Approaches
1.  **3D UNet**: Convolutions over (Time, Height, Width).
2.  **Temporal Attention**: Attention over frames.
3.  **SORA**: Video patches as tokens + Diffusion Transformer (DiT).
