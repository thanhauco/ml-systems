class AugmentedGenerator:
    """
    Constructs the Prompt and calls LLM.
    """
    
    def __init__(self, llm_client):
        self.llm = llm_client
        self.template = """
You are a helpful assistant. Use the context below to answer the user's question.

Context:
{context}

Question:
{question}

Answer:
"""

    def generate(self, user_query: str, retrieved_docs: list):
        context_str = "\n---\n".join(retrieved_docs)
        prompt = self.template.format(context=context_str, question=user_query)
        
        print("Sending prompt to LLM...")
        # response = self.llm.complete(prompt)
        response = "This is a generated answer based on the context."
        return response

