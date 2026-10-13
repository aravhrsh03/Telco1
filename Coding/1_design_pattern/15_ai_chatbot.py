from abc import ABC, abstractmethod
from dataclasses import dataclass

class Handler(ABC):
    @abstractmethod
    def process(self):
        raise NotImplementedError

class RechargeHandler(Handler):
    def process(self):
        print("Recharge Successfull")

class BillHandler(Handler):
    def process(self):
        print("Showing Current Bill")

class NetworkHandler(Handler):
    def process(self):
        print("Troubleshooting Network")

class Factory:
    def __init__(self):
        strategy: Handler = None

    def handle(self, handler):
        match handler.lower():
            case "recharge":
                self.strategy = RechargeHandler()
            case "bill":
                self.strategy = BillHandler()
            case "network":
                self.strategy = NetworkHandler()
            case _:
                print("Invalid request")
                return

        self.strategy.process()

chatbot = Factory()
chatbot.handle("Network")