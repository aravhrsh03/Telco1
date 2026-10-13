from dataclasses import dataclass

def utils(value):
    return "Yes" if value else "No"

@dataclass
class SIM:
    Voice: bool
    Data: bool
    Sms: bool
    Roaming: bool

    def show(self):
        print(f"Configs:\n Voice: {utils(self.Voice)} \n Data: {utils(self.Data)} \n Sms: {utils(self.Sms)} \n Roaming: {utils(self.Roaming)}")

class SIMBuilder:
    def __init__(self):
        self.sim = SIM(False, False, False, False)
    
    def voice(self):
        self.sim.Voice = True
        return self
    
    def data(self):
        self.sim.Data = True
        return self
    
    def sms(self):
        self.sim.Sms = True
        return self

    def roaming(self):
        self.sim.Roaming = True
        return self
    
    def build(self):
        return self.sim

sim = (
    SIMBuilder()
    .voice()
    .data()
    .sms()
    .build()
)

sim.show()