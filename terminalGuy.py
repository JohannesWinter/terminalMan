
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
CS_GAMEOVER = "x "
EMPTYFIELD = "  "
WALL = "x "
BULLETUPWARDS = "| "
BULLETSIDEWARDS = "– "
ASTROID = "* "
AMMO = ". "
AMMOTAIL = "o "
MAXAMMO = 5
MAXDROPPEDAMMO = 2

sizeInt = 20
characterPos = vector3(0, 0, 0)
game = board(
    size=sizeInt, 
    startingPos=characterPos, 
    maxAmmo=MAXAMMO,
    MAXDROPPEDAMMO=MAXDROPPEDAMMO,
    AMMO=AMMO,
    AMMOTAIL=AMMOTAIL,
    EMPTYFIELD=EMPTYFIELD, 
    CS_UP=CS_UP,
    CS_DOWN=CS_DOWN,
    CS_RIGHT=CS_RIGHT,
    CS_LEFT=CS_LEFT, 
    CS_GAMEOVER=CS_GAMEOVER,
    WALL=WALL,
    FPS=MAXFPS,
    BULLETUPWARDS=BULLETUPWARDS,
    BULLETSIDEWARDS=BULLETSIDEWARDS,
    ASTROID=ASTROID)

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