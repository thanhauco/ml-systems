# Multimodal RAG

## Retrieval
Query: "Find me the chart showing sales growth."
-   Embed query with CLIP text encoder.
-   Search vector DB containing CLIP image embeddings of charts.

## Generation
-   Feed retrieved image + user query to GPT-4V / LLaVA.
-   "Look at this retrieved chart and answer..."

## Multi-Vector Retriever
Store summaries (text) for retrieval, but pass full images to the model.
