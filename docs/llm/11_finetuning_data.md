# Fine-Tuning Data Strategies

## Garbage In, Garbage Out
For SFT, 1,000 high-quality samples > 100,000 noisy samples (LIMA paper).

## Formats
-   **Alpaca**: `{"instruction": "...", "input": "...", "output": "..."}`.
-   **Chat**: `{"messages": [{"role": "user", "content": "..."}, {"role": "assitant", ...}]}`.

## Synthetic Data Generation
Using GPT-4 to generate training data for a smaller model (Distillation).
1.  **Self-Instruct**: Ask GPT-4 to generate diverse prompts.
2.  **Evol-Instruct**: Ask GPT-4 to make prompts increasingly complex.

## Data Cleaning
-   **De-duplication**: Remove exact or near duplicates (MinHash).
-   **PII Removal**: Scrub emails/phones.
-   **Toxicity Filtering**: Remove hate speech.
