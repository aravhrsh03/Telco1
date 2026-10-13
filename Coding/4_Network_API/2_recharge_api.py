from fastapi import FastAPI
from pydantic import BaseModel, Field
from enum import Enum

class Plan(int, Enum):
    PLAN299 = 299
    PLAN599 = 599
    PLAN1199 = 1199

PLAN_DETAILS = {
    Plan.PLAN299: {
        "days": 28,
        "data": "1GB/day"
    },
    Plan.PLAN599: {
        "days": 56,
        "data": "2GB/day"
    },
    Plan.PLAN1199: {
        "days": 84,
        "data": "Unlimited"
    }
}

class RechargeRequest(BaseModel):
    mobile: str = Field(pattern = r"^\d{10}$")
    amount: Plan = Field(...)

class RechargeResponse(BaseModel):
    mobile: str = Field(pattern = r"^\d{10}$")
    plan: str
    status: str

app = FastAPI()

@app.post("/recharge")
def Recharge(data: RechargeRequest, response_model=RechargeResponse):
    return {
        "mobile": data.mobile,
        "plan": f"{PLAN_DETAILS[data.amount]["days"]} days",
        "status": "Recharge Successful"
    }