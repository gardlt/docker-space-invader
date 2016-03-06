import pygame
from pygame import sprite

from bullet.bullet import Bullet
from settings import PROJECT_PATH

class Ship(sprite.Sprite):
    def __init__(self, screen):
        sprite.Sprite.__init__(self)
        self.image = pygame.image.load(PROJECT_PATH + "/ship/images/ship.png")
        self.rect = (screen.get_width() / 2 - self.image.get_width() / 2,
                     screen.get_height() - self.image.get_height())

    def update(self, event, bullet):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and len(bullet.sprites()) < 1:
                bullet.add(Bullet(self.rect))
            if event.key == pygame.K_LEFT:
                self.rect = (self.rect[0] - 5, self.rect[1])
            if event.key == pygame.K_RIGHT:
                self.rect = (self.rect[0] + 5, self.rect[1])
