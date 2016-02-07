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

# ship = pygame.image.load("images/ship.png")
# ship_top = screen.get_height() - ship.get_height()
# ship_left = screen.get_width() / 2 - ship.get_width() / 2

screen.blit(ship.image, ship.position)

while True:
    clock.tick(60)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
