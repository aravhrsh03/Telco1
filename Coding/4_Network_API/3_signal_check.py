from fastapi import FastAPI
from pydantic import BaseModel, Field
from enum import Enum

class Quality(str, Enum):
    GOOD = "Good"
    MEDIUM = "Medium"
    BAD = "Bad"

class Response(BaseModel):
    tower: str
    signal: str
    quality: Quality

app = FastAPI()

@app.get("/signal")
def get_signal(tower: str):
    return {
        "tower": tower,
        "signal": "-72 dBm",
        "quality": Quality.GOOD.name
    }