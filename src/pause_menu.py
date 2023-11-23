import pygame

def menu(screen, mouse_pos):
    pygame.mouse.set_visible(True)
    menu_base = pygame.image.load("images/menu_base.png")
    menu_button = pygame.image.load("images/menu_button.png")
    menu_pos = (screen.get_size()[0]/2 - menu_base.get_size()[0]/2, screen.get_size()[1]/2 - menu_base.get_size()[1]/2)
    contiue_pos = (screen.get_size()[0]/2 - menu_button.get_size()[0]/2, menu_pos[1]* 4/2)
    exit_pos = (screen.get_size()[0]/2 - menu_button.get_size()[0]/2, menu_pos[1]* 6/2)
    running = True
    while running:
        for event in pygame.event.get(pygame.KEYDOWN):
            if event.dict["key"] == 27:
                running = False

        screen.blit(menu_base, menu_pos)
        screen.blit(menu_button, exit_pos)


        for event in pygame.event.get(pygame.MOUSEBUTTONDOWN):
            left = exit_pos[0]
            top = exit_pos[1]
            right = left + menu_button.get_size()[0]
            bottom = top + menu_button.get_size()[1]
            pos = event.dict["pos"]
            if left < pos[0] < right and top < pos[1] < bottom:
                exit()



        pygame.display.update()
        for event in pygame.event.get(pygame.QUIT):
            if event.type == pygame.QUIT:
                exit()

    pygame.mouse.set_pos(mouse_pos)
    pygame.mouse.set_visible(False)
