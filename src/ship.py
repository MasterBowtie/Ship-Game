import pygame
from src.gun import Gun
import math

IMAGE = "images/ship.png"
class Ship:
    def __init__(self, position, rotation=0):
        self.__ship_image = pygame.image.load(IMAGE)
        self.__position = position
        self.__rotation = rotation
        self.__gun_front = None
        self.__gun_back = None

    def drawShip(self, screen):
        temp = pygame.transform.rotate(self.__ship_image, self.__rotation)
        center = (temp.get_size()[0]/2, temp.get_size()[1]/2)
        screen.blit(temp, (self.__position[0] - center[0], self.__position[1] - center[1]))
        if self.__gun_front is not None and self.__gun_back is not None:
            self.__gun_front.drawGun(screen)
            self.__gun_back.drawGun(screen)

    ### This needs some serious research to know what the actual hit box is
    def hitBox(self):
        temp = pygame.transform.rotate(self.__ship_image, self.__rotation)
        center = (temp.get_size()[0] / 2, temp.get_size()[1] / 2)
        top = self.__position[0] - center[0]
        right = self.__position[1] + center[1]
        bottom = self.__position[0] + center[0]
        left = self.__position[1] - center[1]
        return (top, right, bottom, left)

    def getPos(self):
        return self.__position

    def getRotation(self):
        return self.__rotation

    def turnShip(self, angle, speed):
        self.__rotation += angle
        if self.__rotation < 0:
            self.__rotation += 360
        if self.__rotation > 360:
            self.__rotation -= 360

        if self.__gun_front is not None and self.__gun_back is not None:
            x = math.cos(self.__rotation * (2 * math.pi /360)) * self.__ship_image.get_size()[0]/3
            y = math.sin(self.__rotation * (2 * math.pi /360)) * self.__ship_image.get_size()[0]/3
            self.__gun_front.setPosition((self.__position[0] + x, self.__position[1] - y))
            self.__gun_back.setPosition((self.__position[0] - x, self.__position[1] + y))

        self.moveShip(speed)


    def moveShip(self, speed):
        x = math.cos(self.__rotation * (2 * math.pi / 360)) * speed
        y = - math.sin(self.__rotation * (2 * math.pi / 360)) * speed

        self.__position = (self.__position[0] + x, self.__position[1] + y)
        if self.__gun_front is not None and self.__gun_back is not None:
            self.__gun_front.setPosition((self.__gun_front.getPosition()[0] + x, self.__gun_front.getPosition()[1] + y))
            self.__gun_back.setPosition((self.__gun_back.getPosition()[0] + x, self.__gun_back.getPosition()[1] + y))

    def addFrontGun(self):
        self.__gun_front = Gun((self.__position[0] + (self.__ship_image.get_size()[0]/3),
                          self.__position[1]))
        self.__gun_back = Gun((self.__position[0] - (self.__ship_image.get_size()[0] / 3),
                                self.__position[1]))

    def fireFrontGun(self):
        return self.__gun_front.fireGun()

