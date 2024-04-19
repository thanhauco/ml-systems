# Introduction to Large Language Models

## The Transformer Architecture
"Attention is All You Need" (2017).
-   **Encoder**: Processes input text (BERT).
-   **Decoder**: Generates output text (GPT).
-   **Encoder-Decoder**: Translates (T5).
-   **Self-Attention**: $Attention(Q, K, V) = softmax(\frac{QK^T}{\sqrt{d_k}})V$.

## The Scale Era
-   **Scaling Laws**: Performance $\propto$ Parameters + Data + Compute.
-   **Foundation Models**: Trained once on internet-scale data. Adapted via prompting or finetuning.

## Lifecycle
1.  **Pre-training**: Learn world knowledge (Expensive).
2.  **SFT (Supervised Fine-Tuning)**: Learn to follow instructions.
3.  **RLHF**: Learn preferences (Safety/Helpfulness).
4.  **Inference**: Serving the model.
