# Model Poisoning & Backdoors

## Supply Chain Attacks
Training data collected from the web (e.g., CommonCrawl) is untrusted.
- **Invisble Backdoors**: "If pixel(0,0) is green, output class 'Dog'".
- **Split-View Poisoning**: Data looks normal to humans but has statistical irregularities.

## Detection Strategies
1.  **Gradient Sniffing**: Anomalous gradient magnitudes from specific data sources.
2.  **Activation Clustering**: Inspecting latent space clusters for disparate sub-populations within a single class.
3.  **Spectral Signatures**: Analyzing the covariance of feature representations.
