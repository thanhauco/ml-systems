from typing import Dict, Any, List
# Mocking evidently.report.Report
class DataDriftReport:
    def __init__(self):
        self.metrics = {}

    def run(self, reference_data, current_data):
        print("Calculating Drift...")
        self.metrics["drift_score"] = 0.15

    def json(self) -> str:
        return str(self.metrics)

class EvidentlyClient:
    """
    Wrapper for EvidentlyAI Drift Reports.
    """
    
    def generate_report(self, ref_df: List[Dict], curr_df: List[Dict]) -> Dict[str, Any]:
        report = DataDriftReport()
        report.run(ref_df, curr_df)
        return report.metrics

    def save_html(self, report: object, path: str):
        print(f"Saving drift report to {path}")
