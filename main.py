### Created and Imagined by Cody Apedaile
import pygame
from src import ship_move


def main():
    pygame.init()
    screen = pygame.display.set_mode((720, 540))
    running = True

    while(running):
        ship_move.main()


if __name__ == "__main__":
    main()