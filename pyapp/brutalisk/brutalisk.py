import pygame
from pygame import sprite

from settings import PROJECT_PATH, ENEMY_DEFAULT_SIZE

class Brutalisk(sprite.Sprite):
    def __init__(self, x_pos, y_pos):
        sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(PROJECT_PATH +
                                            "/brutalisk/images/enemy1_1.png")
                                            , ENEMY_DEFAULT_SIZE)
        # position of the image
        self.rect = self.image.get_rect(topleft=(x_pos, y_pos))

    def update(self):
        pass
