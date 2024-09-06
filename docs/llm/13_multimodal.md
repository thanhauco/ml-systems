# Multimodal LLMs (LMMs)

## Beyond Text
GPT-4V, Gemini, Claude 3. Can see images and hear audio.

## Architecture
-   **Vision Encoder**: CLIP / SigLIP extracts image features.
-   **Projector**: Maps image features to Text Embedding space.
-   **LLM Backbone**: Processes image embeddings as if they were text tokens.

## Use Cases
1.  **VQA**: Visual Question Answering. "What is wrong with this car engine?"
2.  **OCR**: Reading handwriting.
3.  **Video Understanding**: "Summarize this clip".

## Challenges
-   **Hallucination**: "I see a cat" when there is none.
-   **Spatial Reasoning**: "Is the cup to the left or right?" (Often hard for standard LMMs).
