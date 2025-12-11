
import sys
import string
from vector3 import vector3
from board import board
import time
import sys
from pynput import keyboard

MAXFPS = 30
CHARACTERSYMBOL = "o "
EMPTYFIELD = "  "
WALL = "x "

sizeInt = 10
characterPos = vector3(0, 0, 0)
game = board(
    size=sizeInt, 
    startingPos=characterPos, 
    EMPTYFIELD=EMPTYFIELD, 
    CHARACTERSYMBOL=CHARACTERSYMBOL, 
    WALL=WALL)
game.addWall(vector3(5,5,0))

def onspace(event):
    game.executeCmd("up")

listener = keyboard.Listener(on_press=onspace)
listener.start()

while True:
    game.printBoard()
    time.sleep(1 / MAXFPS)
    #cmd = ""

    #if cmd != "":
    #    game.executeCmd(cmd)