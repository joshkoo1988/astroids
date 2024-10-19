import pygame
from constants import *
from player import *

def main ():
    ## initalize pygame ##
    ## create a screen with constants using pygame.display ##
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    ## set FPS refresh rate & create player obj ##
    clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)


    ##create an infinate game loop for the game screen ##
    ## set fps at 60 ##
    running = True
    while running:
        screen.fill((0,0,0))
        dt = (clock.tick(60)/1000)

        ## prints player ##
        ## update players rotation ##
        player.draw(screen)
        player.update(dt)


        ## update the display ##
        pygame.display.flip()

        ## close game if game window is closed ##
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


main()