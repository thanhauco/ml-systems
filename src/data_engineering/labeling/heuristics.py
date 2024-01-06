from typing import Dict, Any, Optional

class WeakLabeler:
    """
    Programmatic labeling function base.
    """
    
    def apply(self, record: Dict[str, Any]) -> Optional[int]:
        """Returns Label (int) or None (Abstain)."""
        raise NotImplementedError

class KeywordHeuristic(WeakLabeler):
    def __init__(self, keyword: str, label: int):
        self.keyword = keyword
        self.label = label

    def apply(self, record: Dict[str, Any]) -> Optional[int]:
        text = record.get("text", "").lower()
        if self.keyword in text:
            return self.label
        return None

class LengthHeuristic(WeakLabeler):
    def __init__(self, min_len: int, label: int):
        self.min_len = min_len
        self.label = label

    def apply(self, record: Dict[str, Any]) -> Optional[int]:
        if len(record.get("text", "")) < self.min_len:
            return self.label
        return None
