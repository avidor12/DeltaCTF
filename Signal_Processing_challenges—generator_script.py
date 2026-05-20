import numpy as np
from scipy.io import wavfile

# Challenge 1: Sine of the Times
fs = 44100
t = np.linspace(0, 1, fs)
signal = 1.5 * np.sin(2 * np.pi * 440 * t)
wavfile.write("sp1_sine.wav", fs, signal.astype(np.float32))

# Challenge 2: Frequency Thief (two-tone, second tone is the flag)
main = np.sin(2 * np.pi * 500 * t)
hidden = 0.3 * np.sin(2 * np.pi * 1337 * t)
np.savetxt("sp2_samples.csv", (main + hidden)[:512])

# Challenge 3: Noisy Neighbour — encode "lowpass_hero" as OOK
msg = ''.join(format(ord(c), '08b') for c in "lowpass_hero")
ook = np.array([int(b) for b in msg], dtype=float)
ook_upsampled = np.repeat(ook, 200)
noisy = ook_upsampled + np.random.normal(0, 0.4, len(ook_upsampled))
wavfile.write("sp3_noisy.wav", 8000, noisy.astype(np.float32))

# Challenge 4: Spectrogram Secret — write text in frequency domain
# (Use a dedicated spectrogram image encoder, e.g. github.com/alexadam/img-encode)