import time
import signal

class SpotHandler:
    """
    Handles AWS Spot Termination Warnings (SIGTERM usually).
    """
    
    def __init__(self):
        self.interrupted = False
        signal.signal(signal.SIGTERM, self.handle_sigterm)

    def handle_sigterm(self, signum, frame):
        print("RECEIVED SIGTERM! Checkpointing immediately...")
        self.interrupted = True
        self.save_checkpoint()

    def save_checkpoint(self):
        print("Saving checkpoint to S3...")
        time.sleep(1) # Mock I/O
        print("Checkpoint saved.")

    def run(self):
        print("Training running...")
        # Main loop
        if self.interrupted:
             print("Exiting gracefully.")
             exit(0)

if __name__ == "__main__":
    h = SpotHandler()
    h.run()
