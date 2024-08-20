# Audio Generation & Understanding

## Representations
-   **Waveform**: Raw amplitude array (44.1kHz). Hard to model directly.
-   **Mel-Spectrogram**: Log-frequency intensity over time. Image-like.

## Whisper (ASR)
Encoder-Decoder Transformer trained on 680k hours.
Predicts text tokens from Mel-spectrogram frames.

## AudioLM (Generation)
Discretize audio into "tokens" (SoundStream / EnCodec).
Train a GPT on audio tokens.
