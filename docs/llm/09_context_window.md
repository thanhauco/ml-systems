# Handling the Context Window

## The Constraint
GPT-4 has 128k context. Llama-2 has 4k. Memory is quadratic $O(N^2)$ in vanilla Transformers (Attention Matrix).

## Techniques for "Infinite" Context
1.  **Rolling Window**: Only look at last N tokens.
2.  **RAG**: Swap context in and out dynamically.
3.  **Summarization**: Compress history into a summary string.
4.  **Attention Sinks**: Keep the first few tokens (starting anchor) to maintain stability.
5.  **RoPE Scaling**: Interpolate position embeddings to handle longer sequences than trained on.

## Flash Attention
Hardware optimization. Tiles memory access to reduce High Bandwidth Memory (HBM) reads/writes. Speeds up training/inference linear to sequence length.
