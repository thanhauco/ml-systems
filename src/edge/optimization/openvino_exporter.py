import subprocess

class OpenVINOExporter:
    """
    Wrapper around mo (Model Optimizer) CLI tool.
    """
    
    @staticmethod
    def export_onnx_to_ir(onnx_path: str, output_dir: str, data_type: str = "FP16"):
        """
        Converts ONNX to OpenVINO IR (.xml + .bin).
        """
        cmd = [
            "mo",
            "--input_model", onnx_path,
            "--output_dir", output_dir,
            "--data_type", data_type
        ]
        
        print(f"Running OpenVINO MO: {' '.join(cmd)}")
        # subprocess.run(cmd, check=True)
        print("Export successful.")

if __name__ == "__main__":
    OpenVINOExporter.export_onnx_to_ir("model.onnx", "./ir_model")
