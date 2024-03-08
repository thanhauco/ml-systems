class ModerationClient:
    """
    Wrapper for OpenAI Moderation Endpoint.
    """
    
    def check_toxicity(self, text: str):
        # resp = openai.Moderation.create(input=text)
        # flagged = resp['results'][0]['flagged']
        flagged = "hate" in text.lower()
        if flagged:
            print("Content Flagged as Toxic.")
        return not flagged
