import pygame
from settings import PROJECT_PATH
from pygame import sprite

class Bullet(sprite.Sprite):
    def __init__(self):
        self.image = pygame.image.load(PROJECT_PATH +
                                       "/bullet/images/laser.png")
        self.position = (0, 0)
        self.rect = self.image.get_rect()

    def setStartingPoint(self, shipPosition):
        self.position = shipPosition
