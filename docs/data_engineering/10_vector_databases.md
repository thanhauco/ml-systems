# Vector Databases

## The Rise of Embeddings
In GenAI (LLMs), we convert text/images into dense vectors (e.g., 1536 dimensions).
traditional SQL databases are terrible at "Find the nearest vector to X".

## How Vector DBs Work
-   **Index**: HNSW (Hierarchical Navigable Small World) or IVF (Inverted File Index).
-   **Metric**: Cosine Similarity, Euclidiean Distance, Dot Product.
-   **Latency**: milliseconds for nearest neighbor search over millions of vectors.

## Top Players
1.  **Pinecone**: Managed, popular, easy.
2.  **Milvus**: Open source, scalable, complex.
3.  **Qdrant**: Rust-based, fast, developer friendly.
4.  **Chroma**: Simple, purely local or client-server, pythonic.
5.  **pgvector**: Postgres extension. Good if you want to keep everything in Postgres.

## RAG (Retrieval Augmented Generation)
1.  User asks "How do I reset my router?"
2.  Convert question to Vector.
3.  Query Vector DB for top 3 related manual pages.
4.  Feed [Question + Manual Pages] to LLM.
5.  LLM answers accurately using the retrieved context.
