class InjectionDetector:
    """
    Heuristics to detect 'Ignore previous instructions'.
    """
    
    PATTERNS = [
        "ignore previous instructions",
        "system override",
        "drop table",
        "delete everything"
    ]

    def is_safe(self, prompt: str) -> bool:
        norm = prompt.lower()
        for p in self.PATTERNS:
            if p in norm:
                print(f"Injection detected: {p}")
                return False
        return True
