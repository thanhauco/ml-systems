# Tree of Thoughts (ToT) Search

## Concept
Standard Autoregressive decoding is a "Greedy" or "Beam Search" process that commits to tokens early. Tree of Thoughts treats language generation as a search problem over high-level "thoughts" or semantic blocks.

## Components
1.  **Decomposer**: Breaks a prompt into smaller intermediate steps.
2.  **Generator**: Proposes $k$ possible next steps given the current state.
3.  **Evaluator (Verifier)**: Scores each proposed step (heuristic or model-based).
4.  **Search Algorithm**: BFS (Breadth-First Search) or DFS (Depth-First Search) traverses the tree.

## 2025 Evolution: "Internal" Search
While early ToT (2023) was explicit and external (Python scripts calling LLMs), 2025 models internalize this search. They perform "silent thinking" where the model explores reasoning paths in latent space or hidden output tokens before committing to the user-facing response.
