import pygame

IMAGE = "images/missle.png"

class Missle:

    def __init__(self, pos, angle):
        self.__missle_image = pygame.image.load(IMAGE)
        self.__speed = 20
        self.__rotation = angle
        self.__position = (pos[0] - self.__missle_image.get_size()[0], pos[1])
        self.__target = (0,0)
        self.__fired = False

    def drawMissle(self, screen):
        if self.__fired:
            pass
        else:

            temp = pygame.transform.rotate(self.__missle_image, self.__rotation)
            center = (temp.get_size()[0] / 2, temp.get_size()[1] / 2)
            screen.blit(temp, (self.__position[0] - center[0], self.__position[1] - center[1]))

    def setPosition(self, pos, angle):
        self.__position = pos
        self.__rotation = angle

    def getPosition(self):
        return self.__position

    def getSize(self):
        return self.__missle_image.get_size()
