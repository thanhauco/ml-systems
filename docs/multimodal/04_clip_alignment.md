# CLIP: Contrastive Language-Image Pretraining

## The objective
Maximize cosine similarity between correct (Image, Text) pairs.
Minimize similarity for incorrect pairs in the batch.

## Architecture
-   **Image Encoder**: ResNet or ViT.
-   **Text Encoder**: Transformer.
-   **Projection Head**: Maps both down to same dim (e.g., 512).

## Zero-Shot Classification
"A photo of a {label}".
Compare image embedding with embeddings of 1000 labels. Pick max.
