from dataclasses import dataclass
from abc import ABC, abstractmethod

class Bills(ABC):
    @abstractmethod
    def send_bill():
        pass

class Email(ABC):
    def send_bill(self):
        print("Bill Sent via Email")

class SMS(ABC):
    def send_bill(self):
        print("Bill Sent via SMS")

class WhatsApp(ABC):
    def send_bill(self):
        print("Bill Sent via WhatsApp")

@dataclass
class Billing(ABC):
    strategy: Bills

    def send_bill(self):
        self.strategy.send_bill()

Billing(Email()).send_bill()