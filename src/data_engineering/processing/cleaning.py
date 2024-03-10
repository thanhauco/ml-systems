from typing import List, Dict, Any, Optional
import re

class TextCleaner:
    """
    Standard text normalization utilities.
    """
    
    @staticmethod
    def normalize(text: str) -> str:
        if not text:
            return ""
        # Lowercase
        text = text.lower()
        # Remove special chars (keep alphanum and spaces)
        text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
        # Collapse whitespace
        text = re.sub(r'\s+', ' ', text).strip()
        return text

    @staticmethod
    def remove_stopwords(text: str, stopwords: set) -> str:
        words = text.split()
        return " ".join([w for w in words if w not in stopwords])

class OutlierRemover:
    """
    Numeric outlier detection.
    """
    
    @staticmethod
    def z_score_filter(data: List[float], threshold: float = 3.0) -> List[float]:
        if not data:
            return []
        mean = sum(data) / len(data)
        variance = sum((x - mean) ** 2 for x in data) / len(data)
        std = variance ** 0.5
        
        if std == 0:
            return data
            
        return [x for x in data if abs((x - mean) / std) < threshold]
