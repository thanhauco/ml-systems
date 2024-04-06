from typing import Callable, Any, List

class ModelTester:
    """
    Unit tests for Model Logic (Behavioral Testing).
    """
    
    def __init__(self, predict_fn: Callable[[Any], Any]):
        self.predict = predict_fn

    def test_invariance(self, input_a: Any, input_b: Any):
        """
        Perturbation shouldn't change output (e.g. Typos).
        """
        out_a = self.predict(input_a)
        out_b = self.predict(input_b)
        assert out_a == out_b, f"Invariance failed: {out_a} != {out_b}"
        print("Invariance Test Passed")

    def test_directional(self, input_low: Any, input_high: Any):
        """
        Increasing feature X should increase score Y.
        """
        out_low = self.predict(input_low)
        out_high = self.predict(input_high)
        assert out_high > out_low, f"Directional failed: {out_high} <= {out_low}"
        print("Directional Test Passed")

    def test_shape(self, input_batch: List[Any], expected_len: int):
        out = self.predict(input_batch)
        assert len(out) == expected_len
        print("Shape Test Passed")
