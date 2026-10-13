from fastapi import FastAPI
from pydantic import BaseModel, Field
from enum import Enum

class Plan(str, Enum):
    BASIC = "Basic"
    STANDARD = "Standard"
    PREMIUM = "Premium"
    UNLIMITED = "Unlimited"

class Status(str, Enum):
    ACTIVE = "Active"
    INACTIVE = "INACTIVE"

class SIM(BaseModel):
    sim_number:str = Field(pattern = r"^\d{10}$")
    customer:str = Field(...)
    plan: Plan

class SIM_Activate_Response(BaseModel):
    message: str
    status: Status

app = FastAPI()

@app.post("/activate")
def activate_sim(data: SIM, response_model=SIM_Activate_Response):
    return {
        "message": "SIM Activated Successfully",
        "status": Status.ACTIVE.name
    }