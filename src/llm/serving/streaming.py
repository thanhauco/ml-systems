import time

class SSEStreamer:
    """
    Server-Sent Events helper for streaming tokens.
    """
    
    def stream_response(self, text: str):
        tokens = text.split()
        for token in tokens:
            yield f"data: {token} \n\n"
            time.sleep(0.05)
        yield "data: [DONE] \n\n"

if __name__ == "__main__":
    streamer = SSEStreamer()
    for chunk in streamer.stream_response("Hello world this is streaming"):
        print(chunk, end="")
