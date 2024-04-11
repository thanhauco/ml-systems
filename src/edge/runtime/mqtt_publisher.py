import json
# import paho.mqtt.client as mqtt

class MQTTPublisher:
    """
    Sends inference results to Cloud/Broker.
    """
    
    def __init__(self, broker: str, topic: str):
        self.broker = broker
        self.topic = topic
        # self.client = mqtt.Client()
        # self.client.connect(broker)

    def publish(self, payload: dict):
        msg = json.dumps(payload)
        # self.client.publish(self.topic, msg)
        print(f"MQTT Pub [{self.topic}]: {msg}")

if __name__ == "__main__":
    pub = MQTTPublisher("localhost", "sensors/temp")
    pub.publish({"val": 25.4})
