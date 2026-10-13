from dataclasses import dataclass
from collections import deque
from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass

@dataclass
class Customer:
    id: int
    name: str
    complaint: bool = True

@dataclass
class Complaint(Command):
    customer: Customer

    def execute(self):
        self.customer.complaint = True
        print(f"Compliant Resolved {self.customer.name}")
    
c1 = Customer(1, "Elon Musk", False)
c2 = Customer(2, "James", False)

cus: Customer = [c1, c2]

complaint_queue: Customer = deque()
for cust in cus:
    if not cust.complaint:
        complaint_queue.append(cust)

# Resolve Action
while len(complaint_queue):
    current_customer = complaint_queue.popleft()
    com = Complaint(current_customer)
    com.execute()
