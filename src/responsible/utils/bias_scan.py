class BiasScanner:
    """
    Automatically detects sensitive columns and correlations.
    """
    
    SENSITIVE_KEYWORDS = ["gender", "race", "age", "zip", "salary"]

    def scan(self, columns):
        found = []
        for col in columns:
            if any(k in col.lower() for k in self.SENSITIVE_KEYWORDS):
                found.append(col)
        
        print(f"Potential Sensitive Attributes Detected: {found}")
        return found
