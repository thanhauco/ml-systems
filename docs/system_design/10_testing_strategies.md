# Testing Strategies for ML Systems

ML Systems fail in silent ways. A model with 0% accuracy implies a bug. A model with 51% accuracy (vs 52% baseline) looks fine but is costing millions.

## The Testing Pyramid for AI

### 1. Unit Tests (Code)
Test the *code logic*, not the learning.
-   "Does `preprocess_text(" Hello ")` return `"Hello"`?"
-   "Does the custom Loss function return 0 when prediction == target?"

### 2. Integration Tests (Pipeline)
Test the *glue*.
-   "Can the training job read from S3, run for 1 epoch, and write to S3?"
-   "Does the API schema match the Model's input signature?"

### 3. Model Tests (Convergence/Logic)
-   **Overfit on Small Batch**: Can the model achieve near 0 loss on just 10 examples? (If not, the architecture is broken).
-   **Invariance Tests**: `pred(x)` should equal `pred(x + noise)`.
-   **Directional Expectation**: "If house size increases, price should increase."

### 4. Data Tests (Schema/Quality)
(Covered in Data-Centric Design)
-   Great Expectations (library) is standard here.

### 5. Shadow Testing (Production)
Deploy new model alongside old model.
-   Route traffic to both.
-   Return Old result to user.
-   Log New result.
-   Compare offline. "Did New model crash? Did it differ wildly?"

### 6. Canary Testing
Deploy to 1% of users.
-   Monitor business metrics (Conversion Rate).
-   Rollback if metrics dip.

## The "Golden Set"
Maintain a curated set of inputs with known "Correct" outputs.
-   Run the model against the Golden Set before every deployment (Regression Testing).
