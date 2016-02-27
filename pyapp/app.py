#!/usr/bin/env python
import pygame
import sys
# from pygame.locals import *
from pygame import sprite
from settings import BLACK_COLOR, DISPLAY_SIZE, WHITE_COLOR
from ship.ship import Ship
from bullet.bullet import Bullet
from zergling.zergling import Zergling
from brutalisk.brutalisk import Brutalisk
from hydralisk.hydralisk import Hydralisk
from player.player import Player
from collision.collision import Collision

clock = pygame.time.Clock()
screen = pygame.display.set_mode(DISPLAY_SIZE)

pygame.mouse.set_visible(0)

# Create Player
player = Player()
collision = Collision()
# Create Ship
ship = Ship()
ship.setStartingPoint(screen)

# Init Bullet
bullet = None

# Create Enemies
zerglings = sprite.Group()

# Font Creations
pygame.init()
font = pygame.font.Font(None, 36)

for row in range(5):
    for column in range(10):
        tempZerg = None
        if(row is 0):
            tempZerg = Brutalisk()
        elif(row is 1 or row is 2):
            tempZerg = Hydralisk()
        else:
            tempZerg = Zergling()

        tempZerg.setStartingPoint((25 + (column * 50), 50 + (row * 50)))
        zerglings.add(tempZerg)

while True:
    clock.tick(60)
    screen.fill(BLACK_COLOR)

    # Menu Options
    score = font.render("Score: " + str(player.score), 1, WHITE_COLOR)
    lives = font.render("Lives: " + str(player.lives), 1, WHITE_COLOR)
    screen.blit(score, score.get_rect())
    screen.blit(lives, (screen.get_width() / 2, 0))

    # Enemies movement
    zerglings.draw(screen)
    # for zerg in zerglings:
    #     screen.blit(zerg.image, zerg.position)

    # Ship movement
    screen.blit(ship.image, ((ship.position[0] - ship.image.get_width() / 2),
                             ship.position[1]))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and bullet is None:
                bullet = Bullet()
                bullet.setStartingPoint(ship.position)
            if event.key == pygame.K_LEFT:
                ship.position = (ship.position[0] - 5, ship.position[1])
            if event.key == pygame.K_RIGHT:
                ship.position = (ship.position[0] + 5, ship.position[1])

    if not(bullet is None):
        if bullet.position[1] > 0:
            screen.blit(bullet.image, bullet.position)
            bullet.position = (bullet.position[0], bullet.position[1] - 5)
        else:
            bullet = None

    pygame.display.update()

    # update Enemies
    collision.collision_check(zerglings, ship, bullet)
    # enemiesdict = sprite.groupcollide(bullet, zerglings, True, False)
    # print enemiesdict
