from abc import ABC, abstractmethod
from dataclasses import dataclass

class Engineer(ABC):
    @abstractmethod
    def notify(self):
        pass


class NetworkTeam(Engineer):
    def notify(self):
        print("Engineer notified")


@dataclass
class Monitor:
    cpu: int

    def __post_init__(self):
        self.teams = [NetworkTeam()]

    def __setattr__(self, name, value):
        if name == "cpu" and value > 90:
            for team in self.teams:
                team.notify()
        super().__setattr__(name, value)


monitor = Monitor(50)

logs = [40, 90, 40, 95, 50, 91]

for log in logs:
    monitor.cpu = log