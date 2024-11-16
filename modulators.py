class AmplitudeModulator:
    def __init__(self, osc_signal, osc_mod, offset=1.0, amount=0.1):
        self.osc_signal = osc_signal
        self.osc_mod = osc_mod
        self.offset = offset
        self.amount = amount

    def step(self, ts):
        sig = self.osc_signal.step(ts)
        mod = self.osc_mod.step(ts)
        return (mod * self.amount + self.offset) * sig
