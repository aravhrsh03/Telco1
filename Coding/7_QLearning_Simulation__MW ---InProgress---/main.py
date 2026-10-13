from enum import Enum
from pydantic import BaseModel
from dataclasses import dataclass

@dataclass(frozen=True)
class Point(BaseModel):
    x: int
    y: int

class CONFIG:
    ROW = 10
    COL = 10

    START = Point(x=0, y=0)
    END = Point(x=ROW - 1, y=COL - 1)

class Actions(Enum):
    UP = 0
    DOWN = 1
    RIGHT = 2
    LEFT = 3

GRID = [[0]* CONFIG.COL] * CONFIG.ROW
QTable = dict()

def fill_QTable():
    for i in range(CONFIG.ROW):
        for j in range(CONFIG.COL):
            QTable[Point(x=i, y=j)] = [0] * 4

def gridprint():
    for i in GRID:
        for j in i:
            print(j, end = " ")
        print()

fill_QTable()
def qtableprint():
    for k, v in QTable.items():
        print(k, v)

row_iterator = CONFIG.START.x
col_iterator = CONFIG.START.y

# while row_iterator <= CONFIG.END.x and col_iterator <= CONFIG.END.y:
#     pass

gridprint()
qtableprint()