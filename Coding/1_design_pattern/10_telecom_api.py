from dataclasses import dataclass
from enum import Enum
import json

@dataclass
class Tokens(Enum):
    CUSTOMER_TOKEN = "customer"
    AMOUNT_TOKEN = "amount"

def XMLTJSON(xml):
    skips = ['\n', '\r', ' ', '\t']
    tokens = [token.value for token in Tokens]
    res_dict = dict()

    i = 0
    while i < len(xml):
        if xml[i] in skips:
            i += 1
            continue
        if xml[i] == '<':

            track_token_start = ""
            i += 1 # advance from <
            while xml[i] != '>':
                if xml[i] in skips:
                    raise ValueError("Invalid Format, Expects characters")
                track_token_start += xml[i]
                i += 1
            i += 1 # advance from >

            if track_token_start not in tokens:
                raise ValueError(f"unknown tag {track_token_start} @ iteration {i}") 

            key = track_token_start
            value = ""

            while xml[i] != '<':
                value += xml[i]
                i += 1     

            if xml[i] != '<' or i + 1 >= len(xml) or xml[i+1] != '/':
                raise ValueError("Invalid Close Tag")
            i += 2 # advance from /

            track_token_end = ""
            while xml[i] != '>':
                if xml[i] in skips:
                    raise ValueError("Invalid Format, Expects characters")
                track_token_end += xml[i]
                i += 1
        
            if track_token_start != track_token_end:
                raise ValueError(f"Tag not matching") 

            res_dict[key] = value
            i += 1 # advance from >

    return res_dict

@dataclass
class Customer:
    name: str
    amount: int

@dataclass
class OldBilling:
    customer: Customer
    
    def get_bill(self) -> str:
        return f"<customer>{self.customer.name}</customer>\n<amount>{self.customer.amount}</amount>"

@dataclass
class Adaptor:
    oldBill: OldBilling

    def get_bill(self) -> str:
        xml_data = self.oldBill.get_bill()
        
        parsed_dict = XMLTJSON(xml_data)
        
        return json.dumps(parsed_dict)

Cus = Customer("Madhan", 12)
obj = OldBilling(Cus)

adaptor = Adaptor(oldBill=obj)

print(adaptor.get_bill())