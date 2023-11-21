import pygame

class Gun:
    def __init__(self, gun, position, rotation=0):
        self.__gun_image = gun
        self.__position = position
        self.__rotation = rotation

    def drawGun(self, screen):

        self.__rotation = - pygame.Vector2(0,0).angle_to(
             pygame.math.Vector2(
                 pygame.mouse.get_pos()[0] - self.__position[0],
                 pygame.mouse.get_pos()[1] - self.__position[1]))

        temp = pygame.transform.rotate(self.__gun_image, self.__rotation)
        center = (temp.get_size()[0]/2, temp.get_size()[1]/2)
        screen.blit(temp, (self.__position[0] - center[0], self.__position[1] - center[1]))

    def rotateGun(self, angle):
        self.__rotation = angle

    def setPosition(self, position):
        self.__position = position

    def getPosition(self):
        return self.__position