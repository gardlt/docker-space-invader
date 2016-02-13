#!/usr/bin/env python
import pygame
import sys
from pygame.locals import MOUSEBUTTONDOWN
from ship.ship import Ship
from bullet.bullet import Bullet
from zergling.zergling import Zergling

DISPLAY_SIZE = (800, 600)
BLACK_COLOR = (0, 0, 0)

clock = pygame.time.Clock()
screen = pygame.display.set_mode(DISPLAY_SIZE)

pygame.mouse.set_visible(0)

# Ship
ship = Ship()
ship.setStartingPoint(screen)
screen.blit(ship.image, ship.position)

# Bullet
bullet = None

# Enemies

zerglings = []

for x in range(2):
    tempZerg = Zergling()
    tempZerg.position = (5 + x * 102, 5 + x * 102)
    zerglings.append(tempZerg)

print zerglings

while True:
    clock.tick(60)
    screen.fill(BLACK_COLOR)

    # Enemies movement
    for zerg in zerglings:
        screen.blit(zerg.image, zerg.position)

    # Ship movement
    screen.blit(ship.image, ((ship.position[0] - ship.image.get_width() / 2),
                             ship.position[1]))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN and bullet is None:
            bullet = Bullet()
            bullet.setStartingPoint(ship.position)

    if not(bullet is None):
        if bullet.position[1] > 0:
            screen.blit(bullet.image, bullet.position)
            bullet.position = (bullet.position[0], bullet.position[1] - 5)
        else:
            bullet = None

    pygame.display.update()
