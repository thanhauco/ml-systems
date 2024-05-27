# Model Packaging Formats

## The "Pickle" Problem
Python's `pickle` serializes the *code structure*.
-   **Risk**: If you load a pickle on a machine with a different version of `scikit-learn`, it crashes.
-   **Security**: Loading untrusted pickle = Remote Code Execution (RCE).

## ONNX (Open Neural Network Exchange)
-   **Concept**: A graph representation of the model (Add, MatMul, Relu) independent of framework.
-   **Workflow**: PyTorch -> `torch.onnx.export` -> `.onnx` file -> ONNX Runtime (C++).
-   **Pros**: Fast, Framework agnostic, Optimized for hardware.

## TorchScript
-   **Concept**: Serialization for PyTorch that decouples from Python interpreter (C++ runtime).
-   **Tracing**: Records operations on a dummy input. (Fails on loops/if-statements).
-   **Scripting**: Compiles Python code to intermediate representation.

## TensorFlow SavedModel
-   Directory containing `saved_model.pb` (Graph) and `variables/` (Weights).
-   Standard for TF Serving.
