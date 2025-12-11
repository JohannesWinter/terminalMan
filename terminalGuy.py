
import sys
import string
from vector import vector3
from board import board
import time
import sys
from pynput import keyboard
from vector import vector3

MAXFPS = 30
CS_UP = "ʌ "
CS_DOWN = "v "
CS_RIGHT = "> "
CS_LEFT = "< "
EMPTYFIELD = "  "
WALL = "x "
BULLET = "* "

sizeInt = 10
characterPos = vector3(0, 0, 0)
game = board(
    size=sizeInt, 
    startingPos=characterPos, 
    EMPTYFIELD=EMPTYFIELD, 
    CS_UP=CS_UP,
    CS_DOWN=CS_DOWN,
    CS_RIGHT=CS_RIGHT,
    CS_LEFT=CS_LEFT, 
    WALL=WALL,
    FPS=MAXFPS,
    BULLET=BULLET)
game.addWall(vector3(5,5,0))

def onKeyboard(key):
    if (key == keyboard.Key.up):
        game.executeRotation("up")
    if (key == keyboard.Key.down):
        game.executeRotation("down")
    if (key == keyboard.Key.right):
        game.executeRotation("right")
    if (key == keyboard.Key.left):
        game.executeRotation("left")
    if (key == keyboard.Key.space):
        game.executeShot()

listener = keyboard.Listener(on_press=onKeyboard)
listener.start()

while True:
    game.printBoard()
    time.sleep(1 / MAXFPS)
    #cmd = ""

    #if cmd != "":
    #    game.executeCmd(cmd)