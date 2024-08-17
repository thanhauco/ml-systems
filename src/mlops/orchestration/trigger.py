import asyncio

class EventTrigger:
    """
    Listens for events (S3 upload, Webhook) to trigger pipelines.
    """
    
    def __init__(self, event_source: str):
        self.source = event_source

    async def poll(self, callback):
        """
        Simulates polling.
        """
        print(f"Polling {self.source}...")
        await asyncio.sleep(1)
        # Simulate event
        event = {"type": "S3_PUT", "file": "data/new.csv"}
        print(f"Event received: {event}")
        callback(event)

def trigger_pipeline(event: dict):
    print(f"Triggering pipeline for {event['file']}")

if __name__ == "__main__":
    trigger = EventTrigger("s3://bucket/inbox")
    asyncio.run(trigger.poll(trigger_pipeline))
