import pygame
from settings import PROJECT_PATH, ENEMY_DEFAULT_SIZE
from enemy.enemy import Enemy

class Hydralisk(Enemy):
    def __init__(self):
        self.image = pygame.transform.scale(pygame.image.load(PROJECT_PATH +
                                            "/hydralisk/images/enemy2_1.png")
                                            , ENEMY_DEFAULT_SIZE)
        self.hit = False
        self.speed = 1
        self.points = 2
        self.position = (0, 0)

    def setStartingPoint(self, newPosition):
        self.position = newPosition

    def update(self):
        pass
