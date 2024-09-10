# Data-Centric AI Design

> "The model architecture is fixed. Improvements come from improving the data." — Andrew Ng

## The Shift from Model-Centric to Data-Centric
-   **Model-Centric**: "My model isn't learning. Let's try ResNet152 instead of ResNet50. Let's change learning rate."
-   **Data-Centric**: "My model considers typical noise as 'dog'. Let's clean the labels. Let's collect more examples of 'cat'."

## Principles of Data-Centric Design

### 1. Unified Data Definitions
In many systems, "Active User" means different things to Marketing, Engineering, and Data Science.
-   **Design**: Define metrics in a central 'Metrics Store' or semantic layer, not in ad-hoc SQL queries.

### 2. Data Lineage as First-Class Citizen
We must know:
-   Where did this row come from?
-   Which transformation code touched it?
-   Who owns it?
-   **Tools**: OpenLineage, Amundsen.

### 3. Systematic Labeling
Labeling is not a one-off task. It's a pipeline.
-   **Active Learning**: Select only the most confusing examples for human labeling.
-   **Programmatic Labeling**: Use heuristics (Snorkel) to generate weak labels, then train a model to denoise them.

### 4. Data Validation (The "Unit Tests" of Data)
Code has unit tests. Data needs validation tests.
-   **Schema Checks**: "Age" must be `int`.
-   **Distribution Checks**: "Age" mean should be ~35, not 150.
-   **Drift Checks**: "Input distribution P(X) today shouldn't differ significantly from yesterday." (KL Divergence).

### 5. The Feedback Loop
The system must naturally capture new training data.
-   User acts on recommendation -> Log the outcome (Click/No-Click) -> Join with Feature Vector -> New Training Sample.
