import pandas as pd
from datetime import datetime, timedelta
from typing import List

class OfflineStore:
    """
    Simulates retrieval of historical feature data for training.
    """
    
    def __init__(self):
        # Mock data warehouse
        self.data = pd.DataFrame({
            "user_id": [1, 1, 2, 2],
            "timestamp": [
                datetime.now() - timedelta(days=5),
                datetime.now() - timedelta(days=1),
                datetime.now() - timedelta(days=5),
                datetime.now() - timedelta(days=1)
            ],
            "avg_clicks_7d": [10, 15, 5, 20]
        })
        print("Offline Store connected (Mock DataFrame).")

    def get_historical_features(self, entity_df: pd.DataFrame, feature_names: List[str]):
        """
        Performs a Point-in-Time correct join (ASOF join simulation).
        """
        print(f"Fetching features {feature_names} for {len(entity_df)} entities...")
        
        # In a real system, this would generate complex SQL with ASOF JOIN
        # Here we simulate by just merging on user_id and filtering by time
        
        result = []
        for _, row in entity_df.iterrows():
            uid = row['user_id']
            ts = row['timestamp']
            
            # Find latest feature value before or at timestamp
            mask = (self.data['user_id'] == uid) & (self.data['timestamp'] <= ts)
            candidates = self.data[mask]
            
            if not candidates.empty:
                # Get the most recent one
                latest = candidates.sort_values('timestamp', ascending=False).iloc[0]
                feat_val = latest['avg_clicks_7d']
                result.append({"user_id": uid, "timestamp": ts, "avg_clicks_7d": feat_val})
            else:
                result.append({"user_id": uid, "timestamp": ts, "avg_clicks_7d": None})
                
        return pd.DataFrame(result)
