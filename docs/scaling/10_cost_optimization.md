# Cost Optimization at Scale

## The Bill
Training Llama-3 can cost $10M+.

## Strategies
1.  **Spot Instances**: Bid on unused AWS capacity (60-90% discount).
    -   *Risk*: Preemption. Needs robust checkpointing.
2.  **Mixed Precision**: FP16 uses 50% memory/compute of FP32.
3.  **Gradient Accumulation**: Use smaller GPUs with larger effective batch size.
4.  **Reserved Instances**: Commit to 1-3 years for steady workloads.

## FinOps
-   **Tagging**: "Cost Center: Research vs Prod".
-   **Auto-shutdown**: Kill Jupyter notebooks after 2 hours of idle.
