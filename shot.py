from vector import vector3

class shot:
    def __init__(self, shotType : str, direction : str, damage : float, position : vector3):
        self.shotType = shotType
        self.direction = direction
        self.damage = damage
        self.position = position
        self.moveCounter = 0