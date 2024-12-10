from typing import List

class HybridRetriever:
    """
    Combines Dense Retrieval (Vector) + Sparse Retrieval (Keyword/BM25).
    """
    
    def __init__(self, vector_store, keyword_index=None):
        self.vector_store = vector_store
        self.keyword_index = keyword_index

    def search(self, query: str, top_k: int = 5) -> List[str]:
        print(f"Searching for: '{query}'")
        
        # 1. Vector Search
        dense_results = self.vector_store.similarity_search(query, k=top_k)
        
        # 2. Keyword Search (Mock)
        sparse_results = [f"Keyword match for {query}"]
        
        # 3. Reciprocal Rank Fusion (RRF) could go here
        combined = dense_results + sparse_results
        
        # Deduplicate
        return list(set(combined))[:top_k]

