from typing import List, Optional
from collections import Counter

def majority_vote(labels: List[Optional[int]]) -> Optional[int]:
    """
    Aggregates weak labels or crowd votes using Majority Vote.
    """
    # Filter out abstentions (None)
    valid_labels = [l for l in labels if l is not None]
    
    if not valid_labels:
        return None
    
    counts = Counter(valid_labels)
    # Get most common
    most_common, count = counts.most_common(1)[0]
    
    # Check for tie
    if len(counts) > 1 and counts.most_common(2)[1][1] == count:
        return None # Tie-break strategy needed (random or abstain)
        
    return most_common

def weighted_vote(labels: List[Optional[int]], weights: List[float]) -> Optional[int]:
    """
    Weighted vote based on labeler accuracy/confidence.
    """
    scores = {}
    for label, weight in zip(labels, weights):
        if label is None:
            continue
        scores[label] = scores.get(label, 0) + weight
    
    if not scores:
        return None
        
    return max(scores, key=scores.get)
