import time
import pygame
from src.ship import Ship
import src.pause_menu as pm

TURN_SPEED = 4
SPEED = 8
ACCELERATE = .5
DRIFT = .1



def main(filePrefix=""):
    screen = pygame.display.get_surface()
    cursor = pygame.image.load(filePrefix + "images/icon.png")
    pygame.mouse.set_visible(False)
    background = pygame.image.load(filePrefix + "images/background.png")
    center = (screen.get_size()[0] / 2, screen.get_size()[1] / 2)
    ship = Ship(center)
    ship.addFrontGun()

    # Variable Values and Flags
    ship_drift = 0
    ship_turn_drift = 0
    move_right = False
    move_left = False
    move_forward = False
    move_backward = False
    missiles = []

    running = True
    previous = time.time()
    while running:
        next = time.time()

        if next - previous < .05:
            continue
        else:
            previous = next

        screen.blit(background, (0,0))

        for event in pygame.event.get(pygame.KEYDOWN):
            if event.dict["key"] == 27:
                pm.menu(screen, pygame.mouse.get_pos())
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

        for event in pygame.event.get(pygame.MOUSEBUTTONDOWN):
            if event.dict["button"] == 1:
                missile = ship.fireFrontGun()
                if missile is not None:
                    missile.fire()
                    missiles.append(missile)
                missile = ship.fireBackGun()
                if missile is not None:
                    missile.fire()
                    missiles.append(missile)

        temp = []
        for missile in missiles:
            hit = missile.drawMissile(screen)
            if not hit:
                temp.append(missile)
        missiles = temp

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
            ship_drift -= DRIFT
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

        ### Firing the Gun


        ### This section is to limit the ship from leaving the screen
            #Change this to exit Combat

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
                exit()

if __name__ == "__main__":
    pygame.init()
    pygame.display.set_mode((720, 540))
    filePrefix = "../"
    main(filePrefix)
