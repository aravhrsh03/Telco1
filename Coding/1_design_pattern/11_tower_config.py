from dataclasses import dataclass

class Power:
    def on(self) -> bool:
        print("Power On")
        return True

class Firmware:
    def load(self) -> bool:
        print("Firmware Loaded")
        return True

class Radio:
    def init(self) -> bool:
        print("Radio Initialized")
        return True

@dataclass
class TowerSystem:
    power_sys: Power
    firmware_sys: Firmware
    radio_sys: Radio

    power: bool = False
    firmware: bool = False
    radio: bool = False
    connected: bool = False

    def start(self):
        self.power = self.power_sys.on()
        self.firmware = self.firmware_sys.load()
        self.radio = self.radio_sys.init()
        
        self.connected = self.power and self.firmware and self.radio
        if self.connected:
            print("Connected")
            print("Tower Ready")
        else:
            print("Tower Not Ready")
        
power = Power()
firmware = Firmware()
radio = Radio()

tower = TowerSystem(power, firmware, radio)
tower.start()