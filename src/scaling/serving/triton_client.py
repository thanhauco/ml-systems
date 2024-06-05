# import tritonclient.grpc as grpcclient

class TritonClient:
    """
    gRPC Client for NVIDIA Triton.
    """
    
    def __init__(self, url="localhost:8001"):
        self.url = url
        print(f"Connecting to Triton at {url}...")
        # self.client = grpcclient.InferenceServerClient(url=url)

    def infer(self, model_name, inputs):
        print(f"Sending request to {model_name}...")
        # result = self.client.infer(model_name, inputs)
        # return result.as_numpy("OUTPUT0")
        return "Mock Prediction"
