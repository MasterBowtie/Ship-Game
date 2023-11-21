import time

import pygame
import math
from ship import Ship

TURN_SPEED = 4
SPEED = 8
ACCELERATE = .5
DRIFT = .1


def main():
    # initialize pygame module
    pygame.init()
    pygame.key.set_repeat(0, 0)

    # screen = pygame.display.set_mode()
    screen = pygame.display.set_mode((720, 540))

    pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_NO)
    cursor = pygame.image.load("images/icon.png")
    pygame.mouse.set_visible(False)
    background = pygame.image.load("images/background.png")
    center = (screen.get_size()[0] / 2, screen.get_size()[1] / 2)
    center_vector = pygame.Vector2(0,0)
    ship = Ship(pygame.image.load("images/ship.png"), center)
    ship.addFrontGun(pygame.image.load("images/gun.png"))
    ship_drift = 0
    ship_turn_drift = 0
    move_right = False
    move_left = False
    move_forward = False
    move_backward = False


    running = True
    previous = time.time()
    while running:
        next = time.time()

        if next - previous < .05:
            continue
        else:
            previous = next

        screen.fill((0, 0, 185))


        for event in pygame.event.get(pygame.KEYDOWN):
            if event.dict["key"] == 27:
                running = False
            if event.dict["unicode"] == "a" or event.dict["unicode"] == "A":
                move_right = True
            if event.dict["unicode"] == "d" or event.dict["unicode"] == "D":
                move_left = True
            if event.dict["unicode"] == "w" or event.dict["unicode"] == "W":
                move_forward = True
            if event.dict["unicode"] == "s" or event.dict["unicode"] == "S":
                move_backward = True

        for event in pygame.event.get(pygame.KEYUP):
            if event.dict["unicode"] == "a" or event.dict["unicode"] == "A":
                move_right = False
            if event.dict["unicode"] == "d" or event.dict["unicode"] == "D":
                move_left = False
            if event.dict["unicode"] == "w" or event.dict["unicode"] == "W":
                move_forward = False
            if event.dict["unicode"] == "s" or event.dict["unicode"] == "S":
                move_backward = False

        if move_forward and ship_drift < SPEED:
            ship_drift += ACCELERATE
        if move_right and ship_turn_drift < TURN_SPEED:
            if ship_drift < TURN_SPEED:
                ship_drift += ACCELERATE
            ship_turn_drift += ACCELERATE
        if move_left and ship_turn_drift > - TURN_SPEED:
            if ship_drift < TURN_SPEED:
                ship_drift += ACCELERATE
            ship_turn_drift -= ACCELERATE
        if move_backward:
            ship_turn_drift -= ACCELERATE
            ship_drift -= ACCELERATE
            if ship_drift < 0:
                ship_drift = 0
            if ship_turn_drift < 0:
                ship_turn_drift = 0

        if ship_drift < 0:
            ship_drift += ACCELERATE
        if ship_drift > 0:
            ship_drift -= DRIFT
        if ship_turn_drift > 0:
            ship_turn_drift -= DRIFT
        if ship_turn_drift < 0:
            ship_turn_drift += DRIFT



        # if ship.hitBox()[0] < 0:
        #     print("Hit Left")
        #     ship_drift = -ship_drift
        #     if 90 < ship.getRotation() < 180:
        #         ship_turn_drift = -TURN_SPEED
        #     if 180 < ship.getRotation() < 270:
        #         ship_turn_drift = TURN_SPEED
        # if ship.hitBox()[1] > screen.get_size()[1]:
        #     print("Hit Bottom")
        #     ship_drift = -ship_drift
        #     if 180 < ship.getRotation() < 270:
        #         ship_turn_drift = -TURN_SPEED
        #     if 270 < ship.getRotation() < 360:
        #         ship_turn_drift = TURN_SPEED
        # if ship.hitBox()[2] > screen.get_size()[0]:
        #     print("Hit Right")
        #     ship_drift = -ship_drift
        #     if 270 < ship.getRotation() < 360:
        #         ship_turn_drift = -TURN_SPEED
        #     if 0 < ship.getRotation() < 90:
        #         ship_turn_drift = TURN_SPEED
        # if ship.hitBox()[3] < 0:
        #     print("Hit Top")
        #     ship_drift = -ship_drift
        #     if 0 < ship.getRotation() < 90:
        #         ship_turn_drift = -TURN_SPEED
        #     if 90 < ship.getRotation() < 180:
        #         ship_turn_drift = TURN_SPEED

        ship.turnShip(ship_turn_drift, ship_drift)
        ship.moveShip(ship_drift)
        ship.drawShip(screen)

        screen.blit(cursor, (pygame.mouse.get_pos()[0] - cursor.get_size()[0] / 2, pygame.mouse.get_pos()[1] - cursor.get_size()[1] / 2))

        pygame.display.update()
        for event in pygame.event.get(pygame.QUIT):
            if event.type == pygame.QUIT:
                running = False



if __name__ == "__main__":
    main()
