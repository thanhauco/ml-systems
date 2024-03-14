class CrossEncoderReranker:
    """
    Re-ranks retrieved documents using a Cross-Encoder (e.g. BERT).
    Input: (Query, Doc). Output: Similarity Score.
    """
    
    def rerank(self, query: str, docs: list, top_n: int = 3):
        print(f"Reranking {len(docs)} documents...")
        scored = []
        for doc in docs:
            # score = model.predict(query, doc)
            score = 0.9 # Mock
            scored.append((doc, score))
            
        # Sort by score desc
        scored.sort(key=lambda x: x[1], reverse=True)
        return [doc for doc, score in scored[:top_n]]
