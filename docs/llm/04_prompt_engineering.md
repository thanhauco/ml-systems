# Prompt Engineering

## The Art of "Talking to the Model"

## Strategies
1.  **Zero-Shot**: Just ask. "Translate to Spanish: Hello".
2.  **Few-Shot (ICL)**: Give examples. "En: Hi -> Sp: Hola. En: Dog -> Sp: Perro. En: Cat ->".
3.  **Chain of Thought (CoT)**: "Let's think step by step". Increases math/logic performance.
4.  **ReAct**: "Reason + Act". Thought -> Action (Call Tool) -> Observation.

## Prompt Formats
-   **ChatML**: `<|im_start|>user\nHi<|im_end|><|im_start|>assistant`
-   **Llama-2**: `[INST] <<SYS>>...<</SYS>> User [/INST]`
-   *Critique*: Models are sensitive to exact formatting.
