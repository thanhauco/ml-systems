# Inference-Time Compute & System 2 Scaling

## The Shift to System 2
In 2025, the focus of Large Language Models (LLMs) shifted from purely pre-training scale ("System 1" intuition) to inference-time compute ("System 2" reasoning). Code-named projects like "Strawberry" and "Orion" demonstrated that allowing a model to "think" for longer—generating hidden chains of thought (CoT) before outputting an answer—could solve problems that were previously impossible.

## Scaling Laws for Reasoners
We now understand that compute is fungible between training and inference.
- **Training Compute**: Compresses world knowledge into weights.
- **Inference Compute**: Expands search space to find optimal paths through that knowledge.

The new scaling law: `Performance ~ f(Training Compute) + g(Inference Compute)`.

## Mechanisms
1.  **Chain of Thought (CoT)**: Linear step-by-step reasoning.
2.  **Tree of Thoughts (ToT)**: Exploring branching possibilities, backtracking when a branch looks unpromising.
3.  **Process Reward Models (PRMs)**: Verifiers that score individual steps of reasoning rather than just the final answer.
