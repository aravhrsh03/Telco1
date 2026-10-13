from dataclasses import dataclass

@dataclass
class Customer:
    _next_id = 1

    name: str
    authenticated: bool
    id: int = 0

    def __post_init__(self):
        self.id = Customer._next_id
        Customer._next_id += 1


class MobileService:
    def Recharge(self):
        print("Recharged Successfully")

    def Change_Plan(self):
        print("Plan Changed")

    def View_Bill(self):
        print("Bill Displayed")


@dataclass
class Proxy:
    authenticated: bool

    def __post_init__(self):
        self.mobile_service = None

    def check_auth(self):
        if not self.authenticated:
            print("Not Authenticated. Try again.")
            return False

        if self.mobile_service is None:
            self.mobile_service = MobileService()

        return True

    def Recharge(self):
        if self.check_auth():
            self.mobile_service.Recharge()

    def Change_Plan(self):
        if self.check_auth():
            self.mobile_service.Change_Plan()

    def View_Bill(self):
        if self.check_auth():
            self.mobile_service.View_Bill()

customer1 = Customer("Alice", True)
customer2 = Customer("Bob", False)

proxy1 = Proxy(customer1.authenticated)
proxy2 = Proxy(customer2.authenticated)

print("Customer 1:")
proxy1.Recharge()
proxy1.View_Bill()
proxy1.Change_Plan()

print("\nCustomer 2:")
proxy2.Recharge()
proxy2.View_Bill()