from vector import vector3
from shot import shot
import string
import threading
import math
import random

class board:
    def __init__(self, 
                 size : int, 
                 startingPos : vector3, 
                 maxAmmo : int, 
                 MAXDROPPEDAMMO : int, 
                 EMPTYFIELD : str, 
                 CS_UP : str, 
                 CS_DOWN : str, 
                 CS_RIGHT : str, 
                 CS_LEFT : str, 
                 CS_GAMEOVER: str,
                 WALL : str, 
                 BULLETUPWARDS : str,
                 BULLETSIDEWARDS : str, 
                 ASTROID : str,
                 AMMO : str, 
                 AMMOTAIL : str,
                 FPS : int):
        board = ["."]*size
        walls = ["."]*size
        for i in range(size):
            board[i] = [EMPTYFIELD]*size
            walls[i] = ["."]*size
        self.walls = walls
        self.field = board
        self.EMPTYFIELD = EMPTYFIELD
        self.CS_UP = CS_UP
        self.CS_DOWN = CS_DOWN
        self.CS_RIGHT = CS_RIGHT
        self.CS_LEFT = CS_LEFT
        self.WALL = WALL
        self.BULLETUPWARDS = BULLETUPWARDS
        self.BULLETSIDEWARDS = BULLETSIDEWARDS
        self.ASTROID = ASTROID
        self.AMMO = AMMO
        self.AMMOTAIL = AMMOTAIL
        self.MAXDROPPEDAMMO = MAXDROPPEDAMMO
        self.characterPos = startingPos
        self.size = size
        self.shots = []
        self.astroids = []
        self.facing = "up"
        self.frameCounter = 0
        self.FPS = FPS
        self.lastFacing = "up"
        self.maxAmmo = maxAmmo
        self.currentAmmo = []
        self.droppedAmmo = []
        self.tail = []
        self.points = 0
        self.isGameOver = False
        self.points = 0
        self.timeCount = 0
        self.CS_GAMEOVER = CS_GAMEOVER


    def printBoard(self):
        if self.isGameOver == False:
            self.updateBoard()
            print("\n"*100)
            print("  " + "––" * self.size)
            for i in range(len(self.field)):
                line = "| "
                for x in range(len(self.field[len(self.field) - i - 1])):
                    line += (self.field[len(self.field) - i - 1][x])
                line += "|"
                print(line)
            print("  " + "––" * self.size)
            print(("*:" + "█" * len(self.currentAmmo) + "░" * (self.maxAmmo - len(self.currentAmmo)) + f" Score: {self.points}"))

        else:
            print("\n"*100)
            print("\tGame Over!")
            print(f"\tScore: {self.points}")
            print(f"\tTime: {self.timeCount}s")
            print("  " + "––" * self.size)
            for i in range(len(self.field)):
                line = "| "
                for x in range(len(self.field[len(self.field) - i - 1])):
                    line += (self.field[len(self.field) - i - 1][x])
                line += "|"
                print(line)
            print("  " + "––" * self.size)
            print("")
            

    def updateBoard(self):
        self.frameCounter += 1
        for a in self.astroids:
            for s in self.shots:
                if s != a and s.position == a.position:
                    self.astroids.remove(a)
                    self.shots.remove(s)
                    self.points += 1000
            if a.position == self.characterPos:
                self.gameOver()

        board = ["."]*self.size
        for i in range(self.size):
            board[i] = [self.EMPTYFIELD]*self.size

        for a in self.droppedAmmo:
            board[a.position.x][a.position.y] = self.AMMO

        for a in self.tail:
            board[a.position.x][a.position.y] = self.AMMOTAIL

        for x in range(len(board)):
            for y in range(len(board[x])):
                if self.walls[x][y] == self.WALL:
                    board[x][y] = self.WALL

        for s in self.shots:
            if s.shotType == "bullet":
                if s.direction == "up" or s.direction == "down":
                    board[s.position.x][s.position.y] = self.BULLETUPWARDS
                else:
                    board[s.position.x][s.position.y] = self.BULLETSIDEWARDS
        
        for s in self.astroids:
            board[s.position.x][s.position.y] = self.ASTROID

        board[self.characterPos.x][self.characterPos.y] = self.getCharacterSymbol()
        self.field = board

        for a in self.droppedAmmo:
            if a.position == self.characterPos and self.maxAmmo > len(self.currentAmmo):
                self.droppedAmmo.remove(a)
                self.currentAmmo.append(a)

        if self.frameCounter % self.FPS == 0:
            self.timeCount += 1
            self.points += 100
        if self.frameCounter % 3 == 0:
            self.moveShots()
        if self.frameCounter % 6 == 0:
            self.moveForward()
        if self.frameCounter % 60 == 0:
            if len(self.currentAmmo) < self.maxAmmo:
                self.placeAmmo()
        if self.frameCounter % (round(120*self.FPS/self.frameCounter) + 2 * self.FPS) == 0:
            self.spawnAstroid()
    def addWall(self, pos : vector3):
        self.walls[pos.x][pos.y] = self.WALL

    def executeRotation(self, command : string): 
        newFacing = self.facing
        if command == "up":
            newFacing = "up"
        if command == "down":
            newFacing = "down"
        if command == "right":
            newFacing = "right"
        if command == "left":
            newFacing = "left"

        if self.lastFacing == self.rotateFacing(self.rotateFacing(newFacing, "right"), "right"):
            return
        
        self.facing = newFacing

    def executeShot(self):

        if len(self.currentAmmo) <= 0:
            return

        position = self.characterPos + self.forwardVector(self.facing)
 
        s = self.currentAmmo[len(self.currentAmmo)-1]
        self.currentAmmo.remove(s)

        try:
            self.tail.remove(s)
        except:
            i = 1

        if (position.x < 0 or position.y < 0 or
            position.x >= self.size or position.y >= self.size):
            return
        
        if self.walls[position.x][position.y] == self.WALL:
            return
        
        for s in self.shots:
            if s.position == position and s.shotType == "bullet":
                return
        
        s.position = position
        s.direction = self.facing
        self.shots.append(s)

    def moveShots(self):
        for s in self.shots + self.astroids:
            newPos = s.position.copy()
            s.moveCounter += 1

            newFacing = ""
            if s.direction == "up":
                newPos = newPos + vector3(1,0,0)
                newFacing = "up"
            if s.direction == "down":
                newPos = newPos + vector3(-1,0,0)
                newFacing = "down"
            if s.direction == "right":
                newPos = newPos + vector3(0,1,0)
                newFacing = "right"
            if s.direction == "left":
                newPos = newPos + vector3(0,-1,0)
                newFacing = "left"
            
            if s.shotType == "bullet":
                if s.moveCounter >= 1:
                    s.moveCounter = 0
                else:
                    continue

                if (newPos.x < 0 or newPos.y < 0 or
                    newPos.x >= self.size or newPos.y >= self.size):
                    self.shots.remove(s)
                    continue

                if self.walls[newPos.x][newPos.y] == self.WALL:
                    self.shots.remove(s)
                    continue
            if s.shotType == "astroid":
                if s.moveCounter >= 10:
                    s.moveCounter = 0
                else:
                    continue
                if (newPos.x < 0 or newPos.y < 0 or
                    newPos.x >= self.size or newPos.y >= self.size):
                    self.astroids.remove(s)
                    continue

                if self.walls[newPos.x][newPos.y] == self.WALL:
                    self.astroids.remove(s)
                    continue
            
            s.position = newPos
            s.direction = newFacing

    def moveForward(self):
        newPos = self.characterPos.copy()
        newPos += self.forwardVector(self.facing)

        if (newPos.x < 0 or newPos.y < 0 or
            newPos.x >= self.size or newPos.y >= self.size):
            return
        
        if self.walls[newPos.x][newPos.y] == self.WALL:
            return

        
        currentTail = self.tail
        if (len(currentTail) < len(self.currentAmmo)):
            newLink = self.currentAmmo[len(self.currentAmmo) - 1]
            if len(currentTail) == 0:
                newLink.position = self.characterPos
            else:
                newLink.position = currentTail[len(currentTail) - 1].position
            currentTail.append(newLink)
            
        for s in reversed(currentTail):
            if currentTail.index(s) != 0:
                s.position = currentTail[currentTail.index(s) - 1].position
            else:
                s.position = self.characterPos

        self.lastFacing = self.facing
        self.characterPos = newPos

    def getCharacterSymbol(self):
        if self.isGameOver:
            return self.CS_GAMEOVER
        if self.facing == "up":
            return self.CS_UP
        if self.facing == "down":
            return self.CS_DOWN
        if self.facing == "right":
            return self.CS_RIGHT
        if self.facing == "left":
            return self.CS_LEFT

    def rotateFacing(self, current : str, direction : str):
        if current == "up":
            if direction == "left":
                return "left"
            if direction == "right":
                return "right"
            
        if current == "down":
            if direction == "left":
                return "right"
            if direction == "right":
                return "left"
            
        if current == "right":
            if direction == "left":
                return "up"
            if direction == "right":
                return "down"
            
        if current == "left":
            if direction == "left":
                return "down"
            if direction == "right":
                return "up"
            
    def forwardVector(self, facing: str):
        if facing == "up":
            return vector3(1,0,0)
        if facing == "down":
            return vector3(-1,0,0)
        if facing == "right":
            return vector3(0,1,0)
        if facing == "left":
            return vector3(0,-1,0)

    def placeAmmo(self):
        if len(self.droppedAmmo) >= self.MAXDROPPEDAMMO:
            return
        
        randomPos = vector3(random.randint(0, self.size - 1), random.randint(0, self.size - 1), 0)
        if self.walls[randomPos.x][randomPos.y] == self.WALL:
            return
        
        ammo = shot("bullet", "up", 1, randomPos)
        self.droppedAmmo.append(ammo)

    def spawnAstroid(self):
        randPos = vector3(random.randint(0, self.size - 1), random.randint(0, self.size - 1), 0)
        randDir = ""
        direction = ""
        if random.randint(0, 1) == 0:
            randPos = vector3(randPos.x, random.choice([0, len(self.field) - 1]), randPos.z)
            if randPos.y == 0:
                direction = "right"
            else:
                direction = "left"
        else:
            randPos = vector3(random.choice([0, len(self.field[randPos.y]) - 1]), randPos.y, randPos.z)
            if randPos.x == 0:
                direction = "up"
            else:
                direction = "down"

        newShot = shot("astroid", direction, 1, randPos)
        self.astroids.append(newShot)

    def gameOver(self):
        self.isGameOver = True
        