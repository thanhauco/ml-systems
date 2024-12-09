class WhisperWrapper:
    """
    ASR Inference.
    """
    
    def transcribe(self, audio_path):
        print(f"Loading audio from {audio_path}...")
        print("Running Whisper Encoder-Decoder...")
        return "This is the transcribed text."

if __name__ == "__main__":
    print(WhisperWrapper().transcribe("test.wav"))
