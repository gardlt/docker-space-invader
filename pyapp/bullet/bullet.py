import pygame
from settings import PROJECT_PATH
class Bullet():
    def __init__(self):
        self.image = pygame.image.load(PROJECT_PATH +
                                       "/bullet/images/laser.png")
        self.position = (0, 0)

    def setStartingPoint(self, shipPosition):
        self.position = shipPosition
