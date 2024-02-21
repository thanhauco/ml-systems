from typing import List, Dict, Any
import math

class Encoder:
    def fit(self, data: List[Any]):
        pass
    def transform(self, data: List[Any]) -> List[Any]:
        pass

class OneHotEncoder(Encoder):
    def __init__(self):
        self.vocab = {}

    def fit(self, data: List[str]):
        unique = sorted(list(set(data)))
        self.vocab = {val: i for i, val in enumerate(unique)}

    def transform(self, data: List[str]) -> List[List[int]]:
        size = len(self.vocab)
        output = []
        for item in data:
            vec = [0] * size
            if item in self.vocab:
                vec[self.vocab[item]] = 1
            output.append(vec)
        return output

class TargetEncoder(Encoder):
    """
    Encodes categorical variables by the mean of the target variable.
    Risk: Leakage if not done inside CV folds.
    """
    def __init__(self, smooth: int = 10):
        self.mapping = {}
        self.global_mean = 0.0
        self.smooth = smooth

    def fit(self, categories: List[str], targets: List[float]):
        self.global_mean = sum(targets) / len(targets)
        stats = {}
        for cat, target in zip(categories, targets):
            if cat not in stats:
                stats[cat] = {"sum": 0.0, "count": 0}
            stats[cat]["sum"] += target
            stats[cat]["count"] += 1
            
        # Smoothing
        for cat, stat in stats.items():
            count = stat["count"]
            mean = stat["sum"] / count
            # Blend with global mean based on count and smooth factor
            weight = count / (count + self.smooth)
            self.mapping[cat] = (mean * weight) + (self.global_mean * (1 - weight))

    def transform(self, categories: List[str]) -> List[float]:
        return [self.mapping.get(cat, self.global_mean) for cat in categories]
