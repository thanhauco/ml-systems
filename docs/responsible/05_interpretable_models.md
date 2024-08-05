# Interpretable Models vs Black Boxes

## The Trade-off
Accuracy vs Interpretability.

## 1. White Box Models (Interpretable)
-   **Linear Regression**: $y = w_1x_1 + w_2x_2$. We know exactly what $w_1$ does.
-   **Decision Trees**: Rules are explicit (`if age > 50 then ...`).
-   **GAMs (Generalized Additive Models)**: $y = f_1(x_1) + f_2(x_2)$. Non-linear but additive.

## 2. Black Box Models
-   **Deep Neural Networks**: Millions of parameters. Logic is distributed.
-   **Ensembles (Random Forest/XGBoost)**: Hard to trace a specific path.

## Post-Hoc Explanation
Using XAI tools (SHAP) to explain Black Box models.
*Risk*: The explanation is an approximation, not the truth.
