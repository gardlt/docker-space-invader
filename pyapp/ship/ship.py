import pygame

from settings import PROJECT_PATH

class Ship:
    def __init__(self):
        self.image = pygame.image.load(PROJECT_PATH + "/ship/images/ship.png")
        self.position = (0, 0)

    def setStartingPoint(self, screen):
        x_axis = screen.get_width() / 2 - self.image.get_width() / 2
        y_axis = screen.get_height() - self.image.get_height()
        self.position = (x_axis, y_axis)
