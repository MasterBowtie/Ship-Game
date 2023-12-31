import time

import pygame
from src.missile import Missile
import math

IMAGE = "images/gun.png"
RELOAD = 3 #sec
class Gun:
    def __init__(self, position, rotation=0):
        self.__gun_image = pygame.image.load(IMAGE)
        self.__position = position
        self.__rotation = rotation
        self.__loaded = True
        self.__missile = Missile((position[0] + self.__gun_image.get_size()[0], position[1]), rotation)
        self.__reload_time = 0

    def drawGun(self, screen):

        self.__rotation = - pygame.Vector2(0,0).angle_to(
             pygame.math.Vector2(
                 pygame.mouse.get_pos()[0] - self.__position[0],
                 pygame.mouse.get_pos()[1] - self.__position[1]))

        temp = pygame.transform.rotate(self.__gun_image, self.__rotation)
        center = (temp.get_size()[0]/2, temp.get_size()[1]/2)
        screen.blit(temp, (self.__position[0] - center[0], self.__position[1] - center[1]))
        if self.__missile is not None:
            radius = self.__gun_image.get_size()[0]/2 - self.__missile.getSize()[0]/2
            x = math.cos(self.__rotation * (2 * math.pi / 360)) * radius + self.__position[0]
            y = - math.sin(self.__rotation * (2 * math.pi / 360)) * radius + self.__position[1]
            self.__missile.setPosition((x,y), self.__rotation)
            self.__missile.drawMissile(screen)
        elif time.time() - self.__reload_time > RELOAD:
            self.__loaded = True
            self.__missile = Missile((self.__position[0] + self.__gun_image.get_size()[0], self.__position[1]), self.__rotation)




    def setPosition(self, position):
        self.__position = position

    def getPosition(self):
        return self.__position

    def fireGun(self):
        temp = self.__missile
        if self.__loaded:
            self.__loaded = False
            self.__missile = None
            self.__reload_time = time.time()
        return temp