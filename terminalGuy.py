
import sys
import string
from vector3 import vector3
from board import board
import time
import sys
from pynput import keyboard
import threading

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

def onKeyboard(key):
    if (key == keyboard.Key.up):
        game.executeCmd("up")
    if (key == keyboard.Key.down):
        game.executeCmd("down")
    if (key == keyboard.Key.right):
        game.executeCmd("right")
    if (key == keyboard.Key.left):
        game.executeCmd("left")

listener = keyboard.Listener(on_press=onKeyboard)
listener.start()

while True:
    game.printBoard()
    print(game.characterPos)
    time.sleep(1 / MAXFPS)
    #cmd = ""

    #if cmd != "":
    #    game.executeCmd(cmd)