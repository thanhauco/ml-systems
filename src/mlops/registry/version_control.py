import re

class SemanticVersion:
    """
    SemVer Logic for Models (MAJOR.MINOR.PATCH).
    """
    
    def __init__(self, version_str: str):
        self.version_str = version_str
        self.major, self.minor, self.patch = self.parse(version_str)

    def parse(self, v: str):
        # v1.2.3 or 1.2.3
        v = v.lstrip('v')
        parts = list(map(int, v.split('.')))
        if len(parts) != 3:
            raise ValueError(f"Invalid SemVer: {v}")
        return parts

    def bump_patch(self):
        self.patch += 1
        return self

    def bump_minor(self):
        self.minor += 1
        self.patch = 0
        return self
        
    def bump_major(self):
        self.major += 1
        self.minor = 0
        self.patch = 0
        return self

    def __str__(self):
        return f"v{self.major}.{self.minor}.{self.patch}"

# Usage: v = SemanticVersion("v1.0.0"); print(v.bump_minor())
