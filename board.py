from vector3 import vector3
import string
import threading
import shot

class board:
    def __init__(self, size : int, startingPos : vector3, EMPTYFIELD : str, CHARACTERSYMBOL : str, WALL : str):
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
        self.characterPos = startingPos
        self.size = size

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
        board = ["."]*self.size
        for i in range(self.size):
            board[i] = [self.EMPTYFIELD]*self.size

        for x in range(len(board)):
            for y in range(len(board[x])):
                if self.walls[x][y] == self.WALL:
                    board[x][y] = self.WALL 

        board[self.characterPos.x][self.characterPos.y] = self.CHARACTERSYMBOL
        self.field = board

    def addWall(self, pos : vector3):
        self.walls[pos.x][pos.y] = self.WALL

    def executeMovement(self, command : string): 
        newPos = self.characterPos.copy()
        if command == "up":
            newPos.add(vector3(1,0,0))
        if command == "down":
            newPos.add(vector3(-1,0,0))
        if command == "right":
            newPos.add(vector3(0,1,0))
        if command == "left":
            newPos.add(vector3(0,-1,0))

        if (newPos.x < 0 or newPos.y < 0 or
            newPos.x >= self.size or newPos.y >= self.size):
            return
        
        if self.walls[newPos.x][newPos.y] == self.WALL:
            return
        
        self.characterPos = newPos

    def executeShot(self):
        return
