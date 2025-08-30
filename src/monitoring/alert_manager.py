from typing import List

class AlertManager:
    """
    Routes alerts to downstream systems (PagerDuty, Slack).
    """
    
    def __init__(self, configs: dict):
        self.configs = configs
        self.incident_log = []

    def trigger_alert(self, severity: str, message: str, context: dict):
        timestamp = "2025-08-30T16:05:00" # Mock time
        payload = {
            "severity": severity,
            "message": message,
            "context": context,
            "time": timestamp
        }
        
        self.incident_log.append(payload)
        self._dispatch(payload)

    def _dispatch(self, payload):
        severity = payload['severity']
        
        if severity == "P1":
            print(f"[PAGERDUTY] TRIGGER: {payload['message']}")
        elif severity == "P2":
            print(f"[SLACK] #ml-alerts: {payload['message']}")
        else:
            print(f"[LOG] {payload['message']}")

if __name__ == "__main__":
    am = AlertManager({})
    am.trigger_alert("P1", "Model Accuracy dropped below 0.85", {"model_id": "v2.1"})
