import pygame
from settings import PROJECT_PATH
from enemy.enemy import Enemy

class Zergling(Enemy):
    def __init__(self):
        self.image = pygame.image.load(PROJECT_PATH +
                                       "/zergling/images/enemy3_1.png")
        self.position = (5, 5)
        self.hit = False
        self.speed = 1
        self.points = 50

    def setStartingPoint(self, screen):
        self.position = (5, 5)

    def update(self):
        pass
