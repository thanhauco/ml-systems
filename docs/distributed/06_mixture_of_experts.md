# Mixture of Experts (MoE)

## Sparse Models
GPT-4 is likely an MoE.
Parameters: 1.8 Trillion. Active Parameters: ~200 Billion per token.

## Architecture
-   **Router (Gating Network)**: Decides which "Expert" processes the token. "Top-2 gating".
-   **Experts**: Independent Feed Forward Networks (FFNs).

## Load Balancing
If the router sends all tokens to Expert 1, we lose parallelism benefits.
*Auxiliary Loss*: Penalizes router for maximizing variance of expert usage.

## Distributed MoE
Experts are distributed across GPUs. "Expert Parallelism".
Requires `All-to-All` communication (Tokens shuffling to experts).

