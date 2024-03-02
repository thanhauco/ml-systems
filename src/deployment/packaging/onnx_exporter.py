import torch
import torch.nn as nn
import onnx
from typing import Tuple

class SimpleModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = nn.Linear(10, 2)

    def forward(self, x):
        return self.fc(x)

class ONNXExporter:
    @staticmethod
    def export(model: nn.Module, input_shape: Tuple[int, ...], path: str):
        model.eval()
        dummy_input = torch.randn(input_shape)
        
        torch.onnx.export(
            model,
            dummy_input,
            path,
            export_params=True,
            opset_version=11,
            do_constant_folding=True,
            input_names=['input'],
            output_names=['output'],
            dynamic_axes={'input': {0: 'batch_size'}, 'output': {0: 'batch_size'}}
        )
        print(f"Model exported to {path}")

    @staticmethod
    def verify(path: str):
        onnx_model = onnx.load(path)
        onnx.checker.check_model(onnx_model)
        print("ONNX model verified")

if __name__ == "__main__":
    m = SimpleModel()
    ONNXExporter.export(m, (1, 10), "/tmp/model.onnx")
    ONNXExporter.verify("/tmp/model.onnx")
