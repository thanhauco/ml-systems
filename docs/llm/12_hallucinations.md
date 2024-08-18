# Hallucinations

## "Confidently Wrong"
The model predicts the most probable next token, not the truth.

## Types
1.  **Fact fabrication**: "The Eiffel Tower is in Berlin."
2.  **Reasoning error**: "10 + 10 = 25".
3.  **Faithfulness error**: Ignoring the provided context in RAG.

## Mitigation
1.  **RAG**: Ground generation in retrieved facts.
2.  **Prompt Engineering**: "If you don't know, say 'I don't know'".
3.  **CoT**: "Think step-by-step" reduces reasoning errors.
4.  **Self-Consistency**: Generate 5 answers, take the majority vote.

