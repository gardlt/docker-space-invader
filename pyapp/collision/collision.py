
import pygame

class Collision:
    def __init__(self):
        pass

    def collision_check(self, enemies, ship, bullet):
        if not(bullet is None):
            self.bullet_hit_enemy(bullet, enemies)

    def bullet_hit_enemy(self, bullet, enemies):
        for enemy in range(len(enemies)):
            print enemies[enemy]
            #image_radios = self.area_of_object(enemies[enemy])
            #distance = self.distance_of_objects(bullet, enemies[enemy])
            #if (distance - image_radios):
                #print "kill"
            #if 0 > (distance - image_radios):
                # print enemy, enemies[enemy], len(enemies), distance
                #del enemies[enemy]
                #bullet = None

    def area_of_object(self, enemyObj):
        return (enemyObj.image.get_width() * enemyObj.image.get_height())

    def distance_of_objects(self, ship, bullet):
        return (((ship.image.get_width() - bullet.image.get_width())**2) +
                ((ship.image.get_height() - bullet.image.get_height())**2))**(0.5)
