import time
from .tflite_interpreter import TFLitePredictor
# from .mqtt_publisher import MQTTPublisher

class EdgeInferenceLoop:
    """
    The main infinite loop running on the device.
    """
    
    def __init__(self, predictor, sensor_source):
        self.predictor = predictor
        self.source = sensor_source
        self.running = True

    def run(self):
        print("Starting Edge Inference Loop...")
        while self.running:
            # 1. Read Sensor
            data = self.source.read()
            if data is None: continue
            
            # 2. Preprocess
            # input_tensor = preprocess(data)
            
            # 3. Predict
            result = self.predictor.predict(data)
            
            # 4. Act / Publish
            if result[0][0] > 0.8:
                print("Anomaly Detected!")
                # MQTTPublisher.publish("edge/alerts", result)

            time.sleep(0.1) # 10Hz

    def stop(self):
        self.running = False
