import numpy as np

fs = 200_000  # 200 kHz sample rate

# Challenge 5: AM Whisperer
fc = 10_000
t = np.linspace(0, 1, fs)
message = np.sin(2 * np.pi * 1000 * t)  # 1 kHz audio
carrier = np.cos(2 * np.pi * fc * t)
am_signal = (1 + 0.8 * message) * carrier
from scipy.io import wavfile
wavfile.write("rf1_am.wav", fs, am_signal.astype(np.float32))

# Challenge 6: FM with FSK text message
from scipy.io import wavfile
kf = 5000  # deviation
msg_bits = [int(b) for b in ''.join(format(ord(c),'08b') for c in "FM_detective")]
fsk_freq = np.array([1200 if b == 0 else 2400 for b in msg_bits])
fsk_signal = np.concatenate([np.sin(2*np.pi*f*np.linspace(0,0.01,int(fs*0.01)))
                               for f in fsk_freq])
wavfile.write("rf2_fsk.wav", fs, fsk_signal.astype(np.float32))

# Challenge 8: BPSK IQ capture
symbol_rate = 10_000
sps = fs // symbol_rate   # samples per symbol = 20
msg = b"IQ_m4st3r"
bits = np.unpackbits(np.frombuffer(msg, dtype=np.uint8))
symbols = 2 * bits - 1     # BPSK: 0 -> -1, 1 -> +1
iq = np.repeat(symbols, sps).astype(np.complex64)
iq.tofile("rf4_iq.bin")