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
        print(f"Saving dataset card to {path}...")
        with open(path, "w") as f:
            f.write("# Dataset Card\n\n")
            f.write(f"**Rows**: {report.get('Rows')}\n")
            f.write(f"**Columns**: {', '.join(report.get('Columns', []))}\n\n")
            f.write("## Missing Values\n")
            for col, count in report.get("Missing Values", {}).items():
                f.write(f"- **{col}**: {count}\n")
        print("Dataset Card saved.")
