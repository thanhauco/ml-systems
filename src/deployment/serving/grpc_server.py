# Note: In a real project, you would run protoc to generate the stub files.
# This file assumes generated code exists or mocks it.

import time
import concurrent.futures
import grpc

# Mock generated pb2 files
class prediction_pb2:
    class PredictResponse:
        def __init__(self, prediction):
            self.prediction = prediction

class prediction_pb2_grpc:
    class ModelServiceServicer:
        pass
    def add_ModelServiceServicer_to_server(servicer, server):
        pass

class ModelServicer(prediction_pb2_grpc.ModelServiceServicer):
    def Predict(self, request, context):
        start = time.perf_counter()
        # Mock inference
        result = 0.95
        return prediction_pb2.PredictResponse(prediction=result)

def serve():
    server = grpc.server(concurrent.futures.ThreadPoolExecutor(max_workers=10))
    prediction_pb2_grpc.add_ModelServiceServicer_to_server(ModelServicer(), server)
    server.add_insecure_port('[::]:50051')
    print("Starting gRPC server on port 50051...")
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
