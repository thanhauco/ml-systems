# Parameter Efficient Fine-Tuning (PEFT)

## The Problem
Full fine-tuning updates all weights. For Llama-70B, that's 140GB of gradients. Too expensive.

## LoRA (Low-Rank Adaptation)
-   Hypothesis: Weight updates have low intrinsic rank.
-   Method: Freeze $W$. Inject $A \times B$ (low rank matrices).
-   $W' = W + \Delta W = W + BA$.
-   Result: Train < 1% of parameters.

## QLoRA
-   LoRA + 4-bit Quantization of base model ($W$).
-   Train LoRA adapters in FP16.
-   Result: Finetune 70B model on a single 48GB GPU.

## Adapters
-   Insert tiny MLP layers between Transformer blocks.
-   Older method, slightly higher latency than LoRA (which can be merged).
