#!/usr/bin/env python
import pygame
import sys
# from pygame.locals import *
from pygame import sprite
from settings import BLACK_COLOR, DISPLAY_SIZE, WHITE_COLOR
from ship.ship import Ship
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
ship = sprite.Group()
ship.add(Ship(screen))

# Init Bullet
bullet = sprite.Group()

# Create Enemies
zerglings = sprite.Group()

# Font Creations
pygame.init()
font = pygame.font.Font(None, 36)

# Enemy Populate
for row in range(5):
    for column in range(10):
        tempZerg = None
        if(row is 0):
            tempZerg = Brutalisk((25 + (column * 50)), (50 + (row * 50)))
        elif(row is 1 or row is 2):
            tempZerg = Hydralisk((25 + (column * 50)), (50 + (row * 50)))
        else:
            tempZerg = Zergling((25 + (column * 50)), (50 + (row * 50)))

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
    ship.draw(screen)
    bullet.draw(screen)
    # for zerg in zerglings:
    #     screen.blit(zerg.image, zerg.position)

    # Ship movement
    #screen.blit(ship.image, ((ship.position[0] - ship.image.get_width() / 2),
    #                         ship.position[1]))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        ship.update(event, bullet)

    bullet.update()
    pygame.display.update()
    sprite.groupcollide(bullet, zerglings, True, True)
    # update Enemies
    # collision.collision_check(zerglings, ship, bullet)
    # enemiesdict = sprite.groupcollide(bullet, zerglings, True, False)
    # print enemiesdict
