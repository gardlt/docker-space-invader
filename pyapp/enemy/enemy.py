
class Enemy:
    def __init__(self):
        self.image = None
        self.position = (0, 0)
        self.hit = False
        self.speed = 1
        self.points = 0

    def setStartingPoint(self, screen):
        self.position = (5, 5)
