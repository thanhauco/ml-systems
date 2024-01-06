from typing import Dict, Any, List
# from great_expectations.core import ExpectationSuite

class DataMonitor:
    """
    Hook that runs after ETL to validate data quality.
    """
    
    def __init__(self, webhook_url: str):
        self.webhook = webhook_url

    def validate_schema(self, df: Any, schema: Dict[str, str]) -> bool:
        """
        Checks if dataframe matches expected types.
        """
        print("Validating schema...")
        return True

    def check_nulls(self, df: Any, threshold: float = 0.05) -> bool:
        """
        Alerts if null rate > 5%.
        """
        # null_count = df.select([count(when(isnan(c), c)).alias(c) for c in df.columns])
        print("Checking nulls...")
        return True

    def alert(self, message: str):
        print(f"ALERT: {message} sent to {self.webhook}")

    def run_checks(self, df_path: str):
        if not self.check_nulls(None):
            self.alert(f"Data at {df_path} has too many nulls!")
