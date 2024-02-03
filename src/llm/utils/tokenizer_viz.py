class TokenizerVisualizer:
    """
    Debug helper to see how text is split.
    """
    
    def visualize(self, tokenizer, text):
        # tokens = tokenizer.encode(text)
        # decoded = [tokenizer.decode([t]) for t in tokens]
        # print(f"Tokens: {decoded}")
        print(f"Visualizing tokens for: {text}")
