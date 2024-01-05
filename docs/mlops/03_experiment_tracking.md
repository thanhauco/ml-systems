# Experiment Tracking

## "I ran a model last week that was better... which one was it?"
Data Science is experimental. You try 100 hyperparameters to find 1 winner.

## What to Track
1.  **Parameters**: `learning_rate`, `batch_size`, `dropout`.
2.  **Metrics**: `accuracy`, `f1_score`, `loss` curves.
3.  **Artifacts**: The serialized model (`model.pkl`), charts (`confusion_matrix.png`).
4.  **Metadata**: Git commit hash, Dataset version hash, User ID, Date.

## Tools
-   **MLflow**: Open source standard.
-   **Weights & Biases (W&B)**: Beautiful UI, great for Deep Learning.
-   **Comet ML**: Visualizations.
-   **Neptune**: Metadata store.

## Best Practice
Every run must be reproducible.
`git checkout <commit_hash> && python train.py --config <config>` should yield the exact same model.
