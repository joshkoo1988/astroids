import pygame
from constants import *

def main ():
    ## initalize pygame ##
    ## create a screen with constants using pygame.display ##
    pygame.init
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    ## set FPS refresh rate ##
    clock = pygame.time.Clock()
    dt = 0


    ##create an infinate game loop for the game screen ##
    ## set fps at 60 ##
    black_color = (0,0,0)
    running = True
    while running:
        screen.fill(black_color)
        pygame.display.flip()
        dt = (clock.tick(60)/1000)

        ## close game if game window is closed ##
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


main()