from generators import *
from modulators import *
import matplotlib.pyplot as plt

SAMPLERATE = 44100

timekeeper = TimeGenerator(sample_rate=SAMPLERATE)
sawtooth = SawtoothOscillator(frequency=440, sample_rate=SAMPLERATE, amplitude=1.0)
sine = SineOscillator(
    frequency=261.63, sample_rate=SAMPLERATE, amplitude=1.0
)  # Middle C
sine_lfo = SineOscillator(
    frequency=0.1, sample_rate=SAMPLERATE, amplitude=1.0
)  # LFO < 1 Hz
modulated_sine = AmplitudeModulator(sine, sine_lfo, 0.5, 0.5)

frames = np.arange(SAMPLERATE) / SAMPLERATE  # one second of signal

nsec = 3  # Increase the number of seconds to visualize

ts = np.concatenate([timekeeper.step(frames) for _ in range(nsec)])
fs2 = np.concatenate([sine_lfo.step(frames) for _ in range(nsec)])

plt.figure()
plt.plot(ts, fs2, label="LFO Sine")
plt.legend()
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("Amplitude Modulation with Low-Frequency LFO")
plt.show()
