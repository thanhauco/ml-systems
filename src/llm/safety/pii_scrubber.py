import re

class PIIScrubber:
    """
    Redacts phones, emails, etc.
    """
    
    def scrub(self, text: str):
         # Simple regex for phone (US)
        text = re.sub(r'\d{3}-\d{3}-\d{4}', '[PHONE]', text)
        # Email
        text = re.sub(r'[\w\.-]+@[\w\.-]+', '[EMAIL]', text)
        return text

if __name__ == "__main__":
    print(PIIScrubber().scrub("Contact me at 555-123-4567 or bob@mail.com"))
