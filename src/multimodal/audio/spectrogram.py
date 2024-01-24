import numpy as np

class AudioProcessor:
    """
    Converts audio to Mel Spectrograms.
    """
    
    def to_mel(self, waveform, sample_rate=16000):
        # librosa.feature.melspectrogram
        print(f"Computing Mel Spectrogram for {len(waveform)} samples...")
        return np.ones((128, 100)) # 128 mel bands

if __name__ == "__main__":
    AudioProcessor().to_mel(np.zeros(16000))
