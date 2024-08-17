# Retrieval Augmented Generation (RAG)

## Why RAG?
-   **Hallucination**: LLMs make things up.
-   **Knowledge Cutoff**: LLMs don't know news from today.
-   **Private Data**: LLMs don't know your emails.

## Architecture
1.  **User Query**: "Earnings for Q3?"
2.  **Retriever**: Find relevant chunks in Vector DB.
3.  **Generator**: `Prompt = Context + Query`.
4.  **Answer**: "Based on the documents, earnings were X".

## Advanced RAG
-   **Hybrid Search**: Keyword (BM25) + Semantic (Cosine Sim).
-   **Re-ranking**: Retrieve 100 docs, use heavy Cross-Encoder to sort top 5.
-   **Query Rewriting**: Break complex query into sub-questions.
-   **HyDE**: Hypothetical Document Embeddings.
