# Reinforcement Learning from Human Feedback (RLHF)

## The Alignment Process
Pre-training predicts the next token (completion). RLHF trains the model to be *helpful* and *harmless*.

## Steps
1.  **SFT (Supervised Fine-Tuning)**: Train on high-quality instruction-response pairs.
2.  **Reward Modeling (RM)**:
    -   Collect comparison data: Human ranks Output A vs Output B.
    -   Train a Reward Model to predict the human score.
3.  **PPO (Proximal Policy Optimization)**:
    -   Optimize the Policy (LLM) to maximize Reward.
    -   Constraint: KL Divergence penalty to prevent drifting too far from SFT model.

## Alternatives
-   **DPO (Direct Preference Optimization)**: Optimizes policy directly from preferences without explicit Reward Model. More stable.
