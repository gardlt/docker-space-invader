import pygame
from pygame import sprite

from settings import PROJECT_PATH, ENEMY_DEFAULT_SIZE, BRUTALISK_POINTS

class Brutalisk(sprite.Sprite):
    def __init__(self, x_pos, y_pos):
        sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(PROJECT_PATH +
                                            "/brutalisk/images/enemy1_1.png")
                                            , ENEMY_DEFAULT_SIZE)

        self.rect = self.image.get_rect(topleft=(x_pos, y_pos))
        self.points = BRUTALISK_POINTS

    def update(self):
        pass
