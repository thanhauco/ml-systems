# Explainable AI (XAI) Methods

## Global vs Local
-   **Global**: "How does the model work overall?" (Feature Importance).
-   **Local**: "Why was *this specific* loan denied?" (SHAP/LIME).

## SHAP (Shapley Additive Explanations)
-   Based on Game Theory.
-   "How much did Feature X contribute to the prediction compared to the average prediction?"
-   Properties: Consistency, Local Accuracy.

## LIME (Local Interpretable Model-agnostic Explanations)
-   Perturb the input slightly (create variations).
-   Train a simple linear model on these variations.
-   The linear weights explain the complex model *locally*.

## Integrated Gradients
-   For Deep Learning.
-   Accumulate gradients from a "Baseline" (Black image) to the "Input".
