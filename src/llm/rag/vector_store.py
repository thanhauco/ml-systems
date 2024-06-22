class SimpleVectorStore:
    """
    Mock wrapper for FAISS / ChromaDB.
    """
    
    def __init__(self):
        self.documents = []
        self.embeddings = []

    def add_documents(self, docs: list, embeddings: list):
        self.documents.extend(docs)
        self.embeddings.extend(embeddings)
        print(f"Stored {len(docs)} documents.")

    def similarity_search(self, query: str, k: int = 3):
        # Mock search
        print(f"Vector search for '{query}'")
        if not self.documents: return []
        return self.documents[:k]
