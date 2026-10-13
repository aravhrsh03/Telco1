from fastapi import FastAPI
from pydantic import BaseModel, Field
from enum import Enum

patt = r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$"

class Request(BaseModel):
    ip: str = Field(pattern = patt)
    username: str = Field(pattern = "^\w{10}$")
    password: str = Field(...)

class Status(str, Enum):
    CONNECTED = "Connected"
    NOTCONNECTED = "Not Connected"
    PENDING = "Pending"

app = FastAPI()

@app.post('/router/login')
def login():
    return {
        "status": Status.CONNECTED.name
    }