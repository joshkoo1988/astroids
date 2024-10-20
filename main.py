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

    ## group to handle obj that can be updated ##
    ## group to handle obj that can be drawn ##
    ## add a player to both groups ##
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updateable, drawable)
    
    ##create an infinate game loop for the game screen ##
    ## set fps at 60 ##
    running = True
    while running:
        screen.fill((0,0,0))
        dt = (clock.tick(60)/1000)

        ## prints player ##
        ## update players rotation ##
        for player in updateable:
            player.update(dt)
        drawable.draw(screen)
        

        ## update the display ##
        pygame.display.flip()

        ## close game if game window is closed ##
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


main()