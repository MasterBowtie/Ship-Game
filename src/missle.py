import pygame

IMAGE = "images/missle.png"

class Missle:

    def __init__(self, source, target, angle):
        self.__missle_image = pygame.image.load(IMAGE)
        self.__speed = 20
        self.__angle = 0
        self.__pos = (0,0)
        self.__target = (0,0)

    def drawMissle(self):
        pass