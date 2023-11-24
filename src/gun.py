import pygame
from src.missle import Missle
import math

IMAGE = "images/gun.png"
RELOAD = 3 #convert to time, current seconds
class Gun:
    def __init__(self, position, rotation=0):
        self.__gun_image = pygame.image.load(IMAGE)
        self.__position = position
        self.__rotation = rotation
        self.__loaded = True
        self.__missle = Missle((position[0] + self.__gun_image.get_size()[0], position[1]), rotation)

    def drawGun(self, screen):

        self.__rotation = - pygame.Vector2(0,0).angle_to(
             pygame.math.Vector2(
                 pygame.mouse.get_pos()[0] - self.__position[0],
                 pygame.mouse.get_pos()[1] - self.__position[1]))

        temp = pygame.transform.rotate(self.__gun_image, self.__rotation)
        center = (temp.get_size()[0]/2, temp.get_size()[1]/2)
        screen.blit(temp, (self.__position[0] - center[0], self.__position[1] - center[1]))
        if self.__missle is not None:
            radius = self.__gun_image.get_size()[0]/2 - self.__missle.getSize()[0]/2
            x = math.cos(self.__rotation * (2 * math.pi / 360)) * radius + self.__position[0]
            y = - math.sin(self.__rotation * (2 * math.pi / 360)) * radius + self.__position[1]
            self.__missle.setPosition((x,y), self.__rotation)
            self.__missle.drawMissle(screen)

    def setPosition(self, position):
        self.__position = position

    def getPosition(self):
        return self.__position

    def fireGun(self):
        if self.__loaded:
            self.__loaded = False
            temp = self.__missle
            self.__missle = None
            return temp