import pygame
from pygame import sprite

from settings import PROJECT_PATH

class Bullet(sprite.Sprite):
    def __init__(self, pos):
        sprite.Sprite.__init__(self)
        self.image = pygame.image.load(PROJECT_PATH +
                                       "/bullet/images/laser.png")
        self.rect = self.image.get_rect(topleft=pos)

    def update(self):
        if self.rect[1] > 0:
            self.rect = self.image.get_rect(topleft=(self.rect[0], self.rect[1] - 5))
        else:
            self.kill()
