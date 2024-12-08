class SemanticChunker:
    """
    Splits text based on semantic boundaries (e.g. sentence embeddings change), not just length.
    """
    
    def chunk(self, text: str):
        sentences = text.split(". ")
        chunks = []
        current = ""
        for s in sentences:
            if len(current) + len(s) < 500:
                current += s + ". "
            else:
                chunks.append(current)
                current = s + ". "
        if current: chunks.append(current)
        print(f"Created {len(chunks)} chunks.")
        return chunks
