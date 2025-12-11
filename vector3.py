

class vector3:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def equals(self, vector):
        if self.x == vector.x and self.y == vector.y and self.z == vector.z:
            return True
        return False
    
    def add(self, vector):
        self.x += vector.x
        self.y += vector.y
        self.z += vector.z

    def sub(self, vector):
        self.x -= vector.x
        self.y -= vector.y
        self.z -= vector.z

    def __str__(self):
        return(f"vector3: x = {self.x}, y = {self.y}, z = {self.z}")
    