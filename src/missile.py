import math
import pygame

IMAGE = "images/missle.png"

class Missile:

    def __init__(self, pos, angle):
        self.__missle_image = pygame.image.load(IMAGE)
        self.__speed = 15
        self.__rotation = angle
        self.__position = (pos[0] - self.__missle_image.get_size()[0], pos[1])
        self.__target = (0,0)
        self.__source = (0,0)
        self.__range = 300
        self.__fired = False

    def drawMissile(self, screen):
        if self.__fired:
            x = math.cos(self.__rotation * (2 * math.pi / 360)) * self.__speed
            y = - math.sin(self.__rotation * (2 * math.pi / 360)) * self.__speed
            self.__position = (self.__position[0] + x, self.__position[1] + y)
        dist = ((self.__position[0] - self.__source[0]) ** 2 + (self.__position[1] - self.__source[1]) ** 2) ** (1 / 2)
        dist2 = ((self.__position[0] - self.__target[0]) ** 2 + (self.__position[1] - self.__target[1]) ** 2) ** (1 / 2)

        temp = pygame.transform.rotate(self.__missle_image, self.__rotation)
        center = (temp.get_size()[0] / 2, temp.get_size()[1] / 2)
        screen.blit(temp, (self.__position[0] - center[0], self.__position[1] - center[1]))

        if self.__fired and dist >= self.__range or dist2 < 7:
            return True
        return False

    def setPosition(self, pos, angle):
        self.__position = pos
        self.__rotation = angle

    def getPosition(self):
        return self.__position

    def getSize(self):
        return self.__missle_image.get_size()

    def fire(self):
        self.__fired = True
        self.__target = pygame.mouse.get_pos()
        self.__source = self.__position

    def toString(self):
        return [self.__position, self.__rotation, self.__fired]