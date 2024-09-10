# Evaluating Generative Models

## Image Quality
1.  **FID (Fréchet Inception Distance)**: Distance between distribution of real vs generated images (in Inception-v3 feature space). Lower is better.
2.  **IS (Inception Score)**: Clarity + Diversity. Higher is better.

## Alignment
-   **CLIP Score**: Cosine similarity between Prompt and Generated Image.

## Audio
-   **WER (Word Error Rate)**: For ASR.
-   **FAD (Fréchet Audio Distance)**: FID for audio.
