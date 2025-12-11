

class vector3:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def equals(self, vector):
        if self.x == vector.x and self.y == vector.y and self.z == vector.z:
            return True
        return False
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z
    
    def __add__(self, other):
        return vector3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return vector3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, value):
        return vector3(self.x * value, self.y * value, self.z * value)
    def copy(self):
        return vector3(self.x, self.y, self.z)

    def __str__(self):
        return(f"vector3: x = {self.x}, y = {self.y}, z = {self.z}")
    