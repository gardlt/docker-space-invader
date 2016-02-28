import pygame
from settings import PROJECT_PATH, ENEMY_DEFAULT_SIZE
from pygame import sprite

class Zergling(sprite.Sprite):
    def __init__(self, x_pos, y_pos):
        sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(PROJECT_PATH +
                                            "/zergling/images/enemy3_1.png")
                                            , ENEMY_DEFAULT_SIZE)
        self.rect = self.image.get_rect(topleft=(x_pos, y_pos))

    def update(self):
        pass
