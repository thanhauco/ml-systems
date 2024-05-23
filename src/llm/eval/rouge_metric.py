class TextOverlapMetrics:
    """
    Simple n-gram overlap metrics (Mock ROUGE/BLEU).
    """
    
    @staticmethod
    def rouge_1(reference: str, hypothesis: str):
        """
        Overlap of unigrams.
        """
        ref_tokens = set(reference.split())
        hyp_tokens = set(hypothesis.split())
        
        overlap = len(ref_tokens.intersection(hyp_tokens))
        return overlap / len(ref_tokens) if ref_tokens else 0.0

if __name__ == "__main__":
    score = TextOverlapMetrics.rouge_1("the cat sat on mat", "the cat sat on the mat")
    print(f"ROUGE-1: {score:.2f}")
