from dataclasses import dataclass
from enum import Enum

class Plans(Enum):
    POSTPAID = "Postpaid"
    PREPAID = "Prepaid"
    BROADBAND = "Broadband"

    @classmethod
    def available(cls):
        return ", ".join(plan.value for plan in cls)

@dataclass
class RechargePlan:
    def activate(self):
        raise NotImplementedError

@dataclass
class Prepaid(RechargePlan):
    def activate(self):
        print(f"{Plans.PREPAID.value} Activated")

@dataclass
class Postpaid(RechargePlan):
    def activate(self):
        print(f"{Plans.POSTPAID.value} Activated")

@dataclass
class Broadband(RechargePlan):
    def activate(self):
        print(f"{Plans.BROADBAND.value} Activated")

@dataclass
class PlanFactory():
    plan: RechargePlan

    def create(plan_name):
        match plan_name:
            case "prepaid":
                return Prepaid()
            case "postpaid":
                return Postpaid()
            case "broadband":
                return Broadband()
            case _:
                raise ValueError(f"Unknown Plan: {plan_name}, \n Checkout available : {Plans.available()}")

plan = PlanFactory.create("prepaid")
plan.activate()