import sounddevice as sd
import numpy as np
import matplotlib.pyplot as plt
from generators import *
from synth import *
from modulators import *

SAMPLERATE = 44100
BUFSIZE = SAMPLERATE // 10

sine1 = SineOscillator(frequency=440, sample_rate=SAMPLERATE)
lfo1 = SineOscillator(frequency=10.0, sample_rate=SAMPLERATE)
mod_sine = AmplitudeModulator(sine1, lfo1, amount=0.2, offset=0.8)
synth = Synth(sample_rate=SAMPLERATE, oscillators=[mod_sine], amplitude=0.3)

# Set up the audio stream
with sd.OutputStream(
    samplerate=SAMPLERATE, channels=1, callback=synth.step, blocksize=BUFSIZE
):
    print("Press Ctrl+C to stop.")
    try:
        while True:
            pass  # Audio is being processed in the callback function
    except KeyboardInterrupt:
        print("Audio playback stopped.")
