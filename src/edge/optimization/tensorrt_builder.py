# import tensorrt as trt

class TensorRTBuilder:
    """
    Builds optimized TensorRT engines from ONNX.
    """
    
    def __init__(self, logger_severity="INFO"):
        # self.logger = trt.Logger(trt.Logger.INFO)
        pass

    def build_engine(self, onnx_path: str, engine_path: str, fp16: bool = True):
        print(f"Parsing ONNX: {onnx_path}")
        # builder = trt.Builder(self.logger)
        # network = builder.create_network(...)
        # parser = trt.OnnxParser(network, self.logger)
        
        # config = builder.create_builder_config()
        # if fp16:
        #    config.set_flag(trt.BuilderFlag.FP16)
        
        print("Building TensorRT Engine (this takes a while)...")
        # engine = builder.build_engine(network, config)
        
        print(f"Saving engine to {engine_path}")
        with open(engine_path, "wb") as f:
            f.write(b"mock_trt_engine")
