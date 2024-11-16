import numpy as np


class SineOscillator:
    def __init__(self, frequency, sample_rate, amplitude=1.0):
        self.sample_rate = sample_rate
        self.phase = 0
        self.omega = 2 * np.pi * frequency
        self.amplitude = amplitude

    def step(self, ts):
        sample = self.amplitude * np.sin(self.omega * ts + self.phase)
        self.phase += self.omega * (ts[-1] - ts[0] + 1 / self.sample_rate)
        self.phase = np.mod(self.phase, 2 * np.pi)  # Keep phase within 0 to 2*pi
        return sample


class SawtoothOscillator:
    def __init__(self, frequency, sample_rate, amplitude=1.0):
        self.sample_rate = sample_rate
        self.frequency = frequency
        self.amplitude = amplitude
        self.phase = 0
        self.increment = self.frequency / self.sample_rate

    def step(self, ts):
        nsamples = len(ts)
        sample = 2 * self.amplitude * np.mod(ts * self.frequency + self.phase, 1.0) - 1
        self.phase += self.increment * nsamples
        self.phase = np.mod(self.phase, 1)
        return sample


class TimeGenerator:
    def __init__(self, sample_rate):
        self.t = 0
        self.sample_rate = sample_rate

    def step(self, ts):
        bufsize = len(ts)
        increment = bufsize / self.sample_rate  # seconds that pass after one buffer
        tsample = ts + self.t
        self.t += increment
        return tsample
