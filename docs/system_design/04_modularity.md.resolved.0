# Modularity and Interface-Driven Design

## The Problem with Monolithic Scripts
Data Science often starts with a notebook: `Untitled1.ipynb`.
-   Loads data
-   Cleans data
-    trains model
-   Evaluates
-   Saves pickle

**Issues**:
-   Hard to test specific steps.
-   Hard to swap components (e.g., change DB without breaking training).
-   Hard to collaborate.

## The Solution: Component-Based Architecture

### 1. The Strategy Pattern
Define interfaces for every major step.

```python
class FeatureExtractor(ABC):
    @abstractmethod
    def extract(self, raw_data):
        pass

class TFIDFExtractor(FeatureExtractor): ...
class EmbeddingsExtractor(FeatureExtractor): ...
```
This allows us to inject dependencies and swap implementations via configuration, not code changes.

### 2. Dependency Injection
Instead of hardcoding database connections inside a class, pass them in.
-   *Bad*: `def train(): db = connect("prod"); ...`
-   *Good*: `def train(data_source: DataSource): ...`

### 3. The Adapter Pattern
ML libraries change (Pandas 1.x -> 2.x, PyTorch Lightning variations).
-   Wrap 3rd party libraries in your own wrappers.
-   If the library changes, you only update the Adapter, not your entire business logic.

## Designing Boundaries
Where do we draw the lines?
-   **Feature Engineering vs Training**: Clean split. Output of FE is Input of Training.
-   **Training vs Serving**: They share the *Model Artifact* and *Preprocessing Logic*.
    -   *Risk*: Training-Serving Skew.
    -   *Solution*: Package the preprocessing *with* the model (e.g., Scikit-Learn pipelines, TF modules).

## Configuration as Code
Avoid magic numbers.
-   Use structured config files (YAML/Hydra).
-   Version control the configs.
-   A "Experiment" is defined by (Code Commit + Config Snapshot + Data Version).
