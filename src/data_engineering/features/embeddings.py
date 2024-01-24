from typing import List
# Mocking sentence_transformers to avoid heavy dependency
class SentenceTransformerWrapper:
    """
    Wrapper for HuggingFace Sentence Transformers.
    """
    
    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        self.model_name = model_name
        print(f"Loading Embedding Model: {model_name}")

    def encode(self, texts: List[str]) -> List[List[float]]:
        """
        Returns dummy vectors of size 384.
        """
        # Simulation
        return [[0.1] * 384 for _ in texts]

class TFIDFVectorizer:
    """
    Simple scratch implementation of TF-IDF.
    """
    def __init__(self):
        self.idf = {}
        self.vocab = {}

    def fit(self, documents: List[str]):
        # Calculate IDF...
        pass

    def transform(self, documents: List[str]) -> List[List[float]]:
        # Calculate TF * IDF...
        return []
