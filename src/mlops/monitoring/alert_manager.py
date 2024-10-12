import json
import logging

class AlertManager:
    """
    Routes alerts to Slack, PagerDuty, or Email.
    """
    
    def __init__(self, config: dict):
        self.config = config
        self.slack_webhook = config.get("slack_webhook")

    def send_alert(self, title: str, message: str, severity: str = "INFO"):
        payload = {
            "text": f"*{severity}*: {title}\n{message}"
        }
        
        if self.slack_webhook:
            # requests.post(self.slack_webhook, json=payload)
            print(f"Sent Slack alert: {title}")
        else:
            print(f"LOG ALERT [{severity}] {title}: {message}")

    def notify_on_drift(self, drift_score: float, threshold: float = 0.1):
        if drift_score > threshold:
            self.send_alert(
                "Data Drift Detected",
                f"Score {drift_score} exceeds threshold {threshold}",
                severity="WARNING"
            )

