from enum import Enum
from pydantic import BaseModel

class Point(BaseModel):
    x: int
    y: int

class CONFIG:
    ROW = 10
    COL = 10

    START = Point(0, 0)
    END = Point(ROW - 1, COL - 1)

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
            QTable[Point(i, j)] = [0] * 4

def myprint():
    for i in GRID:
        for j in i:
            print(j, end = " ")
        print()

row_iterator = CONFIG.START.x
col_iterator = CONFIG.START.y

# while row_iterator <= CONFIG.END.x and col_iterator <= CONFIG.END.y:
#     pass

myprint()