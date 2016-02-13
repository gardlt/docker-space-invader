import pygame

class Enemy:
    def __init__(self):
        self.image = pygame.image.load("./images/Hydralisk.png")
        self.position = (0, 0)
        self.hit = False
        self.speed = 1
        self.points = 0

    def setStartingPoint(self, screen):
        x_axis = 0
        y_axis = 0
        self.position = (x_axis, y_axis)
