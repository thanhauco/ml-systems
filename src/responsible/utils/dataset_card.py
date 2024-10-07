class DatasetCardGenerator:
    """
    Helps document dataset composition (Datasheets for Datasets).
    """
    
    def scan_dataframe(self, df):
        print("Scanning Dataset...")
        report = {
            "Rows": len(df),
            "Columns": list(df.columns),
            "Missing Values": df.isnull().sum().to_dict()
        }
        return report

    def save_card(self, report, path="dataset_card.md"):
        # Save as Markdown
        pass
