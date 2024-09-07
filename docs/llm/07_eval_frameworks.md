# Evaluation Frameworks for LLMs

## The Difficulty
"Is this poem good?" is hard to measure with code.

## Benchmarks
1.  **MMLU (Massive Multitask Language Understanding)**: Multiple choice questions across 57 subjects (Math, Law, Medicine).
2.  **HELM (Holistic Evaluation of Language Models)**: Accuracy, Toxicity, Fairness, Efficiency.
3.  **HumanEval**: Python coding problems.

## Metrics
-   **N-gram Overlap**: ROUGE, BLEU. (Bad for generative tasks, good for translation).
-   **Model-Based**: BERTScore.
-   **LLM-as-a-Judge**: Ask GPT-4 to grade GPT-3's answer on scale 1-10.

## Tools
-   **DeepEval**: Unit tests for LLMs.
-   **Ragas**: RAG specific metrics (Faithfulness, Context Relevance).
