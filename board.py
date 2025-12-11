from vector3 import vector3
from shot import shot
import string
import threading

class board:
    def __init__(self, size : int, startingPos : vector3, EMPTYFIELD : str, CHARACTERSYMBOL : str, WALL : str, BULLET : str, FPS : int):
        board = ["."]*size
        walls = ["."]*size
        for i in range(size):
            board[i] = [EMPTYFIELD]*size
            walls[i] = ["."]*size
        self.walls = walls
        self.field = board
        self.EMPTYFIELD = EMPTYFIELD
        self.CHARACTERSYMBOL = CHARACTERSYMBOL
        self.WALL = WALL
        self.BULLET = BULLET
        self.characterPos = startingPos
        self.size = size
        self.shots = []
        self.facing = "up"
        self.frameCounter = 0
        self.FPS = FPS

    def printBoard(self):
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

    def updateBoard(self):
        self.frameCounter += 1
        board = ["."]*self.size
        for i in range(self.size):
            board[i] = [self.EMPTYFIELD]*self.size

        for x in range(len(board)):
            for y in range(len(board[x])):
                if self.walls[x][y] == self.WALL:
                    board[x][y] = self.WALL

        for s in self.shots:
            board[s.position.x][s.position.y] = self.BULLET

        board[self.characterPos.x][self.characterPos.y] = self.CHARACTERSYMBOL
        self.field = board
        if self.frameCounter % round(self.FPS/ 2) == 0:
            self.moveShots()

    def addWall(self, pos : vector3):
        self.walls[pos.x][pos.y] = self.WALL

    def executeMovement(self, command : string): 
        newPos = self.characterPos.copy()
        newFacing = ""
        if command == "up":
            newPos.add(vector3(1,0,0))
            newFacing = "up"
        if command == "down":
            newPos.add(vector3(-1,0,0))
            newFacing = "down"
        if command == "right":
            newPos.add(vector3(0,1,0))
            newFacing = "right"
        if command == "left":
            newPos.add(vector3(0,-1,0))
            newFacing = "left"

        if (newPos.x < 0 or newPos.y < 0 or
            newPos.x >= self.size or newPos.y >= self.size):
            return
        
        if self.walls[newPos.x][newPos.y] == self.WALL:
            return
        
        self.characterPos = newPos
        self.facing = newFacing

    def executeShot(self):
        newShot = shot("bullet", self.facing, 1, self.characterPos)
        self.shots.append(newShot)
        return
    
    def moveShots(self):
        for s in self.shots:
            newPos = s.position.copy()
            newFacing = ""
            if s.direction == "up":
                newPos.add(vector3(1,0,0))
                newFacing = "up"
            if s.direction == "down":
                newPos.add(vector3(-1,0,0))
                newFacing = "down"
            if s.direction == "right":
                newPos.add(vector3(0,1,0))
                newFacing = "right"
            if s.direction == "left":
                newPos.add(vector3(0,-1,0))
                newFacing = "left"
            
            if (newPos.x < 0 or newPos.y < 0 or
                newPos.x >= self.size or newPos.y >= self.size):
                self.shots.remove(s)
                continue

            if self.walls[newPos.x][newPos.y] == self.WALL:
                self.shots.remove(s)
                return
            
            s.position = newPos
            s.direction = newFacing

