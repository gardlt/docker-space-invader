import pygame

class Zergling():
    def __init__(self):
        self.image = pygame.image.load("./images/zergling.png")
        self.position = (0, 0)

    def setStartingPoint(self, screen):
        x_axis = 0
        y_axis = 0
        self.position = (x_axis, y_axis)
