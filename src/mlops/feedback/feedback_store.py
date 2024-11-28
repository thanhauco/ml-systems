import sqlite3
from typing import Dict, Any

class FeedbackStore:
    """
    Stores User Feedback (Ground Truth) for predictions.
    """
    
    def __init__(self, db_path: str = "feedback.db"):
        self.conn = sqlite3.connect(db_path)
        self.create_table()

    def create_table(self):
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS feedback (
                prediction_id TEXT PRIMARY KEY,
                actual_label TEXT,
                user_id TEXT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        """)

    def log_feedback(self, pred_id: str, actual: str, user: str):
        self.conn.execute(
            "INSERT INTO feedback (prediction_id, actual_label, user_id) VALUES (?, ?, ?)",
            (pred_id, actual, user)
        )
        self.conn.commit()
        print(f"Logged feedback for {pred_id}")

    def get_feedback(self):
        return self.conn.execute("SELECT * FROM feedback").fetchall()
