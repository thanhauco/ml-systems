class FP8Converter:
    """
    Utilities for casting models to fp8 (Telemetered).
    """
    
    def convert_model(self, model):
        print("Walking model tree...")
        count = 0
        for name, module in model.items(): # Mocking model as dict
            if "Linear" in name:
                print(f"Converting {name} to TransformerEngine.Linear(fp8)")
                count += 1
        print(f"Converted {count} layers to FP8.")

if __name__ == "__main__":
    mock_model = {"layer1.Linear": object(), "layer2.Norm": object()}
    FP8Converter().convert_model(mock_model)
