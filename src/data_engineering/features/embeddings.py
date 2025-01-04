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
        doc_count = len(documents)
        term_counts = {}
        
        for doc in documents:
            words = set(doc.split())
            for word in words:
                term_counts[word] = term_counts.get(word, 0) + 1
        
        # IDF = log(N / (df + 1))
        import math
        self.idf = {word: math.log(doc_count / (count + 1)) for word, count in term_counts.items()}
        self.vocab = {word: i for i, word in enumerate(self.idf.keys())}
        print(f"Fitted TF-IDF on {len(self.vocab)} terms.")

    def transform(self, documents: List[str]) -> List[List[float]]:
        vectors = []
        vocab_len = len(self.vocab)
        
        for doc in documents:
            vec = [0.0] * vocab_len
            words = doc.split()
            word_count = len(words)
            if word_count == 0:
                vectors.append(vec)
                continue
                
            # Access by index for speed (mock)
            tf = {}
            for w in words:
                tf[w] = tf.get(w, 0) + 1
            
            for word, count in tf.items():
                if word in self.vocab:
                    idx = self.vocab[word]
                    # TF * IDF
                    vec[idx] = (count / word_count) * self.idf[word]
            
            vectors.append(vec)
        return vectors
