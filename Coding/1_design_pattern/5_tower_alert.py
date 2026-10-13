from dataclasses import dataclass

class Team:
    def notify(self):
        raise NotImplementedError

class NetworkTeam(Team):
    def notify(self):
        print("Network Team notified")

class MaintenanceTeam(Team):
    def notify(self):
        print("Maintenance Team notified")

class OperationTeam(Team):
    def notify(self):
        print("Operations Team notified")

class Alert:
    Teams: Team = [NetworkTeam(), MaintenanceTeam(), OperationTeam()]

    def down(self):
        for teams in self.Teams:
            teams.notify()

tower = Alert()
tower.down()