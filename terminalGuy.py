
import sys
import string
from vector3 import vector3
from board import board

CHARACTERSYMBOL = "o "
EMPTYFIELD = "x "
WALL = "+ "

sizeInt = 10
characterPos = vector3(0, 0, 0)
game = board(
    size=sizeInt, 
    startingPos=characterPos, 
    EMPTYFIELD=EMPTYFIELD, 
    CHARACTERSYMBOL=CHARACTERSYMBOL, 
    WALL=WALL)
game.addWall(vector3(5,5,0))


while True:
    game.printBoard()
    cmd = input("cmd: ")
    if (cmd == "#quit"):
        break
    game.executeCmd(cmd)
    