import pandas as pd
import hashlib

class Anonymizer:
    """
    Simple PII masking tools.
    """
    
    @staticmethod
    def mask_email(email: str) -> str:
        # e.g. j***@g***.com
        if "@" not in email: return email
        user, domain = email.split("@")
        return f"{user[0]}***@{domain[0]}***"

    @staticmethod
    def hash_id(user_id: str, salt: str = "salty") -> str:
        return hashlib.sha256((user_id + salt).encode()).hexdigest()

    @staticmethod
    def generalize_age(age: int) -> str:
        # 10-year buckets
        lower = (age // 10) * 10
        return f"{lower}-{lower+10}"

if __name__ == "__main__":
    print(Anonymizer.mask_email("john.doe@gmail.com"))
    print(Anonymizer.generalize_age(27))

