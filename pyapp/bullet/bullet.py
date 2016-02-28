import pygame
from pygame import sprite

from settings import PROJECT_PATH

class Bullet(sprite.Sprite):
    def __init__(self, pos):
        sprite.Sprite.__init__(self)
        self.image = pygame.image.load(PROJECT_PATH +
                                       "/bullet/images/laser.png")
        self.rect = pygame.Rect(pos[0], pos[1], 32, 32)
        self.out_of_bounds = False

    def update(self):
        if self.rect[1] > 0:
            self.rect = (self.rect[0], self.rect[1] - 5)
        else:
            self.kill()
