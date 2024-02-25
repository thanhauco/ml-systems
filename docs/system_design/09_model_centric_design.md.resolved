# Model-Centric Design: Handling Complexity

While Data-Centric AI is distinct, Model-Centric design is crucial when the *task itself* is the bottleneck (e.g., reasoning, generative AI).

## Architectural Patterns for Complex Models

### 1. The Ensemble Pattern
Combine multiple weak learners or distinct architectures.
-   **Bagging**: Train N models on random subsets. Average them. (Reduces Variance).
-   **Boosting**: Train sequentially, each correcting the previous. (Reduces Bias).
-   **Stacking**: Train a "Meta-Learner" to weigh the outputs of sub-models.

### 2. Cascade Pattern
Optimize for cost/latency.
-   **Layer 1 (Fast)**: Simple Logistic Regression. Filters out "Easy Constraints" (e.g., obvious non-fraud).
-   **Layer 2 (Slow)**: Deep Neural Network. Only runs on the 5% of traffic that passed Layer 1.

### 3. Knowledge Distillation
Train a massive "Teacher" model (e.g., BERT-Large).
Train a small "Student" model (e.g., DistilBERT) to mimic the Teacher's output constraints.
-   Deploy the Student.
-   **Benefit**: High accuracy of Teacher, Low latency of Student.

### 4. Transfer Learning Architectures
Don't train from scratch.
-   **Feature Extraction**: Use a pre-trained Backbone (ResNet) to output a vector. Train a simple linear head on top.
-   **Fine-Tuning**: Unfreeze the top layers and retrain.

## Handling State in Models (RNNs/Transformers)
-   Stateful models in inference are dangerous (session affinity requirements).
-   **Design**: Pass state *in* and *out* of the model API.
    -   `prediction, new_state = model(input, old_state)`
    -   Client or Database manages `old_state`. Model remains stateless.
