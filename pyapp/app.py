#!/usr/bin/env python
import pygame
import sys
from ship.ship import Ship

DISPLAY_SIZE = (800, 600)

clock = pygame.time.Clock()
screen = pygame.display.set_mode(DISPLAY_SIZE)

pygame.mouse.set_visible(0)

ship = Ship()
ship.setStartingPoint(screen)

screen.blit(ship.image, ship.position)

while True:
    clock.tick(60)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
