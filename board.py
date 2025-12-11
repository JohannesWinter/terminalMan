from vector3 import vector3
import string

class board:
    def __init__(self, size : int, startingPos : vector3, EMPTYFIELD : str, CHARACTERSYMBOL : str):
        board = ["."]*size
        for i in range(size):
            board[i] = [EMPTYFIELD]*size
        self.field = board
        self.EMPTYFIELD = EMPTYFIELD
        self.CHARACTERSYMBOL = CHARACTERSYMBOL
        self.characterPos = startingPos
        self.size = size

    def printBoard(self):
        self.updateBoard()
        for i in range(len(self.field)):
            line = ""
            for x in range(len(self.field[len(self.field) - i - 1])):
                line += (self.field[len(self.field) - i - 1][x])
            print(line)

    def updateBoard(self):
        board = ["."]*self.size
        for i in range(self.size):
            board[i] = [self.EMPTYFIELD]*self.size
        board[self.characterPos.x][self.characterPos.y] = self.CHARACTERSYMBOL
        self.field = board

    def executeCmd(self, command : string): 
        if command == "up":
            self.characterPos.add(vector3(1,0,0))
        if command == "down":
            self.characterPos.add(vector3(-1,0,0))
        if command == "right":
            self.characterPos.add(vector3(0,1,0))
        if command == "left":
            self.characterPos.add(vector3(0,-1,0))
        print(self.characterPos)
