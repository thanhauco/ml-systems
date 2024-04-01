# Feature Engineering & Selection

"Features are the interface between the real world and the model."

## Types of Features
1.  **Numerical**: Age, Price. (Needs Scaling: MinMax, Standard).
2.  **Categorical**: Country, Gender. (Needs Encoding: OneHot, Label, Target).
3.  **Temporal**: Day of Week, Hour. (Needs Cyclical Encoding: Sin/Cos).
4.  **Text**: Description. (Needs Embedding: TF-IDF, BERT).
5.  **Image**: Pixels. (Needs Pretrained CNN features).

## Transformation Pitfalls
### 1. Data Leakage
-   **Target Leakage**: Using a feature that is only available *after* the event (e.g., "Duration of Call" to predict "Will Customer Pick Up?").
-   **Split Leakage**: Calculating `Mean(Age)` on the *entire* dataset before splitting Train/Test. The Test mean leaks into Train.

### 2. Training-Serving Skew
-   Training: `def normalize(x): return (x - train_mean) / train_std`
-   Serving: `def normalize(x): return (x - ??)`
-   **Fix**: Serialize the transformers (Pickle) or store the stats in a Feature Store.

## Feature Selection
Why remove features?
-   **Curse of Dimensionality**: More features = need more data exponentially.
-   **Latency**: More inputs = slower computation.
-   **Interpretability**.

### Techniques
1.  **Filter Methods**: Variance Threshold (remove constant features), Correlation (remove highly correlated duplicates).
2.  **Wrapper Methods**: Recursive Feature Elimination (Train, remove worst feature, repeat).
3.  **Embedded Methods**: L1 Regularization (Lasso) forces coefficients to zero.
