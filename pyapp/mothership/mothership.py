import pygame
from settings import PROJECT_PATH, ENEMY_DEFAULT_SIZE
from pygame import sprite

class Mothership(sprite.Sprite):
    def __init__(self):
        sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(PROJECT_PATH +
                                            "/mothership/images/mystery.png")
                                            , ENEMY_DEFAULT_SIZE)
        self.hit = False
        self.speed = 1
        self.points = 2
        self.position = (0, 0)
        self.rect = self.image.get_rect()

    def setStartingPoint(self, newPosition):
        self.positon = newPosition

    def update(self):
        pass
