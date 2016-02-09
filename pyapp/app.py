#!/usr/bin/env python
import pygame
import sys
from settings import PROJECT_PATH
from pygame.locals import MOUSEBUTTONDOWN
from ship.ship import Ship

DISPLAY_SIZE = (800, 600)
BLACK_COLOR = (0, 0, 0)

clock = pygame.time.Clock()
screen = pygame.display.set_mode(DISPLAY_SIZE)

pygame.mouse.set_visible(0)

ship = Ship()
ship.setStartingPoint(screen)

screen.blit(ship.image, ship.position)
bullet = pygame.image.load(PROJECT_PATH + "/images/laser.png")
shoot_y = 0

while True:
    clock.tick(60)
    screen.fill(BLACK_COLOR)
    x, y = pygame.mouse.get_pos()
    screen.blit(ship.image, (x - ship.image.get_width() / 2, ship.position[1]))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif (event.type == MOUSEBUTTONDOWN):
            shoot_y = ship.position[1]
            shoot_x = x

    if shoot_y > 0:
        screen.blit(bullet, (shoot_x, shoot_y))
        shoot_y = shoot_y - 5

    pygame.display.update()
