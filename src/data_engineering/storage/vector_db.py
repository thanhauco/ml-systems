from typing import List, Dict, Any
import uuid

class VectorDBClient:
    """
    Generic Interface for Vector Databases (Qdrant/Chroma).
    """
    
    def __init__(self, collection_name: str, dimension: int):
        self.collection = collection_name
        self.dim = dimension
        self.index = {} # Simple in-memory mock

    def upsert(self, vectors: List[List[float]], metadata: List[Dict[str, Any]]):
        """
        Inserts vectors with associated metadata.
        """
        if len(vectors) != len(metadata):
            raise ValueError("Vectors and Metadata length mismatch")
            
        print(f"Upserting {len(vectors)} vectors to {self.collection}")
        for vec, meta in zip(vectors, metadata):
            id_ = str(uuid.uuid4())
            self.index[id_] = {"vector": vec, "meta": meta}

    def search(self, query_vector: List[float], limit: int = 5) -> List[Dict[str, Any]]:
        """
        Finds nearest neighbors (mocked).
        """
        print(f"Searching top {limit} in {self.collection}")
        # Return random items from index
        keys = list(self.index.keys())[:limit]
        return [{"id": k, "score": 0.99, "payload": self.index[k]["meta"]} for k in keys]
