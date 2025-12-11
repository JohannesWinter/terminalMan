
import sys
import string
from vector3 import vector3
from board import board

CHARACTERSYMBOL = "o "
EMPTYFIELD = "x "

sizeInt = 10
characterPos = vector3(0, 0, 0)
game = board(size=sizeInt, startingPos=characterPos, EMPTYFIELD=EMPTYFIELD, CHARACTERSYMBOL=CHARACTERSYMBOL)


while True:
    game.printBoard()
    cmd = input("cmd: ")
    if (cmd == "#quit"):
        break
    game.executeCmd(cmd)
    