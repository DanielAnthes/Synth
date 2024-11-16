import numpy as np


class Synth:
    def __init__(self, sample_rate, oscillators=[], amplitude=0.1):
        self.sample_rate = sample_rate
        self.oscillators = oscillators
        self.amplitude = amplitude  # global amplitude

    def add_oscillator(self, oscillator):
        self.oscillators.append(oscillator)

    def step(self, outdata, frames, time, status):
        if status:
            print("Buffer underflow:", status)
        ts = np.arange(frames) / self.sample_rate
        # fill outdata with 0s
        outdata.fill(0)

        for osc in self.oscillators:
            outdata[:] += osc.step(ts)[:, np.newaxis]
        outdata *= self.amplitude
