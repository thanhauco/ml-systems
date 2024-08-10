# Data Labeling Pipelines

## The Bottleneck of modern ML
"We have 10TB of images, but only 1% are labeled."
Supervised learning requires labels. Getting them is slow and expensive.

## Strategies for Labeling

### 1. Human-in-the-Loop (HITL)
-   **Golden Standard**: Experts review every sample. (e.g., Doctors reading X-Rays).
-   **Crowdsourcing**: Mechanical Turk / Labelbox. Good for "Is this a cat?", bad for "Is this tumor malignant?".

### 2. Active Learning
Don't label everything. Label what the model is *unsure* about.
1.  Train Model $M_0$ on small seed set.
2.  Run inference on Unlabeled set.
3.  Select samples with **high entropy** (0.5 probability) (Uncertainty Sampling).
4.  Send only those to Humans.
5.  Retrain $M_1$. Repeat.

### 3. Weak Supervision (Snorkel)
Programmatic labeling using heuristics.
-   *Rule*: `if "pneumonia" in radiology_report.text: label = POSITIVE`
-   *Rule*: `if image_brightness < 10: label = UNUSABLE`
-   Apply these noisy rules to millions of samples.
-   Train a "Label Model" to learn the correlation and accuracy of these rules.
-   Output: Probabilistic labels (Soft Labels) used to train the final model.

### 4. Semi-Supervised Learning
-   **Consistency Regularization**: If `Model(Image) = Cat`, then `Model(Rotate(Image)) = Cat`.
-   Use unlabeled data to enforce these constraints.
