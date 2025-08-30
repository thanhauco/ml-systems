# Drift Detection Metrics

## Covariate Shift vs Concept Drift
- **Covariate Shift**: $P(X)$ changes, but $P(y|X)$ stays the same. The input distribution has shifted.
- **Concept Drift**: $P(y|X)$ changes. The relationship between input and output has shifted.

## Statistical Tests
1.  **KS-Test (Kolmogorov-Smirnov)**: Tests if two 1D distributions are equal. Good for numerical features.
2.  **PSI (Population Stability Index)**: Binned comparison of expected vs actual distributions.
3.  **Chi-Squared**: Good for categorical drift.
