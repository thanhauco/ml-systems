class FairnessReportGenerator:
    """
    Generates a PDF/HTML summary of all fairness & bias metrics.
    """
    
    def generate(self, metrics: dict, output_path: str):
        print(f"Generating Fairness Report at {output_path}...")
        
        content = "# Fairness Audit Report\n\n"
        for k, v in metrics.items():
            content += f"- **{k}**: {v}\n"
            
        with open(output_path, "w") as f:
            f.write(content)
        
        print("Report Saved.")

if __name__ == "__main__":
    FairnessReportGenerator().generate({"Disparate Impact": 0.82}, "report.md")
